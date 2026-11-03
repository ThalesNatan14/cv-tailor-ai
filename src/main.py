import os
import json
import argparse
from src.services.scraper import extrair_texto_vaga
from src.services.ai_service import otimizar_curriculo, carregar_cv_base
from src.services.pdf_service import gerar_pdf_curriculo
from src.services.apply_service import candidatar_vaga

def processar_vaga(url: str, nome_arquivo_pdf: str, auto_apply: bool =False, headless: bool = False):
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
    print(f"PDF gerado: {nome_arquivo_pdf}\n")

    if auto_apply:
        print("5. Tentando candidatar-se à vaga automaticamente")
        sucesso = candidatar_vaga(url, nome_arquivo_pdf, headless=headless)
        if sucesso:
            print("Candidatura enviada com sucesso!")
        else:
            print("Falha ao enviar a candidatura.")

    print("Processo concluído.")

def main():
    parser = argparse.ArgumentParser(
        description="CV Tailor AI: Agente autônomo de otimização de currículo e candidatura."
    )
    
    parser.add_argument("url", type=str, help="URL da página de descrição/aplicação da vaga.")
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="curriculo_otimizado.pdf",
        help="Caminho/nome do arquivo PDF de saída (Padrão: curriculo_otimizado.pdf)."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Ativa o agente Playwright para abrir o navegador e realizar o upload do PDF no formulário."
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Executa o Playwright em modo invisível (sem abrir a janela do navegador)."
    )

    args = parser.parse_args()
    processar_vaga(args.url, args.output, auto_apply=args.apply, headless=args.headless)

if __name__ == "__main__":
    main()