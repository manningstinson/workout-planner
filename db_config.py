import os
import mysql.connector

def create_connection():
    # Print the value of _self.PORT for debugging
    port = os.getenv('_self.PORT')
    print("Port number:", port)

    # Define database connection details using environment variables
    DB_CONFIG = {
        'host': os.getenv('_self.HOSTNAME'),
        'port': port,
        'username': os.getenv('_self.USERNAME'),
        'password': os.getenv('_self.PASSWORD'),
        'database': os.getenv('_self.DATABASE'),
        'ssl_mode': 'REQUIRED',  # Set SSL mode to 'REQUIRED'
    }

    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(e)
    return conn