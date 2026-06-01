from src.checks import check_missing_values, check_duplicates, check_constant_columns, check_class_imbalance, check_high_cardinality
import pandas as pd

def validate(df: pd.DataFrame, target_col: str = None) -> list:
    results = []
    results.append(check_missing_values(df))
    results.append(check_duplicates(df))
    results.append(check_constant_columns(df))
    if target_col is not None:
        results.append(check_class_imbalance(df, target_col))
    results.append(check_high_cardinality(df))

    return results
