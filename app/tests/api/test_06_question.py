import pytest

from httpx import AsyncClient

from tests.api.fixtures import create_subject, create_category_and_lesson, create_discipline_and_lesson_level


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_question(client: AsyncClient, create_subject: int):
    subject_id = create_subject
    print(f"subject_id: {subject_id}")

    question = {
        "text": "Test question",
        "answer": "Test answer",
        "subject_id": subject_id
    }
    response = await client.post("/api/v1/questions/", json=question)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == question["text"]
    assert data["answer"] == question["answer"]
    assert data["subject_id"] == question["subject_id"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_question(client: AsyncClient):
    response = await client.get("/api/v1/questions/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Test question"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_question(client: AsyncClient, create_subject: int):
    subject_id = create_subject

    update_question = {
        "text": "Updated Test question",
        "answer": "Updated Test answer",
        "subject_id": subject_id
    }
    response = await client.put("/api/v1/questions/1", json=update_question)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == update_question["text"]
    assert data["answer"] == update_question["answer"]
    assert data["subject_id"] == update_question["subject_id"]


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_questions(client: AsyncClient):
    response = await client.get("/api/v1/questions/")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_question_by_subject(client: AsyncClient, create_subject: int):
    subject_id = create_subject
    response = await client.get(f"/api/v1/questions/subject/{subject_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_delete_question(client: AsyncClient):
    response = await client.delete("/api/v1/questions/1")
    print("Response status:", response.status_code)
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Updated Test question"
    assert data["answer"] == "Updated Test answer"
    assert data["id"] == 1