from rich.table import Table

from ..models.movie import Movie


def list_movies(session, console):

    results = session.query(Movie)

    print()

    # Creates table structure.
    table = Table(show_header=True, header_style="bold bright_magenta")
    table.add_column("Id")
    table.add_column("Title")
    table.add_column("Year")
    table.add_column("Director")
    table.add_column("Rating", justify="center", width=20)

    # Adds results to the table.
    for result in results:

        rating = (getattr(result, "rating") * ":star:")

        row = [
            str(getattr(result, "id")),
            getattr(result, "title"),
            str(getattr(result, "year")),
            getattr(result, "director"),
            rating
        ]

        table.add_row(*row)

    console.print(table)

    print()
