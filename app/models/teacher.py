from sqlalchemy import Column, String, Integer, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    role = Column(String , default="teacher")
    
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="teachers")