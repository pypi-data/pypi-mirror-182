"""Console script for gwapandas."""

import typer

app = typer.Typer()

def main():
    """Main entrypoint."""
    typer.echo("gwapandas")
    typer.echo("=" * len("gwapandas"))
    typer.echo("Python tools for GWAS summary statistics")


if __name__ == "__main__":
   app(main)