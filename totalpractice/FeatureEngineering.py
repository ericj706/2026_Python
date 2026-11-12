import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class BikeFeatureEngineer(TransformerMixin, BaseEstimator):
    """입력값에서 파생 피처를 생성. 학습과 서버 예측에서 함께 사용."""

    def fit(self, X, y=None):
        self.feature_names_in_ = np.asarray(X.columns, dtype=object)
        self.n_features_in_ = len(X.columns)
        return self

    def transform(self, X):
        result = X.copy()
        result["Temperature_squared"] = result["Temperature"] ** 2
        result["Is_weekend"] = (result["DayOfWeek"] >= 5).astype(int)
        result["Is_raining"] = (result["Rainfall(mm)"] > 0).astype(int)
        result["Is_snowing"] = (result["Snowfall (cm)"] > 0).astype(int)
        return result
