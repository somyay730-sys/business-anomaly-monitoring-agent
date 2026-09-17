# AI-Powered Business Anomaly Monitoring Agent

An end-to-end AI-powered business monitoring system that automatically analyzes e-commerce data, detects unusual business behavior, investigates the reasons behind anomalies, estimates business impact, generates AI-based explanations, and sends automated email alerts.

The project combines statistical analysis, machine learning, rule-based reasoning, LLM-based explanations, email automation, alert history tracking, and an interactive Streamlit dashboard.

---

## Project Overview

Businesses generate large amounts of transaction data every day. Important changes in revenue, orders, profit, customer behavior, payment failures, delivery delays, or customer sentiment can easily be missed when monitoring is performed manually.

This project builds an automated Business Anomaly Monitoring Agent that continuously analyzes business KPIs and identifies unusual patterns.

The system follows this workflow:

Raw Business Data
→ Data Cleaning
→ Data Preprocessing
→ Daily KPI Aggregation
→ KPI Validation
→ Statistical Anomaly Detection
→ Machine Learning Anomaly Detection
→ Model Comparison
→ Final Anomaly Decision
→ Automated Investigation
→ Business Impact Analysis
→ AI Explanation
→ Alert Generation
→ Email Notification
→ Alert History
→ Interactive Dashboard

---

## Business Problem

Traditional business monitoring often depends on manually checking dashboards and reports.

This creates several problems:

- Important business anomalies may be missed.
- Sudden revenue drops may not be detected quickly.
- Profit changes may go unnoticed.
- Customer dissatisfaction may increase without immediate attention.
- Payment failures can affect business performance.
- Delivery delays can negatively affect customer experience.
- Manual investigation takes time.
- Repeated alerts can create unnecessary noise.

The goal of this project is to automate the monitoring process and provide business-friendly explanations instead of only showing technical anomaly scores.

---

## Project Objectives

The main objectives of the project are:

1. Clean and preprocess e-commerce transaction data.
2. Convert transaction-level data into daily business KPIs.
3. Validate KPI quality and consistency.
4. Detect anomalies using statistical methods.
5. Detect anomalies using machine learning.
6. Compare multiple anomaly detection methods.
7. Determine the final anomaly status and confidence.
8. Automatically identify the KPIs responsible for an anomaly.
9. Estimate business impact.
10. Generate business-friendly explanations.
11. Use an LLM selectively for important anomaly explanations.
12. Generate high-priority alerts.
13. Send automated email notifications.
14. Maintain alert history to prevent duplicate alerts.
15. Provide an interactive Streamlit dashboard.
16. Validate the complete project pipeline.

---

# System Architecture

The complete system is designed as an end-to-end monitoring pipeline.

Raw E-Commerce Data
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Daily KPI Aggregation
        ↓
KPI Validation
        ↓
Z-Score Anomaly Detection
        ↓
Isolation Forest
        ↓
Model Comparison
        ↓
Final Anomaly Decision
        ↓
Anomaly Investigation
        ↓
Business Impact Analysis
        ↓
AI Business Explanation
        ↓
Alert Generation
        ↓
Alert History
        ↓
Email Automation
        ↓
Streamlit Dashboard

---

# Dataset

The project uses an e-commerce transaction dataset containing business, customer, payment, delivery, marketing, sales, and profitability information.

Important fields include:

- order_id
- order_date
- order_time
- order_status
- sales_channel
- customer_id
- customer_age
- gender
- customer_segment
- customer_type
- customer_city
- customer_state
- customer_country
- region
- payment_method
- payment_status
- currency
- shipping_method
- warehouse
- delivery_days
- estimated_delivery_days
- delivery_status
- return_status
- return_reason
- customer_rating
- review_sentiment
- customer_review
- marketing_channel
- campaign_name
- coupon_code
- quantity
- gross_sales
- discount_amount
- tax_amount
- shipping_cost
- net_sales
- product_cost
- profit
- profit_margin_percentage
- customer_lifetime_value
- is_repeat_customer
- customer_order_count

The original transaction dataset contains approximately 138,000 transaction records covering multiple years.

The project converts transaction-level information into daily business KPI records for anomaly monitoring.

---

# Data Cleaning

The first stage of the project focuses on preparing the dataset for analysis.

The cleaning process includes:

- Removing unnecessary whitespace from column names.
- Converting date columns into appropriate date formats.
- Handling missing values.
- Checking duplicate records.
- Validating numerical columns.
- Ensuring KPI calculations use valid business data.
- Preparing the dataset for aggregation and modeling.

The cleaned dataset is then used for KPI generation.

---

# Daily KPI Aggregation

Instead of directly monitoring individual transactions, the project aggregates business activity by date.

The following daily KPIs are calculated:

- Orders
- Revenue
- Gross Sales
- Discount
- Product Cost
- Profit
- Quantity
- Average Order Value
- Profit Margin
- Repeat Customer Rate
- Average Rating
- Negative Sentiment Rate
- Payment Failure Rate
- Delivery Delay Rate

The resulting dataset contains:

- 1,826 daily records
- Date range: 2021-01-01 to 2025-12-31
- 15 daily KPI columns

The daily KPI file is stored as:

    data/daily_kpis.csv

---

# KPI Validation

Before anomaly detection, the daily KPI dataset is validated.

Validation checks include:

- Missing values
- Duplicate dates
- Data types
- Numerical ranges
- KPI consistency
- Basic statistical summaries

This ensures the anomaly detection models operate on reliable business metrics.

---

# Statistical Anomaly Detection

The first anomaly detection approach uses the Z-score method.

For each KPI, the system calculates how far the daily value is from the historical mean.

The anomaly rule is:

    Absolute Z-score > 3

This means a KPI value is considered unusual when it is more than three standard deviations away from its historical mean.

The system checks multiple KPIs for every day.

The output is stored in:

    data/anomaly_results.csv

The Z-score approach identified:

- 100 anomalous days
- 1,726 normal days

---

# Anomaly Severity

After detecting anomalies, the system determines the severity based on the number of anomalous KPIs.

The severity logic is:

- 6 or more anomalous KPIs → Critical
- 4 or more anomalous KPIs → High
- 2 or more anomalous KPIs → Medium
- 1 anomalous KPI → Low

This provides a simple business-oriented severity classification.

---

# Machine Learning Anomaly Detection

The second anomaly detection approach uses the Isolation Forest algorithm.

Isolation Forest is an unsupervised machine learning algorithm designed to identify unusual observations.

The model configuration used in the project includes:

- Number of estimators: 200
- Contamination: 0.05
- Random state: 42

The model analyzes the daily KPI patterns and identifies observations that differ from normal business behavior.

The output is stored in:

    data/isolation_forest_results.csv

The Isolation Forest model identified:

- 92 ML anomalies
- 1,734 normal days

---

# Why Use Multiple Anomaly Detection Methods?

Using only one anomaly detection technique can produce incomplete results.

The project therefore combines:

1. Statistical anomaly detection
2. Machine learning anomaly detection

The Z-score method identifies KPI-level deviations.

Isolation Forest identifies unusual combinations of KPI values.

Using both approaches provides a more comprehensive anomaly monitoring system.

---

# Model Comparison

The project compares the results from both anomaly detection approaches.

The comparison identifies:

- Anomalies detected by both models
- Anomalies detected only by Z-score
- Anomalies detected only by Isolation Forest
- Normal observations

The comparison file is:

    data/anomaly_model_comparison.csv

This provides transparency into how different detection approaches behave.

---

# Final Anomaly Decision

The project combines the results from the statistical and machine learning models.

The final decision logic is:

Both models detect anomaly
→ Confirmed Anomaly
→ High Confidence

Only one model detects anomaly
→ Possible Anomaly
→ Medium Confidence

Neither model detects anomaly
→ Normal
→ Low Confidence

The final results are stored in:

    data/final_anomaly_results.csv

Final project results:

- Confirmed anomalies: 29
- Possible anomalies: 134
- Normal days: 1,663

---

# Automated Anomaly Investigation

Once an anomaly is detected, the system investigates which KPIs contributed to the unusual behavior.

The investigation process:

1. Identifies anomalous KPIs.
2. Calculates KPI Z-scores.
3. Measures the magnitude of the deviation.
4. Selects the strongest contributing KPIs.
5. Produces an explanation-ready record.

The investigation results are stored in:

    data/anomaly_investigation_results.csv

The system identifies the top KPI causes for each anomalous day.

---

# Business Impact Analysis

Technical anomaly detection alone is not enough for business monitoring.

The project therefore estimates the business impact of detected anomalies.

The system calculates:

- Revenue impact
- Profit impact
- Orders impact
- Revenue impact percentage
- Profit impact percentage
- Orders impact percentage

The impact is compared with the overall business baseline.

Impact classification:

- 30% or more → Critical
- 20% or more → High
- 10% or more → Medium
- Below 10% → Low

The business impact results are stored in:

    data/business_impact_results.csv

Final impact summary:

- Critical: 104
- High: 24
- Medium: 20

---

# AI Business Explanation

The project converts technical anomaly results into business-friendly explanations.

Instead of displaying only:

    Z-score = 4.2

the system produces an explanation describing:

- What happened
- Which KPIs changed
- Whether the anomaly is confirmed or possible
- The confidence level
- The potential business impact

Example explanation:

    A significant business anomaly was detected.
    Revenue and profit showed unusual movement compared with
    historical business behavior. The anomaly was detected by
    multiple monitoring methods and requires investigation.

The generated explanations are stored in:

    data/ai_explanation_results.csv

---

# LLM Integration

The project also includes OpenAI LLM integration.

The LLM is not used for every single record.

Instead, the system uses traditional statistical and machine learning techniques for large-scale anomaly detection and selectively uses the LLM for important anomalies.

This architecture reduces unnecessary API usage while still providing natural-language business explanations.

The LLM can receive information such as:

- Date
- Revenue
- Profit
- Orders
- KPI deviations
- Anomaly status
- Confidence
- Business impact

The LLM then generates a concise business-oriented explanation.

This creates a hybrid architecture:

Statistical Models
+
Machine Learning
+
Rule-Based Reasoning
+
LLM
=
AI Business Monitoring Agent

---

# Alert Generation

The alert system filters important business anomalies.

Alerts are generated for anomalies with:

- Critical business impact
- High business impact

The system ranks alerts using business impact so that important events can be reviewed first.

The alert file is:

    data/alerts.csv

Current alert count:

- 128 high-priority alerts

---

# Alert History

To avoid sending the same alert repeatedly, the project maintains an alert history.

The alert history system:

1. Reads existing alerts.
2. Checks whether the anomaly date has already been recorded.
3. Identifies only new alerts.
4. Sends notifications only for new alerts.
5. Stores the new alert dates.

The alert history file is:

    data/alert_history.csv

Current alert history:

- 128 alerts recorded
- 0 duplicate alert dates

---

# Email Alert Automation

The project integrates Gmail SMTP to send business alerts through email.

The email system can send:

- Alert date
- Anomaly status
- Confidence
- Business impact
- Revenue impact
- Profit impact
- Main anomaly causes
- AI-generated explanation

The system was tested successfully using a Gmail App Password.

Sensitive credentials are stored in an environment file and are not committed to GitHub.

Example environment variables:

    EMAIL_SENDER=yourgmail@gmail.com
    EMAIL_PASSWORD=your_gmail_app_password
    EMAIL_RECEIVER=yourgmail@gmail.com

The .env file is excluded through .gitignore.

---

# Automated Monitoring

The automated monitoring script checks for new alerts.

Workflow:

    Load Current Alerts
            ↓
    Load Alert History
            ↓
    Compare Alert Dates
            ↓
    Identify New Alerts
            ↓
    Send Email
            ↓
    Update Alert History

If no new alert is detected, no email is sent.

Example output:

    Total alerts: 128
    New alerts: 0
    No new alerts. No email sent.

This prevents duplicate notifications.

---

# Streamlit Dashboard

The project includes an interactive Streamlit dashboard for monitoring business performance.

The dashboard provides a visual interface for business users to understand:

- Overall business performance
- Revenue trends
- Profit trends
- Order trends
- Anomaly counts
- Business impact
- High-priority alerts
- Anomaly explanations
- Alert history

The final dashboard is implemented in:

    20_final_dashboard.py

The dashboard reads the generated CSV outputs from the data directory.

---

# Dashboard Features

The dashboard includes:

## Business KPI Overview

Displays:

- Total Orders
- Total Revenue
- Total Profit
- Number of Anomaly Days

## Revenue Trend

Visualizes revenue over time to help identify unusual business periods.

## Profit Trend

Shows profit movement across the monitored period.

## Anomaly Summary

Displays:

- Confirmed anomalies
- Possible anomalies
- Normal days
- Critical impact
- High impact
- Medium impact

## High-Priority Alerts

Displays important alerts that require business attention.

## Anomaly Investigation

Users can inspect:

- Anomaly date
- Anomaly status
- Confidence
- Business impact
- Main causes
- AI explanation

## Alert History

Users can review previously generated alerts and monitor historical anomaly activity.

---

# Dashboard Preview

The dashboard can be documented in this README using screenshots.

Recommended screenshots:

    screenshots/dashboard_main.png
    screenshots/anomaly_investigation.png
    screenshots/alert_monitoring.png

Once screenshots are added to the project, they can be displayed using:

    ![Main Dashboard](screenshots/dashboard_main.png)

    ![Anomaly Investigation](screenshots/anomaly_investigation.png)

    ![Alert Monitoring](screenshots/alert_monitoring.png)

These screenshots make the GitHub repository easier to understand and demonstrate the actual working interface of the project.

---

# Dashboard Workflow

The dashboard provides a business monitoring flow:

    Business Overview
            ↓
    KPI Trends
            ↓
    Anomaly Detection
            ↓
    Investigation
            ↓
    Business Impact
            ↓
    AI Explanation
            ↓
    Alert Monitoring

---

# Project Results

The completed system currently produces the following results:

| Metric | Result |
|---|---:|
| Daily Records | 1,826 |
| Confirmed Anomalies | 29 |
| Possible Anomalies | 134 |
| Normal Days | 1,663 |
| Critical Impact | 104 |
| High Impact | 24 |
| Medium Impact | 20 |
| Current Alerts | 128 |
| Alert History | 128 |
| Duplicate Alert Dates | 0 |

---

# Example Business Scenario

Suppose the system detects an unusual business day.

The daily KPI values show:

- Revenue significantly changed.
- Profit changed.
- Order volume changed.
- Payment failure rate increased.
- Delivery delay rate increased.

The Z-score model identifies unusual KPI behavior.

The Isolation Forest model also identifies the day as unusual.

The system therefore classifies the event as:

    Confirmed Anomaly
    Confidence: High

The investigation module identifies the major KPI contributors.

The business impact module estimates the financial effect.

The AI explanation module generates a business-friendly summary.

The alert system determines whether the event requires notification.

If it is a new high-priority alert, the email automation sends the alert to the configured receiver.

The event is then stored in alert history so that the same alert is not repeatedly sent.

---

# End-to-End Business Workflow

The complete business process is:

    E-Commerce Transactions
            ↓
    Clean Data
            ↓
    Generate Daily KPIs
            ↓
    Validate KPIs
            ↓
    Detect Statistical Anomalies
            ↓
    Detect ML Anomalies
            ↓
    Compare Models
            ↓
    Determine Final Status
            ↓
    Investigate Causes
            ↓
    Calculate Business Impact
            ↓
    Generate AI Explanation
            ↓
    Generate Alerts
            ↓
    Send Email Notification
            ↓
    Store Alert History
            ↓
    Display in Dashboard

---

# Technologies Used

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Machine Learning

- Scikit-learn
- Isolation Forest

## Statistical Analysis

- Z-score based anomaly detection

## Artificial Intelligence

- OpenAI API
- LLM-based business explanation

## Dashboard

- Streamlit

## Visualization

- Matplotlib
- Streamlit charts

## Automation

- Python automation
- SMTP email
- Gmail App Password

## Environment Management

- python-dotenv

## Development Environment

- PyCharm

## Version Control

- Git
- GitHub

---

# Project Structure

The project structure is organized into separate scripts for each stage of the pipeline.

    AI-Business-Anomaly-Monitoring-Agent/
    │
    ├── data/
    │   ├── daily_kpis.csv
    │   ├── anomaly_results.csv
    │   ├── anomaly_severity_results.csv
    │   ├── isolation_forest_results.csv
    │   ├── anomaly_model_comparison.csv
    │   ├── final_anomaly_results.csv
    │   ├── anomaly_investigation_results.csv
    │   ├── business_impact_results.csv
    │   ├── ai_explanation_results.csv
    │   ├── alerts.csv
    │   └── alert_history.csv
    │
    ├── screenshots/
    │   ├── dashboard_main.png
    │   ├── anomaly_investigation.png
    │   └── alert_monitoring.png
    │
    ├── main.py
    │
    ├── 01_data_understanding.py
    ├── 02_data_cleaning.py
    ├── 03_data_preprocessing.py
    ├── 04_kpi_validation.py
    ├── 05_zscore_anomaly_detection.py
    ├── 06_daily_kpi_aggregation.py
    ├── 07_model_comparison.py
    ├── 08_final_anomaly_decision.py
    ├── 15_generate_alerts.py
    ├── 16_alert_history.py
    ├── 17_dashboard.py
    ├── 18_dashboard_filters.py
    ├── 18_dashboard_ai_explanation.py
    ├── 19_dashboard_alerts.py
    ├── 20_final_dashboard.py
    ├── 21_email_alert_test.py
    ├── 22_send_business_alert.py
    ├── 23_automated_monitoring.py
    ├── 25_final_project_test.py
    │
    ├── .env
    ├── .gitignore
    └── README.md

---

# Installation

Clone the repository and open the project in PyCharm or another Python IDE.

Create a virtual environment and install the required packages.

Required packages include:

    pandas
    numpy
    scikit-learn
    matplotlib
    streamlit
    python-dotenv
    openai

Install packages using:

    pip install pandas numpy scikit-learn matplotlib streamlit python-dotenv openai

---

# Environment Variables

Create a .env file in the project root.

Add:

    EMAIL_SENDER=yourgmail@gmail.com
    EMAIL_PASSWORD=your_gmail_app_password
    EMAIL_RECEIVER=yourgmail@gmail.com
    OPENAI_API_KEY=your_openai_api_key

Do not upload the .env file to GitHub.

The project includes .gitignore rules to prevent sensitive environment variables from being committed.

---

# Running the Project

Run the Python scripts in pipeline order.

Start with data understanding and cleaning.

Then generate the daily KPI dataset.

Run anomaly detection.

Run the machine learning model.

Compare the anomaly detection methods.

Generate final anomaly decisions.

Run anomaly investigation and business impact analysis.

Generate AI explanations.

Generate alerts.

Update alert history.

Run the final validation script.

The final validation script is:

    25_final_project_test.py

---

# Running the Dashboard

Start the Streamlit dashboard using:

    streamlit run 20_final_dashboard.py

The dashboard will open in the browser.

It provides an interactive view of:

- Business KPIs
- Revenue trends
- Profit trends
- Anomalies
- Business impact
- Alerts
- AI explanations
- Alert history

---

# Running Email Alerts

First test the email configuration using:

    21_email_alert_test.py

Then send a business anomaly alert using:

    22_send_business_alert.py

For automated monitoring, run:

    23_automated_monitoring.py

The automated monitoring script checks whether an alert is new before sending an email.

---

# Project Validation

The final validation script checks whether all major project components are working correctly.

The validation checks:

- Required files
- Main data
- Anomaly counts
- Business impact
- Alert counts
- Alert history
- Duplicate alert dates

The final validation result is:

    PROJECT VALIDATION PASSED

---

# Methodology

The project follows a hybrid anomaly monitoring methodology.

## Stage 1: Statistical Detection

Z-score identifies individual KPI deviations.

## Stage 2: Machine Learning Detection

Isolation Forest identifies unusual combinations of KPIs.

## Stage 3: Model Comparison

The results from both models are compared.

## Stage 4: Final Decision

The system assigns:

- Confirmed Anomaly
- Possible Anomaly
- Normal

## Stage 5: Investigation

The system identifies the main KPI causes.

## Stage 6: Business Impact

The system estimates revenue, profit, and order impact.

## Stage 7: AI Explanation

Rule-based logic and LLM capabilities convert technical results into business-friendly explanations.

## Stage 8: Alerting

Important anomalies are converted into alerts.

## Stage 9: Automation

Email notifications are sent for new alerts.

## Stage 10: Visualization

The Streamlit dashboard provides an interactive monitoring interface.

---

# AI Architecture

The AI architecture uses multiple layers instead of depending entirely on an LLM.

    Business Data
          ↓
    KPI Engineering
          ↓
    Statistical Detection
          ↓
    ML Detection
          ↓
    Model Agreement
          ↓
    Business Impact
          ↓
    Rule-Based Reasoning
          ↓
    LLM Explanation
          ↓
    Alert Automation

This hybrid architecture combines deterministic analysis with generative AI.

---

# Why This Architecture?

Different technologies solve different parts of the problem.

Statistical methods are useful for detecting KPI-level deviations.

Machine learning is useful for identifying unusual multivariate patterns.

Rule-based logic provides consistent business decisions.

LLMs are useful for converting technical outputs into human-readable explanations.

Email automation enables real-time communication.

Streamlit provides a visual monitoring interface.

Combining these components creates an end-to-end AI business monitoring system.

---

# Alert Logic

The alert system follows this logic:

    Anomaly Detected
            ↓
    Calculate Business Impact
            ↓
    Is Impact High or Critical?
            ↓
       YES       NO
        ↓         ↓
      Alert     No Alert
        ↓
    Check Alert History
        ↓
    Is Alert New?
        ↓
     YES → Send Email
        ↓
    Update History

This reduces duplicate notifications.

---

# Dashboard Capabilities

The final dashboard allows users to monitor:

- Total orders
- Total revenue
- Total profit
- Revenue trends
- Profit trends
- Confirmed anomalies
- Possible anomalies
- Business impact
- High-priority alerts
- Alert explanations
- Investigation results
- Alert history

The dashboard acts as the business-facing layer of the anomaly monitoring system.

---

# Limitations

The project has several limitations.

## Historical Baseline

The current anomaly detection approach primarily uses historical KPI behavior.

Seasonality and business-specific calendar effects may require additional modeling.

## LLM API Limits

LLM usage is intentionally selective because API usage can be limited by rate limits and cost.

The system therefore does not send every anomaly to the LLM.

## Rule-Based Impact Thresholds

Business impact classifications use predefined thresholds.

Real organizations may use thresholds specific to their industry and business size.

## Dataset Simulation

The project dataset represents e-commerce business activity and may not perfectly represent a production organization's operational data.

---

# Future Improvements

Potential future improvements include:

- Real-time data ingestion
- Streaming anomaly detection
- Advanced time-series forecasting
- Seasonal anomaly detection
- Prophet or ARIMA-based forecasting
- Autoencoder-based anomaly detection
- Advanced NLP analysis of customer reviews
- Root-cause analysis using causal models
- Slack or Microsoft Teams alerts
- SMS notifications
- Cloud deployment
- Docker deployment
- AWS or Azure integration
- Database integration
- Automated scheduled monitoring
- Role-based dashboard access
- More advanced LLM agents
- Business-specific anomaly thresholds
- Feedback-based anomaly learning

---

# Learning Outcomes

This project demonstrates practical understanding of:

- Data cleaning
- Data preprocessing
- Feature engineering
- KPI design
- Statistical analysis
- Anomaly detection
- Unsupervised machine learning
- Isolation Forest
- Model comparison
- Business impact analysis
- Explainable AI
- LLM integration
- API integration
- Email automation
- Dashboard development
- Python project architecture
- Environment variable management
- Git and GitHub practices

---

# Skills Demonstrated

## Data Science

- Pandas
- NumPy
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- KPI Analytics

## Machine Learning

- Unsupervised Learning
- Isolation Forest
- Statistical Anomaly Detection
- Model Comparison

## Artificial Intelligence

- LLM Integration
- Prompt Engineering
- AI-Based Explanation
- Hybrid AI Architecture

## Software Engineering

- Modular Python Scripts
- File-Based Data Pipeline
- Environment Variables
- Error Handling
- Automation

## Visualization

- Streamlit
- KPI Dashboards
- Business Monitoring
- Data Visualization

## Automation

- SMTP
- Gmail App Password
- Automated Alerts
- Alert History
- Duplicate Prevention

---

# Project Highlights

The project demonstrates an end-to-end business AI workflow rather than only a machine learning model.

Key highlights include:

- 1,826 daily business records
- Multiple KPI monitoring
- Statistical anomaly detection
- Machine learning anomaly detection
- Model agreement analysis
- Automated root-cause investigation
- Business impact estimation
- AI-generated explanations
- LLM integration
- Automated email alerts
- Alert history tracking
- Duplicate alert prevention
- Interactive Streamlit dashboard
- Final project validation

---

# Portfolio / Resume Description

## Short Description

AI-powered business anomaly monitoring system that combines statistical analysis, Isolation Forest, business impact analysis, LLM-based explanations, automated email alerts, and a Streamlit dashboard to detect and explain unusual e-commerce business behavior.

---

# Resume Bullet Points

- Developed an end-to-end AI-powered business anomaly monitoring system using Python, Pandas, Scikit-learn, and Streamlit to monitor daily e-commerce KPIs.

- Implemented Z-score statistical anomaly detection and Isolation Forest to identify unusual business behavior across revenue, profit, orders, customer, payment, and delivery KPIs.

- Built a hybrid anomaly decision framework combining statistical and machine learning outputs to classify events as confirmed, possible, or normal anomalies.

- Automated anomaly investigation and business impact analysis by identifying contributing KPIs and estimating revenue, profit, and order impact.

- Integrated an LLM-based explanation layer to convert technical anomaly results into concise business-friendly insights.

- Developed automated email alerting with Gmail SMTP and alert-history tracking to prevent duplicate notifications.

- Built an interactive Streamlit dashboard for monitoring KPIs, anomaly trends, business impact, AI explanations, and high-priority alerts.

---

# Interview Explanation

If asked:

"What is your project?"

A concise explanation is:

"This project is an AI-powered business anomaly monitoring agent for e-commerce data. The system takes transaction-level business data and converts it into daily KPIs such as revenue, profit, orders, customer rating, payment failure rate, and delivery delay rate.

I used Z-score analysis for statistical anomaly detection and Isolation Forest for machine learning-based anomaly detection. I then compared the outputs of both models to determine whether an anomaly was confirmed or only possible.

After detecting an anomaly, the system investigates the main KPI causes and calculates its business impact in terms of revenue, profit, and orders. I also added an AI explanation layer using an LLM to convert the technical results into business-friendly explanations.

Finally, the system generates high-priority alerts, sends email notifications for new alerts, maintains alert history to avoid duplicates, and displays everything through a Streamlit dashboard."

---

# Project Workflow Summary

    1. Load Business Data
    ↓
    2. Understand Data
    ↓
    3. Clean Data
    ↓
    4. Preprocess Data
    ↓
    5. Generate Daily KPIs
    ↓
    6. Validate KPIs
    ↓
    7. Detect Anomalies Using Z-score
    ↓
    8. Detect Anomalies Using Isolation Forest
    ↓
    9. Compare Models
    ↓
    10. Make Final Anomaly Decision
    ↓
    11. Investigate Anomaly Causes
    ↓
    12. Calculate Business Impact
    ↓
    13. Generate AI Explanation
    ↓
    14. Generate Alerts
    ↓
    15. Maintain Alert History
    ↓
    16. Send Email Notifications
    ↓
    17. Display Results in Streamlit
    ↓
    18. Validate Complete Project

---

# Conclusion

The AI-Powered Business Anomaly Monitoring Agent demonstrates how data science, machine learning, artificial intelligence, automation, and visualization can be combined into a practical business monitoring solution.

Instead of simply detecting unusual values, the system attempts to answer the complete business monitoring workflow:

    What happened?
        ↓
    Which KPIs changed?
        ↓
    Is the anomaly statistically or algorithmically supported?
        ↓
    How severe is it?
        ↓
    What is the business impact?
        ↓
    Why did it happen?
        ↓
    How should the result be communicated?
        ↓
    Has this alert already been sent?

The final system provides an end-to-end framework for detecting, investigating, explaining, and communicating unusual business behavior.

---

# Author

Somya

MSc Applied Data Science

BSc Statistics

---

# Project Summary

AI-Powered Business Anomaly Monitoring Agent

    Data
    ↓
    Analytics
    ↓
    Machine Learning
    ↓
    Anomaly Detection
    ↓
    Investigation
    ↓
    Business Impact
    ↓
    AI Explanation
    ↓
    Alert Automation
    ↓
    Dashboard

An end-to-end portfolio project demonstrating practical Data Science, Machine Learning, AI, LLM integration, automation, and business analytics skills.