"""Baixa o wikitext das páginas de temporada da es.wikipedia (Primera División de España AAAA-AA)
e a lista do Trofeo Pichichi. Cache em data/cache/revisao/ES/. Uso: python -I revisao/ES/baixar_eswiki.py"""
import json, os, sqlite3, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import baixar

API = "https://es.wikipedia.org/w/api.php?action=parse&page={}&prop=wikitext&format=json&redirects=1"

def url_pagina(titulo):
    return API.format(urllib.parse.quote(titulo.replace(" ", "_")))

def temporadas():
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    return [r[0] for r in c.execute("""select temporada from edicao join competicao using(competicao_id)
                                        where slug='esp-1' order by ano_inicio""")]

def arquivo_temporada(t):
    return baixar(url_pagina("Primera División de España " + t.replace("/", "-")))

if __name__ == "__main__":
    falhas = []
    for t in temporadas():
        a = arquivo_temporada(t)
        ok = a and "parse" in json.load(open(a, encoding="utf-8"))
        if not ok: falhas.append(t)
    for extra in ["Trofeo Pichichi", "Primera División de España", "Anexo:Máximos goleadores de la Primera División de España"]:
        print(extra, baixar(url_pagina(extra)))
    print("falhas:", falhas)
