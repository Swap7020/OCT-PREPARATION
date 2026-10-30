from fastapi.testclient import TestClient
from model_api import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_rejects_wrong_feature_count():
    response = client.post(
        "/predict",
        json={"features": [0.0, 1.0]},
    )

    assert response.status_code == 422


def test_returns_prediction():
    response = client.post(
        "/predict",
        json={"features": [0.0] * 30},
    )

    assert response.status_code == 200

    result = response.json()

    assert result["prediction"] in {"benign", "malignant"}
    assert 0 <= result["confidence"] <= 1