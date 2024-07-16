from typing import List

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.lesson_level import LessonLevel, LessonLevelCreate, LessonLevelUpdate
from services.lesson_level import LessonLevelService
from repositories.lesson_level import LessonLevelRepository
from db.session import get_async_session


router = APIRouter()


def get_lesson_level_service() -> LessonLevelService:
    return LessonLevelService(repository=LessonLevelRepository())


@router.post("/lesson-levels/", response_model=LessonLevel)
async def create_lesson_level(
    lesson_level_create: LessonLevelCreate,
    db: AsyncSession = Depends(get_async_session),
    service: LessonLevelService = Depends(get_lesson_level_service)
):
    return await service.create_lesson_level(db, lesson_level_create)


@router.get("/lesson-levels/{lesson_level_id}", response_model=LessonLevel)
async def read_lesson_level(
    lesson_level_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LessonLevelService = Depends(get_lesson_level_service)
):
    db_lesson_level = await service.get_lesson_level(db, lesson_level_id)
    if db_lesson_level is None:
        raise HTTPException(status_code=404, detail="Lesson level not found")
    return db_lesson_level


@router.put("/lesson-levels/{lesson_level_id}", response_model=LessonLevel)
async def update_lesson_level(
    lesson_level_id: int, 
    lesson_level_update: LessonLevelUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: LessonLevelService = Depends(get_lesson_level_service)
):
    updated_lesson_level = await service.update_lesson_level(db, lesson_level_id, lesson_level_update)
    if updated_lesson_level is None:
        raise HTTPException(status_code=404, detail="Lesson level not found")
    return updated_lesson_level


@router.delete("/lesson-levels/{lesson_level_id}", response_model=LessonLevel)
async def delete_lesson_level(
    lesson_level_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LessonLevelService = Depends(get_lesson_level_service)
):
    success = await service.delete_lesson_level(db, lesson_level_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lesson level not found")
    return success


@router.get("/lesson-levels/", response_model=List[LessonLevel])
async def read_lesson_levels(
    db: AsyncSession = Depends(get_async_session),
    service: LessonLevelService = Depends(get_lesson_level_service)
):
    result = await service.get_all_lesson_levels(db)
    if result is None:
        raise HTTPException(status_code=404, detail="Lesson levels not found")
    return result