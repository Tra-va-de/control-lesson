from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class DisciplineBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class DisciplineCreate(DisciplineBase):
    pass


class DisciplineUpdate(DisciplineBase):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    

class Discipline(DisciplineBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)
