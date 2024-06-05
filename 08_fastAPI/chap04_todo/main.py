from fastapi import FastAPI
import models
from database import engine


app = FastAPI()

@app.get("/")
def home():
    return {"hi": "hi"}

#sqlalchemy 라이브러리 기능을 이용해 데이터 베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)