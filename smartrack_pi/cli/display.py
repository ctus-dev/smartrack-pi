from typing import Annotated

import typer

from smartrack_pi.display import display_text, stats_status

app = typer.Typer()


@app.command()
def stats(
    enable: Annotated[bool, typer.Option(help="Turns Stats Loop on or off")] = True
):
    print(f"Setting stats display to {enable}")
    stats_status(enable)


@app.command()
def message(text: Annotated[str, typer.Argument(help="Message to display")]):
    print(f"Displaying Message: {text}")
    print("Warning:  Stats will be disabled, to re-enable 'smartrack display stats'")
    display_text(text)


if __name__ == "__main__":
    app()
