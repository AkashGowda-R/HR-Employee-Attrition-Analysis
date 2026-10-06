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
The cleaned CSV and supplied SQLite database produce the same headline KPIs. Excel analysis tables were regenerated from the cleaned CSV. Python validates the core row and attrition counts before producing its chart. SQL analysis queries execute successfully against the supplied database.

## Presentation improvements completed
- Rebuilt Excel workbook with consistent headers, widths, freezes and professional dashboard/KPI presentation.
- Rebuilt dashboard preview with clear KPI cards and segment charts.
- Tightened SQL documentation so data-quality validation is distinguished from the earlier CSV cleaning step.
- Added reproducible Python validation and output generation.
- Updated Power BI DAX/model/layout documentation to the verified KPI baseline.
- Added a simple Power BI theme JSON.
- Removed claims that could imply causal relationships.

## One external application limitation
A native `.pbix` file cannot be generated in this environment because it is created/saved by Power BI Desktop. Everything required to create the report is included in `powerbi/` and the cleaned dataset is included in `data/`.
