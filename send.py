import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()


def create_email(subject, body, to_email, from_email):
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))
    return msg


def connect_to_smtp(smtp_server, smtp_port, from_email, password):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    return server


def send_email(subject, body, to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    msg = create_email(subject, body, to_email, from_email)

    try:
        server = connect_to_smtp(smtp_server, smtp_port, from_email, password)
        server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
