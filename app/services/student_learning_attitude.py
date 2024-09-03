from typing import List, Optional

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.student_learning_attitude import StudentLearningAttitudeRepository
from schemas.student_learning_attitude import StudentLearningAttitudeCreate, \
                                              StudentLearningAttitudeCreateOrUpdate, \
                                              StudentLearningAttitudeUpdate, \
                                              StudentLearningAttitude


class StudentLearningAttitudeService:

    def __init__(self, repository: StudentLearningAttitudeRepository):
        self.repository = repository

    async def create_student_learning_attitude(self, db: AsyncSession, student_learning_attitude_create: StudentLearningAttitudeCreate) -> StudentLearningAttitude:
        result = await self.repository.create(db, student_learning_attitude_create)
        await self.invalidate_cache()
        return StudentLearningAttitude.model_validate(result)

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_student_learning_attitude(self, db: AsyncSession, student_learning_attitude_id: int) -> Optional[StudentLearningAttitude]:
        result = await self.repository.get(db, student_learning_attitude_id)
        return StudentLearningAttitude.model_validate(result) if result else None

    async def update_student_learning_attitude(self, db: AsyncSession, student_learning_attitude_id: int, student_learning_attitude_update: StudentLearningAttitudeUpdate) -> Optional[StudentLearningAttitude]:
        result = await self.repository.update(db, student_learning_attitude_id, student_learning_attitude_update)
        await self.invalidate_cache()
        return StudentLearningAttitude.model_validate(result) if result else None

    async def delete_student_learning_attitude(self, db: AsyncSession, student_learning_attitude_id: int) -> Optional[StudentLearningAttitude]:
        result = await self.repository.delete(db, student_learning_attitude_id)
        await self.invalidate_cache()
        return result

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_student_learning_attitudes(self, db: AsyncSession) -> List[StudentLearningAttitude]:
        result = await self.repository.get_all(db)
        return [StudentLearningAttitude.model_validate(attitude) for attitude in result]

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_student_learning_attitudes_by_student_id(self, db: AsyncSession, student_id: int) -> StudentLearningAttitude:
        result = await self.repository.get_by_student_id(db, student_id)
        return StudentLearningAttitude.model_validate(result) if result else None

    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_student_learning_attitudes_by_learning_attitude_id(self, db: AsyncSession, learning_attitude_id: int) -> StudentLearningAttitude:
        result = await self.repository.get_by_learning_attitude_id(db, learning_attitude_id)
        return StudentLearningAttitude.model_validate(result) if result else None
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_student_learning_attitudes_by_student_and_learning_attitude_id(self, db: AsyncSession, student_id: int, learning_attitude_id: int) -> StudentLearningAttitude:
        result = await self.repository.get_by_student_id_and_learning_attitude_id(db, student_id, learning_attitude_id)
        return StudentLearningAttitude.model_validate(result) if result else None
    
    async def create_or_update_student_learning_attitude(self, db: AsyncSession, student_learning_attitude: StudentLearningAttitudeCreateOrUpdate) -> StudentLearningAttitude:
        return await self.repository.create_or_update(db, student_learning_attitude)

    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()