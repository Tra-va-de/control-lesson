from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.subject import SubjectCreate, SubjectUpdate, Subject
from services.subject import SubjectService
from repositories.subject import SubjectRepository
from db.session import get_async_session


router = APIRouter()


async def get_subject_service() -> SubjectService:
    return SubjectService(repository=SubjectRepository())


@router.post("/subjects/", response_model=Subject)
async def create_subject(
    subject: SubjectCreate,
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    return await service.create_subject(db, subject)


@router.get("/subjects/{subject_id}", response_model=Subject)
async def get_subject(
    subject_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    result = await service.get_subject(db, subject_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return result


@router.put("/subjects/{subject_id}", response_model=Subject)
async def update_subject(
    subject_id: int,
    subject_update: SubjectUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    result = await service.update_subject(db, subject_id, subject_update)
    if result is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return result


@router.delete("/subjects/{subject_id}", response_model=Subject)
async def delete_subject(
    subject_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    result = await service.delete_subject(db, subject_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return result


@router.get("/subjects/", response_model=List[Subject])
async def get_subjects(
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    result = await service.get_all_subjects(db)
    if result is None:
        raise HTTPException(status_code=404, detail="Subjects not found")
    return result


@router.get("/subjects/lesson/{lesson_id}", response_model=List[Subject])
async def get_subjects_by_lesson(
    lesson_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    result = await service.get_subjects_by_lesson(db, lesson_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Subjects not found")
    return result    


@router.get("/subjects/category/{category_id}", response_model=List[Subject])
async def get_subjects_by_category(
    category_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    result = await service.get_subjects_by_category(db, category_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Subjects not found")
    return result


@router.get("/subjects/lesson/{lesson_id}/category/{category_id}", response_model=List[Subject])
async def get_subjects_by_lesson_and_category(
    lesson_id: int,
    category_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: SubjectService = Depends(get_subject_service),
):
    result = await service.get_subjects_by_lesson_and_category(db, lesson_id, category_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Subjects not found")
    return result