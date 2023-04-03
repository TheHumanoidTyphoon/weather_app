from flask import render_template, request
from app.app import app, db
import smtplib
from app.models import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('404.html'), 404

@app.route('/process-form', methods=['POST'])
def process_form():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save email to database
    email_obj = Email(email=email)
    db.session.add(email_obj)
    db.session.commit()

    # Send email
    sender_email = ""
    receiver_email = email
    password = ""
    message_text = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message_text)
    server.quit()

    # Display confirmation message
    return render_template('confirmation.html')


