from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db
from app.modules.category import schemas, services

router = APIRouter(prefix="/categories", tags=["Categories"])


# create endpoint
@router.post("/", response_model=schemas.CategoryResponse)
async def create_new_category(
    category_in: schemas.CategoryCreate, db: AsyncSession = Depends(get_db)
):
    return await services.create_category(db, category_in)


@router.get("/", response_model=List[schemas.CategoryResponse])
async def list_categories(db: AsyncSession = Depends(get_db)):
    return await services.get_active_categories(db)
