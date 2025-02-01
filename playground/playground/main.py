import click
from playground import commands

VERSION = "0.1.0"  # Define la versión de tu aplicación

@click.group()
@click.version_option(version=VERSION, prog_name="playground")
def cli() -> None:
    """CLI principal de Playground."""
    pass  # El grupo CLI no necesita hacer nada al ejecutarse solo

# Añade el comando "test" desde commands.py
cli.add_command(commands.test)