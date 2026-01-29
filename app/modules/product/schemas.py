from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from decimal import Decimal
from typing import Optional

from app.modules.category.schemas import CategoryResponse


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(..., ge=0)
    stock_quantity: int = Field(default=0, ge=0)
    category_id: UUID


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: UUID
    category: Optional["CategoryResponse"] = None
    model_config = ConfigDict(from_attributes=True)
    # Pydantic (The Schema): By default. It only take Python Dictionaries (e.g., {"name": "Laptop", "price": 999.99}).SQLAlchemy (The Model): When you fetch data from the database, it doesn't give you a dictionary. It gives you a Class Object (e.g., <Product object at 0x123...>). so tell pydantic to read data from class attributes.
