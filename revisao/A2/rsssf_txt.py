"""Mostra o texto de uma página da RSSSF guardada pela coleta. Uso: python -I revisao/A2/rsssf_txt.py 1979 [regex] [contexto]"""
import sys, re, html
sys.stdout.reconfigure(encoding="utf-8")
a = sys.argv[1]
t = open(f"data/coleta/bra-sp-2/rsssfbrasil/sp{a}l2.htm" if a.isdigit() else f"data/coleta/bra-sp-2/rsssfbrasil/{a}", "rb").read().decode("latin-1")
t = html.unescape(re.sub(r"<[^>]+>", "", t))
if len(sys.argv) > 2:
    ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 600
    for m in re.finditer(sys.argv[2], t):
        print("-----", m.start()); print(t[max(0, m.start()-100): m.start()+ctx])
else:
    print(t)
