from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Meeting Organizer Ana Sayfası'

@app.route('/create-meeting', methods=['GET', 'POST'])
def create_meeting():
    if request.method == 'POST':
        # Form verilerini burada işleyebilirsiniz
        topic = request.form['topic']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        participants = request.form['participants']

        # Verileri işledikten sonra, örneğin veritabanına kaydedebilirsiniz

        return 'Toplantı başarıyla kaydedildi'
    else:
        return render_template('meeting_form.html')

if __name__ == '__main__':
    app.run(debug=True)
