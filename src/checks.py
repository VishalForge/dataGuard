import pandas as pd

def check_missing_values(df: pd.DataFrame) -> dict:
    """
    Check for missing values across all columns.
    
    Severity:
    CRITICAL: any column has more than 20% missing values
    WARNING: any column has between 1-20% missing values
    INFO: no missing values found
    
    Returns:
    dict with keys: check, severity, details
    """
    null_percentages = (df.isnull().sum()) / len(df) * 100
    columns_with_nulls = null_percentages[null_percentages > 0].to_dict()
    
    if not columns_with_nulls:
        severity = "INFO"
    else:
        max_null = max(columns_with_nulls.values())
        if max_null >= 20:
            severity = "CRITICAL"
        else:
            severity = "WARNING"
    
    return {
        "check": "missing_values",
        "severity": severity,
        "details": columns_with_nulls
    }


def check_duplicates(df: pd.DataFrame) -> dict:
    """
    Check for duplicate rows in the dataset.
    
    Severity:
    CRITICAL: 3 or more duplicate rows found
    WARNING: 1-2 duplicate rows found
    INFO: no duplicate found
    
    Returns:
    dict with keys: check, severity, details
    """
    duplicate_count = df.duplicated().sum()
    

    if duplicate_count == 0:
        severity = "INFO"
        details = {"message": "No duplicates found"}
    elif duplicate_count >= 3:
        severity = "CRITICAL"
        details = {"duplicate_count": int(duplicate_count)}
    else:
        severity = "WARNING"
        details = {"duplicate_count": int(duplicate_count)}
    
    return {
        "check": "duplicates",
        "severity": severity,
        "details": details
    }


def check_constant_columns(df: pd.DataFrame)-> dict:
    """
    Check for columns where every value is identical.
    Constant columns provide no useful signal to ML models.
    
    Severity:
    CRITICAL: 3 or more constant columns found
    WARNING: 1-2 constant columns found
    INFO: no constant columns found
    
    Returns:
    dict with keys: check, severity, details
    """
    constant_cols = df.columns[df.nunique() == 1].to_list()

    if len(constant_cols) == 0:
        severity = "INFO"
        details = {"message": "No constant columns found"}
    elif len(constant_cols) >= 3:
        severity = "CRITICAL"
        details = {"constant_columns": constant_cols}
    else:
        severity = "WARNING"
        details = {"constant_columns": constant_cols}
    
    return{
        "check": "constant_columns",
        "severity": severity,
        "details": details
    }


def check_class_imbalance(df: pd.DataFrame, target_col: str) -> dict:
    """
    Check if the target column has severe class imbalance.
    Imbalanced targets cause models to predict the majority
    class and appear accurate while being useless.
    
    Args:
    target_col: name of the target/label column
    
    Severity:
    CRITICAL: majority class is 90% or above
    WARNING: majority class is between 70-89%
    INFO: classes are reasonably balanced
    
    Returns:
    dict with keys: check, severity, details
    """
    if target_col not in df.columns:
        return {
            "check": "class_imbalance",
            "severity": "INFO",
            "details": {"message": f"column '{target_col}' not found"}
        }
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

 
def check_high_cardinality(df: pd.DataFrame) -> dict:
    """
    Check for columns with too many unique values relative to
    dataset size. High cardinality columns are often identifiers
    that leak no learnable pattern to models.
    
    Severity:
    CRITICAL: any column has 90% or more unique values
    WARNING: anu column has between 50-89% unique values
    INFO: all column has acceptable cardinality
    
    Returns:
    dict with keys: check, severity, details
    """
    cardinality_cols = df.columns[df.nunique() / len(df) > 0.5].tolist()
    cardinality_percentage = (df.nunique() / len(df)) * 100


    if not cardinality_cols:
        severity = "INFO"
    else:
        max_cardinality = cardinality_percentage.max()
        if max_cardinality >= 90:
            severity = "CRITICAL"
        elif max_cardinality >= 50:
            severity = "WARNING"
        else:
            severity = "INFO"
    
    return {
        "check": "cardinality",
        "severity": severity,
        "details": {
            "high_cardinality_cols": cardinality_cols,
            "cardinality_percentage": cardinality_percentage.round(2).to_dict()
        }
    }
