import json
from log_reg.config import config
from log_reg.processing.data_management import load_data



def test_prediction_endpoint_val_200(flask_test_client):

    test_data = load_data(file_name=config.TEST_DATA)
    post_json = test_data.to_json(orient='records')

    response = flask_test_client.post('/v1/predict/log_reg',
                                    json=json.loads(post_json))

    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json.get('errors') is None
    assert len(response_json.get('predictions')) == 1
