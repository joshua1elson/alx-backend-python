# 2-lazy_paginate.py

seed = __import__('seed')

def paginate_users(page_size, offset):
    """Fetch a page of users from user_data."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """Generator that lazily paginates user_data one page at a time."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
