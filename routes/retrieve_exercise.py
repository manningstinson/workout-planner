from flask import Flask, render_template

app = Flask(__name__)

@app.route('/retrieve_exercise')
def retrieve_exercise_function():
    # Any necessary logic here
    # For example:
    # process_form_data()
    return render_template('retrieve-exercise.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')