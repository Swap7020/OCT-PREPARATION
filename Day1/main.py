from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="My Driver Booking API")


class BookingRequest(BaseModel):
    customer_name: str = Field(min_length=2, max_length=100)
    distance_km: float = Field(gt=0, le=500)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/estimate-fare")
def estimate_fare(booking: BookingRequest):
    base_fare = 50
    fare_per_km = 15

    fare = base_fare + booking.distance_km * fare_per_km

    return {
        "customer_name": booking.customer_name,
        "distance_km": booking.distance_km,
        "estimated_fare": round(fare, 2)
    }