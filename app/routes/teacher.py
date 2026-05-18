from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.teacher import TeacherCreate, TeacherResponse, TeacherUpdate
from app.db.dependencies import get_db
from app.crud.teacher import create_teacher, get_teacher, get_teacher_by_id, delete_teacher

router = APIRouter()

@router.post("/", response_model=TeacherResponse)
def create_teacher_route(
    teacher: TeacherCreate,
    db: Session = Depends(get_db)
):
    return create_teacher(db, teacher)

@router.get("/", response_model=list[TeacherResponse])
def get_all_teacher_route(
    db: Session = Depends(get_db)
):
    return get_teacher(db)

@router.get("/{teacher_id}", response_model=TeacherResponse)
def get_teacher_by_id_route(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    
    teacher = get_teacher_by_id(db, teacher_id)
    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )

    return teacher


@router.put("/{teacher_id}", response_model=TeacherResponse)
def update_teacher_route(
    teacher_id: int,
    updated_teacher: TeacherUpdate,
    db: Session = Depends(get_db)
):
    teacher = TeacherUpdate(
        db,
        teacher_id,
        updated_teacher
    )

    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )

    return teacher


@router.delete("/{teacher_id}")
def delete_teacher_route(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    teacher = delete_teacher(
        db,
        teacher_id
    )

    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )

    return {
        "message": "Teacher deleted successfully"
    }