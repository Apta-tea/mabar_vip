import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('moba.db')

# Create a cursor object
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert a sample user (for demonstration purposes)
cursor.execute('''
    INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)
''', ('user', 'pass'))

# Commit and close the connection
conn.commit()
conn.close()
