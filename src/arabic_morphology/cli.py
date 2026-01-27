from .morphology import *
from .exporter import *


def main():
    """ Entry point for the command-line interface """

    cards = []
    
    print("--- Arabic Morphology Tool ---")

    while(True):

        letters = input("Enter the root letters (w to write to file): ")

        if (letters == "w"):
            break

        else:
            forms = generate_card(letters)

            cards.append(forms)

            print(forms)

    write_to_sheet(cards)
