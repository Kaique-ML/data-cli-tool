"""Comando convert: converte entre formatos de arquivo."""
import typer
import pandas as pd
from rich.console import Console

app = typer.Typer()
console = Console()


@app.callback(invoke_without_command=True)
def convert(
    file: str = typer.Argument(...),
    to: str = typer.Option(..., help="Formato: json, parquet, csv"),
    output: str = typer.Option(None, "--output"),
):
    """Converte arquivos entre formatos (CSV, JSON, Parquet, Excel)."""
    df = pd.read_csv(file) if file.endswith(".csv") else pd.read_excel(file)
    out = output or file.rsplit(".", 1)[0] + f".{to}"
    {"json": df.to_json, "parquet": df.to_parquet, "csv": df.to_csv}[to](out, index=False)
    console.print(f"[green]✅ Convertido → {out}[/]")
