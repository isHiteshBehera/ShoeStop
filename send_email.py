from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    # Get the email address from the form data
    email = request.form['email']

    # Define the email message
    msg = MIMEText('Hello, this is a test message')
    msg['Subject'] = 'Test Message'
    msg['From'] = 'sender@example.com'
    msg['To'] = email

    try:
        # Send the email
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('sender@example.com', 'password')
        s.sendmail('sender@example.com', [email], msg.as_string())
        s.quit()
        return "Email sent successfully!"
    except Exception as e:
        return "Error sending email: " + str(e)

if __name__ == '__main__':
    app.run()