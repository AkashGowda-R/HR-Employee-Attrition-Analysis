# Power BI — HR Employee Attrition Analysis

## Status
The project is Power BI-ready, but the native `.pbix` file is not included because Power BI Desktop is required to create/save it. The supplied CSV, DAX measures, model definition and dashboard specification are the source materials for the report.

## Data source
Import `../data/cleaned_hr_attrition.csv`. Rename the imported table to `Employees`.

## Recommended report pages
Use one main page named **HR Attrition Overview**. Keep the report beginner-friendly and focused on the business question.

## Required verification before saving the PBIX
- Total Employees = 1,470
- Employees Left = 408
- Attrition Rate = 27.8%
- Average Monthly Income = ₹5,848
- Average Tenure = 6.3 years

## Important interpretation rule
The dataset is synthetic and observational. The dashboard shows associations and patterns, not proven causes of attrition.

## Final filename
Save the manually created report as `HR_Attrition_Analysis.pbix`.
