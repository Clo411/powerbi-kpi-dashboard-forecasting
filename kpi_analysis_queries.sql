-- KPI Dashboard & Forecasting Project
-- Author: Clovis Niyomwungere

SELECT Month, Users_Supported, IT_Tickets_Logged, Tickets_Resolved,
       Resolution_Rate, System_Downtime_Hours, Reporting_Hours_Saved,
       KPI_Performance_Score
FROM sample_kpi_dataset
ORDER BY Month;

SELECT ROUND(AVG(Resolution_Rate), 2) AS Average_Resolution_Rate
FROM sample_kpi_dataset;

SELECT SUM(Reporting_Hours_Saved) AS Total_Reporting_Hours_Saved
FROM sample_kpi_dataset;

SELECT Month, System_Downtime_Hours
FROM sample_kpi_dataset
WHERE System_Downtime_Hours > 10
ORDER BY System_Downtime_Hours DESC;
