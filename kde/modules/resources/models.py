from pydantic import BaseModel


class TextEnricherPayload(BaseModel):
    input_text: str
