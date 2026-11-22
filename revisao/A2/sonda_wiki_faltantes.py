"""Procura na Wikipédia pt as páginas das edições da 2ª divisão paulista que o pacote não tem (1967-1978, 1980-1984)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
NOMES = {**{a: "Primeira Divisão" for a in range(1967, 1977)}, **{a: "Divisão Intermediária" for a in range(1977, 1980)},
         **{a: "Segunda Divisão" for a in range(1980, 1985)}}
ALT = ["Primeira Divisão", "Divisão Intermediária", "Segunda Divisão", "Série A2"]
for a, n in NOMES.items():
    achou = None
    for nome in [n] + [x for x in ALT if x != n]:
        t = f"Campeonato Paulista de Futebol de {a} - {nome}"
        w = wikitext(t)
        if w:
            achou = (t, len(w)); break
    print(a, achou)
