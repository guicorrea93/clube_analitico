"""FR: varredura de coerência do pacote fra-1 (não está no painel). Uso: python -I revisao/FR/varredura_pacote.py"""
import csv
from collections import Counter, defaultdict
P = "data/coleta/fra-1/pacote/"
def ler(n): return list(csv.DictReader(open(P + n, encoding="utf-8")))
J = ler("partidas.csv"); CF = ler("classificacao_final.csv"); ED = ler("edicoes.csv"); G = ler("gols.csv")
CR = ler("classificacao_rodada.csv"); AR = ler("artilheiros.csv"); CL = ler("clubes.csv")
out = []
def acha(t, tipo, txt): out.append(f"{t}\t{tipo}\t{txt}")
por_t = defaultdict(list)
for j in J: por_t[j["temporada"]].append(j)
eds = {e["temporada"]: e for e in ED}
cft = defaultdict(list)
for x in CF: cft[x["temporada"]].append(x)
for T, js in por_t.items():
    a0 = int(T[:4])
    for j in js:
        if j["mandante"] == j["visitante"]: acha(T, "clube x ele mesmo", j["id"])
        d = j["data"]
        if d and not (f"{a0}-07-01" <= d <= f"{a0+1}-07-15"): acha(T, "data fora da temporada", f"{d} {j['mandante']} x {j['visitante']}")
    dup = Counter((j["data"], j["mandante"], j["visitante"]) for j in js if j["data"])
    for k, n in dup.items():
        if n > 1: acha(T, "jogo repetido", str(k))
    par = Counter((j["fase"], j["mandante"], j["visitante"]) for j in js)
    for k, n in par.items():
        if n > 1: acha(T, "par repetido", str(k))
    dia = Counter((j["data"], c) for j in js if j["data"] for c in (j["mandante"], j["visitante"]))
    for (d, c), n in dia.items():
        if n > 1: acha(T, "2 jogos no mesmo dia", f"{c} {d}")
    # clube com jogos em dias muito próximos (<2 dias)
    por_c = defaultdict(list)
    for j in js:
        if j["data"]:
            for c in (j["mandante"], j["visitante"]): por_c[c].append(j["data"])
    # posições
    cf = sorted(cft[T], key=lambda x: int(x["posicao"]))
    pos = [int(x["posicao"]) for x in cf]
    if pos != list(range(1, len(pos) + 1)): acha(T, "posições", str(pos))
    e = eds[T]
    if e["campeao"] and cf and cf[0]["clube"] != e["campeao"]: acha(T, "campeão fora do 1º", f"{e['campeao']} x {cf[0]['clube']}")
    if cf and e["vice"] != cf[1]["clube"]: acha(T, "vice != 2º", f"{e['vice']} x {cf[1]['clube']}")
    if int(e["num_clubes"]) != len(cf): acha(T, "num_clubes", f"{e['num_clubes']} x {len(cf)}")
    # pontos decrescentes
    for x, y in zip(cf, cf[1:]):
        if int(y["pontos"]) > int(x["pontos"]) and T != "2019/20" and T != "1932/33":
            acha(T, "pontos fora de ordem", f"{x['posicao']} {x['clube']} {x['pontos']} < {y['posicao']} {y['clube']} {y['pontos']}")
    for x in cf:
        s = int(x["vitorias"]) + int(x["empates"]) + int(x["derrotas"])
        if s != int(x["jogos"]): acha(T, "J != V+E+D", x["clube"])
    gp = sum(int(x["gols_pro"]) for x in cf); gc = sum(int(x["gols_contra"]) for x in cf)
    gj = sum(int(j["gols_mandante"]) + int(j["gols_visitante"]) for j in js)
    if gp != gc or (gp != gj and T != "1932/33"): acha(T, "gols", f"pro {gp} contra {gc} jogos {gj}")
    # rebaixados x próxima temporada
# rebaixados
temps = sorted(por_t)
clubes_t = {T: {c for j in js for c in (j["mandante"], j["visitante"])} for T, js in por_t.items()}
for i, T in enumerate(temps[:-1]):
    prox = temps[i + 1]
    reb = {x["clube"] for x in cft[T] if x["situacao"] == "rebaixado"}
    fora = clubes_t[T] - clubes_t[prox]
    if reb != fora: acha(T, "rebaixados x próxima", f"marcados {sorted(reb)} ; ausentes em {prox} {sorted(fora)}")
    novos = clubes_t[prox] - clubes_t[T]
    acha(T, "info sobe/desce", f"caem {len(fora)} {sorted(fora)} | sobem p/ {prox}: {len(novos)} {sorted(novos)}")
# gols com autor <= placar
gpj = defaultdict(Counter)
for g in G: gpj[g["partida_id"]][g["clube"]] += 1
jid = {j["id"]: j for j in J}
for pid, cn in gpj.items():
    j = jid[pid]
    if cn[j["mandante"]] > int(j["gols_mandante"]) or cn[j["visitante"]] > int(j["gols_visitante"]) or set(cn) - {j["mandante"], j["visitante"]}:
        acha(j["temporada"], "gols com autor > placar", pid)
for l in out: print(l)
