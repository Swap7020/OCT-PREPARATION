from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

bookings = {
    1: {"booking_id": 1, "status": "pending", "fare": 200}
}


class BookingUpdate(BaseModel):
    status: str = Field(
        pattern="^(pending|completed|cancelled)$"
    )


@app.patch("/bookings/{booking_id}")
def update_booking(booking_id: int, update: BookingUpdate):
    booking = bookings.get(booking_id)

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking["status"] = update.status
    return booking