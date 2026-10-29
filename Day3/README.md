# Day 3 — Short Notes

Python Developer & AI/ML Developer Preparation

## 1. FastAPI testing

FastAPI lets you build APIs, and `pytest` helps verify that endpoints behave correctly.

```
from fastapi.testclient import TestClientfrom main import appclient = TestClient(app)def test_health():    response = client.get("/health")    assert response.status_code == 200
```

Run tests:

```
python -m pytest -v
```

Remember:

- `200` — successful request.
- `404` — resource not found.
- `422` — validation error.
- Test valid inputs, invalid inputs, and edge cases.

## 2. Python generators

A generator uses `yield` to produce values one at a time.

```
def high_value_bookings(bookings, minimum_fare):    for booking in bookings:        if booking["status"] == "completed" and booking["fare"] >= minimum_fare:            yield booking
```

Benefit: Memory-efficient processing of large datasets.

## 3. SQL ranking functions

```
SELECT booking_id, status, fare,
       RANK() OVER (
           PARTITION BY status
           ORDER BY fare DESC
       ) AS fare_rank
FROM booking;
```

- `RANK()` — ties share a rank; gaps follow.
- `DENSE_RANK()` — ties share a rank; no gaps.
- `ROW_NUMBER()` — every row gets a unique number.
- `PARTITION BY` creates separate ranking groups.

## 4. Regression evaluation metrics

| Metric    | Meaning                                            |
| --------- | -------------------------------------------------- |
| MAE       | Average absolute prediction error                  |
| MSE       | Average squared prediction error                   |
| RMSE      | Square root of MSE; same units as target           |
| \\(R^2\\) | Performance relative to predicting the target mean |

Key points:

- Lower MAE and RMSE are generally better.
- \\(R^2=1\\) means perfect predictions.
- \\(R^2=0\\) means performance equivalent to the test-set mean baseline.
- Negative \\(R^2\\) means worse than that baseline.

## 5. Python unit testing

```
import pytestdef calculate_fare(distance):    if distance <= 0:        raise ValueError("Distance must be positive")    return distance * 20def test_valid_fare():    assert calculate_fare(10) == 200def test_invalid_distance():    with pytest.raises(ValueError):        calculate_fare(0)
```

Save as `test_fare.py` and run:

```
python -m pytest test_fare.py -v
```

Important: Pytest normally discovers test files named `test_*.py` or `*_test.py` and test functions beginning with `test_`.

## 6. Git essentials

```
git status
git add .
git commit -m "Complete Day 3 practice"
git log --oneline
git push
```

- `add` stages changes.
- `commit` saves a local snapshot.
- `push` uploads commits to a configured remote repository.

## Day 3 completion checklist

Run FastAPI endpoint tests

Implement the booking generator

Write the SQL RANK query

Calculate and record regression metrics

Run Python unit tests

Commit practice code to Git

0/6 completed

Interview focus: Be able to explain how you test an API, why generators save memory, how SQL ranking works, and how to interpret MAE, RMSE, and \\(R^2\\).

MAE: Average absolute prediction error.
RMSE: Error metric that penalizes large errors more heavily.
R²: Measures model performance relative to the mean-prediction baseline.
Negative R²: Worse than the mean baseline on the evaluated dataset.
Test-set discipline: Keep test data independent of model selection.