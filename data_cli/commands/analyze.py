"""Comando analyze: estatísticas descritivas."""
import typer
import pandas as pd
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


@app.callback(invoke_without_command=True)
def analyze(
    file: str = typer.Argument(..., help="Arquivo CSV/Excel/JSON"),
    cols: str = typer.Option(None, help="Colunas separadas por vírgula"),
    top: int = typer.Option(10, help="Número de linhas a mostrar"),
):
    """Mostra estatísticas descritivas do arquivo."""
    df = _load(file)
    if cols:
        df = df[[c.strip() for c in cols.split(",")]]

    console.print(f"[bold green]📊 Arquivo:[/] {file}  |  [bold]{len(df):,}[/] linhas × [bold]{len(df.columns)}[/] colunas")

    table = Table(title="Primeiras linhas", show_header=True, header_style="bold cyan")
    for col in df.columns:
        table.add_column(col, style="white")
    for _, row in df.head(top).iterrows():
        table.add_row(*[str(v) for v in row])
    console.print(table)

    console.print("[bold]Estatísticas Numéricas:[/]")
    console.print(df.describe().to_string())


def _load(path: str) -> pd.DataFrame:
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith((".xls", ".xlsx")):
        return pd.read_excel(path)
    elif path.endswith(".json"):
        return pd.read_json(path)
    elif path.endswith(".parquet"):
        return pd.read_parquet(path)
    raise typer.BadParameter(f"Formato não suportado: {path}")
