import os
import time
from playwright.sync_api import sync_playwright

def candidatar_vaga(url: str, caminho_pdf: str,headless: bool = False) ->bool:
    """
    Navega até a página da vaga, localiza o campo de upload do PDF do currículo
    e tenta realizar a anexação do arquivo.
    
    :param url: URL do formulário/página da vaga.
    :param caminho_pdf: Caminho absoluto ou relativo do PDF gerado.
    :param headless: Se True, executa o navegador em segundo plano sem janela visível.
    """

    abs_pdf_path = os.path.abspath(caminho_pdf)

    if not os.path.isfile(abs_pdf_path):
        print(f"Arquivo PDF não encontrado: {abs_pdf_path}")
        return False

    print(f"Navegando para a URL: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=500)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        try:
            print("Carregando a página...")
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(2000)

            file_input = page.query_selector('input[type="file"]')

            if file_input:
                print("Campo de upload encontrado. Anexando o arquivo PDF...")
                file_input.set_input_files(abs_pdf_path)
                print("Arquivo PDF anexado com sucesso.")
            else:
                print("Campo de upload não encontrado na página.")

            page.wait_for_timeout(5000)
            return True

        except Exception as e:
            print(f"Ocorreu um erro durante a navegação ou upload: {e}")
            return False

        finally:
            browser.close()
            print("Navegador fechado.")