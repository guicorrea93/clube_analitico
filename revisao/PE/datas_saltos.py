"""Datas fora do lugar: jogo com data a mais de 60 dias da mediana da sua rodada (mesma fase), e fases inteiras cujas datas
ficam antes da primeira fase da temporada (sinal de ano trocado, ex.: janeiro do ano seguinte gravado no ano da edição).
python -I revisao/PE/datas_saltos.py"""
import csv, sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from statistics import median_low
sys.stdout.reconfigure(encoding="utf-8")
R = Path(__file__).resolve().parents[2] / "data/coleta/per-1/pacote"
ordem = {(r["temporada"], r["fase"]): int(r["ordem"]) for r in csv.DictReader(open(R / "fases.csv", encoding="utf-8"))}
por = defaultdict(list); fase_d = defaultdict(list)
for r in csv.DictReader(open(R / "partidas.csv", encoding="utf-8")):
    if r["data"]:
        d = date.fromisoformat(r["data"])
        por[(r["temporada"], r["fase"], r["grupo"], r["rodada"])].append((d, r))
        fase_d[(r["temporada"], r["fase"])].append(d)
n = 0
for k, js in sorted(por.items()):
    m = median_low([d for d, _ in js])
    for d, r in js:
        if abs((d - m).days) > 60:
            n += 1
            print("RODADA", k, r["data"], "mediana", m, r["mandante"], r["gols_mandante"], "x", r["gols_visitante"], r["visitante"], r["fonte_id"].split()[0])
print("jogos longe da rodada:", n)
for t in sorted({k[0] for k in fase_d}):
    fs = sorted([(ordem[(t, f)], f, min(ds), max(ds)) for (tt, f), ds in fase_d.items() if tt == t])
    for a, b in zip(fs, fs[1:]):
        if b[2] < a[2] and (a[2] - b[2]).days > 120:
            print("FASE", t, f"'{b[1]}' {b[2]}..{b[3]} antes de '{a[1]}' {a[2]}..{a[3]}")
