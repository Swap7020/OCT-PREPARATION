import sqlite3
from typing import Literal

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

DB_PATH = "bookings_day4.db"

app = FastAPI(title="Emergency Driver Booking API")


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = connect_db()

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                distance_km REAL NOT NULL,
                fare REAL NOT NULL,
                status TEXT NOT NULL
                    CHECK (
                        status IN (
                            'pending',
                            'completed',
                            'cancelled'
                        )
                    )
            )
        """)

        conn.commit()
    finally:
        conn.close()


def get_db():
    conn = connect_db()

    try:
        yield conn
    finally:
        conn.close()


init_db()


class BookingCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=100)
    distance_km: float = Field(gt=0, le=500)


class BookingStatusUpdate(BaseModel):
    status: Literal["pending", "completed", "cancelled"]


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/bookings", status_code=201)
def create_booking(
    data: BookingCreate,
    conn: sqlite3.Connection = Depends(get_db)
):
    fare = round(50 + data.distance_km * 15, 2)

    cursor = conn.execute(
        """
        INSERT INTO bookings (
            customer_name,
            distance_km,
            fare,
            status
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            data.customer_name,
            data.distance_km,
            fare,
            "pending"
        )
    )

    conn.commit()

    booking = conn.execute(
        "SELECT * FROM bookings WHERE booking_id = ?",
        (cursor.lastrowid,)
    ).fetchone()

    return dict(booking)


@app.get("/bookings/{booking_id}")
def get_booking(
    booking_id: int,
    conn: sqlite3.Connection = Depends(get_db)
):
    booking = conn.execute(
        "SELECT * FROM bookings WHERE booking_id = ?",
        (booking_id,)
    ).fetchone()

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return dict(booking)


@app.patch("/bookings/{booking_id}")
def update_booking(
    booking_id: int,
    update: BookingStatusUpdate,
    conn: sqlite3.Connection = Depends(get_db)
):
    booking = conn.execute(
        "SELECT * FROM bookings WHERE booking_id = ?",
        (booking_id,)
    ).fetchone()

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    conn.execute(
        "UPDATE bookings SET status = ? WHERE booking_id = ?",
        (update.status, booking_id)
    )

    conn.commit()

    updated_booking = conn.execute(
        "SELECT * FROM bookings WHERE booking_id = ?",
        (booking_id,)
    ).fetchone()

    return dict(updated_booking)