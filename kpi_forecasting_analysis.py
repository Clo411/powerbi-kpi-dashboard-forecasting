"""
Power BI KPI Dashboard & Forecasting Models
Author: Clovis Niyomwungere
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_kpi_dataset.csv")
df["Month"] = pd.to_datetime(df["Month"])

summary = {
    "average_resolution_rate": round(df["Resolution_Rate"].mean(), 2),
    "total_reporting_hours_saved": int(df["Reporting_Hours_Saved"].sum()),
    "average_kpi_score": round(df["KPI_Performance_Score"].mean(), 1),
    "total_tickets_logged": int(df["IT_Tickets_Logged"].sum()),
    "total_tickets_resolved": int(df["Tickets_Resolved"].sum())
}

print(summary)

plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["KPI_Performance_Score"], marker="o")
plt.title("KPI Performance Score Trend")
plt.xlabel("Month")
plt.ylabel("KPI Performance Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("kpi_performance_trend.png")
