from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Driver Booking API")

bookings = {
    1: {
        "booking_id": 1,
        "status": "pending",
        "fare": 200
    }
}


class BookingCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=100)
    distance_km: float = Field(gt=0, le=500)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/bookings", status_code=201)
def create_booking(data: BookingCreate):
    booking_id = max(bookings.keys(), default=0) + 1

    fare = 50 + data.distance_km * 15

    booking = {
        "booking_id": booking_id,
        "customer_name": data.customer_name,
        "distance_km": data.distance_km,
        "fare": round(fare, 2),
        "status": "pending"
    }

    bookings[booking_id] = booking

    return booking


@app.get("/bookings/{booking_id}")
def get_booking(booking_id: int):
    booking = bookings.get(booking_id)

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking

def completed_bookings(bookings):
    for booking in bookings:
        if booking["status"] == "completed":
            yield booking


records = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "completed"},
]

for booking in completed_bookings(records):
    print(booking)