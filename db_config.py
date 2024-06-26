import mysql.connector

def create_connection():
    """
    Establishes a connection to the MySQL database using individual connection parameters.
    """
    # Database connection parameters
    db_config = {
        'host': 'db-mysql-nyc3-35936-do-user-15450315-0.c.db.ondigitalocean.com',
        'user': 'doadmin',
        'password': 'AVNS_utNfcoxxn5nK7Qcx-kB',
        'database': 'defaultdb',
        'port': 25060,
    }

    conn = None
    try:
        # Connect to the database using the provided parameters
        conn = mysql.connector.connect(**db_config)
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