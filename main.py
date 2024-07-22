from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

todos = []

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    """
    Add a new todo item to the list. Toggle the 'completed' status
    between True and False on each request.
    """
    # Set the completed status based on the last added todo item
    if todos and todos[-1].completed:
        todo.completed = False
    else:
        todo.completed = True
    todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
def read_todos():
    """
    Retrieve all todo items.
    """
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    """
    Retrieve a todo item by its ID.
    """
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    """
    Update a todo item by its ID. Toggle the 'completed' status
    between True and False on each request.
    """
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            # Toggle the completed status
            updated_todo.completed = not todos[index].completed
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    """
    Delete a todo item by its ID.
    """
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")
