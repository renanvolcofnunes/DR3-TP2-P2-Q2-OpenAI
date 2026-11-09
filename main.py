import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from models import translate_text

app = FastAPI(title="TP2 - Parte 2 - Q2 - OpenAI", description="API de tradução utilizando LangChain e OpenAI.")

class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)

class TranslationResponse(BaseModel):
    text: str
    translated_text: str

@app.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    if os.getenv("EXECUTAR_API_OPENAI") != "SIM":
        raise HTTPException(status_code=503, detail="API OpenAI desativada para evitar custos.")

    resultado = translate_text(request.text)

    return TranslationResponse(text=request.text, translated_text=resultado)
