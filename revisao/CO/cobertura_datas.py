"""Seção 4 (cobertura): jogos com data no pacote x títulos de rodada com data na página da Wikipédia es que a coleta já baixou.
Uso (da raiz): python -I revisao/CO/cobertura_datas.py"""
import csv, collections, os, re
P = 'data/coleta/col-1/pacote/'
tot = collections.Counter(); com = collections.Counter()
for p in csv.DictReader(open(P + 'partidas.csv', encoding='utf-8')):
    tot[p['temporada']] += 1; com[p['temporada']] += bool(p['data'])
for t in sorted(tot):
    if t[:4] < '1995' and com[t] < tot[t]:
        f = f"data/coleta/col-1/wikipedia/es_{t}.txt"
        n = 0
        if os.path.exists(f):
            s = open(f, encoding='utf-8').read()
            n = len(re.findall(r"(?i)fecha\s*\d+[^\n]{0,40}(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)", s))
        print(t, f"{com[t]}/{tot[t]} com data; títulos de rodada com data na Wikipédia es: {n}")
