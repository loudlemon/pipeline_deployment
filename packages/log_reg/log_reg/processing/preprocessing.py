import numpy as np
import pandas as pd
from log_reg.config import config
from sklearn.base import BaseEstimator, TransformerMixin


class DropUnnecessaryFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables_to_drop=None):
        if not isinstance(variables_to_drop, list):
            self.variables = [variables_to_drop]
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X.drop(self.variables, axis=1, errors='ignore')

        return X
