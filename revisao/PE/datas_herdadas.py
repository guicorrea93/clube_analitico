"""Jogos de mata-mata (fases de tipo mata_mata) com a data E a rodada iguais às do último jogo de liga anterior na página:
sinal de data herdada (a página da RSSSF não traz a data da final, o leitor repete a última). python -I revisao/PE/datas_herdadas.py"""
import csv, sys
from collections import defaultdict
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
R = Path(__file__).resolve().parents[2] / "data/coleta/per-1/pacote"
tipo = {(r["temporada"], r["fase"]): r["tipo"] for r in csv.DictReader(open(R / "fases.csv", encoding="utf-8"))}
jogos = defaultdict(list)
for r in csv.DictReader(open(R / "partidas.csv", encoding="utf-8")):
    jogos[r["temporada"]].append(r)
tot = 0; lista = []
for t, js in jogos.items():
    vistos = defaultdict(int)
    for r in js:
        if tipo.get((t, r["fase"])) == "mata_mata" and r["data"]:
            vistos[(r["data"], r["rodada"])] += 1
    for r in js:
        if tipo.get((t, r["fase"])) != "mata_mata" or not r["data"]:
            continue
        # mesma data e rodada que algum jogo de liga
        liga = [x for x in js if tipo.get((t, x["fase"])) != "mata_mata" and x["data"] == r["data"] and x["rodada"] == r["rodada"]]
        mm = [x for x in js if tipo.get((t, x["fase"])) == "mata_mata" and x["data"] == r["data"]]
        if liga or len({(x['mandante'], x['visitante']) for x in mm} | {(x['visitante'], x['mandante']) for x in mm}) < 2 * len(mm) and len(mm) > 1:
            tot += 1; lista.append((t, r["fase"], r["data"], r["rodada"], r["mandante"], r["gols_mandante"], r["gols_visitante"], r["visitante"], r["fonte_id"].split()[0]))
print("jogos de mata-mata com data suspeita:", tot)
anos = defaultdict(int)
for x in lista: anos[x[0]] += 1
print(dict(sorted(anos.items())))
with open(Path(__file__).resolve().parent / "datas_herdadas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["temporada","fase","data","rodada","mandante","gm","gv","visitante","fonte_id"]); w.writerows(sorted(lista))
