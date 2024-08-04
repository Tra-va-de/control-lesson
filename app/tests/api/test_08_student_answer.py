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
async def test_get_student_answer_by_student(client: AsyncClient, create_student: int):
    student_id = create_student
    print(f"student_id: {student_id}")
    response = await client.get(f"/api/v1/student-answers/student/{student_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_get_student_answer_by_question(client: AsyncClient, create_question: int):
    question_id = create_question
    print(f"question_id: {question_id}")
    response = await client.get(f"/api/v1/student-answers/question/{question_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.asyncio
@pytest.mark.order(7)
async def test_create_or_update_student_answer_before_delete(client: AsyncClient, create_question: int, create_student: int):
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
@pytest.mark.order(8)
async def test_delete_student_answer(client: AsyncClient):
    response = await client.delete("/api/v1/student-answers/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(9)
async def test_create_or_update_student_answer_after_delete(client: AsyncClient, create_question: int, create_student: int):
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
@pytest.mark.order(10)
async def test_read_student_answers_by_student_id(client: AsyncClient, create_student: int):
    student_id = create_student
    print(f"student_id: {student_id}")
    response = await client.get(f"/api/v1/student-answers/student/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for student_answer in data:
        assert student_answer["student_id"] == student_id


@pytest.mark.asyncio
@pytest.mark.order(11)
async def test_read_student_answers_by_question_id(client: AsyncClient, create_question: int):
    question_id = create_question
    print(f"question_id: {question_id}")
    response = await client.get(f"/api/v1/student-answers/question/{question_id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for student_answer in data:
        assert student_answer["question_id"] == question_id


@pytest.mark.asyncio
@pytest.mark.order(12)
async def test_read_student_answer_by_student_and_question_id(client: AsyncClient, create_student: int, create_question: int):
    student_id = create_student
    print(f"student_id: {student_id}")
    question_id = create_question
    print(f"question_id: {question_id}")
    response = await client.get(f"/api/v1/student-answers/student-and-question/{student_id}/{question_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id
    assert data["question_id"] == question_id


@pytest.mark.asyncio
@pytest.mark.order(13)
async def test_get_non_existent_student_answer(client: AsyncClient):
    response = await client.get("/api/v1/student-answers/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Student answer not found"}
