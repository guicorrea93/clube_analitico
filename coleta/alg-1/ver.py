"""Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta.

Uso: python coleta/alg-1/ver.py "1991/92 Apertura" "River Plate" "Racing Club" [linhas de contexto]
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
sys.path.insert(0, str(AQUI))
from conferir import preparar  # noqa: E402
from edicoes import EDICOES  # noqa: E402
from ler_rsssf import linhas  # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    temp, a = sys.argv[1], sys.argv[2]
    b = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].isdigit() else None
    ctx = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 2
    e = next(x for x in EDICOES if x.temporada == temp)
    p = preparar(e)
    for j in p["jogos"]:
        if a in (j["m"], j["v"]) and (b is None or b in (j["m"], j["v"])):
            pag, lin = j["j"].texto.split(":")
            ls = linhas(pag)
            print(f"--- {pag}:{lin}  {j['m']} {j['gm']}-{j['gv']} {j['v']}  fase={j['fase']!r} grupo={j['grupo']!r} esp={j['esp']!r} data={j['j'].data}")
            for k in range(max(0, int(lin) - ctx), min(len(ls), int(lin) + ctx + 1)):
                print(f"   {k}: {ls[k]}")
