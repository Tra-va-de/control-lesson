from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from core.config import settings


# Получение базового URL базы данных
DATABASE_URL = settings.DATABASE_URL

# Создание базы данных
class Base(DeclarativeBase):
    pass

# Создание движка базы данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Создание сессии
async_session_maker  = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session