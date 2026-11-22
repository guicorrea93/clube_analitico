"""Pacote ecu-1 x ESPN: data do jogo (local, UTC-5) e placar, nos jogos casados (fonte_id com espn:<id>).
Também diz se o mando bate. Saída: lista das diferenças."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, json, glob, re
from datetime import datetime, timedelta
esp = {}
for f in glob.glob("data/coleta/ecu-1/espn/ecu1_*.json"):
    for g in json.load(open(f, encoding="utf-8")):
        esp[g["id"]] = g
n = nd = npl = 0
saida = []
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/partidas.csv", encoding="utf-8")):
    m = re.search(r"espn:(\d+)", r["fonte_id"])
    if not m: continue
    g = esp.get(m.group(1))
    if not g: continue
    n += 1
    loc = (datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")) - timedelta(hours=5)).date().isoformat()
    if loc != r["data"]:
        nd += 1
        saida.append(("DATA", r["temporada"], r["fase"], r["rodada"], r["data"], loc, r["mandante"], r["gols_mandante"], r["gols_visitante"], r["visitante"], g["mandante"], g["gols_mandante"], g["gols_visitante"], g["visitante"]))
    if (g["gols_mandante"], g["gols_visitante"]) != (r["gols_mandante"], r["gols_visitante"]):
        npl += 1
        saida.append(("PLACAR", r["temporada"], r["fase"], r["rodada"], r["data"], loc, r["mandante"], r["gols_mandante"], r["gols_visitante"], r["visitante"], g["mandante"], g["gols_mandante"], g["gols_visitante"], g["visitante"], r["resultado_especial"]))
print("casados", n, "data diferente", nd, "placar diferente", npl)
for s in saida: print(*s, sep=" | ")
