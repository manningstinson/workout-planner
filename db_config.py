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

    # Debugging: Print DB_CONFIG
    print("DB_CONFIG:")
    for key, value in DB_CONFIG.items():
        print(f"{key}: {value}")

    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(e)
    return conn

# Test the connection
conn = create_connection()
if conn:
    print("Connection successful!")
else:
    print("Connection failed!")
