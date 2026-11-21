"""Comum da revisão EN (eng-1): banco só leitura, temporadas, páginas das fontes."""
import sqlite3, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from baixar import baixar, wikitext

def banco():
    return sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)

def temporadas(c):
    return c.execute("""select e.edicao_id, e.temporada, e.ano_inicio, e.ano_fim from edicao e join competicao co using(competicao_id)
                        where co.slug='eng-1' order by e.ano_inicio""").fetchall()

def pagina_wiki(ai):
    s = f"{ai}–{str(ai+1)[-2:]}" if ai != 1899 else "1899–1900"
    if ai < 1992: return f"{s} Football League"
    if ai < 2007: return f"{s} FA Premier League"
    return f"{s} Premier League"

def url_11v11(ai):
    comp = "premier-league" if ai >= 1992 else "league-division-one"
    return f"https://www.11v11.com/league-tables/{comp}/31-july-{ai+1}/"
