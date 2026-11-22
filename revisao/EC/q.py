"""Lista jogos do pacote ecu-1: python -I revisao/EC/q.py <temporada> [fase-substr] [clube-substr] [data-substr]"""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, sys
a = sys.argv[1:] + [""] * 4
t, f, c, d = a[:4]
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/partidas.csv", encoding="utf-8")):
    if r["temporada"] != t: continue
    if f and f.lower() not in r["fase"].lower(): continue
    if c and c.lower() not in (r["mandante"] + r["visitante"]).lower(): continue
    if d and d not in r["data"]: continue
    print(r["id"], r["fase"], r["grupo"], r["rodada"], r["data"], r["mandante"], r["gols_mandante"], "x", r["gols_visitante"], r["visitante"], r["penaltis_mandante"], r["penaltis_visitante"], r["resultado_especial"], r["fonte"], r["fonte_id"], r["observacao"][:80], sep=" | ")
