from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentResponse

from app.crud.department import create_department, get_departments, get_department_by_id, update_department, delete_department

router = APIRouter()

@router.post("/", response_model=DepartmentResponse)
def create_department_route(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return create_department(db, department)


@router.get("/", response_model=list[DepartmentResponse])
def get_departments_route(
    db: Session = Depends(get_db)
):
    return get_departments(db)


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department_by_id_route(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = get_department_by_id(
        db,
        department_id
    )

    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )

    return department


@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department_route(
    department_id: int,
    updated_department: DepartmentUpdate,
    db: Session = Depends(get_db)
):
    department = update_department(
        db,
        department_id,
        updated_department
    )

    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )

    return department


@router.delete("/{department_id}")
def delete_department_route(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = delete_department(
        db,
        department_id
    )

    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )

    return {
        "message": "Department deleted successfully"
    }