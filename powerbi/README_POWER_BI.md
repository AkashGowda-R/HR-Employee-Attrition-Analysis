# Power BI — HR Employee Attrition Analysis

## Status
The Power BI report is complete. The native Power BI Desktop file is included in this repository at `powerbi/HR_Attrition_Analysis.pbix`, alongside the dashboard screenshot at `dashboard/powerbi_dashboard.png`.

## Open the report
Download `HR_Attrition_Analysis.pbix` from this folder and open it in Power BI Desktop. The cleaned CSV used by the report is available at `../data/cleaned_hr_attrition.csv`.

## Data model
The imported data table is named `Employees`. The supporting DAX measures, model notes and dashboard layout are documented in this folder.

## Verified KPI baseline
- Total Employees = 1,470
- Employees Left = 408
- Attrition Rate = 27.8%
- Average Monthly Income = ₹5,848
- Average Tenure = 6.3 years

## Important interpretation rule
The dataset is synthetic and observational. The dashboard shows associations and patterns, not proven causes of attrition.
