"""Revisão Série C (SC): pacote x banco x painel (campeão, vice, 3º, classificação, jogos, gols com autor)."""
import sys
from collections import Counter, defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from comum import banco_dados, ler_csv, painel  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
P = painel()
B = banco_dados()
ed = {int(r["temporada"]): r for r in ler_csv("edicoes.csv")}
cf = defaultdict(list)
for r in ler_csv("classificacao_final.csv"):
    cf[int(r["temporada"])].append(r)
pt = defaultdict(list)
for r in ler_csv("partidas.csv"):
    pt[int(r["temporada"])].append(r)
gl = defaultdict(list)
for r in ler_csv("gols.csv"):
    gl[r["partida_id"]].append(r)

print("anos pacote", sorted(ed))
print("anos banco ", sorted(B))
print("anos painel", [e["ano"] for e in P["ED"]])
print()
print("ano  | pacote camp/vice/3º | banco camp/vice | painel camp/vice/3º")
for e in P["ED"]:
    a = e["ano"]
    c3 = sorted(cf[a], key=lambda r: int(r["posicao"]))
    pac = (ed[a]["campeao"], ed[a]["vice"], c3[2]["clube"])
    ban = (B[a]["campeao"], B[a]["vice"], B[a]["classif"][2][1])
    pai = (e["campeao"], e["vice"], e["terceiro"])
    flag = "" if pac == pai and pac[:2] == ban[:2] and ban[2] == pai[2] else "  <-- DIFERE"
    print(a, pac, ban, pai, flag)

print("\n# total de jogos")
tot = [0, 0, 0]
for e in P["EDS"]:
    a = e["ano"]
    n = (len(pt[a]), len(B[a]["partidas"]), len(e["jogos"]), e["j"])
    tot[0] += n[0]; tot[1] += n[1]; tot[2] += n[2]
    if len(set(n)) > 1:
        print(a, "pacote", n[0], "banco", n[1], "painel jogos", n[2], "painel j", n[3])
print("total pacote/banco/painel", tot)

print("\n# classificação: pacote x banco x painel")
for e in P["EDS"]:
    a = e["ano"]
    pk = [(int(r["posicao"]), r["clube"], int(r["jogos"]), int(r["vitorias"]), int(r["empates"]), int(r["derrotas"]),
           int(r["gols_pro"]), int(r["gols_contra"])) for r in sorted(cf[a], key=lambda r: int(r["posicao"]))]
    bk = [(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]) for x in B[a]["classif"]]
    tk = [(r[1], r[0], r[2], r[3], r[4], r[5], r[6], r[7]) for r in e["tab"]]
    if pk != bk:
        print(a, "pacote != banco", [x for x in pk if x not in bk][:5], [x for x in bk if x not in pk][:5])
    if bk != tk:
        print(a, "banco != painel", [x for x in bk if x not in tk][:5], [x for x in tk if x not in bk][:5])

print("\n# classificação x soma dos jogos (pacote)")
for a in sorted(pt):
    s = defaultdict(lambda: [0, 0, 0, 0, 0, 0])
    for r in pt[a]:
        if r["gols_mandante"] == "":
            continue
        gm, gv = int(r["gols_mandante"]), int(r["gols_visitante"])
        for c, x, y in ((r["mandante"], gm, gv), (r["visitante"], gv, gm)):
            t = s[c]; t[0] += 1; t[4] += x; t[5] += y
            t[1 if x > y else 2 if x == y else 3] += 1
    for r in cf[a]:
        k = [int(r[f]) for f in ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra")]
        if s[r["clube"]] != k:
            print(a, r["clube"], "classif", k, "jogos", s[r["clube"]])
    falt = set(s) - {r["clube"] for r in cf[a]}
    if falt:
        print(a, "clubes nos jogos sem classificação", falt)

print("\n# gols com autor > placar (pacote)")
ruim = 0
for a in sorted(pt):
    for r in pt[a]:
        g = gl.get(r["id"], [])
        if not g or r["gols_mandante"] == "":
            continue
        cm = sum(1 for x in g if x["clube"] == r["mandante"])
        cv = sum(1 for x in g if x["clube"] == r["visitante"])
        outros = [x for x in g if x["clube"] not in (r["mandante"], r["visitante"])]
        if cm > int(r["gols_mandante"]) or cv > int(r["gols_visitante"]) or outros:
            ruim += 1
            print(a, r["id"], r["mandante"], r["gols_mandante"], "x", r["gols_visitante"], r["visitante"], "autores", cm, cv, outros[:2])
print("jogos com autor > placar:", ruim)
print("\n# gols com autor > placar (banco)")
ruim = 0
for a, e in B.items():
    for p in e["partidas"]:
        cm = sum(1 for x in p["gols"] if x[0] == p["m"]); cv = sum(1 for x in p["gols"] if x[0] == p["v"])
        if p["gm"] is not None and (cm > p["gm"] or cv > p["gv"] or cm + cv < len(p["gols"])):
            ruim += 1; print(a, p)
print("banco:", ruim)
