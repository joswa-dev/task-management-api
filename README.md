# Task Management API

A simple Task Management API built using FastAPI, SQLAlchemy, and SQLite.

## Features

- Create Task
- Get All Tasks
- Get Single Task
- Update Task
- Delete Task
- Request Validation
- Swagger API Documentation

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/task-management-api.git
```

Go to project folder:

```bash
cd task-management-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn main:app --reload
```

## API Documentation

Open:

```bash
http://127.0.0.1:8000/docs
```

## Project Structure

```bash
task-management-api/
│── core/
│── database/
│── models/
│── routes/
│── schemas/
│── services/
│── main.py
│── requirements.txt
```