from typing import List

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.student import Student, StudentCreate, StudentUpdate
from services.student import StudentService
from repositories.student import StudentRepository
from db.session import get_async_session


router = APIRouter()


def get_student_service() -> StudentService:
    return StudentService(repository=StudentRepository())


@router.post("/students/", response_model=Student)
async def create_student(
    student_create: StudentCreate,
    db: AsyncSession = Depends(get_async_session),
    service: StudentService = Depends(get_student_service)
):
    return await service.create_student(db, student_create)


@router.get("/students/{student_id}", response_model=Student)
async def read_student(
    student_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentService = Depends(get_student_service)
):
    db_student = await service.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@router.put("/students/{student_id}", response_model=Student)
async def update_student(
    student_id: int, 
    student_update: StudentUpdate,
    db: AsyncSession = Depends(get_async_session),
    service: StudentService = Depends(get_student_service)
):
    updated_student = await service.update_student(db, student_id, student_update)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student


@router.delete("/students/{student_id}", response_model=Student)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_async_session),
    service: StudentService = Depends(get_student_service)
):
    success = await service.delete_student(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return success


@router.get("/students/", response_model=List[Student])
async def read_students(
    db: AsyncSession = Depends(get_async_session),
    service: StudentService = Depends(get_student_service)
):
    result = await service.get_all_students(db)
    if result is None:
        raise HTTPException(status_code=404, detail="Students not found")
    return result
