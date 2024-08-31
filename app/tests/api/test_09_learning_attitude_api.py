import pytest

from httpx import AsyncClient


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_learning_attitude(client: AsyncClient):
    learning_attitude_data = {"name": "Успеваемость"}
    response = await client.post("/api/v1/learning-attitudes/", json=learning_attitude_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == learning_attitude_data["name"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_learning_attitude(client: AsyncClient):
    response = await client.get("/api/v1/learning-attitudes/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Успеваемость"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_learning_attitude(client: AsyncClient):
    update_data = {"name": "Интерес"}
    response = await client.put("/api/v1/learning-attitudes/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Интерес"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_delete_learning_attitude(client: AsyncClient):
    response = await client.delete("/api/v1/learning-attitudes/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Интерес"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_non_existent_learning_attitude(client: AsyncClient):
    response = await client.get("/api/v1/learning-attitudes/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Learning attitude not found"}