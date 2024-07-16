from pydantic import BaseModel, Field, ConfigDict


class SubjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    lesson_id: int = Field(..., gt=0)
    category_id: int = Field(..., gt=0)


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectBase):
    pass


class SubjectInDBBase(SubjectBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)


class Subject(SubjectInDBBase):
    pass


class SubjectInDB(SubjectInDBBase):
    pass