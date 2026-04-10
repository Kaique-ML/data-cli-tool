"""Data CLI Tool — CLI profissional para análise de dados."""
import typer
from data_cli.commands import analyze, transform, sql_cmd, convert

app = typer.Typer(name="data-cli", help="🖥️ Análise e transformação de dados no terminal")
app.add_typer(analyze.app, name="analyze")
app.add_typer(transform.app, name="transform")
app.add_typer(sql_cmd.app, name="sql")
app.add_typer(convert.app, name="convert")

if __name__ == "__main__":
    app()
