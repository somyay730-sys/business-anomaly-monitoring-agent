import pandas as pd
import os

print("=" * 60)
print("STEP 17: ALERT HISTORY")
print("=" * 60)

alerts_file = "data/alerts.csv"
history_file = "data/alert_history.csv"

alerts = pd.read_csv(alerts_file)

if os.path.exists(history_file):
    history = pd.read_csv(history_file)
else:
    history = pd.DataFrame(columns=alerts.columns)

new_alerts = alerts[
    ~alerts["order_date"].isin(history["order_date"])
].copy()

if len(new_alerts) > 0:
    history = pd.concat(
        [history, new_alerts],
        ignore_index=True
    )

history.to_csv(history_file, index=False)

print("Current alerts:", len(alerts))
print("New alerts:", len(new_alerts))
print("Total alert history:", len(history))

print()
print("Alert history saved to:")
print(history_file)

print()
print("Step 17 completed successfully!")