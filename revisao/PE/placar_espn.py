"""Placar do pacote x placar da ESPN nos jogos casados (independente da RSSSF). python -I revisao/PE/placar_espn.py"""
import csv, json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
R = Path(__file__).resolve().parents[2]
espn = {}
for f in (R / "data/coleta/per-1/espn").glob("per1_*.json"):
    for e in json.load(open(f, encoding="utf-8")):
        espn[str(e["id"])] = e
n = dif = 0
for r in csv.DictReader(open(R / "data/coleta/per-1/pacote/partidas.csv", encoding="utf-8")):
    ids = [x.split(":")[1] for x in r["fonte_id"].split() if x.startswith("espn:")]
    if not ids or ids[0] not in espn: continue
    e = espn[ids[0]]; n += 1
    pe = (e["gols_mandante"], e["gols_visitante"])
    if pe != (r["gols_mandante"], r["gols_visitante"]):
        dif += 1
        print(r["temporada"], r["fase"], r["data"], r["mandante"], r["gols_mandante"], "x", r["gols_visitante"], r["visitante"],
              "| ESPN", e["mandante"], pe[0], "x", pe[1], e["visitante"], e["situacao"], "|", r["resultado_especial"], r["observacao"][:80])
print("casados", n, "placar diferente", dif)
