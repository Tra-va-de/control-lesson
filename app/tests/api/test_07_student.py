import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_student(client: AsyncClient):
    student_data = {
        "first_name": "Иван",
        "last_name": "Петров",
        "date_of_birth": "2000-01-01"
    }
    response = await client.post("/api/v1/students/", json=student_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == student_data["first_name"]
    assert data["last_name"] == student_data["last_name"]
    assert data["date_of_birth"] == student_data["date_of_birth"]


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_student(client: AsyncClient):
    response = await client.get("/api/v1/students/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Иван"
    assert data["last_name"] == "Петров"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_student(client: AsyncClient):
    update_data = {
        "first_name": "Александр",
        "last_name": "Иванов",
        "date_of_birth": "2001-02-02"
    }
    response = await client.put("/api/v1/students/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Александр"
    assert data["last_name"] == "Иванов"
    assert data["date_of_birth"] == "2001-02-02"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_students(client: AsyncClient):
    response = await client.get("/api/v1/students/")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_delete_student(client: AsyncClient):
    response = await client.delete("/api/v1/students/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Александр"
    assert data["last_name"] == "Иванов"
    assert data["date_of_birth"] == "2001-02-02"
    assert data["id"] == 1


@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_get_non_existent_student(client: AsyncClient):
    response = await client.get("/api/v1/students/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}
