import os
import mysql.connector

def create_connection():
    """
    Establishes a connection to the MySQL database 
    using the database URL from an environment variable.
    """
    # Get database URL from environment variable
    db_url = os.getenv('woplanner.DATABASE_URL')
    
    conn = None
    try:
        # Connect to the database using the provided URL
        conn = mysql.connector.connect(db_url)
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

# Test the connection (optional)
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        print("Connection successful!")
        # Close the connection after testing
        close_connection(conn)
    else:
        print("Connection failed!")
