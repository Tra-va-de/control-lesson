from typing import Optional, List

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.lesson import Lesson
from schemas.lesson import LessonCreate, LessonUpdate


class LessonRepository:
    
    async def create(self, db: AsyncSession, lesson: LessonCreate) -> Lesson:
        db_lesson = Lesson(
            name=lesson.name,
            discipline_id=lesson.discipline_id,
            lesson_level_id=lesson.lesson_level_id
        )
        db.add(db_lesson)
        await db.commit()
        await db.refresh(db_lesson)
        return db_lesson

    async def get(self, db: AsyncSession, lesson_id: int) -> Optional[Lesson]:
        result = await db.execute(select(Lesson).filter(Lesson.id == lesson_id))
        return result.scalars().first()

    async def update(self, db: AsyncSession, lesson_id: int, lesson_update: LessonUpdate) -> Optional[Lesson]:
        result = await db.execute(select(Lesson).filter(Lesson.id == lesson_id))
        db_lesson = result.scalars().first()
        if not db_lesson:
            return None
        for var, value in vars(lesson_update).items():
            setattr(db_lesson, var, value) if value else None
        db.add(db_lesson)
        await db.commit()
        await db.refresh(db_lesson)
        return db_lesson

    async def delete(self, db: AsyncSession, lesson_id: int) -> Optional[Lesson]:
    
        result = await db.execute(select(Lesson).filter(Lesson.id == lesson_id))
        db_lesson = result.scalars().first()
        if not db_lesson:
            return None
        await db.execute(sqlalchemy_delete(Lesson).where(Lesson.id == lesson_id))
        await db.commit()
        return db_lesson

    async def get_all(self, db: AsyncSession) -> List[Lesson]:
        result = await db.execute(select(Lesson))
        return result.scalars().all()

    async def get_by_discipline_id(self, db: AsyncSession, discipline_id: int) -> List[Lesson]:
        result = await db.execute(select(Lesson).filter(Lesson.discipline_id == discipline_id))
        return result.scalars().all()

    async def get_by_lesson_level_id(self, db: AsyncSession, lesson_level_id: int) -> List[Lesson]:
        result = await db.execute(select(Lesson).filter(Lesson.lesson_level_id == lesson_level_id))
        return result.scalars().all()
    
    async def get_by_discipline_and_lesson_level_id(self, db: AsyncSession, discipline_id: int, lesson_level_id: int) -> List[Lesson]:
        result = await db.execute(select(Lesson).filter(Lesson.discipline_id == discipline_id, Lesson.lesson_level_id == lesson_level_id))
        return result.scalars().all()