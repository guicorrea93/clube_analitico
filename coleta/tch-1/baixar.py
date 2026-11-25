"""Baixa as fontes do campeonato da Tchecoslováquia (tch-1), 1925 a 1992/93.

Fontes (cada uma numa pasta de data/coleta/tch-1/):
  rsssf  RSSSF: tabelas finais de todas as temporadas (tablest/tsjslhist.html) e lista de campeões (tsjslchamp.html).
  wiki   Wikipédia em inglês: artigo de cada temporada (matriz de resultados, tabela final, punições), com os modelos.
O ogol, a ESPN e o football-data não têm esta liga.

Uso: python coleta/tch-1/baixar.py rsssf wiki
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(1, str(AQUI))
from baixar import pegar  # noqa: E402

from edicoes import DADOS, TEMPORADAS, wiki_titulo  # noqa: E402


def rsssf() -> None:
    for n in ("tsjslhist", "tsjslchamp"):
        d = pegar(f"https://www.rsssf.org/tablest/{n}.html", DADOS / "rsssf" / f"{n}.html", espera=2.0)
        print(f"rsssf {n}: {len(d or b'')} bytes", flush=True)


def wiki() -> None:
    from wikipedia import wikitexto
    pasta = DADOS / "wikipedia"
    pasta.mkdir(parents=True, exist_ok=True)
    for t in [wiki_titulo(a) for a in TEMPORADAS] + ["Czechoslovak First League"]:
        arq = pasta / (t.replace("/", "_") + ".wiki")
        if arq.exists():
            continue
        txt = wikitexto("en", t, espera=3.0)
        if txt is None:
            print(f"wiki: não achei '{t}'", flush=True)
            continue
        arq.write_text(txt, encoding="utf-8")
        print(f"wiki {t}: {len(txt)}", flush=True)
    for a in TEMPORADAS:
        t = wiki_titulo(a)
        if not (pasta / f"{t}.wiki").exists():
            continue
        modelos = re.findall(r"\{\{(\d{4}(?:[–-]\d{2,4})? [A-Za-zÁ-ž' -]+? (?:table|results))\}\}",
                             (pasta / f"{t}.wiki").read_text(encoding="utf-8"))
        for i, mod in enumerate(dict.fromkeys(modelos), 1):
            arq = pasta / (f"{t} (tabela).wiki" if i == 1 else f"{t} (tabela {i}).wiki")
            if arq.exists():
                continue
            txt = wikitexto("en", f"Template:{mod}", espera=3.0)
            if txt:
                arq.write_text(txt, encoding="utf-8")
                print(f"wiki Template:{mod}: {len(txt)}", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for nome in sys.argv[1:]:
        globals()[nome]()
