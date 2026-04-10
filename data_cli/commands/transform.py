"""Comando transform: filtra, seleciona e ordena dados."""
import typer
import pandas as pd
from rich.console import Console

app = typer.Typer()
console = Console()


@app.callback(invoke_without_command=True)
def transform(
    file: str = typer.Argument(...),
    filter_expr: str = typer.Option(None, "--filter"),
    select: str = typer.Option(None, "--select"),
    output: str = typer.Option("output.csv", "--output"),
):
    """Filtra e seleciona colunas de um arquivo."""
    df = pd.read_csv(file)
    if filter_expr:
        df = df.query(filter_expr)
    if select:
        df = df[[c.strip() for c in select.split(",")]]
    df.to_csv(output, index=False)
    console.print(f"[green]✅ {len(df)} registros salvos em {output}[/]")
