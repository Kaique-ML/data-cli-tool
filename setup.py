from setuptools import setup, find_packages

setup(
    name="data-cli-kaique",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["typer", "rich", "pandas", "duckdb", "polars"],
    entry_points={"console_scripts": ["data-cli=data_cli.main:app"]},
    author="Gabriel Kaique Portel Silva",
    description="CLI profissional para análise e transformação de dados no terminal",
    python_requires=">=3.11",
)
