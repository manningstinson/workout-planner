import os
import mysql.connector

# Define database connection details using environment variables
DB_CONFIG = {
    'host': os.getenv('_self.HOSTNAME'),
    'port': os.getenv('_self.PORT'),  # Keep the port as a string
    'user': os.getenv('_self.USERNAME'),
    'password': os.getenv('_self.PASSWORD'),
    'database': os.getenv('_self.DATABASE'),
    'database_url': os.getenv('_self.DATABASE_URL'),  # Corrected key name
    'ssl_ca': os.getenv('_self.CA_CERT'),
}

def create_connection():
    conn = None
    try:
        # Check if the port environment variable is set and not None
        if DB_CONFIG['port'] is not None:
            # Convert the port to an integer if it's not None
            DB_CONFIG['port'] = int(DB_CONFIG['port'])
        conn = mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(e)
    return conn