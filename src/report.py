from rich.console import Console

console = Console()

def print_report(results: list) -> None:
    """
    Print validation results to the terminal with color coding.
    CRITICAL in red, WARNING in yellow, INFO in green.
    
    Args:
    results: list of check result dicts from validate()
    """
    console.print("\n===DataGuard Report===\n")

    for result in results:
        check = result["check"]
        severity = result["severity"]
        details = result["details"]

        if severity == "CRITICAL":
            console.print(f"[red]{severity}: {check} | {details}[/red]")
        elif severity == "WARNING":
            console.print(f"[yellow]{severity}: {check} | {details}[/yellow]")
        else:
            console.print(f"[green]{severity}: {check} | {details}[/green]")


def generate_html_report(results: list) -> None:
    """
    Generate a styled HTML report from validation results.
    Saves the report as report.html in the current directory.
    
    Args:
    results: list of check result dicts from validate()
    """
    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader("src/templates"))
    template = env.get_template("report_template.html")

    html_output = template.render(results=results)

    with open("report.html", "w") as f:
        f.write(html_output)
        