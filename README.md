# Parte 2 - Q2 - OpenAI

## Descricao
API de traducao do ingles para o frances com LangChain e OpenAI.

## Requisitos
Python 3.14 e dependencias listadas em requirements.txt.

## Instalacao
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

## Execucao
    python -m uvicorn main:app --reload --port 8003

## Documentacao da API
http://127.0.0.1:8003/docs

## Endpoint
POST /translate

## Exemplo de requisicao
    {"text":"Hello, how are you today?"}

## Observacoes
Integracao preparada, mas sem teste real. As chamadas pagas estao desativadas por padrao, retornando HTTP 503. Exige chave e creditos da API para utilizacao real.
