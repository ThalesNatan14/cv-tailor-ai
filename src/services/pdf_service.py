import os
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

def gerar_pdf_curriculo(dados_cv: dict, caminho_saida: str = "curriculo_otimizado.pdf") -> str:
    """
    Recebe o dicionário do currículo otimizado e gera um PDF formatado e profissional.
    """
    doc = SimpleDocTemplate(
        caminho_saida,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Estilos customizados
    style_nome = ParagraphStyle(
        'NomeStyle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A202C"),
        alignment=1,  # Centralizado
        spaceAfter=4
    )
    
    style_contato = ParagraphStyle(
        'ContatoStyle',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#4A5568"),
        alignment=1,
        spaceAfter=12
    )

    style_secao_titulo = ParagraphStyle(
        'SecaoTituloStyle',
        parent=styles['Heading2'],
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=10,
        spaceAfter=4,
        fontName="Helvetica-Bold"
    )

    style_corpo = ParagraphStyle(
        'CorpoStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=6
    )

    style_bullet = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#2D3748"),
        leftIndent=12,
        spaceAfter=3
    )

    elements = []

    # 1. Dados Pessoais
    dp = dados_cv.get("dados_pessoais", {})
    elements.append(Paragraph(dp.get("nome", ""), style_nome))
    
    contatos = [
        dp.get("localizacao", ""),
        dp.get("email", ""),
        dp.get("linkedin", ""),
        dp.get("github", "")
    ]
    texto_contato = " | ".join([c for c in contatos if c])
    elements.append(Paragraph(texto_contato, style_contato))
    
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E2E8F0"), spaceAfter=10))

    # 2. Resumo Profissional
    resumo = dados_cv.get("resumo_profissional", "")
    if resumo:
        elements.append(Paragraph("RESUMO PROFISSIONAL", style_secao_titulo))
        elements.append(Paragraph(resumo, style_corpo))
        elements.append(Spacer(1, 6))

    # 3. Formação Acadêmica
    formacao = dados_cv.get("formacao", [])
    if formacao:
        elements.append(Paragraph("FORMAÇÃO ACADÊMICA", style_secao_titulo))
        for f in formacao:
            texto_f = f"<b>{f.get('curso', '')}</b> - {f.get('instituicao', '')} ({f.get('status', '')} - Previsão: {f.get('previsao_formatura', '')})"
            elements.append(Paragraph(texto_f, style_corpo))
        elements.append(Spacer(1, 6))

    # 4. Habilidades Técnicas
    habilidades = dados_cv.get("habilidades", {})
    if habilidades:
        elements.append(Paragraph("HABILIDADES TÉCNICAS", style_secao_titulo))
        for categoria, itens in habilidades.items():
            if isinstance(itens, list):
                if itens and isinstance(itens[0], dict): # Ex: idiomas
                    itens_str = ", ".join([f"{i.get('idioma')}: {i.get('nivel')}" for i in itens])
                else:
                    itens_str = ", ".join(itens)
                cat_nome = categoria.replace('_', ' ').title()
                elements.append(Paragraph(f"<b>{cat_nome}:</b> {itens_str}", style_corpo))
        elements.append(Spacer(1, 6))

    # 5. Projetos
    projetos = dados_cv.get("projetos", [])
    if projetos:
        elements.append(Paragraph("PROJETOS RELEVANTES", style_secao_titulo))
        for p in projetos:
            tecs = ", ".join(p.get("tecnologias", []))
            elements.append(Paragraph(f"<b>{p.get('nome', '')}</b> <i>({tecs})</i>", style_corpo))
            for ponto in p.get("descricao_pontos", []):
                elements.append(Paragraph(f"• {ponto}", style_bullet))
            elements.append(Spacer(1, 4))

    doc.build(elements)
    print(f"PDF gerado com sucesso em: {caminho_saida}")
    return caminho_saida

if __name__ == "__main__":
    # Teste rápido com o JSON gerado
    with open("cv_base.json", "r", encoding="utf-8") as f:
        cv_exemplo = json.load(f)
    gerar_pdf_curriculo(cv_exemplo, "teste_curriculo.pdf")