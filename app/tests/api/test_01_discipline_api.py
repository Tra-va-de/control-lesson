import pytest

from httpx import AsyncClient


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_discipline(client: AsyncClient):
    discipline_data = {"name": "Biology"}
    response = await client.post("/api/v1/disciplines/", json=discipline_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == discipline_data["name"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_discipline(client: AsyncClient):
    response = await client.get("/api/v1/disciplines/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Biology"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_discipline(client: AsyncClient):
    update_data = {"name": "Advanced Biology"}
    response = await client.put("/api/v1/disciplines/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Advanced Biology"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_delete_discipline(client: AsyncClient):
    # Сначала получаем все уроки, связанные с этой дисциплиной
    lessons_response = await client.get(f"/api/v1/lessons/discipline/1")
    assert lessons_response.status_code == 200
    lessons = lessons_response.json()

    # Удаляем каждый связанный урок
    for lesson in lessons:
        lesson_id = lesson["id"]
        await client.delete(f"/api/v1/lessons/{lesson_id}")

    # Удаление самой дисциплины
    response = await client.delete("/api/v1/disciplines/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Advanced Biology"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_non_existent_discipline(client: AsyncClient):
    response = await client.get("/api/v1/disciplines/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Discipline not found"}