# Power BI Build Checklist

The only remaining manual application step in the project is saving the native Power BI `.pbix`, because Power BI Desktop is required for that proprietary file format.

- [ ] Import `data/cleaned_hr_attrition.csv`
- [ ] Rename table to `Employees`
- [ ] Create measures from `DAX_MEASURES.md`
- [ ] Format measures
- [ ] Create five KPI cards
- [ ] Add the five slicers
- [ ] Create the seven recommended visuals
- [ ] Check that 1,470 / 408 / 27.8% / ₹5,848 / 6.3 years appear with no slicers
- [ ] Save as `HR_Attrition_Analysis.pbix`
- [ ] Put the `.pbix` in `powerbi/` only if repository size remains reasonable
