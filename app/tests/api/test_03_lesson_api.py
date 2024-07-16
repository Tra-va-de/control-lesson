import pytest

from httpx import AsyncClient

from tests.api.fixtures import create_discipline_and_lesson_level


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_lesson(client: AsyncClient, create_discipline_and_lesson_level: tuple[int, int]):
    discipline_id, level_id = create_discipline_and_lesson_level

    # создание урока
    data = {
        "name": "Introduction to Python",
        "discipline_id": discipline_id,
        "lesson_level_id": level_id
    }
    lesson_response = await client.post("/api/v1/lessons/", json=data)
    print("Response status:", lesson_response.status_code)
    print("Response JSON:", lesson_response.json())
    assert lesson_response.status_code == 200
    lesson_data = lesson_response.json()
    assert lesson_data["name"] == data["name"]
    assert lesson_data["discipline_id"] == data["discipline_id"]
    assert lesson_data["lesson_level_id"] == data["lesson_level_id"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_lesson(client: AsyncClient):
    response = await client.get("/api/v1/lessons/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Introduction to Python"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_lesson(client: AsyncClient, create_discipline_and_lesson_level: tuple[int, int]):
    discipline_id, level_id = create_discipline_and_lesson_level

    update_data = {
        "name": "Advanced Python Concepts",
        "discipline_id": discipline_id,
        "lesson_level_id": level_id
    }
    response = await client.put("/api/v1/lessons/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["discipline_id"] == update_data["discipline_id"]
    assert data["lesson_level_id"] == update_data["lesson_level_id"]


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_lessons(client: AsyncClient):
    response = await client.get("/api/v1/lessons/")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_lessons_by_discipline(client: AsyncClient, create_discipline_and_lesson_level: tuple[int, int]):
    discipline_id, _ = create_discipline_and_lesson_level
    response = await client.get(f"/api/v1/lessons/discipline/{discipline_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_get_lessons_by_level(client: AsyncClient, create_discipline_and_lesson_level: tuple[int, int]):
    _, level_id = create_discipline_and_lesson_level
    response = await client.get(f"/api/v1/lessons/level/{level_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
@pytest.mark.order(7)
async def test_get_lessons_by_discipline_and_level(client: AsyncClient, create_discipline_and_lesson_level: tuple[int, int]):
    discipline_id, level_id = create_discipline_and_lesson_level
    response = await client.get(f"/api/v1/lessons/discipline/{discipline_id}/level/{level_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
@pytest.mark.order(8)
async def test_get_non_existent_lesson(client: AsyncClient):
    response = await client.get("/api/v1/lessons/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Lesson not found"}


@pytest.mark.asyncio
@pytest.mark.order(9)
async def test_delete_lesson(client: AsyncClient):
    response = await client.delete("/api/v1/lessons/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Advanced Python Concepts"
    assert data["id"] == 1