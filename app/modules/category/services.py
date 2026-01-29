from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.modules.category.models import Category
from app.modules.category.schemas import CategoryCreate


async def create_category(db: AsyncSession, category_data: CategoryCreate):
    # Check if a category with this name already exists
    query = select(Category).where(Category.name == category_data.name)
    result = await db.execute(query)
    existing_category = result.scalar_one_or_none()

    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A category with this name already exists.",
        )

    # If the name is unique, create the new Category object
    new_category = Category(
        name=category_data.name,
        description=category_data.description,
        is_active=category_data.is_active,
    )

    # Save to db
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category


async def get_active_categories(db: AsyncSession):
    # Filter by is_active == True to satisfy the requirement
    query = select(Category).where(Category.is_active == True)
    result = await db.execute(query)
    return result.scalars().all()
