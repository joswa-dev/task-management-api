from fastapi import FastAPI
from routes.task_routes import router as task_router
from database.db import engine, Base
from models.task_model import Task

app = FastAPI(
    title="Task Management API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(task_router)


@app.get("/")
def home():
    return {
        "message": "Task Management API running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }