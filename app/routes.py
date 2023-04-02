from flask import render_template, request
from app.app import app
import smtplib

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/process-form', methods=['POST'])
def process_form():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Send email
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    password = "your_email_password"
    message_text = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message_text)
    server.quit()

    # Display confirmation message
    return render_template('confirmation.html')


