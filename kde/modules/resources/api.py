from fastapi import FastAPI

from kde.modules.resources.models import TextEnricherPayload
from kde.services.enricher.text_enricher import TextEnricher

app = FastAPI(title="API",
              swagger_ui_parameters={"defaultModelsExpandDepth": -1})
text_enricher = TextEnricher()


@app.get("/")
async def root():
    return {"message": "Welcome to Kde API"}


@app.post("/enricher/emails")
def extract_email(body: TextEnricherPayload):
    result = text_enricher.extract_email(body.input_text)
    return result


@app.post("/enricher/languages")
def detect_language(body: TextEnricherPayload):
    result = text_enricher.detect_language(body.input_text)
    return result
