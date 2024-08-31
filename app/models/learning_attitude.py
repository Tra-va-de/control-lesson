from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.session import Base


class LearningAttitude(Base):
    
    __tablename__ = "learning_attitudes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    student_learning_attitudes = relationship("StudentLearningAttitude", back_populates="learning_attitude")
