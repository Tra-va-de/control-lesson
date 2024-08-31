from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.student_learning_attitude import StudentLearningAttitude, StudentLearningAttitudeCreate, StudentLearningAttitudeUpdate
from services.student_learning_attitude import StudentLearningAttitudeService
from repositories.student_learning_attitude import StudentLearningAttitudeRepository
from db.session import get_async_session


router = APIRouter()


async def get_student_learning_attitude_service() -> StudentLearningAttitudeService:
    return StudentLearningAttitudeService(repository=StudentLearningAttitudeRepository())


@router.post("/student-learning-attitudes/", response_model=StudentLearningAttitude)
async def create_student_learning_attitude(
    student_learning_attitude: StudentLearningAttitudeCreate,
    db: AsyncSession = Depends(get_async_session),
    service: StudentLearningAttitudeService = Depends(get_student_learning_attitude_service)
):
    return await service.create_student_learning_attitude(db, student_learning_attitude)


@router.get("/student-learning-attitudes/{student_learning_attitude_id}", response_model=StudentLearningAttitude)
async def read_student_learning_attitude(
    student_learning_attitude_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentLearningAttitudeService = Depends(get_student_learning_attitude_service)
):
    db_student_learning_attitude = await service.get_student_learning_attitude(db, student_learning_attitude_id)
    if db_student_learning_attitude is None:
        raise HTTPException(status_code=404, detail="Student learning attitude not found")
    return db_student_learning_attitude


@router.put("/student-learning-attitudes/{student_learning_attitude_id}", response_model=StudentLearningAttitude)
async def update_student_learning_attitude(
    student_learning_attitude_id: int,
    updates: StudentLearningAttitudeUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: StudentLearningAttitudeService = Depends(get_student_learning_attitude_service)
):
    db_student_learning_attitude = await service.update_student_learning_attitude(db, student_learning_attitude_id, updates)
    if db_student_learning_attitude is None:
        raise HTTPException(status_code=404, detail="Student learning attitude not found")
    return db_student_learning_attitude


@router.delete("/student-learning-attitudes/{student_learning_attitude_id}", response_model=StudentLearningAttitude)
async def delete_student_learning_attitude(
    student_learning_attitude_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentLearningAttitudeService = Depends(get_student_learning_attitude_service)
):
    db_student_learning_attitude = await service.delete_student_learning_attitude(db, student_learning_attitude_id)
    if db_student_learning_attitude is None:
        raise HTTPException(status_code=404, detail="Student learning attitude not found")
    return db_student_learning_attitude


@router.get("/student-learning-attitudes/", response_model=List[StudentLearningAttitude])
async def read_student_learning_attitudes(
    db: AsyncSession = Depends(get_async_session),
    service: StudentLearningAttitudeService = Depends(get_student_learning_attitude_service)
):
    student_learning_attitudes = await service.get_all_student_learning_attitudes(db)
    if student_learning_attitudes is None:
        raise HTTPException(status_code=404, detail="Student learning attitudes not found")
    return student_learning_attitudes


@router.get("/student-learning-attitudes/student/{student_id}", response_model=List[StudentLearningAttitude])
async def read_student_learning_attitudes_by_student(
    student_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentLearningAttitudeService = Depends(get_student_learning_attitude_service)
):
    student_learning_attitudes = await service.get_student_learning_attitudes_by_student_id(db, student_id)
    if student_learning_attitudes is None:
        raise HTTPException(status_code=404, detail="Student learning attitudes not found")
    return student_learning_attitudes


@router.get("/student-learning-attitudes/learning-attitude/{learning_attitude_id}", response_model=List[StudentLearningAttitude])
async def read_student_learning_attitudes_by_learning_attitude(
    learning_attitude_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentLearningAttitudeService = Depends(get_student_learning_attitude_service)
):
    student_learning_attitudes = await service.get_student_learning_attitudes_by_learning_attitude_id(db, learning_attitude_id)
    if student_learning_attitudes is None:
        raise HTTPException(status_code=404, detail="Student learning attitudes not found")
    return student_learning_attitudes