from typing import List, Optional

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.student import StudentRepository
from schemas.student import StudentCreate, StudentUpdate, Student


class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    async def create_student(self, db: AsyncSession, student_create: StudentCreate) -> Student:
        result = await self.repository.create(db, student_create)
        await self.invalidate_cache()
        return Student.model_validate(result)

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_student(self, db: AsyncSession, student_id: int) -> Optional[Student]:
        result = await self.repository.get(db, student_id)
        return Student.model_validate(result) if result else None

    async def update_student(self, db: AsyncSession, student_id: int, student_update: StudentUpdate) -> Optional[Student]:
        result = await self.repository.update(db, student_id, student_update)
        await self.invalidate_cache()
        return Student.model_validate(result) if result else None

    async def delete_student(self, db: AsyncSession, student_id: int) -> Optional[Student]:
        result = await self.repository.delete(db, student_id)
        await self.invalidate_cache()
        return result

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_students(self, db: AsyncSession) -> List[Student]:
        result = await self.repository.get_all(db)
        return [Student.model_validate(student) for student in result]

    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()