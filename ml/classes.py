# flake8: noqa
from sklearn import base
import numpy as np
import pandas as pd

class CityEstimator(base.BaseEstimator, base.RegressorMixin):
    def __init__(self):
        # initialization code
        return None

    def fit(self, X, xcol, ycol):
        # fit the model ...
        assert isinstance(X, pd.DataFrame)
        assert isinstance(xcol, basestring)
        assert isinstance(ycol, basestring)
        self.fit = X.groupby(xcol)[ycol].mean().to_dict()
        self.grand_mean = np.mean(X[ycol])
        return self

    def predict(self, city):
        if city in self.fit:
            return self.fit[city]
        else:
            return self.grand_mean

class Transformer(base.BaseEstimator, base.TransformerMixin):
    def __init__(self):
        # initialization code
        return self

    def fit(self, X, y=None):
        # fit the transformation
        # ...
        return self

    def transform(self, X):
        return self # transformation
