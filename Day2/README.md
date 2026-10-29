# Day 2 — Short Notes

Python Developer & AI/ML Developer Preparation

## 1. Python advanced concepts

List comprehension: Create a list in one line.

```
squares = [x**2 for x in range(1, 6)]# [1, 4, 9, 16, 25]
```

Dictionary comprehension:

```
squares = {x: x**2 for x in range(1, 4)}# {1: 1, 2: 4, 3: 9}
```

Lambda function: Small anonymous function.

```
square = lambda x: x * xprint(square(5))  # 25
```

Generator: Produces values one at a time using `yield`, saving memory for large sequences.

```
def numbers():    for i in range(3):        yield i
```

Decorator: Wraps a function to add behavior without changing its main code.

```
def log_call(func):    def wrapper():        print("Function called")        return func()    return wrapper
```

## 2. Object-oriented programming

- Inheritance: A child class reuses functionality from a parent class.
- Encapsulation: Combines data and methods in a class.
- Polymorphism: Same interface, different implementations.
- Abstraction: Hides implementation details.

```
class Booking:    def __init__(self, fare):        self.fare = fare    def get_fare(self):        return self.farebooking = Booking(200)print(booking.get_fare())
```

## 3. SQL — Joins and ranking

INNER JOIN: Returns matching rows from both tables.

LEFT JOIN: Returns all rows from the left table, with matching right-table data where available.

```
SELECT b.booking_id, c.customer_name
FROM booking b
LEFT JOIN customers c
ON b.customer_id = c.customer_id;
```

Window function: Calculates rankings without collapsing individual rows.

```
SELECT booking_id, fare,
       RANK() OVER (ORDER BY fare DESC) AS fare_rank
FROM booking;
```

- `ROW_NUMBER()` — unique sequential number.
- `RANK()` — ties share a rank, leaving gaps.
- `DENSE_RANK()` — ties share a rank, without gaps.

## 4. Machine learning

Overfitting: High training performance but poor test performance.

Underfitting: Poor performance on both training and test data.

Cross-validation: Evaluates a model across multiple train-validation splits.

Regularization: Penalizes model complexity to help reduce overfitting.

Data leakage: Test or future information improperly influences training.

Common evaluation metrics:

| Task           | Metrics                               |
| -------------- | ------------------------------------- |
| Classification | Accuracy, precision, recall, F1-score |
| Regression     | MAE, MSE, RMSE, \\(R^2\\)             |

## 5. FastAPI and API testing

Pydantic: Validates and parses incoming data using models.

```
from pydantic import BaseModel, Fieldclass BookingCreate(BaseModel):    fare: float = Field(gt=0)    status: str
```

HTTP status codes:

- `200` — success
- `201` — resource created
- `400` — bad request
- `404` — resource not found
- `422` — request validation error
- `500` — internal server error

Testing with pytest:

```
def test_addition():    assert 2 + 3 == 5
```

Run tests:

```
python -m pytest -v
```

Test valid inputs, invalid inputs, boundary conditions, and expected exceptions.

## 6. DSA — Time complexity

| Complexity       | Example                 |
| ---------------- | ----------------------- |
| \\(O(1)\\)       | List index access       |
| \\(O(n)\\)       | Linear search           |
| \\(O(n\log n)\\) | Sorting                 |
| \\(O(n^2)\\)     | Nested-loop comparisons |

Merge overlapping intervals: Sort intervals by start time, then merge each interval if it overlaps the previous one.

```
if current[0] <= last[1]:    last[1] = max(last[1], current[1])
```

## Day 2 quick revision checklist

Practice list and dictionary comprehensions

Explain generators and decorators

Write INNER JOIN and LEFT JOIN queries

Explain RANK versus DENSE_RANK

Revise overfitting and regression metrics

Create a Pydantic model and test an API

Run pytest successfully

0 of 7 completed

Interview tip: Don't just memorize definitions. Practise explaining each concept and writing a small working example without looking at the notes.