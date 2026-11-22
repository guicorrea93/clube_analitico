"""Baixa da Wikipédia em espanhol o texto-fonte das temporadas peruanas ("Campeonato Peruano de Fútbol de <ano>" até 1965,
"Campeonato Descentralizado <ano>" de 1966 em diante) para data/coleta/per-1/wikipedia/es_<ano>.txt. Elas trazem os jogos
(quase sempre em tabela de confrontos, "|match_ALI_CHA=1—0") de 1926-1929, 1943-1967, 1982 e 1985, que a RSSSF não tem.
Baixa também a lista de campeões da Wikipédia em inglês ("List of Peruvian football champions") para en_campeoes.txt, segunda fonte
do campeão.

Uso: python coleta/per-1/baixar_wikipedia.py [ano ...]
"""
from __future__ import annotations

import sys
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "per-1" / "wikipedia"
URL = "https://es.wikipedia.org/w/index.php?title={t}&action=raw"
URL_EN = "https://en.wikipedia.org/w/index.php?title=List_of_Peruvian_football_champions&action=raw"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if not sys.argv[1:]:
        b = pegar(URL_EN, PASTA / "en_campeoes.txt", espera=1.0)
        print("en_campeoes", "404" if b is None else f"{len(b)} bytes", flush=True)
    for ano in [int(a) for a in sys.argv[1:]] or [*range(1926, 1930), *range(1943, 1968), 1982, 1985]:
        titulo = f"Campeonato Peruano de Fútbol de {ano}" if ano <= 1965 else f"Campeonato Descentralizado {ano}"
        b = pegar(URL.format(t=urllib.parse.quote(titulo.replace(" ", "_"))), PASTA / f"es_{ano}.txt", espera=1.0)
        t = (b or b"").decode("utf-8", "ignore")
        print(ano, "404" if b is None else f"{len(t)} bytes, {t.count('match_')} match_{' REDIRECT' if t.startswith('#RED') else ''}", flush=True)
