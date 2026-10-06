# Project Documentation — HR Employee Attrition Analysis

## Objective
Analyze employee attrition patterns and identify employee segments with comparatively higher attrition rates.

## Dataset
Synthetic HR employee dataset created for portfolio/educational use. It contains no real employee PII.

## Workflow
Raw CSV → data quality checks/cleaning → cleaned CSV → Excel / SQLite SQL / Python → Power BI dashboard.

## Verified dataset
- Raw rows: 1,471
- Cleaned rows: 1,470
- Cleaned columns: 35
- Employees left: 408
- Overall attrition: 27.8%

## Verified KPIs
- Total employees: 1,470
- Employees left: 408
- Attrition rate: 27.8%
- Average monthly income: ₹5,848
- Average tenure: 6.3 years

## Data-quality issues represented in the raw file
The raw dataset contains a small number of intentionally preserved quality issues for demonstration: missing values, a duplicate EmployeeID and a text-standardization issue. The cleaned dataset resolves these issues and adds analysis-ready derived columns.

## Analysis
The project examines attrition by department, job role, overtime, salary range, age group, tenure group and satisfaction level.

## Interpretation
The analysis identifies associations in observational data. It does not prove that a particular factor causes employees to leave.

## Tools
Excel, SQLite/SQL, Python/Pandas/Matplotlib, Power BI and Git/GitHub.

## Power BI limitation
The repository is Power BI-ready, but the native `.pbix` file must be saved from Power BI Desktop. The supplied Power BI documentation contains the model, DAX and dashboard specification.
