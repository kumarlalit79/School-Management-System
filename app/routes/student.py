from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate , StudentResponse , StudentUpdate
from app.models.student import Student
from app.db.dependencies import get_db
import bcrypt

router = APIRouter()

@router.post("/", response_model=StudentResponse)
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
    
    return new_student

    
@router.get("/", response_model=list[StudentResponse])
def get_students(
    db: Session = Depends(get_db)
):
    students = db.query(Student).all()
    
    return students


@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()
  
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    
    return student
    
    
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    update_student: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student not found"
        )
    
    student.name = update_student.name
    student.email = update_student.email
    
    db.commit()
    db.refresh(student)

    return student

@router.delete("/{student_id}")
def student_delete(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student not found"
        )
    
    db.delete(student)
    db.commit()
    return {
        "message": "Student deleted successfully"
    }