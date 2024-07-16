from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    

class Category(CategoryBase):
    id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)
