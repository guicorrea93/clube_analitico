"""Compara as datas dos jogos da Série B entre o commit da 1ª rodada (04cb286) e os CSV atuais."""
import csv, io, subprocess, glob, os, sys
from collections import Counter
tot = Counter(); viradas = []
for f in sorted(glob.glob("data/serie_b/csv/serie_b_*_partidas.csv")):
    a = os.path.basename(f)[8:12]
    try: old = subprocess.run(["git", "show", "04cb286:" + f.replace("\\", "/")], capture_output=True, check=True).stdout.decode("utf-8")
    except subprocess.CalledProcessError: continue
    def ld(t):
        r = list(csv.reader(io.StringIO(t), delimiter=";"))
        h = r[0]; return [dict(zip(h, x)) for x in r[1:]]
    o = ld(old); n = ld(open(f, encoding="utf-8").read())
    key = lambda x: (x.get("fase"), x.get("mandante"), x.get("visitante"), x.get("placar"))
    od = Counter(); 
    oldd = {}
    for x in o: oldd.setdefault(key(x), []).append(x.get("data"))
    for x in n:
        k = key(x)
        if k in oldd and oldd[k]:
            d0 = oldd[k].pop(0)
            if d0 != x.get("data"):
                tot[a] += 1
                if d0 and x.get("data") and abs((int(x["data"][5:7]) - int(d0[5:7]))) >= 1 and x["data"][8:] == d0[8:]:
                    viradas.append((a, x.get("fase"), x.get("mandante"), x.get("visitante"), d0, x.get("data")))
print(sorted(tot.items()))
print("mesmo dia, mês trocado:", len(viradas))
for v in viradas[:40]: print(v)
