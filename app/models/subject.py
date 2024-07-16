from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    lesson = relationship("Lesson", back_populates="subjects")
    category = relationship("Category", back_populates="subjects")

    questions = relationship("Question", back_populates="subject")