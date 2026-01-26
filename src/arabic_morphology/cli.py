from .morphology import *

def main():

    
    print("--- Arabic Morphology Tool ---")

    while(True):

        letters = input("Enter the root letters: ")

        forms = generate_card(letters)

        print(forms)

        pass