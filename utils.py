import sqlite3

def authenticate(username, password):
    conn = sqlite3.connect('moba.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    stored_password = cursor.fetchone()
    conn.close()
    
    return stored_password and stored_password[0] == password

def is_authenticated(session_state):
    return session_state.get('authenticated', False)

def login(session_state, username, password):
    if authenticate(username, password):
        session_state.authenticated = True
        session_state.username = username
    else:
        session_state.authenticated = False
