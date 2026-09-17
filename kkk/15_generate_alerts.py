import pandas as pd

print("=" * 60)
print("STEP 16: ALERT GENERATION")
print("=" * 60)

input_file = "data/ai_explanation_results.csv"
output_file = "data/alerts.csv"

df = pd.read_csv(input_file)

alerts = df[
    (df["final_anomaly_status"] != "Normal") &
    (df["business_impact"].isin(["Critical", "High"]))
].copy()

alerts = alerts.sort_values(
    by="revenue_impact_percentage",
    key=lambda x: x.abs(),
    ascending=False
)

alert_columns = [
    "order_date",
    "final_anomaly_status",
    "confidence",
    "business_impact",
    "main_anomaly_causes",
    "orders",
    "revenue",
    "profit",
    "revenue_impact_percentage",
    "profit_impact_percentage",
    "orders_impact_percentage",
    "ai_business_explanation"
]

alerts = alerts[alert_columns]

alerts.to_csv(output_file, index=False)

print("Total alerts generated:", len(alerts))
print("Alert file:", output_file)

print()
print("Top alerts:")
print(alerts.head(10))

print()
print("Step 16 completed successfully!")