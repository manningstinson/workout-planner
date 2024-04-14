from flask import Flask, render_template

app = Flask(__name__)

@app.route('/retrieve-exercise')
def retrieve_exercise_function():
    # Any necessary logic here
    # For example:
    # process_form_data()
    return render_template('retrieve-exercise.html')

if __name__ == '__main__':
    # Specify the desired host and port here
    app.run(debug=False, host='0.0.0.0', port=8080)