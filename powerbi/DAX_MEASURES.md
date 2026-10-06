# DAX Measures

After importing `cleaned_hr_attrition.csv`, rename the table to `Employees`. Create these measures:

```DAX
Total Employees = COUNTROWS(Employees)

Employees Left = CALCULATE(
    [Total Employees],
    Employees[Attrition] = "Yes"
)

Attrition Rate = DIVIDE(
    [Employees Left],
    [Total Employees],
    0
)

Employees Stayed = CALCULATE(
    [Total Employees],
    Employees[Attrition] = "No"
)

Average Monthly Income = AVERAGE(Employees[MonthlyIncome])

Average Tenure = AVERAGE(Employees[YearsAtCompany])

Average Job Satisfaction = AVERAGE(Employees[JobSatisfaction])
```

Format `Attrition Rate` as Percentage with one decimal place. Format `Average Monthly Income` as currency/whole number and `Average Tenure` as one decimal place.
