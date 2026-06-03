from rich.console import Console

console = Console()

def print_report(results: list) -> None:
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
        