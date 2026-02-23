from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from .models import Task, TaskCreate
from . import models_orm

class ITaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Task]: pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task: pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]: pass

    # Challenge 1: เพิ่ม method update
    @abstractmethod
    def update_status(self, task_id: int, completed: bool) -> Optional[Task]: pass

    # Challenge 2: เพิ่ม method เพื่อค้นหาด้วยชื่อ
    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Task]: pass

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(models_orm.TaskORM).all()

    def create(self, task_in: TaskCreate):
        db_task = models_orm.TaskORM(**task_in.model_dump())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_by_id(self, task_id: int):
        return self.db.query(models_orm.TaskORM).filter(models_orm.TaskORM.id == task_id).first()

    # Challenge 1 Implement: เปลี่ยนสถานะ completed
    def update_status(self, task_id: int, completed: bool):
        db_task = self.get_by_id(task_id)
        if db_task:
            db_task.completed = completed
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    # Challenge 2 Implement: ค้นหาด้วยชื่อ
    def get_by_title(self, title: str):
        return self.db.query(models_orm.TaskORM).filter(models_orm.TaskORM.title == title).first()

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def get_all(self): return self.tasks

    def create(self, task_in: TaskCreate):
        task = Task(id=self.current_id, **task_in.model_dump())
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int):
        return next((t for t in self.tasks if t.id == task_id), None)

    # Challenge 1 Implement สำหรับ InMemory
    def update_status(self, task_id: int, completed: bool):
        task = self.get_by_id(task_id)
        if task:
            task.completed = completed
        return task

    # Challenge 2 Implement สำหรับ InMemory
    def get_by_title(self, title: str):
        return next((t for t in self.tasks if t.title == title), None)