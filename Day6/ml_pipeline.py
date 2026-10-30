import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Reproducible synthetic booking dataset
rng = np.random.default_rng(42)
n = 500

df = pd.DataFrame({
    "distance_km": rng.uniform(1, 30, n),
    "wait_minutes": rng.uniform(1, 30, n),
    "driver_rating": rng.uniform(3, 5, n),
    "vehicle_type": rng.choice(
        ["hatchback", "sedan", "suv"], n
    )
})

# Synthetic target for practising classification
risk_score = (
    0.08 * df["distance_km"]
    + 0.05 * df["wait_minutes"]
    - 0.8 * df["driver_rating"]
    + (df["vehicle_type"] == "suv") * 0.5
)

df["high_risk"] = (
    risk_score + rng.normal(0, 0.5, n) > 1.2
).astype(int)

X = df.drop(columns=["high_risk"])
y = df["high_risk"]

numeric_features = [
    "distance_km",
    "wait_minutes",
    "driver_rating"
]

categorical_features = ["vehicle_type"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

model = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

joblib.dump(model, "booking_risk_pipeline.joblib")

print("Complete preprocessing and model pipeline saved.")