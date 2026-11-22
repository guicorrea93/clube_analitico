"""Baixa (cache) o código das páginas da Wikipédia pt de cada edição da A2: 1947-2026, com o nome de cada época."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
def nome(a):
    if a <= 1959: return "Segunda Divisão"
    if a <= 1976: return "Primeira Divisão"
    if a <= 1979: return "Divisão Intermediária"
    if a <= 1986: return "Segunda Divisão"
    if a <= 1990: return "Divisão Especial"
    if a <= 1993: return "Divisão Intermediária"
    return "Série A2"
if __name__ == "__main__":
    anos = [int(x) for x in sys.argv[1:]] or range(1947, 2027)
    for a in anos:
        t = f"Campeonato Paulista de Futebol de {a} - {nome(a)}"
        w = wikitext(t)
        if not w and a >= 1994:
            w = wikitext(f"Campeonato Paulista de Futebol de {a} - Série A2 ")
        print(a, len(w), w.count("footballbox") + w.count("Footballbox"), w.count("{{fb r") + w.count("{{Fb r"), flush=True)
