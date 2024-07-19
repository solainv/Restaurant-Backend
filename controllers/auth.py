# backend/app/controllers/auth.py
from fastapi import HTTPException, Depends
from jose import JWTError
from utils.security import decode_access_token, verify_password, get_password_hash
from schemas.user import User, UserCreate
from utils.database import get_db_connection
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(username: str, password: str):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    user = get_user_by_username(conn, username)
    if not user or not verify_password(password, user['hashed_password']):
        return None
    
    return User(**user)

def get_user_by_username(conn, username: str):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, username, hashed_password, role FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
    return user

def create_user(user: UserCreate):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    hashed_password = get_password_hash(user.password)
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (username, hashed_password, role) VALUES (%s, %s, %s) RETURNING id, username, role",
            (user.username, hashed_password, user.role),
        )
        created_user = cursor.fetchone()
        conn.commit()
    
    return created_user

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username = decode_access_token(token)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    conn = get_db_connection()
    user = get_user_by_username(conn, username)
    if user is None:
        raise credentials_exception
    
    return User(**user)

def get_current_active_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user
