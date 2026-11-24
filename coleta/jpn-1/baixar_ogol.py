"""Baixa o calendário de cada edição da J1 (1993-2025) no ogol para data/coleta/jpn-1/ogol/<ano>.json.

As edições vêm do seletor da página da competição ("liga-japonesa", guardada em data/coleta/jpn-1/ogol/). As páginas de
calendário ficam em data/cache/ogol-jpn-1/calendario_<ano>_<id>_p<n>.html (o agente 1 tira os escudos delas). O ogol
não tem a JSL (1965-1991/92).

Uso: python coleta/jpn-1/baixar_ogol.py [ano ...]
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
PASTA = RAIZ / "data" / "coleta" / "jpn-1" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol-jpn-1"


def edicoes() -> list[tuple[int, int]]:
    """[(id, ano)] de 1993 a 2025, do seletor de edições da página guardada."""
    t = (PASTA / "competicao_liga-japonesa.html").read_text(encoding="utf-8", errors="ignore")
    for sel in re.findall(r"<select\b.*?</select>", t, flags=re.S):
        ops = re.findall(r'<option value="(\d+)"[^>]*>\s*([^<]+?)\s*</option>', sel)
        if ops and all(re.match(r"^\d{4}(/\d{2})?$", n) for _, n in ops):
            return [(int(i), int(n)) for i, n in ops if re.match(r"^\d{4}$", n) and int(n) <= 2025]
    return []


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    anos = {int(a) for a in sys.argv[1:]}
    for ed, ano in edicoes():
        if anos and ano not in anos:
            continue
        jogos = calendario(ed, CACHE, f"calendario_{ano}")
        (PASTA / f"{ano}.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
        print(ano, ed, len(jogos), "jogos", flush=True)
