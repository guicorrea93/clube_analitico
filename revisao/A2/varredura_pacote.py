"""Varredura de coerência do pacote bra-sp-2 (ainda fora do banco): adapta revisao/tela/varredura.py e datas_repetidas.py
para ler os CSV de data/coleta/bra-sp-2/pacote/. Uso (na raiz): python -I revisao/A2/varredura_pacote.py > saida.txt"""
import csv, re, sys
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding="utf-8")
P = "data/coleta/bra-sp-2/pacote/"
L = lambda f: list(csv.DictReader(open(P + f, encoding="utf-8")))
ed = {r["temporada"]: r for r in L("edicoes.csv")}
fases = defaultdict(list)
for r in L("fases.csv"): fases[r["temporada"]].append(r)
jogos = defaultdict(list)
for r in L("partidas.csv"): jogos[r["temporada"]].append(r)
cf = defaultdict(list)
for r in L("classificacao_final.csv"): cf[r["temporada"]].append(r)
gols = defaultdict(list)
for r in L("gols.csv"): gols[r["partida_id"]].append(r)
ING = re.compile(r"\b(round|stage|phase|group|relegation|playoffs?|first|second|third|quarter|semi-?finals?)\b", re.I)
out = []
def acha(t, tipo, txt): out.append((t, tipo, txt))
for t, e in ed.items():
    js = jogos[t]; fs = sorted(fases[t], key=lambda f: int(f["ordem"]))
    pf = defaultdict(list)
    for j in js: pf[j["fase"]].append(j)
    c = cf[t]; pos = {r["clube"]: int(r["posicao"]) for r in c}
    incompleto = e["formato"].startswith(("sem jogos", "jogos incompletos")) or "incompletos" in e["formato"]
    for f in fs:
        if ING.search(f["fase"]): acha(t, "fase em inglês", f["fase"])
    for j in js:
        if ING.search(j["fase"]) or ING.search(j["grupo"] or ""): acha(t, "fase/grupo em inglês no jogo", f"{j['fase']} / {j['grupo']}"); break
    ini = []
    for f in fs:
        ds = [j["data"] for j in pf[f["fase"]] if j["data"]]
        if ds: ini.append((f["fase"], min(ds), max(ds)))
    for a, b in zip(ini, ini[1:]):
        if b[1] < a[1] and b[2] < a[2]: acha(t, "fase fora de ordem", f"'{b[0]}' ({b[1]}..{b[2]}) depois de '{a[0]}' ({a[1]}..{a[2]})")
    for f in fs:
        if f["fase"] == "Final":
            cl = {x for j in pf["Final"] for x in (j["mandante"], j["visitante"])}
            if len(pf["Final"]) > 3 or len(cl) > 2: acha(t, "Final com jogos demais", f"{len(pf['Final'])} jogos, {len(cl)} clubes")
            if cl and (e["campeao"] not in cl or e["vice"] not in cl): acha(t, "pódio x final", f"final {sorted(cl)}; campeão {e['campeao']}, vice {e['vice']}")
    # última fase em liga com 4 ou menos clubes: ordem do topo deve seguir a tabela dessa fase
    if fs:
        ult = [f for f in fs if f["fase"] not in ("Torneio de rebaixamento", "Repescagem")][-1]
        if ult["tipo"] == "liga" and pf[ult["fase"]]:
            pts = Counter(); sg = Counter(); cl = set()
            for j in pf[ult["fase"]]:
                if j["gols_mandante"] == "": continue
                m, v, gm, gv = j["mandante"], j["visitante"], int(j["gols_mandante"]), int(j["gols_visitante"])
                cl |= {m, v}; pv = int(e["pontos_vitoria"])
                pts[m] += pv if gm > gv else 1 if gm == gv else 0; pts[v] += pv if gv > gm else 1 if gm == gv else 0
                sg[m] += gm - gv; sg[v] += gv - gm
            if len(cl) <= 8:
                ordem = sorted(cl, key=lambda x: (-pts[x], -sg[x]))
                topo = [r["clube"] for r in c[:len(cl)]]
                if topo[1:] != ordem[1:] and set(topo) == set(ordem):
                    acha(t, "ordem do topo x tabela da última fase", f"'{ult['fase']}' pelos jogos: {[(x, pts[x]) for x in ordem]}; classificação: {topo}")
                elif set(topo) != set(ordem):
                    acha(t, "topo da classificação x clubes da última fase", f"'{ult['fase']}': {sorted(cl)}; topo: {topo}")
    for j in js:
        if j["mandante"] == j["visitante"]: acha(t, "clube contra ele mesmo", f"{j['mandante']} {j['data']}")
    dup = Counter((j["data"], j["mandante"], j["visitante"]) for j in js if j["data"])
    for k, n in dup.items():
        if n > 1: acha(t, "jogo repetido", f"{k} {n}x")
    dia = Counter((j["data"], x) for j in js if j["data"] for x in (j["mandante"], j["visitante"]))
    for (d, x), n in dia.items():
        if n > 1: acha(t, "clube 2 jogos no mesmo dia", f"{x} em {d}")
    for j in js:
        if j["data"] and not (str(int(t[:4]) - 1) <= j["data"][:4] <= str(int(t[:4]) + 1)): acha(t, "data fora do ano", f"{j['id']} {j['data']}")
    jogaram = {x for j in js for x in (j["mandante"], j["visitante"])}
    if jogaram - set(pos): acha(t, "jogou e não está na classificação", ", ".join(sorted(jogaram - set(pos))))
    if not incompleto and set(pos) - jogaram: acha(t, "na classificação sem jogar", ", ".join(sorted(set(pos) - jogaram)))
    if c and pos.get(e["campeao"]) != 1: acha(t, "campeão não é 1º", f"{e['campeao']} {pos.get(e['campeao'])}")
    if c and pos.get(e["vice"]) != 2: acha(t, "vice não é 2º", f"{e['vice']} {pos.get(e['vice'])}")
    ps = [int(r["posicao"]) for r in c]
    if len(set(ps)) != len(ps): acha(t, "posição repetida", str(sorted(p for p, n in Counter(ps).items() if n > 1)))
    if e["num_clubes"] and int(e["num_clubes"]) != len(c): acha(t, "num_clubes x classificação", f"{e['num_clubes']} x {len(c)}")
    for r in c:
        if r["jogos"]:
            J, V, E, D = (int(r[k] or 0) for k in ("jogos", "vitorias", "empates", "derrotas"))
            if J != V + E + D: acha(t, "J != V+E+D", r["clube"])
            pv = int(e["pontos_vitoria"])
            if r["pontos"] and int(r["pontos"]) != pv * V + E + int(r["ajuste_pontos"] or 0): acha(t, "pontos != pv*V+E+ajuste", f"{r['clube']} {r['pontos']} ({V}V {E}E aj {r['ajuste_pontos']})")
    if not incompleto:
        gp = Counter(); gc = Counter(); n = Counter()
        for j in js:
            if j["gols_mandante"] == "": continue
            gm, gv = int(j["gols_mandante"]), int(j["gols_visitante"])
            gp[j["mandante"]] += gm; gc[j["mandante"]] += gv; gp[j["visitante"]] += gv; gc[j["visitante"]] += gm
            n[j["mandante"]] += 1; n[j["visitante"]] += 1
        for r in c:
            if r["jogos"] and (int(r["jogos"]), int(r["gols_pro"]), int(r["gols_contra"])) != (n[r["clube"]], gp[r["clube"]], gc[r["clube"]]):
                acha(t, "classificação x soma dos jogos", f"{r['clube']}: J/GP/GC {r['jogos']}/{r['gols_pro']}/{r['gols_contra']} x jogos {n[r['clube']]}/{gp[r['clube']]}/{gc[r['clube']]}")
    for j in js:
        g = gols.get(j["id"], [])
        if g and j["gols_mandante"] != "":
            gm = sum(1 for x in g if x["clube"] == j["mandante"])
            gv = len(g) - gm
            if gm > int(j["gols_mandante"]) or gv > int(j["gols_visitante"]): acha(t, "gols com autor > placar", f"{j['id']} {j['mandante']} {j['gols_mandante']}x{j['gols_visitante']} {j['visitante']}")
for t, tipo, txt in out: print(f"{t}\t{tipo}\t{txt}")
print(Counter(x[1] for x in out), file=sys.stderr)
