"""Baixa o calendário de cada edição da 1ª divisão camaronesa no ogol para data/coleta/cmr-1/ogol/<id>.json.

As edições vêm do menu da "Liga dos Camarões" guardado em data/coleta/cmr-1/ogol/competicao_liga-dos-camaroes.html (edições do menu, em
diante). As páginas de calendário ficam em data/cache/ogol-cmr-1/calendario_<ano_inicio>_<id>_p<n>.html (o agente 1 tira
os escudos delas).

Uso: python coleta/cmr-1/baixar_ogol.py [ano_inicio ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
from ogol import calendario  # noqa: E402

RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "cmr-1" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol-cmr-1"
ULTIMO = 2026   # última temporada terminada (2026)


def edicoes() -> list[tuple[int, str, int]]:
    """[(id, nome no menu, ano_inicio)] até a última temporada terminada."""
    t = (PASTA / "competicao_liga-dos-camaroes.html").read_text(encoding="utf-8", errors="ignore")
    sel = re.findall(r"<select\b.*?</select>", t, flags=re.S)[0]
    saida = []
    for i, nome in re.findall(r'<option value="(\d+)"[^>]*>\s*([^<]+?)\s*</option>', sel):
        ano = int(nome[:4])
        if ano <= ULTIMO:
            saida.append((int(i), nome, ano))
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
        if (PASTA / f"{i}.json").exists():
            continue
        js = calendario(i, CACHE, f"calendario_{ano}")
        (PASTA / f"{i}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano} {nome} ({i}): {len(js)} jogos", flush=True)
