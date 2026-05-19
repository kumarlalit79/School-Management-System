from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    
    email = Column(String, unique=True, nullable=False)
    
    hashed_password = Column(String, nullable=False)

    role = Column(String, default="student")
    
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="students")