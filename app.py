from flask import Flask, render_template
from routes.submit_exercise import submit_exercise_function
from routes.retrieve_exercise import retrieve_exercise_function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_exercise')
def submit_exercise():
    return submit_exercise_function()

@app.route('/retrieve_exercise')
def retrieve_exercise():
    return retrieve_exercise_function()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
