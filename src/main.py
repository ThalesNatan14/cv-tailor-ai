import os
import json
import argparse
from src.services.scraper import extrair_texto_vaga
from src.services.ai_service import otimizar_curriculo, carregar_cv_base
from src.services.pdf_service import gerar_pdf_curriculo

def processar_vaga(url: str, nome_arquivo_pdf: str):
    """
    Orquestra o pipeline completo:
    1. Scraping da vaga (Jina Reader)
    2. Otimização do CV via IA (Gemini 3.8 Flash)
    3. Geração do arquivo PDF formatado (ReportLab)
    """
    print(f". Extraindo texto da vaga: {url}")
    texto_vaga =extrair_texto_vaga(url)

    if not texto_vaga:
        print("Não foi possível extrair o texto da vaga.")
        return

    print("2. Carregando currículo base")
    cv_base = carregar_cv_base()

    print("3. Otimizando currículo com base na descrição da vaga")
    curriculo_otimizado_json = otimizar_curriculo(texto_vaga, cv_base)

    dados_cv = json.loads(curriculo_otimizado_json)

    print("4. Gerando PDF do currículo otimizado")
    gerar_pdf_curriculo(dados_cv, nome_arquivo_pdf)

    print("\n--- PROCESSO CONCLUÍDO COM SUCESSO! ---")
    print(f"PDF gerado: {nome_arquivo_pdf}\n")


def main():
    parser = argparse.ArgumentParser(
        description="CV Tailor AI: Otimize seu currículo em PDF para vagas específicas usando IA."
    )
    
    # Argumento obrigatório: URL da vaga
    parser.add_argument(
        "url",
        type=str,
        help="URL da página de descrição da vaga."
    )
    
    # Argumento opcional: Nome do arquivo de saída em PDF
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="curriculo_otimizado.pdf",
        help="Caminho/nome do arquivo PDF de saída (Padrão: curriculo_otimizado.pdf)."
    )

    args = parser.parse_args()
    processar_vaga(args.url, args.output)

if __name__ == "__main__":
    main()