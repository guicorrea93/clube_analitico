"""Texto visível de um DOM salvo (telas/<nome>.html): python -I revisao/RC/texto.py <nome> [trecho]"""
import re, sys, html
sys.stdout.reconfigure(encoding="utf-8")
S = r"C:\Users\GUILHE~1\AppData\Local\Temp\claude\c--Users-guilhermecorrea-Downloads-Gui-GitHub\a75361b9-f474-4b01-be59-ef64c90aa262\scratchpad\RC\telas"
t = open(S + "\\" + sys.argv[1] + ".html", encoding="utf-8", errors="replace").read()
t = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", t)
i = t.find('id="conteudo"'); t = t[i:] if i > 0 else t
t = re.sub(r"<(br|/div|/tr|/li|/h\d|/p|/section)[^>]*>", "\n", t)
t = html.unescape(re.sub(r"<[^>]+>", " ", t))
t = "\n".join(re.sub(r"[ \t]+", " ", l).strip() for l in t.splitlines())
t = re.sub(r"\n{2,}", "\n", t)
if len(sys.argv) > 2:
    for m in re.finditer(re.escape(sys.argv[2]), t):
        print(t[max(0, m.start()-300):m.start()+500].replace("\n", " | ")); print("-----")
else:
    print(t[:6000])
