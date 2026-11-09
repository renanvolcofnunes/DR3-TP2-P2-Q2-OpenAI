from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def translate_text(text):
    modelo = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_messages([("system", "Traduza o texto do inglês para o francês. Retorne apenas a tradução."), ("human", "{text}")])
    chain = prompt | modelo
    resposta = chain.invoke({"text": text})

    return resposta.content

