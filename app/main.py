from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import Student
from app.routes.student import router as student_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    student_router,
    prefix="/students",
    tags=["Students"]
)

@app.get("/")
def home():
    return {"message" : "API working"}