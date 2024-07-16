from typing import List, Optional

from fastapi import Depends
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.discipline import DisciplineRepository
from schemas.discipline import DisciplineCreate, DisciplineUpdate, Discipline


class DisciplineService:

    def __init__(self, repository: DisciplineRepository):
        self.repository = repository
    
    async def create_discipline(self, db: AsyncSession, discipline_create: DisciplineCreate) -> Discipline:
        result = await self.repository.create(db, discipline_create)
        await self.invalidate_cache()
        return Discipline.model_validate(result)
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_discipline(self, db: AsyncSession, discipline_id: int) -> Optional[Discipline]:
        result = await self.repository.get(db, discipline_id)
        return Discipline.model_validate(result) if result else None
    
    async def update_discipline(self, db: AsyncSession, discipline_id: int, discipline_update: DisciplineUpdate) -> Optional[Discipline]:
        result = await self.repository.update(db, discipline_id, discipline_update)
        await self.invalidate_cache()
        return Discipline.model_validate(result) if result else None
    
    async def delete_discipline(self, db: AsyncSession, discipline_id: int) -> Optional[Discipline]:
        result = await self.repository.delete(db, discipline_id)
        await self.invalidate_cache()
        return result
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_disciplines(self, db: AsyncSession) -> List[Discipline]:
        result = await self.repository.get_all(db)
        return [Discipline.model_validate(discipline) for discipline in result]
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()
