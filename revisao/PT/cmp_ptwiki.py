"""Pacote por-1 x Wikipédia pt: classificação final (ordem e números) e matriz de resultados (placar jogo a jogo).
Uso (na raiz): python -I revisao/PT/cmp_ptwiki.py > SCRATCH/PT/cmp_ptwiki.txt"""
import sys, pathlib
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8")
import ptw
from comum import ler, partidas
CF = defaultdict(list)
for x in ler("classificacao_final.csv"):
    CF[int(x["temporada"][:4])].append(x)
JG = defaultdict(dict)
for j in partidas():
    JG[j["a"]][(j["mandante"], j["visitante"])] = j
tot = {"tab": 0, "tab_ok": 0, "ordem_ok": 0, "jogos": 0, "jogos_ok": 0}
for a in sorted(CF):
    n = len(CF[a]); T = CF[a][0]["temporada"]
    url = "https://pt.wikipedia.org/wiki/" + ptw.TIT[a].replace(" ", "_")
    c = ptw.classificacao(a, n)
    if c:
        tot["tab"] += 1
        meu = {x["clube"]: x for x in CF[a]}
        difs = []
        for d in c:
            x = meu.get(d["clube"])
            if not x:
                difs.append(f"clube só na pt: {d['clube']}"); continue
            m = [int(x[k]) for k in ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "pontos")]
            w = [d[k] for k in ("j", "v", "e", "d", "gp", "gc", "pts")]
            if m != w:
                difs.append(f"{d['clube']}: pacote {m} pt {w}")
        ordem_pt = [d["clube"] for d in c]
        ordem_pac = [x["clube"] for x in CF[a]]
        if not difs:
            tot["tab_ok"] += 1
        if ordem_pt == ordem_pac:
            tot["ordem_ok"] += 1
        else:
            dif = [(i + 1, p, w) for i, (p, w) in enumerate(zip(ordem_pac, ordem_pt)) if p != w]
            print(f"{T}\tORDEM\t{dif}\t{url}")
        for d in difs:
            print(f"{T}\tTABELA\t{d}\t{url}")
    else:
        print(f"{T}\tSEM TABELA LEGÍVEL\t\t{url}")
    m = ptw.matriz(a, n)
    if m:
        for (h, v), (g1, g2) in m.items():
            j = JG[a].get((h, v))
            tot["jogos"] += 1
            if not j:
                print(f"{T}\tJOGO SEM PAR\t{h} x {v} {g1}-{g2}\t{url}"); continue
            if (j["gm"], j["gv"]) == (g1, g2):
                tot["jogos_ok"] += 1
            else:
                print(f"{T}\tPLACAR\t{h} x {v} ({j['data']}): pacote {j['gm']}-{j['gv']}, pt {g1}-{g2}{' [' + j['resultado_especial'] + ']' if j['resultado_especial'] else ''}\t{url}")
print(tot, file=sys.stderr)
