from typing import List

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.discipline import Discipline, DisciplineCreate, DisciplineUpdate
from services.discipline import DisciplineService
from repositories.discipline import DisciplineRepository
from db.session import get_async_session


router = APIRouter()


def get_discipline_service() -> DisciplineService:
    return DisciplineService(repository=DisciplineRepository())


@router.post("/disciplines/", response_model=Discipline)
async def create_discipline(
    discipline_create: DisciplineCreate,
    db: AsyncSession = Depends(get_async_session),
    service: DisciplineService = Depends(get_discipline_service)
):
    return await service.create_discipline(db, discipline_create)


@router.get("/disciplines/{discipline_id}", response_model=Discipline)
async def read_discipline(
    discipline_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: DisciplineService = Depends(get_discipline_service)
):
    db_discipline = await service.get_discipline(db, discipline_id)
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return db_discipline


@router.put("/disciplines/{discipline_id}", response_model=Discipline)
async def update_discipline(
    discipline_id: int, 
    discipline_update: DisciplineUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: DisciplineService = Depends(get_discipline_service)
):
    updated_discipline = await service.update_discipline(db, discipline_id, discipline_update)
    if updated_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return updated_discipline


@router.delete("/disciplines/{discipline_id}", response_model=Discipline)
async def delete_discipline(
    discipline_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: DisciplineService = Depends(get_discipline_service)
):
    success = await service.delete_discipline(db, discipline_id)
    if not success:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return success


@router.get("/disciplines/", response_model=List[Discipline])
async def read_disciplines(
    db: AsyncSession = Depends(get_async_session),
    service: DisciplineService = Depends(get_discipline_service)
):
    result = await service.get_all_disciplines(db)
    if result is None:
        raise HTTPException(status_code=404, detail="Disciplines not found")
    return result