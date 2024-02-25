from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from database_config import create_connection  # Import the create_connection function from database_config module

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/add_exercise', methods=['POST'])
def add_exercise():
    # Retrieve form data using request.form
    ex_name = request.form['ex_name']
    ex_difficulty = request.form['ex_difficulty']
    ex_type = request.form['ex_type']

    # Print the received form data for debugging
    print("Received form data:", ex_name, ex_difficulty, ex_type)

    # Create a connection to the database
    conn = create_connection()
    if conn is None:
        return "Error connecting to the database"

    # Create a cursor object
    cur = conn.cursor()

    try:
        # Execute the INSERT query
        cur.execute("INSERT INTO exercise (ex_name, ex_difficulty, ex_type) VALUES (%s, %s, %s)", (ex_name, ex_difficulty, ex_type))
        conn.commit()  # Commit the transaction
        print("Exercise added to the database successfully")
    except mysql.connector.Error as e:
        print("Error adding exercise to the database:", e)
        conn.rollback()  # Rollback the transaction in case of an error
    finally:
        cur.close()  # Close the cursor
        conn.close()  # Close the connection

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
