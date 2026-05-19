from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    name: str
    building: str
    
class DepartmentUpdate(BaseModel):
    name: str
    building: str

class DepartmentResponse(BaseModel):
    id: int
    name: str
    building: str
    
    class Config:
        from_attributes = True
    
class DepartmentBasic(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True