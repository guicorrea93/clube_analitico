"""Prova pelo dia da semana: jogos de liga caem quase sempre no fim de semana (domingo na era amadora).
Para cada edição, compara a parte de cada ano civil: % de jogos em sábado/domingo com a data como está e com o ano trocado (-1, -2).
Só leitura do futebol.db."""
import sqlite3, datetime as dt
from collections import defaultdict
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
eds = c.execute("""select e.edicao_id, e.temporada from edicao e join competicao co using(competicao_id)
                   where co.slug='arg-1' order by e.ano_inicio, e.edicao_id""").fetchall()
def fds(d):
    return d.weekday() >= 5
def troca(d, k):
    try: return d.replace(year=d.year + k)
    except ValueError: return None
for eid, temp in eds:
    grupos = defaultdict(list)
    for (d,) in c.execute("select data from partida where edicao_id=? and data is not null and coalesce(resultado_especial,'') not in ('wo','n/p')", (eid,)):
        try: grupos[d[:4]].append(dt.date.fromisoformat(d))
        except ValueError: print(f"{temp}	DATA INVÁLIDA {d}")
    for ano, ds in sorted(grupos.items()):
        if len(ds) < 8: continue
        p0 = sum(fds(d) for d in ds) / len(ds)
        alt = {}
        for k in (-1, -2):
            dd = [troca(d, k) for d in ds]; dd = [d for d in dd if d]
            alt[k] = sum(fds(d) for d in dd) / len(dd)
        marca = "  <== SUSPEITO" if max(alt.values()) - p0 > 0.35 else ""
        print(f"{temp}\t{ano}\t{len(ds)} jogos\tfim de semana: como está {p0:.0%} | ano-1 {alt[-1]:.0%} | ano-2 {alt[-2]:.0%}{marca}")
