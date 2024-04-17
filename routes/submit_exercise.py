from flask import request, redirect, url_for, render_template
from db_config import create_connection

def submit_exercise_function():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            if request.method == 'POST':
                ex_name = request.form['ex_name']
                ex_difficulty = request.form['ex_difficulty']
                ex_description = request.form['ex_description']
                ex_video_url = request.form['ex_video_url']

                # Insert data into the ex_list table
                sql = "INSERT INTO ex_list (ex_name, ex_difficulty, ex_description, ex_video_url) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (ex_name, ex_difficulty, ex_description, ex_video_url))
                conn.commit()
                return redirect(url_for('submit_success'))  # Redirect to the success page after submission
        except Exception as e:
            conn.rollback()
            print('Error: ', e)
        finally:
            cursor.close()
            conn.close()
    return render_template('submit-exercise.html')