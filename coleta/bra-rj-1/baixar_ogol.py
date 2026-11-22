"""Baixa o calendário de cada edição do Campeonato Carioca no ogol para data/coleta/bra-rj-1/ogol/rj1_{temporada}.json
e a ficha de cada clube para data/coleta/bra-rj-1/ogol/clubes.json.

Os códigos das edições ficam em data/coleta/bra-rj-1/ogol/edicoes.json (lista de edições da página
"competicao/campeonato-carioca/893" do ogol; baixar_edicoes() refaz a lista). Nos anos de duas ligas, uma edição por liga
("campeonato-carioca-1933-amea", "-1933-lcf"); 1979 tem a edição normal e a "especial".

Uso: python coleta/bra-rj-1/baixar_ogol.py [temporada ...] [--sem-fichas]
Com --sem-fichas só baixa os calendários (várias frentes em paralelo, cada uma com as suas temporadas); as fichas dos
clubes vêm depois, numa rodada só (python coleta/bra-rj-1/baixar_ogol.py clubes).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import ogol  # noqa: E402
from ogol import calendario, equipe  # noqa: E402
from edicoes import PASTA_DADOS, RAIZ, TEMPORADAS, slug_ogol  # noqa: E402

PASTA = PASTA_DADOS / "ogol"
ogol.ESPERA = 6.0   # com 3 s o ogol punia a 1ª página de cada edição (60 s ou mais de espera); com 6 s não
CACHE = RAIZ / "data" / "cache" / "ogol_rj1"


def arquivo(temporada: str) -> Path:
    return PASTA / f"rj1_{temporada.replace(' ', '_')}.json"


def baixar_edicoes() -> dict[str, int]:
    """Temporada -> código da edição, pela página da competição no ogol."""
    from baixar import pegar
    html = (pegar(f"{ogol.BASE}/competicao/campeonato-carioca/893", None, espera=ogol.ESPERA) or b"").decode("utf-8", "ignore")
    por_slug = {}
    for slug, i in re.findall(r'/edicao/([^"/]+)/(\d+)', html):
        por_slug.setdefault(slug, int(i))
    eds = {t: por_slug[slug_ogol(t)] for t in TEMPORADAS if slug_ogol(t) in por_slug}
    PASTA.mkdir(parents=True, exist_ok=True)
    (PASTA / "edicoes.json").write_text(json.dumps(eds, indent=1, ensure_ascii=False), encoding="utf-8")
    return eds


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if not (PASTA / "edicoes.json").exists():
        baixar_edicoes()
    edicoes = json.loads((PASTA / "edicoes.json").read_text(encoding="utf-8"))
    args = [a for a in sys.argv[1:] if a != "--sem-fichas"]
    alvo = [t for t in (args or TEMPORADAS) if t != "clubes"]
    for t in alvo:
        if t not in edicoes:
            print(t, "sem edição no ogol", flush=True)
            continue
        if arquivo(t).exists() and json.loads(arquivo(t).read_text(encoding="utf-8")):
            continue
        js = calendario(edicoes[t], CACHE, f"calendario_{t.replace(' ', '_')}", titulo="Carioca")
        arquivo(t).write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{t}: {len(js)} jogos", flush=True)
    if "--sem-fichas" in sys.argv:
        sys.exit(0)
    # fichas dos clubes
    ids: dict[str, set] = {}
    for f in sorted(PASTA.glob("rj1_*.json")):
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
