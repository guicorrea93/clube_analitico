"""Revisão Série C (SC): baixa o wikitexto das páginas da Wikipédia (pt, en, es) de cada edição.

Guarda em data/cache/revisao/SC/wiki/{lingua}_{ano}.txt (e .url com o título achado). Não baixa de novo.
Uso: python revisao/SC/baixar.py [pt|en|es] [ano ...]
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PASTA = RAIZ / "data" / "cache" / "revisao" / "SC" / "wiki"
UA = {"User-Agent": "clube-analitico-revisao/1.0 (uso pessoal)"}
ANOS = [1981, 1988, 1990, 1992] + list(range(1994, 2000)) + list(range(2001, 2026))
TITULOS = {
    "pt": ["Campeonato Brasileiro de Futebol de {a} - Série C", "Campeonato Brasileiro de Futebol de {a} – Série C",
           "Taça de Bronze de {a}", "Campeonato Brasileiro de Futebol de {a} - Taça de Bronze"],
    "en": ["{a} Campeonato Brasileiro Série C", "{a} Taça de Bronze"],
    "es": ["Campeonato Brasileño de Serie C {a}", "Campeonato Brasileño Serie C {a}", "Serie C de Brasil {a}",
           "Campeonato Brasileño de Fútbol Serie C {a}"],
}
EXTRAS = {"pt_lista": ("pt", "Campeonato Brasileiro de Futebol - Série C"),
          "en_lista": ("en", "Campeonato Brasileiro Série C"),
          "es_lista": ("es", "Campeonato Brasileño de Serie C")}
_ultimo = [0.0]


def pedir(lingua, titulo):
    q = urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                                "titles": titulo, "redirects": 1, "format": "json", "formatversion": 2})
    for tentativa in range(6):
        espera = 2.1 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://{lingua}.wikipedia.org/w/api.php?{q}", headers=UA),
                                        timeout=40) as r:
                pag = json.loads(r.read())["query"]["pages"][0]
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or tentativa == 5:
                raise
            time.sleep(45)
    if pag.get("missing"):
        return None, None
    return pag["title"], pag["revisions"][0]["slots"]["main"]["content"]


def guardar(nome, lingua, modelos):
    destino = PASTA / f"{nome}.txt"
    if destino.exists():
        return
    for m in modelos:
        titulo, txt = pedir(lingua, m)
        if txt:
            destino.write_text(txt, encoding="utf-8")
            (PASTA / f"{nome}.url").write_text(
                f"https://{lingua}.wikipedia.org/wiki/" + urllib.parse.quote(titulo.replace(" ", "_")), encoding="utf-8")
            print(nome, titulo, len(txt), flush=True)
            return
    print(nome, "sem página", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    linguas = [a for a in sys.argv[1:] if not a.isdigit()] or list(TITULOS)
    anos = [int(a) for a in sys.argv[1:] if a.isdigit()] or ANOS
    for nome, (lg, t) in EXTRAS.items():
        if lg in linguas:
            guardar(nome, lg, [t])
    for a in anos:
        for lg in linguas:
            guardar(f"{lg}_{a}", lg, [m.format(a=a) for m in TITULOS[lg]])
