notes.md

## What I Learned
- Data validation is important
- Edge cases matter
- Structured functions improve readability

Runs 5 data quality checks on a sample dataset:

| Check | What it catches |
|---|---|
| Missing Values | `None` or empty strings |
| Score Range | Values outside 0–100 |
| Negative Age | Age below 0 |
| Email Format | Missing `@` or `.` |
| Status Casing | Values like `"PASS"` instead of `"pass"` |

Then prints a summary with basic statistics (mean, median, stdev) and a status distribution.

### Sample Output

```
=======================================================
       🧪 DATA QUALITY REPORT
=======================================================

[❌ FAIL] Missing Values
  Row 3 [Carol]: 'age' is missing
  Row 6 [UNKNOWN]: 'name' is missing

[❌ FAIL] Score Out of Range
  Row 4 [Dave]: score=101 is out of range [0-100]

[✅ PASS] Negative Age — no issues!
...

=======================================================
  Total rows checked : 10
  Total issues found : 6
=======================================================

       📊 DATA ANALYSIS SUMMARY

📈 Score Statistics:
  mean    : 80.5
  median  : 80.0
  stdev   : 13.72

🗂  Status Distribution:
  pass  : ██████ (6)
  fail  : ████ (4)
```

## Problems Faced
- Handling missing values
- Validating incorrect email formats
- Standardizing status values

## Conclusions

The analysis identified multiple data quality issues:
- Missing age and name fields
- Invalid score values above accepted range
- Incorrect email formatting
- Negative age values
- Inconsistent capitalization in status labels

The project demonstrates how Python can be used to:
- automate validation checks
- improve dataset reliability
- support QA workflows
- reduce manual inspection effort

This project also highlights the importance of clean data in analytics and software systems.
