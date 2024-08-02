from typing import List, Optional

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.lesson_level import LessonLevelRepository
from schemas.lesson_level import LessonLevelCreate, LessonLevelUpdate, LessonLevel


class LessonLevelService:

    def __init__(self, repository: LessonLevelRepository):
        self.repository = repository
    
    async def create_lesson_level(self, db: AsyncSession, lesson_level_create: LessonLevelCreate) -> LessonLevel:
        result = await self.repository.create(db, lesson_level_create)
        await self.invalidate_cache()
        return LessonLevel.model_validate(result)
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_lesson_level(self, db: AsyncSession, lesson_level_id: int) -> Optional[LessonLevel]:
        result = await self.repository.get(db, lesson_level_id)
        return LessonLevel.model_validate(result) if result else None
    
    async def update_lesson_level(self, db: AsyncSession, lesson_level_id: int, lesson_level_update: LessonLevelUpdate) -> Optional[LessonLevel]:
        result = await self.repository.update(db, lesson_level_id, lesson_level_update)
        await self.invalidate_cache()
        return LessonLevel.model_validate(result) if result else None
    
    async def delete_lesson_level(self, db: AsyncSession, lesson_level_id: int) -> Optional[LessonLevel]:
        result = await self.repository.delete(db, lesson_level_id)
        await self.invalidate_cache()
        return result
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_lesson_levels(self, db: AsyncSession) -> List[LessonLevel]:
        result = await self.repository.get_all(db)
        return [LessonLevel.model_validate(lesson_level) for lesson_level in result]
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()