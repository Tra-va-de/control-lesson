from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Lesson(Base):
    
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    discipline_id = Column(Integer, ForeignKey("disciplines.id"), nullable=False)
    lesson_level_id = Column(Integer, ForeignKey("lesson_levels.id"), nullable=False)

    discipline = relationship("Discipline", back_populates="lessons")
    lesson_level = relationship("LessonLevel", back_populates="lessons")

    subjects = relationship("Subject", back_populates="lesson")