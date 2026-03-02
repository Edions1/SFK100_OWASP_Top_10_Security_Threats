# -*- coding: utf-8 -*-
# Versão compatível sem input interativo (menu automático de demonstração)
# Gera:
# - Exibição da tabela
# - CSV da matriz atual
# - PDF da matriz atual

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

# ========================
# MATRIZ ATUAL
# ========================

rtm_data = [
    ["Cadastro de usuário",
     "Acesso não autorizado aos dados de registro",
     "Exposição de dados sensíveis",
     "Controles de acesso adequados"],

    ["Funcionalidade de login",
     "Força bruta / quebra de senha",
     "Política fraca / roubo credenciais",
     "Bloqueio de conta + senha forte"],

    ["Pesquisa de produtos",
     "Injeção SQL / vazamento",
     "Falhas banco de dados",
     "Sanitização + queries parametrizadas"],

    ["Carrinho de compras",
     "Acesso não autorizado",
     "Sequestro sessão / CSRF",
     "Gerenciamento seguro + CSRF token"],

    ["Processamento de pagamento",
     "Roubo dados / MITM",
     "Interceptação rede",
     "Criptografia + protocolo seguro"],

    ["Realização do pedido",
     "Manipulação de preço",
     "Validação insegura / CSRF",
     "Verificação pedido + CSRF"],

    ["Avaliações de clientes",
     "Avaliações falsas",
     "Spam / injeção conteúdo",
     "Moderação + validação"]
]

colunas = ["Caso de Uso", "Caso de Abuso", "Ameaças", "Mitigações"]

# ========================
# MOSTRAR TABELA
# ========================

df = pd.DataFrame(rtm_data, columns=colunas)
print("\n=== MATRIZ RTM ===\n")
print(df.to_string(index=False))
print("\n")

# ========================
# EXPORTAR CSV
# ========================

csv_path = "/mnt/data/rtm_export.csv"
df.to_csv(csv_path, index=False)

# ========================
# EXPORTAR PDF
# ========================

pdf_path = "/mnt/data/rtm_export.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title = Paragraph("<b>Matriz RTM</b>", styles["Title"])
elements.append(title)
elements.append(Spacer(1, 0.5 * inch))

table_data = [colunas] + rtm_data
table = Table(table_data, repeatRows=1)

table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
]))

elements.append(table)
doc.build(elements)

print("Arquivos gerados com sucesso:")
print(f"CSV: {csv_path}")
print(f"PDF: {pdf_path}")
