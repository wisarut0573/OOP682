from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        existing_task = self.repo.get_by_title(task_in.title)
        
        if existing_task:
            raise HTTPException(status_code=400, detail="Task with this title already exists")

        return self.repo.create(task_in)

    def mark_task_completed(self, task_id: int):
        current_task = self.repo.get_by_id(task_id)
        if not current_task:
            return None
        updated_task = current_task.model_copy(update={"completed": True})
        return self.repo.update(updated_task)