"""Bloco C: data de cada jogo do banco x data da ESPN (hora de Montevideo, UTC-3), nos jogos que a coleta casou com a ESPN
(o id da ESPN está no fonte_id do pacote). Uso: python -I revisao/UY/datas_espn.py > SCRATCH/UY/datas_espn.txt"""
import csv, glob, json, re
from collections import Counter
from datetime import datetime, timedelta
espn = {}
for f in glob.glob("data/coleta/uru-1/espn/*.json"):
    for j in json.load(open(f, encoding="utf-8")):
        espn[j["id"]] = (datetime.strptime(j["data_hora"], "%Y-%m-%dT%H:%MZ") - timedelta(hours=3)).strftime("%Y-%m-%d")
n, difs = 0, []
for r in csv.DictReader(open("data/coleta/uru-1/pacote/partidas.csv", encoding="utf-8")):
    m = re.search(r"espn:(\d+)", r["fonte_id"])
    if not m or m.group(1) not in espn or not r["data"]:
        continue
    n += 1
    if espn[m.group(1)] != r["data"]:
        dias = (datetime.strptime(espn[m.group(1)], "%Y-%m-%d") - datetime.strptime(r["data"], "%Y-%m-%d")).days
        difs.append((r["temporada"], r["fase"], r["mandante"], r["visitante"], r["gols_mandante"] + "-" + r["gols_visitante"], r["data"], espn[m.group(1)], str(dias)))
print(f"jogos com id da ESPN: {n}; data diferente: {len(difs)}")
print("por fase:", Counter(d[1] for d in difs))
print("por temporada:", Counter(d[0] for d in difs))
for d in difs:
    print("\t".join(d))
