from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class StudentLearningAttitudeBase(BaseModel):
    student_id: int = Field(..., gt=0)
    learning_attitude_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)


class StudentLearningAttitudeCreate(StudentLearningAttitudeBase):
    pass


class StudentLearningAttitudeUpdate(StudentLearningAttitudeBase):
    rating: Optional[int] = Field(None, ge=1, le=5)
    

class StudentLearningAttitudeInDBBase(StudentLearningAttitudeBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)


class StudentLearningAttitude(StudentLearningAttitudeInDBBase):
    pass


class StudentLearningAttitudeInDB(StudentLearningAttitudeInDBBase):
    pass