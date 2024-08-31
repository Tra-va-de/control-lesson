import pytest

from httpx import AsyncClient

from tests.api.fixtures import create_category_and_lesson, create_discipline_and_lesson_level  


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_subject(client: AsyncClient, create_category_and_lesson: tuple[int, int]):
    # Создание категории и урока
    category_id, lesson_id = create_category_and_lesson
    print(f"category_id: {category_id}, lesson_id: {lesson_id}")

    subject = {
        "name": "Test subject",
        "category_id": category_id,
        "lesson_id": lesson_id
    }
    response = await client.post("/api/v1/subjects/", json=subject)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == subject["name"]
    assert data["category_id"] == subject["category_id"]
    assert data["lesson_id"] == subject["lesson_id"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_subject(client: AsyncClient):
    response = await client.get("/api/v1/subjects/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test subject"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_subject(client: AsyncClient, create_category_and_lesson: tuple[int, int]):
    # Создание категории и урока
    category_id, lesson_id = create_category_and_lesson
    print(f"category_id: {category_id}, lesson_id: {lesson_id}")

    update_subject = {
        "name": "Updated Test subject",
        "category_id": category_id,
        "lesson_id": lesson_id
    }
    response = await client.put("/api/v1/subjects/1", json=update_subject)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_subject["name"]
    assert data["lesson_id"] == update_subject["lesson_id"]
    assert data["category_id"] == update_subject["category_id"]


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_subjects(client: AsyncClient):
    response = await client.get("/api/v1/subjects/")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_subjects_by_lesson(client: AsyncClient, create_category_and_lesson: tuple[int, int]):
    _, lesson_id = create_category_and_lesson
    response = await client.get(f"/api/v1/subjects/lesson/{lesson_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_get_subjects_by_category(client: AsyncClient, create_category_and_lesson: tuple[int, int]):
    category_id, _ = create_category_and_lesson
    response = await client.get(f"/api/v1/subjects/category/{category_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.order(7)
async def test_get_subjects_by_lesson_and_category(client: AsyncClient, create_category_and_lesson: tuple[int, int]):
    category_id, lesson_id = create_category_and_lesson
    response = await client.get(f"/api/v1/subjects/lesson/{lesson_id}/category/{category_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.order(8)
async def get_non_existent_subject(client: AsyncClient):
    response = await client.get("/api/v1/subjects/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Subject not found"}


@pytest.mark.asyncio
@pytest.mark.order(9)
async def test_delete_subject(client: AsyncClient):
    response = await client.delete("/api/v1/subjects/1")
    print("Response status:", response.status_code)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Test subject"
    assert data["id"] == 1