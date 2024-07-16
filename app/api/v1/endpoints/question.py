from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.question import QuestionCreate, QuestionUpdate, Question
from services.question import QuestionService
from repositories.question import QuestionRepository
from db.session import get_async_session


router = APIRouter()


async def get_question_service() -> QuestionService:
    return QuestionService(repository=QuestionRepository())


@router.post("/questions/", response_model=Question)
async def create_question(
    question: QuestionCreate,
    db: AsyncSession = Depends(get_async_session),
    service: QuestionService = Depends(get_question_service),
):
    return await service.create_question(db, question)


@router.get("/questions/{question_id}", response_model=Question)
async def get_question(
    question_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: QuestionService = Depends(get_question_service),
):
    result = await service.get_question(db, question_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return result


@router.put("/questions/{question_id}", response_model=Question)
async def update_question(
    question_id: int,
    question_update: QuestionUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: QuestionService = Depends(get_question_service),
):
    result = await service.update_question(db, question_id, question_update)
    if result is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return result


@router.delete("/questions/{question_id}", response_model=Question)
async def delete_question(
    question_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: QuestionService = Depends(get_question_service),
):
    result = await service.delete_question(db, question_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return result


@router.get("/questions/", response_model=List[Question])
async def get_all_questions(
    db: AsyncSession = Depends(get_async_session),
    service: QuestionService = Depends(get_question_service),
):
    result = await service.get_all_questions(db)
    return result


@router.get("/questions/subject/{subject_id}", response_model=List[Question])
async def get_questions_by_subject(
    subject_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: QuestionService = Depends(get_question_service),
):
    result = await service.get_questions_by_subject(db, subject_id)
    return result