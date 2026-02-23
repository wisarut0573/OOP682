from fastapi import HTTPException, status
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    # Challenge 2: ตรวจสอบชื่อซ้ำใน Service
    def create_task(self, task_in: TaskCreate):
        # เช็คชื่อซ้ำผ่าน Repository
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
            # ถ้าซ้ำให้ Raise HTTPException (400)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Task with title '{task_in.title}' already exists."
            )
        return self.repo.create(task_in)

    # Challenge 1: เพิ่ม Logic การเปลี่ยนสถานะงาน
    def complete_task(self, task_id: int):
        task = self.repo.update_status(task_id, completed=True)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task