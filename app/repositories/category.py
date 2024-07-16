from typing import Optional

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate


class CategoryRepository:
    
    async def create(self, db: AsyncSession, category: CategoryCreate) -> Category:    
        db_category = Category(name=category.name)
        db.add(db_category)
        await db.commit()
        await db.refresh(db_category)
        return db_category
    
    async def get(self, db: AsyncSession, category_id: int) -> Category:
        result = await db.execute(select(Category).filter(Category.id == category_id))
        return result.scalars().first()
    
    async def update(self, db: AsyncSession, category_id: int, category_update: CategoryUpdate) -> Optional[Category]:
        result = await db.execute(select(Category).filter(Category.id == category_id))
        db_category = result.scalars().first()
        if not db_category:
            return None
        for var, value in vars(category_update).items():
            setattr(db_category, var, value) if value else None
        db.add(db_category)
        await db.commit()
        await db.refresh(db_category)
        return db_category
    
    async def delete(self, db: AsyncSession, category_id: int) -> Optional[Category]:
        result = await db.execute(select(Category).filter(Category.id == category_id))
        db_category = result.scalars().first()
        if not db_category:
            return None
        await db.execute(sqlalchemy_delete(Category).where(Category.id == category_id))
        await db.commit()
        return db_category
    
    async def get_all(self, db: AsyncSession) -> list[Category]:
        result = await db.execute(select(Category))
        return result.scalars().all()