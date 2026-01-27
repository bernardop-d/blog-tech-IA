from datetime import datetime
import random
import os

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

now = datetime.now()

for i in range(2):  # dois posts por execução
    title, tags = random.choice(topics)
    filename = f"_posts/{now.strftime('%Y-%m-%d')}-{now.strftime('%H%M')}-{i}.md"

    content = f"""---
title: "{title}"
description: "Discussão técnica sobre {title.lower()}"
tags: {tags}
---

## Contexto
Este artigo faz parte de um **blog técnico totalmente automatizado**, focado em tecnologia aplicada ao mundo real.

## O problema real
Na prática, decisões técnicas envolvem custo, manutenção, segurança e impacto a longo prazo.

## Abordagem técnica
Aqui o foco é **engenharia de software**, não modismo ou hype.

## Conclusão
Boas decisões técnicas surgem de entendimento profundo, não de tendências passageiras.
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
