from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate , StudentResponse , StudentUpdate
from app.db.dependencies import get_db
from app.crud.student import create_student, get_students, get_student_by_id, update_student, student_delete
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=StudentResponse)
def create_student_route(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student)
    
    

@router.get("/me")
def get_logged_in_student(
    current_user = Depends(get_current_user)
):
    return {
        "message" : "Protected route accessed",
        "user" : current_user
    }
    
    
@router.get("/", response_model=list[StudentResponse])
def get_students_route(
    db: Session = Depends(get_db)
):
    return get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id_route(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = get_student_by_id(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student
    
    
@router.put("/{student_id}", response_model=StudentResponse)
def update_student_route(
    student_id: int,
    updated_student: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = update_student(
        db,
        student_id,
        updated_student
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student

@router.delete("/{student_id}")
def delete_student_route(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_delete(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }
    

