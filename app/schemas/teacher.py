from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    

class TeacherUpdate(BaseModel):
    name: str
    email: str
    
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    
    class Config:
        from_attribute = True