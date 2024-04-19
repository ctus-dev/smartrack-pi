"""This module provides the Smartrack CLI."""

# smartrack/cli/cli.py

from typing import Optional

import typer

import smartrack_pi.cli.display as display
import smartrack_pi.cli.net as net
from smartrack_pi import __app_name__, __version__

app = typer.Typer()
app.add_typer(display.app, name="display")
app.add_typer(net.app, name="net")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return