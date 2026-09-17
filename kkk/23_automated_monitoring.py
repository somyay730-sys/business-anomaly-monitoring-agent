import os
import smtplib
import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")

alerts_file = "data/alerts.csv"
history_file = "data/alert_history.csv"

alerts = pd.read_csv(alerts_file)
history = pd.read_csv(history_file)

alerts["order_date"] = pd.to_datetime(alerts["order_date"])
history["order_date"] = pd.to_datetime(history["order_date"])

new_alerts = alerts[
    ~alerts["order_date"].isin(history["order_date"])
]

print(f"Total alerts: {len(alerts)}")
print(f"New alerts: {len(new_alerts)}")

if len(new_alerts) == 0:

    print("No new alerts. No email sent.")

else:

    for _, alert in new_alerts.iterrows():

        subject = (
            f"🚨 Business Anomaly Alert - "
            f"{alert['order_date'].date()}"
        )

        body = f"""
AI-POWERED BUSINESS ANOMALY MONITORING SYSTEM
==============================================

NEW BUSINESS ANOMALY DETECTED

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

Please investigate this anomaly using the
AI Business Anomaly Monitoring Dashboard.
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

            print(
                f"Email sent for "
                f"{alert['order_date'].date()}"
            )

        except Exception as e:

            print("Email sending failed:")
            print(e)

            continue

    new_alert_dates = new_alerts[["order_date"]]

    history = pd.concat(
        [history, new_alert_dates],
        ignore_index=True
    )

    history = history.drop_duplicates(
        subset=["order_date"]
    )

    history.to_csv(
        history_file,
        index=False
    )

    print("Alert history updated successfully.")