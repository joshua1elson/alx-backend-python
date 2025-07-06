 """def batch_users(batch_size=100, min_age=50):
    ..."""


# 1-batch_processing.py

import mysql.connector

def batch_users(batch_size=100, min_age=50):
    """Generator that yields batches of users with age > min_age"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # ← Replace with your MySQL password
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data WHERE age > %s", (min_age,))

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:  # yield remaining rows if any
        yield batch

    cursor.close()
    connection.close()
