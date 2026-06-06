import typer, pandas as pd
from src.validator import validate
from src.report import print_report

app = typer.Typer()

@app.command()
def analyze(
    data: str,
    target_col: str = typer.Option(None, "--target"),
    report: str = typer.Option("terminal", "--report")
):
    df = pd.read_csv(data)
    results = validate(df, target_col=target_col)
    if report == "html":
        from .report import generate_html_report
        generate_html_report(results)
        typer.echo("Report saved to report.html")
    else:
        print_report(results)

if __name__ == "__main__":
    app()