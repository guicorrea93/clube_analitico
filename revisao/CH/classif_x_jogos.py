"""Classificação final (pacote) x soma de todos os jogos de cada clube na edição (V/E/D/GP/GC e pontos).
Mostra as edições em que a classificação não bate com os jogos, e pontos x conta (pv*V+E+ajuste).
Uso: python -I revisao/CH/classif_x_jogos.py"""
import csv
from collections import defaultdict
PK = "data/coleta/chi-1/pacote/"
pv = {r["temporada"]: int(r["pontos_vitoria"]) for r in csv.DictReader(open(PK + "edicoes.csv", encoding="utf-8"))}
soma = defaultdict(lambda: [0] * 6)
for r in csv.DictReader(open(PK + "partidas.csv", encoding="utf-8")):
    if r["gols_mandante"] == "" or r["resultado_especial"] in ("abd", "n/p"):
        continue
    gm, gv = int(r["gols_mandante"]), int(r["gols_visitante"])
    for c, a, b in ((r["mandante"], gm, gv), (r["visitante"], gv, gm)):
        s = soma[(r["temporada"], c)]
        s[0] += 1; s[4] += a; s[5] += b
        s[1 if a > b else 2 if a == b else 3] += 1
ruins = defaultdict(list)
for r in csv.DictReader(open(PK + "classificacao_final.csv", encoding="utf-8")):
    t, c = r["temporada"], r["clube"]
    cl = [int(r[k]) for k in ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra")]
    s = soma[(t, c)]
    pts = int(r["pontos"]); conta = pv[t] * cl[1] + cl[2]
    msg = []
    if cl != s:
        msg.append(f"classif {cl} jogos {s}")
    if abs(pts - conta) > 3:
        msg.append(f"pontos {pts} x conta {conta} (ajuste {r['ajuste_pontos']})")
    if msg:
        ruins[t].append(f"{r['posicao']:>2} {c}: " + "; ".join(msg))
for t, v in ruins.items():
    print(f"== {t}: {len(v)} clubes")
    for x in v[:4]: print("   ", x)
