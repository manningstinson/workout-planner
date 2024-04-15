from flask import Flask, render_template

app = Flask(__name__)

@app.route('/submit_exercise')
def submit_exercise_function():
    # Any necessary logic here
    # For example:
    # process_form_data()
    return render_template('submit-exercise.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')