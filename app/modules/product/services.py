from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status

from app.modules.product.models import Product
from app.modules.product.schemas import ProductCreate
from app.modules.category.models import Category


async def create_product(db: AsyncSession, product_data: ProductCreate):
    # Integrity Check, ensure the category exists before linking a product to it.
    category_query = select(Category).where(Category.id == product_data.category_id)
    category_result = await db.execute(category_query)
    category = category_result.scalar_one_or_none()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category ID not found.",
        )

    # create the Product instance
    new_product = Product(**product_data.model_dump())

    # Save to DB
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


async def get_products_by_category(db: AsyncSession, category_id: str):
    query = select(Product).where(Product.category_id == category_id)
    result = await db.execute(query)
    return result.scalars().all()
