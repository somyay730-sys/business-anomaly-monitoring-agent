import pandas as pd

zscore_file = "data/anomaly_results.csv"
isolation_file = "data/isolation_forest_results.csv"

zscore = pd.read_csv(zscore_file)
isolation = pd.read_csv(isolation_file)

zscore["order_date"] = pd.to_datetime(zscore["order_date"])
isolation["order_date"] = pd.to_datetime(isolation["order_date"])

print("=" * 60)
print("STEP 9: MODEL COMPARISON")
print("=" * 60)

comparison = pd.DataFrame()

comparison["order_date"] = zscore["order_date"]

comparison["zscore_anomaly"] = zscore["is_anomaly"]

comparison["isolation_forest_anomaly"] = isolation["ml_anomaly"]

comparison["both_models_anomaly"] = (
    comparison["zscore_anomaly"] &
    comparison["isolation_forest_anomaly"]
)

comparison["zscore_only"] = (
    comparison["zscore_anomaly"] &
    ~comparison["isolation_forest_anomaly"]
)

comparison["isolation_forest_only"] = (
    ~comparison["zscore_anomaly"] &
    comparison["isolation_forest_anomaly"]
)

print("\n" + "=" * 60)
print("ANOMALY COUNTS")
print("=" * 60)

zscore_count = comparison["zscore_anomaly"].sum()
isolation_count = comparison["isolation_forest_anomaly"].sum()
both_count = comparison["both_models_anomaly"].sum()
zscore_only_count = comparison["zscore_only"].sum()
isolation_only_count = comparison["isolation_forest_only"].sum()

print("\nZ-score anomalies:", zscore_count)
print("Isolation Forest anomalies:", isolation_count)
print("Detected by both models:", both_count)
print("Z-score only:", zscore_only_count)
print("Isolation Forest only:", isolation_only_count)

agreement = (
    (comparison["zscore_anomaly"] ==
     comparison["isolation_forest_anomaly"]).mean()
) * 100

print("\nModel agreement:", round(agreement, 2), "%")

print("\n" + "=" * 60)
print("ANOMALIES DETECTED BY BOTH MODELS")
print("=" * 60)

both_models = comparison[
    comparison["both_models_anomaly"] == True
]

print(
    both_models[
        ["order_date"]
    ].to_string(index=False)
)

print("\n" + "=" * 60)
print("Z-SCORE ONLY ANOMALIES")
print("=" * 60)

zscore_only = comparison[
    comparison["zscore_only"] == True
]

print(
    zscore_only[
        ["order_date"]
    ].to_string(index=False)
)

print("\n" + "=" * 60)
print("ISOLATION FOREST ONLY ANOMALIES")
print("=" * 60)

isolation_only = comparison[
    comparison["isolation_forest_only"] == True
]

print(
    isolation_only[
        ["order_date"]
    ].to_string(index=False)
)

output_file = "data/anomaly_model_comparison.csv"

comparison.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 60)
print("RESULT SAVED")
print("=" * 60)

print("File:", output_file)
print("Rows:", comparison.shape[0])
print("Columns:", comparison.shape[1])

print("\nStep 9 completed successfully!")