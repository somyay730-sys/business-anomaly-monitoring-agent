import pandas as pd

# ============================================================
# RECREATE DAILY KPI FILE
# ============================================================

input_file = "data/anomaly_results.csv"
output_file = "data/daily_kpis.csv"

# Load existing anomaly results
df = pd.read_csv(input_file)

print("Anomaly results shape:", df.shape)

# These are the original daily KPI columns
kpi_columns = [
    "order_date",
    "orders",
    "revenue",
    "gross_sales",
    "discount",
    "product_cost",
    "profit",
    "quantity",
    "average_order_value",
    "profit_margin",
    "repeat_customer_rate",
    "average_rating",
    "negative_sentiment_rate",
    "payment_failure_rate",
    "delivery_delay_rate"
]

# Extract only KPI columns
daily_kpis = df[kpi_columns].copy()

# Save
daily_kpis.to_csv(output_file, index=False)

print("\nDaily KPI file recreated successfully!")
print("Shape:", daily_kpis.shape)
print("Saved to:", output_file)

print("\nColumns:")
print(list(daily_kpis.columns))

print("\nFirst 5 rows:")
print(daily_kpis.head())