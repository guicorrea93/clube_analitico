"""Baixa o calendário de cada edição da 1ª divisão argentina no ogol para data/coleta/arg-1/ogol/<id>.json.

As edições vêm das listas guardadas em data/coleta/arg-1/ogol/competicao_*.html: o menu de edições do
"Campeonato Argentino" (1931 em diante, sem o Metropolitano e o Nacional) e as páginas do Metropolitano e do
Nacional (1967-1985). As páginas de calendário ficam em data/cache/ogol-arg-1/calendario_<ano_inicio>_<id>_p<n>.html
(o agente 1 tira os escudos delas). O ogol não tem os jogos de vários anos antigos (a página vem vazia).

Uso: python coleta/arg-1/baixar_ogol.py [ano_inicio ...]
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
PASTA = RAIZ / "data" / "coleta" / "arg-1" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol-arg-1"


def ano_inicio(nome: str) -> int:
    """Ano de início da temporada (o do nome do arquivo de calendário). O Clausura de 1991 a 2013 fecha a temporada
    começada no ano anterior; "89/90" começa em 1989; "Campeonato Argentino 2020" é a temporada 2019/20."""
    if m := re.search(r"(\d{2,4})/(\d{2})\b", nome):
        a = int(m.group(1))
        return a if a > 1000 else (1900 + a if a > 30 else 2000 + a)
    a = int(re.search(r"(\d{4})", nome).group(1))
    if re.match(r"Clausura", nome) and 1991 <= a <= 2013:
        return a - 1
    if nome == "Campeonato Argentino 1991" or (nome == "Campeonato Argentino 2013") or nome == "Campeonato Argentino 2020":
        return a - 1
    return a


def edicoes() -> list[tuple[int, str, int]]:
    """[(id, nome no ogol, ano_inicio)] até a temporada 2025."""
    saida = []
    t = (PASTA / "competicao_campeonato-argentino.html").read_text(encoding="utf-8", errors="ignore")
    menu = t[:t.find('value="0"')]
    for i, nome in re.findall(r'<option value="(\d+)"[^>]*>([^<]+)', menu):
        saida.append((int(i), nome.strip(), ano_inicio(nome.strip())))
    for arq, rotulo in (("competicao_metropolitano.html", "Metropolitano"), ("competicao_nacional.html", "Nacional")):
        t = (PASTA / arq).read_text(encoding="utf-8", errors="ignore")
        for ano, i in sorted(set(re.findall(r'href="/edicao/campeonato-\w+-argentino-(\d{4})/(\d+)"', t))):
            saida.append((int(i), f"{rotulo} {ano}", int(ano)))
    return [e for e in saida if e[2] <= 2025 and not re.match(r"(Apertura|Clausura) 2026", e[1])]


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
