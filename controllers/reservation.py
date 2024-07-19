# app\controllers\reservation.py
from utils.database import get_db_connection
from schemas.reservation import ReservationCreate, ReservationUpdate, ReservationResponse

def get_all_reservations():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [ReservationResponse(**dict(row)) for row in rows]

def create_reservation(reservation: ReservationCreate):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO reservations (user_id, reservation_date, guests_count) VALUES (%s, %s, %s) RETURNING *",
        (reservation.user_id, reservation.reservation_date, reservation.guests_count)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return ReservationResponse(**dict(row))

def update_reservation(reservation_id: int, reservation: ReservationUpdate):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE reservations SET reservation_date = %s, guests_count = %s WHERE id = %s RETURNING *",
        (reservation.reservation_date, reservation.guests_count, reservation_id)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return ReservationResponse(**dict(row))

def delete_reservation(reservation_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id = %s", (reservation_id,))
    conn.commit()
    cur.close()
    conn.close()
