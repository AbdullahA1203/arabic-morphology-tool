from pydantic import BaseModel

class FlashCard(BaseModel):
    front: str
    back: str