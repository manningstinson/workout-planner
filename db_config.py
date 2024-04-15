def create_connection():
    # Print the value of _self.PORT for debugging
    port = os.getenv('workout-planner.PORT')
    print("Port number:", port)

    # Define database connection details using environment variables
    DB_CONFIG = {
        'hostname': os.getenv('workout-planner.HOSTNAME'),
        'port': int(port) if port else None,
        'username': os.getenv('workout-planner.USERNAME'),
        'password': os.getenv('workout-planner.PASSWORD'),
        'database': os.getenv('workout-planner.DATABASE'),
        'database_url': os.getenv('workout-planner.DATABASE_URL'),  # Add database URL
        'ca_cert': os.getenv('workout-planner.CA_CERT'),  # Add CA certificate
    }

    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(e)
    return conn
