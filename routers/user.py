# app\routers\user.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.security import decode_access_token
from controllers.user import get_user_by_username, update_user
from schemas.user import UserUpdate

router = APIRouter()

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/profile")
def read_user_profile(token: str = Depends(oauth2_scheme)):
    username = decode_access_token(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


@router.put("/profile")
def update_user_profile(user_id: int, user: UserUpdate):
    return update_user(user_id, user)
