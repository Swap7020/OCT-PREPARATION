# Day 6 — Short Notes

Python Developer & AI/ML Developer Preparation

## 1. Machine Learning Pipeline

An ML pipeline automates the steps required to prepare data and train a model.

Typical workflow:

1. Data collection
2. Data cleaning
3. Feature preprocessing
4. Train-test split
5. Model training
6. Model evaluation
7. Model saving

Example using Scikit-learn:

```
from sklearn.pipeline import Pipelinefrom sklearn.preprocessing import StandardScalerfrom sklearn.linear_model import LogisticRegressionpipeline = Pipeline([    ("scaler", StandardScaler()),    ("model", LogisticRegression())])pipeline.fit(X_train, y_train)predictions = pipeline.predict(X_test)
```

## 2. Feature Engineering

Feature engineering means selecting, transforming, or creating useful input variables for ML models.

Examples:

- Converting categories into numerical values.
- Scaling numerical features.
- Handling missing values.
- Creating new features from existing data.

Common techniques:

- StandardScaler
- MinMaxScaler
- OneHotEncoder
- SimpleImputer

## 3. Model Evaluation

| Metric    | Purpose                                      |
| --------- | -------------------------------------------- |
| Accuracy  | Overall correct predictions                  |
| Precision | Correctness of positive predictions          |
| Recall    | Ability to identify actual positives         |
| F1-score  | Balance between precision and recall         |
| MAE       | Average absolute regression error            |
| RMSE      | Penalizes larger regression errors           |
| R²        | Regression performance against mean baseline |

Important: Choose evaluation metrics according to the problem. Accuracy alone may be misleading for imbalanced datasets.

## 4. Saving and Loading ML Models

Use Joblib to save trained models.

```
import joblib# Savejoblib.dump(pipeline, "booking_risk_pipeline.joblib")# Loadmodel = joblib.load("booking_risk_pipeline.joblib")# Predictprediction = model.predict(X_test)
```

Only load trusted Joblib files because loading can execute arbitrary code.

## 5. Python Project Structure

A clean ML project can be organized as:

```
Day6/
│
├── main.py
├── ml_pipeline.py
├── booking_risk_pipeline.joblib
├── train.py
└── evaluation.py
```

- `main.py`: Application entry point.
- `ml_pipeline.py`: Pipeline definition.
- `train.py`: Model training.
- `evaluation.py`: Model performance evaluation.
- `.joblib`: Saved model artifact.

## 6. DSA — Stack

A stack follows LIFO (Last In, First Out).

Common operations:

```
stack = []stack.append(10)  # Pushstack.append(20)stack.pop()       # Remove 20print(stack[-1])  # Top element
```

Common applications:

- Valid parentheses.
- Undo operations.
- Browser history.
- Expression evaluation.

## 7. Git — Branching and commits

```
git checkout -b feature/ml-pipeline
git add .
git commit -m "Add ML pipeline"
git push -u origin feature/ml-pipeline
```

- Branch: Independent line of development.
- Commit: Saves a snapshot of changes.
- Push: Uploads commits to GitHub.
- Merge: Combines changes from branches.

## Day 6 revision checklist

Revision progress

0/7

Understand the ML pipeline workflow

Practice feature preprocessing

Calculate classification evaluation metrics

Save and load a model using Joblib

Understand project structure

Practice stack operations

Create and push a Git branch

Interview focus: Explain how an ML pipeline works, why preprocessing matters, how you evaluate a model, and how you save and reuse a trained model.