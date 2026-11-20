"""Série B: jogos possivelmente duplicados (mesmo par de clubes no mesmo dia, ou mesmo jogo repetido na mesma fase)."""
import os, sqlite3
RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
c = sqlite3.connect("file:" + os.path.join(RAIZ, "db", "futebol.db").replace("\\", "/") + "?mode=ro", uri=True)
q = """SELECT e.temporada, f.nome, p.data, m.nome, p.gols_mandante, p.gols_visitante, v.nome, p.partida_id,
              min(p.mandante_id, p.visitante_id) a, max(p.mandante_id, p.visitante_id) b
       FROM partida p JOIN edicao e USING(edicao_id) JOIN fase f USING(fase_id)
       JOIN clube m ON m.clube_id=p.mandante_id JOIN clube v ON v.clube_id=p.visitante_id WHERE e.competicao_id=2"""
rows = c.execute(q).fetchall()
from collections import defaultdict
por_dia = defaultdict(list); por_fase = defaultdict(list)
for r in rows:
    por_dia[(r[0], r[2], r[8], r[9])].append(r)
    por_fase[(r[0], r[1], r[3], r[6], r[4], r[5])].append(r)
print("Mesmo par de clubes no mesmo dia:")
for k, v in sorted(por_dia.items(), key=lambda kv: str(kv[0])):
    if len(v) > 1 and k[1]:
        print(" ", k[0], k[1], [(x[1], f"{x[3]} {x[4]}-{x[5]} {x[6]}") for x in v])
print("Mesmo jogo (mando e placar) repetido na mesma fase de mata-mata/final:")
for k, v in sorted(por_fase.items(), key=lambda kv: str(kv[0])):
    if len(v) > 1 and any(w in k[1].lower() for w in ("final", "semi", "quartas", "mata")):
        print(" ", k[0], k[1], [(x[2], f"{x[3]} {x[4]}-{x[5]} {x[6]}") for x in v])
