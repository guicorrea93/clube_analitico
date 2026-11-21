"""Baixa o calendário de cada edição da 1ª divisão colombiana no ogol para data/coleta/col-1/ogol/<id>.json.

As edições vêm do menu da "Liga Colombiana" guardado em data/coleta/col-1/ogol/competicao_liga-colombiana.html (1948 a
2001, uma por ano; Apertura e Finalización de 2002 em diante não estão nesse menu). As páginas de calendário ficam em
data/cache/ogol-col-1/calendario_<ano>_<id>_p<n>.html (o agente 1 tira os escudos delas).

Uso: python coleta/col-1/baixar_ogol.py [ano ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from ogol import calendario  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "col-1" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol-col-1"


def edicoes() -> list[tuple[int, str, int]]:
    """[(id, nome no menu, ano)]."""
    t = (PASTA / "competicao_liga-colombiana.html").read_text(encoding="utf-8", errors="ignore")
    return [(int(i), n.strip(), int(n.strip()[:4])) for i, n in re.findall(r'<option value="(\d+)"[^>]*>(\d{4})</option>', t)]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    lista = edicoes()
    (PASTA / "edicoes.json").write_text(json.dumps([{"id": i, "nome": n, "ano_inicio": a} for i, n, a in lista],
                                                   ensure_ascii=False, indent=0), encoding="utf-8")
    anos = {int(a) for a in sys.argv[1:]}
    for i, nome, ano in lista:
        if anos and ano not in anos:
            continue
        js = calendario(i, CACHE, f"calendario_{ano}")
        (PASTA / f"{i}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano} {nome} ({i}): {len(js)} jogos", flush=True)
