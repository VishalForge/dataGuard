import pandas as pd

def check_missing_values(df: pd.DataFrame) -> dict:
    null_percentages = (df.isnull().sum()) / len(df) * 100
    columns_with_nulls = null_percentages[null_percentages > 0].to_dict()
    max_null = max(columns_with_nulls.values())
    if not columns_with_nulls:
        severity = "INFO"
    elif max_null >= 20:
        severity = "CRITICAL"
    else:
        severity = "WARNING"
    
    return {
        "check": "missing_values",
        "severity": severity,
        "details": columns_with_nulls
    }

