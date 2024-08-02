from typing import Optional

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.student import Student
from schemas.student import StudentCreate, StudentUpdate


class StudentRepository:

    async def create(self, db: AsyncSession, student: StudentCreate) -> Student:
        db_student = Student(
            first_name=student.first_name,
            last_name=student.last_name,
            date_of_birth=student.date_of_birth,
        )
        db.add(db_student)
        await db.commit()
        await db.refresh(db_student)
        return db_student

    async def get(self, db: AsyncSession, student_id: int) -> Optional[Student]:
        result = await db.execute(select(Student).filter(Student.id == student_id))
        return result.scalars().first()

    async def update(self, db: AsyncSession, student_id: int, student_update: StudentUpdate) -> Optional[Student]:
        result = await db.execute(select(Student).filter(Student.id == student_id))
        db_student = result.scalars().first()
        if not db_student:
            return None
        for var, value in vars(student_update).items():
            setattr(db_student, var, value) if value else None
        db.add(db_student)
        await db.commit()
        await db.refresh(db_student)
        return db_student

    async def delete(self, db: AsyncSession, student_id: int) -> Optional[Student]:
        result = await db.execute(select(Student).filter(Student.id == student_id))
        db_student = result.scalars().first()
        if not db_student:
            return None
        await db.execute(sqlalchemy_delete(Student).where(Student.id == student_id))
        await db.commit()
        return db_student

    async def get_all(self, db: AsyncSession) -> list[Student]:
        result = await db.execute(select(Student))
        return result.scalars().all()
