from rich.prompt import Confirm

from ..models.movie import Movie


def reset(session, console):

    # Prompts the user to ask for confirmation on whether to reset.
    toReset = Confirm.ask("\n[red]Are you sure you want to reset the database? [/red]")

    if toReset:
        # Resets the database by deleting all movies.
        session.query(Movie).delete()
        session.commit()

        console.print("\n[bright_yellow]Database has been successfully reset. [/bright_yellow]\n")
