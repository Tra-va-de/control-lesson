from typing import List, Optional

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.lesson import LessonRepository
from schemas.lesson import LessonCreate, LessonUpdate, Lesson


class LessonService:

    def __init__(self, repository: LessonRepository):
        self.repository = repository
    
    async def create_lesson(self, db: AsyncSession, lesson_create: LessonCreate) -> Lesson:
        result = await self.repository.create(db, lesson_create)
        await self.invalidate_cache()
        return Lesson.model_validate(result)
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_lesson(self, db: AsyncSession, lesson_id: int) -> Optional[Lesson]:
        result = await self.repository.get(db, lesson_id)
        return Lesson.model_validate(result) if result else None
    
    async def update_lesson(self, db: AsyncSession, lesson_id: int, lesson_update: LessonUpdate) -> Optional[Lesson]:
        result = await self.repository.update(db, lesson_id, lesson_update)
        await self.invalidate_cache()
        return Lesson.model_validate(result) if result else None
    
    async def delete_lesson(self, db: AsyncSession, lesson_id: int) -> Optional[Lesson]:
        result = await self.repository.delete(db, lesson_id)
        await self.invalidate_cache()
        return result
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_lessons(self, db: AsyncSession) -> List[Lesson]:
        result = await self.repository.get_all(db)
        return [Lesson.model_validate(lesson) for lesson in result]
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_lessons_by_discipline(self, db: AsyncSession, discipline_id: int) -> List[Lesson]:
        result = await self.repository.get_by_discipline_id(db, discipline_id)
        return [Lesson.model_validate(lesson) for lesson in result]
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_lessons_by_lesson_level(self, db: AsyncSession, lesson_level_id: int) -> List[Lesson]:
        result = await self.repository.get_by_lesson_level_id(db, lesson_level_id)
        return [Lesson.model_validate(lesson) for lesson in result]
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_lessons_by_discipline_and_lesson_level(self, db: AsyncSession, lesson_level_id: int, discipline_id: int) -> List[Lesson]:
        result = await self.repository.get_by_discipline_and_lesson_level_id(db, lesson_level_id, discipline_id)
        return [Lesson.model_validate(lesson) for lesson in result]
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()