import sqlite3

conn = sqlite3.connect("practice.db")

try:
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS practice_bookings (
                booking_id INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                fare REAL NOT NULL CHECK (fare >= 0)
            )
        """)

        conn.execute(
            """
            INSERT INTO practice_bookings
                (booking_id, customer_name, fare)
            VALUES (?, ?, ?)
            """,
            (1, "Rahul", 200),
        )

        conn.execute(
            """
            INSERT INTO practice_bookings
                (booking_id, customer_name, fare)
            VALUES (?, ?, ?)
            """,
            (2, "Priya", 150),
        )

    print("Transaction committed")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    conn.close()