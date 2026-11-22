"""Data do pacote x data local (UTC-5) da ESPN, nos jogos casados (fonte_id com espn:). python -I revisao/PE/datas_espn.py"""
import csv, json, sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
R = Path(__file__).resolve().parents[2]
espn = {}
for f in (R / "data/coleta/per-1/espn").glob("per1_*.json"):
    for e in json.load(open(f, encoding="utf-8")):
        espn[str(e["id"])] = e
dif = []
por_fase = Counter(); por_ano = defaultdict(int); casados = 0
for r in csv.DictReader(open(R / "data/coleta/per-1/pacote/partidas.csv", encoding="utf-8")):
    ids = [x.split(":")[1] for x in r["fonte_id"].split() if x.startswith("espn:")]
    if not ids or ids[0] not in espn:
        continue
    casados += 1
    e = espn[ids[0]]
    loc = (datetime.strptime(e["data_hora"], "%Y-%m-%dT%H:%MZ") - timedelta(hours=5)).date().isoformat()
    if r["data"] != loc:
        dias = (datetime.fromisoformat(loc) - datetime.fromisoformat(r["data"])).days if r["data"] else None
        dif.append((r["temporada"], r["fase"], r["data"], loc, dias, r["mandante"], r["gols_mandante"], r["gols_visitante"], r["visitante"]))
        por_fase[r["fase"]] += 1; por_ano[r["temporada"]] += 1
print("casados com a ESPN:", casados, "| data diferente:", len(dif))
print("por fase:", por_fase.most_common())
print("por ano:", dict(sorted(por_ano.items())))
grandes = [d for d in dif if d[4] is None or abs(d[4]) > 1]
print("diferença > 1 dia:", len(grandes))
out = R / "revisao/PE/datas_espn_diferentes.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["temporada","fase","data_pacote","data_espn_local","dias","mandante","gm","gv","visitante"]); w.writerows(dif)
for d in grandes[:60]: print(d)
