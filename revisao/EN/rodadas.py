"""Rodadas do eng-1: temporadas em que um clube tem 2+ jogos na mesma rodada ou a rodada tem mais de n/2 jogos."""
import sqlite3
from collections import Counter
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nm = dict(c.execute("select clube_id,nome from clube"))
print("temporada\trodadas\tmaior_rodada(jogos)\tclube_rodada_repetidos\texemplo")
for t, eid, n in c.execute("select temporada,edicao_id,num_clubes from edicao where competicao_id=8 order by ano_inicio").fetchall():
    js = c.execute("select rodada,mandante_id,visitante_id,data from partida where edicao_id=? order by data", (eid,)).fetchall()
    cnt = Counter(j[0] for j in js)
    per = Counter((j[0], x) for j in js for x in j[1:3])
    dup = [(r, x) for (r, x), v in per.items() if v > 1]
    if max(cnt.values()) > n // 2 or dup:
        r, x = dup[0] if dup else (None, None)
        ex = [f"{nm[j[1]]} x {nm[j[2]]} ({j[3]})" for j in js if j[0] == r and x in j[1:3]] if dup else []
        print(f"{t}\t{len(cnt)}\t{max(cnt.values())}\t{len(dup)}\trodada {r}: " + "; ".join(ex))
