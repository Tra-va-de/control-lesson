from pydantic import BaseModel, Field, ConfigDict


class QuestionBase(BaseModel):
    text: str = Field(..., min_length=1, max_length=100)
    answer: str = Field(..., min_length=1, max_length=100)
    subject_id: int = Field(..., gt=0)


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass


class QuestionInDBBase(QuestionBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)


class Question(QuestionInDBBase):
    pass


class QuestionInDB(QuestionInDBBase):
    pass