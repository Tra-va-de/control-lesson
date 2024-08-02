from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.student_answer import StudentAnswer, StudentAnswerCreate, StudentAnswerUpdate
from services.student_answer import StudentAnswerService
from repositories.student_answer import StudentAnswerRepository
from db.session import get_async_session


router = APIRouter()


def get_student_answer_service() -> StudentAnswerService:
    return StudentAnswerService(repository=StudentAnswerRepository())


@router.post("/student-answers/", response_model=StudentAnswer)
async def create_student_answer(
    student_answer_create: StudentAnswerCreate,
    db: AsyncSession = Depends(get_async_session),
    service: StudentAnswerService = Depends(get_student_answer_service)
):
    return await service.create_student_answer(db, student_answer_create)


@router.get("/student-answers/{student_answer_id}", response_model=StudentAnswer)
async def read_student_answer(
    student_answer_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentAnswerService = Depends(get_student_answer_service)
):
    student_answer = await service.get_student_answer(db, student_answer_id)
    if student_answer is None:
        raise HTTPException(status_code=404, detail="Student answer not found")
    return student_answer


@router.put("/student-answers/{student_answer_id}", response_model=StudentAnswer)
async def update_student_answer(
    student_answer_id: int,
    student_answer_update: StudentAnswerUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: StudentAnswerService = Depends(get_student_answer_service)
):
    updated_student_answer = await service.update_student_answer(db, student_answer_id, student_answer_update)
    if updated_student_answer is None:
        raise HTTPException(status_code=404, detail="Student answer not found")
    return updated_student_answer


@router.delete("/student-answers/{student_answer_id}", response_model=StudentAnswer)
async def delete_student_answer(
    student_answer_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentAnswerService = Depends(get_student_answer_service)
):
    student_answer = await service.delete_student_answer(db, student_answer_id)
    if student_answer is None:
        raise HTTPException(status_code=404, detail="Student answer not found")
    return student_answer


@router.get("/student-answers/", response_model=List[StudentAnswer])
async def read_student_answers(
    db: AsyncSession = Depends(get_async_session),
    service: StudentAnswerService = Depends(get_student_answer_service)
):
    result = await service.get_all_student_answers(db)
    if result is None:
        raise HTTPException(status_code=404, detail="Student answers not found")
    return result
