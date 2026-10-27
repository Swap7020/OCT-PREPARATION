from fastapi.testclient import TestClient
from api_day2 import app

client = TestClient(app)


def test_update_existing_booking():
    response = client.patch(
        "/bookings/1",
        json={"status": "completed"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "completed"


def test_update_missing_booking():
    response = client.patch(
        "/bookings/99",
        json={"status": "completed"}
    )

    assert response.status_code == 404