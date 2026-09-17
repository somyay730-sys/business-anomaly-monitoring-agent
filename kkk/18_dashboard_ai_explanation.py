import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Business Anomaly Monitoring",
    layout="wide"
)

st.title("AI-Powered Business Anomaly Monitoring Dashboard")

df = pd.read_csv("data/ai_explanation_results.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# -----------------------------
# KPI SUMMARY
# -----------------------------

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

# -----------------------------
# SEVERITY
# -----------------------------

st.subheader("Anomaly Severity")

col1, col2, col3 = st.columns(3)

col1.metric("Critical", critical)
col2.metric("High", high)
col3.metric("Medium", medium)

st.divider()

# -----------------------------
# TRENDS
# -----------------------------

st.subheader("Revenue Trend")

st.line_chart(
    df.set_index("order_date")["revenue"]
)

st.subheader("Profit Trend")

st.line_chart(
    df.set_index("order_date")["profit"]
)

st.divider()

# -----------------------------
# SELECT ANOMALY
# -----------------------------

st.subheader("AI Anomaly Investigation")

anomaly_dates = anomalies["order_date"].dt.strftime("%Y-%m-%d").tolist()

selected_date = st.selectbox(
    "Select an anomaly date",
    anomaly_dates
)

selected_row = anomalies[
    anomalies["order_date"].dt.strftime("%Y-%m-%d") == selected_date
].iloc[0]

# -----------------------------
# ANOMALY DETAILS
# -----------------------------

st.subheader("Anomaly Details")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Status",
    selected_row["final_anomaly_status"]
)

col2.metric(
    "Confidence",
    selected_row["confidence"]
)

col3.metric(
    "Business Impact",
    selected_row["business_impact"]
)

col4.metric(
    "Revenue Impact",
    f"{selected_row['revenue_impact_percentage']:.2f}%"
)

st.write(
    "**Main Anomaly Causes:**",
    selected_row["main_anomaly_causes"]
)

st.divider()

# -----------------------------
# AI EXPLANATION
# -----------------------------

st.subheader("AI Business Explanation")

st.info(
    selected_row["ai_business_explanation"]
)

st.divider()

# -----------------------------
# IMPACT
# -----------------------------

st.subheader("Business Impact")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Revenue Impact",
    f"{selected_row['revenue_impact_percentage']:.2f}%"
)

col2.metric(
    "Profit Impact",
    f"{selected_row['profit_impact_percentage']:.2f}%"
)

col3.metric(
    "Orders Impact",
    f"{selected_row['orders_impact_percentage']:.2f}%"
)

st.divider()

st.subheader("Anomaly Table")

st.dataframe(
    anomalies[
        [
            "order_date",
            "final_anomaly_status",
            "confidence",
            "business_impact",
            "main_anomaly_causes",
            "revenue_impact_percentage",
            "profit_impact_percentage"
        ]
    ],
    width="stretch"
)