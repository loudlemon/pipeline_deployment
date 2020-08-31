from log_reg.config import config as model_config
from log_reg.processing.data_management import load_data
from log_reg import __version__ as _version
from api import __version__ as api_version

import json
import numpy as np

def test_health_endpoint_returns_200(flask_test_client):
    response = flask_test_client.get('/health')

    assert response.status_code == 200


def test_version_endpoint(flask_test_client):
    response = flask_test_client.get('/version')

    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version

def test_prediction_endpoint(flask_test_client):

    test_data = load_data(file_name=model_config.TEST_DATA)
    post_json = test_data.to_json(orient='records')
    response = flask_test_client.post('/v1/predict/log_reg',
                                    json=json.loads(post_json))

    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    assert isinstance(prediction[0][1], float)
    assert response_version == _version
