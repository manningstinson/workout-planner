import os
import mysql.connector

def create_connection():
    """
    Establishes a connection to the MySQL database 
    using a connection string and environment variables.
    """
    connection_string = os.getenv("workoutplanner.DATABASE_URL")

    conn = None
    try:
        # Connect to the database using the provided connection string
        conn = mysql.connector.connect(connection_string)
    except mysql.connector.Error as e:
        print(e)

    return conn

def close_connection(conn):
    """
    Closes the database connection.
    """
    if conn:
        conn.close()
        print("Connection closed.")

# Add Flask Cors to requirements.txt
with open('requirements.txt', 'a') as file:
    file.write("Flask-Cors>=1.0.0\n")