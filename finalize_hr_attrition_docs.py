from pathlib import Path

FILES = {
    "README.md": """# HR Employee Attrition Analysis

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
- The `<4K` salary range shows approximately **45.1%** attrition.
- Employees aged 18–24 show approximately **52.5%** attrition.
- Employees with 0–2 years at the company show approximately **42.7%** attrition.
- The Low job-satisfaction group shows approximately **35.2%** attrition.

These findings describe **associations**, not proven causes.

## Power BI dashboard
The Power BI report is completed and included in this repository as `powerbi/HR_Attrition_Analysis.pbix`.

![Power BI Dashboard](dashboard/powerbi_dashboard.png)

To explore the interactive report, download the PBIX file and open it in Power BI Desktop.

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
Open `powerbi/HR_Attrition_Analysis.pbix` in Power BI Desktop. Supporting model, DAX and layout notes are available in the `powerbi/` folder.

## Documentation
- `documentation/PROJECT_DOCUMENTATION.md` — project methodology and verified results
- `documentation/DATA_DICTIONARY.md` — field definitions
- `documentation/BUSINESS_INSIGHTS.md` — findings and recommendations
- `documentation/INTERVIEW_PREPARATION.md` — project-specific interview preparation
- `documentation/FINAL_VALIDATION.md` — validation summary

## Limitations
This is a synthetic, observational dataset. The analysis is descriptive and does not establish causation. Real HR decisions should be based on validated organizational data, employee feedback and appropriate statistical analysis.
""",
    "documentation/PROJECT_DOCUMENTATION.md": """# Project Documentation — HR Employee Attrition Analysis

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

## Power BI report
The interactive Power BI report has been created in Power BI Desktop, saved as `powerbi/HR_Attrition_Analysis.pbix` and committed to the GitHub repository. The dashboard screenshot is available at `dashboard/powerbi_dashboard.png`. Supporting model, DAX measures and layout documentation are included in `powerbi/`.

## Interpretation
The analysis identifies associations in observational data. It does not prove that a particular factor causes employees to leave.

## Tools
Excel, SQLite/SQL, Python/Pandas/Matplotlib, Power BI and Git/GitHub.
""",
    "documentation/BUSINESS_INSIGHTS.md": """# Business Insights

## Overall picture
The cleaned dataset contains **1,470 employees**, of whom **408 left**, producing an overall attrition rate of **27.8%**.

## Observed patterns

| Segment | Attrition rate | Interpretation |
|---|---:|---|
| Research & Development | 27.9% | Highest department rate, but very close to Sales |
| Sales Representative | 32.6% | Highest rate among job roles with at least 10 employees |
| Overtime = Yes | 36.1% | Higher observed attrition than the non-overtime group |
| Salary <4K | 45.1% | Highest observed salary-band attrition |
| Age 18–24 | 52.5% | Highest observed age-group attrition |
| Tenure 0–2 years | 42.7% | Highest observed tenure-group attrition |
| Low job satisfaction | 35.2% | Higher observed attrition than higher-satisfaction groups |

## Practical recommendations
1. Review early-tenure onboarding and support because the 0–2 year group has a comparatively high observed attrition rate.
2. Examine workload and scheduling for employees working overtime.
3. Review compensation progression for lower salary bands.
4. Investigate retention challenges in roles with higher observed attrition, especially Sales Representative.
5. Use satisfaction and exit feedback to investigate whether these patterns persist in real organizational data.

## Important caveat
These are **associations**, not causal conclusions. The dataset is synthetic and observational, so the analysis cannot establish that overtime, salary, age, tenure or satisfaction directly causes attrition.
""",
    "powerbi/README_POWER_BI.md": """# Power BI — HR Employee Attrition Analysis

## Status
The Power BI report is complete. The native Power BI Desktop file is included in this repository at `powerbi/HR_Attrition_Analysis.pbix`, alongside the dashboard screenshot at `dashboard/powerbi_dashboard.png`.

## Open the report
Download `HR_Attrition_Analysis.pbix` from this folder and open it in Power BI Desktop. The cleaned CSV used by the report is available at `../data/cleaned_hr_attrition.csv`.

## Data model
The imported data table is named `Employees`. The supporting DAX measures, model notes and dashboard layout are documented in this folder.

## Verified KPI baseline
- Total Employees = 1,470
- Employees Left = 408
- Attrition Rate = 27.8%
- Average Monthly Income = ₹5,848
- Average Tenure = 6.3 years

## Important interpretation rule
The dataset is synthetic and observational. The dashboard shows associations and patterns, not proven causes of attrition.
""",
    "documentation/FINAL_VALIDATION.md": """# Final Project Validation

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
"""
}

def main():
    root = Path(__file__).resolve().parent
    missing = [name for name in FILES if not (root / name).is_file()]
    if missing:
        raise SystemExit(
            "Run this script from the root of your HR-Employee-Attrition-Analysis "
            "repository. Missing expected files: " + ", ".join(missing)
        )

    for name, content in FILES.items():
        target = root / name
        target.write_text(content, encoding="utf-8", newline="\n")
        print(f"Updated: {name}")

    print("\nDocumentation update completed. Next run:")
    print("git status")
    print('git add README.md documentation/PROJECT_DOCUMENTATION.md '
          'documentation/BUSINESS_INSIGHTS.md powerbi/README_POWER_BI.md '
          'documentation/FINAL_VALIDATION.md')
    print('git commit -m "Finalize project documentation"')
    print("git push origin main")

if __name__ == "__main__":
    main()
