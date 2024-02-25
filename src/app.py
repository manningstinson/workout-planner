from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create the exercises table if not exists
def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        type TEXT NOT NULL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

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

    conn = create_connection('exercises.db')
    with conn:
        create_table(conn)
        cur = conn.cursor()
        cur.execute("INSERT INTO exercises (name, difficulty, type) VALUES (?, ?, ?)", (name, difficulty, ex_type))
        conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
