import os
import mysql.connector

def create_connection():
    """
    Establishes a connection to the MySQL database 
    using a connection string and environment variables.
    """
    # Get the database connection string from the environment variable
    connection_string = os.getenv("workoutplanner.DATABASE_URL")

    conn = None
    try:
        # Connect to the database using the provided connection string
        conn = mysql.connector.connect(host=connection_string)
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")

    return conn

def close_connection(conn):
    """
    Closes the database connection.
    """
    if conn:
        conn.close()
        print("Connection closed.")