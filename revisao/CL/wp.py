"""Revisão CL: mostra trechos do wikitext de páginas da Wikipédia guardadas (baixa se faltar).

Uso: python -I revisao/CL/wp.py <lang> "<Título>" [termo1 termo2 ...]
Sem termos: imprime o começo (infobox). Com termos: imprime as linhas que têm algum termo.
"""
import json
import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar import baixar  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
lang, titulo, *termos = sys.argv[1:]
f = baixar(f"wp:{lang}:{titulo}")
d = json.loads(f.read_text(encoding="utf-8"))
if "error" in d:
    print("ERRO", d["error"].get("info"))
    sys.exit()
print("#", d["parse"]["title"], f"https://{lang}.wikipedia.org/wiki/" + d["parse"]["title"].replace(" ", "_"))
txt = d["parse"]["wikitext"]["*"]
if not termos:
    print(txt[:2500])
else:
    for linha in txt.splitlines():
        if any(t.lower() in linha.lower() for t in termos):
            print(linha[:400])
