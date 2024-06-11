import mysql.connector
from mysql.connector import Error
import bcrypt # type: ignore
import getpass

# Function to connect to the MySQL database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",  # Default MAMP password
            database="pwusers"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to create a new user
def create_user(connection, username, password, email):
    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s)", (username, hashed_password, email))
        connection.commit()
        print("User created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Function to authenticate a user
def authenticate_user(connection, username, password):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        print("Login successful!")
    else:
        print("Invalid username or password")

