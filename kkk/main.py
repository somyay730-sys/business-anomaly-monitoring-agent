import pandas as pd
from sklearn.ensemble import IsolationForest

file_path = "data/anomaly_severity_results.csv"

daily = pd.read_csv(file_path)
daily["order_date"] = pd.to_datetime(daily["order_date"])

print("=" * 60)
print("STEP 8: ISOLATION FOREST ANOMALY DETECTION")
print("=" * 60)

print("\nDataset shape:", daily.shape)

kpi_columns = [
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

X = daily[kpi_columns]

print("\nNumber of KPIs used:", len(kpi_columns))
print("Rows used for ML:", len(X))

model = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)

model.fit(X)

daily["isolation_forest_prediction"] = model.predict(X)

daily["isolation_forest_score"] = model.decision_function(X)

daily["ml_anomaly"] = (
    daily["isolation_forest_prediction"] == -1
)

print("\n" + "=" * 60)
print("ISOLATION FOREST RESULTS")
print("=" * 60)

print("\nNormal days:",
      (daily["ml_anomaly"] == False).sum())

print("Anomalous days:",
      daily["ml_anomaly"].sum())

print("\n" + "=" * 60)
print("TOP 20 ML ANOMALIES")
print("=" * 60)

top_ml_anomalies = daily[
    daily["ml_anomaly"] == True
].sort_values(
    by="isolation_forest_score"
)

print(
    top_ml_anomalies[
        [
            "order_date",
            "isolation_forest_score",
            "orders",
            "revenue",
            "profit",
            "profit_margin",
            "payment_failure_rate",
            "delivery_delay_rate"
        ]
    ].head(20)
)

output_file = "data/isolation_forest_results.csv"

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

print("\nStep 8 completed successfully!")