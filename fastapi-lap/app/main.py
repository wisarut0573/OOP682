from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models_orm
from .models import Task, TaskCreate
from .repositories import SqlTaskRepository
from .services import TaskService

# สร้างตาราง database
models_orm.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)

# Challenge 1: สร้าง Route ใหม่
@app.put("/tasks/{task_id}/complete", response_model=Task)
def mark_task_complete(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.complete_task(task_id)