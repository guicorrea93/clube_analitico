"""Baixa (wikitext) as páginas de cada edição citadas na tabela de campeões da Wikipédia pt e en."""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
w = wikitext("Campeonato Paulista de Futebol", "pt")
i = w.find("=== Campeonato Paulista ==="); j = w.find("=== Supercampeonato")
tit = []
for t in re.findall(r"\[\[(Campeonato Paulista de Futebol de \d{4}[^]|]*)", w[i:j]):
    if t not in tit: tit.append(t)
print(len(tit), file=sys.stderr)
for t in tit:
    print(t, len(wikitext(t, "pt")), flush=True)
we = wikitext("Campeonato Paulista", "en")
i = we.find("==Champions=="); j = we.find("=== Names change")
for t in sorted(set(re.findall(r"\[\[(\d{4} Campeonato Paulista)", we[i:j]))):
    print(t, len(wikitext(t, "en")), flush=True)
