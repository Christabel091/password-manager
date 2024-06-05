#reference on how the database works.
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pwusers"
)

# Create cursor object
cursor = conn.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
"""
cursor.execute(create_table_query)

# Get user information
name = input("Enter your name: ")
password = input("Enter your password: ")

# Insert user information into the database
insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
cursor.execute(insert_query, (name, password))

# Commit changes
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()
