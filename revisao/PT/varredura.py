"""Varredura do pacote por-1 (adaptada de revisao/tela/varredura.py para ler os CSVs do pacote; a competição não está no banco).
Uso (na raiz): python -I revisao/PT/varredura.py"""
import sys, pathlib, json
from collections import Counter, defaultdict
from datetime import date
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from comum import ler, partidas, ano
sys.stdout.reconfigure(encoding="utf-8")
P = partidas(); CF = ler("classificacao_final.csv"); ED = {e["temporada"]: e for e in ler("edicoes.csv")}
CR = ler("classificacao_rodada.csv"); G = ler("gols.csv"); C = ler("cartoes.csv"); ART = ler("artilheiros.csv")
out = []
def acha(t, tipo, txt): out.append((t, tipo, txt))
por_t = defaultdict(list)
for j in P: por_t[j["temporada"]].append(j)
cf_t = defaultdict(list)
for x in CF: cf_t[x["temporada"]].append(x)
gols_por = Counter((g["partida_id"], g["clube"]) for g in G)
for t, js in por_t.items():
    a = ano(t)
    for j in js:
        if j["mandante"] == j["visitante"]: acha(t, "clube contra ele mesmo", j["id"])
        if not j["data"]: acha(t, "sem data", j["id"]); continue
        d = date.fromisoformat(j["data"])
        if not (date(a, 7, 1) <= d <= date(a + 1, 7, 31)): acha(t, "data fora da temporada", f"{j['mandante']} x {j['visitante']} {j['data']}")
        gm, gv = gols_por[(j["id"], j["mandante"])], gols_por[(j["id"], j["visitante"])]
        if gm > j["gm"] or gv > j["gv"]: acha(t, "gols com autor > placar", f"{j['mandante']} {j['gm']}-{j['gv']} {j['visitante']} ({gm}-{gv})")
        if (gm or gv) and (gm, gv) != (j["gm"], j["gv"]): acha(t, "gols com autor parciais", j["id"])
    dup = Counter((j["data"], j["mandante"], j["visitante"]) for j in js)
    for k, n in dup.items():
        if n > 1: acha(t, "jogo repetido", str(k))
    pares = Counter((j["mandante"], j["visitante"]) for j in js)
    for k, n in pares.items():
        if n > 1: acha(t, "par repetido", str(k))
    dia = Counter((j["data"], c) for j in js if j["data"] for c in (j["mandante"], j["visitante"]))
    for (d, c), n in dia.items():
        if n > 1: acha(t, "clube 2 jogos no mesmo dia", f"{c} em {d} ({n})")
    # dias consecutivos para o mesmo clube
    por_clube = defaultdict(list)
    for j in js:
        for c in (j["mandante"], j["visitante"]): por_clube[c].append((j["data"], j["rodada"]))
    for c, l in por_clube.items():
        l.sort()
        for (d1, r1), (d2, r2) in zip(l, l[1:]):
            if (date.fromisoformat(d2) - date.fromisoformat(d1)).days == 1: acha(t, "clube com jogos em dias seguidos", f"{c} {d1} (r{r1}) e {d2} (r{r2})")
    # rodada x data: jogos de uma rodada muito longe da mediana da rodada
    rod = defaultdict(list)
    for j in js: rod[int(j["rodada"])].append(j)
    for r, l in rod.items():
        ds = sorted(date.fromisoformat(j["data"]) for j in l); med = ds[len(ds)//2]
        for j in l:
            dd = (date.fromisoformat(j["data"]) - med).days
            if abs(dd) > 21: acha(t, "jogo longe da data da rodada", f"r{r} {j['mandante']} x {j['visitante']} {j['data']} (mediana {med}, {dd:+d} dias)")
    # clubes x classificação
    cl = cf_t[t]
    jog = {c for j in js for c in (j["mandante"], j["visitante"])}
    noc = {x["clube"] for x in cl}
    if jog != noc: acha(t, "jogou x classificação", str(jog ^ noc))
    ps = [int(x["posicao"]) for x in cl]
    if sorted(ps) != list(range(1, len(ps) + 1)): acha(t, "posições", str(ps))
    camp = [x["clube"] for x in cl if x["situacao"] == "campeao"]
    if camp != [cl[0]["clube"]] or ED[t]["campeao"] != cl[0]["clube"] or ED[t]["vice"] != cl[1]["clube"]: acha(t, "campeão/vice", f"{camp} {ED[t]['campeao']} {ED[t]['vice']}")
    # pontos decrescentes na classificação
    pts = [int(x["pontos"]) for x in cl]
    for i in range(len(pts) - 1):
        if pts[i] < pts[i + 1]: acha(t, "pontos fora de ordem", f"{cl[i]['clube']} {pts[i]} acima de {cl[i+1]['clube']} {pts[i+1]}")
    # n de clubes e jogos
    n = len(cl)
    if int(ED[t]["num_clubes"]) != n or len(js) != n * (n - 1): acha(t, "num clubes/jogos", f"{ED[t]['num_clubes']} {n} {len(js)}")
    # J,V,E,D somam
    for x in cl:
        J, V, E, D = (int(x[k]) for k in ("jogos", "vitorias", "empates", "derrotas"))
        pv = int(ED[t]["pontos_vitoria"])
        if J != V + E + D or int(x["pontos"]) != pv * V + E + int(x["ajuste_pontos"] or 0): acha(t, "linha da classificação", str(x))
    # rodada final x classificação final
    ult = max(int(x["rodada"]) for x in CR if x["temporada"] == t)
    fin = {x["clube"]: x for x in CR if x["temporada"] == t and int(x["rodada"]) == ult}
    for x in cl:
        f = fin.get(x["clube"])
        if not f or int(f["pontos"]) != int(x["pontos"]) or int(f["posicao"]) != int(x["posicao"]):
            acha(t, "última rodada x classificação final", f"{x['clube']}: final {x['posicao']}º {x['pontos']} pts; rodada {ult}: {f and (f['posicao'], f['pontos'])}")
# artilheiros
ta = Counter(x["temporada"] for x in ART)
for t in por_t:
    if ta[t] == 0: acha(t, "sem artilheiro", "")
for x in ART:
    if not x["clube"]: acha(x["temporada"], "artilheiro sem clube", x["jogador"])
for t, tipo, txt in sorted(out):
    print(f"{t}\t{tipo}\t{txt}")
print(Counter(tipo for _, tipo, _ in out), file=sys.stderr)
