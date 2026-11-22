"""Data do pacote x data da ESPN (UTC-4/-3 -> dia local aproximado) nos jogos do chi-1 ligados à ESPN (fonte_id espn:).
Uso: python -I revisao/CH/datas_espn.py"""
import csv, glob, json
from collections import Counter, defaultdict
from datetime import datetime, timedelta
esp = {}
for f in glob.glob("data/coleta/chi-1/espn/chi1_*.json"):
    for g in json.load(open(f, encoding="utf-8")):
        dt = datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")) - timedelta(hours=4)
        esp[g["id"]] = (dt.date().isoformat(), g)
dif = defaultdict(list)
tot = Counter()
for r in csv.DictReader(open("data/coleta/chi-1/pacote/partidas.csv", encoding="utf-8")):
    ids = [x.split(":")[1] for x in r["fonte_id"].split() if x.startswith("espn:")]
    if not ids or ids[0] not in esp:
        continue
    tot[r["temporada"]] += 1
    de, g = esp[ids[0]]
    if r["data"] != de:
        try:
            d = abs((datetime.fromisoformat(r["data"]) - datetime.fromisoformat(de)).days) if r["data"] else 999
        except ValueError:
            d = 999
        if d > 1:
            dif[r["temporada"]].append((r["fase"], r["data"], de, r["mandante"], r["visitante"]))
n = 0
for t in sorted(dif):
    print(f"{t}: {len(dif[t])} de {tot[t]} jogos com data a mais de 1 dia da ESPN")
    for x in dif[t][:6]:
        print("    ", x)
    n += len(dif[t])
print("total", n, "de", sum(tot.values()))
