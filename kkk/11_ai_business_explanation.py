import pandas as pd

file_path = "data/business_impact_results.csv"

daily = pd.read_csv(file_path)
daily["order_date"] = pd.to_datetime(daily["order_date"])

print("=" * 60)
print("STEP 13: AI BUSINESS EXPLANATION")
print("=" * 60)

print("\nDataset shape:", daily.shape)


def generate_explanation(row):

    if row["final_anomaly_status"] == "Normal":
        return "No significant business anomaly detected."

    status = row["final_anomaly_status"]
    confidence = row["confidence"]
    business_impact = row["business_impact"]

    revenue_change = row["revenue_impact_percentage"]
    profit_change = row["profit_impact_percentage"]
    orders_change = row["orders_impact_percentage"]

    causes = row["main_anomaly_causes"]

    if pd.isna(causes) or causes == "":
        causes = "multiple business KPIs"

    if revenue_change > 0:
        revenue_text = f"Revenue increased by {abs(revenue_change):.1f}%"
    else:
        revenue_text = f"Revenue decreased by {abs(revenue_change):.1f}%"

    if profit_change > 0:
        profit_text = f"profit increased by {abs(profit_change):.1f}%"
    else:
        profit_text = f"profit decreased by {abs(profit_change):.1f}%"

    if orders_change > 0:
        orders_text = f"orders increased by {abs(orders_change):.1f}%"
    else:
        orders_text = f"orders decreased by {abs(orders_change):.1f}%"

    explanation = (
        f"An anomaly was detected on {row['order_date'].date()} "
        f"with {confidence.lower()} confidence. "
        f"The anomaly is classified as {status.lower()} "
        f"with {business_impact.lower()} business impact. "
        f"{revenue_text} compared with normal business performance, "
        f"{profit_text}, and {orders_text}. "
        f"The main contributing KPIs were {causes}."
    )

    return explanation


daily["ai_business_explanation"] = daily.apply(
    generate_explanation,
    axis=1
)

print("\n" + "=" * 60)
print("AI BUSINESS EXPLANATIONS")
print("=" * 60)

anomalies = daily[
    daily["final_anomaly_status"] != "Normal"
]

print("\nTotal anomaly explanations:", len(anomalies))

for _, row in anomalies.head(20).iterrows():

    print("\nDate:", row["order_date"].date())

    print(
        "Status:",
        row["final_anomaly_status"]
    )

    print(
        "Confidence:",
        row["confidence"]
    )

    print(
        "Business Impact:",
        row["business_impact"]
    )

    print(
        "Explanation:",
        row["ai_business_explanation"]
    )


output_file = "data/ai_explanation_results.csv"

daily.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 60)
print("RESULT SAVED")
print("=" * 60)

print("File:", output_file)
print("Rows:", daily.shape[0])
print("Columns:", daily.shape[1])

print("\nStep 13 completed successfully!")