from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete as sqlalchemy_delete

from models.student_answer import StudentAnswer
from schemas.student_answer import StudentAnswerCreate, StudentAnswerUpdate, StudentAnswerCreateOrUpdate


class StudentAnswerRepository:

    async def create(self, db: AsyncSession, student_answer: StudentAnswerCreate) -> StudentAnswer:
        db_student_answer = StudentAnswer(
            student_id = student_answer.student_id,
            question_id = student_answer.question_id,
            answer = student_answer.answer
        )
        db.add(db_student_answer)
        await db.commit()
        await db.refresh(db_student_answer)
        return db_student_answer

    async def get(self, db: AsyncSession, student_answer_id: int) -> Optional[StudentAnswer]:
        result = await db.execute(select(StudentAnswer).filter(StudentAnswer.id == student_answer_id))
        return result.scalars().first()

    async def update(self, db: AsyncSession, student_answer_id: int, student_answer_update: StudentAnswerUpdate) -> Optional[StudentAnswer]:
        result = await db.execute(select(StudentAnswer).filter(StudentAnswer.id == student_answer_id))
        db_student_answer = result.scalars().first()
        if not db_student_answer:
            return None
        for var, value in vars(student_answer_update).items():
            setattr(db_student_answer, var, value) if value is not None else None
        db.add(db_student_answer)
        await db.commit()
        await db.refresh(db_student_answer)
        return db_student_answer

    async def delete(self, db: AsyncSession, student_answer_id: int) -> Optional[StudentAnswer]:
        result = await db.execute(select(StudentAnswer).filter(StudentAnswer.id == student_answer_id))
        db_student_answer = result.scalars().first()
        if not db_student_answer:
            return None
        await db.execute(sqlalchemy_delete(StudentAnswer).where(StudentAnswer.id == student_answer_id))
        await db.commit()
        return db_student_answer

    async def get_all(self, db: AsyncSession) -> List[StudentAnswer]:
        result = await db.execute(select(StudentAnswer))
        return result.scalars().all()
    
    async def get_by_student_id(self, db: AsyncSession, student_id: int) -> List[StudentAnswer]:
        result = await db.execute(select(StudentAnswer).where(StudentAnswer.student_id == student_id))
        return result.scalars().all()
    
    async def get_by_question_id(self, db: AsyncSession, question_id: int) -> List[StudentAnswer]:
        result = await db.execute(select(StudentAnswer).where(StudentAnswer.question_id == question_id))
        return result.scalars().all()
    
    async def get_by_student_and_question_id(self, db: AsyncSession, student_id: int, question_id: int) -> Optional[StudentAnswer]:
        result = await db.execute(select(StudentAnswer).where(
            (StudentAnswer.student_id == student_id) &
            (StudentAnswer.question_id == question_id)
        ))
        return result.scalars().first()
    
    async def create_or_update(self, db: AsyncSession, student_answer: StudentAnswerCreateOrUpdate) -> StudentAnswer:
        # Поиск существующей записи
        query = select(StudentAnswer).where(
            (StudentAnswer.student_id == student_answer.student_id) &
            (StudentAnswer.question_id == student_answer.question_id)
        )
        result = await db.execute(query)
        existing_answer = result.scalar_one_or_none()

        if existing_answer:
            # Обновление существующей записи
            for key, value in vars(student_answer).items():
                setattr(existing_answer, key, value)
            await db.commit()
            await db.refresh(existing_answer)
            return existing_answer
        else:
            # Создание новой записи
            new_answer = StudentAnswer(
                student_id = student_answer.student_id,
                question_id = student_answer.question_id,
                answer = student_answer.answer
            )
            db.add(new_answer)
            await db.commit()
            await db.refresh(new_answer)
            return new_answer
