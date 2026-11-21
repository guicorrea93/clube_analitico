"""Baixa o calendário de cada edição da 1ª divisão chilena no ogol para data/coleta/chi-1/ogol/<id>.json.

As edições vêm do menu da "Liga Chilena" guardado em data/coleta/chi-1/ogol/competicao_liga-chilena.html. O menu chama de
"X/Y" a temporada do ano Y ("1975/76" é 1976) e não traz os anos de Apertura e Clausura (2002-2017). As páginas de
calendário ficam em data/cache/ogol-chi-1/calendario_<ano>_<id>_p<n>.html (o agente 1 tira os escudos delas).

Uso: python coleta/chi-1/baixar_ogol.py [ano ...]
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
PASTA = RAIZ / "data" / "coleta" / "chi-1" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol-chi-1"


def edicoes() -> list[tuple[int, str, int]]:
    """[(id, nome no menu, ano)] até 2025."""
    t = (PASTA / "competicao_liga-chilena.html").read_text(encoding="utf-8", errors="ignore")
    saida = []
    for i, nome in re.findall(r'<option value="(\d+)"[^>]*>([^<]+)', t[:t.find('value="0"')]):
        nome = nome.strip()
        m = re.fullmatch(r"(\d{4})(?:/(\d{2}))?", nome)
        ano = int(nome[:2] + m.group(2)) if m.group(2) else int(m.group(1))
        if ano <= 2025:
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
        js = calendario(i, CACHE, f"calendario_{ano}")
        (PASTA / f"{i}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano} {nome} ({i}): {len(js)} jogos", flush=True)
