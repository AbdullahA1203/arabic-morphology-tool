from .morphology import *
from .exporter import *
import typer

app = typer.Typer()

@app.command()
def interactive():
    """ Interactive mode """

    cards = []
    
    print("--- Arabic Morphology Tool ---")

    while(True):

        letters = typer.prompt("Enter the root letters (w to write to file): ")

        if (letters.lower() == "exit"):
            break

        else:
            forms = generate_card(letters)

            cards.append(forms)

            print(forms)

    write_to_sheet(cards)

@app.command()
def exit():
    """ Exit the application """

    raise typer.Exit()