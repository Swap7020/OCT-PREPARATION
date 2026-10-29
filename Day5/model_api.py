import math
import joblib

from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"

if not MODEL_PATH.exists():
    raise RuntimeError(
        "Model artifact not found. Run train_model.py first."
    )

artifact = joblib.load(MODEL_PATH)

model = artifact["model"]
target_names = artifact["target_names"]

app = FastAPI(title="ML Prediction API")


class PredictionRequest(BaseModel):
    features: list[float] = Field(
        min_length=30,
        max_length=30,
    )


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(request: PredictionRequest):
    features = request.features

    if not all(math.isfinite(value) for value in features):
        raise HTTPException(
            status_code=422,
            detail="Features must be finite numbers",
        )

    try:
        prediction = int(model.predict([features])[0])

        probabilities = model.predict_proba([features])[0]
        confidence = float(max(probabilities))

        return {
            "prediction": target_names[prediction],
            "confidence": round(confidence, 4),
        }

    except (ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=422,
            detail="Invalid prediction input",
        ) from exc