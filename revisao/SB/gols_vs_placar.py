"""Série B: soma dos gols com autor de cada lado <= placar daquele lado, em todos os jogos."""
import sqlite3, os
RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
c = sqlite3.connect("file:" + os.path.join(RAIZ, "db", "futebol.db").replace("\\", "/") + "?mode=ro", uri=True)
rows = c.execute("""
SELECT e.temporada, p.partida_id, m.nome, v.nome, p.gols_mandante, p.gols_visitante,
  (SELECT count(*) FROM gol g WHERE g.partida_id=p.partida_id AND g.clube_id=p.mandante_id),
  (SELECT count(*) FROM gol g WHERE g.partida_id=p.partida_id AND g.clube_id=p.visitante_id),
  (SELECT count(*) FROM gol g WHERE g.partida_id=p.partida_id AND g.clube_id NOT IN (p.mandante_id,p.visitante_id))
FROM partida p JOIN edicao e USING(edicao_id) JOIN clube m ON m.clube_id=p.mandante_id JOIN clube v ON v.clube_id=p.visitante_id
WHERE e.competicao_id=2""").fetchall()
n = com_gol = 0; maior = []; parcial = 0
for t, pid, m, v, gm, gv, am, av, fora in rows:
    if am + av + fora == 0:
        continue
    com_gol += 1
    if gm is None or am > gm or av > gv or fora:
        maior.append((t, pid, m, v, gm, gv, am, av, fora))
    elif am < gm or av < gv:
        parcial += 1
print("jogos:", len(rows), "com algum autor:", com_gol, "parciais (autor < placar):", parcial)
print("autor > placar ou gol de clube de fora:", len(maior))
for x in maior:
    print(x)
