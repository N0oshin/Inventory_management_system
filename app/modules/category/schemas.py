from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True


# inherit the categorybase
class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


"""
Pydantic expects data as a Python Dictionary ({"id": ...}). However, SQLAlchemy returns data as a Database Object.
from_attributes=True tells Pydantic to look at the object's attributes and convert them.
"""
