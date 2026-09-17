import os
import pandas as pd

print("=" * 60)
print("FINAL PROJECT VALIDATION")
print("=" * 60)

required_files = [
    "data/daily_kpis.csv",
    "data/anomaly_results.csv",
    "data/anomaly_severity_results.csv",
    "data/isolation_forest_results.csv",
    "data/anomaly_model_comparison.csv",
    "data/final_anomaly_results.csv",
    "data/anomaly_investigation_results.csv",
    "data/business_impact_results.csv",
    "data/ai_explanation_results.csv",
    "data/alerts.csv",
    "data/alert_history.csv"
]

print("\n1. CHECKING PROJECT FILES")

missing_files = []

for file in required_files:
    if os.path.exists(file):
        print(f"✓ {file}")
    else:
        print(f"✗ {file}")
        missing_files.append(file)

print("\n2. CHECKING MAIN DATA")

df = pd.read_csv("data/ai_explanation_results.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n3. ANOMALY SUMMARY")

print(
    "Confirmed anomalies:",
    (df["final_anomaly_status"] == "Confirmed Anomaly").sum()
)

print(
    "Possible anomalies:",
    (df["final_anomaly_status"] == "Possible Anomaly").sum()
)

print(
    "Normal days:",
    (df["final_anomaly_status"] == "Normal").sum()
)

print("\n4. BUSINESS IMPACT")

print(
    "Critical:",
    (df["business_impact"] == "Critical").sum()
)

print(
    "High:",
    (df["business_impact"] == "High").sum()
)

print(
    "Medium:",
    (df["business_impact"] == "Medium").sum()
)

print("\n5. ALERT SYSTEM")

alerts = pd.read_csv("data/alerts.csv")
history = pd.read_csv("data/alert_history.csv")

print("Current alerts:", len(alerts))
print("Alert history:", len(history))

duplicate_dates = history["order_date"].duplicated().sum()

print("Duplicate alert dates:", duplicate_dates)

print("\n6. FINAL RESULT")

if len(missing_files) == 0 and duplicate_dates == 0:
    print("✓ PROJECT VALIDATION PASSED")
else:
    print("✗ PROJECT VALIDATION NEEDS ATTENTION")

print("=" * 60)