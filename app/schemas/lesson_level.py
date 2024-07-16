from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class LessonLevelBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class LessonLevelCreate(LessonLevelBase):
    pass


class LessonLevelUpdate(LessonLevelBase):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    

class LessonLevel(LessonLevelBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)
