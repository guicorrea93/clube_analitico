"""Baixa do Bola n@ Área (bolanaarea.com) as páginas das Séries C não oficiais de 1987 (Módulos Azul e Branco da Copa
União) e 2000 (Módulos Verde e Branco da Copa João Havelange), para data/coleta/bra-serie-c/bola/ (decisão D-10, achado
SC-029). Educado: uma página a cada 2,5 s; página já baixada não é baixada de novo.
Uso: python coleta/bra-serie-c/baixar_bola.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from baixar import pegar  # noqa: E402
from edicoes import PASTA_DADOS  # noqa: E402

PASTA = PASTA_DADOS / "bola"
PAGINAS = ["serie_c_1987", "serie_c_1987_md-azul", "serie_c_1987_md-branco",
           "serie_c_2000", "serie_c_2000_modulo_verde", "serie_c_2000_modulo_branco", "serie_c_2000_fasefinal"]

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for p in PAGINAS:
        dados = pegar(f"https://www.bolanaarea.com/{p}.htm", PASTA / f"{p}.htm", espera=2.5)
        print(p, len(dados or b""), "bytes", flush=True)
