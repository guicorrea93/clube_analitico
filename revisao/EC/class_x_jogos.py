"""Classificação final do pacote: jogos de cada clube na tabela x jogos do clube na edição (partidas.csv).
Mostra a fonte da classificação e quantos clubes têm menos jogos na tabela que na edição."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, collections
J = collections.Counter(); JL = collections.Counter()
fases = {(r["temporada"], r["fase"]): r["tipo"] for r in csv.DictReader(open("data/coleta/ecu-1/pacote/fases.csv", encoding="utf-8"))}
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/partidas.csv", encoding="utf-8")):
    if r["gols_mandante"] == "": continue
    for c in (r["mandante"], r["visitante"]):
        J[(r["temporada"], c)] += 1
cl = collections.defaultdict(list)
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/classificacao_final.csv", encoding="utf-8")):
    cl[r["temporada"]].append(r)
for t, rs in cl.items():
    menos = [(r["clube"], int(r["jogos"] or 0), J[(t, r["clube"])]) for r in rs if int(r["jogos"] or 0) != J[(t, r["clube"])]]
    print(t, rs[0]["fonte"], f"{len(menos)}/{len(rs)} clubes com jogos diferentes", menos[:3], sep=" | ")
