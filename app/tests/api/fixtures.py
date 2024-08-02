import pytest

from httpx import AsyncClient


# Фикстуры создания дисциплины и уровня
@pytest.fixture(scope="session")
async def create_discipline_and_lesson_level(client: AsyncClient) -> tuple[int, int]:
    # Создание дисциплины
    discipline_response_data = {
        "name": "Computer Science"
    }
    discipline_response = await client.post("/api/v1/disciplines/", json=discipline_response_data)
    print("Response status:", discipline_response.status_code)
    print("Response JSON:", discipline_response.json())
    assert discipline_response.status_code == 200
    discipline_data = discipline_response.json()
    assert discipline_data["name"] == discipline_response_data["name"]
    discipline_id = discipline_data["id"]

    # Создание уровня урока
    level_response_data = {
        "name": "Middle"
    }
    level_response = await client.post("/api/v1/lesson-levels/", json=level_response_data)
    print("Response status:", level_response.status_code)
    print("Response JSON:", level_response.json())
    assert level_response.status_code == 200
    level_data = level_response.json()
    assert level_data["name"] == level_response_data["name"]
    level_id = level_data["id"]

    # Сохраняем ID дисциплины и уровня урока для использования в следующих тестах
    return discipline_id, level_id


# Фикстуры создания категории и урока
@pytest.fixture(scope="session")
async def create_category_and_lesson(client: AsyncClient, create_discipline_and_lesson_level: tuple[int, int]) -> tuple[int, int]:
    # Создание категории
    category = {
        "name": "Test category",
    }
    response = await client.post("/api/v1/categories/", json=category)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == category["name"]
    category_id = data["id"]

    # Получение id дисциплины и уровня урока
    discipline_id, lesson_level_id = create_discipline_and_lesson_level

    # Создание урока
    lesson = {
        "name": "Test lesson",
        "discipline_id": discipline_id,
        "lesson_level_id": lesson_level_id
    }
    response = await client.post("/api/v1/lessons/", json=lesson)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == lesson["name"]
    lesson_id = data["id"]

    # Сохраняем ID категории и урока для использования в следующих тестах
    return category_id, lesson_id


@pytest.fixture(scope="session")
async def create_subject(client: AsyncClient, create_category_and_lesson: tuple[int, int]):
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
    subject_id = data["id"]

    return subject_id


@pytest.fixture(scope="session")
async def create_question(client: AsyncClient, create_subject: int):
    subject_id = create_subject
    print(f"subject_id: {subject_id}")

    question = {
        "subject_id": subject_id,
        "text": "Test question",
        "answer": "Test answer"
    }
    response = await client.post("/api/v1/questions/", json=question)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["subject_id"] == question["subject_id"]
    assert data["text"] == question["text"]
    assert data["answer"] == question["answer"]
    question_id = data["id"]

    return question_id


@pytest.fixture(scope="session")
async def create_student(client: AsyncClient):
    student = {
        "first_name": "Семён",
        "last_name": "Семёнов",
        "date_of_birth": "2002-01-01",
    }
    response = await client.post("/api/v1/students/", json=student)
    print("Response status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == student["first_name"]
    assert data["last_name"] == student["last_name"]
    assert data["date_of_birth"] == student["date_of_birth"]
    student_id = data["id"]

    return student_id