"""Resumo por temporada do esp-1 no banco: clubes, jogos, gols, campeão, vice, 3º, rebaixados, artilheiros."""
import sqlite3, json
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))
eds = c.execute("""select edicao_id, temporada, ano_inicio, num_clubes, pontos_vitoria, campeao_id, vice_id, nome_oficial, edicao.observacao
                   from edicao join competicao using(competicao_id) where slug='esp-1' order by ano_inicio""").fetchall()
for eid, t, a, n, pv, ca, vi, no, ob in eds:
    cf = c.execute("select posicao, clube_id, situacao, ajuste_pontos from classificacao_final where edicao_id=? order by posicao", (eid,)).fetchall()
    j, g = c.execute("select count(*), sum(gols_mandante+gols_visitante) from partida where edicao_id=?", (eid,)).fetchone()
    reb = [f"{nome[x]}({p})" for p, x, s, _ in cf if s == "rebaixado"]
    aj = [f"{nome[x]}:{aj}" for p, x, s, aj in cf if aj]
    art = c.execute("select jogador, clube_id, gols from artilheiro where edicao_id=?", (eid,)).fetchall()
    print(t, n, pv, j, g, "|", nome.get(ca), "/", nome.get(vi), "/", nome[cf[2][1]], "| reb:", ", ".join(reb), "| aj:", aj,
          "| art:", "; ".join(f"{p} ({nome.get(x)}) {gg}" for p, x, gg in art), "|", ob or "")
