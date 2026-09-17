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

anomaly_days = (df["final_anomaly_status"] != "Normal").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", f"{total_orders:,.0f}")
col2.metric("Total Revenue", f"${total_revenue:,.2f}")
col3.metric("Total Profit", f"${total_profit:,.2f}")
col4.metric("Anomaly Days", anomaly_days)

st.divider()

st.subheader("Revenue Trend")

revenue_chart = df.set_index("order_date")["revenue"]

st.line_chart(revenue_chart)

st.subheader("Profit Trend")

profit_chart = df.set_index("order_date")["profit"]

st.line_chart(profit_chart)

st.subheader("Anomaly Summary")

anomaly_data = df[
    df["final_anomaly_status"] != "Normal"
][[
    "order_date",
    "final_anomaly_status",
    "confidence",
    "business_impact",
    "main_anomaly_causes",
    "revenue_impact_percentage",
    "profit_impact_percentage"
]]

st.dataframe(
    anomaly_data,
    use_container_width=True
)
