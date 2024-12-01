import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_create_todos(client: AsyncClient):
    todo_data = {
        "title": "Dinner",
        "description": "Make Chapati",
        "status": "Open",
    }

    response = await client.post(f"{TEST_BASE_URL}/api/todos/", json=todo_data)
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data
    assert response_data["title"] == todo_data["title"]
    assert response_data["description"] == todo_data["description"]
    assert response_data["status"] == todo_data["status"]


@pytest.mark.asyncio
async def test_get_todos(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/todos/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_todo_id(client: AsyncClient):
    # Create a todo
    todo_obj = {
        "title": "Dinner",
        "description": "Make dinner",
        "status": "Open",
    }
    create_response = await client.post(f"{TEST_BASE_URL}/api/todos/", json=todo_obj)
    assert create_response.status_code == 201
    created_todo = create_response.json()

    # Fetch the specific todo by ID
    get_response = await client.get(f"{TEST_BASE_URL}/api/todos/{created_todo['id']}")
    assert get_response.status_code == 200
    fetched_todo = get_response.json()

    # Verify the fetched todo matches the created one
    assert fetched_todo["id"] == created_todo["id"]
    assert fetched_todo["title"] == todo_obj["title"]
    assert fetched_todo["description"] == todo_obj["description"]
    assert fetched_todo["status"] == todo_obj["status"]


@pytest.mark.asyncio
async def test_update_todo_id(client: AsyncClient):
    todo_data = {
        "title": "short break",
        "description": "smoking break",
        "status": "Open",
    }

    response = await client.post(f"{TEST_BASE_URL}/api/todos/", json=todo_data)

    todo_response = response.json()
    assert "id" in todo_response
    todo_id = todo_response["id"]
    update_data = {
        **todo_data,
        "title": "short break",
        "description": "smoking break",
        "status": "Cancelled",
    }
    response = await client.put(
        f"{TEST_BASE_URL}/api/todos/{todo_id}",
        json=update_data,
    )

    # Check the update response
    assert response.status_code == 200
    updated_todo = response.json()
    assert updated_todo["title"] == "short break"
    assert updated_todo["description"] == "smoking break"
    assert updated_todo["status"] == "Cancelled"


@pytest.mark.asyncio
async def test_delete_todo_id(client: AsyncClient):
    # Create a todo to delete
    todo_obj = {
        "title": "Dinner",
        "description": "Make dinner",
        "status": "Open",
    }
    create_response = await client.post(f"{TEST_BASE_URL}/api/todos/", json=todo_obj)
    assert create_response.status_code == 201

    todo_id = create_response.json()["id"]

    # Confirm item exists before deletion
    get_response_before = await client.get(f"{TEST_BASE_URL}/api/todos/{todo_id}")
    assert get_response_before.status_code == 200

    # Perform deletion
    delete_response = await client.delete(f"{TEST_BASE_URL}/api/todos/{todo_id}")
    assert delete_response.status_code == 204
