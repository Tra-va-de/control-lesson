from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    subjects = relationship("Subject", back_populates="category")