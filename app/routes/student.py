from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate
from app.models.student import Student
from app.db.dependencies import get_db
import bcrypt

router = APIRouter()

@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    hashed_password = bcrypt.hashpw(
        student.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")
    
    new_student = Student(
        name=student.name,
        email=student.email,
        hashed_password=hashed_password
    )
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return {
        "message" : "Student created successfully"
    }
    