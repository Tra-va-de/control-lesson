import pytest

from httpx import AsyncClient


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_lesson_level(client: AsyncClient):
    lesson_level_data = {"name": "Beginner"}
    response = await client.post("/api/v1/lesson-levels/", json=lesson_level_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == lesson_level_data["name"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_lesson_level(client: AsyncClient):
    response = await client.get("/api/v1/lesson-levels/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Beginner"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_lesson_level(client: AsyncClient):
    update_data = {"name": "Intermediate"}
    response = await client.put("/api/v1/lesson-levels/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Intermediate"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_delete_lesson_level(client: AsyncClient):
    # Сначала получаем все уроки, связанные с этим уровнем
    lessons_response = await client.get(f"/api/v1/lessons/level/1")
    print("Response status:", lessons_response.status_code)
    print("Response JSON:", lessons_response.json())
    assert lessons_response.status_code == 200
    lessons = lessons_response.json()

    # Удаляем каждый связанный урок
    for lesson in lessons:
        lesson_id = lesson["id"]
        await client.delete(f"/api/v1/lessons/{lesson_id}")

    # Удаление самого уровня урока
    response = await client.delete("/api/v1/lesson-levels/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Intermediate"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_non_existent_lesson_level(client: AsyncClient):
    response = await client.get("/api/v1/lesson-levels/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Lesson level not found"}