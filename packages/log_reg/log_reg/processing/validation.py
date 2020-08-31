from log_reg.config import config
import pandas as pd


def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Check model inputs for unprocessable values
    """
    val_data = input_data.copy()

    # check for features with NA before training
    if input_data[config.FEATURES].isnull().any().any():
        val_data.dropna(inplace=True)
    # check for values <= 0 before applying logscale
    if (input_data[config.TO_LOGSCALE] <= 0).any().any():
        to_include = input_data[config.TO_LOGSCALE].columns[
            (input_data[config.TO_LOGSCALE] > 0).any()]
        val_data = input_data[to_include]

    return val_data
