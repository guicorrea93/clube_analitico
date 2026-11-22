"""Para cada jogo com data do pacote diferente (> 1 dia) da Wikipédia it, a data da RSSSF decide.
Uso: python -I revisao/IT/datas_triangular.py > SCRATCH/IT/datas_triangular.txt
"""
import csv, os, sys
from collections import defaultdict, Counter
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itwiki, rsssf_datas  # noqa: E402
pj = defaultdict(list)
for x in csv.DictReader(open(os.path.join(itwiki.RAIZ, "data/coleta/ita-1/pacote/partidas.csv"), encoding="utf-8")):
    pj[int(x["temporada"][:4])].append(x)
res = Counter(); por_ano = defaultdict(Counter); linhas = []
for a in itwiki.ANOS:
    if a in (1945, 2019):
        continue
    cal = itwiki.calendario(a); rs = rsssf_datas.datas(a)
    for j in pj[a]:
        k = (j["mandante"], j["visitante"])
        w = cal.get(k); r = rs.get(k)
        if not w:
            continue
        d = abs((date.fromisoformat(j["data"]) - date.fromisoformat(w)).days)
        if d <= 1:
            continue
        if r is None:
            cat = "sem RSSSF"
        elif r[0] == w:
            cat = "RSSSF = wiki (pacote errado)"
        elif r[0] == j["data"]:
            cat = "RSSSF = pacote (wiki errada)"
        else:
            cat = "três datas diferentes"
        res[cat] += 1; por_ano[f"{a}/{str(a+1)[-2:]}"][cat] += 1
        linhas.append(f"{a}/{str(a+1)[-2:]} {k[0]} x {k[1]}: pacote {j['data']} | wiki {w} | RSSSF {r[0] + ' (' + r[1] + ')' if r else '-'} -> {cat}")
print(dict(res))
for a, c in por_ano.items():
    print(a, dict(c))
print()
print("\n".join(linhas))
