from typing import Optional

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.discipline import Discipline
from schemas.discipline import DisciplineCreate, DisciplineUpdate


class DisciplineRepository:
    
    async def create(self, db: AsyncSession, discipline: DisciplineCreate) -> Discipline:    
        db_discipline = Discipline(name=discipline.name)
        db.add(db_discipline)
        await db.commit()
        await db.refresh(db_discipline)
        return db_discipline
    
    async def get(self, db: AsyncSession, discipline_id: int) -> Discipline:
        result = await db.execute(select(Discipline).filter(Discipline.id == discipline_id))
        return result.scalars().first()
    
    async def update(self, db: AsyncSession, discipline_id: int, discipline_update: DisciplineUpdate) -> Optional[Discipline]:
        result = await db.execute(select(Discipline).filter(Discipline.id == discipline_id))
        db_discipline = result.scalars().first()
        if not db_discipline:
            return None
        for var, value in vars(discipline_update).items():
            setattr(db_discipline, var, value) if value else None
        db.add(db_discipline)
        await db.commit()
        await db.refresh(db_discipline)
        return db_discipline
    
    async def delete(self, db: AsyncSession, discipline_id: int) -> Optional[Discipline]:
        result = await db.execute(select(Discipline).filter(Discipline.id == discipline_id))
        db_discipline = result.scalars().first()
        if not db_discipline:
            return None
        await db.execute(sqlalchemy_delete(Discipline).where(Discipline.id == discipline_id))
        await db.commit()
        return db_discipline
    
    async def get_all(self, db: AsyncSession) -> list[Discipline]:
        result = await db.execute(select(Discipline))
        return result.scalars().all()
