import pytest
import pandas as pd
from src.checks import (
    check_missing_values,
    check_duplicates,
    check_constant_columns,
    check_class_imbalance,
    check_high_cardinality
)

@pytest.fixture
def dirty_df():
    return pd.DataFrame({
    "name": ["Joe", "Raven", "Harry", "Kevin", "Samira", "Joe"],
    "age": [21, 22, 23, 24, 25, 21],
    "user_id": [1, 2, 3, 4, 5, 1],
    "transaction_id": [1001, 1002, 1003, 1004, 1005, 1001],
    "salary": [50000, None, None, 40000, None, 50000],
    "department": ["HR", "HR", "HR", "HR", "HR", "HR"],
    "gender": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "target": [1, 1, 1, 1, 0, 1]
    })

@pytest.fixture
def clean_df():
    return pd.DataFrame({
    "name": ["Joe", "Raven", "Harry", "Kevin", "Samira"],
    "age": [21, 22, 23, 24, 25],
    "salary": [50000, 70000, 83000, 40000, 90000],
    "department": ["HR", "IT", "HR", "IT", "HR"],
    "gender": ["Male", "Female", "Male", "Male", "Female"],
    "target": [1, 0, 1, 0, 1]
    })


def test_missing_values_critical(dirty_df):
    result = check_missing_values(dirty_df)
    assert result["severity"] == "CRITICAL"
    assert result["check"] == "missing_values"

def test_missing_values_clean(clean_df):
    result = check_missing_values(clean_df)
    assert result["severity"] == "INFO"

def test_duplicates_warning(dirty_df):
    result = check_duplicates(dirty_df)
    assert result["severity"] == "WARNING"
    assert result["check"] == "duplicates"

def test_duplicates_clean(clean_df):
    result = check_duplicates(clean_df)
    assert result["severity"] == "INFO"

def test_constant_columns_warning(dirty_df):
    result = check_constant_columns(dirty_df)
    assert result["severity"] == "WARNING"
    assert result["check"] == "constant_columns"

def test_constant_columns_clean(clean_df):
    result = check_constant_columns(clean_df)
    assert result["severity"] == "INFO"

def test_class_imbalance_warning(dirty_df):
    result = check_class_imbalance(dirty_df, "target")
    assert result["severity"] == "WARNING"
    assert result["check"] == "class_imbalance"

def test_class_imbalance_clean(clean_df):
    result = check_class_imbalance(clean_df, "target")
    assert result["severity"] == "INFO"
    
def high_cardinality_critical(dirty_df):
    result = check_high_cardinality(dirty_df)
    assert result["severity"] == "CRITICAL"
    assert result["check"] == "cardinality"

def high_cardinality_clean(clean_df):
    result = check_high_cardinality(clean_df)
    assert result["severity"] == "INFO"
