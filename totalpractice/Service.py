from datetime import date
import math

import joblib
import pandas as pd
from fastapi import HTTPException


class BikeService:
    def __init__(self):
        # 서버에서 모듈을 불러올 때 한 번만 로드
        saved = joblib.load("./totalpractice/models/best_model.pkl")
        self.model = saved["model"]
        self.metrics = saved["metrics"]
        self.prediction_unit = saved.get("prediction_unit")

    def predict(self, item: dict):
        if self.prediction_unit != "day":
            raise HTTPException(status_code=503, detail="일별 모델이 필요합니다. predict.py를 실행하고 서버를 재시작하세요.")
        try:
            selected_date = date.fromisoformat(item["date"])
            weather_keys = [
                "temperature", "humidity", "wind_speed", "visibility",
                "dew_point", "solar_radiation", "rainfall", "snowfall",
            ]
            weather = {key: float(item[key]) for key in weather_keys}
            if not all(math.isfinite(value) for value in weather.values()):
                raise ValueError("날씨 값은 유한한 숫자여야 합니다.")
            if not 0 <= weather["humidity"] <= 100:
                raise ValueError("습도는 0~100이어야 합니다.")
            for key in weather_keys[2:4] + weather_keys[5:]:
                if weather[key] < 0:
                    raise ValueError(f"{key}는 0 이상이어야 합니다.")
            
        except (KeyError, TypeError, ValueError, OverflowError) as error:
            raise HTTPException(
                status_code=422, detail=f"입력값을 확인하세요: {error}"
            ) from error

        # 계절 계산
        month = selected_date.month
        if month in (3, 4, 5):
            season = "Spring"
        elif month in (6, 7, 8):
            season = "Summer"
        elif month in (9, 10, 11):
            season = "Autumn"
        else:
            season = "Winter"

        # 학습에 사용한 CSV 컬럼 이름으로 변환
        input_df = pd.DataFrame([{
            "Temperature": weather["temperature"],
            "Humidity(%)": weather["humidity"],
            "Wind speed (m/s)": weather["wind_speed"],
            "Visibility (10m)": weather["visibility"],
            "Dew point temperature": weather["dew_point"],
            "Solar Radiation (MJ/m2)": weather["solar_radiation"],
            "Rainfall(mm)": weather["rainfall"],
            "Snowfall (cm)": weather["snowfall"],
            "Seasons": season,
            "Month": month,
            "DayOfWeek": selected_date.weekday()
        }])
        input_df = input_df.loc[:, self.model.feature_names_in_]

        # 저장된 Pipeline이 전처리와 예측을 함께 수행
        prediction = float(self.model.predict(input_df)[0])
        return {
            "prediction": prediction,
            "r2": float(self.metrics["r2"]),
            "mae": float(self.metrics["mae"]),
        }

serv = BikeService()
