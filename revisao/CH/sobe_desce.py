"""Rebaixados marcados x participação na temporada seguinte (pacote do chi-1).
- marcado 'rebaixado' mas joga a 1ª divisão no ano seguinte: suspeito;
- jogou no ano e não joga no seguinte, sem marca: queda (ou saída) sem registro.
Uso: python -I revisao/CH/sobe_desce.py"""
import csv
from collections import defaultdict, OrderedDict
PK = "data/coleta/chi-1/pacote/"
ed = [r["temporada"] for r in csv.DictReader(open(PK + "edicoes.csv", encoding="utf-8"))]
cl = defaultdict(set); reb = defaultdict(set)
for r in csv.DictReader(open(PK + "classificacao_final.csv", encoding="utf-8")):
    cl[r["temporada"]].add(r["clube"])
    if r["situacao"] == "rebaixado": reb[r["temporada"]].add(r["clube"])
# só a última edição de cada ano civil "fecha" o ano (Apertura/Clausura: compara Clausura com o próximo)
anos = OrderedDict()
for t in ed:
    anos.setdefault(t[:4] if "/" not in t else t[:4], []).append(t)
seq = []
for a, ts in anos.items():
    seq.append((a, set().union(*[cl[t] for t in ts]), set().union(*[reb[t] for t in ts]), ts))
tot_sem = 0
for (a, c, r, ts), (b, c2, _, _) in zip(seq, seq[1:]):
    errado = sorted(r & c2)
    sem = sorted((c - c2) - r)
    tot_sem += len(sem)
    if errado or sem:
        print(f"{a} ({'/'.join(ts)}): marcados e seguem em {b}: {errado} | saíram sem marca: {sem}")
print("total saídas sem marca:", tot_sem)
