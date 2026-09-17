import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")

subject = "🚨 Business Anomaly Alert - Test"

body = """
AI-Powered Business Anomaly Monitoring System

This is a test email alert.

The email alert system is working successfully.

Next step:
Automate alerts for Critical and High business anomalies.
"""

msg = EmailMessage()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject
msg.set_content(body)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully!")

except Exception as e:
    print("Email sending failed:")
    print(e)