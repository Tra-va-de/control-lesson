from typing import List, Optional

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.learning_attitude import LearningAttitudeRepository
from schemas.learning_attitude import LearningAttitudeCreate, LearningAttitudeUpdate, LearningAttitude


class LearningAttitudeService:

    def __init__(self, repository: LearningAttitudeRepository):
        self.repository = repository
    
    async def create_learning_attitude(self, db: AsyncSession, learning_attitude_create: LearningAttitudeCreate) -> LearningAttitude:
        result = await self.repository.create(db, learning_attitude_create)
        await self.invalidate_cache()
        return LearningAttitude.model_validate(result)
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_learning_attitude(self, db: AsyncSession, learning_attitude_id: int) -> Optional[LearningAttitude]:
        result = await self.repository.get(db, learning_attitude_id)
        return LearningAttitude.model_validate(result) if result else None
    
    async def update_learning_attitude(self, db: AsyncSession, learning_attitude_id: int, learning_attitude_update: LearningAttitudeUpdate) -> Optional[LearningAttitude]:
        result = await self.repository.update(db, learning_attitude_id, learning_attitude_update)
        await self.invalidate_cache()
        return LearningAttitude.model_validate(result) if result else None
    
    async def delete_learning_attitude(self, db: AsyncSession, learning_attitude_id: int) -> Optional[LearningAttitude]:
        result = await self.repository.delete(db, learning_attitude_id)
        await self.invalidate_cache()
        return result
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_learning_attitudes(self, db: AsyncSession) -> List[LearningAttitude]:
        result = await self.repository.get_all(db)
        return [LearningAttitude.model_validate(learning_attitude) for learning_attitude in result]
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()