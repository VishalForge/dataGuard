# from src.checks import check_constant_columns
# from src.checks import check_class_imbalance
# from src.checks import check_high_cardinality
import pandas as pd


df = pd.DataFrame({
    "age": [25, 25, 25],
    "salary": [1, 2000, 3000],
    "gender": ["Male", "Male", "Male"]
})

# print(check_constant_columns(df))


df2 = pd.DataFrame({
    "age": [25, 24, 30, 28, 29, 27, 33, 45, 65, 70],
    "salary": [50000, 55000, 60000, 65000, 70000, 62000, 63000, 80000, 10, 20],
    "target": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
})

# print(check_class_imbalance(df2, "target"))


df3 = pd.DataFrame({
    "age": [23, 20, 24, 26, 27, 23, 20, 24, 26, 27],
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "department": ["HR", "IT", "HR", "IT", "HR", "IT", "HR", "IT", "HR", "IT"]
})

# print(check_high_cardinality(df3))

from src.validator import validate

results = validate(df2, target_col='target')
for result in results:
    print(result)
    

from src.report import print_report
print_report(results)