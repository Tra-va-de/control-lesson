from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.session import Base


class StudentLearningAttitude(Base):
    
    __tablename__ = "student_learning_attitudes"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    learning_attitude_id = Column(Integer, ForeignKey("learning_attitudes.id"), nullable=False)
    rating = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="student_learning_attitudes")
    learning_attitude = relationship("LearningAttitude", back_populates="student_learning_attitudes")