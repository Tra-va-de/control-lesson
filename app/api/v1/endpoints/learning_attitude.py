from typing import List

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.learning_attitude import LearningAttitude, LearningAttitudeCreate, LearningAttitudeUpdate
from services.learning_attitude import LearningAttitudeService
from repositories.learning_attitude import LearningAttitudeRepository
from db.session import get_async_session


router = APIRouter()


def get_learning_attitude_service() -> LearningAttitudeService:
    return LearningAttitudeService(repository=LearningAttitudeRepository())


@router.post("/learning-attitudes/", response_model=LearningAttitude)
async def create_learning_attitude(
    learning_attitude_create: LearningAttitudeCreate,
    db: AsyncSession = Depends(get_async_session),
    service: LearningAttitudeService = Depends(get_learning_attitude_service)
):
    return await service.create_learning_attitude(db, learning_attitude_create)


@router.get("/learning-attitudes/{learning_attitude_id}", response_model=LearningAttitude)
async def read_learning_attitude(
    learning_attitude_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LearningAttitudeService = Depends(get_learning_attitude_service)
):
    db_learning_attitude = await service.get_learning_attitude(db, learning_attitude_id)
    if db_learning_attitude is None:
        raise HTTPException(status_code=404, detail="Learning attitude not found")
    return db_learning_attitude


@router.put("/learning-attitudes/{learning_attitude_id}", response_model=LearningAttitude)
async def update_learning_attitude(
    learning_attitude_id: int, 
    learning_attitude_update: LearningAttitudeUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: LearningAttitudeService = Depends(get_learning_attitude_service)
):
    updated_learning_attitude = await service.update_learning_attitude(db, learning_attitude_id, learning_attitude_update)
    if updated_learning_attitude is None:
        raise HTTPException(status_code=404, detail="Learning attitude not found")
    return updated_learning_attitude


@router.delete("/learning-attitudes/{learning_attitude_id}", response_model=LearningAttitude)
async def delete_learning_attitude(
    learning_attitude_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: LearningAttitudeService = Depends(get_learning_attitude_service)
):
    success = await service.delete_learning_attitude(db, learning_attitude_id)
    if not success:
        raise HTTPException(status_code=404, detail="Learning attitude not found")
    return success


@router.get("/learning-attitudes/", response_model=List[LearningAttitude])
async def read_learning_attitudes(
    db: AsyncSession = Depends(get_async_session),
    service: LearningAttitudeService = Depends(get_learning_attitude_service)
):
    result = await service.get_all_learning_attitudes(db)
    if result is None:
        raise HTTPException(status_code=404, detail="Learning attitudes not found")
    return result