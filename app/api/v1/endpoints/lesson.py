from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.lesson import Lesson, LessonCreate, LessonUpdate
from services.lesson import LessonService
from repositories.lesson import LessonRepository
from db.session import get_async_session


router = APIRouter()


async def get_lesson_service() -> LessonService:
    return LessonService(repository=LessonRepository())


@router.post("/lessons/", response_model=Lesson)
async def create_lesson(
    lesson: LessonCreate,
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    return await service.create_lesson(db, lesson)


@router.get("/lessons/{lesson_id}", response_model=Lesson)
async def read_lesson(
    lesson_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    db_lesson = await service.get_lesson(db, lesson_id)
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return db_lesson


@router.put("/lessons/{lesson_id}", response_model=Lesson)
async def update_lesson(
    lesson_id: int,
    updates: LessonUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    db_lesson = await service.update_lesson(db, lesson_id, updates)
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return db_lesson


@router.delete("/lessons/{lesson_id}", response_model=Lesson)
async def delete_lesson(
    lesson_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    db_lesson = await service.delete_lesson(db, lesson_id)
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return db_lesson


@router.get("/lessons/", response_model=List[Lesson])
async def read_lessons(
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    lessons = await service.get_all_lessons(db)
    if lessons is None:
        raise HTTPException(status_code=404, detail="Lessons not found")
    return lessons


@router.get("/lessons/discipline/{discipline_id}", response_model=List[Lesson])
async def read_lessons_by_discipline(
    discipline_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    lessons = await service.get_lessons_by_discipline(db, discipline_id)
    if lessons is None:
        raise HTTPException(status_code=404, detail="Lessons not found")
    return lessons


@router.get("/lessons/discipline/{discipline_id}/level/{lesson_level_id}", response_model=List[Lesson])
async def read_lessons_by_discipline_and_level(
    discipline_id: int,
    lesson_level_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    lessons = await service.get_lessons_by_discipline_and_lesson_level(db, lesson_level_id, discipline_id)
    if lessons is None:
        raise HTTPException(status_code=404, detail="Lessons not found")
    return lessons


@router.get("/lessons/level/{lesson_level_id}", response_model=List[Lesson])
async def read_lessons_by_level(
    lesson_level_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LessonService = Depends(get_lesson_service)
):
    lessons = await service.get_lessons_by_lesson_level(db, lesson_level_id)
    if lessons is None:
        raise HTTPException(status_code=404, detail="Lessons not found")
    return lessons