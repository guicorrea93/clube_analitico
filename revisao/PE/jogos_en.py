"""Placares do pacote per-1 nos anos em que a FONTE foi a Wikipédia es (1926-1929, 1943-1967, 1982, 1985) x as páginas da
temporada na Wikipédia em inglês (match_X_Y), como segunda opinião. Uso (raiz): python -I revisao/PE/jogos_en.py"""
import csv, json, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from jogos_es import clubes_pacote, resolve, jogos_es, FONTE_WIKI  # noqa: E402
R = Path(__file__).resolve().parents[2]
C = R / "data/cache/revisao/PE"; P = R / "data/coleta/per-1/pacote"
sys.stdout.reconfigure(encoding="utf-8")
mapa = clubes_pacote()
por = defaultdict(lambda: defaultdict(list)); cl = defaultdict(set)
for r in csv.DictReader(open(P / "partidas.csv", encoding="utf-8")):
    if r["gols_mandante"] == "": continue
    y = int(r["temporada"]); por[y][(r["mandante"], r["visitante"])].append(r); cl[y] |= {r["mandante"], r["visitante"]}
saida = []; tot = [0, 0, 0]
for y in sorted(FONTE_WIKI):
    f = C / f"en_temporada_{y}.json"
    if not f.exists(): continue
    d = json.loads(f.read_text(encoding="utf-8"))
    if "parse" not in d: continue
    n = ok = sp = 0
    for a0, b0, p, o in jogos_es(d["parse"]["wikitext"]):
        a, b = resolve(a0, mapa, cl[y]), resolve(b0, mapa, cl[y])
        if not a or not b or a == b: continue
        n += 1; js = por[y].get((a, b), [])
        if not js: sp += 1; saida.append(f"{y} SEM JOGO: {a} x {b} {p}"); continue
        if any((int(j["gols_mandante"]), int(j["gols_visitante"])) == p for j in js): ok += 1
        else: saida.append(f"{y} PLACAR: en {a} {p[0]}-{p[1]} {b} | pacote " + "; ".join(f"{j['gols_mandante']}-{j['gols_visitante']}" for j in js))
    print(y, n, ok, sp); tot = [tot[0] + n, tot[1] + ok, tot[2] + sp]
print("TOTAL", tot)
(Path(__file__).parent / "jogos_en_saida.txt").write_text("\n".join(saida), encoding="utf-8")
