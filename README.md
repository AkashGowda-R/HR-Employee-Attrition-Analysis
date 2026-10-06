# HR Employee Attrition Analysis

Entry-level Data Analyst portfolio project analyzing employee attrition using one consistent synthetic HR dataset across **Excel, SQLite/SQL, Python/Pandas and Power BI**.

## Business question
What employee segments show comparatively higher attrition rates, and what areas could HR investigate further?

## Verified project KPIs
| KPI | Value |
|---|---:|
| Total Employees | **1,470** |
| Employees Left | **408** |
| Attrition Rate | **27.8%** |
| Average Monthly Income | **₹5,848** |
| Average Tenure | **6.3 years** |

## Key observed patterns
- Research & Development has the highest department attrition at approximately **27.9%**, only marginally above Sales.
- Sales Representative has the highest job-role attrition among roles with at least 10 employees at approximately **32.6%**.
- Employees working overtime show approximately **36.1%** attrition.
- The `<4K` salary range shows approximately **45.0%** attrition.
- Employees aged 18–24 show approximately **52.5%** attrition.
- Employees with 0–2 years at the company show approximately **42.7%** attrition.
- The Low job-satisfaction group shows approximately **35.2%** attrition.

These findings describe **associations**, not proven causes.

## Data
The dataset is synthetic and created for portfolio/educational use. It contains no real employee PII.

- `data/raw_hr_attrition.csv` — source snapshot containing demonstration data-quality issues
- `data/cleaned_hr_attrition.csv` — analysis-ready dataset with 1,470 rows and 35 columns
- `data/hr_attrition.db` — SQLite database containing the cleaned employee table

## Tools
- Microsoft Excel
- SQLite / SQL
- Python / Pandas / Matplotlib
- Power BI
- Git / GitHub

## Repository structure
```text
HR-Attrition-Analysis/
├── data/
├── excel/
├── sql/
├── python/
├── powerbi/
├── dashboard/
├── documentation/
├── README.md
└── .gitignore
```

## Reproduce the analysis
### Python
From the repository root:
```bash
python python/hr_attrition_analysis.py
```
The script validates the key baseline counts and creates a reproducible department attrition chart in `dashboard/python_outputs/`.

### SQL
Open `data/hr_attrition.db` in a SQLite client and run the SQL files in `sql/`.

### Excel
Open `excel/HR_Attrition_Analysis.xlsx`. The workbook contains the raw data, cleaned data, analysis tables, KPI summary and a presentation dashboard.

### Power BI
Import `data/cleaned_hr_attrition.csv`, rename the table to `Employees`, add the measures from `powerbi/DAX_MEASURES.md`, and build the report according to `powerbi/DASHBOARD_LAYOUT.md`.

**Native `.pbix` creation is the one step that cannot be generated outside Power BI Desktop.** The repository is otherwise Power BI-ready.

## Documentation
- `documentation/PROJECT_DOCUMENTATION.md` — project methodology and verified results
- `documentation/DATA_DICTIONARY.md` — field definitions
- `documentation/BUSINESS_INSIGHTS.md` — findings and recommendations
- `documentation/INTERVIEW_PREPARATION.md` — project-specific interview preparation

## Limitations
This is a synthetic, observational dataset. The analysis is descriptive and does not establish causation. Real HR decisions should be based on validated organizational data, employee feedback and appropriate statistical analysis.
# HR-Employee-Attrition-Analysis
