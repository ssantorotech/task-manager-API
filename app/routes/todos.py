
from fastapi import APIRouter, HTTPException, Query
from typing import Annotated
from app.schemas import (
    TodoCreate,
    TodoReplace,
    TodoPatch,
    TodoResponse,
    Priorita
)

from app import database


router = APIRouter(prefix='/todos', tags=['todos'])

@router.get("/", response_model=list[TodoResponse], status_code=200) 
def get_todos():
    todos = list(database.TODOS_DB.values())
    return todos

@router.get("", response_model=list[TodoResponse], status_code=200)
def get_filtered_todos(
    completed: bool | None = None,
    q: str | None = None,
    skip: int = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    priorita: Priorita | None = None
):
    todos = list(database.TODOS_DB.values())
    
    if (completed is not None):
        todos = [todo for todo in todos if todo['completed'] == completed]
    if (q is not None):
        todos = [todo for todo in todos if q.lower() in todo['title'].lower()]

    todos = todos[skip: skip + limit]
    return todos



@router.get("/stats")
def get_todo_stats():
    total_todos = len(database.TODOS_DB)
    completed_todos = sum(1 for todo in database.TODOS_DB.values() if todo['completed'] is True)
    incompleted_todos = sum(1 for todo in database.TODOS_DB.values() if todo['completed'] is False)
    per_priorita = {
        'bassa': 0,
        'media': 0,
        'alta': 0
    }
    for todo in database.TODOS_DB.values():
        per_priorita[todo['priorita']] += 1

    return {
        "total": total_todos,
        "completed": completed_todos,
        "incompleted": incompleted_todos,
        "per_priorita": per_priorita
    }

@router.get("/{todo_id}", response_model=TodoResponse, status_code=200)
def get_todo(todo_id: int):
    if (todo_id not in database.TODOS_DB):
        raise HTTPException(status_code=404, detail="Todo not found")
    return database.TODOS_DB[todo_id]





@router.post("", status_code=201)
def add_todo(todo: TodoCreate):
   new_todo = {'id': next(database.ID), 'completed': False, **todo.model_dump()}
   database.TODOS_DB[new_todo['id']] = new_todo
   return new_todo


@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: TodoReplace):
    if (todo_id not in database.TODOS_DB):
        raise HTTPException(status_code=404, detail="Todo not found")
    database.TODOS_DB[todo_id] = {'id': todo_id, **todo.model_dump()}
    return database.TODOS_DB[todo_id]

@router.patch("/{todo_id}")
def partial_update_todo(todo_id: int, todo: TodoPatch):
    if (todo_id not in database.TODOS_DB):
        raise HTTPException(status_code=404, detail="Todo not found")
    item = database.TODOS_DB[todo_id]
    cambi = todo.model_dump(exclude_unset=True)
    item.update(cambi)
    return item


@router.delete("/{todo_id}")
def delete_todo(todo_id: int) -> dict:
    if (todo_id not in database.TODOS_DB):
        raise HTTPException(status_code=404, detail="Todo not found")
    del database.TODOS_DB[todo_id]
    return {"detail": "Todo deleted"}