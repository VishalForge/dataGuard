from src.checks import check_constant_columns
import pandas as pd


df = pd.DataFrame({
    "age": [25, 25, 25],
    "salary": [1, 2000, 3000],
    "gender": ["Male", "Male", "Male"]
})

print(check_constant_columns(df))