import uuid

from fastapi import APIRouter, Depends

from app.repositories.todo_repositories import TodoRepository
from app.schemas.todo_schema import TodoSchema

router = APIRouter()

# CRUD Operation


@router.post("/todos/")
async def create_todo(
    todo: TodoSchema,
    todo_repo: TodoRepository = Depends(TodoRepository),
):
    """
    Create a Todo and store it in the database
    """
    new_todo = await todo_repo.create_todo(todo)
    return new_todo


@router.get("/todos/")
async def get_todos(repo: TodoRepository = Depends(TodoRepository)):
    """
    Get todos that are in the database
    """
    return await repo.get_todos()


@router.get("/todos/{id}")
async def get_todo_id(id: uuid.UUID, repo: TodoRepository = Depends(TodoRepository)):
    """
    Get todos that are in the database by id
    """
    return await repo.get_todo_by_id(id)


@router.put("/todos/{id}")
async def update_todo_id(
    id: uuid.UUID,
    todo: TodoSchema,
    repo: TodoRepository = Depends(TodoRepository),
):
    """
    Update todo details using their ID that is in the database
    """
    updated_todo = await repo.update_todo(id, todo.description, todo.status)
    return updated_todo  # think of including http verbs with a message


# include error codes


@router.delete("/todos/{id}")
async def delete_todo_id(id: uuid.UUID, repo: TodoRepository = Depends(TodoRepository)):
    """
    Delete todo details using their UUID that is stored in the database
    """
    deleted_todo = await repo.delete_todo(id)
    return deleted_todo
