from dotenv import load_dotenv

load_dotenv()

from .cli import app

def main():
    app()

if __name__ == "__main__":
    main()
