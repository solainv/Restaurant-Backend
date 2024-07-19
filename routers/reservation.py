# app\routers\reservation.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.security import decode_access_token
from controllers.reservation import get_all_reservations, create_reservation, update_reservation, delete_reservation
from schemas.reservation import ReservationCreate, ReservationUpdate

router = APIRouter()

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/")
def read_all_reservations(token: str = Depends(oauth2_scheme)):
    # Decode and verify the access token
    user = decode_access_token(token)
    # Now you can use the user or its ID for further operations
    return get_all_reservations()

@router.post("/")
def create_new_reservation(reservation: ReservationCreate):
    return create_reservation(reservation)

@router.put("/{reservation_id}")
def update_reservation_by_id(reservation_id: int, reservation: ReservationUpdate):
    return update_reservation(reservation_id, reservation)

@router.delete("/{reservation_id}")
def delete_reservation_by_id(reservation_id: int):
    return delete_reservation(reservation_id)
