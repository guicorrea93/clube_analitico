"""Datas dos jogos do pacote x Calendario da Wikipédia it, temporada a temporada.
Uso: python -I revisao/IT/compara_datas.py > SCRATCH/IT/datas_itwiki.txt
"""
import csv, os, sys
from collections import defaultdict, Counter
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itwiki  # noqa: E402
pj = defaultdict(list)
for x in csv.DictReader(open(os.path.join(itwiki.RAIZ, "data/coleta/ita-1/pacote/partidas.csv"), encoding="utf-8")):
    pj[int(x["temporada"][:4])].append(x)
tot = Counter()
por_dec = defaultdict(Counter)
difs = []
for a in itwiki.ANOS:
    if a == 1945:
        continue
    cal = itwiki.calendario(a)
    for j in pj[a]:
        k = (j["mandante"], j["visitante"])
        dec = f"{a // 10 * 10}s"
        if k not in cal:
            tot["sem_wiki"] += 1; por_dec[dec]["sem_wiki"] += 1
            continue
        d = abs((date.fromisoformat(j["data"]) - date.fromisoformat(cal[k])).days)
        cat = "igual" if d == 0 else "1 dia" if d == 1 else "mais"
        tot[cat] += 1; por_dec[dec][cat] += 1
        if d > 1:
            difs.append((a, j["data"], cal[k], k))
print(dict(tot))
for dec in sorted(por_dec):
    print(dec, dict(por_dec[dec]))
print()
por_ano = Counter(a for a, *_ in difs)
print("diferenças > 1 dia por temporada:", dict(por_ano))
for a, dp, dw, k in difs:
    print(f"{a}/{str(a+1)[-2:]} {k[0]} x {k[1]}: pacote {dp} | wiki {dw}")
