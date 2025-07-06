# 0-stream_users.py

import mysql.connector

def stream_users():
    """Generator that yields user records one by one from user_data table."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # <-- replace with your MySQL password
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
