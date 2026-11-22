"""Pares de clubes com número de jogos fora do padrão na fase de liga de cada edição (pacote do chi-1).
Uso: python -I revisao/CH/pares.py [temporada...]"""
import csv, sys
from collections import Counter, defaultdict
P = "data/coleta/chi-1/pacote/partidas.csv"
jogos = defaultdict(list)
for r in csv.DictReader(open(P, encoding="utf-8")):
    jogos[(r["temporada"], r["fase"], r["grupo"])].append(r)
alvo = set(sys.argv[1:])
for (t, f, g), js in jogos.items():
    if alvo and t not in alvo:
        continue
    if len(js) < 20:
        continue
    pares = Counter(frozenset((j["mandante"], j["visitante"])) for j in js)
    modo = Counter(pares.values()).most_common(1)[0][0]
    clubes = {x for j in js for x in (j["mandante"], j["visitante"])}
    # pares que nunca se enfrentaram
    falt = [(a, b) for a in sorted(clubes) for b in sorted(clubes) if a < b and frozenset((a, b)) not in pares]
    fora = [(sorted(p), n) for p, n in pares.items() if n != modo]
    if fora or falt:
        print(f"{t} | {f} {g} | {len(js)} jogos, {len(clubes)} clubes, padrão {modo}x")
        for p, n in fora: print("   ", n, "x", " x ".join(p))
        for a, b in falt[:10]: print("    0 x", a, "x", b)
