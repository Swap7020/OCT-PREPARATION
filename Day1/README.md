# Day 1 Notes — Python Developer & AI/ML Developer Preparation

These notes cover your Day 1 preparation: Python fundamentals, coding problems, OOP, FastAPI, machine learning, SQL, DSA, and interview questions. Use them for revision and interview practice.

## 1. Python fundamentals

### Variables and data types

Variables store values in memory.

```
name = "Swapnil"       # strage = 23               # intcgpa = 7.01            # floatis_ready = True        # boolskills = ["Python", "SQL"]  # list
```

Common data types:

| Type    | Example         | Mutable? |
| ------- | --------------- | -------- |
| `int`   | `10`            | No       |
| `float` | `10.5`          | No       |
| `str`   | `"Python"`      | No       |
| `bool`  | `True`          | No       |
| `list`  | `[1, 2, 3]`     | Yes      |
| `tuple` | `(1, 2, 3)`     | No       |
| `set`   | `{1, 2, 3}`     | Yes      |
| `dict`  | `{"fare": 200}` | Yes      |

Mutable means an object can be modified after creation. Lists and dictionaries are mutable; strings and tuples are immutable.

### Lists, dictionaries, and sets

List: An ordered collection that allows duplicates.

```
fares = [200, 150, 300]fares.append(250)print(fares[0])  # 200
```

Dictionary: Stores key-value pairs.

```
booking = {    "booking_id": 1,    "status": "completed",    "fare": 200}print(booking["fare"])  # 200booking["fare"] = 250
```

Set: Stores unique values.

```
numbers = [1, 2, 2, 3, 3, 4]unique_numbers = set(numbers)print(unique_numbers)  # {1, 2, 3, 4}
```

### List vs tuple

- List: use when data needs to change.
- Tuple: use when data should remain fixed.
- Dictionary: use when values need to be accessed by keys.
- Set: use when you need unique values.

### Functions

Functions make code reusable.

```
def calculate_fare(distance):    if distance < 0:        raise ValueError("Distance cannot be negative")    return distance * 20print(calculate_fare(10))  # 200
```

Important concepts:

- `return` sends a result back to the caller.
- `raise` signals an exception.
- Parameters receive input.
- Arguments are the values passed when calling a function.

### Exception handling

```
try:    distance = int(input("Enter distance: "))    print(calculate_fare(distance))except ValueError as error:    print("Invalid input:", error)
```

Use `try` and `except` to handle errors instead of allowing expected input problems to crash your program.

## 2. Python coding practice

### Problem 1: Count character frequencies

```
def character_frequency(text):    frequency = {}    for char in text:        frequency[char] = frequency.get(char, 0) + 1    return frequencyprint(character_frequency("python"))
```

Output:

```
{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
```

`dict.get(key, 0)` returns the existing count or `0` when the key is missing.

### Problem 2: Find the second-largest distinct number

```
def second_largest(numbers):    unique = sorted(set(numbers))    if len(unique) < 2:        return None    return unique[-2]print(second_largest([10, 20, 20, 5, 15]))
```

Output:

```
15
```

The set removes duplicates, sorting arranges the numbers, and `[-2]` accesses the second-last element.

### Problem 3: Find a palindrome

A palindrome reads the same forward and backward.

```
def is_palindrome(text):    text = text.lower()    return text == text[::-1]print(is_palindrome("madam"))  # Trueprint(is_palindrome("python")) # False
```

`[::-1]` reverses a sequence.

### Problem 4: Filter completed bookings

```
bookings = [    {"id": 1, "status": "completed", "fare": 200},    {"id": 2, "status": "pending", "fare": 150},    {"id": 3, "status": "completed", "fare": 300}]completed_ids = [    booking["id"]    for booking in bookings    if booking["status"] == "completed"]print(completed_ids)
```

Output:

```
[1, 3]
```

This is called a list comprehension.

### Problem 5: Count completed bookings

```
completed_count = sum(    1 for booking in bookings    if booking["status"] == "completed")print(completed_count)  # 2
```

Remember: `sum()` can count matching items by adding `1` for each match.

## 3. Object-oriented programming (OOP)

OOP organizes code around classes and objects.

- Class: A blueprint.
- Object: An instance of a class.
- Attribute: Data stored on an object.
- Method: A function defined inside a class.
- `self`: Refers to the current object.

Example:

```
class Booking:    def __init__(self, booking_id, status, fare):        self.booking_id = booking_id        self.status = status        self.fare = fare    def complete_booking(self):        self.status = "completed"booking1 = Booking(1, "pending", 200)booking1.complete_booking()print(booking1.status)  # completed
```

Four major OOP principles:

1. Encapsulation: Group data and methods together.
2. Inheritance: Create a class based on another class.
3. Polymorphism: Different objects can implement the same interface differently.
4. Abstraction: Hide implementation details and expose essential functionality.

Interview tip: Be ready to explain why you might use a `Booking` class rather than storing every operation in unrelated functions.

## 4. FastAPI basics

FastAPI is a Python framework for building APIs. It supports request validation through Pydantic and generates API documentation.

### Create a simple API

Install dependencies:

```
python -m pip install fastapi uvicorn
```

Create `main.py`:

```
from fastapi import FastAPIapp = FastAPI()@app.get("/health")def health_check():    return {"status": "healthy"}@app.get("/estimate-fare")def estimate_fare(distance: float):    if distance < 0:        return {"error": "Distance cannot be negative"}    return {"estimated_fare": distance * 20}
```

Run the application:

```
python -m uvicorn main:app --reload
```

Open:

- API: `http://127.0.0.1:8000/health`
- Interactive documentation: `http://127.0.0.1:8000/docs`
- Fare example: `http://127.0.0.1:8000/estimate-fare?distance=10`

Expected fare response:

```
{"estimated_fare": 200.0}
```

For a production-quality API, use `HTTPException` for error responses and Pydantic models to validate structured request bodies.

Important HTTP methods

| Method   | Purpose                     |
| -------- | --------------------------- |
| `GET`    | Retrieve data               |
| `POST`   | Create a resource           |
| `PUT`    | Replace a resource          |
| `PATCH`  | Partially update a resource |
| `DELETE` | Delete a resource           |

## 5. Machine learning fundamentals

### Supervised vs unsupervised learning

| Supervised learning                  | Unsupervised learning                   |
| ------------------------------------ | --------------------------------------- |
| Uses labelled data                   | Uses unlabelled data                    |
| Learns input-to-target relationships | Finds patterns or structure             |
| Classification and regression        | Clustering and dimensionality reduction |
| Example: Predict house prices        | Example: Group customers by behavior    |

Classification: Predicts a category, such as spam or not spam.

Regression: Predicts a numeric value, such as a fare or house price.

### Train-test split

Training data is used to fit the model. Test data estimates how well the trained model generalizes to unseen data.

```
from sklearn.datasets import load_irisfrom sklearn.model_selection import train_test_splitfrom sklearn.linear_model import LogisticRegressionfrom sklearn.metrics import accuracy_scoreiris = load_iris()X = iris.datay = iris.targetX_train, X_test, y_train, y_test = train_test_split(    X, y,    test_size=0.2,    random_state=42,    stratify=y)model = LogisticRegression(max_iter=1000)model.fit(X_train, y_train)predictions = model.predict(X_test)print("Accuracy:", accuracy_score(y_test, predictions))
```

### Key ML concepts

- Overfitting: Performs well on training data but poorly on unseen data.
- Underfitting: Model is too simple to learn the underlying pattern.
- Data leakage: Information from outside the legitimate training process improperly influences model training or evaluation.
- Accuracy: Fraction of predictions that are correct.
- Precision: Of predicted positives, how many were actually positive?
- Recall: Of actual positives, how many did the model find?
- F1-score: Harmonic mean of precision and recall.

Avoid fitting preprocessing steps on the full dataset before splitting. Fit them on training data only, preferably using a scikit-learn pipeline.

## 6. SQL fundamentals

Use SQL to filter, group, and summarize database records.

Assume this table:

`booking(booking_id, status, fare)`

| booking_id | status    | fare |
| ---------- | --------- | ---- |
| 1          | completed | 200  |
| 2          | pending   | 150  |
| 3          | completed | 300  |
| 4          | cancelled | 100  |
| 5          | completed | 250  |

### Basic queries

```
-- Retrieve all bookings
SELECT * FROM booking;

-- Filter completed bookings
SELECT *
FROM booking
WHERE status = 'completed';

-- Calculate total fare
SELECT SUM(fare) AS total_fare
FROM booking;

-- Count bookings by status
SELECT status, COUNT(*) AS booking_count
FROM booking
GROUP BY status;

-- Find statuses with at least two bookings
SELECT status, COUNT(*) AS booking_count
FROM booking
GROUP BY status
HAVING COUNT(*) >= 2;

-- Sort fares from highest to lowest
SELECT *
FROM booking
ORDER BY fare DESC;
```

### WHERE vs HAVING

- `WHERE` filters rows before grouping.
- `HAVING` filters groups after `GROUP BY`.

### SQL execution order to remember

Conceptually, the common order is:

`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`

This helps explain why aggregate conditions such as `COUNT(*) >= 2` usually belong in `HAVING`, not `WHERE`.

## 7. DSA fundamentals

### Time complexity

Time complexity describes how an algorithm's running time grows as the input grows.

| Complexity       | Example                               |
| ---------------- | ------------------------------------- |
| \\(O(1)\\)       | Access an item by list index          |
| \\(O(\log n)\\)  | Binary search on sorted data          |
| \\(O(n)\\)       | Scan a list once                      |
| \\(O(n\log n)\\) | Efficient comparison sorting          |
| \\(O(n^2)\\)     | Compare every pair using nested loops |

### Merge overlapping intervals

```
def merge_intervals(intervals):    if not intervals:        return []    intervals.sort(key=lambda interval: interval[0])    merged = [intervals[0]]    for current in intervals[1:]:        last = merged[-1]        if current[0] <= last[1]:            last[1] = max(last[1], current[1])        else:            merged.append(current)    return mergedintervals = [    [1, 3],    [2, 6],    [8, 10],    [9, 12]]print(merge_intervals(intervals))
```

Output:

```
[[1, 6], [8, 12]]
```

The intervals `[1, 3]` and `[2, 6]` overlap, so they merge into `[1, 6]`. The same process merges `[8, 10]` and `[9, 12]` into `[8, 12]`.

Time complexity: \\(O(n\log n)\\) because of sorting.

## 8. Git and GitHub

Git tracks code changes; GitHub hosts repositories online.

```
git init
git status
git add .
git commit -m "Complete Day 1 preparation"
git branch
```

To connect an existing local repository to GitHub, create a repository on GitHub, then use its actual URL:

```
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin master
```

Replace the URL with your repository URL. If your branch is named `main`, use `main` instead of `master`.

Add a `.gitignore` file to exclude generated files and secrets:

```
__pycache__/
*.py[cod]
.venv/
venv/
.env
.pytest_cache/
```

Never commit API keys, passwords, or other credentials.

## 9. Day 1 interview questions

Try answering these without looking at the notes.

1\. What is the difference between a list and a tuple?

Reveal answer

2\. What is the difference between == and is in Python?

Reveal answer

3\. What is the difference between return and raise?

Reveal answer

4\. Why do we split data into training and testing sets?

Reveal answer

5\. What is the difference between WHERE and HAVING?

Reveal answer

6\. What is an API endpoint?

Reveal answer

7\. What is overfitting?

Reveal answer

8\. What does a Python dictionary store?

Reveal answer

## 10. Day 1 completion checklist

### Day 1 revision tracker

0/8 completed

Revise Python data types, lists, dictionaries, and functions

Write the character-frequency and second-largest programs

Implement a Booking class

Run a FastAPI health-check endpoint

Train an Iris classification baseline and calculate accuracy

Write a SQL GROUP BY query

Solve the palindrome problem

Commit Day 1 code to Git

Revision advice: Focus first on explaining your code in your own words, then practice writing it without copying. For fresher Python Developer and AI/ML interviews, understanding the logic is more valuable than memorizing the output.