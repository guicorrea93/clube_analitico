"""Jogos com data impossível: o mesmo clube com 2+ jogos na mesma data. Lista por competição e edição."""
import sqlite3
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
q = """with x as (select p.partida_id, p.edicao_id, p.data, p.mandante_id cl from partida p where data is not null
               union all select p.partida_id, p.edicao_id, p.data, p.visitante_id from partida p where data is not null),
     d as (select edicao_id, data, cl from x group by 1,2,3 having count(*)>1)
select co.slug, e.temporada, count(distinct x.partida_id), min(cn.nome||' em '||x.data)
from x join d using(edicao_id, data, cl) join edicao e using(edicao_id) join competicao co using(competicao_id) join clube cn on cn.clube_id=x.cl
where co.slug = 'arg-1' group by 1,2 order by 1,2"""
for r in c.execute(q): print(*r, sep="\t")
