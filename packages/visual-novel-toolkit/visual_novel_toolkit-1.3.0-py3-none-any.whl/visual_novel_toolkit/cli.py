# mypy: disable-error-code = misc
from typer import Exit
from typer import Typer

from .find_missed_drafts import find_missed_drafts
from .find_unused_words import find_unused_words
from .make_draft import make_draft
from .sort_words import sort_words


cli = Typer()


@cli.command()
def sort() -> None:
    if sort_words():
        raise Exit(code=1)


@cli.command()
def unused() -> None:
    if find_unused_words():
        raise Exit(code=1)


@cli.command()
def draft() -> None:
    make_draft()


@cli.command()
def missed() -> None:
    if find_missed_drafts():
        raise Exit(code=1)
