# app\schemas\reservation.py
from pydantic import BaseModel
from datetime import datetime

class ReservationCreate(BaseModel):
    user_id: int
    reservation_date: datetime
    guests_count: int

class ReservationUpdate(BaseModel):
    reservation_date: datetime
    guests_count: int

class ReservationResponse(BaseModel):
    id: int
    user_id: int
    reservation_date: datetime
    guests_count: int
    created_at: datetime

    class Config:
        from_attributes = True
