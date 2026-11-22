"""Pares de clubes em ordem trocada entre o pacote e a Wikipédia it (posição estritamente diferente), por temporada."""
import csv, os, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itwiki  # noqa: E402
cf = defaultdict(dict)
for x in csv.DictReader(open(os.path.join(itwiki.RAIZ, "data/coleta/ita-1/pacote/classificacao_final.csv"), encoding="utf-8")):
    cf[int(x["temporada"][:4])][x["clube"]] = (int(x["posicao"]), int(x["pontos"]), x["situacao"])
empates = 0
for a in itwiki.ANOS:
    if a == 1945:
        continue
    w = {x["clube"]: x["pos"] for x in itwiki.classifica(a)}
    p = cf[a]
    inv = [(c1, c2) for c1 in w for c2 in w if w[c1] < w[c2] and p[c1][0] > p[c2][0]]
    emp = sum(1 for c1 in w for c2 in w if c1 < c2 and w[c1] == w[c2])
    empates += emp
    if inv:
        print(f"{a}/{str(a+1)[-2:]}", "; ".join(f"{c1} (wiki {w[c1]}, pacote {p[c1][0]}, {p[c1][1]} pts{', '+p[c1][2] if p[c1][2] else ''}) acima de "
                                               f"{c2} (wiki {w[c2]}, pacote {p[c2][0]}{', '+p[c2][2] if p[c2][2] else ''})" for c1, c2 in inv))
print("pares empatados (pari merito) na wiki:", empates)
