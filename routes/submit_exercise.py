from flask import Flask, render_template, request, redirect, url_for
from db_config import create_connection

app = Flask(__name__)

@app.route('/submit_exercise', methods=['GET', 'POST'])
def submit_exercise_function():
    conn = create_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        ex_name = request.form['ex_name']
        ex_difficulty = request.form['ex_difficulty']
        ex_description = request.form['ex_description']
        ex_video_url = request.form['ex_video_url']

        try:
            # Insert data into the ex_list table
            sql = "INSERT INTO ex_list (ex_name, ex_difficulty, ex_description, ex_video_url) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (ex_name, ex_difficulty, ex_description, ex_video_url))
            conn.commit()
            return redirect(url_for('submit_exercise_function'))  # Redirect to the same page after submission
        except Exception as e:
            conn.rollback()
            return 'Error: ' + str(e)
        finally:
            cursor.close()
            conn.close()

    # If it's a GET request, render the template normally
    return render_template('submit-exercise.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
