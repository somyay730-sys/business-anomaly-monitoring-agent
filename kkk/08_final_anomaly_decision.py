import pandas as pd

file_path = "data/anomaly_model_comparison.csv"

df = pd.read_csv(file_path)

df["order_date"] = pd.to_datetime(df["order_date"])

print("=" * 60)
print("STEP 10: FINAL ANOMALY DECISION")
print("=" * 60)

def get_final_status(row):

    if row["zscore_anomaly"] and row["isolation_forest_anomaly"]:
        return "Confirmed Anomaly"

    elif row["zscore_anomaly"] or row["isolation_forest_anomaly"]:
        return "Possible Anomaly"

    else:
        return "Normal"


df["final_anomaly_status"] = df.apply(
    get_final_status,
    axis=1
)

def get_confidence(status):

    if status == "Confirmed Anomaly":
        return "High"

    elif status == "Possible Anomaly":
        return "Medium"

    else:
        return "Low"


df["confidence"] = df["final_anomaly_status"].apply(
    get_confidence
)

print("\n" + "=" * 60)
print("FINAL ANOMALY SUMMARY")
print("=" * 60)

print(
    df["final_anomaly_status"].value_counts()
)

print("\n" + "=" * 60)
print("CONFIDENCE SUMMARY")
print("=" * 60)

print(
    df["confidence"].value_counts()
)

print("\n" + "=" * 60)
print("CONFIRMED ANOMALIES")
print("=" * 60)

confirmed = df[
    df["final_anomaly_status"] == "Confirmed Anomaly"
]

print(
    confirmed[
        [
            "order_date",
            "zscore_anomaly",
            "isolation_forest_anomaly",
            "final_anomaly_status",
            "confidence"
        ]
    ].to_string(index=False)
)

output_file = "data/final_anomaly_results.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 60)
print("RESULT SAVED")
print("=" * 60)

print("File:", output_file)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nStep 10 completed successfully!")