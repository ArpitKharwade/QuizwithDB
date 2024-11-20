import sqlite3
import hashlib

def create_user_db():
    """
    Creates the 'users.db' database and the 'users' table if it doesn't exist.
    """
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Create 'users' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT)''')

    conn.commit()
    conn.close()

def register_user(username, password):
    """
    Registers a new user by storing the username and hashed password in the 'users.db' database.
    """
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Insert the username and hashed password into the 'users' table
        c.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, hashed_password))
        conn.commit()
        print(f"User {username} registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")

    conn.close()

def login_user(username, password):
    """
    Verifies a user's login credentials by checking the hashed password.
    """
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Hash the entered password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    c.execute('''SELECT password FROM users WHERE username=?''', (username,))
    stored_password = c.fetchone()

    conn.close()

    if stored_password and stored_password[0] == hashed_password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid credentials!")
        return False

# Call the function to set up the user database (run this once)
create_user_db()
