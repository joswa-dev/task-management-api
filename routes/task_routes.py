from fastapi import APIRouter
from schemas.task_schema import TaskCreate
from services.task_service import (
    create_task_service,
    get_tasks_service,
    get_task_by_id_service,
    update_task_service,
    delete_task_service
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def get_tasks():
        return get_tasks_service()

@router.put("/{task_id}")
def update_task(task_id: int, task: TaskCreate):
      return update_task_service(task_id, task)

@router.get("/{task_id}")
def get_task(task_id: int):
      return get_task_by_id_service(task_id)

@router.post("/")
def create_task(task: TaskCreate):
    return create_task_service(task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
      return delete_task_service(task_id)