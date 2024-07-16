from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.session import Base


class LessonLevel(Base):
    
    __tablename__ = "lesson_levels"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    lessons = relationship("Lesson", back_populates="lesson_level")
