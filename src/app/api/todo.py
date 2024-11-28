import uuid

from fastapi import APIRouter, Depends, HTTPException, status

from app.repositories.todo_repositories import TodoRepository
from app.schemas.todo_schema import TodoResponse, TodoSchema

router = APIRouter()


# CRUD Operation
@router.post("/todos/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo: TodoSchema,
    todo_repo: TodoRepository = Depends(TodoRepository),
):
    """
    Create a Todo and store it in the database
    """
    new_todo = await todo_repo.create_todo(todo)
    return new_todo


@router.get("/todos/", response_model=list[TodoResponse], status_code=status.HTTP_200_OK)
async def get_todos(repo: TodoRepository = Depends(TodoRepository)):
    """
    Get todos that are in the database
    """
    todos = await repo.get_todos()
    if not todos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No todos found"
        )
    return todos


@router.get("/todos/{id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
async def get_todo_id(id: uuid.UUID, repo: TodoRepository = Depends(TodoRepository)):
    """
    Get a todo by ID that is in the database
    """
    todo = await repo.get_todo_by_id(id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    return todo


@router.put("/todos/{id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
async def update_todo_id(
    id: uuid.UUID,
    todo: TodoSchema,
    repo: TodoRepository = Depends(TodoRepository),
):
    """
    Update todo details using their ID that is in the database
    """
    updated_todo = await repo.update_todo(id, todo.description, todo.status)
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    return updated_todo


@router.delete("/todos/{id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
async def delete_todo_id(id: uuid.UUID, repo: TodoRepository = Depends(TodoRepository)):
    deleted_todo = await repo.delete_todo(id)
    if not deleted_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    return deleted_todo
