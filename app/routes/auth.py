from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.models.student import Student
from app.core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.email == login_data.email).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    is_password_correct = verify_password(
        login_data.password, student.hashed_password
    )
    
    if not is_password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    access_token = create_access_token({
        "sub" : student.email,
        "role" : student.role,
        "user_id" : student.id
    })
    
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }