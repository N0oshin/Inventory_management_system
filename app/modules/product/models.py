from sqlalchemy import String, Numeric, Integer, ForeignKey, false
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

#  We use TYPE_CHECKING to prevent circular imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.category.models import Category


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0)
    category_id: Mapped[str] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )

    # --- THE RELATIONSHIP ---
    category: Mapped["Category"] = relationship("Category", back_populates="products")
