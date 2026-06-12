from database.db import SessionLocal
from models.task_model import Task
from fastapi import HTTPException


def create_task_service(task):

    db = SessionLocal()

    new_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed
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


def get_tasks_service():

    db = SessionLocal()

    tasks = db.query(Task).all()

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

    db.close()

    if not task:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
def update_task_service(task_id: int, task):

    db = SessionLocal()

    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if not existing_task:
        db.close()
        return HTTPException(
            status_code=404,
            detail="Task not found"
        )

    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.completed = task.completed

    db.commit()
    db.refresh(existing_task)

    db.close()

    return {
        "message": "Task updated successfully",
        "task": {
            "id": existing_task.id,
            "title": existing_task.title,
            "description": existing_task.description,
            "completed": existing_task.completed
        }
    }

    
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }