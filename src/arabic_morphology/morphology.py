from pydantic import BaseModel
from openai import OpenAI


class FlashCard(BaseModel):
    front: str
    back: str



