from pydantic import BaseModel
from openai import OpenAI

OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPEN_AI_KEY)

class FlashCard(BaseModel):
    front: str
    back: str



