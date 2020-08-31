import pathlib
import pandas as pd
import log_reg

PACKAGE_ROOT = pathlib.Path(log_reg.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_model'
DATASET_DIR = PACKAGE_ROOT / 'datasets'


# data
TRAIN_DATA = 'train_data.csv'
TEST_DATA = 'test_data.csv'
TARGET = 'tenyearchd'
PATH = None
SEED = 5
TEST_SIZE = 0.2
RESAMPLE = True
DROPNA = True
PIPENAME = 'LogisticRegression'
PIPE_SAVE = f'{PIPENAME}_v_'
ACCEPTABLE_MODEL_DIFFERENCE = 0.05

# all input features
FEATURES = [
    'male', 'age', 'currentsmoker', 'cigsperday', 'education',
    'bpmeds', 'prevalentstroke', 'prevalenthyp', 'diabetes', 'totchol',
    'sysbp', 'diabp', 'bmi', 'heartrate', 'glucose'
]

# for now, keep only these features
FEATURES_TO_KEEP = [
    'male', 'age', 'currentsmoker', 'cigsperday', 'prevalenthyp',
    'diabetes', 'sysbp', 'diabp', 'heartrate', 'bmi'
]

# features of no use
FEATURES_TO_DROP = [
    'education', 'prevalentstroke', 'totchol', 'glucose', 'bpmeds'
]

# non-binary features to scale in the future
TO_LOGSCALE = ['age', 'bmi', 'heartrate', 'sysbp', 'diabp']

# LogisticRegression learning parameters
LR_PARAMS = {
    'C': 1,
    'solver': 'lbfgs',
    'class_weight': 'balanced',
    'random_state': SEED,
    'max_iter': 10000
}
