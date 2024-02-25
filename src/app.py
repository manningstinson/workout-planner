import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from database_config import DB_CONFIG  # Import database configuration

app = Flask(__name__)

# Function to create a connection to the MySQL database
def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG['url'])
    except mysql.connector.Error as e:
        print("Error connecting to the database:", e)
    return conn

# Route to display the form
@app.route('/')
def index():
    print("Rendering index.html")
    return render_template('index.html')

# Route to handle form submission
@app.route('/add_exercise', methods=['POST'])
def add_exercise():
    name = request.form['ex_name']
    difficulty = request.form['ex_difficulty']
    ex_type = request.form['ex_type']

    print("Received form data:", ex_name, ex_difficulty, ex_type)

    conn = create_connection()
    with conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO exercise (ex_name, ex_difficulty, ex_type) VALUES (%s, %s, %s)", (name, difficulty, ex_type))
            conn.commit()
            print("Exercise added to the database successfully")
        except mysql.connector.Error as e:
            print("Error adding exercise to the database:", e)

    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)
