from typing import List, Optional

from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from repositories.question import QuestionRepository
from schemas.question import QuestionCreate, QuestionUpdate, Question


class QuestionService:

    def __init__(self, repository: QuestionRepository):
        self.repository = repository
    
    async def create_question(self, db: AsyncSession, question_create: QuestionCreate) -> Question:
        result = await self.repository.create(db, question_create)
        await self.invalidate_cache()
        return Question.model_validate(result)
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_question(self, db: AsyncSession, question_id: int) -> Optional[Question]:
        result = await self.repository.get(db, question_id)
        return Question.model_validate(result) if result else None
    
    async def update_question(self, db: AsyncSession, question_id: int, question_update: QuestionUpdate) -> Optional[Question]:
        result = await self.repository.update(db, question_id, question_update)
        await self.invalidate_cache()
        return Question.model_validate(result) if result else None
    
    async def delete_question(self, db: AsyncSession, question_id: int) -> Optional[Question]:
        result = await self.repository.delete(db, question_id)
        await self.invalidate_cache()
        return result
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_all_questions(self, db: AsyncSession) -> List[Question]:
        result = await self.repository.get_all(db)
        return [Question.model_validate(question) for question in result]
    
    @cache(expire=settings.CACHE_EXPIRE_IN_SECONDS)
    async def get_questions_by_subject(self, db: AsyncSession, subject_id: int) -> List[Question]:
        result = await self.repository.get_by_subject_id(db, subject_id)
        return [Question.model_validate(question) for question in result]
    
    async def invalidate_cache(self):
        # Метод для очистки кэша
        await FastAPICache.clear()