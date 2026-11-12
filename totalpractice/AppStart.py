from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

import Controller
app = FastAPI()
app.include_router(Controller.router)

STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")

if __name__ == "__main__":
  # 서버 실행 설정
  uvicorn.run("AppStart:app", host="127.0.0.1", port=8000, reload=True)
