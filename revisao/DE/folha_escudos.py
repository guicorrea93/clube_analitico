"""Folha de contato dos escudos dos clubes do ger-1 (mapa ESCUDOS do painel/index.html).
Uso: python -I revisao/AR/folha_escudos.py <saida.html>  (depois, print com o Chrome)"""
import json, re, sys, sqlite3, pathlib
h = open("painel/index.html", encoding="utf-8").read()
i = h.index("const ESCUDOS ="); j = h.index("};", i)
esc = json.loads(h[i + len("const ESCUDOS ="):j + 1])
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
rows = c.execute("""select cl.nome, count(*) n, min(e.ano_inicio) from classificacao_final cf join clube cl using(clube_id) join edicao e using(edicao_id)
                    join competicao co using(competicao_id) where slug='ger-1' group by cl.clube_id order by n desc, cl.nome""").fetchall()
base = pathlib.Path("painel").resolve().as_uri()
cel = []; sem = []
for nome, n, a in rows:
    f = esc.get(nome)
    if not f: sem.append(f"{nome} ({n}, desde {a})"); continue
    cel.append(f'<div class="c"><img src="{base}/{f}"><b>{nome}</b><small>{n} ed. · {f.split("/")[-1]}</small></div>')
html = """<!doctype html><meta charset="utf-8"><style>body{font:12px sans-serif;background:#fff;margin:8px}
.g{display:grid;grid-template-columns:repeat(8,1fr);gap:6px}.c{border:1px solid #ccc;padding:4px;text-align:center}
img{width:64px;height:64px;object-fit:contain;display:block;margin:0 auto 3px}b{display:block;font-size:11px}small{color:#777;font-size:9px}</style>
<h3>ger-1: %d clubes com escudo; %d sem escudo</h3><div class="g">%s</div><p>Sem escudo: %s</p>""" % (len(cel), len(sem), "".join(cel), "; ".join(sem))
open(sys.argv[1], "w", encoding="utf-8").write(html)
print(len(cel), "com escudo;", len(sem), "sem")
