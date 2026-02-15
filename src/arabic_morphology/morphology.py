from pydantic import BaseModel
from openai import OpenAI
import os


class FlashCard(BaseModel):
    """ Represents a single flashcard generated from Arabic root letters """

    front: str
    back: str

OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPEN_AI_KEY)

verb_content_prompt = """
    Create ONE verb flashcard for the given Arabic verb.
    Return JSON with keys: front, back.
    front: 1–2 common English meanings.
    back: list forms exactly like: past / present / imperative / verbal-noun (omit any missing).
    Then a new line: الجذر: <letters separated by spaces>
    Example back format: ذَهَبَ / يَذْهَبُ / اِذْهَبْ / ذَهَاب
"""

noun_content_prompt = """
    Create ONE noun flashcard for the given Arabic noun.
    Return JSON with keys: front, back.
    front: 1–2 common English meanings.
    back: list forms exactly like: plural / singular (omit any missing).
    Then a new line: الجذر: <letters separated by spaces>
    Example back format: موضوع / مواضيع
    """

def generate_verb_card(root_letters):
    """ Calls OpenAI API, sending the root letters and returning the flashcard for the verb """

    response = client.responses.parse(
        model="gpt-5",
        input=[
            {"role": "system", "content": verb_content_prompt},
            {
                "role": "user",
    
                "content": root_letters,
            },
        ],
        text_format=FlashCard,
    )

    # Returning the structured object
    return response.output_parsed


def generate_noun_card(root_letters):
    """ Calls OpenAI API, sending the root letters and returning the flashcard for the noun """

    response = client.responses.parse(
        model="gpt-5",
        input=[
            {"role": "system", "content": noun_content_prompt},
            {
                "role": "user",
    
                "content": root_letters,
            },
        ],
        text_format=FlashCard,
    )

    # Returning the structured object
    return response.output_parsed