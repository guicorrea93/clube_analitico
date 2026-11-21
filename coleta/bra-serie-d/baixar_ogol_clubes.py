"""Baixa a ficha no ogol de cada clube que aparece nos calendários da Série D (nome completo, cidade, UF)
e grava data/coleta/bra-serie-d/ogol/clubes.json. As páginas ficam em data/cache/ogol_equipes/.

Uso: python coleta/bra-serie-d/baixar_ogol_clubes.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from ogol import equipe  # noqa: E402
from edicoes import PASTA_DADOS, RAIZ  # noqa: E402

PASTA = PASTA_DADOS / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol_equipes"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    ids: dict[str, set] = {}
    for f in sorted(PASTA.glob("serie_d_*.json")):
        for j in json.loads(f.read_text(encoding="utf-8")):
            for lado in ("mandante", "visitante"):
                if j.get(f"{lado}_id"):
                    ids.setdefault(j[f"{lado}_id"], set()).add(j[lado])
    # fichas que já estão no arquivo e não vêm dos calendários (copiadas à mão de outra coleta: SE Ariquemes na Série C) ficam
    antigo = json.loads((PASTA / "clubes.json").read_text(encoding="utf-8")) if (PASTA / "clubes.json").exists() else {}
    saida = {i: f for i, f in antigo.items() if i not in ids}
    for i, (id_ogol, nomes) in enumerate(sorted(ids.items(), key=lambda x: (not x[0].isdigit(), int(x[0]) if x[0].isdigit() else 0, x[0]))):
        ficha = equipe(id_ogol, CACHE)
        ficha["nomes_ogol"] = sorted(nomes)
        saida[id_ogol] = ficha
        if i % 25 == 0:
            print(i, len(ids), ficha, flush=True)
    (PASTA / "clubes.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(saida), "clubes;", sum(1 for f in saida.values() if not f["uf"]), "sem UF")
