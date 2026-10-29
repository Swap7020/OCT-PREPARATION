import numpy as np
import joblib

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# Build the pipeline
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=2000),
)

# Train
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print(
    "Macro-independent positive-class precision:",
    precision_score(y_test, predictions),
)
print(
    "Positive-class recall:",
    recall_score(y_test, predictions),
)
print(
    "Positive-class F1:",
    f1_score(y_test, predictions),
)

print("\nConfusion matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=data.target_names,
    )
)

# Save the trained model and its metadata
artifact = {
    "model": model,
    "target_names": data.target_names.tolist(),
    "feature_names": data.feature_names.tolist(),
}

joblib.dump(artifact, "model.joblib")

print("\nModel saved to model.joblib")