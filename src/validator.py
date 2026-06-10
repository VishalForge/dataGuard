from src.checks import check_missing_values, check_duplicates, check_constant_columns, check_class_imbalance, check_high_cardinality
import pandas as pd
import logging
logger = logging.getLogger(__name__)

def validate(df: pd.DataFrame, target_col: str = None) -> list:
    """
    Run all  Dataguard checks on the provided DataFrame.
    
    Args:
    df: the dataset to validate
    target_col: optional name of the target column.
                Required for class imbalance check.
    
    Returns:
    list of result dicts, one per check
    """
    logger.info(f"Starting validation on dataset with {len(df)} rows and {len(df.columns)} columns")
    results = []
    logger.info("Running missing values check")
    results.append(check_missing_values(df))
    logger.info("Running duplicates check")
    results.append(check_duplicates(df))
    logger.info("Running constant columns check")
    results.append(check_constant_columns(df))
    if target_col is not None:
        logger.info(f"Running class imbalance check on column: {target_col}")
        results.append(check_class_imbalance(df, target_col))
    logger.info("Running high cardinality check")
    results.append(check_high_cardinality(df))
    logger.info("Validation complete")

    return results
