"""Edições cuja classificação final traz menos jogos que os que o clube jogou no ano (ex.: só o Clausura em vez da tabela
acumulada). Compara J da classificação com os jogos do clube no pacote (todas as fases). python -I revisao/PE/classif_parcial.py"""
import csv, sys
from collections import defaultdict, Counter
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
P = Path(__file__).resolve().parents[2] / "data/coleta/per-1/pacote"
jog = defaultdict(Counter)
for r in csv.DictReader(open(P / "partidas.csv", encoding="utf-8")):
    if r["gols_mandante"] != "" or r["resultado_especial"]:
        jog[r["temporada"]][r["mandante"]] += 1; jog[r["temporada"]][r["visitante"]] += 1
cl = defaultdict(list)
for r in csv.DictReader(open(P / "classificacao_final.csv", encoding="utf-8")): cl[r["temporada"]].append(r)
for t in sorted(cl):
    if not jog[t]: continue
    rs = [r for r in cl[t] if r["jogos"]]
    if not rs: continue
    razao = sum(int(r["jogos"]) for r in rs) / max(1, sum(jog[t][r["clube"]] for r in rs))
    if razao < 0.8:
        ex = rs[0]
        print(f"{t}: classificação soma {razao:.0%} dos jogos | fonte {ex['fonte']} | ex.: {ex['clube']} J{ex['jogos']} na tabela x {jog[t][ex['clube']]} jogos no pacote")
