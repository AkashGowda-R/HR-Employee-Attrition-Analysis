# Power BI Data Model

## Model
Use a simple single-table model:

`Employees`

No relationships are required for this project. A single-table model is appropriate because the dataset is a flat employee-level analytical dataset and the project goal is descriptive attrition analysis.

## Important fields
- EmployeeID — employee identifier
- Department — department category
- JobRole — job role
- Attrition — Yes/No outcome
- AttritionFlag — 1/0 helper field
- MonthlyIncome — numeric income field
- YearsAtCompany — tenure in years
- Overtime — Yes/No
- AgeGroup — derived age band
- SalaryRange — derived salary band
- TenureGroup — derived tenure band
- SatisfactionLabel — derived satisfaction category
