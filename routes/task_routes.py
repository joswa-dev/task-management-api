from fastapi import APIRouter
from schemas.task_schema import TaskCreate
from services.task_service import (
    create_task_service,
    get_tasks_service,
    get_task_by_id_service,
    update_task_service,
    delete_task_service
)
from schemas.task_schema import UserCreate
from services.task_service import create_user_service
from schemas.task_schema import UserLogin
from services.task_service import login_user_service
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from core.dependencies import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/")
def get_all_tasks(
    current_user: dict = Depends(get_current_user)
):
    return get_tasks_service(current_user)

@router.post("/signup")
def signup(user: UserCreate):
    return create_user_service(user)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return login_user_service(form_data)

@router.post("/")
def create_task(
    task: TaskCreate,
    current_user: dict = Depends(get_current_user)
):
    return create_task_service(task, current_user)


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskCreate,
    current_user: dict = Depends(get_current_user)
):
    return update_task_service(task_id, task)


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: dict = Depends(get_current_user)
):
    return delete_task_service(task_id)


@router.get("/{task_id}")
def get_task(
    task_id: int,
    current_user: dict = Depends(get_current_user)
):
    return get_task_by_id_service(task_id)