"""Rebaixados marcados x clubes que somem na edição seguinte (pacote per-1). python -I revisao/PE/rebaixados.py"""
import csv, sys
from collections import defaultdict
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
P = Path(__file__).resolve().parents[2] / "data" / "coleta" / "per-1" / "pacote"
cl = defaultdict(dict)
for r in csv.DictReader(open(P / "classificacao_final.csv", encoding="utf-8")):
    cl[int(r["temporada"])][r["clube"]] = r
part = defaultdict(set)
for r in csv.DictReader(open(P / "partidas.csv", encoding="utf-8")):
    part[int(r["temporada"])] |= {r["mandante"], r["visitante"]}
anos = sorted(cl)
for i, a in enumerate(anos[:-1]):
    b = anos[i + 1]
    if a < 1926:
        continue
    agora = set(cl[a]) | part[a]
    depois = set(cl[b]) | part[b]
    some = agora - depois
    reb = {c for c, r in cl[a].items() if r["situacao"] == "rebaixado"}
    if some != reb:
        print(f"{a}->{b}: rebaixados marcados {sorted(reb)} | somem em {b}: {sorted(some)}")
        print(f"     marcados que continuam: {sorted(reb - some)}; somem sem marca: {sorted(some - reb)}")
