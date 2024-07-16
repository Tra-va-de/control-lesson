from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.session import Base


class Discipline(Base):
    
    __tablename__ = "disciplines"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    lessons = relationship("Lesson", back_populates="discipline")
