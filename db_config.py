import os
import mysql.connector

# Define database connection details using environment variables
DB_CONFIG = {
    'host': os.getenv('_self.HOSTNAME'),
    'port': os.getenv('_self.PORT'),  # Retrieve port from environment variable
    'user': os.getenv('_self.USERNAME'),
    'password': os.getenv('_self.PASSWORD'),
    'database': os.getenv('_self.DATABASE'),
    'database_url': os.getenv('_self.DATABASE_URL'),  # Corrected key name
    'ssl_ca': os.getenv('_self.CA_CERT'),
}

def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(e)
    return conn