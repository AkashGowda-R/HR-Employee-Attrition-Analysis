-- HR ATTRITION ANALYSIS QUERIES

-- Overall KPI
SELECT COUNT(*) AS total_employees,
       SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees;

-- Department
SELECT Department, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY Department
ORDER BY attrition_rate_pct DESC;

-- Job role: restrict to roles with at least 10 employees to avoid overinterpreting tiny groups
SELECT JobRole, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY JobRole
HAVING COUNT(*) >= 10
ORDER BY attrition_rate_pct DESC;

-- Overtime
SELECT Overtime, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees GROUP BY Overtime ORDER BY attrition_rate_pct DESC;

-- Salary range
SELECT SalaryRange, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees GROUP BY SalaryRange ORDER BY attrition_rate_pct DESC;

-- Age group
SELECT AgeGroup, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees GROUP BY AgeGroup ORDER BY attrition_rate_pct DESC;

-- Tenure group
SELECT TenureGroup, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees GROUP BY TenureGroup ORDER BY attrition_rate_pct DESC;

-- Satisfaction label
SELECT SatisfactionLabel, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
       ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees GROUP BY SatisfactionLabel ORDER BY attrition_rate_pct DESC;

-- Department ranking
WITH d AS (
    SELECT Department, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
           1.0 * SUM(AttritionFlag) / COUNT(*) AS rate
    FROM employees GROUP BY Department
)
SELECT *, RANK() OVER (ORDER BY rate DESC) AS dept_rank FROM d;

-- Job-role ranking for roles with at least 10 employees
WITH r AS (
    SELECT JobRole, COUNT(*) AS employees, SUM(AttritionFlag) AS employees_left,
           1.0 * SUM(AttritionFlag) / COUNT(*) AS rate
    FROM employees GROUP BY JobRole
)
SELECT *, DENSE_RANK() OVER (ORDER BY rate DESC) AS role_rank
FROM r WHERE employees >= 10;

-- Employee-level detail joined to department summary
WITH department_summary AS (
    SELECT Department,
           COUNT(*) AS department_employees,
           SUM(AttritionFlag) AS department_left
    FROM employees
    GROUP BY Department
)
SELECT e.EmployeeID, e.Department, e.JobRole, e.Attrition,
       d.department_employees, d.department_left
FROM employees e
JOIN department_summary d
  ON e.Department = d.Department
WHERE e.Attrition = 'Yes';

-- Simple business-rule segmentation using CASE
SELECT
    CASE
        WHEN Overtime = 'Yes' AND JobSatisfaction <= 2 AND YearsAtCompany <= 5
            THEN 'Overtime + lower satisfaction + early tenure'
        WHEN Overtime = 'Yes' AND YearsAtCompany <= 5
            THEN 'Overtime + early tenure'
        WHEN JobSatisfaction <= 2
            THEN 'Lower satisfaction'
        ELSE 'Other'
    END AS segment,
    COUNT(*) AS employees,
    SUM(AttritionFlag) AS employees_left,
    ROUND(100.0 * SUM(AttritionFlag) / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY segment
ORDER BY attrition_rate_pct DESC;
