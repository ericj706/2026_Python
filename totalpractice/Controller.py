from fastapi import APIRouter
router = APIRouter(prefix="/bike")

from Service import serv

# 대여량 예측
@router.post("/predict")
def predict(item: dict):
    return serv.predict(item)
