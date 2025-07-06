"""first""" """pip install mysql-connector-python"""
"""it should be running and accessible"""


import mysql.connector
import csv
import uuid

def connect_db():
    """Connect to MySQL server."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Replace with your actual password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Create ALX_prodev database if not exists."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database created or already exists")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

def connect_to_prodev():
    """Connect to ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your actual password
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Create user_data table if not exists."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            )
        """)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed to create table: {err}")

def insert_data(connection, csv_file):
    """Insert data into user_data from CSV."""
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cursor.execute("""
                    SELECT COUNT(*) FROM user_data WHERE email = %s
                """, (row["email"],))
                if cursor.fetchone()[0] == 0:
                    uid = str(uuid.uuid4())
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (uid, row["name"], row["email"], row["age"]))
        connection.commit()
        print("Data inserted successfully")
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")



"""Ensure your user_data.csv is in the same directory as 0-main.py, or adjust the path."""
"""./0-main.py"""

