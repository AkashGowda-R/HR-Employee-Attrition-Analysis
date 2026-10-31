# Final Project Validation

## Dataset validation
- Cleaned employee records: **1,470**
- Employees who left: **408**
- Attrition rate: **27.8%**
- Average monthly income: **₹5,848**
- Average tenure: **6.3 years**
- Cleaned dataset duplicate EmployeeIDs: **0**
- Cleaned dataset missing values: **0**

## Cross-tool validation
The cleaned CSV and supplied SQLite database produce the same headline KPIs. Excel analysis tables were regenerated from the cleaned CSV. Python validates the core row and attrition counts before producing its chart. SQL analysis queries execute successfully against the supplied database. The Power BI report uses the same cleaned dataset and its displayed headline KPI values were checked against the verified baseline above.

## Presentation and reporting completed
- Rebuilt Excel workbook with consistent headers, widths, freezes and professional dashboard/KPI presentation.
- Rebuilt dashboard preview with clear KPI cards and segment charts.
- Tightened SQL documentation so data-quality validation is distinguished from the earlier CSV cleaning step.
- Added reproducible Python validation and output generation.
- Completed the Power BI report in Power BI Desktop and saved `powerbi/HR_Attrition_Analysis.pbix`.
- Saved the dashboard screenshot as `dashboard/powerbi_dashboard.png`.
- Added Power BI model, DAX, layout and theme documentation.
- Committed and pushed the PBIX file to the GitHub repository (commit `c6a5d16`).
- Removed claims that could imply causal relationships.

## Limitations
This is a synthetic, observational dataset created for portfolio/educational use. It contains no real employee PII. The analysis is descriptive and does not establish causation.
