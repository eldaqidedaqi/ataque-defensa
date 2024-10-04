
import sqlite3

def perform_sql_injection(user_input):
    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
    conn.execute("INSERT INTO users (id, username, password) VALUES (1, 'admin', 'password123')")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor = conn.execute(query)
    result = cursor.fetchall()
    if result:
        print(f"Logged in as: {result[0][1]}")
    else:
        print("Login failed!")
    conn.close()
perform_sql_injection("admin' OR '1'='1")
