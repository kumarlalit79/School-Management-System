from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.database import Base

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, unique=True)

    building = Column(String, nullable=False)

    students = relationship("Student", back_populates="department")

    teachers = relationship("Teacher", back_populates="department")
