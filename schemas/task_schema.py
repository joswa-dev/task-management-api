from pydantic import BaseModel, EmailStr, Field

class TaskCreate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=100
    )
    
    description: str
    completed: bool = False

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str