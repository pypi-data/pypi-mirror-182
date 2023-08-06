from rich.prompt import Prompt
from rich.prompt import IntPrompt

from ..models.movie import Movie


def add(session, console):

    console.print("\n[bright_yellow]Enter the details of the movie to add.[/bright_yellow]\n")

    rating_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    # Prompts and obtains the details of the movie.
    title = Prompt.ask("[turquoise2]Title \t\t[/turquoise2]")
    year = IntPrompt.ask("[turquoise2]Year \t\t[/turquoise2]")
    director = Prompt.ask("[turquoise2]Director \t[/turquoise2]")
    rating = IntPrompt.ask("[turquoise2]Rating (1 - 10) [/turquoise2]", choices=rating_choices, show_choices=False)

    movie = Movie(title, year, director, rating)

    # Adds the movie.
    session.add(movie)
    session.commit()

    console.print("\n[bright_yellow]Movie has been successfully added.[/bright_yellow]\n")

    return
