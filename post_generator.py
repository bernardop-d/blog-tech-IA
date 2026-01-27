import os
from datetime import datetime
import random

os.makedirs("_posts", exist_ok=True)

topics = [
    # IA / ML
    ("IA em produção: decisões técnicas que importam", ["ia","engenharia","backend"]),
    ("RAG além do hype: quando realmente usar", ["ia","llm","rag"]),
    ("Erros comuns ao escalar sistemas de IA", ["ia","mlops"]),

    # Cyber Security
    ("Falhas de segurança comuns em APIs REST", ["security","api","backend"]),
    ("Por que autenticação mal feita quebra sistemas", ["security","auth"]),
    ("Boas práticas básicas de cyber security que muitos ignoram", ["security","infra"]),

    # Linguagens de Programação
    ("Por que Python continua dominante no backend", ["python","backend"]),
    ("Quando NÃO usar JavaScript no backend", ["javascript","arquitetura"]),
    ("Comparando linguagens: performance vs produtividade", ["programacao"]),

    # Backend / Arquitetura
    ("Monólito ou microsserviços? A decisão real", ["arquitetura","backend"]),
    ("Erros clássicos ao escalar aplicações web", ["backend","infra"]),
    ("Trade-offs técnicos que todo backend enfrenta", ["engenharia"]),

    # Softwares / Ferramentas
    ("Ferramentas que realmente aumentam produtividade dev", ["software","produtividade"]),
    ("Automatizando tarefas repetitivas com scripts simples", ["automacao","devops"]),
    ("Git além do básico: hábitos profissionais", ["git","workflow"]),

    # Hardware / Infra
    ("Como hardware impacta performance de aplicações", ["hardware","performance"]),
    ("SSD vs HDD: impacto real no dia a dia", ["hardware"]),
    ("Quando vale investir em mais RAM", ["hardware","infra"]),

    # DevOps
    ("Automação com GitHub Actions na prática", ["devops","automacao"]),
    ("Erros comuns em pipelines CI/CD", ["devops","ci"]),
]

today = datetime.now()
date_str = today.strftime("%Y-%m-%d")
title = random.choice(topics)

# Nome do arquivo no padrão que o Jekyll exige
filename = f"_posts/{date_str}-post-{random.randint(1000,9999)}.md"

content = f"""---
layout: post
title: "{title}"
date: {date_str}
categories: [Tecnologia, IA]
---

Este artigo foi gerado automaticamente por um sistema em Python.

O objetivo do projeto é demonstrar automação de geração de conteúdo,
integração com GitHub Actions e publicação contínua usando Jekyll.

Isso simula um blog técnico que se mantém atualizado de forma autônoma.
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Post criado: {filename}")
