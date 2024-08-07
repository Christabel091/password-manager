import mysql.connector
from mysql.connector import Error
import bcrypt # type: ignore

def create_connection():
    connection = None
    try:
        #For MAMP
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",  
            database="pwusers"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_user(connection, username, password, email):
    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s)", (username, hashed_password, email))
        connection.commit()
        print("User created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def authenticate_user(connection, username, password):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT user_id, password_hash FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        print("Login successful!")
        return user['user_id']
    else:
        print("Invalid username or password")
        return None

def get_user_id(connection, username):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()    
    return user['user_id'] if user else None

def store_password(connection, user_id, password):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO passwords (user_id, password) VALUES (%s, %s)", (user_id, password))
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def store_platform(connection, user_id, password_id, platform):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO platforms (user_id, password_id, platform) VALUES (%s, %s, %s)", (user_id, password_id, platform))
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")

def retrievePassword(connection, platform, user_id):
    cursor = connection.cursor(dictionary=True)  # a dictionary cursor
    try:
        cursor.execute("SELECT password_id FROM platforms WHERE platform = %s AND user_id = %s", (platform, user_id))
        id_result = cursor.fetchone()
        if id_result:
            password_id = id_result["password_id"]
            cursor.execute("SELECT password FROM passwords WHERE password_id = %s", (password_id,))
            password_result = cursor.fetchone()
            return password_result['password'] if password_result else None
    except Error as e:
        print(f"The error '{e}' occurred")

def passwordReuse(connection, user_id):
    cursor = connection.cursor()
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT passwords.password
            FROM passwords
            JOIN users ON passwords.user_id = users.user_id
            WHERE users.user_id = %s
            """
            cursor.execute(query, (user_id,))
            passwords = cursor.fetchall()
            return passwords
        
        
    except Error as e:
         print(f"The error '{e}' occoured ")

def passwordChange(connection, user_id, platform, new_password):
    cursor = connection.cursor()
    try:
        # Start a transaction
        connection.start_transaction()
        
        # Retrieve the password_id from the platforms table
        query = """
        SELECT password_id
        FROM platforms
        WHERE user_id = %s AND platform = %s
        """
        cursor.execute(query, (user_id, platform))
        result = cursor.fetchone()
        
        if result:        
            password_id = result[0]
            
            
            update_query = """
            UPDATE passwords
            SET password = %s
            WHERE password_id = %s
            """
            cursor.execute(update_query, (new_password, password_id))
            connection.commit()
            return True
        else:
            connection.rollback()
            print("No matching password found for the specified platform.")
            print("You may have to create a fresh password for the platform ot try sgain.")
            return False
    except Error as e:
        # Error handling
        connection.rollback()
        print(f"The error '{e}' occurred")
        return False
    finally:
        cursor.close()
