import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_create_todos(client: AsyncClient):
    todo_data = {
        "description": "Make Chapati",
        "status": "Open",
    }

    response = await client.post(f"{TEST_BASE_URL}/api/todos/", json=todo_data)
    assert response.status_code == 200
    todo_data["id"] = response.json()["id"]
    assert response.json() == todo_data


@pytest.mark.asyncio
async def test_get_todos(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/todos/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_todo_id(client: AsyncClient):
    # ensure todo exists before getting
    todo_obj = {
        "description": "Make dinner",
        "id": "55602bab-b1c6-412e-8489-f8ec881e7b95",
        "status": "Open",
    }
    await client.post(f"{TEST_BASE_URL}/api/todos/", json=todo_obj)
    get_response = await client.get(f"{TEST_BASE_URL}/api/todos/")
    assert get_response.status_code == 200


@pytest.mark.asyncio
async def test_update_todo_id(client: AsyncClient):
    todo_data = {
        "name": "smoking break",
        "phone": "Open",
    }
    response = await client.post(f"{TEST_BASE_URL}/api/todos/", json=todo_data)
    todo_id = response.json()["id"]
    response = await client.put(
        f"{TEST_BASE_URL}/api/todos/{todo_id}",
        json={
            **todo_data,
            "description": "smoking break",
            "status": "Cancelled",
        },
    )
    assert response.status_code == 200
    assert response.json()["Description"] == "smoking break"
    assert response.json()["status"] == "Cancelled"


@pytest.mark.asyncio
async def test_delete_todo_id(client: AsyncClient):
    todo_obj = {
        "description": "Make dinner",
        "id": "55602bab-b1c6-412e-8489-f8ec881e7b95",
        "status": "Open",
    }
    await client.delete(f"{TEST_BASE_URL}/api/todos/", json=todo_obj)
    get_response = await client.get(f"{TEST_BASE_URL}/api/todos/")
    assert get_response.status_code == 200
