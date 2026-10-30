from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class BookingRequest(BaseModel):
    pickup: str = Field(min_length=3, max_length=100)
    distance_km: float = Field(gt=0, le=100)
    passengers: int = Field(ge=1, le=4)
    vehicle_type: Literal["hatchback", "sedan", "suv"]


class FareService:
    def calculate_fare(self, distance_km: float, passengers: int):
        base_fare = 50
        distance_charge = distance_km * 12
        passenger_charge = max(0, passengers - 1) * 10

        return round(
            base_fare + distance_charge + passenger_charge, 2
        )


fare_service = FareService()


@app.post("/bookings/quote")
def create_booking_quote(booking: BookingRequest):
    fare = fare_service.calculate_fare(
        booking.distance_km,
        booking.passengers
    )

    return {
        "pickup": booking.pickup,
        "distance_km": booking.distance_km,
        "vehicle_type": booking.vehicle_type,
        "estimated_fare": fare
    }