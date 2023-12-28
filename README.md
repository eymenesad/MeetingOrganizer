Meeting Organizer
Meeting Organizer is a simple web application that allows users to record, update, and manage their meetings. It provides an easy way to keep track of meeting details such as the topic, date, start time, end time, and participants. This project is built using Flask, a Python web framework, and SQLite for the database.

Features
Create new meetings with the following information:
Meeting Topic
Date
Start Time
End Time
Participants
View a list of all created meetings.
Update existing meetings.
Delete meetings.
Getting Started
To get this project up and running on your local machine, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/meeting-organizer.git
cd meeting-organizer
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Initialize the database:

bash
Copy code
python main.py
Run the Flask application:

bash
Copy code
flask run
Open your web browser and go to http://localhost:5000 to access the Meeting Organizer.
