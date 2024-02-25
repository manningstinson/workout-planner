# app.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database_config import DB_CONFIG  # Import database configuration

app = Flask(__name__)

# Function to create a connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_CONFIG['database'])
    except sqlite3.Error as e:
        print(e)
    return conn

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/add_exercise', methods=['POST'])
def add_exercise():
    name = request.form['ex_name']
    difficulty = request.form['ex_difficulty']
    ex_type = request.form['ex_type']

    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO exercises (ex_name, ex_difficulty, ex_type) VALUES (?, ?, ?)", (name, difficulty, ex_type))
        conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
