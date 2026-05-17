from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import Student

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message" : "API working"}

