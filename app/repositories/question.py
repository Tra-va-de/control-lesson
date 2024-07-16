from typing import List, Optional

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.question import Question
from schemas.question import QuestionCreate, QuestionUpdate


class QuestionRepository:
    
    async def create(self, db: AsyncSession, question: QuestionCreate) -> Question:
        db_question = Question(
            text=question.text,
            answer=question.answer,
            subject_id=question.subject_id
        )
        db.add(db_question)
        await db.commit()
        await db.refresh(db_question)
        return db_question

    async def get(self, db: AsyncSession, question_id: int) -> Optional[Question]:
        result = await db.execute(select(Question).filter(Question.id == question_id))
        return result.scalars().first()     
    
    async def update(self, db: AsyncSession, question_id: int, question_update: QuestionUpdate) -> Optional[Question]:
        result = await db.execute(select(Question).filter(Question.id == question_id))
        db_question = result.scalars().first()
        if not db_question:
            return None
        for var, value in vars(question_update).items():
            setattr(db_question, var, value) if value else None
        db.add(db_question)
        await db.commit()
        await db.refresh(db_question)
        return db_question
    
    async def delete(self, db: AsyncSession, question_id: int) -> Optional[Question]:
        result = await db.execute(select(Question).filter(Question.id == question_id))
        db_question = result.scalars().first()
        if not db_question:
            return None
        await db.execute(sqlalchemy_delete(Question).where(Question.id == question_id))
        await db.commit()
        return db_question
    
    async def get_all(self, db: AsyncSession) -> List[Question]:
        result = await db.execute(select(Question))
        return result.scalars().all()
    
    async def get_by_subject_id(self, db: AsyncSession, subject_id: int) -> List[Question]:
        result = await db.execute(select(Question).where(Question.subject_id == subject_id))
        return result.scalars().all()