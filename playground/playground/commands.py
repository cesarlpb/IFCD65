import click

@click.command()
def test() -> None:
    """Simple CLI to test receiving arguments and options."""
    click.echo("Esto es un test 🤔")
