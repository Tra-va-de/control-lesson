from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from db.session import engine, Base
from core.cache import init_cache
from api.v1.endpoints import discipline, lesson_level, category, lesson, subject, question


def create_app() -> FastAPI:
    """
    Фабрика FastAPI.
    """
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        async with engine.begin() as conn:
            # Создаем таблицы в базе данных, если они еще не существуют
            await conn.run_sync(Base.metadata.create_all)
        # Инициализируем кэш
        await init_cache()
        yield


    app = FastAPI(
        title="Lesson Control API",
        description="API для управления контрольными уроками",
        version="1.0.0",
        lifespan=lifespan,
    )

    # Подключаем роутеры для различных endpoints
    app.include_router(discipline.router, prefix="/api/v1", tags=["Discipline"])
    app.include_router(lesson_level.router, prefix="/api/v1", tags=["Lesson level"])
    app.include_router(category.router, prefix="/api/v1", tags=["Category"])
    app.include_router(lesson.router, prefix="/api/v1", tags=["Lesson"])
    app.include_router(subject.router, prefix="/api/v1", tags=["Subjects"])
    app.include_router(question.router, prefix="/api/v1", tags=["Questions"])

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080", "http://localhost:8000"],  # URL вашего фронтенда
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    app = create_app()

    uvicorn.run(app, host="0.0.0.0", port=8000)