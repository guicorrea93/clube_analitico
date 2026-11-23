"""BDFutbol (bdfutbol.com): leitor da página de uma temporada (/es/t/teng1960-61.html para a Inglaterra, /es/t/t1928-29.html
para a Espanha). Cada jogo traz rodada, data, mandante, placar, visitante, estádio, árbitro (nome completo) e o id da ficha.

Uso como biblioteca: jogos(arq) -> [{"rodada", "data" (AAAA-MM-DD), "mandante", "visitante", "gm", "gv", "estadio",
"arbitro", "pid"}]
"""
from __future__ import annotations

import html
import re
from pathlib import Path

LINHA = re.compile(r"<tr class='jornadai ij(\d+)'[^>]*data-jornada='(\d+)'>(.*?)</tr>", re.S)


def _txt(x: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x))).strip()


def jogos(arq: Path) -> list[dict]:
    t = arq.read_text(encoding="utf-8", errors="replace")
    res = []
    for m in LINHA.finditer(t):
        corpo = m.group(3)
        if "p.php?id=" not in corpo:
            continue
        tds = re.findall(r"<td[^>]*>(.*?)</td>", corpo, re.S)
        if len(tds) < 4:
            continue
        d = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", _txt(tds[0]))
        gols = re.findall(r"\d+", _txt(tds[2]))
        res.append({"rodada": int(m.group(2)), "data": f"{d.group(3)}-{int(d.group(2)):02d}-{int(d.group(1)):02d}" if d else None,
                    "mandante": _txt(tds[1]), "visitante": _txt(tds[3]),
                    "gm": int(gols[0]) if len(gols) > 1 else None, "gv": int(gols[1]) if len(gols) > 1 else None,
                    "estadio": _txt(tds[4]) if len(tds) > 4 else "", "arbitro": _txt(tds[5]) if len(tds) > 5 else "",
                    "pid": re.search(r"p\.php\?id=(\d+)", corpo).group(1)})
    return res
