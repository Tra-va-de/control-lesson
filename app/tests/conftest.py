import asyncio
from typing import AsyncGenerator

import pytest
from fastapi import FastAPI

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from httpx import AsyncClient

from core.config import settings
from db.session import Base
from core.cache import init_cache

from db.session import get_async_session

from main import create_app


# Получение базового URL тестовой базы данных
TEST_DATABASE_URL = settings.TEST_DATABASE_URL

# Создание движка базы данных
test_engine = create_async_engine(TEST_DATABASE_URL, echo=True)

# Создание сессии
async_session_maker = async_sessionmaker(bind=test_engine, class_=AsyncSession, expire_on_commit=False)


# Setup
@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Create an instance of the default event loop for each test case."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


# Инициализация кэша
@pytest.fixture(scope="session", autouse=True)
async def initialize_redis(event_loop):
    await init_cache()


# Инициализация базы данных
@pytest.fixture(scope="session", autouse=True)
async def db_init(event_loop):
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield 
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# Подключение к базе данных для тестов
async def get_test_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


# Подключение к тестовому API
@pytest.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    # Создание приложения
    app: FastAPI = create_app()
    # Переопределение зависимостей
    app.dependency_overrides[get_async_session] = get_test_session

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac