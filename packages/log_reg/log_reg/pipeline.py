from log_reg.processing import preprocessing as pp
from log_reg.processing import features
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from log_reg.config import config


CHD_pipe = Pipeline(
    [
        ('drop_unnecessary',
            pp.DropUnnecessaryFeatures(
                variables_to_drop=config.FEATURES_TO_DROP)),

        ('log_transformer',
            features.LogTransformer(variables=config.TO_LOGSCALE)),

        ('scaler', StandardScaler()),
        ('Logistic_regression', LogisticRegression(**config.LR_PARAMS))
    ]
)
