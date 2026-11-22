"""Compara pacote (data/coleta/chi-1/pacote) x banco (db/futebol.db) x painel (painel/dados/chi-1.js), edição a edição:
campeão, vice, jogos, gols e classificação final (posição, J, V, E, D, GP, GC). Uso: python -I revisao/CH/tres_vias.py"""
import csv, json, sqlite3
from collections import defaultdict
PK = "data/coleta/chi-1/pacote/"
ed = {r["temporada"]: r for r in csv.DictReader(open(PK + "edicoes.csv", encoding="utf-8"))}
pj = defaultdict(lambda: [0, 0])
for r in csv.DictReader(open(PK + "partidas.csv", encoding="utf-8")):
    pj[r["temporada"]][0] += 1
    if r["gols_mandante"]:
        pj[r["temporada"]][1] += int(r["gols_mandante"]) + int(r["gols_visitante"])
pc = defaultdict(list)
for r in csv.DictReader(open(PK + "classificacao_final.csv", encoding="utf-8")):
    pc[r["temporada"]].append((int(r["posicao"]), r["clube"], *[int(r[k]) for k in ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra")]))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))
bd = {}
for eid, t, ca, vi in c.execute("select edicao_id, temporada, campeao_id, vice_id from edicao join competicao using(competicao_id) where slug='chi-1'"):
    nj, g = c.execute("select count(*), sum(coalesce(gols_mandante,0)+coalesce(gols_visitante,0)) from partida where edicao_id=?", (eid,)).fetchone()
    cl = [(p, nome[k], j, v, e, d, gp, gc) for p, k, j, v, e, d, gp, gc in c.execute(
        "select posicao, clube_id, jogos, vitorias, empates, derrotas, gols_pro, gols_contra from classificacao_final where edicao_id=? order by posicao", (eid,))]
    bd[t] = (nome.get(ca), nome.get(vi), nj, g, cl)
s = open("painel/dados/chi-1.js", encoding="utf-8").read()
D = json.loads(s[s.index("=") + 1:].strip().rstrip(";"))
pn = {}
for e in D["EDS"]:
    pn[e["id"]] = e
edp = {}
for e in D["ED"]:
    k = str(e["ano"]) + ((" " + e["t"]) if e.get("t") else "")
    edp[k] = e
prob = 0
print("ids no painel (EDS) que não estão no pacote:", sorted(set(pn) - set(ed)))
print("temporadas do pacote sem EDS no painel:", sorted(set(ed) - set(pn)))
for t, r in ed.items():
    b = bd.get(t)
    if not b:
        print(t, "FALTA NO BANCO"); prob += 1; continue
    msgs = []
    if (r["campeao"], r["vice"]) != b[:2]:
        msgs.append(f"campeão/vice pacote {r['campeao']}/{r['vice']} banco {b[0]}/{b[1]}")
    if pj[t][0] != b[2] or pj[t][1] != (b[3] or 0):
        msgs.append(f"jogos/gols pacote {pj[t]} banco {b[2]}/{b[3]}")
    pcl = sorted(pc[t]); bcl = sorted(b[4])
    if pcl != bcl:
        msgs.append(f"classificação difere ({len(pcl)} x {len(bcl)} linhas)")
    e = pn.get(t)
    if e:
        if e["j"] != b[2] or e["g"] != b[3]:
            msgs.append(f"painel j/g {e['j']}/{e['g']} banco {b[2]}/{b[3]}")
        tab = sorted((x[1], x[0], *x[2:8]) for x in e["tab"])
        if tab != sorted((x[0], x[1], *x[2:8]) for x in bcl):
            msgs.append("tabela do painel difere do banco")
    if msgs:
        prob += 1
        print(t, "|", "; ".join(msgs))
print("edições com diferença:", prob, "de", len(ed))
