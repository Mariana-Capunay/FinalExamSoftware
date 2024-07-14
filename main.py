from fastapi import FastAPI,HTTPException 
from pydantic import BaseModel #to check the data type in a class
from pydantic import Field #to give a default value to a field
from typing import Optional, List #for optional data 
from uuid import UUID, uuid4 # to generate hast

app = FastAPI() 


class Task(BaseModel):
    # id: UUID = Field(default_factory=uuid4, alias="_id") #to generate a hash
    id: int 
    name: str
    description: str
    completed: Optional[bool] = False
    date: Optional[str] = None


tasks: List[Task] = [] #List of tasks
used_ids: set = set()  # to store unique ids

@app.get("/")
def main():
    return {"message": "Hello World"}


@app.post("/create_task/")
def create_task(task: Task):
    if task.id in used_ids:
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks.append(task)
    used_ids.add(task.id)
    return {"message": "Task created successfully", "data": task.model_dump()}


@app.get("/get_tasks/")
def get_tasks():
    return {"message": "Tasks fetched successfully", "data": [task.model_dump() for task in tasks]}


@app.get("get_task/{task_id}")
def get_task_by_id(task_id: int):
    try:
        return {"message": "Task fetched successfully", "data": tasks[task_id].model_dump()}
    except:
        return {"message": "Task not found"}
