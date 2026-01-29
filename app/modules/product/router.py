from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.modules.product import schemas, services

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=schemas.ProductResponse)
async def create_new_product(
    product_in: schemas.ProductCreate,
    db: AsyncSession = Depends(get_db),
    # Depends(get_db) asks your database utility to "hand over" a live session. Once the function is finished, FastAPI handles the cleanup automatically.
):
    return await services.create_product(db, product_in)


@router.get("/", response_model=List[schemas.ProductResponse])
async def list_all_products(db: AsyncSession = Depends(get_db)):
    from sqlalchemy.future import select
    from app.modules.product.models import Product

    # query = select(Product)
    query = select(Product).options(selectinload(Product.category))
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/category/{category_id}", response_model=List[schemas.ProductResponse])
async def get_products_by_category(
    category_id: UUID, db: AsyncSession = Depends(get_db)
):
    # Requirement: Filter products by category
    return await services.get_products_by_category(db, str(category_id))


"""
response_model=schemas.ProductResponse: 
This is the Outgoing Filter. It ensures that even if our database object has 20 fields, the API only sends back the fields defined in ProductResponse
"""
