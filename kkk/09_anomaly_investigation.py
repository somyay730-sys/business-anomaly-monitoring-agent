import pandas as pd

final_file = "data/final_anomaly_results.csv"
zscore_file = "data/anomaly_results.csv"

final = pd.read_csv(final_file)
zscore = pd.read_csv(zscore_file)

final["order_date"] = pd.to_datetime(final["order_date"])
zscore["order_date"] = pd.to_datetime(zscore["order_date"])

print("=" * 60)
print("STEP 11: AUTOMATED ANOMALY INVESTIGATION")
print("=" * 60)

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

zscore_columns = [
    column + "_zscore"
    for column in kpi_columns
]

investigation = final.merge(
    zscore[
        ["order_date"] + kpi_columns + zscore_columns
    ],
    on="order_date",
    how="left"
)

def find_main_causes(row):

    causes = []

    for column in zscore_columns:

        score = row[column]

        if abs(score) > 2:

            kpi_name = column.replace("_zscore", "")

            causes.append(
                (kpi_name, score)
            )

    causes.sort(
        key=lambda x: abs(x[1]),
        reverse=True
    )

    return causes[:3]


investigation["main_anomaly_causes"] = investigation.apply(
    find_main_causes,
    axis=1
)

investigation["main_anomaly_causes"] = investigation[
    "main_anomaly_causes"
].apply(
    lambda x: ", ".join(
        [
            f"{kpi} (z={score:.2f})"
            for kpi, score in x
        ]
    )
)

print("\n" + "=" * 60)
print("ANOMALY INVESTIGATION RESULTS")
print("=" * 60)

anomalies = investigation[
    investigation["final_anomaly_status"] != "Normal"
]

print("\nTotal anomalies:", len(anomalies))

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
        "Main causes:",
        row["main_anomaly_causes"]
    )

output_file = "data/anomaly_investigation_results.csv"

investigation.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 60)
print("RESULT SAVED")
print("=" * 60)

print("File:", output_file)
print("Rows:", investigation.shape[0])
print("Columns:", investigation.shape[1])

print("\nStep 11 completed successfully!")