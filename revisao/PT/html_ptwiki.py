"""Baixa o HTML (API parse) das 92 páginas de temporada da Wikipédia pt."""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import baixar
T = json.load(open(pathlib.Path(__file__).with_name("ptwiki_titulos.json"), encoding="utf-8"))
for a, t in T.items():
    h = baixar.html_wiki("pt", t)
    print(a, len(h), flush=True)
