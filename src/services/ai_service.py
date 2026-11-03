import os
import json
from google import genai
from google.genai import types
from google.genai.errors import ServerError, APIError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=api_key)

def carregar_cv_base(caminho_ficheiro: str = "cv_base.json") -> dict:
    with open(caminho_ficheiro, "r", encoding="utf-8") as f:
        return json.load(f)

@retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=4, max=30),
        retry=retry_if_exception_type((ServerError, APIError)),
        reraise=True
)

def otimizar_curriculo(desc_vaga: str, cv_base: dict) -> str:
    prompt = f"""Você é um especialista em recrutamento de TI e ATS.
    Dado o currículo base em JSON abaixo e a descrição da vaga fornecida:
    
    CURRÍCULO BASE:
    {json.dumps(cv_base, ensure_ascii=False, indent=2)}
    
    DESCRIÇÃO DA VAGA:
    {desc_vaga}
    
    Reescreva o currículo adaptando as experiências, projetos e resumo profissional para destacar 
    as palavras-chave da vaga, mantendo o formato JSON com a mesma estrutura do currículo base."""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json")
    )

    return response.text

if __name__ == "__main__":
    cv = carregar_cv_base()
    vaga_teste = "Desenvolvedor Front-end com experiência em React e TypeScript."
    curriculo_otimizado = otimizar_curriculo(vaga_teste, cv)
    print("Currículo otimizado:")
    print(curriculo_otimizado)