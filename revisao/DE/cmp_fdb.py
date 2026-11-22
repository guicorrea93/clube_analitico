"""Amostra de datas e placares por década: pacote ger-1 x footballdatabase.eu (páginas de rodada), mais os jogos em que
a coleta anotou data diferente no ogol. Uso: python -I revisao/DE/cmp_fdb.py > revisao/DE/cmp_fdb_saida.txt"""
import csv, sys, pathlib
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import fdb  # noqa
PAC = AQUI.parent.parent / "data" / "coleta" / "ger-1" / "pacote"
jogos = defaultdict(dict); por_rod = defaultdict(lambda: defaultdict(list))
for r in csv.DictReader(open(PAC / "partidas.csv", encoding="utf-8")):
    a = int(r["temporada"][:4]); jogos[a][(r["mandante"], r["visitante"])] = r; por_rod[a][int(r["rodada"])].append(r)
# amostra: (temporada, rodadas) — uma ou duas temporadas por década, 3 rodadas cada
AMOSTRA = {1963: [1, 15, 30], 1966: [4, 20, 33], 1972: [5, 18, 34], 1977: [3, 11, 25], 1982: [6, 21, 32], 1984: [2, 16, 29],
           1990: [7, 19, 34], 1993: [1, 2, 3], 1996: [26, 27, 30], 2005: [9, 22, 33], 2014: [12, 24, 34], 2023: [1, 17, 34],
           2025: [10, 20, 31]}
# jogos com data diferente no ogol (relatório da coleta): temporada -> pares
OGOL = {1972: [("Werder Bremen", "Borussia Mönchengladbach")], 1977: [("1860 Munique", "Stuttgart")],
        1982: [("Borussia Mönchengladbach", "Eintracht Frankfurt")], 1983: [("Eintracht Frankfurt", "Bayer Leverkusen")],
        1984: [("Arminia Bielefeld", "Kaiserslautern")], 1990: [("Bayer Leverkusen", "Bochum")]}
for a, pares in OGOL.items():
    for p in pares:
        AMOSTRA.setdefault(a, [])
        r = int(jogos[a][p]["rodada"])
        if r not in AMOSTRA[a]: AMOSTRA[a].append(r)
tot = Counter(); sem_nome = Counter()
for a, rods in sorted(AMOSTRA.items()):
    R = fdb.rodadas(a)
    ok = dif = 0; linhas = []
    for r in rods:
        for j in fdb.jogos(R[r], a):
            if not j["m"] or not j["v"]:
                sem_nome[j["m_fonte"] if not j["m"] else j["v_fonte"]] += 1; continue
            p = jogos[a].get((j["m"], j["v"]))
            if not p:
                linhas.append(f"  sem par no pacote: {j['m']} x {j['v']}"); continue
            tot["n"] += 1
            d_ok = p["data"] == j["data"]; s_ok = (int(p["gols_mandante"]), int(p["gols_visitante"])) == (j["gm"], j["gv"])
            r_ok = int(p["rodada"]) == r
            if d_ok and s_ok and r_ok: ok += 1
            else:
                dif += 1
                linhas.append(f"  DIF rodada {r}: {j['m']} x {j['v']}: pacote {p['data']} {p['gols_mandante']}-{p['gols_visitante']} (rodada {p['rodada']}, fonte {p['fonte']}) | fdb {j['data']} {j['gm']}-{j['gv']}")
            ng = len(j["gols"])
            tot["gols_fdb"] += ng; tot["gols_placar"] += j["gm"] + j["gv"]
            if ng == j["gm"] + j["gv"]: tot["jogos_gols_completos"] += 1
    tot["ok"] += ok; tot["dif"] += dif
    print(f"{a}/{str(a+1)[-2:]} rodadas {rods}: {ok + dif} jogos, {ok} iguais (data, placar, rodada), {dif} diferentes")
    for l in linhas: print(l)
print("nomes sem cadastro:", dict(sem_nome))
print(dict(tot))
