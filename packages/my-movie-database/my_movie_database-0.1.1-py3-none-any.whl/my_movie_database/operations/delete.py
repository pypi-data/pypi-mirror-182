from sqlalchemy.exc import NoResultFound
from rich.prompt import IntPrompt

from ..models.movie import Movie


def delete(session, console):

    # Prompts the user for the id of the movie to be deleted.
    id_del = IntPrompt.ask("\n[red]Enter the id of the movie you wish to delete[red]")

    try:
        movie_del = session.query(Movie).filter(Movie.id == id_del).one()
    except NoResultFound:
        console.print("\n[bright_yellow]No movie with the given id was found. [bright_yellow]\n")
        return

    # Deletes the movie.
    session.delete(movie_del)
    session.commit()

    title_del = getattr(movie_del, "title")

    console.print(f"\n[bright_yellow]Movie '{title_del}' has been successfully deleted.[/bright_yellow]\n")

    return
