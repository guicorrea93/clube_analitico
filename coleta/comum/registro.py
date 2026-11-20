"""Cadastro comum de clubes das coletas: código do clube no ogol -> nome de exibição, UF e cidade.

Garante que o mesmo clube tenha o mesmo nome em todos os pacotes (Série C, Série D, estaduais...).
Fica em data/coleta/comum/clubes_ogol.json. Cada coleta lê o cadastro antes de dar nome a um clube e,
ao gravar o pacote, acrescenta os clubes novos.
"""
from __future__ import annotations

import json
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "comum" / "clubes_ogol.json"


def ler() -> dict[str, dict]:
    return json.loads(ARQUIVO.read_text(encoding="utf-8")) if ARQUIVO.exists() else {}


def acrescentar(clubes: dict[str, dict], slug: str) -> None:
    """clubes: código -> {clube, uf, cidade}. Não troca o nome de quem já está no cadastro."""
    reg = ler()
    for i, c in clubes.items():
        atual = reg.setdefault(i, {"clube": c["clube"], "uf": c.get("uf"), "cidade": c.get("cidade"), "competicoes": []})
        if slug not in atual["competicoes"]:
            atual["competicoes"].append(slug)
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    ARQUIVO.write_text(json.dumps(dict(sorted(reg.items())), ensure_ascii=False, indent=1), encoding="utf-8")
