"""FR: 1946/47 com os 9 placares da Wikipédia fr (= base descartada) fecha com as tabelas publicadas?"""
import csv
from collections import defaultdict
P = "data/coleta/fra-1/pacote/"
nov = {("Lens", "Le Havre"): (8, 0), ("Lille", "Le Havre"): (3, 0), ("Olympique de Marseille", "Bordeaux"): (0, 0),
       ("SO Montpellier", "Stade Français"): (1, 3), ("CO Roubaix-Tourcoing", "Bordeaux"): (4, 1), ("CO Roubaix-Tourcoing", "Lens"): (5, 2),
       ("CO Roubaix-Tourcoing", "SO Montpellier"): (2, 1), ("Rouen", "Sète"): (6, 1), ("Strasbourg", "Rouen"): (2, 1)}
t = defaultdict(lambda: [0] * 7)
for j in csv.DictReader(open(P + "partidas.csv", encoding="utf-8")):
    if j["temporada"] != "1946/47": continue
    gm, gv = nov.get((j["mandante"], j["visitante"]), (int(j["gols_mandante"]), int(j["gols_visitante"])))
    for c, a, b in ((j["mandante"], gm, gv), (j["visitante"], gv, gm)):
        x = t[c]; x[0] += 1; x[4] += a; x[5] += b
        if a > b: x[1] += 1; x[6] += 2
        elif a == b: x[2] += 1; x[6] += 1
        else: x[3] += 1
for r in csv.DictReader(open(P + "tabelas_publicadas.csv", encoding="utf-8")):
    if r["temporada"] == "1946/47":
        pub = [int(r[k]) for k in ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "pontos")]
        if pub != t[r["clube"]]: print(r["fonte"][:30], r["clube"], "pub", pub, "calc", t[r["clube"]])
