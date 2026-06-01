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


def check_duplicates(df: pd.DataFrame) -> dict:
    duplicate_count = df.duplicated().sum()
    

    if duplicate_count == 0:
        severity = "INFO"
    elif duplicate_count >= 3:
        severity = "CRITICAL"
    else:
        severity = "WARNING"
    
    return {
        "check": "duplicates",
        "severity": severity,
        "details": {"duplicate_count": int(duplicate_count)}
    }


def check_constant_columns(df: pd.DataFrame)-> dict:
    constant_cols = df.columns[df.nunique() == 1].to_list()

    if len(constant_cols) == 0:
        severity = "INFO"
    elif len(constant_cols) >= 3:
        severity = "CRITICAL"
    else:
        severity = "WARNING"
    
    return{
        "check": "constant_columns",
        "severity": severity,
        "details": {"constant_columns": constant_cols}
    }


def check_class_imbalance(df: pd.DataFrame, target_col: str) -> dict:
    imbalance_count = df[target_col].value_counts()
    imbalance_percentage = df[target_col].value_counts(normalize=True) * 100

    majority_percentage = imbalance_percentage.iloc[0]

    if majority_percentage >= 90:
        severity = "CRITICAL"
    elif majority_percentage >= 70:
        severity = "WARNING"
    else:
        severity = "INFO"
    
    return {
        "check": "class_imbalance",
        "severity": severity,
        "details": {
            "class_counts": imbalance_count.to_dict(),
            "class_percentage": imbalance_percentage.round(2).to_dict()
        }
    }

 