from typing import Optional

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.learning_attitude import LearningAttitude
from schemas.learning_attitude import LearningAttitudeCreate, LearningAttitudeUpdate


class LearningAttitudeRepository:
    
    async def create(self, db: AsyncSession, learning_attitude: LearningAttitudeCreate) -> LearningAttitude:    
        db_learning_attitude = LearningAttitude(name=learning_attitude.name)
        db.add(db_learning_attitude)
        await db.commit()
        await db.refresh(db_learning_attitude)
        return db_learning_attitude
    
    async def get(self, db: AsyncSession, learning_attitude_id: int) -> LearningAttitude:
        result = await db.execute(select(LearningAttitude).filter(LearningAttitude.id == learning_attitude_id))
        return result.scalars().first()
    
    async def update(self, db: AsyncSession, learning_attitude_id: int, learning_attitude_update: LearningAttitudeUpdate) -> Optional[LearningAttitude]:
        result = await db.execute(select(LearningAttitude).filter(LearningAttitude.id == learning_attitude_id))
        db_learning_attitude = result.scalars().first()
        if not db_learning_attitude:
            return None
        for var, value in vars(learning_attitude_update).items():
            setattr(db_learning_attitude, var, value) if value else None
        db.add(db_learning_attitude)
        await db.commit()
        await db.refresh(db_learning_attitude)
        return db_learning_attitude
    
    async def delete(self, db: AsyncSession, learning_attitude_id: int) -> Optional[LearningAttitude]:
        result = await db.execute(select(LearningAttitude).filter(LearningAttitude.id == learning_attitude_id))
        db_learning_attitude = result.scalars().first()
        if not db_learning_attitude:
            return None
        await db.execute(sqlalchemy_delete(LearningAttitude).where(LearningAttitude.id == learning_attitude_id))
        await db.commit()
        return db_learning_attitude
    
    async def get_all(self, db: AsyncSession) -> list[LearningAttitude]:
        result = await db.execute(select(LearningAttitude))
        return result.scalars().all()