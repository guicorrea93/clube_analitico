"""Baixa (com cache) as tabelas finais do 11v11 e o wikitext en de cada temporada."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import *
c = banco()
for eid, t, ai, af in temporadas(c):
    b = baixar(url_11v11(ai))
    w = wikitext("en", pagina_wiki(ai))
    print(t, len(b), len(w), flush=True)
