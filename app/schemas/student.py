from pydantic import BaseModel, EmailStr
from app.schemas.department import DepartmentBasic

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    department_id: int
    
    
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    department: DepartmentBasic
    
    class Config:
        from_attributes = True
        
        
class StudentUpdate(BaseModel):
    name: str
    email: EmailStr