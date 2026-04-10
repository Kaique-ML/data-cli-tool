# 🖥️ Data CLI Tool — Typer + Rich
> Ferramenta de linha de comando para análise e transformação de dados, com saída bonita no terminal

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![Typer](https://img.shields.io/badge/Typer-0.12-000000)](https://typer.tiangolo.com)
[![Rich](https://img.shields.io/badge/Rich-13.7-1d4d4f)](https://rich.readthedocs.io)
[![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen)](https://coverage.readthedocs.io)
[![PyPI](https://img.shields.io/badge/PyPI-instalável-blue?logo=pypi)](https://pypi.org)

## 🎯 Sobre

CLI profissional para **análise rápida de dados** no terminal. Substitui abrir Jupyter apenas para ver um CSV, calcular estatísticas ou transformar um arquivo.

```bash
# Instalar
pip install data-cli-kaique

# Usar
data-cli analyze vendas.csv --top 10
data-cli plot vendas.csv --col receita --type bar
data-cli transform input.csv --filter "receita>1000" --output filtrado.csv
data-cli sql "SELECT produto, SUM(valor) FROM data GROUP BY produto" --file vendas.csv
```

## 🛠️ Stack

| Componente | Tech |
|-----------|------|
| CLI Framework | Typer 0.12 |
| Terminal UI | Rich 13.7 |
| Data Processing | Pandas + Polars |
| SQL em CSV | DuckDB |
| Empacotamento | setuptools + PyPI |

## 🧪 Testes

```bash
pytest tests/ --cov=data_cli --cov-report=term-missing
# Coverage: 93%
```

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
