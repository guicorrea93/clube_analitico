"""Baixa as páginas da RSSSF da 1ª divisão angolana (Girabola) para data/coleta/ang-1/rsssf/: a lista de campeões
(angochamp.html) e as páginas de temporada desde o primeiro Girabola (ango79 ... ango99, ango00 ... ango09, ango2010 ...
ango2026). As da era colonial (ango41 ... ango75) e a temporada em andamento (ango2027) ficam de fora.

Uso: python coleta/ang-1/baixar_rsssf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from baixar import pegar  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "ang-1" / "rsssf"
BASE = "https://www.rsssf.org/tablesa/"
ULTIMA = 2026   # última temporada terminada (2025/26)


def no_escopo(pagina: str) -> bool:
    m = re.fullmatch(r"ango(\d+)\.html", pagina)
    if not m:
        return False
    n = m.group(1)
    if len(n) == 4:
        return n.startswith("20") and int(n) <= ULTIMA
    return len(n) == 2 and (n.startswith("0") or int(n) >= 79)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    t = (pegar(BASE + "angochamp.html", PASTA / "angochamp.html") or b"").decode("cp1252", "ignore")
    paginas = {p for p in re.findall(r'href="?(ango\d+\.html)', t, re.I) if no_escopo(p)}
    for p in sorted(paginas):
        ok = pegar(BASE + p, PASTA / p)
        print(p, "ok" if ok else "404", flush=True)
