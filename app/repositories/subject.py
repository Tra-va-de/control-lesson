from typing import List, Optional

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.subject import Subject
from schemas.subject import SubjectCreate, SubjectUpdate


class SubjectRepository:
    
    async def create(self, db: AsyncSession, subject: SubjectCreate) -> Subject:
        db_subject = Subject(
            name=subject.name,
            lesson_id=subject.lesson_id,
            category_id=subject.category_id
        )
        db.add(db_subject)
        await db.commit()
        await db.refresh(db_subject)
        return db_subject

    async def get(self, db: AsyncSession, subject_id: int) -> Optional[Subject]:
        result = await db.execute(select(Subject).filter(Subject.id == subject_id))
        return result.scalars().first()     
    
    async def update(self, db: AsyncSession, subject_id: int, subject_update: SubjectUpdate) -> Optional[Subject]:
        result = await db.execute(select(Subject).filter(Subject.id == subject_id))
        db_subject = result.scalars().first()
        if not db_subject:
            return None
        for var, value in vars(subject_update).items():
            setattr(db_subject, var, value) if value else None
        db.add(db_subject)
        await db.commit()
        await db.refresh(db_subject)
        return db_subject

    async def delete(self, db: AsyncSession, subject_id: int) -> Optional[Subject]:
        result = await db.execute(select(Subject).filter(Subject.id == subject_id))
        db_subject = result.scalars().first()
        if not db_subject:
            return None
        await db.execute(sqlalchemy_delete(Subject).where(Subject.id == subject_id))
        await db.commit()
        return db_subject
    
    async def get_all(self, db: AsyncSession) -> List[Subject]:
        result = await db.execute(select(Subject))
        return result.scalars().all()
    
    async def get_by_lesson_id(self, db: AsyncSession, lesson_id: int) -> List[Subject]:
        result = await db.execute(select(Subject).where(Subject.lesson_id == lesson_id))
        return result.scalars().all()
    
    async def get_by_category_id(self, db: AsyncSession, category_id: int) -> List[Subject]:
        result = await db.execute(select(Subject).where(Subject.category_id == category_id))
        return result.scalars().all()
    
    async def get_by_lesson_id_and_category_id(self, db: AsyncSession, lesson_id: int, category_id: int) -> List[Subject]:
        result = await db.execute(select(Subject).where(Subject.lesson_id == lesson_id, Subject.category_id == category_id))
        return result.scalars().all()