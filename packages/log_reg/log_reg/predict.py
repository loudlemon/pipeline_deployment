import pandas as pd
import logging
import json
import typing as t
from log_reg.processing.data_management import load_pipeline
from log_reg.config import config
from log_reg.processing.validation import validate_inputs
from log_reg import __version__ as _version

_logger = logging.getLogger(__name__)

pipe_name = f"{config.PIPE_SAVE}{_version}.pkl"
_chd_pipe = load_pipeline(pipe_name=pipe_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict],
                    ) -> dict:
    """
    Make prediction using saved model pipeline.
    Args:
        input_data: Array pf model predictions inputs.
    Returns:
        predictions for each iput row, as well as the model version
    """
    data = pd.DataFrame(input_data)
    validated_data = validate_inputs(input_data=data)
    prediction = _chd_pipe.predict_proba(validated_data[config.FEATURES])
    response = {'predictions': prediction, 'version': _version}

    _logger.info(
        f'Making prediction with model version: {_version}'
        f'inputs: {validated_data}'
        f'predictions: {response}'
    )

    return response
