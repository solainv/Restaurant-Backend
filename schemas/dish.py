# app\schemas\dish.py
from pydantic import BaseModel

class DishCreate(BaseModel):
    name: str
    description: str
    price: float
    image: str

class DishUpdate(BaseModel):
    name: str
    description: str
    price: float
    image: str

class Dish(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: str

    class Config:
        from_attributes = True
