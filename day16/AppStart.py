# 파이썬 파일 분리
# AppStart.py : FastAPI 실행 파일
# Controller.py : HTTP REST 파일
# Service.py : 로직 파일

# 1. 서버실행
from fastapi import FastAPI
import uvicorn

import Controller
app = FastAPI()
app.include_router(Controller.router)

@app.get("/")
async def home(): 
  return 'FAST API SERVER RUNNING...'

if __name__ == "__main__":
  # 서버 실행 설정
  uvicorn.run("AppStart:app", host="127.0.0.1", port=8000, reload=True)