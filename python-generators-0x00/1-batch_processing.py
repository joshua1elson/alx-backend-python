# 1-batch_processing.py

import mysql.connector

def stream_users_in_batches(batch_size=100):
    """Generator: Yields users in batches where age > 25"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your actual password
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data WHERE age > 25")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:  # Yield any remaining users
        yield batch

    cursor.close()
    connection.close()

def batch_processing():
    """Example function that consumes the generator (age > 25)."""
    for batch in stream_users_in_batches():
        for user in batch:
            print(user)


grep return 1-batch_processing.py
