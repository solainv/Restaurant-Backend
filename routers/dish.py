# app\routers\dish.py
from fastapi import APIRouter, Depends, HTTPException
from utils.security import decode_access_token
from controllers.dish import get_all_dishes, create_dish, update_dish, delete_dish, get_dish_by_id
from schemas.dish import DishCreate, DishUpdate, Dish
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Dish])
def read_all_dishes():
    return get_all_dishes()

@router.post("/", response_model=Dish)
def create_new_dish(dish: DishCreate):
    return create_dish(dish)

@router.put("/{dish_id}", response_model=Dish)
def update_dish_by_id(dish_id: int, dish: DishUpdate):
    return update_dish(dish_id, dish)

@router.delete("/{dish_id}", response_model=Dish)
def delete_dish_by_id(dish_id: int):
    return delete_dish(dish_id)

@router.get("/{dish_id}", response_model=Dish)  # Neue Route für Einzelgericht
def read_dish_by_id(dish_id: int):
    return get_dish_by_id(dish_id)
