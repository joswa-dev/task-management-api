from database.db import SessionLocal
from models.task_model import Task
from fastapi import HTTPException
from models.task_model import User
from schemas.task_schema import UserCreate
from core.security import hash_password
from core.security import verify_password, create_access_token
from schemas.task_schema import UserLogin


def create_task_service(task, current_user):

    db = SessionLocal()

    new_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user_id=current_user["user_id"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    db.close()

    return {
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "completed": new_task.completed
        }
    }


def get_tasks_service(current_user):

    db = SessionLocal()

    tasks = db.query(Task).filter(
        Task.user_id == current_user["user_id"]
    ).all()

    db.close()

    return {
        "message": "All tasks fetched successfully",
        "tasks": [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed
            }
            for task in tasks
        ]
    }

def delete_task_service(task_id: int):

    db = SessionLocal()

    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if not existing_task:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(existing_task)
    db.commit()

    db.close()

    return {
        "message": "Task deleted successfully"
    }

def get_task_by_id_service(task_id: int):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    response = {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    db.close()

    return response
def update_task_service(task_id: int, task, current_user):

    db = SessionLocal()

    existing_task = db.query(Task).filter(Task.id == task_id).first()
    
    if (
        current_user["role"] != "admin"
        and existing_task.user_id !=
current_user["user_id"]
    ):

        db.close()
        return {
            "message": "You are not allowed to update this task"
        }
    
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.completed = task.completed


def create_user_service(user: UserCreate):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        db.close()
        return {
            "message": "User already exists"
        }

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "role": new_user.role
        }
    }

def login_user_service(user):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not existing_user:
        db.close()
        return {
            "message": "Invalid email or password"
        }

    is_valid_password = verify_password(
        user.password,
        existing_user.password
    )

    if not is_valid_password:
        db.close()
        return {
            "message": "Invalid email or password"
        }

    access_token = create_access_token(
        data={
            "user_id": existing_user.id,
            "role": existing_user.role
        }
    )

    db.close()

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }