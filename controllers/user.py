# app\controllers\user.py
from fastapi import HTTPException
from utils.database import get_db_connection  
from utils.security import get_password_hash
from schemas.user import UserUpdate

def get_user_by_username(username: str):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
    
    conn.close()
    return user


def update_user(user_id: int, user: UserUpdate):
    conn = get_db_connection  ()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    hashed_password = get_password_hash(user.password)
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE users SET username = %s, hashed_password = %s WHERE id = %s RETURNING *",
            (user.username, hashed_password, user_id),
        )
        updated_user = cursor.fetchone()
        conn.commit()
    conn.close()
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user