# dataGuard
Intelligent dataset validator that automatically detects silent data issues before they corrupt ML model training.

## The Problem

ML models fail silently when trained on bad data. A model trained on a dataset with 30% missing values, duplicate rows, or severe class imbalance will produce confident but wrong predictions - and you won't know until it's in production.

DataGuard catches these issues before training starts.

## Checks it runs

| Check | What it detects | Severity levels |
|-------|-----------------|-----------------|
| missing_values | Columns with null values | CRITICAL / WARNING / INFO |
| duplicates | Identical rows in dataset | CRITICAL / WARNING / INFO |
constant_columns | Columns where every value is identical | CRITICAL / WARNING / INFO |
| class_imbalance | Skewed target column distribution | CRITICAL / WARNING / INFO |
| high_cardinality | Columns with too many unique values | CRITICAL / WARNING / INFO |


## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/VishalForge/dataGuard.git
cd dataGuard
pip install pandas typer rich jinja2
```

## Usage

### Basic validation:
```bash
python -m src your_dataset.csv
```

### With target column (enables class imbalance check):
```bash
python -m src your_dataset.csv --target target
```

### Generate HTML report:
```bash
python -m src your_dataset.csv --report html
```

## Project Structure

dataGuard/
  src/
    checks.py     - 5 check functions, one per data quality issue
    validator.py  - orchestrates all checks, results combined results
    report.py     - terminal output (colored) and HTML report generation
    __main__.py   - CLI entry point, accepts CSV file and options
    templates/
      report_template.html - Jinja2 template for HTML report
  tests/
    test_checks.py - pytest tests for all 5 functions



## Tech Stack

- **Python** - core language
- **Pandas** - data loading and analysis
- **Typer** - CLI interface
- **Jinja2** - HTML report generation
- **pytest** - automated testing

