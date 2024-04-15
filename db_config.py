import os
import mysql.connector

def create_connection():
  """
  Establishes a connection to the MySQL database 
  using a connection string from an environment variable.
  """
  db_url = os.getenv('workout-planner.DATABASE_URL')  # Get connection string from environment variable
  conn = None
  try:
    conn = mysql.connector.connect(db_url)
  except mysql.connector.Error as e:
    print(e)
  return conn

# Test the connection
conn = create_connection()
if conn:
  print("Connection successful!")
else:
  print("Connection failed!")

# Close the connection (optional, recommended when connection is no longer needed)
if conn:
  conn.close()
  print("Connection closed.")
