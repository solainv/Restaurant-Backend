# backend/app/schemas/user.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = 'user'  # Default role for new users

class UserUpdate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True  # Allows Pydantic models to read from attributes