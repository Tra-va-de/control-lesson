from typing import Optional

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.lesson_level import LessonLevel
from schemas.lesson_level import LessonLevelCreate, LessonLevelUpdate


class LessonLevelRepository:
    
    async def create(self, db: AsyncSession, lesson_level: LessonLevelCreate) -> LessonLevel:    
        db_lesson_level = LessonLevel(name=lesson_level.name)
        db.add(db_lesson_level)
        await db.commit()
        await db.refresh(db_lesson_level)
        return db_lesson_level
    
    async def get(self, db: AsyncSession, lesson_level_id: int) -> LessonLevel:
        result = await db.execute(select(LessonLevel).filter(LessonLevel.id == lesson_level_id))
        return result.scalars().first()
    
    async def update(self, db: AsyncSession, lesson_level_id: int, lesson_level_update: LessonLevelUpdate) -> Optional[LessonLevel]:
        result = await db.execute(select(LessonLevel).filter(LessonLevel.id == lesson_level_id))
        db_lesson_level = result.scalars().first()
        if not db_lesson_level:
            return None
        for var, value in vars(lesson_level_update).items():
            setattr(db_lesson_level, var, value) if value else None
        db.add(db_lesson_level)
        await db.commit()
        await db.refresh(db_lesson_level)
        return db_lesson_level
    
    async def delete(self, db: AsyncSession, lesson_level_id: int) -> Optional[LessonLevel]:
        result = await db.execute(select(LessonLevel).filter(LessonLevel.id == lesson_level_id))
        db_lesson_level = result.scalars().first()
        if not db_lesson_level:
            return None
        await db.execute(sqlalchemy_delete(LessonLevel).where(LessonLevel.id == lesson_level_id))
        await db.commit()
        return db_lesson_level
    
    async def get_all(self, db: AsyncSession) -> list[LessonLevel]:
        result = await db.execute(select(LessonLevel))
        return result.scalars().all()