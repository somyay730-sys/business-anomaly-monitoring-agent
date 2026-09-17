import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

file_path = "data/ai_explanation_results.csv"

daily = pd.read_csv(file_path)

anomalies = daily[
    daily["final_anomaly_status"] != "Normal"
].copy()

row = anomalies.iloc[0]

prompt = f"""
You are a business intelligence analyst.

Analyze this business anomaly and explain it to a business manager.

Date: {row['order_date']}
Anomaly Status: {row['final_anomaly_status']}
Confidence: {row['confidence']}
Main Causes: {row['main_anomaly_causes']}

Orders: {row['orders']}
Revenue: {row['revenue']}
Profit: {row['profit']}
Profit Margin: {row['profit_margin']}
Average Order Value: {row['average_order_value']}
Payment Failure Rate: {row['payment_failure_rate']}
Delivery Delay Rate: {row['delivery_delay_rate']}

Revenue Impact: {row['revenue_impact_percentage']}%
Profit Impact: {row['profit_impact_percentage']}%
Orders Impact: {row['orders_impact_percentage']}%

Give:
1. What happened
2. Possible business reason
3. Business impact
4. Recommended action

Keep the explanation simple and practical.
"""

response = client.responses.create(
    model="gpt-5.6-luna",
    input=prompt
)

print("=" * 60)
print("STEP 14B: AI ANOMALY EXPLANATION")
print("=" * 60)

print("\nDate:", row["order_date"])
print("\nAI Explanation:")
print(response.output_text)

print("\nStep 14B completed successfully!")