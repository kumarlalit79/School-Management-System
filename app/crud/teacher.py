from sqlalchemy.orm import Session
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherResponse, TeacherUpdate
import bcrypt


def create_teacher(
    db: Session,
    teacher: TeacherCreate
):
    hashed_password = bcrypt.hashpw(
        teacher.password.encode("utf-8")
    ).decode("utf-8")
    
    new_teacher = Teacher(
        name = teacher.name,
        email = teacher.email,
        hashed_password = hashed_password
    )
    
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    
    return new_teacher


def get_teacher(db: Session):
    return db.query(Teacher).all()

def get_teacher_by_id(
    db: Session,
    teacher_id: int
):
    teacher =  db.query(Teacher).filter(Teacher.id == teacher_id).first()
    return teacher

def update_teacher(
    db: Session,
    teacher_id: int,
    updated_teacher: TeacherUpdate
):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if not teacher:
        return None
    
    teacher.name = updated_teacher.name
    teacher.email = updated_teacher.email
    
    db.commit()
    db.refresh(teacher)

    return teacher


def delete_teacher(
    db: Session,
    teacher_id: int
):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if not teacher:
        return None
    
    db.delete(teacher)
    
    db.commit()

    return teacher