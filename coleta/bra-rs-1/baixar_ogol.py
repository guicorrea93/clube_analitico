"""Baixa o calendário de cada edição do Campeonato Gaúcho no ogol para data/coleta/bra-rs-1/ogol/rs1_{temporada}.json
e a ficha de cada clube para data/coleta/bra-rs-1/ogol/clubes.json.

Os códigos das edições ficam em data/coleta/bra-rs-1/ogol/edicoes.json (lista de edições da página
"competicao/campeonato-gaucho" do ogol, guardada em competicao_campeonato-gaucho.html; baixar_edicoes() refaz a lista).
O cache dos calendários fica em data/cache/ogol-bra-rs-1/ (plano de coleta, 2.1: os escudos saem deles).

Uso: python coleta/bra-rs-1/baixar_ogol.py [temporada ...] [--sem-fichas]
Com --sem-fichas só baixa os calendários (várias frentes em paralelo, cada uma com as suas temporadas); as fichas dos
clubes vêm depois, numa rodada só (python coleta/bra-rs-1/baixar_ogol.py clubes).
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
from edicoes import EDICAO_OGOL, PASTA_DADOS, RAIZ, TEMPORADAS  # noqa: E402

PASTA = PASTA_DADOS / "ogol"
ogol.ESPERA = 6.0   # como no Carioca: com 3 s o ogol pune a 1ª página de cada edição
CACHE = RAIZ / "data" / "cache" / "ogol-bra-rs-1"


def arquivo(temporada: str) -> Path:
    return PASTA / f"rs1_{temporada.replace(' ', '_')}.json"


def baixar_edicoes() -> dict[str, int]:
    """Temporada -> código da edição, pelo menu de edições da página da competição no ogol."""
    from baixar import pegar
    html = (pegar(f"{ogol.BASE}/competicao/campeonato-gaucho", PASTA / "competicao_campeonato-gaucho.html",
                  espera=ogol.ESPERA) or b"").decode("utf-8", "ignore")
    sel = re.findall(r"<select\b.*?</select>", html, flags=re.S)[0]
    por_ano: dict[str, int] = {}
    for i, rotulo in re.findall(r'<option value="(\d+)"[^>]*>\s*([^<]+?)\s*</option>', sel):
        por_ano.setdefault(rotulo, int(i))
    eds = {t: EDICAO_OGOL.get(t) or por_ano[t] for t in TEMPORADAS if t in EDICAO_OGOL or t in por_ano}
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
        js = calendario(edicoes[t], CACHE, f"calendario_{t.replace(' ', '_')}", titulo="Gaúcho")
        arquivo(t).write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{t}: {len(js)} jogos", flush=True)
    if "--sem-fichas" in sys.argv:
        sys.exit(0)
    # fichas dos clubes
    ids: dict[str, set] = {}
    for f in sorted(PASTA.glob("rs1_*.json")):
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
