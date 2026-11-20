"""Revisão Série C (SC): anomalias nos jogos do pacote.

- clube contra ele mesmo;
- clube em mais de um grupo na mesma fase;
- clube com dois jogos no mesmo dia (ou em dias seguidos);
- mesmo confronto repetido mais vezes do que o turno/returno permite dentro do mesmo grupo.
"""
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comum import ler_csv  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
P = ler_csv("partidas.csv")
print("# clube contra ele mesmo")
for r in P:
    if r["mandante"] == r["visitante"]:
        print(r["id"], r["fase"], r["grupo"], r["data"], r["mandante"], r["gols_mandante"], "x", r["gols_visitante"])
print("\n# clube em mais de um grupo na mesma fase")
g = defaultdict(set)
for r in P:
    if r["grupo"]:
        for c in (r["mandante"], r["visitante"]):
            g[(r["temporada"], r["fase"], c)].add(r["grupo"])
for k, v in sorted(g.items()):
    if len(v) > 1:
        print(k, sorted(v))
print("\n# clube com dois jogos a menos de 2 dias")
d = defaultdict(list)
for r in P:
    if r["data"]:
        for c in (r["mandante"], r["visitante"]):
            d[(r["temporada"], c)].append((date.fromisoformat(r["data"]), r["id"], r["mandante"] + " x " + r["visitante"]))
for k, v in sorted(d.items()):
    v.sort()
    for a, b in zip(v, v[1:]):
        if (b[0] - a[0]).days < 2:
            print(k, a[0], a[1], a[2], "|", b[0], b[1], b[2])
print("\n# confronto repetido no mesmo grupo (mesmo mando)")
c = Counter((r["temporada"], r["fase"], r["grupo"], r["mandante"], r["visitante"]) for r in P if r["grupo"])
for k, n in sorted(c.items()):
    if n > 1:
        print(k, n)
