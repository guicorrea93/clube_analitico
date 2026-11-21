"""Números do painel (painel/dados/eng-1.js) x banco: pódio, jogos e gols por edição, totais por clube (VIT), participações, tabela."""
import sys, json, pathlib
from collections import defaultdict, Counter
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas
c = banco()
nm = dict(c.execute("select clube_id, nome from clube"))
d = json.loads(open("painel/dados/eng-1.js", encoding="utf-8").read().split("=", 1)[1].strip().rstrip(";"))
ED = {e["t"]: e for e in d["ED"]}; EDS = {e["t"]: e for e in d["EDS"]}
prob = []
vit = defaultdict(lambda: [0] * 6)
part = Counter()
for eid, t, ai, af in temporadas(c):
    cf = c.execute("select clube_id, posicao from classificacao_final where edicao_id=? order by posicao", (eid,)).fetchall()
    pod = [nm[x[0]] for x in cf[:3]]
    e = ED.get(t)
    if not e: prob.append(f"{t} falta no ED"); continue
    if [e["campeao"], e["vice"], e["terceiro"]] != pod: prob.append(f"{t} pódio painel {[e['campeao'], e['vice'], e['terceiro']]} banco {pod}")
    js = c.execute("select mandante_id, visitante_id, gols_mandante, gols_visitante from partida where edicao_id=?", (eid,)).fetchall()
    s = EDS[t]
    if s["j"] != len(js) or s["g"] != sum(j[2] + j[3] for j in js): prob.append(f"{t} jogos/gols painel {s['j']}/{s['g']} banco {len(js)}/{sum(j[2]+j[3] for j in js)}")
    if s["pv"] != c.execute("select pontos_vitoria from edicao where edicao_id=?", (eid,)).fetchone()[0]: prob.append(f"{t} pv")
    # maior goleada da edição
    mx = max(js, key=lambda j: (abs(j[2] - j[3]), j[2] + j[3]))
    g = s["gol"]
    if abs(g["gm"] - g["gv"]) != abs(mx[2] - mx[3]): prob.append(f"{t} goleada painel {g} banco {nm[mx[0]]} {mx[2]}x{mx[3]} {nm[mx[1]]}")
    for m, v, gm, gv in js:
        for x, gp, gc in ((m, gm, gv), (v, gv, gm)):
            r = vit[nm[x]]; r[0] += 1; r[4] += gp; r[5] += gc
            r[1 if gp > gc else 2 if gp == gc else 3] += 1
    for x, _ in cf: part[nm[x]] += 1
for row in d["VIT"]:
    n = row[0]
    if list(row[1:]) != vit[n]: prob.append(f"VIT {n} painel {row[1:]} banco {vit[n]}")
for n, lst in d["PART"].items():
    if len(lst) != part[n]: prob.append(f"PART {n} painel {len(lst)} banco {part[n]}")
print("\n".join(prob) or "tudo igual")
print("clubes VIT", len(d["VIT"]), "PART", len(d["PART"]))
