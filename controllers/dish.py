# app\controllers\dish.py
from fastapi import HTTPException
from utils.database import get_db_connection  
from schemas.dish import DishCreate, DishUpdate

def get_all_dishes():
    conn = get_db_connection  ()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM dishes")
        dishes = cursor.fetchall()
    conn.close()
    return dishes

def create_dish(dish: DishCreate):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        image_path = f"/images/{dish.image}"  # Assuming dish.image contains the filename
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO dishes (name, description, price, image) VALUES (%s, %s, %s, %s) RETURNING *",
                (dish.name, dish.description, dish.price, image_path),
            )
            new_dish = cursor.fetchone()
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating dish: {e}")
    finally:
        conn.close()
    
    return new_dish

def update_dish(dish_id: int, dish: DishUpdate):
    conn = get_db_connection  ()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE dishes SET name = %s, description = %s, price = %s, image = %s WHERE id = %s RETURNING *",
            (dish.name, dish.description, dish.price, dish.image, dish_id),
        )
        updated_dish = cursor.fetchone()
        conn.commit()
    conn.close()
    if updated_dish is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return updated_dish

def delete_dish(dish_id: int):
    conn = get_db_connection  ()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM dishes WHERE id = %s RETURNING *", (dish_id,))
        deleted_dish = cursor.fetchone()
        conn.commit()
    conn.close()
    if deleted_dish is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return deleted_dish

def get_dish_by_id(dish_id: int):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM dishes WHERE id = %s", (dish_id,))
        dish = cursor.fetchone()
    conn.close()
    return dish
