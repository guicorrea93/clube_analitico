"""Folha de contato dos escudos dos clubes do esp-1 (mapa de escudos do painel/index.html). Gera um HTML; o print é feito pelo Chrome.
Uso: python -I revisao/ES/folha_escudos.py SAIDA.html"""
import json, re, sys
s = open("painel/index.html", encoding="utf-8").read()
m = re.search(r"\{\"15 de Novembro\": \"escudos/[^\n]*?\}", s)
esc = json.loads(m.group())
d = open("painel/dados/esp-1.js", encoding="utf-8").read()
d = json.loads(d[d.index("=") + 1:].strip().rstrip(";"))
clubes = sorted(d["PART"], key=lambda c: -len(d["PART"][c]))
raiz = "file:///C:/Users/guilhermecorrea/Downloads/Gui/GitHub/clube_analitico/painel/"
cel = "".join(f'<div class=c><img src="{raiz + esc[c]}" onerror="this.style.outline=\'3px solid red\'"><b>{c}</b><small>{len(d["PART"][c])} temp.</small></div>' if c in esc
              else f'<div class=c><div class=x>SEM</div><b>{c}</b></div>' for c in clubes)
open(sys.argv[1], "w", encoding="utf-8").write("<html><body style='font:12px sans-serif;background:#ddd'><style>.c{display:inline-block;width:120px;height:120px;text-align:center;margin:4px;background:#fff;vertical-align:top}.c img{width:72px;height:72px;object-fit:contain;display:block;margin:4px auto}.x{height:72px;color:red}.c b{display:block}</style>" + cel + "</body></html>")
print(len(clubes), "clubes;", sum(c in esc for c in clubes), "com escudo")
