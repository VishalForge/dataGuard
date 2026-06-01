from src.checks import check_constant_columns
from src.checks import check_class_imbalance
import pandas as pd


df = pd.DataFrame({
    "age": [25, 25, 25],
    "salary": [1, 2000, 3000],
    "gender": ["Male", "Male", "Male"]
})

print(check_constant_columns(df))


df2 = pd.DataFrame({
    "age": [25, 24, 30, 28, 29, 27, 33, 45],
    "salary": [50000, 55000, 60000, 65000, 70000, 62000, 63000, 80000],
    "target": [0, 0, 0, 0, 0, 0, 0, 1]
})

print(check_class_imbalance(df2, "target"))