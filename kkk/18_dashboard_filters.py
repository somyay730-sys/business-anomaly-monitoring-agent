import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Business Anomaly Monitoring",
    layout="wide"
)

st.title("AI-Powered Business Anomaly Monitoring Dashboard")

df = pd.read_csv("data/ai_explanation_results.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

total_orders = df["orders"].sum()
total_revenue = df["revenue"].sum()
total_profit = df["profit"].sum()

anomalies = df[df["final_anomaly_status"] != "Normal"]

critical = (df["business_impact"] == "Critical").sum()
high = (df["business_impact"] == "High").sum()
medium = (df["business_impact"] == "Medium").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", f"{total_orders:,.0f}")
col2.metric("Total Revenue", f"${total_revenue:,.2f}")
col3.metric("Total Profit", f"${total_profit:,.2f}")
col4.metric("Anomaly Days", len(anomalies))

st.divider()

st.subheader("Anomaly Severity")

col1, col2, col3 = st.columns(3)

col1.metric("Critical", critical)
col2.metric("High", high)
col3.metric("Medium", medium)

st.divider()

st.subheader("Revenue Trend")

st.line_chart(
    df.set_index("order_date")["revenue"]
)

st.subheader("Profit Trend")

st.line_chart(
    df.set_index("order_date")["profit"]
)

st.divider()

st.subheader("Anomaly Filter")

status_filter = st.selectbox(
    "Select anomaly status",
    [
        "All",
        "Confirmed Anomaly",
        "Possible Anomaly"
    ]
)

if status_filter == "All":
    filtered = anomalies

else:
    filtered = anomalies[
        anomalies["final_anomaly_status"] == status_filter
    ]

st.write("Number of anomalies:", len(filtered))

display_columns = [
    "order_date",
    "final_anomaly_status",
    "confidence",
    "business_impact",
    "main_anomaly_causes",
    "revenue_impact_percentage",
    "profit_impact_percentage"
]

st.dataframe(
    filtered[display_columns],
    width="stretch"
)

st.success("Dashboard loaded successfully!")
