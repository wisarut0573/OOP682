from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

# Import จากไฟล์ภายในโปรเจกต์ของคุณ
from .database import SessionLocal, engine
from . import models_orm
from .models import Task, TaskCreate
from .repositories import SqlTaskRepository
from .services import TaskService

# สร้างตาราง database อัตโนมัติเมื่อรันโปรแกรม
models_orm.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="ระบบจัดการงาน (Task) เชื่อมต่อกับ Database"
)

# Dependency สำหรับสร้าง Database Session ในแต่ละ Request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency สำหรับสร้าง TaskService โดยฉีด Repository เข้าไป
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

# --- Routes ---

@app.get("/", include_in_schema=False)
def root():
    """หน้าแรกของ API: ทำการ Redirect ไปที่หน้า Documentation (/docs) อัตโนมัติ"""
    return RedirectResponse(url="/docs")

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    """ดึงรายการงานทั้งหมด"""
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    """สร้างงานใหม่ลงใน Database"""
    return service.create_task(task)

# Challenge 1: อัปเดตสถานะงานว่าเสร็จสิ้นแล้ว
@app.put("/tasks/{task_id}/complete", response_model=Task)
def mark_task_complete(task_id: int, service: TaskService = Depends(get_task_service)):
    """เปลี่ยนสถานะงาน (task_id) ให้เป็น Completed"""
    task = service.complete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="ไม่พบงานที่ระบุ")
    return task