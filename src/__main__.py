import typer, pandas as pd
from src.validator import validate
from src.report import print_report

app = typer.Typer()

@app.command()
def analyze(
    data: str,
    target_col: str = typer.Option(None, "--target")
):
    df = pd.read_csv(data)
    results = validate(df, target_col=target_col)
    print_report(results)

if __name__ == "__main__":
    app()