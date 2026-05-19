from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate

def create_department(
    db: Session,
    department: DepartmentCreate
):
    new_department = Department(
        name = department.name,
        building = department.building       
    )
    
    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department


def get_departments(db: Session):
    return db.query(Department).all()


def get_department_by_id(
    db: Session,
    id: int
):
    department = db.query(Department).filter(Department.id == id).first()

    return department


def update_department(
    db: Session,
    id: int,
    department_update: DepartmentUpdate
):
    department = db.query(Department).filter(Department.id == id).first()
    
    if not department:
        return None
    
    department.name = department_update.name
    department.building = department_update.building
    
    db.commit()
    db.refresh(department)

    # Route expects the updated department back for response_model serialization.
    return department
    

def delete_department(
    db : Session,
    id : int
):
    # The second argument should be an id value. Naming it "int" was shadowing
    # Python's built-in int type and the query below was accidentally using id.
    department = db.query(Department).filter(Department.id == id).first()
    
    if not department:
        return None
    
    db.delete(department)
    db.commit()

    return department
