Task Management API

A secure Task Management API built using FastAPI, SQLAlchemy, JWT Authentication, and SQLite.

Features

- JWT Login Authentication
- User Registration
- Protected Routes
- Create Task
- Get All Tasks
- Get Single Task
- Update Task
- Delete Task
- User-specific Tasks
- Request Validation
- Swagger API Documentation
- Proper Folder Structure

Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Uvicorn
- Swagger UI

Installation

Clone repository:

git clone https://github.com/joswa-dev/task-management-api

Go to project folder:

cd task-management-api

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

API Documentation

Open:

http://127.0.0.1:8000/docs

Project Structure

task-management-api/
│── core/
│── database/
│── models/
│── routes/
│── schemas/
│── services/
│── main.py
│── requirements.txt