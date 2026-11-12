import pandas as pd
df = pd.read_csv("./SeoulBikeData.csv", )
df.info()

print("결측치:\n", df.isnull().sum())       # 결측치 0개
print("중복 행:", df.duplicated().sum())    # 중복 행 0개

df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
# 24시간 모두 정상 운영한 날짜만 집계
complete_days = df.groupby("Date").filter(
    lambda g: len(g) == 24 and g["Hour"].nunique() == 24
    and g["Functioning Day"].eq("Yes").all()
)
df = complete_days.groupby("Date", as_index=False).agg({
    "Rented Bike Count": "sum",
    "Temperature": "mean", "Humidity(%)": "mean",
    "Wind speed (m/s)": "mean", "Visibility (10m)": "mean",
    "Dew point temperature": "mean",
    "Solar Radiation (MJ/m2)": "sum", "Rainfall(mm)": "sum",
    "Snowfall (cm)": "max", "Seasons": "first",
}).sort_values("Date").reset_index(drop=True)
df = df.rename(columns={"Rented Bike Count": "Daily Bike Count"})
print("일별 학습 데이터 수:", len(df))

df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.dayofweek

# 습도, 이슬점 온도, 일사량을 포함한 전체 날씨 입력 사용
X = df.drop(columns=[
    "Daily Bike Count", "Date",
])
Y = df["Daily Bike Count"]

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit, train_test_split
from FeatureEngineering import BikeFeatureEngineer

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,  shuffle=False)
# 숫자이지만 범주로 처리할 컬럼 포함
categorical_columns = [
    "DayOfWeek",
    "Month",
    "Seasons",
    "Is_weekend",
    "Is_raining",
    "Is_snowing",
]
# 나머지 수치형컬럼으로 처리
numeric_columns = [
    column
    for column in X.columns
    if column not in categorical_columns
]
# Pipeline의 첫 단계에서 만들어질 수치형 피처
numeric_columns.append("Temperature_squared")
preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric", StandardScaler(), numeric_columns
        ),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ]
)
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
# 학습
pipeline = Pipeline([
    ("features", BikeFeatureEngineer()),
    ("preprocessor", preprocessor),
    ("model", Ridge())
])
param_grid = {
    "model__alpha": [0.01, 0.1, 1, 10, 100],
}
grid = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring="r2",
    cv=TimeSeriesSplit(n_splits=5),
    n_jobs=-1
)
grid.fit(X_train,Y_train)
best_model = grid.best_estimator_
print('최적 파라미터: ',grid.best_params_)
print('교차 검증 R²: ',grid.best_score_)

# 최적모델로 평가
print('Train R² : ', best_model.score(X_train,Y_train)) # 훈련
print('Test R² : ', best_model.score(X_test,Y_test))   # 테스트

Y_pred = best_model.predict(X_test)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
metrics = {
    "r2": float(r2_score(Y_test, Y_pred)),
    "mae": float(mean_absolute_error(Y_test, Y_pred)),          # mae : 실제값과 예측값이 평균적으로 몇 대 차이 나는지
    "rmse": float(mean_squared_error(Y_test, Y_pred) ** 0.5),   # mse : 큰 예측 오차에 더 큰 벌점을 주는 지표
}
print("최종 검증 성능:", metrics)

# 모델 저장
import joblib
joblib.dump(
        {"metrics": metrics, "model": best_model, "prediction_unit": "day"} , './totalpractice/models/best_model.pkl'
)

