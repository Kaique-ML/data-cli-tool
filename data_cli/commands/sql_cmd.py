"""Comando sql: executa SQL diretamente em arquivos CSV/JSON/Parquet."""
import typer
import duckdb
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


@app.callback(invoke_without_command=True)
def sql(
    query: str = typer.Argument(..., help="Query SQL (use 'data' como nome da tabela)"),
    file: str = typer.Option(..., "--file", "-f", help="Arquivo de entrada"),
):
    """Executa SQL diretamente em arquivos CSV/JSON/Parquet."""
    conn = duckdb.connect()
    conn.execute(f"CREATE VIEW data AS SELECT * FROM read_auto('{file}')")
    result = conn.execute(query).df()

    table = Table(show_header=True, header_style="bold cyan")
    for col in result.columns:
        table.add_column(col)
    for _, row in result.iterrows():
        table.add_row(*[str(v) for v in row])
    console.print(table)
    console.print(f"
[dim]{len(result)} registros[/]")
