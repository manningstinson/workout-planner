from flask import Flask, render_template, request, redirect, url_for
from db_config import create_connection  # Import database configuration

app = Flask(__name__, static_url_path='/static')  # Define static route

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

    conn = create_connection()
    with conn:
        cur = conn.cursor()
        try:
            # Use parameterized query to prevent SQL injection
            cur.execute("INSERT INTO exercise (ex_name, ex_difficulty, ex_type) VALUES (%s, %s, %s)", (ex_name, ex_difficulty, ex_type))
            conn.commit()
            print("Exercise added to the database successfully")
        except mysql.connector.Error as e:
            print("Error adding exercise to the database:", e)

return redirect(url_for('test'))

if __name__ == '__main__':
    # Specify the desired host and port here
    app.run(debug=False, host='0.0.0.0', port=8080)