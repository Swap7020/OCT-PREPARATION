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