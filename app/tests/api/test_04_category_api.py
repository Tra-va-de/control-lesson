import pytest

from httpx import AsyncClient


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_category(client: AsyncClient):
    category_data = {"name": "Science"}
    response = await client.post("/api/v1/categories/", json=category_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == category_data["name"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_category(client: AsyncClient):
    response = await client.get("/api/v1/categories/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Science"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_category(client: AsyncClient):
    update_data = {"name": "Natural Sciences"}
    response = await client.put("/api/v1/categories/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Natural Sciences"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_delete_category(client: AsyncClient):
    response = await client.delete("/api/v1/categories/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Natural Sciences"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_non_existent_category(client: AsyncClient):
    response = await client.get("/api/v1/categories/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}