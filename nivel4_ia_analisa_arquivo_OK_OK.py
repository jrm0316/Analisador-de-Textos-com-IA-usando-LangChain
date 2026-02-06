# -*- coding: utf-8 -*-

import os
print("Diretorio atual:", os.getcwd())

import sys
sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

with open("dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

prompt = PromptTemplate(
    input_variables=["texto"],
    template="""
Analise o texto abaixo e retorne:
- Resumo
- Principais pontos

Texto:
{texto}
"""
)

prompt_final = prompt.format(texto=conteudo)

resposta = llm.invoke(prompt_final)
print(resposta.content)