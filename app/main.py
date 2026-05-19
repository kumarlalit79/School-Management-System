from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import Student
from app.routes.student import router as student_router
from app.routes.teacher import router as teacher_router
from app.routes.department import router as department_router

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
    # This must be department_router. Using teacher_router here made Swagger show
    # Teacher request/response schemas under the /departments endpoints.
    department_router,
    prefix="/departments",
    tags=["Departments"]   
)

@app.get("/")
def home():
    return {"message" : "API working"}
