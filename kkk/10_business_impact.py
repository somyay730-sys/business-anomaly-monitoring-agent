import pandas as pd

file_path = "data/anomaly_investigation_results.csv"

daily = pd.read_csv(file_path)
daily["order_date"] = pd.to_datetime(daily["order_date"])

print("=" * 60)
print("STEP 12: BUSINESS IMPACT ANALYSIS")
print("=" * 60)

print("\nDataset shape:", daily.shape)

normal_days = daily[
    daily["final_anomaly_status"] == "Normal"
]

anomaly_days = daily[
    daily["final_anomaly_status"] != "Normal"
].copy()

normal_revenue = normal_days["revenue"].mean()
normal_profit = normal_days["profit"].mean()
normal_orders = normal_days["orders"].mean()

print("\nNormal day average revenue:", round(normal_revenue, 2))
print("Normal day average profit:", round(normal_profit, 2))
print("Normal day average orders:", round(normal_orders, 2))

anomaly_days["revenue_impact"] = (
    anomaly_days["revenue"] - normal_revenue
)

anomaly_days["profit_impact"] = (
    anomaly_days["profit"] - normal_profit
)

anomaly_days["orders_impact"] = (
    anomaly_days["orders"] - normal_orders
)

anomaly_days["revenue_impact_percentage"] = (
    anomaly_days["revenue_impact"] / normal_revenue
) * 100

anomaly_days["profit_impact_percentage"] = (
    anomaly_days["profit_impact"] / normal_profit
) * 100

anomaly_days["orders_impact_percentage"] = (
    anomaly_days["orders_impact"] / normal_orders
) * 100


def get_business_impact(row):

    revenue_impact = abs(row["revenue_impact_percentage"])
    profit_impact = abs(row["profit_impact_percentage"])

    if revenue_impact >= 30 or profit_impact >= 30:
        return "Critical"

    elif revenue_impact >= 20 or profit_impact >= 20:
        return "High"

    elif revenue_impact >= 10 or profit_impact >= 10:
        return "Medium"

    else:
        return "Low"


anomaly_days["business_impact"] = anomaly_days.apply(
    get_business_impact,
    axis=1
)

daily["revenue_impact"] = 0.0
daily["profit_impact"] = 0.0
daily["orders_impact"] = 0.0

daily["revenue_impact_percentage"] = 0.0
daily["profit_impact_percentage"] = 0.0
daily["orders_impact_percentage"] = 0.0

daily["business_impact"] = "None"

daily.loc[
    anomaly_days.index,
    "revenue_impact"
] = anomaly_days["revenue_impact"]

daily.loc[
    anomaly_days.index,
    "profit_impact"
] = anomaly_days["profit_impact"]

daily.loc[
    anomaly_days.index,
    "orders_impact"
] = anomaly_days["orders_impact"]

daily.loc[
    anomaly_days.index,
    "revenue_impact_percentage"
] = anomaly_days["revenue_impact_percentage"]

daily.loc[
    anomaly_days.index,
    "profit_impact_percentage"
] = anomaly_days["profit_impact_percentage"]

daily.loc[
    anomaly_days.index,
    "orders_impact_percentage"
] = anomaly_days["orders_impact_percentage"]

daily.loc[
    anomaly_days.index,
    "business_impact"
] = anomaly_days["business_impact"]

print("\n" + "=" * 60)
print("BUSINESS IMPACT SUMMARY")
print("=" * 60)

print(
    daily["business_impact"].value_counts()
)

print("\n" + "=" * 60)
print("TOP BUSINESS IMPACT DAYS")
print("=" * 60)

top_impact = daily[
    daily["final_anomaly_status"] != "Normal"
].sort_values(
    by="revenue_impact_percentage",
    key=lambda x: x.abs(),
    ascending=False
).head(20)

print(
    top_impact[
        [
            "order_date",
            "final_anomaly_status",
            "confidence",
            "business_impact",
            "revenue",
            "revenue_impact_percentage",
            "profit",
            "profit_impact_percentage",
            "orders",
            "orders_impact_percentage",
            "main_anomaly_causes"
        ]
    ]
)

output_file = "data/business_impact_results.csv"

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

print("\nStep 12 completed successfully!")