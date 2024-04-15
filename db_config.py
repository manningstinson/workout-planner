import os
import mysql.connector

def create_connection():
    # Define database connection details using environment variables
    DB_CONFIG = {
        'hostname': os.getenv('workout-planner.HOSTNAME'),
        'port': int(os.getenv('workout-planner.PORT')),  # Ensure port is converted to int
        'username': os.getenv('workout-planner.USERNAME'),
        'password': os.getenv('workout-planner.PASSWORD'),
        'database': os.getenv('workout-planner.DATABASE'),
        'database_url': os.getenv('workout-planner.DATABASE_URL'),
        'ca_cert': os.getenv('workout-planner.CA_CERT'),
    }

    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(e)
    return conn
