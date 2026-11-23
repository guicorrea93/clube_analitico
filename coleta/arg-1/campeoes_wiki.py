"""Lista de campeões da Wikipédia em inglês ("List of Argentine football champions"), segunda fonte do campeão.

Página guardada em data/coleta/arg-1/wikipedia/en_campeoes.txt (wikitexto, baixado pela API). Os rótulos da página
viram as temporadas do pacote: "1912 FAF" -> "1912 Federación", "1919 AAmF" -> "1919 Amateurs", "1931 LAF" -> "1931 Liga",
"1936 (H)" -> "1936 Copa de Honor", "1991 Apertura" -> "1991/92 Apertura", "1992 Clausura" -> "1991/92 Clausura",
"2012–13" -> "2012/13 Campeonato", "1985–86" -> "1985/86".

Uso: campeoes() / vices() / terceiros() -> {temporada: nome do clube na Wikipédia}
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "arg-1" / "wikipedia" / "en_campeoes.txt"


def _temporada(rot: str) -> str | None:
    rot = rot.replace("–", "-").strip()
    if m := re.fullmatch(r"(\d{4}) (FAF|AAmF|LAF)", rot):
        return f"{m.group(1)} " + {"FAF": "Federación", "AAmF": "Amateurs", "LAF": "Liga"}[m.group(2)]
    if m := re.fullmatch(r"1936 \((H|C|O)\)", rot):
        return "1936 " + {"H": "Copa de Honor", "C": "Campeonato", "O": "Copa de Oro"}[m.group(1)]
    if m := re.fullmatch(r"(\d{4}) (Metropolitano|Nacional)", rot):
        return rot
    if m := re.fullmatch(r"(\d{4}) (Apertura|Clausura|Inicial|Final)", rot):
        a, t = int(m.group(1)), m.group(2)
        if a >= 2025:   # 2025 e 2026: Apertura e Clausura no ano civil
            return rot
        ini = a if t in ("Apertura", "Inicial") else a - 1
        return f"{ini}/{(ini + 1) % 100:02d} {t}"
    if m := re.fullmatch(r"(\d{4})-(\d{2})", rot):
        a = int(m.group(1))
        return f"{a}/{m.group(2)} Campeonato" if a == 2012 else f"{a}/{m.group(2)}"
    if m := re.fullmatch(r"(\d{4})(?: Transición)?", rot):
        a = int(m.group(1))
        return f"{a} Asociación" if a in (1912, 1913, 1914, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1931, 1932, 1933, 1934) else str(a)
    return None


def _podio() -> dict[str, list[str]]:
    """{temporada: [campeão, vice, 3º]} como na página (vice e 3º vazios quando a página não tem: "–")."""
    t = ARQ.read_text(encoding="utf-8")
    m = re.search(r"==\s*Titles by club", t)
    t = t[:m.start()] if m else t
    t = re.sub(r"\{\{refn[^{}]*(\{\{[^{}]*\}\}[^{}]*)*\}\}", "", t)
    t = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    saida: dict[str, list[str]] = {}
    for r in t.split("\n|-"):
        m = re.search(r"\[\[[^\]|]*Argentine Primera Divisi[^\]|]*\|([^\]]+)\]\]", r) or             re.search(r"\[\[[^\]|]*AFA Liga Profesional[^\]|]*\|([^\]]+)\]\]", r)
        if not m:
            continue
        rot = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        cel = r[m.end():].split("||")
        nomes = []
        for c in cel[1:4]:
            n = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", c)
            nomes.append(n.group(1).strip() if n else "")
        if not nomes or not nomes[0]:
            continue
        temp = _temporada(rot) or ("2025 Liga" if rot == "2025 Liga" else None)
        if temp and temp not in saida:
            saida[temp] = (nomes + ["", ""])[:3]
    return saida


def campeoes() -> dict[str, str]:
    return {t: v[0] for t, v in _podio().items()}


def vices() -> dict[str, str]:
    """Vice da lista oficial (AR-002 a AR-013: o vice da tabela lida não bate em várias edições)."""
    return {t: v[1] for t, v in _podio().items() if v[1]}


def terceiros() -> dict[str, str]:
    return {t: v[2] for t, v in _podio().items() if v[2]}
