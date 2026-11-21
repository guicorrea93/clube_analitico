"""Baixa da Wikipédia em espanhol o texto-fonte das páginas das temporadas colombianas de 1948 a 1995
("Campeonato de Fútbol Profesional Colombiano 1948", "Campeonato colombiano <ano>") e dos torneios de 2011 e 2012
("Torneo Apertura 2011 (Colombia)"...; 2011, 2012 e 2025) para data/coleta/col-1/wikipedia/es_<nome>.txt. Elas trazem os jogos que a RSSSF
não tem (1948-1985, 1988-1990; 2011 e 2012 completos).

Uso: python coleta/col-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "col-1" / "wikipedia"
URL = "https://es.wikipedia.org/w/index.php?title={t}&action=raw"

PAGINAS = {"1948": "Campeonato de Fútbol Profesional Colombiano 1948",
           **{str(a): f"Campeonato colombiano {a}" for a in range(1949, 1996)},
           **{f"{a} {t}": f"Torneo {t} {a} (Colombia)" for a in (2011, 2012, 2025) for t in ("Apertura", "Finalización")}}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for chave, titulo in PAGINAS.items():
        b = pegar(URL.format(t=urllib.parse.quote(titulo.replace(" ", "_"))), PASTA / f"es_{chave.replace(' ', '_')}.txt", espera=1.0)
        t = (b or b"").decode("utf-8", "ignore")
        print(chave, "404" if b is None else f"{len(t)} bytes{' REDIRECT ' + t[:80] if t.startswith('#RED') else ''}", flush=True)
