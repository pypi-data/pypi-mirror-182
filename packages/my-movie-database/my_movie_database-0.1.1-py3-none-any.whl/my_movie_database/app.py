from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rich.console import Console
from rich.prompt import Prompt
from rich.prompt import Confirm
import os

from .models.movie import Base
from .operations.add import add
from .operations.delete import delete
from .operations.reset import reset
from .operations.list import list_movies


def main(verbose=False):

    # Build the path of the directory in which to create the database file.
    db_dir_path = os.path.expanduser("~") + "/.my-movie-database"

    # If that directory does not exist, creates it.
    if not os.path.isdir(db_dir_path):
        os.makedirs(db_dir_path)

    # Constructs the path of the database file.
    db_path = db_dir_path + "/movie_db.db"

    # Creates engine
    engine = create_engine("sqlite:///" + db_path, echo=verbose)

    # Creates the table if it does not exist.
    Base.metadata.create_all(bind=engine)

    # Creates a Session class.
    Session = sessionmaker(bind=engine)

    # Creates a Session object.
    session = Session()

    # Creates a Console object.
    console = Console()

    console.print()

    # Loops until the user chooses 'EXIT' as the option.
    while True:

        choices = ["ADD", "DELETE", "LIST", "RESET", "EXIT", "add", "delete", "list", "reset", "exit"]

        # Prompts the user for the operation.
        op = Prompt.ask("[bright_yellow]Enter the operation you wish to perform " +
                        "[/bright_yellow][purple](ADD/DELETE/LIST/EXIT/RESET)[/purple]\n",
                        choices=choices, show_choices=False)

        # Executes the proper operation.
        if op.upper() == "ADD":
            add(session, console)
        elif op.upper() == "DELETE":
            delete(session, console)
        elif op.upper() == "LIST":
            list_movies(session, console)
        elif op.upper() == "RESET":
            reset(session, console)
        elif op.upper() == "EXIT":
            toExit = Confirm.ask("\n[red]Are you sure you want to exit my-movie-database? [/red]")

            if toExit:
                console.print("\n[bright_yellow]Exiting my-movie-database.[/bright_yellow]\n")
                break
            else:
                console.print()

        else:
            console.print("Invalid operation.")
    return


if __name__ == "__main__":
    main()
