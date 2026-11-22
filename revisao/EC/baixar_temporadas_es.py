"""Baixa (com cache) as páginas de temporada da Wikipédia es, pelos links da seção Historial de 'Serie A de Ecuador'."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import re
sys.path.insert(0, "revisao/EC")
import baixar
t = baixar.wikitext("es", "Serie A de Ecuador")
a = t.index("== Historial =="); b = t.index("== Palmarés ==")
pags = []
for m in re.finditer(r"'''\[\[([^\]|]+)\|(\d{4})\]\](?:-\[\[([^\]|]+)\|[AC]\]\])?'''", t[a:b]):
    pags.append(m.group(1))
    if m.group(3): pags.append(m.group(3))
pags = list(dict.fromkeys(pags))
for p in pags:
    w = baixar.wikitext("es", p)
    print(len(w), p)
