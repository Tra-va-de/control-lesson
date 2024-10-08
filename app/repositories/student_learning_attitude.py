from typing import Optional, List

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.student_learning_attitude import StudentLearningAttitude
from schemas.student_learning_attitude import StudentLearningAttitudeCreate, \
                                              StudentLearningAttitudeCreateOrUpdate, \
                                              StudentLearningAttitudeUpdate


class StudentLearningAttitudeRepository:
    
    async def create(self, db: AsyncSession, student_learning_attitude: StudentLearningAttitudeCreate) -> StudentLearningAttitude:
        db_student_learning_attitude = StudentLearningAttitude(
            student_id=student_learning_attitude.student_id,
            learning_attitude_id=student_learning_attitude.learning_attitude_id,
            rating=student_learning_attitude.rating
        )
        db.add(db_student_learning_attitude)
        await db.commit()
        await db.refresh(db_student_learning_attitude)
        return db_student_learning_attitude

    async def get(self, db: AsyncSession, student_learning_attitude_id: int) -> Optional[StudentLearningAttitude]:
        result = await db.execute(select(StudentLearningAttitude).filter(StudentLearningAttitude.id == student_learning_attitude_id))
        return result.scalars().first()

    async def update(self, db: AsyncSession, student_learning_attitude_id: int, student_learning_attitude_update: StudentLearningAttitudeUpdate) -> Optional[StudentLearningAttitude]:
        result = await db.execute(select(StudentLearningAttitude).filter(StudentLearningAttitude.id == student_learning_attitude_id))
        db_student_learning_attitude = result.scalars().first()
        if not db_student_learning_attitude:
            return None
        for var, value in vars(student_learning_attitude_update).items():
            setattr(db_student_learning_attitude, var, value) if value else None
        db.add(db_student_learning_attitude)
        await db.commit()
        await db.refresh(db_student_learning_attitude)
        return db_student_learning_attitude

    async def delete(self, db: AsyncSession, student_learning_attitude_id: int) -> Optional[StudentLearningAttitude]:
        result = await db.execute(select(StudentLearningAttitude).filter(StudentLearningAttitude.id == student_learning_attitude_id))
        db_student_learning_attitude = result.scalars().first()
        if not db_student_learning_attitude:
            return None
        await db.execute(sqlalchemy_delete(StudentLearningAttitude).where(StudentLearningAttitude.id == student_learning_attitude_id))
        await db.commit()
        return db_student_learning_attitude

    async def get_all(self, db: AsyncSession) -> List[StudentLearningAttitude]:
        result = await db.execute(select(StudentLearningAttitude))
        return result.scalars().all()

    async def get_by_student_id(self, db: AsyncSession, student_id: int) -> StudentLearningAttitude:
        result = await db.execute(select(StudentLearningAttitude).filter(StudentLearningAttitude.student_id == student_id))
        return result.scalars().first()

    async def get_by_learning_attitude_id(self, db: AsyncSession, learning_attitude_id: int) -> StudentLearningAttitude:
        result = await db.execute(select(StudentLearningAttitude).filter(StudentLearningAttitude.learning_attitude_id == learning_attitude_id))
        return result.scalars().first()
    
    async def get_by_student_id_and_learning_attitude_id(self, db: AsyncSession, student_id: int, learning_attitude_id: int) -> StudentLearningAttitude:
        result = await db.execute(select(StudentLearningAttitude).filter(StudentLearningAttitude.student_id == student_id, StudentLearningAttitude.learning_attitude_id == learning_attitude_id))
        return result.scalars().first()
    
    async def create_or_update(self, db: AsyncSession, student_answer: StudentLearningAttitudeCreateOrUpdate) -> StudentLearningAttitude:
        # Поиск существующей записи
        query = select(StudentLearningAttitude).where(
            (StudentLearningAttitude.student_id == student_answer.student_id) &
            (StudentLearningAttitude.learning_attitude_id == student_answer.learning_attitude_id)
        )
        result = await db.execute(query)
        existing_result = result.scalar_one_or_none()

        if existing_result:
            # Обновление существующей записи
            for key, value in vars(student_answer).items():
                setattr(existing_result, key, value)
            await db.commit()
            await db.refresh(existing_result)
            return existing_result
        else:
            # Создание новой записи
            new_result = StudentLearningAttitude(
                student_id = student_answer.student_id,
                learning_attitude_id = student_answer.learning_attitude_id,
                rating = student_answer.rating
            )
            db.add(new_result)
            await db.commit()
            await db.refresh(new_result)
            print("Создали новую запись при попытке обновления")
            return new_result