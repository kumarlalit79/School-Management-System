from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import Student
from app.routes.student import router as student_router
from app.routes.teacher import router as teacher_router
from app.routes.department import router as department_router
from app.routes.auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    student_router,
    prefix="/students",
    tags=["Students"]
)

app.include_router(
    teacher_router,
    prefix="/teacher",
    tags=["Teachers"]
)

app.include_router(
    department_router,
    prefix="/departments",
    tags=["Departments"]   
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

@app.get("/")
def home():
    return {"message" : "API working"}
