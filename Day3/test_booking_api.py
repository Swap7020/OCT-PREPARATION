
import pytest
from fastapi.testclient import TestClient

import booking_api

client = TestClient(booking_api.app)


@pytest.fixture(autouse=True)
def reset_bookings():
    """Give each test a predictable starting state."""
    booking_api.bookings.clear()
    booking_api.bookings[1] = {
        "booking_id": 1,
        "status": "pending",
        "fare": 200,
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_booking():
    response = client.post(
        "/bookings",
        json={
            "customer_name": "Rahul",
            "distance_km": 10,
        },
    )

    assert response.status_code == 201
    assert response.json()["customer_name"] == "Rahul"
    assert response.json()["fare"] == 200


def test_reject_invalid_booking():
    response = client.post(
        "/bookings",
        json={
            "customer_name": "R",
            "distance_km": -5,
        },
    )

    assert response.status_code == 422


def test_get_missing_booking():
    response = client.get("/bookings/999")

    assert response.status_code == 404
