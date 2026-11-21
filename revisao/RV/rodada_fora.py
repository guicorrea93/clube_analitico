"""Jogos com data muito longe das outras da mesma rodada (mais de 30 dias da mediana), Séries A e B."""
import sqlite3, datetime as dt, statistics
from collections import defaultdict
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
q = """select co.slug, e.temporada, f.nome, coalesce(p.grupo,''), p.rodada, p.data, m.nome, p.gols_mandante, p.gols_visitante, v.nome
from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) join fase f using(fase_id)
join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id
where co.slug in ('bra-serie-a','bra-serie-b') and p.rodada is not null and p.data is not null"""
g = defaultdict(list)
for r in c.execute(q): g[r[:5]].append(r)
n = 0
for k, js in sorted(g.items()):
    ds = [dt.date.fromisoformat(x[5]) for x in js]
    if len(ds) < 3: continue
    med = sorted(ds)[len(ds)//2]
    for x, d in zip(js, ds):
        if abs((d - med).days) > 30:
            n += 1; print(*k, "|", x[5], x[6], f"{x[7]}-{x[8]}", x[9], "| mediana", med)
print("total", n)
