"""Baixa o calendário de cada edição da 1ª divisão uruguaia no ogol para data/coleta/uru-1/ogol/<id>.json.

As edições vêm do menu da "Liga Uruguaia" guardado em data/coleta/uru-1/ogol/competicao_liga-uruguaia.html. O ogol só
tem os jogos de 2005/06 em diante (as edições anteriores existem, mas vêm vazias). As páginas de calendário ficam em
data/cache/ogol-uru-1/calendario_<ano_inicio>_<id>_p<n>.html (o agente 1 tira os escudos delas).

Uso: python coleta/uru-1/baixar_ogol.py [ano_inicio ...]
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
PASTA = RAIZ / "data" / "coleta" / "uru-1" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol-uru-1"

# o menu chama de "2006", "2007" e "2010" as temporadas 2005/06, 2006/07 e 2009/10; e de "2015/16" a Transición 2016
ANO_DO_ID = {37188: 2005, 8996: 2006, 9584: 2009, 99181: 2016}


def edicoes() -> list[tuple[int, str, int]]:
    """[(id, nome no menu, ano_inicio)] de 2005/06 a 2025."""
    t = (PASTA / "competicao_liga-uruguaia.html").read_text(encoding="utf-8", errors="ignore")
    saida = []
    for i, nome in re.findall(r'<option value="(\d+)"[^>]*>([^<]+)', t[:t.find('value="0"')]):
        i, nome = int(i), nome.strip()
        ano = ANO_DO_ID.get(i) or int(nome[:4])
        if 2005 <= ano <= 2025 and (i in ANO_DO_ID or not re.fullmatch(r"200[4-9]|2010", nome)):
            saida.append((i, nome, ano))
    return saida


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
