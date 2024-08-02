import pytest

from httpx import AsyncClient

from tests.api.fixtures import create_category_and_lesson, create_discipline_and_lesson_level, create_subject, create_question, create_student


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_student_answer(client: AsyncClient, create_question: int, create_student: int):
    # Создание вопроса и студента
    question_id = create_question
    student_id = create_student
    print(f"question_id: {question_id}, student_id: {student_id}")

    student_answer_data = {
        "student_id": student_id,
        "question_id": question_id,
        "answer": 0
    }
    response = await client.post("/api/v1/student-answers/", json=student_answer_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_answer_data["student_id"]
    assert data["question_id"] == student_answer_data["question_id"]
    assert data["answer"] == student_answer_data["answer"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_student_answer(client: AsyncClient):
    response = await client.get("/api/v1/student-answers/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == 0
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_student_answer(client: AsyncClient, create_question: int, create_student: int):
    # Создание вопроса и студента
    question_id = create_question
    student_id = create_student
    print(f"question_id: {question_id}, student_id: {student_id}")

    update_data = {
        "student_id": student_id,
        "question_id": question_id,
        "answer": 0.5
    }
    response = await client.put("/api/v1/student-answers/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == update_data["student_id"]
    assert data["question_id"] == update_data["question_id"]
    assert data["answer"] == update_data["answer"]


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_student_answers(client: AsyncClient):
    response = await client.get("/api/v1/student-answers/")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_delete_student_answer(client: AsyncClient):
    response = await client.delete("/api/v1/student-answers/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_get_non_existent_student_answer(client: AsyncClient):
    response = await client.get("/api/v1/student-answers/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Student answer not found"}
