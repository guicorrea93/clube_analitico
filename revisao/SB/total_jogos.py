"""Total de jogos por edição: banco x soma de J/2 da tabela final da Wikipédia pt (quando a tabela cobre todos)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabelas_wiki, compara_classificacao as cc  # noqa: E402
con = cc.con
for (t, n) in con.execute("""SELECT temporada, (SELECT count(*) FROM partida p WHERE p.edicao_id=e.edicao_id) FROM edicao e
                             WHERE competicao_id=2 ORDER BY ano_inicio"""):
    tabs = tabelas_wiki.tabelas(int(t))
    nc = con.execute("SELECT count(*) FROM classificacao_final f JOIN edicao e USING(edicao_id) WHERE competicao_id=2 AND temporada=?", (t,)).fetchone()[0]
    tb = cc.escolhe(tabs, nc) if tabs else None
    sj = sum(r.get("j") or 0 for r in tb["linhas"]) if tb else None
    print(t, "banco", n, "| wiki", (sj / 2 if sj else "-"), (tb["titulo"][:30], len(tb["linhas"])) if tb else "")
