import numpy as np
import pandas as pd
import joblib
import logging
from log_reg.config import config
from log_reg import pipeline
from log_reg.processing.data_management import load_data, \
    resample_classes, \
    save_pipeline
from log_reg import __version__ as _version

_logger = logging.getLogger(__name__)


def run_training():

    data = load_data(file_name='train_data.csv')
    X, y = resample_classes(data)
    pipeline.CHD_pipe.fit(X, y)
    _logger.info(f'saving model version: {_version}')
    save_pipeline(pipeline_to_save=pipeline.CHD_pipe)

if __name__ == '__main__':
    run_training()
