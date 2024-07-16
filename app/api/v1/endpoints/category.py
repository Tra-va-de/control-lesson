from typing import List

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.category import Category, CategoryCreate, CategoryUpdate
from services.category import CategoryService
from repositories.category import CategoryRepository
from db.session import get_async_session


router = APIRouter()


def get_category_service() -> CategoryService:
    return CategoryService(repository=CategoryRepository())


@router.post("/categories/", response_model=Category)
async def create_category(
    category_create: CategoryCreate,
    db: AsyncSession = Depends(get_async_session),
    service: CategoryService = Depends(get_category_service)
):
    return await service.create_category(db, category_create)


@router.get("/categories/{category_id}", response_model=Category)
async def read_category(
    category_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: CategoryService = Depends(get_category_service)
):
    db_category = await service.get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.put("/categories/{category_id}", response_model=Category)
async def update_category(
    category_id: int, 
    category_update: CategoryUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: CategoryService = Depends(get_category_service)
):
    updated_category = await service.update_category(db, category_id, category_update)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@router.delete("/categories/{category_id}", response_model=Category)
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: CategoryService = Depends(get_category_service)
):
    success = await service.delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return success


@router.get("/categories/", response_model=List[Category])
async def read_categories(
    db: AsyncSession = Depends(get_async_session),
    service: CategoryService = Depends(get_category_service)
):
    result = await service.get_all_categories(db)
    if result is None:
        raise HTTPException(status_code=404, detail="Categories not found")
    return result