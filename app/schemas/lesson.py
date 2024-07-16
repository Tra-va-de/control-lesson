from pydantic import BaseModel, Field, ConfigDict


class LessonBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    discipline_id: int = Field(..., gt=0)
    lesson_level_id: int = Field(..., gt=0)


class LessonCreate(LessonBase):
    pass


class LessonUpdate(LessonBase):
    pass


class LessonInDBBase(LessonBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)


class Lesson(LessonInDBBase):
    pass


class LessonInDB(LessonInDBBase):
    pass
