from datetime import date
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class StudentBase(BaseModel):
    first_name: str = Field(..., example="Иван", min_length=1, max_length=30)
    last_name: str = Field(..., example="Петров", min_length=1, max_length=30)
    date_of_birth: date = Field(..., example="2000-01-01")


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    first_name: Optional[str] = Field(None, example="Иван", min_length=1, max_length=30)
    last_name: Optional[str] = Field(None, example="Петров", min_length=1, max_length=30)
    date_of_birth: Optional[date] = Field(None, example="2000-01-01")


class StudentInDBBase(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Student(StudentInDBBase):
    pass


class StudentInDB(StudentInDBBase):
    pass
