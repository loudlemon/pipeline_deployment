import pandas as pd
import joblib
import logging
import typing as t
from sklearn.pipeline import Pipeline
from imblearn.combine import SMOTEENN
from log_reg.config import config
from log_reg import __version__ as _version
from log_reg.processing.validation import validate_inputs


_logger = logging.getLogger(__name__)


def load_data(*, file_name: str) -> pd.DataFrame:
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')

    return _data


def resample_classes(dataframe) -> tuple:
    data = validate_inputs(dataframe)
    X = data[config.FEATURES]
    y = data[config.TARGET]
    X_resampled, y_resampled = SMOTEENN(
                            random_state=config.SEED).\
                            fit_resample(X, y)
    return X_resampled, y_resampled


def save_pipeline(*, pipeline_to_save) -> None:

    name_file = f"{config.PIPE_SAVE}{_version}.pkl"
    path_to_save = config.TRAINED_MODEL_DIR / name_file
    remove_old_pipe(files_to_keep=[name_file])
    joblib.dump(pipeline_to_save, path_to_save)
    _logger.info(f'saved pipeline: {name_file}')



def load_pipeline(*, pipe_name: str) -> Pipeline:

    file_path = config.TRAINED_MODEL_DIR / pipe_name
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline


def remove_old_pipe(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old pipelines
    """
    do_not_delete = files_to_keep + ['__init__.py']
    for file in config.TRAINED_MODEL_DIR.iterdir():
        if file.name not in do_not_delete:
            file.unlink()
