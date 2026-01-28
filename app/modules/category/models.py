from sqlalchemy import String, Text, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
import datetime
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.modules.product.models import Product


class Category(Base):
    __tablename__ = "categories"

    # Category name must be unique
    name: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )

    # Optional description
    description: Mapped[str] = mapped_column(Text, nullable=True)

    # Requirement: Soft delete field
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # 'func.now()' tells Postgres to generate the time itself
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="category"
    )
