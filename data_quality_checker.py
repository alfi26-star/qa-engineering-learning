# data_quality_checker.py
# Day 1 - Learning Python + Data Analysis with a QA mindset
# Goal: Become a QA Engineer

import csv
import statistics
from collections import Counter

# ── Sample dataset (simulating a CSV of test results) ──────────────────────────
# In real life you'd load this with: import pandas as pd; df = pd.read_csv("file.csv")

RAW_DATA = [
    {"name": "Alice",   "age": 28,  "score": 95,  "email": "alice@test.com",  "status": "pass"},
    {"name": "Bob",     "age": 34,  "score": 82,  "email": "bob@test.com",    "status": "pass"},
    {"name": "Carol",   "age": None,"score": 76,  "email": "carol@test.com",  "status": "fail"},
    {"name": "Dave",    "age": 22,  "score": 101, "email": "not-an-email",    "status": "pass"},
    {"name": "Eve",     "age": 29,  "score": 88,  "email": "eve@test.com",    "status": "PASS"},
    {"name": "",        "age": 31,  "score": 67,  "email": "anon@test.com",   "status": "fail"},
    {"name": "Frank",   "age": -5,  "score": 73,  "email": "frank@test.com",  "status": "fail"},
    {"name": "Grace",   "age": 27,  "score": 90,  "email": "grace@test.com",  "status": "pass"},
    {"name": "Heidi",   "age": 45,  "score": 55,  "email": "heidi@test.com",  "status": "fail"},
    {"name": "Ivan",    "age": 38,  "score": 78,  "email": "ivan@test.com",   "status": "pass"},
]

# ── QA Check Functions ──────────────────────────────────────────────────────────

def check_missing_values(data):
    """Check for None or empty string values in each record."""
    issues = []
    for i, row in enumerate(data):
        for key, value in row.items():
            if value is None or value == "":
                issues.append(f"  Row {i+1} [{row.get('name') or 'UNKNOWN'}]: '{key}' is missing")
    return issues


def check_score_range(data, min_val=0, max_val=100):
    """Scores must be between 0 and 100."""
    issues = []
    for i, row in enumerate(data):
        score = row.get("score")
        if score is not None and not (min_val <= score <= max_val):
            issues.append(f"  Row {i+1} [{row['name']}]: score={score} is out of range [{min_val}-{max_val}]")
    return issues


def check_age_positive(data):
    """Age must be a positive number."""
    issues = []
    for i, row in enumerate(data):
        age = row.get("age")
        if age is not None and age < 0:
            issues.append(f"  Row {i+1} [{row['name']}]: age={age} is negative")
    return issues


def check_email_format(data):
    """Very basic email check: must contain '@' and '.'"""
    issues = []
    for i, row in enumerate(data):
        email = row.get("email", "")
        if "@" not in email or "." not in email:
            issues.append(f"  Row {i+1} [{row['name']}]: email='{email}' looks invalid")
    return issues


def check_status_values(data, allowed=("pass", "fail")):
    """Status must be lowercase 'pass' or 'fail'."""
    issues = []
    for i, row in enumerate(data):
        status = row.get("status", "")
        if status.lower() not in allowed or status != status.lower():
            issues.append(
                f"  Row {i+1} [{row['name']}]: status='{status}' — expected lowercase 'pass' or 'fail'"
            )
    return issues


# ── Data Analysis Functions ─────────────────────────────────────────────────────

def summarize_scores(data):
    scores = [row["score"] for row in data if row.get("score") is not None]
    return {
        "count":   len(scores),
        "min":     min(scores),
        "max":     max(scores),
        "mean":    round(statistics.mean(scores), 2),
        "median":  statistics.median(scores),
        "stdev":   round(statistics.stdev(scores), 2),
    }


def status_distribution(data):
    statuses = [row["status"].lower() for row in data if row.get("status")]
    return dict(Counter(statuses))


# ── Runner ──────────────────────────────────────────────────────────────────────

def run_quality_checks(data):
    print("=" * 55)
    print("       🧪 DATA QUALITY REPORT")
    print("=" * 55)

    checks = {
        "Missing Values":      check_missing_values(data),
        "Score Out of Range":  check_score_range(data),
        "Negative Age":        check_age_positive(data),
        "Invalid Email":       check_email_format(data),
        "Invalid Status":      check_status_values(data),
    }

    total_issues = 0
    for check_name, issues in checks.items():
        status = "❌ FAIL" if issues else "✅ PASS"
        print(f"\n[{status}] {check_name}")
        for issue in issues:
            print(issue)
        total_issues += len(issues)

    print("\n" + "=" * 55)
    print(f"  Total rows checked : {len(data)}")
    print(f"  Total issues found : {total_issues}")
    print("=" * 55)


def run_analysis(data):
    print("\n" + "=" * 55)
    print("       📊 DATA ANALYSIS SUMMARY")
    print("=" * 55)

    stats = summarize_scores(data)
    print("\n📈 Score Statistics:")
    for key, val in stats.items():
        print(f"  {key:<8}: {val}")

    dist = status_distribution(data)
    print("\n🗂  Status Distribution:")
    for status, count in dist.items():
        bar = "█" * count
        print(f"  {status:<6}: {bar} ({count})")

    print("=" * 55)


if __name__ == "__main__":
    run_quality_checks(RAW_DATA)
    run_analysis(RAW_DATA)
