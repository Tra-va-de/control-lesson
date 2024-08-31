from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class LearningAttitudeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class LearningAttitudeCreate(LearningAttitudeBase):
    pass


class LearningAttitudeUpdate(LearningAttitudeBase):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    

class LearningAttitude(LearningAttitudeBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)
