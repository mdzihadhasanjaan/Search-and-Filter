import sqlite3
import bcrypt

# User Registration
def register_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    finally:
        conn.close()

# User Login
def login_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    result = cursor.fetchone()
    
    conn.close()

    if result:
        stored_password = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            print("Login successful!")
            return True
        else:
            print("Incorrect password!")
    else:
        print("Username not found!")

    return False
