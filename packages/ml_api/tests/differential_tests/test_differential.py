import math
import pytest
import pandas as pd
from api import config
from log_reg import config as model_config
from log_reg.predict import make_prediction
from log_reg.processing.data_management import load_data


@pytest.mark.differential
def test_model_prediction_differential(
                                *,
                                saved_file: str = 'test_predictions.csv'):
    """
    This test compares the prediction resilt similarity
    of the current model with the previous model's results
    """
    # Given
    previous_model_df = pd.read_csv(f'{config.PACKAGE_ROOT}/{saved_file}')
    previous_model_preds = previous_model_df.predictions.values
    test_data = load_data(file_name=model_config.TEST_DATA)

    # When
    current = make_prediction(input_data=test_data)
    current_model_preds = current.get('predictions')[:, 1]

    #Then
    # diff the current model vs previous model
    assert len(previous_model_preds) == len(
        current_model_preds)

    # Perform the differential test
    for previous_value, current_value in zip(
            previous_model_preds, current_model_preds):
        # convert numpy float64 to Python float
        previous_value = previous_value.item()
        current_value = current_value.item()

        # rel_tol is the relative tolerance - it is the maximum allowed
        # difference between a and b
        assert math.isclose(previous_value,
                            current_value,
                            rel_tol=config.ACCEPTABLE_MODEL_DIFFERENCE)
