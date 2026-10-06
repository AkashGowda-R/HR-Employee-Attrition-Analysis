"""HR Employee Attrition Analysis
Reproducible beginner-friendly analysis using the project's cleaned CSV.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "cleaned_hr_attrition.csv"
OUTPUT_DIR = ROOT / "dashboard" / "python_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

EXPECTED_ROWS = 1470
EXPECTED_LEFT = 408
EXPECTED_ATTRITION = 27.755102040816325


def attrition_summary(data):
    data = data.copy()
    data["AttritionFlag"] = data["Attrition"].eq("Yes").astype(int)
    return {
        "Total Employees": len(data),
        "Employees Left": int(data["AttritionFlag"].sum()),
        "Attrition Rate": data["AttritionFlag"].mean(),
        "Average Monthly Income": data["MonthlyIncome"].mean(),
        "Average Tenure": data["YearsAtCompany"].mean(),
    }


def segment_analysis(data, column, minimum_employees=0):
    grouped = data.groupby(column, observed=False).agg(
        Employees=("EmployeeID", "count"),
        EmployeesLeft=("AttritionFlag", "sum"),
    ).reset_index()
    grouped["AttritionRate"] = grouped["EmployeesLeft"] / grouped["Employees"]
    return grouped[grouped["Employees"] >= minimum_employees].sort_values("AttritionRate", ascending=False)


def main():
    df = pd.read_csv(DATA_PATH)
    df["AttritionFlag"] = df["Attrition"].eq("Yes").astype(int)

    if len(df) != EXPECTED_ROWS:
        raise ValueError(f"Expected {EXPECTED_ROWS} cleaned rows, found {len(df)}")
    if int(df["AttritionFlag"].sum()) != EXPECTED_LEFT:
        raise ValueError("Employee-left count does not match the verified project baseline")

    summary = attrition_summary(df)
    print("=== VERIFIED KPI SUMMARY ===")
    for key, value in summary.items():
        print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")

    print("\n=== SEGMENT ANALYSIS ===")
    for column in ["Department", "JobRole", "Overtime", "SalaryRange", "AgeGroup", "TenureGroup", "SatisfactionLabel"]:
        minimum = 10 if column == "JobRole" else 0
        result = segment_analysis(df, column, minimum)
        print(f"\n{column}")
        print(result.to_string(index=False, formatters={"AttritionRate": lambda x: f"{x:.1%}"}))

    # Department chart used as a simple reproducible visual.
    dept = segment_analysis(df, "Department")
    plt.figure(figsize=(8, 5))
    plt.barh(dept["Department"], dept["AttritionRate"] * 100)
    plt.xlabel("Attrition Rate (%)")
    plt.title("Attrition Rate by Department")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "attrition_by_department.png", dpi=160, bbox_inches="tight")
    plt.close()

    print(f"\nChart saved to: {OUTPUT_DIR / 'attrition_by_department.png'}")


if __name__ == "__main__":
    main()
