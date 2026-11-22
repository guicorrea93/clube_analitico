"""Baixa o calendário de cada edição do Paulista Série A2 (2ª divisão) no ogol para data/coleta/bra-sp-2/ogol/sp2_{temporada}.json
e a ficha de cada clube para data/coleta/bra-sp-2/ogol/clubes.json.

Os códigos das edições ficam em data/coleta/bra-sp-2/ogol/edicoes.json (lista de edições da página
"competicao/campeonato-paulista-a2/562" do ogol; baixar_edicoes() refaz a lista).

Uso: python coleta/bra-sp-2/baixar_ogol.py [temporada ...]
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
CACHE = RAIZ / "data" / "cache" / "ogol_sp2"


def arquivo(temporada: str) -> Path:
    return PASTA / f"sp2_{temporada.replace(' ', '_')}.json"


def baixar_edicoes() -> dict[str, int]:
    """Temporada -> código da edição, pela página da competição no ogol (uma edição por ano)."""
    import re
    from baixar import pegar
    html = (pegar(f"{ogol.BASE}/competicao/campeonato-paulista-a2/562", None, espera=ogol.ESPERA) or b"").decode("utf-8", "ignore")
    eds = {}
    for slug, i in re.findall(r'/edicao/([^"/]+)/(\d+)', html):
        ano = re.findall(r"(\d{4})", slug)
        if ano and "a2" in slug:
            eds[ano[-1]] = int(i)
    PASTA.mkdir(parents=True, exist_ok=True)
    (PASTA / "edicoes.json").write_text(json.dumps(dict(sorted(eds.items())), indent=1), encoding="utf-8")
    return eds


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if not (PASTA / "edicoes.json").exists():
        baixar_edicoes()
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
    for f in sorted(PASTA.glob("sp2_*.json")):
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
