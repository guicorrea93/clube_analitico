"""Lê a tabela final e a matriz de resultados das páginas da Série B na Wikipédia em inglês
(data/serie_b/wikipedia/en_{ano}.txt, baixadas por serie_b/wikipedia.py).

As páginas usam os módulos "Sports table" (tabela: team1..teamN na ordem final, win/draw/loss/gf/ga
de cada sigla, adjust_points para punições) e "Sports results" (match_SIGLA1_SIGLA2 = placar). A sigla
vira nome pelo name_SIGLA ("[[Link|Nome]]").

Uso: python serie_b/wiki.py [ano]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "data" / "serie_b" / "wikipedia"


def _texto(ano: int) -> str | None:
    f = PASTA / f"en_{ano}.txt"
    return f.read_text(encoding="utf-8") if f.exists() else None


def _nome(valor: str) -> str:
    """'[[América Futebol Clube (MG)|América Mineiro]]' -> 'América Mineiro'; tira refs, {{nowrap|..}} e marcações."""
    valor = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", valor)
    valor = re.sub(r"\{\{\s*nowrap\s*\|(.*)\}\}", r"\1", valor)
    m = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", valor)
    return (m.group(1) if m else valor).strip(" '")


def nomes(ano: int) -> dict[str, str]:
    """Sigla -> nome. O valor vai até o próximo parâmetro name_ ou o fim da linha (o "|" do link fica dentro)."""
    t = _texto(ano) or ""
    return {s: _nome(v) for s, v in re.findall(r"\|\s*name_([A-Za-z0-9]+)\s*=\s*(.+?)(?=\s*\|\s*name_|\n|$)", t)}


def tabela(ano: int) -> list[dict]:
    """Tabela final: [{pos, sigla, nome, v, e, d, gp, gc, ajuste}] na ordem oficial (vazia se a página não tem)."""
    t = _texto(ano)
    if not t or "Sports table" not in t:
        return []
    i = t.find("Sports table")
    bloco = t[i:t.find("}}", t.find("|team1", i)) + 2] if "|team1" in t[i:] else ""
    # o bloco vai até o fecho do módulo: pega do início até o próximo "{{#invoke" ou o fim da seção
    fim = t.find("\n}}", i)
    bloco = t[i:fim if fim > 0 else len(t)]
    ordem = re.findall(r"\|\s*team(\d+)\s*=\s*([A-Za-z0-9]+)", bloco)
    nm = nomes(ano)
    num = lambda chave, s: int(m.group(1)) if (m := re.search(rf"\|\s*{chave}_{s}\s*=\s*(-?\d+)", bloco)) else 0
    saida = []
    for pos, s in sorted(((int(p), s) for p, s in ordem)):
        saida.append({"pos": pos, "sigla": s, "nome": nm.get(s, s), "v": num("win", s), "e": num("draw", s), "d": num("loss", s),
                      "gp": num("gf", s), "gc": num("ga", s), "ajuste": num("adjust_points", s)})
    return saida


def ajustes(ano: int) -> dict[str, int]:
    """Punições (e bônus) de pontos: nome -> ajuste (adjust_points_SIGLA), mesmo sem a tabela completa."""
    t = _texto(ano) or ""
    nm = nomes(ano)
    saida: dict[str, int] = {}
    for s, v in re.findall(r"\|\s*adjust_points_([A-Za-z0-9]+)\s*=\s*(-?\d+)", t):
        saida[nm.get(s, s)] = int(v)   # a sigla repetida (página com duas tabelas) vale uma vez
    return saida


def resultados(ano: int) -> list[tuple[str, str, int, int]]:
    """Matriz de resultados: [(mandante, visitante, gols, gols)] pelos nomes da página."""
    t = _texto(ano) or ""
    nm = nomes(ano)
    saida = []
    for a, b, gm, gv in re.findall(r"\|\s*match_([A-Za-z0-9]+)_([A-Za-z0-9]+)\s*=\s*(?:\[[^\s\]]+\s+)?(\d+)\s*[–-]\s*(\d+)", t):
        saida.append((nm.get(a, a), nm.get(b, b), int(gm), int(gv)))
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for ano in [int(a) for a in sys.argv[1:]] or range(2003, 2026):
        tb = tabela(ano)
        print(ano, len(tb), "na tabela,", len(resultados(ano)), "resultados", [(r["pos"], r["nome"], r["ajuste"]) for r in tb[:3]])
