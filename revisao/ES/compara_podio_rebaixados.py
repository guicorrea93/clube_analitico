"""Campeão, vice, 3º e rebaixados: banco x ficha da es.wikipedia (campeón, subcampeón, tercero, descendidos)."""
import re, sqlite3, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eswiki import *
from compara_classificacao import clube
sys.stdout.reconfigure(encoding="utf-8")
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
for t in temporadas():
    ti, w = wikitext(t)
    f = ficha(w)
    rows = c.execute("""select cl.nome,f.posicao,f.situacao from classificacao_final f join edicao x using(edicao_id)
        join competicao k using(competicao_id) join clube cl using(clube_id) where k.slug='esp-1' and x.temporada=? order by posicao""", (t,)).fetchall()
    top = [r[0] for r in rows[:3]]
    wtop = [clube((links(f.get(k, "")) or ["-"])[0]) for k in ("campeón", "subcampeón", "tercero")]
    if wtop[0].startswith("?"): wtop = [clube((links(f.get(k, "")) or ["-"])[0]) for k in ("primero", "segundo", "tercero")]
    reb = sorted(r[0] for r in rows if r[2] == "rebaixado")
    desc = f.get("descendidos", "")
    wreb = sorted(clube(x) for x in links(desc) if not x.lower().startswith(("segunda", "anexo")))
    flag = []
    if top != wtop: flag.append(f"PÓDIO banco {top} wiki {wtop}")
    if reb != wreb: flag.append(f"REBAIXADOS banco {reb} wiki {wreb} [{re.sub(r'\s+',' ',desc)[:160]}]")
    print(t, "ok" if not flag else " | ".join(flag))
