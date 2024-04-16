from flask import Flask, render_template

app = Flask(__name__)

@app.route('/submit_success')
def submit_success():
    return render_template('submit-success.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
