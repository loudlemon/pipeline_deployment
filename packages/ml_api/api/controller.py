from flask import Blueprint, request, jsonify, render_template
from api.config import get_logger
from api import __version__ as api_version
from api.validation import validate_inputs
from log_reg.predict import make_prediction
from log_reg import __version__ as _version



_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})

@prediction_app.route('/v1/predict/log_reg', methods=['POST'])
def predict():
    if request.method == 'POST':
        #Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')
        #Validate input using marshmallow schema
        input_data, errors =  validate_inputs(input_data=json_data)

        #Model prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        predictions = result.get('predictions').tolist()
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})
    
@prediction_app.route('/')
def home():
    return render_template('home.html')
    
@prediction_app.route('/prediction', methods=['POST'])
def prediction():
     if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        _logger.debug(f'Inputs: {data}')
        input_data, errors =  validate_inputs(input_data=data)
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')
        predictions = result.get('predictions').tolist()
        return render_template('home.html',
                               pred='Вероятность ишемической болезни сердца {}%'\
                               .format(round(predictions[0][1]*100)))



