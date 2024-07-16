from typing import List, Optional

from fastapi import Depends
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.category import CategoryRepository
from schemas.category import CategoryCreate, CategoryUpdate, Category


class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository
    
    async def create_category(self, db: AsyncSession, category_create: CategoryCreate) -> Category:
        result = await self.repository.create(db, category_create)
        await self.invalidate_cache()
        return Category.model_validate(result)
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_category(self, db: AsyncSession, category_id: int) -> Optional[Category]:
        result = await self.repository.get(db, category_id)
        return Category.model_validate(result) if result else None
    
    async def update_category(self, db: AsyncSession, category_id: int, category_update: CategoryUpdate) -> Optional[Category]:
        result = await self.repository.update(db, category_id, category_update)
        await self.invalidate_cache()
        return Category.model_validate(result) if result else None
    
    async def delete_category(self, db: AsyncSession, category_id: int) -> Optional[Category]:
        result = await self.repository.delete(db, category_id)
        await self.invalidate_cache()
        return result
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_categories(self, db: AsyncSession) -> List[Category]:
        result = await self.repository.get_all(db)
        return [Category.model_validate(category) for category in result]
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()