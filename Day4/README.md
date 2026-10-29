# Day 4 — Short Notes

Python Developer & AI/ML Developer Preparation

## 1. FastAPI CRUD operations

CRUD stands for Create, Read, Update, and Delete.

| Operation | HTTP method     | Purpose                     |
| --------- | --------------- | --------------------------- |
| Create    | `POST`          | Add a booking               |
| Read      | `GET`           | Retrieve a booking          |
| Update    | `PUT` / `PATCH` | Replace or partially update |
| Delete    | `DELETE`        | Remove a booking            |

Example using FastAPI:

```
from fastapi import FastAPI, HTTPExceptionfrom pydantic import BaseModel, Fieldapp = FastAPI()bookings = {    1: {"booking_id": 1, "status": "pending", "fare": 200}}class BookingUpdate(BaseModel):    status: str = Field(        pattern="^(pending|completed|cancelled)$"    )@app.get("/bookings/{booking_id}")def get_booking(booking_id: int):    if booking_id not in bookings:        raise HTTPException(status_code=404, detail="Booking not found")    return bookings[booking_id]@app.patch("/bookings/{booking_id}")def update_booking(booking_id: int, update: BookingUpdate):    if booking_id not in bookings:        raise HTTPException(status_code=404, detail="Booking not found")    bookings[booking_id]["status"] = update.status    return bookings[booking_id]
```

Key points:

- `HTTPException` returns an appropriate HTTP error.
- Pydantic validates incoming request data.
- A dictionary is suitable for practice; real applications generally use a database.

## 2. Unit testing with pytest

Unit tests check whether individual functions work correctly.

```
import pytestdef calculate_fare(distance):    if distance <= 0:        raise ValueError("Distance must be positive")    return distance * 20def test_valid_fare():    assert calculate_fare(10) == 200def test_invalid_fare():    with pytest.raises(ValueError):        calculate_fare(0)
```

Run:

```
python -m pytest -v
```

Remember:

- Test functions should start with `test_`.
- Use `assert` to check expected results.
- Use `pytest.raises()` to check exceptions.
- If pytest reports 0 items collected, check the test filename and function names.

## 3. SQL — Aggregation and window functions

Aggregate functions: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.

```
SELECT status, COUNT(*) AS total_bookings,
       AVG(fare) AS average_fare
FROM booking
GROUP BY status;
```

Rank bookings by fare:

```
SELECT booking_id, fare,
       RANK() OVER (ORDER BY fare DESC) AS fare_rank
FROM booking;
```

- `GROUP BY` combines rows into groups.
- `HAVING` filters groups.
- `PARTITION BY` separates window-function calculations into groups.
- `ORDER BY` determines the ranking order.

## 4. Python debugging and exceptions

Use clear exceptions to handle invalid input.

```
def calculate_fare(distance):    if distance <= 0:        raise ValueError("Distance must be positive")    return distance * 20try:    print(calculate_fare(-5))except ValueError as error:    print(error)
```

Output:

```
Distance must be positive
```

Interview tip: Explain the difference between `return`, `raise`, `try`, and `except`.

## 5. Git and GitHub

```
git status
git add .
git commit -m "Complete Day 4 practice"
git log --oneline
git push
```

- `git status`: view changed files.
- `git add`: stage changes.
- `git commit`: save a local snapshot.
- `git push`: upload commits to a configured remote.

Add a `.gitignore` file to exclude generated files and secrets:

```
__pycache__/
*.py[cod]
.venv/
.env
.pytest_cache/
```

Never commit passwords or API keys.

## 6. Day 4 quick revision checklist

Implement a FastAPI GET endpoint

Implement and test a PATCH endpoint

Write valid and invalid pytest cases

Write a SQL aggregation query

Handle invalid inputs with exceptions

Check Git status and commit changes

0/6 completed

Day 4 interview focus: Be ready to build a simple API, validate requests, test error cases, write SQL aggregation queries, and explain how you debug code.


Question 1: What is dependency injection in FastAPI?
Answer: Dependency injection lets an endpoint declare the resources or services it needs. FastAPI resolves those dependencies and supplies them to the endpoint.
For example, Depends(get_db) provides a database connection without requiring the endpoint to create and manage that connection itself.

Question 2: Why use parameterised SQL queries?
Answer: Parameterised queries separate SQL instructions from supplied values. They help prevent SQL injection and handle values correctly.

For example:
conn.execute(    "SELECT * FROM bookings WHERE booking_id = ?",    (booking_id,))
Avoid constructing SQL statements by concatenating untrusted user input.

Question 3: What is the difference between precision and recall?
Answer: Precision measures how many predicted positives are correct. Recall measures how many actual positives are identified.
High precision is particularly useful when false positives are costly. High recall is important when missing positive cases is costly.

Question 4: Why use a database instead of a Python dictionary?
Answer: A dictionary is useful for temporary in-memory data. A database supports persistent storage, structured queries, transactions, and better coordination between application operations.

Question 5: What is the difference between unit testing and integration testing?
Answer: Unit tests check a small component in isolation, such as a fare calculation function. Integration tests check whether multiple components work together, such as a FastAPI endpoint interacting with SQLite.