========================================================================
                            CV Tailor AI 🚀
========================================================================

O CV Tailor AI é uma ferramenta em Python alimentada por Inteligência 
Artificial (Google Gemini) que automatiza a personalização de currículos 
para vagas de emprego específicas.

A aplicação extrai a descrição da vaga a partir de uma URL, otimiza o 
currículo base em formato JSON para destacar as competências e projetos 
mais relevantes para a oportunidade, e gera um PDF formatado e totalmente 
compatível com sistemas ATS (Applicant Tracking System).

------------------------------------------------------------------------
1. 🛠️ TECNOLOGIAS UTILIZADAS
------------------------------------------------------------------------
- Python 3.12+
- Google Gemini API (gemini-3.8-flash) – Otimização inteligente do conteúdo
- Jina AI Reader – Scraping e conversão de páginas de vagas para Markdown limpo
- ReportLab – Geração programática de PDFs estilizados e compatíveis com ATS
- Tenacity – Mecanismo de resiliência com retentativas automáticas
- Argparse – Interface de linha de comando (CLI) para execução flexível

------------------------------------------------------------------------
2. 📁 ESTRUTURA DO PROJETO
------------------------------------------------------------------------
cv-tailor-ai/
├── .env.example
├── .gitignore
├── cv_base.json
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py
    ├── main.py
    └── services/
        ├── __init__.py
        ├── ai_service.py
        ├── pdf_service.py
        └── scraper.py

------------------------------------------------------------------------
3. ⚙️ INSTALAÇÃO E CONFIGURAÇÃO
------------------------------------------------------------------------

3.1. Clonar o repositório:
    git clone https://github.com/ThalesNatan14/cv-tailor-ai.git
    cd cv-tailor-ai

3.2. Criar e ativar o ambiente virtual:
    python3 -m venv .venv
    source .venv/bin/activate

3.3. Instalar as dependências:
    pip install -r requirements.txt

3.4. Configurar as variáveis de ambiente:
    cp .env.example .env

    Abra o ficheiro .env e adicione a sua chave da API do Gemini:
    GEMINI_API_KEY=sua_chave_aqui

------------------------------------------------------------------------
4. 🚀 COMO USAR (CLI)
------------------------------------------------------------------------

4.1. Visualizar menu de ajuda:
    python -m src.main --help

4.2. Execução Padrão (Gera curriculo_otimizado.pdf):
    python -m src.main https://www.python.org/jobs/

4.3. Definir nome personalizado para o PDF (-o / --output):
    python -m src.main https://www.python.org/jobs/ -o curriculo_python_developer.pdf

------------------------------------------------------------------------
5. 📄 ESTRUTURA DO CURRÍCULO BASE (cv_base.json)
------------------------------------------------------------------------
O arquivo cv_base.json armazena o histórico completo de dados pessoais, 
formação, habilidades e projetos. A IA utiliza essas informações como 
fonte da verdade para selecionar, enfatizar e reordenar as experiências 
de acordo com os requisitos da vaga informada:

{
  "dados_pessoais": {
    "nome": "Seu Nome Completo",
    "localizacao": "Sua Cidade, Estado",
    "email": "seu.email@exemplo.com",
    "linkedin": "https://linkedin.com/in/seu-perfil",
    "github": "https://github.com/seu-usuario"
  },
  "resumo_profissional": "Resumo geral das suas qualificações...",
  "formacao": [
    {
      "instituicao": "Nome da Instituição",
      "curso": "Nome do Curso",
      "status": "Em andamento / Concluído",
      "previsao_formatura": "MM/AAAA"
    }
  ],
  "habilidades": {
    "linguagens": ["Python", "C++", "TypeScript"],
    "banco_de_dados": ["SQL", "MySQL"],
    "frameworks_e_libs": ["NestJS", "React"],
    "ferramentas": ["Docker", "Git", "Linux"],
    "idiomas": [
      {
        "idioma": "Português",
        "nivel": "Nativo"
      },
      {
        "idioma": "Inglês",
        "nivel": "Intermediário"
      }
    ]
  },
  "projetos": [
    {
      "nome": "Nome do Projeto",
      "tecnologias": ["Tecnologia 1", "Tecnologia 2"],
      "descricao_pontos": [
        "Descrição de conquista ou funcionalidade 1",
        "Descrição de conquista ou funcionalidade 2"
      ]
    }
  ]
}

------------------------------------------------------------------------
6. 📝 LICENÇA
------------------------------------------------------------------------
Este projeto está sob a licença MIT.
========================================================================