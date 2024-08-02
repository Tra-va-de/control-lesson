from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class StudentAnswerBase(BaseModel):
    student_id: int = Field(..., example=1)
    question_id: int = Field(..., example=1)
    answer: float = Field(..., ge=0, le=1, example=0.75)  # Используем Field для задания ограничений



class StudentAnswerCreate(StudentAnswerBase):
    pass


class StudentAnswerUpdate(StudentAnswerBase):
    student_id: Optional[int] = None
    question_id: Optional[int] = None
    answer: Optional[float] = Field(None, ge=0, le=1)  # Задаем ограничение через Field


class StudentAnswerInDBBase(StudentAnswerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class StudentAnswer(StudentAnswerInDBBase):
    pass


class StudentAnswerInDB(StudentAnswerInDBBase):
    pass
