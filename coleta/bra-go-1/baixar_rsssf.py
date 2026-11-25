"""Baixa as páginas do Campeonato Goiano da RSSSF Brasil para data/coleta/bra-go-1/rsssfbrasil/.

gocamp.htm (campeões), gotops.htm (artilheiros, se houver) e go{ano}.htm, uma por ano (1915 a 2026; sem página: 1924-1927,
1929-1932, 1934-1938 e 2025). Página já baixada não é baixada de novo. Quando o site não responde (25/11/2026: parou no
meio do download), vem a cópia do Internet Archive; as páginas que vieram de lá ficam em rsssfbrasil/origem.json.

Uso: python coleta/bra-go-1/baixar_rsssf.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from baixar import pegar  # noqa: E402
from edicoes import PASTA_DADOS, TEMPORADAS, pagina_rsssf  # noqa: E402

PASTA = PASTA_DADOS / "rsssfbrasil"
BASE = "https://rsssfbrasil.com/tablesfq/"
ARQUIVO = "https://web.archive.org/web/2026id_/"   # cópia mais nova do Internet Archive, sem a barra dele


FORA_DO_AR = [False]   # depois da 1ª falha do site, direto para a cópia do Internet Archive


def baixar(arq: str, origem: dict) -> bytes | None:
    if (PASTA / arq).exists():
        return (PASTA / arq).read_bytes()
    if not FORA_DO_AR[0]:
        try:
            dados = pegar(BASE + arq, PASTA / arq, espera=2.0, tentativas=2)
            if dados is not None:
                return dados
        except Exception:   # site fora do ar
            FORA_DO_AR[0] = True
    try:
        dados = pegar(ARQUIVO + BASE + arq, PASTA / arq, espera=3.0, tentativas=3)
    except Exception:
        return None
    if dados is not None:
        origem[arq] = "web.archive.org"
    return dados


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    f_origem = PASTA / "origem.json"
    origem = json.loads(f_origem.read_text(encoding="utf-8")) if f_origem.exists() else {}
    for arq in ["gocamp.htm", "gotops.htm", *sorted({pagina_rsssf(t) for t in TEMPORADAS})]:
        dados = baixar(arq, origem)
        print(arq, "sem página" if dados is None else f"{len(dados)} bytes{' (Internet Archive)' if arq in origem else ''}",
              flush=True)
        f_origem.write_text(json.dumps(origem, indent=1, sort_keys=True), encoding="utf-8")
