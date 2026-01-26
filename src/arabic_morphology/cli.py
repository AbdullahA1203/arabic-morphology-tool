from .morphology import *

cards = []

def main():

    
    print("--- Arabic Morphology Tool ---")

    while(True):

        letters = input("Enter the root letters: ")

        forms = generate_card(letters)

        cards.append(forms)

        print(forms)


        pass