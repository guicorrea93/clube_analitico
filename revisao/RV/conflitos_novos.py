"""Conflitos de data (clube com 2 jogos no mesmo dia) da Série B que não existiam na 1ª rodada: a data de algum dos jogos mudou?"""
import csv, io, subprocess, glob, os
from collections import defaultdict
def ld(t):
    r = list(csv.reader(io.StringIO(t.lstrip("﻿")), delimiter=";")); h = r[0]; return [dict(zip(h, x)) for x in r[1:]]
for a in ("1981", "1989", "1990", "1991", "1997", "1998"):
    f = f"data/serie_b/csv/serie_b_{a}_partidas.csv"
    o = ld(subprocess.run(["git", "show", "04cb286:" + f], capture_output=True).stdout.decode("utf-8")); n = ld(open(f, encoding="utf-8").read())
    def conf(js):
        d = defaultdict(list)
        for x in js:
            if x["data"]:
                for cl in (x["mandante"], x["visitante"]): d[(x["data"], cl)].append(x)
        return {k: v for k, v in d.items() if len(v) > 1}
    co, cn = conf(o), conf(n)
    oldkey = {(x["fase"], x["mandante"], x["visitante"], x["placar"]): x["data"] for x in o}
    for k, v in cn.items():
        if k in co: continue
        print(a, k, [(x["mandante"], x["placar"], x["visitante"], "antes:" + str(oldkey.get((x["fase"], x["mandante"], x["visitante"], x["placar"])))) for x in v])
