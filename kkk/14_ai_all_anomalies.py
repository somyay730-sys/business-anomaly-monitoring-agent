import pandas as pd
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

print("=" * 60)
print("STEP 15: AI EXPLANATIONS FOR ALL ANOMALIES")
print("=" * 60)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

input_file = "data/ai_explanation_results.csv"
output_file = "data/final_ai_anomaly_explanations.csv"

daily = pd.read_csv(input_file)

anomalies = daily[daily["final_anomaly_status"] != "Normal"].copy()

print("Total anomaly days:", len(anomalies))

results = []

for index, row in anomalies.iterrows():

    try:

        prompt = f"""
You are a business anomaly monitoring AI agent.

Analyze the following business anomaly and explain it clearly.

Date: {row['order_date']}
Anomaly Status: {row['final_anomaly_status']}
Confidence: {row['confidence']}
Main Causes: {row['main_anomaly_causes']}

Orders: {row['orders']}
Revenue: {row['revenue']}
Profit: {row['profit']}
Profit Margin: {row['profit_margin']}%
Average Order Value: {row['average_order_value']}

Payment Failure Rate: {row['payment_failure_rate']}%
Delivery Delay Rate: {row['delivery_delay_rate']}%

Revenue Impact: {row['revenue_impact_percentage']}%
Profit Impact: {row['profit_impact_percentage']}%
Orders Impact: {row['orders_impact_percentage']}%

Provide:

1. What happened
2. Most likely causes
3. Business impact
4. Recommended actions

Keep the explanation practical and suitable for a business manager.
"""

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        explanation = response.output_text

        result = row.to_dict()
        result["llm_business_explanation"] = explanation

        results.append(result)

        print(
            f"Processed {len(results)}/{len(anomalies)}: "
            f"{row['order_date']}"
        )

        temp_df = pd.DataFrame(results)
        temp_df.to_csv(
            output_file,
            index=False
        )

        time.sleep(1)

    except Exception as e:

        print(
            f"ERROR processing {row['order_date']}: {e}"
        )

        result = row.to_dict()
        result["llm_business_explanation"] = (
            "AI explanation could not be generated."
        )

        results.append(result)

        temp_df = pd.DataFrame(results)
        temp_df.to_csv(
            output_file,
            index=False
        )

print("=" * 60)
print("RESULT SAVED")
print("=" * 60)

print("File:", output_file)
print("Rows:", len(results))
print("Columns:", len(pd.DataFrame(results).columns))

print()
print("Step 15 completed successfully!")