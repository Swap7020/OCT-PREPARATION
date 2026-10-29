# Day 5 — Short Notes

Python Developer & AI/ML Developer Preparation

## 1. Input validation in Python

Validation ensures input meets the required conditions before processing.

```
def validate_features(features):    if not isinstance(features, int) or isinstance(features, bool):        raise ValueError("Features must be an integer")    if features < 30:        raise ValueError("At least 30 features required")    return 200
```

- `isinstance()` checks an object's type.
- `raise` signals an exception.
- `return` sends a result back.
- Validate types before performing operations such as `len()`.

Important: This example validates a feature count. For actual ML feature vectors, validate a list or array and its length.

## 2. Exception handling

```
try:    result = validate_features(20)except ValueError as error:    print(error)
```

- `try`: Runs code that may fail.
- `except`: Handles an exception.
- `ValueError`: Appropriate when a value is invalid.
- Avoid catching exceptions too broadly without a reason.

## 3. Unit testing with pytest

```
import pytestfrom validation import validate_featuresdef test_valid_input_returns_200():    assert validate_features(30) == 200def test_invalid_input_raises_error():    with pytest.raises(ValueError):        validate_features(20)
```

Run tests:

```
python -m pytest test_validation.py -v
```

Remember:

- Test functions should start with `test_`.
- `assert` checks expected output.
- `pytest.raises()` verifies exceptions.
- Aim to test valid inputs, invalid inputs, and boundary cases.

## 4. Machine learning feature validation

Features are input variables used by a model to make predictions.

Example: A house-price model might use area, bedrooms, and location-related variables.

Before prediction, verify:

- Correct number of features.
- Expected data types.
- No unexpected missing values.
- Valid ranges and consistent preprocessing.

## 5. HTTP status codes

| Code  | Meaning                   |
| ----- | ------------------------- |
| `200` | Request successful        |
| `201` | Resource created          |
| `400` | Bad request               |
| `404` | Resource not found        |
| `422` | Request validation failed |
| `500` | Internal server error     |

In FastAPI, use `HTTPException` to return appropriate HTTP errors rather than returning an error message with a success status.

## 6. Day 5 quick revision checklist

Understand input type and boundary validation

Use try/except and raise correctly

Write pytest success and failure tests

Run pytest and interpret failures

Understand ML feature validation

Review FastAPI status codes

0/6 completed

Interview tip: When a test fails, read the traceback from the assertion to the function that raised the error. Identify whether the issue is in the test expectation, the input, or the implementation before changing code.

Q1. What is model serialization?
Answer: Serialization converts a fitted model or another Python object into a stored representation that can be loaded later. In our exercise, joblib saves the trained pipeline so the API doesn't need to retrain it on every request.

Q2. Why should preprocessing be part of a scikit-learn pipeline?
Answer: A pipeline applies the same preprocessing consistently during training and prediction. When used correctly with cross-validation, it also helps prevent information leakage between training and validation folds.

Q3. What is the difference between POST and GET?
Answer: GET retrieves a resource or representation. POST submits data for processing or resource creation. Our prediction endpoint uses POST because it accepts a structured input payload for processing.

Q4. What happens if you load a model trained with a different feature order?
Answer: Predictions can become incorrect because each input value may be interpreted as the wrong feature. The API must enforce the expected feature order and input schema.

Q5. What is a database transaction, and why is it useful?
Answer: A transaction groups related database operations into a logical unit. It helps prevent partial updates when one operation fails, preserving the intended consistency of the data.