"""Tabela final oficial da Série A de pontos corridos (2003 em diante), com as punições do STJD.

O brasileirao.db montou a classificação final de 2003+ pela última rodada, sem as decisões do tribunal
(ex.: 2013, Flamengo e Portuguesa perderam 4 pontos e a Portuguesa caiu; 2004, São Caetano perdeu 24).
A fonte aqui é a Wikipédia em inglês ("{ano} Campeonato Brasileiro Série A"), módulo "Sports table":
ordem oficial e adjust_points. As páginas ficam em data/serie_a/wikipedia/en_{ano}.txt.

oficial(ano, achar) devolve {clube_id: (posição, ajuste)} usando achar(nome) -> clube_id, ou None quando a
página não tem a tabela ou algum nome não casa. migrar_brasileirao.py aplica isso na Série A.

Uso: python futebol/oficial_serie_a.py [ano ...]     (baixa o que falta e mostra o que leu)
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "data" / "serie_a" / "wikipedia"
ANOS = range(2003, 2026)
sys.path.insert(0, str(RAIZ / "serie_b"))
import wiki  # noqa: E402  (leitor do módulo "Sports table", o mesmo da Série B)
from wikipedia import wikitexto  # noqa: E402


def baixar(anos) -> None:
    PASTA.mkdir(parents=True, exist_ok=True)
    for a in anos:
        destino = PASTA / f"en_{a}.txt"
        if destino.exists():
            continue
        txt = wikitexto("en", f"{a} Campeonato Brasileiro Série A")
        if txt:
            destino.write_text(txt, encoding="utf-8")
        time.sleep(4)


def tabela(ano: int) -> list[dict]:
    """[{pos, nome, ajuste, v, e, d, gp, gc}] do primeiro {{#invoke:sports table}} com time (o nome do módulo varia
    em maiúscula/minúscula entre as páginas)."""
    f = PASTA / f"en_{ano}.txt"
    if not f.exists():
        return []
    t = f.read_text(encoding="utf-8")
    baixo = t.lower()
    i = baixo.find("{{#invoke:sports table")
    while i >= 0:
        fim = t.find("\n}}", i)
        bloco = t[i:fim if fim > 0 else len(t)]
        ordem = re.findall(r"\|\s*team(\d+)\s*=\s*(\w+)", bloco)
        if not ordem and (m := re.search(r"\|\s*team_order\s*=\s*([\w, ]+)", bloco)):   # formato novo: lista numa linha só
            ordem = [(str(k + 1), s.strip()) for k, s in enumerate(m.group(1).split(",")) if s.strip()]
        if ordem:
            nm = {s: wiki._nome(v) for s, v in re.findall(r"\|\s*name_(\w+)\s*=\s*(.+?)(?=\s*\|\s*name_|\n|$)", bloco)}
            num = lambda chave, s: int(m.group(1)) if (m := re.search(rf"\|\s*{chave}_{s}\s*=\s*(-?\d+)", bloco)) else 0
            return [{"pos": int(p), "sigla": s, "nome": nm.get(s, s), "v": num("win", s), "e": num("draw", s), "d": num("loss", s),
                     "gp": num("gf", s), "gc": num("ga", s), "ajuste": num("adjust_points", s)} for p, s in sorted((int(p), s) for p, s in ordem)]
        i = baixo.find("{{#invoke:sports table", i + 1)
    return []


def oficial(ano: int, achar) -> dict[int, tuple[int, int]] | None:
    tb = tabela(ano)
    if not tb:
        return None
    saida = {}
    for r in tb:
        cid = achar(r["nome"])
        if cid is None or cid in saida:
            return None
        saida[cid] = (r["pos"], r["ajuste"])
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    anos = [int(a) for a in sys.argv[1:]] or ANOS
    baixar(anos)
    for a in anos:
        tb = tabela(a)
        print(a, len(tb), [(r["pos"], r["nome"], r["ajuste"]) for r in tb if r["ajuste"]])
