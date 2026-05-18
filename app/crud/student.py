from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate , StudentResponse , StudentUpdate
from app.models.student import Student
from app.db.dependencies import get_db
import bcrypt

def create_student(
    db: Session,
    student: StudentCreate
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


def get_students(
    db: Session
):
    students = db.query(Student).all()
    
    return students


def get_student_by_id(
    db: Session,
    student_id: int
):
    return db.query(Student).filter(
        Student.id == student_id
    ).first()


def update_student(
    db: Session,
    student_id: int,
    updated_student: StudentUpdate,
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return None

    student.name = updated_student.name
    student.email = updated_student.email

    db.commit()

    db.refresh(student)

    return student


def student_delete(
    db: Session,
    student_id: int
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return None

    db.delete(student)

    db.commit()

    return student