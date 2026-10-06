-- DATA QUALITY VALIDATION
-- Note: the cleaned CSV was prepared before loading the SQLite database.
-- This script documents and validates the quality checks performed on the loaded table.

-- 1. Check missing key fields
SELECT
    SUM(CASE WHEN EmployeeID IS NULL OR TRIM(EmployeeID) = '' THEN 1 ELSE 0 END) AS missing_employee_id,
    SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS missing_age,
    SUM(CASE WHEN Department IS NULL OR TRIM(Department) = '' THEN 1 ELSE 0 END) AS missing_department
FROM employees;

-- 2. Check duplicate employee IDs
SELECT EmployeeID, COUNT(*) AS duplicate_count
FROM employees
GROUP BY EmployeeID
HAVING COUNT(*) > 1;

-- 3. Check categorical values
SELECT DISTINCT Attrition FROM employees ORDER BY Attrition;
SELECT DISTINCT Overtime FROM employees ORDER BY Overtime;
SELECT DISTINCT BusinessTravel FROM employees ORDER BY BusinessTravel;

-- 4. Check satisfaction range
SELECT * FROM employees WHERE JobSatisfaction NOT BETWEEN 1 AND 4;

-- Expected result on the supplied cleaned database: no invalid/missing/duplicate records returned.
