import click

@click.command()
@click.argument("title")
# @click.option("--version", type=int, default=VERSION, help="Version number")
def test(title: str) -> None:
    """Simple CLI to test receiving arguments and options."""
    click.echo(f"Title: {title}")

if __name__ == "__main__":
    test()
