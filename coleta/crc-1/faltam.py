"""Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de
vezes diferente do esperado (1 em turno único, ou o que a maioria dos pares tem), e os jogos por clube.

Uso: python coleta/crc-1/faltam.py 1995/96 [fase]
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
sys.path.insert(0, str(AQUI))
from conferir import preparar  # noqa: E402
from edicoes import EDICOES  # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temp = sys.argv[1]
    fase = sys.argv[2] if len(sys.argv) > 2 else ""
    e = next(x for x in EDICOES if x.temporada == temp)
    js = [j for j in preparar(e)["jogos"] if j["fase"] == fase]
    clubes = sorted({x for j in js for x in (j["m"], j["v"]) if x})
    ida = Counter((j["m"], j["v"]) for j in js)
    par = Counter(frozenset((j["m"], j["v"])) for j in js)
    normal = Counter(par.values()).most_common(1)[0][0] if par else 0
    por_clube = Counter(x for j in js for x in (j["m"], j["v"]))
    print(f"{temp}: {len(js)} jogos, {len(clubes)} clubes; jogos por par mais comum: {normal}")
    print("jogos por clube:", dict(sorted(por_clube.items(), key=lambda kv: kv[1])))
    for a in clubes:
        for b in clubes:
            if a < b and par[frozenset((a, b))] != normal:
                print(f"  {a} x {b}: {par[frozenset((a, b))]} (ida {ida[(a, b)]}, volta {ida[(b, a)]})")
