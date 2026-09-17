import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Business Anomaly Monitoring",
    page_icon="📊",
    layout="wide"
)

# =============================
# LOAD DATA
# =============================

df = pd.read_csv("data/ai_explanation_results.csv")
alerts = pd.read_csv("data/alerts.csv")

df["order_date"] = pd.to_datetime(df["order_date"])
alerts["order_date"] = pd.to_datetime(alerts["order_date"])

# =============================
# TITLE
# =============================

st.title("AI-Powered Business Anomaly Monitoring")
st.caption("E-commerce Business Performance & Anomaly Detection System")

st.divider()

# =============================
# KPI CALCULATIONS
# =============================

total_orders = df["orders"].sum()
total_revenue = df["revenue"].sum()
total_profit = df["profit"].sum()

anomalies = df[
    df["final_anomaly_status"] != "Normal"
]

critical = (
    df["business_impact"] == "Critical"
).sum()

high = (
    df["business_impact"] == "High"
).sum()

medium = (
    df["business_impact"] == "Medium"
).sum()

# =============================
# KPI CARDS
# =============================

st.subheader("Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Orders",
    f"{total_orders:,.0f}"
)

col2.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)

col3.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col4.metric(
    "Anomaly Days",
    len(anomalies)
)

# =============================
# SEVERITY
# =============================

st.divider()

st.subheader("Anomaly Severity")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Critical Alerts",
    critical
)

col2.metric(
    "High Alerts",
    high
)

col3.metric(
    "Medium Anomalies",
    medium
)

# =============================
# TRENDS
# =============================

st.divider()

st.subheader("Business Performance Trends")

col1, col2 = st.columns(2)

with col1:

    st.write("Revenue")

    st.line_chart(
        df.set_index("order_date")["revenue"]
    )

with col2:

    st.write("Profit")

    st.line_chart(
        df.set_index("order_date")["profit"]
    )

# =============================
# ALERT SECTION
# =============================

st.divider()

st.subheader("🚨 High-Priority Business Alerts")

st.write(
    f"Total Critical/High alerts: **{len(alerts)}**"
)

if len(alerts) > 0:

    alert_columns = [
        "order_date",
        "final_anomaly_status",
        "confidence",
        "business_impact",
        "main_anomaly_causes",
        "revenue_impact_percentage",
        "profit_impact_percentage"
    ]

    st.dataframe(
        alerts[alert_columns],
        width="stretch"
    )

else:

    st.success(
        "No high-priority business alerts detected."
    )

# =============================
# ALERT INVESTIGATION
# =============================

st.divider()

st.subheader("🔍 Investigate an Alert")

if len(alerts) > 0:

    alert_dates = (
        alerts["order_date"]
        .dt.strftime("%Y-%m-%d")
        .tolist()
    )

    selected_date = st.selectbox(
        "Select an alert date",
        alert_dates
    )

    selected_alert = alerts[
        alerts["order_date"]
        .dt.strftime("%Y-%m-%d")
        == selected_date
    ].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Status",
        selected_alert["final_anomaly_status"]
    )

    col2.metric(
        "Confidence",
        selected_alert["confidence"]
    )

    col3.metric(
        "Business Impact",
        selected_alert["business_impact"]
    )

    col4.metric(
        "Revenue Impact",
        f"{selected_alert['revenue_impact_percentage']:.2f}%"
    )

    st.write(
        "**Main Anomaly Causes:**"
    )

    st.write(
        selected_alert["main_anomaly_causes"]
    )

    st.write(
        "**AI Business Explanation:**"
    )

    st.info(
        selected_alert["ai_business_explanation"]
    )

    st.write(
        "**Business Impact Details:**"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Revenue Impact",
        f"{selected_alert['revenue_impact_percentage']:.2f}%"
    )

    col2.metric(
        "Profit Impact",
        f"{selected_alert['profit_impact_percentage']:.2f}%"
    )

    col3.metric(
        "Orders Impact",
        f"{selected_alert['orders_impact_percentage']:.2f}%"
    )

# =============================
# ANOMALY HISTORY
# =============================

st.divider()

st.subheader("Anomaly History")

status_filter = st.selectbox(
    "Filter anomalies",
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
        anomalies["final_anomaly_status"]
        == status_filter
    ]

history_columns = [
    "order_date",
    "final_anomaly_status",
    "confidence",
    "business_impact",
    "main_anomaly_causes",
    "revenue_impact_percentage",
    "profit_impact_percentage"
]

st.write(
    f"Showing **{len(filtered)}** anomaly days"
)

st.dataframe(
    filtered[history_columns],
    width="stretch"
)

# =============================
# FOOTER
# =============================

st.divider()

st.caption(
    "AI-Powered Business Anomaly Monitoring System | "
    "Statistical Detection + Machine Learning + AI Explanation"
)