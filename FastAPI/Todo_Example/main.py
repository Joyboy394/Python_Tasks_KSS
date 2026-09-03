import json
import os
from enum import Enum
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="ToDo API")

# File to store the data
DATA_FILE = "tasks.json"

# Define the allowed statuses exactly as requested
class TaskStatus(str, Enum):
    NOT_STARTED = "not yet started"
    IN_PROGRESS = "InProgress"
    COMPLETED = "completed"

# Pydantic models for data validation
class TaskCreate(BaseModel):
    title: str
    status: TaskStatus = TaskStatus.NOT_STARTED

class TaskUpdate(BaseModel):
    status: TaskStatus

class Task(BaseModel):
    id: int
    title: str
    status: TaskStatus

# Helper functions for file I/O
def read_tasks() -> List[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def write_tasks(tasks: List[dict]):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# 1. Fetch all tasks
@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    return read_tasks()

# 2. Create a task
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_in: TaskCreate):
    tasks = read_tasks()
    new_id = 1 if not tasks else max(t["id"] for t in tasks) + 1
    
    new_task = {
        "id": new_id,
        "title": task_in.title,
        "status": task_in.status.value
    }
    
    tasks.append(new_task)
    write_tasks(tasks)
    return new_task

# 3. Update with the status
@app.patch("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, task_update: TaskUpdate):
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = task_update.status.value
            write_tasks(tasks)
            return task
            
    raise HTTPException(status_code=404, detail="Task not found")

# 4. Deleting the tasks
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    tasks = read_tasks()
    filtered_tasks = [t for t in tasks if t["id"] != task_id]
    
    if len(tasks) == len(filtered_tasks):
        raise HTTPException(status_code=404, detail="Task not found")
        
    write_tasks(filtered_tasks)
    return None
