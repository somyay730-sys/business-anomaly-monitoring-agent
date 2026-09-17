import os
import smtplib
import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")

alerts = pd.read_csv("data/alerts.csv")

alerts["order_date"] = pd.to_datetime(alerts["order_date"])

alerts = alerts.sort_values(
    "revenue_impact_percentage",
    key=lambda x: x.abs(),
    ascending=False
)

alert = alerts.iloc[0]

subject = f"🚨 Business Anomaly Alert - {alert['order_date'].date()}"

body = f"""
AI-POWERED BUSINESS ANOMALY MONITORING SYSTEM
==============================================

BUSINESS ANOMALY DETECTED

Date:
{alert['order_date'].date()}

Status:
{alert['final_anomaly_status']}

Confidence:
{alert['confidence']}

Business Impact:
{alert['business_impact']}

Main Anomaly Causes:
{alert['main_anomaly_causes']}

BUSINESS IMPACT
---------------

Revenue Impact:
{alert['revenue_impact_percentage']:.2f}%

Profit Impact:
{alert['profit_impact_percentage']:.2f}%

Orders Impact:
{alert['orders_impact_percentage']:.2f}%

AI BUSINESS EXPLANATION
-----------------------

{alert['ai_business_explanation']}

Please investigate this anomaly using the AI Business Anomaly Monitoring Dashboard.
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

    print("Business anomaly alert sent successfully!")
    print(f"Alert date: {alert['order_date'].date()}")
    print(f"Business impact: {alert['business_impact']}")

except Exception as e:
    print("Email sending failed:")
    print(e)