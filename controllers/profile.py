# backend/app/controllers/profile.py
from utils.database import get_db_connection
from schemas.user import User, HTTPException

def get_user_profile(username: str):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, username, role FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
    return User(**user)
