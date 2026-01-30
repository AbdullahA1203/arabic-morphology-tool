from .morphology import *
from .exporter import *
import typer

app = typer.Typer()

@app.command()
def generate(
     root: str = typer.Argument(
        None,
        help="Arabic root letters"
    ),
    interactive: bool = typer.Option(
        False,
        help="Run in interactive mode"
    ),
    card_type: str = typer.Option(False, "--type", "-t"),
):
    """ Command to generate flashcards """

    if interactive:
        run_interactive()
        return

    if not root:
        raise typer.BadParameter("Root is required unless --interactive is used.")
    
    
    card = None

    if card_type == "noun":
        card = generate_noun_card(root)
    
    elif card_type == "verb":
        card = generate_verb_card(root)
    

    print(card)





def run_interactive():
    """ Interactive mode """

    cards = []
    
    print("--- Arabic Morphology Tool ---")

    while(True):

        letters = typer.prompt("Enter the root letters (w to write to file): ")

        if (letters.lower() == "exit"):
            break

        else:
            forms = generate_verb_card(letters)

            cards.append(forms)

            print(forms)

    write_to_sheet(cards)

@app.command()
def exit():
    """ Exit the application """

    raise typer.Exit()