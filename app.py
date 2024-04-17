import logging
from flask import Flask, render_template
from routes.submit_exercise import submit_exercise_function
from routes.retrieve_exercise import retrieve_exercise_function

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_exercise')
def submit_exercise():
    try:
        conn = create_connection()  # Create a database connection
        return submit_exercise_function(conn)  # Pass the connection to the function
    except Exception as e:
        logging.error(f"Error submitting exercise: {e}")
        return render_template('error.html')

@app.route('/retrieve_exercise')
def retrieve_exercise():
    try:
        conn = create_connection()  # Create a database connection
        return retrieve_exercise_function(conn)  # Pass the connection to the function
    except Exception as e:
        logging.error(f"Error retrieving exercise: {e}")
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)