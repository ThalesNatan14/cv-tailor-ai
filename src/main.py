import os
import json
from services.scraper import extrair_texto_vaga
from services.ai_service import otimizar_curriculo, carregar_cv_base
from services.pdf_service import gerar_pdf_curriculo

def processar_vaga(url: str):
    print(f". Extraindo texto da vaga: {url}")
    texto_vaga =extrair_texto_vaga(url)

    if not texto_vaga:
        print("Não foi possível extrair o texto da vaga.")
        return

    print("2. Carregando currículo base")
    cv_base = carregar_cv_base()

    print("3. Otimizando currículo com base na descrição da vaga")
    curriculo_otimizado = otimizar_curriculo(texto_vaga, cv_base)

    print("\n--- CURRÍCULO OTIMIZADO ---")
    print(curriculo_otimizado)

    print("4. Gerando PDF do currículo otimizado")
    gerar_pdf_curriculo(json.loads(curriculo_otimizado))

    return curriculo_otimizado

if __name__ == "__main__":
    url_teste = "https://www.python.org/jobs/"
    processar_vaga(url_teste)