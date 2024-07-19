# backend/app/routers/profile.py
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from controllers.auth import get_current_user
from schemas.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/profile", response_model=User)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user
