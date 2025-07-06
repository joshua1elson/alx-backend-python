# 3-avg_age.py

import mysql.connector

def stream_user_ages():
    """Generator that yields user ages one by one."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your password
        database="ALX_prodev"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield age

    cursor.close()
    connection.close()

def calculate_average_age():
    """Calculates and prints the average age using the generator."""
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")

# Only run if script is executed directly
if __name__ == "__main__":
    calculate_average_age()
