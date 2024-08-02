from typing import Optional, List

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.student_answer import StudentAnswerRepository
from schemas.student_answer import StudentAnswerCreate, StudentAnswerUpdate, StudentAnswer


class StudentAnswerService:
    def __init__(self, repository: StudentAnswerRepository):
        self.repository = repository

    async def create_student_answer(self, db: AsyncSession, student_answer_create: StudentAnswerCreate) -> StudentAnswer:
        return await self.repository.create(db, student_answer_create)

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_student_answer(self, db: AsyncSession, student_answer_id: int) -> Optional[StudentAnswer]:
        return await self.repository.get(db, student_answer_id)

    async def update_student_answer(self, db: AsyncSession, student_answer_id: int, student_answer_update: StudentAnswerUpdate) -> Optional[StudentAnswer]:
        return await self.repository.update(db, student_answer_id, student_answer_update)

    async def delete_student_answer(self, db: AsyncSession, student_answer_id: int) -> Optional[StudentAnswer]:
        return await self.repository.delete(db, student_answer_id)

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_student_answers(self, db: AsyncSession) -> List[StudentAnswer]:
        return await self.repository.get_all(db)
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()
