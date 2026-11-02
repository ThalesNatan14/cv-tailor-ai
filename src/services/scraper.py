import requests
from bs4 import BeautifulSoup

def extrair_texto_vaga(url: str) -> str:
    """
    Utiliza o Jina AI Reader (https://r.jina.ai/) para converter a URL de uma vaga
    diretamente em texto Markdown limpo e otimizado para a IA.
    """
    jina_url=f"https://r.jina.ai/{url}"
    headers = {
        "Users-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
    }

    try:
        print(f"Buscando vaga via Jina Reader: {url}...")
        response = requests.get(jina_url, headers=headers, timeout=15)
        response.raise_for_status()
        
        texto_limpo = response.text
        return texto_limpo
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao extrair conteúdo da vaga via Jina: {e}")
        return ""

if __name__ == "__main__":
    url_teste = "https://www.python.org/jobs/"
    texto = extrair_texto_vaga(url_teste)
    print("\n--- PRIMEIROS 1000 CARACTERES EXTRAÍDOS VIA JINA ---")
    print(texto[:1000])