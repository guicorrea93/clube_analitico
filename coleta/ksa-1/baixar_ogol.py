"""Baixa o calendário de cada edição da liga saudita no ogol ("liga-saudita") para data/coleta/ksa-1/ogol/<fim>.json
(<fim> = ano em que a temporada termina: 2000 é 1999/00). O ogol tem as edições de 1976/77 em diante, mas só tem os jogos
de 1999/00 em diante.

As edições vêm do seletor da página da competição (guardada em data/coleta/ksa-1/ogol/). As páginas de calendário ficam
em data/cache/ogol-ksa-1/calendario_<fim>_<id>_p<n>.html (o agente 1 tira os escudos delas).

Uso: python coleta/ksa-1/baixar_ogol.py [fim ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from ogol import calendario  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "ksa-1" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol-ksa-1"


def edicoes() -> list[tuple[int, int]]:
    """[(id, ano em que termina)] de 1999/00 a 2025/26, do seletor de edições da página guardada."""
    t = (PASTA / "competicao_liga-saudita.html").read_text(encoding="utf-8", errors="ignore")
    for sel in re.findall(r"<select\b.*?</select>", t, flags=re.S):
        ops = re.findall(r'<option value="(\d+)"[^>]*>\s*([^<]+?)\s*</option>', sel)
        if ops and all(re.match(r"^\d{4}/\d{2}$", n) for _, n in ops):
            return [(int(i), int(n[:4]) + 1) for i, n in ops if 2000 <= int(n[:4]) + 1 <= 2026]
    return []


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    anos = {int(a) for a in sys.argv[1:]}
    for ed, fim in edicoes():
        if anos and fim not in anos:
            continue
        jogos = calendario(ed, CACHE, f"calendario_{fim}")
        (PASTA / f"{fim}.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
        print(fim, ed, len(jogos), "jogos", flush=True)
