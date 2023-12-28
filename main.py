import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('meetings.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS meetings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        topic TEXT NOT NULL,
                        date TEXT NOT NULL,
                        start_time TEXT NOT NULL,
                        end_time TEXT NOT NULL,
                        participants TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return 'Meeting Organizer Ana Sayfası'

@app.route('/create-meeting', methods=['GET', 'POST'])
def create_meeting():
    if request.method == 'POST':
        topic = request.form['topic']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        participants = request.form['participants']

        conn = get_db_connection()
        conn.execute('''INSERT INTO meetings (topic, date, start_time, end_time, participants)
                        VALUES (?, ?, ?, ?, ?)''', 
                        (topic, date, start_time, end_time, participants))
        conn.commit()
        conn.close()

        return redirect(url_for('meetings'))
    return render_template('meeting_form.html')

@app.route('/meetings')
def meetings():
    conn = get_db_connection()
    meetings = conn.execute('SELECT * FROM meetings').fetchall()
    conn.close()
    return render_template('meeting_list.html', meetings=meetings)

@app.route('/update-meeting/<int:id>', methods=['GET', 'POST'])
def update_meeting(id):
    conn = get_db_connection()
    if request.method == 'POST':
        topic = request.form['topic']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        participants = request.form['participants']

        conn.execute('''UPDATE meetings SET topic = ?, date = ?, start_time = ?, end_time = ?, participants = ?
                        WHERE id = ?''', 
                        (topic, date, start_time, end_time, participants, id))
        conn.commit()
        conn.close()
        return redirect(url_for('meetings'))
    else:
        meeting = conn.execute('SELECT * FROM meetings WHERE id = ?', (id,)).fetchone()
        conn.close()
        return render_template('update_meeting.html', meeting=meeting)
@app.route('/delete-meeting/<int:id>', methods=['POST'])
def delete_meeting(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM meetings WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('meetings'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
