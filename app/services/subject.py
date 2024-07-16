from typing import List, Optional

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.subject import SubjectRepository
from schemas.subject import SubjectCreate, SubjectUpdate, Subject


class SubjectService:

    def __init__(self, repository: SubjectRepository):
        self.repository = repository
    
    async def create_subject(self, db: AsyncSession, subject_create: SubjectCreate) -> Subject:
        result = await self.repository.create(db, subject_create)
        await self.invalidate_cache()
        return Subject.model_validate(result)
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_subject(self, db: AsyncSession, subject_id: int) -> Optional[Subject]:
        result = await self.repository.get(db, subject_id)
        return Subject.model_validate(result) if result else None
    
    async def update_subject(self, db: AsyncSession, subject_id: int, subject_update: SubjectUpdate) -> Optional[Subject]:
        result = await self.repository.update(db, subject_id, subject_update)
        await self.invalidate_cache()
        return Subject.model_validate(result) if result else None
    
    async def delete_subject(self, db: AsyncSession, subject_id: int) -> Optional[Subject]:
        result = await self.repository.delete(db, subject_id)
        await self.invalidate_cache()
        return result
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_subjects(self, db: AsyncSession) -> List[Subject]:
        result = await self.repository.get_all(db)
        return [Subject.model_validate(subject) for subject in result]
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_subjects_by_lesson(self, db: AsyncSession, lesson_id: int) -> List[Subject]:
        result = await self.repository.get_by_lesson_id(db, lesson_id)
        return [Subject.model_validate(subject) for subject in result]
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_subjects_by_category(self, db: AsyncSession, category_id: int) -> List[Subject]:
        result = await self.repository.get_by_category_id(db, category_id)
        return [Subject.model_validate(subject) for subject in result]
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_subjects_by_lesson_and_category(self, db: AsyncSession, lesson_id: int, category_id: int) -> List[Subject]:
        result = await self.repository.get_by_lesson_id_and_category_id(db, lesson_id, category_id)
        return [Subject.model_validate(subject) for subject in result]
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()