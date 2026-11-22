"""Datas do pacote (base engsoccerdata) x football-data.co.uk (1993/94-2025/26), todos os jogos, pelo par de clubes.
Uso: python -I revisao/DE/datas_fd.py > revisao/DE/datas_fd_saida.txt"""
import csv, sys, pathlib
from collections import defaultdict, Counter
RAIZ = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "coleta" / "comum-europa"))
import clubes_ger as cg  # noqa
sys.stdout.reconfigure(encoding="utf-8")
PAC = RAIZ / "data" / "coleta" / "ger-1" / "pacote"
jogos = defaultdict(dict)
for r in csv.DictReader(open(PAC / "partidas.csv", encoding="utf-8")):
    jogos[int(r["temporada"][:4])][(r["mandante"], r["visitante"])] = r
def dfd(s):
    d, m, y = s.split("/"); y = int(y); y += 2000 if y < 50 else 1900 if y < 100 else 0
    return f"{y:04d}-{int(m):02d}-{int(d):02d}"
tot = Counter()
for a in range(1993, 2026):
    arq = RAIZ / "data" / "coleta" / "ger-1" / "football-data" / f"D1_{str(a)[-2:]}{str(a+1)[-2:]}.csv"
    dif = []
    for x in csv.DictReader(open(arq, encoding="utf-8-sig", errors="replace")):
        if not x.get("HomeTeam"): continue
        m, v = cg.exibicao(cg.esd(x["HomeTeam"], a)), cg.exibicao(cg.esd(x["AwayTeam"], a))
        j = jogos[a].get((m, v))
        if not j: dif.append(f"sem par: {m} x {v}"); continue
        tot["n"] += 1
        d = dfd(x["Date"])
        if d != j["data"]:
            dif.append(f"{m} x {v}: pacote {j['data']} | football-data {d} (fonte pacote: {j['fonte']})")
        if (int(x["FTHG"]), int(x["FTAG"])) != (int(j["gols_mandante"]), int(j["gols_visitante"])):
            dif.append(f"PLACAR {m} x {v}: pacote {j['gols_mandante']}-{j['gols_visitante']} | fd {x['FTHG']}-{x['FTAG']}")
    tot["dif"] += len(dif)
    print(f"{a}/{str(a+1)[-2:]}: {len(dif)} diferenças")
    for d in dif: print("   ", d)
print(dict(tot))
