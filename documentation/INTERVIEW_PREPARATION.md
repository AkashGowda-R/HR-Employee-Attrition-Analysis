# Interview Preparation

## Tell me about your project
I built an HR Employee Attrition Analysis project to understand patterns associated with employees leaving an organization. I worked from a synthetic employee dataset, validated the raw data and used a cleaned analysis dataset across Excel, SQLite SQL and Python, then prepared the Power BI dashboard design and DAX measures. The analysis looked at attrition by department, job role, overtime, salary range, age group, tenure and job satisfaction. The dataset had 1,470 employees after cleaning, with 408 employees marked as having left, giving an overall attrition rate of 27.8%. I treated the findings as associations rather than causal conclusions because the data is observational and synthetic.

## Core questions and answers

### 1. Why did you use a synthetic dataset?
I wanted a consistent dataset that I could legally use for a portfolio project and control from raw data through cleaning and reporting. I clearly documented that it is synthetic and educational.

### 2. What did you clean?
I standardized whitespace and inconsistent text values, handled selected missing numeric values using the median, removed a duplicate employee ID, and created derived fields such as age group, salary range, tenure group and an attrition flag.

### 3. What was the attrition rate?
27.8%: 408 employees left out of 1,470 cleaned employee records.

### 4. What did you find about overtime?
Employees marked for overtime had a 36.1% observed attrition rate versus 24.4% for employees not marked for overtime. I would describe this as an association, not proof that overtime causes attrition.

### 5. Which department had the highest attrition rate?
Research & Development had the highest observed department attrition rate at 27.9% in this dataset.

### 6. Which job role had the highest attrition?
Sales Representative had the highest observed rate among roles with at least 10 employees, at 32.6%.

### 7. How did you calculate attrition rate in SQL?
I divided the number of employees with AttritionFlag = 1 by the total number of employees and multiplied by 100 for a percentage.

### 8. Why use AttritionFlag?
It converts the Yes/No attrition field into 1/0, which makes aggregation straightforward with SUM and makes the same calculation easy to reproduce in Excel, SQL, Python and Power BI.

### 9. Why SQLite?
SQLite is simple for an entry-level portfolio because it requires no database server and supports the SQL concepts demonstrated in the project, including CTEs and window functions.

### 10. What SQL concepts did you use?
SELECT, WHERE, GROUP BY, HAVING, ORDER BY, CASE, aggregate functions, CTEs, JOINs and window functions.

### 11. What does the Power BI dashboard show?
KPI cards for total employees, employees left, attrition rate, average salary and average tenure, plus charts for department, job role, age, salary, overtime, tenure and job satisfaction, with slicers for department, gender, job role, overtime and age group.

### 12. What is a DAX measure?
A DAX measure is a calculation evaluated in the current filter context in Power BI. For example, Attrition Rate uses Employees Left divided by Total Employees, so slicers automatically recalculate the rate for the selected segment.

### 13. Why not claim that overtime causes attrition?
Because this analysis is observational. A higher rate among overtime employees shows an association in this dataset, but other variables could contribute to the pattern and the analysis does not establish causation.

### 14. What would you improve with real company data?
I would add dates, location, manager, recruitment source, compensation components and exit reasons. I would also perform statistical testing and, if appropriate, build a predictive model with proper validation.

### 15. What is the biggest limitation?
The dataset is synthetic, so the findings demonstrate analytical technique rather than representing a real organization's workforce.

## Excel-specific questions

**How did you calculate KPIs?** I used the cleaned employee dataset to produce KPI summaries and percentage calculations, then used Excel tables and charts to present the results.

**Why separate raw and cleaned data?** It preserves the original input and makes the transformation process auditable.

**Why use charts?** To make segment-level attrition differences easier to compare quickly.

## Power BI-specific questions

**Why a single-table model?** The dataset is already at employee grain and the dashboard does not require multiple fact/dimension tables, so a single table keeps the beginner project understandable.

**What happens when a slicer is changed?** The filter context changes and measures such as Total Employees, Employees Left and Attrition Rate recalculate for the selected employees.

## Business questions

**What would you investigate first?** I would prioritize high-attrition segments with meaningful employee counts, then investigate workload, tenure, compensation, satisfaction and management context before recommending interventions.
