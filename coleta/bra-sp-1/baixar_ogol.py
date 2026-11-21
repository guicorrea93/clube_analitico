"""Baixa o calendário de cada edição do Paulista (1ª divisão) no ogol para data/coleta/bra-sp-1/ogol/sp1_{temporada}.json
e a ficha de cada clube para data/coleta/bra-sp-1/ogol/clubes.json.

Os códigos das edições ficam em data/coleta/bra-sp-1/ogol/edicoes.json (lista de edições da página
"campeonato-paulista/555" do ogol); nos anos de duas ligas, uma edição por liga ("1913 LPF", "1913 APEA").

Uso: python coleta/bra-sp-1/baixar_ogol.py [temporada ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import ogol  # noqa: E402
from ogol import calendario, equipe  # noqa: E402
from edicoes import PASTA_DADOS, RAIZ, TEMPORADAS  # noqa: E402

PASTA = PASTA_DADOS / "ogol"
ogol.ESPERA = 3.0   # o ogol limitou os pedidos no Paulista com 1,2 s
CACHE = RAIZ / "data" / "cache" / "ogol_sp1"


def arquivo(temporada: str) -> Path:
    return PASTA / f"sp1_{temporada.replace(' ', '_')}.json"


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    edicoes = json.loads((PASTA / "edicoes.json").read_text(encoding="utf-8"))
    alvo = [t for t in (sys.argv[1:] or TEMPORADAS) if t != "clubes"]
    for t in alvo:
        if t not in edicoes:
            print(t, "sem edição no ogol", flush=True)
            continue
        js = calendario(edicoes[t], CACHE, f"calendario_{t.replace(' ', '_')}", titulo="Paulista")
        arquivo(t).write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{t}: {len(js)} jogos", flush=True)
    # fichas dos clubes
    ids: dict[str, set] = {}
    for f in sorted(PASTA.glob("sp1_*.json")):
        for j in json.loads(f.read_text(encoding="utf-8")):
            for lado in ("mandante", "visitante"):
                if j.get(f"{lado}_id"):
                    ids.setdefault(j[f"{lado}_id"], set()).add(j[lado])
    saida = {}
    for i, nomes in sorted(ids.items()):
        ficha = equipe(i, RAIZ / "data" / "cache" / "ogol_equipes")
        ficha["nomes_ogol"] = sorted(nomes)
        saida[i] = ficha
    (PASTA / "clubes.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(saida), "clubes;", sum(1 for f in saida.values() if not f["uf"]), "sem UF")
