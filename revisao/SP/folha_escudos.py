"""Folha de contato dos escudos dos clubes do Paulista (HTML para print no Chrome). Uso: python -I revisao/SP/folha_escudos.py <saida.html>"""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, os, re, sys, sqlite3
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
h = open("painel/index.html", encoding="utf-8").read()
ESC = json.loads(re.search(r"const ESCUDOS = (\{.*?\});", h).group(1))
q = """with x as (select distinct e.edicao_id, e.ano_inicio, cl from (select edicao_id, mandante_id cl from partida union select edicao_id, visitante_id from partida) p join edicao e using(edicao_id) where e.competicao_id=7)
select cl.nome, cl.cidade, count(*), min(ano_inicio), max(ano_inicio) from x join clube cl on cl.clube_id=x.cl group by cl.clube_id order by count(*) desc"""
raiz = os.path.abspath("painel").replace("\\", "/")
cels, falta = [], []
for nome, cid, n, a, b in c.execute(q):
    arq = ESC.get(nome)
    if not arq: falta.append(nome)
    img = f'<img src="file:///{raiz}/{arq}">' if arq else '<div class="x">sem</div>'
    cels.append(f'<div class="c">{img}<b>{nome}</b><small>{cid or "?"} · {n} ed. {a}-{b}</small></div>')
html = """<html><head><meta charset="utf-8"><style>body{font:11px sans-serif;margin:6px;background:#fff}
.g{display:grid;grid-template-columns:repeat(10,1fr);gap:4px}.c{border:1px solid #ccc;padding:3px;text-align:center;height:118px}
img{width:64px;height:64px;object-fit:contain}.x{width:64px;height:64px;margin:auto;background:#fdd;line-height:64px}
b{display:block;font-size:11px}small{color:#555;font-size:9px}</style></head><body><div class="g">""" + "".join(cels) + "</div></body></html>"
open(sys.argv[1], "w", encoding="utf-8").write(html)
print("clubes", len(cels), "sem escudo:", falta)
