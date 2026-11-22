"""Datas: pacote x Transfermarkt x football-data (1994/95+; o football-data a coleta baixou mas não usou para a data).
Classifica cada jogo com data diferente:
  - "pacote isolado": TM e football-data concordam entre si e discordam do pacote (erro provável do pacote);
  - "só TM": antes de 1994/95, só o TM discorda (sem segunda opinião).
Uso (na raiz): python -I revisao/PT/cmp_datas.py > SCRATCH/PT/cmp_datas.txt"""
import csv, sys, pathlib
from collections import defaultdict, Counter
from datetime import date
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.append(str(AQUI.parents[1] / "coleta" / "comum-europa"))
sys.stdout.reconfigure(encoding="utf-8")
import tm
from cmp_tm import chave
from comum import partidas, RAIZ
import clubes_por as CP

FD = RAIZ / "data" / "coleta" / "por-1" / "football-data"


def fd(a):
    arq = FD / f"P1_{str(a)[-2:]}{str(a + 1)[-2:]}.csv"
    res = {}
    if not arq.exists():
        return res
    with arq.open(encoding="utf-8-sig", errors="replace") as f:
        for x in csv.DictReader(f):
            if not x.get("HomeTeam") or not x.get("Date"):
                continue
            d, m, y = x["Date"].split("/")
            y = int(y) + (2000 if len(y) == 2 and int(y) < 50 else 1900 if len(y) == 2 else 0)
            res[(CP.esd(x["HomeTeam"], a), CP.esd(x["AwayTeam"], a))] = f"{y:04d}-{int(m):02d}-{int(d):02d}"
    return res


P = defaultdict(dict)
for j in partidas():
    P[j["a"]][(j["mandante"], j["visitante"])] = j
cont = Counter(); por_t = defaultdict(Counter)
linhas = []
for a in sorted(P):
    T = next(iter(P[a].values()))["temporada"]
    t = {}
    for x in tm.jogos(a):
        m, v = chave(x["m"], a), chave(x["v"], a)
        if m and v:
            t[(m, v)] = x["data"]
    f = fd(a)
    for k, j in P[a].items():
        dp, dt, df = j["data"], t.get(k), f.get(k)
        if dt is None:
            continue
        if df:
            cont["com_fd"] += 1
            if dp != df and dt == df:
                cont["pacote isolado"] += 1; por_t[T]["pacote isolado"] += 1
                linhas.append((T, "pacote isolado (TM = football-data)", k, dp, dt, j["rodada"]))
            elif dp != df and dp == dt:
                cont["fd isolado"] += 1
            elif dp != dt and dp == df:
                cont["TM isolado"] += 1
            elif dp != dt:
                cont["três diferentes"] += 1; linhas.append((T, "três datas diferentes (fd " + df + ")", k, dp, dt, j["rodada"]))
        elif dp != dt:
            cont["só TM (sem fd)"] += 1; por_t[T]["só TM"] += 1
            linhas.append((T, "só TM", k, dp, dt, j["rodada"]))
for T, tipo, (m, v), dp, dt, r in linhas:
    dd = (date.fromisoformat(dt) - date.fromisoformat(dp)).days
    print(f"{T}\t{tipo}\tr{r} {m} x {v}\tpacote {dp}\tTM {dt}\t{dd:+d}")
print(dict(cont), file=sys.stderr)
for T in sorted(por_t):
    print(T, dict(por_t[T]), file=sys.stderr)
