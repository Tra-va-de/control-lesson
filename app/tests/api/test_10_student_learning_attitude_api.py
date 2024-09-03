import pytest

from httpx import AsyncClient

from tests.api.fixtures import create_student, create_learning_attitude


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_student_learning_attitude(client: AsyncClient, create_student: int, create_learning_attitude: int):
    student_id, learning_attitude_id = create_student, create_learning_attitude

    # создание оценки
    data = {
        "student_id": student_id,
        "learning_attitude_id": learning_attitude_id,
        "rating": 1
    }
    response = await client.post("/api/v1/student-learning-attitudes/", json=data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id
    assert data["learning_attitude_id"] == learning_attitude_id
    assert data["rating"] == 1


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_student_learning_attitude(client: AsyncClient, create_student: int, create_learning_attitude: int):
    student_id, learning_attitude_id = create_student, create_learning_attitude
    response = await client.get("/api/v1/student-learning-attitudes/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id
    assert data["learning_attitude_id"] == learning_attitude_id
    assert data["rating"] == 1


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_student_learning_attitude(client: AsyncClient, create_student: int, create_learning_attitude: int):
    student_id, learning_attitude_id = create_student, create_learning_attitude

    update_data = {
        "student_id": student_id,
        "learning_attitude_id": learning_attitude_id,
        "rating": 2
    }
    response = await client.put("/api/v1/student-learning-attitudes/1", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == update_data["student_id"]
    assert data["learning_attitude_id"] == update_data["learning_attitude_id"]
    assert data["rating"] == update_data["rating"]


@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_student_learning_attitudes(client: AsyncClient):
    response = await client.get("/api/v1/student-learning-attitudes/")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
@pytest.mark.order(5)
async def test_get_student_learning_attitudes_by_student(client: AsyncClient, create_student: int):
    student_id = create_student
    response = await client.get(f"/api/v1/student-learning-attitudes/student/{student_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id
    assert data["rating"] == 2


@pytest.mark.asyncio
@pytest.mark.order(6)
async def test_get_student_learning_attitudes_by_learning_attitude(client: AsyncClient, create_learning_attitude: int):
    learning_attitude_id = create_learning_attitude
    response = await client.get(f"/api/v1/student-learning-attitudes/learning-attitude/{learning_attitude_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["learning_attitude_id"] == learning_attitude_id
    assert data["rating"] == 2


@pytest.mark.asyncio
@pytest.mark.order(7)
async def test_get_student_learning_attitude_by_student_and_learning_attitude(client: AsyncClient, create_student: int, create_learning_attitude: int):
    student_id, learning_attitude_id = create_student, create_learning_attitude
    response = await client.get(f"/api/v1/student-learning-attitudes/student-and-learning-attitude/{student_id}/{learning_attitude_id}")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id
    assert data["learning_attitude_id"] == learning_attitude_id
    assert data["rating"] == 2


@pytest.mark.asyncio
@pytest.mark.order(8)
async def test_create_or_update_student_learning_attitude_before_delete(client: AsyncClient, create_student: int, create_learning_attitude: int):
    student_id, learning_attitude_id = create_student, create_learning_attitude
    print(f"student_id: {student_id}, learning_attitude_id: {learning_attitude_id}")

    update_data = {
        "student_id": student_id,
        "learning_attitude_id": learning_attitude_id,
        "rating": 5
    }

    response = await client.post("/api/v1/student-learning-attitudes/create-or-update/", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == update_data["student_id"]
    assert data["learning_attitude_id"] == update_data["learning_attitude_id"]
    assert data["rating"] == update_data["rating"]


@pytest.mark.asyncio
@pytest.mark.order(9)
async def test_delete_student_learning_attitude(client: AsyncClient, create_student: int, create_learning_attitude: int):
    student_id, learning_attitude_id = create_student, create_learning_attitude
    response = await client.delete("/api/v1/student-learning-attitudes/1")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["student_id"] == student_id
    assert data["learning_attitude_id"] == learning_attitude_id
    assert data["rating"] == 5


@pytest.mark.asyncio
@pytest.mark.order(10)
async def test_create_or_update_student_learning_attitude_after_delete(client: AsyncClient, create_student: int, create_learning_attitude: int):
    student_id, learning_attitude_id = create_student, create_learning_attitude
    print(f"student_id: {student_id}, learning_attitude_id: {learning_attitude_id}")

    update_data = {
        "student_id": student_id,
        "learning_attitude_id": learning_attitude_id,
        "rating": 4
    }

    response = await client.post("/api/v1/student-learning-attitudes/create-or-update/", json=update_data)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == update_data["student_id"]
    assert data["learning_attitude_id"] == update_data["learning_attitude_id"]
    assert data["rating"] == update_data["rating"]


@pytest.mark.asyncio
@pytest.mark.order(11)
async def test_get_non_existent_student_learning_attitude(client: AsyncClient):
    response = await client.get("/api/v1/student-learning-attitudes/999")
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Student learning attitude not found"}