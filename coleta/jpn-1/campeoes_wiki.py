"""Campeão, vice e 3º de cada temporada na Wikipédia em inglês (List of Japanese football champions), segunda fonte do
campeão e do vice. Cada linha liga o clube pela página de hoje ("[[Sanfrecce Hiroshima|Toyo Industries]]"): o alvo do link
dá o clube e o rótulo dá o nome da época.

Uso como biblioteca: podio() -> {temporada: (campeão, vice, 3º)} (nomes de exibição); python coleta/jpn-1/campeoes_wiki.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from clubes_jpn import clube  # noqa: E402

ARQ = AQUI.parent.parent / "data" / "coleta" / "jpn-1" / "wikipedia" / "en_campeoes.txt"


def _clube(cel: str) -> tuple[str | None, str]:
    m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", cel)
    if not m:
        return None, cel.strip()
    alvo, rotulo = m.group(1).strip(), (m.group(2) or m.group(1)).strip()
    return clube(alvo) or clube(rotulo), rotulo


def podio() -> dict[str, tuple]:
    saida = {}
    for l in ARQ.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\|\{\{center\|\s*\[\[[^\]|]+\|(\d{4})(?:[–-](\d{2}))?\]\]\}\}\s*\|\|(.*)$", l)
        if not m:
            continue
        temporada = m.group(1) + (f"/{m.group(2)}" if m.group(2) else "")
        cels = m.group(3).split("||")
        if "Cup" in cels[0]:   # 1992: sem liga, a linha traz só a Copa da J.League
            continue
        saida[temporada] = tuple(_clube(c) for c in cels[:3])
    return saida


def artilheiros() -> dict[str, list[tuple[str, str | None, str, int]]]:
    """Artilheiro oficial de cada temporada (a linha logo abaixo da do pódio): {temporada: [(jogador, clube de exibição,
    clube como escrito, gols)]}. Empates vêm separados por <br />."""
    def celula(texto: str, gols: str) -> list:
        lista = []
        for parte in re.split(r"<br\s*/?>", texto):
            j = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", parte)
            c = re.search(r"\(([^)]+)\)\s*$", parte.strip())
            if j and c:
                lista.append(((j.group(2) or j.group(1)).strip(), clube(c.group(1)), c.group(1).strip(), int(gols)))
        return lista

    saida, atual = {}, None
    for l in ARQ.read_text(encoding="utf-8").split("\n"):
        if m := re.match(r"^\|\{\{center\|\s*\[\[[^\]|]+\|(\d{4})(?:[–-](\d{2}))?\]\]\}\}(.*)$", l):
            atual = m.group(1) + (f"/{m.group(2)}" if m.group(2) else "")
            cels = m.group(3).split("||")
            if len(cels) >= 6:   # 2020 e 2021: o artilheiro vem na mesma linha do pódio
                saida[atual] = celula(cels[4], cels[5].strip())
                atual = None
            continue
        m = re.match(r"^\|(.*)\|\|\s*(\d+)\s*$", l)
        if atual and m and "{{center" not in l:
            saida[atual] = celula(m.group(1), m.group(2))
            atual = None
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for t, p in podio().items():
        print(t, p)
    for t, a in artilheiros().items():
        print(t, a)
