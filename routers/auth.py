# app\routers\auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from controllers.auth import create_user
from schemas.user import UserCreate
from utils.security import create_access_token
from controllers.auth import authenticate_user
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register")
def register_user(user: UserCreate):
    return create_user(user)

@router.post("/login")
async def login(user: UserCreate):
    try:
        authenticated_user = authenticate_user(user.username, user.password)
        if authenticated_user:
            access_token = create_access_token({"sub": authenticated_user.username})
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/logout")
def logout():
    return {"message": "Logged out successfully"}

@router.post("/login")
async def login(user: UserCreate):
    try:
        authenticated_user = authenticate_user(user.username, user.password)
        if authenticated_user:
            access_token = create_access_token({"sub": authenticated_user.username})
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))