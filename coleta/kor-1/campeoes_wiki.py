"""Campeão e vice de cada ano da K League pela Wikipédia em inglês (List of South Korean football champions,
data/coleta/kor-1/wikipedia/en_campeoes.txt), para conferir o campeão e o vice tirados dos jogos.

O clube vem pelo alvo do link ("[[Busan IPark|Daewoo Royals]]" -> Busan IPark), que é o nome de hoje; ALVO liga o alvo ao
código do clube no portal (clubes_kor.py).

Uso como biblioteca: podio() -> {ano: (código do campeão, código do vice, texto do campeão, texto do vice)}.
"""
from __future__ import annotations

import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ARQ = AQUI.parent.parent / "data" / "coleta" / "kor-1" / "wikipedia" / "en_campeoes.txt"

ALVO = {
    "Hallelujah FC": "K11", "Busan IPark": "K06", "Jeju United FC": "K04", "Jeju SK FC": "K04", "FC Seoul": "K09",
    "Pohang Steelers": "K03", "Ulsan HD FC": "K01", "Ulsan Hyundai FC": "K01", "Seongnam FC": "K08",
    "Suwon Samsung Bluewings": "K02", "Jeonbuk Hyundai Motors": "K05", "Jeonnam Dragons": "K07", "Gangwon FC": "K21",
    "Daejeon Hana Citizen": "K10", "Gimcheon Sangmu FC": "K35", "Incheon United FC": "K18", "Gyeongnam FC": "K20",
    "Daegu FC": "K17", "Suwon FC": "K29", "Bucheon SK": "K04", "Chunnam Dragons": "K07", "Daewoo Royals": "K06",
    "Gwangju FC": "K22",
}


def podio() -> dict[int, tuple]:
    t = ARQ.read_text(encoding="utf-8")
    saida = {}
    for m in re.finditer(r"\|\s*\{\{center\|\s*\[\[(\d{4}) K[- ]Leag[^|\]]*\|\d{4}\]\]\}\}\s*\n\|([^\n]*)\n\|([^\n]*)\n\|([^\n]*)", t):
        ano = int(m.group(1))
        cods, txts = [], []
        for cel in (m.group(3), m.group(4)):
            l = re.search(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", cel)
            alvo = l.group(1).split("#")[0].strip() if l else ""
            cods.append(ALVO.get(alvo))
            txts.append((l.group(2) or l.group(1)) if l else cel.strip())
            if l and alvo not in ALVO:
                raise SystemExit(f"alvo de link sem código: {alvo!r} ({ano}); acrescente em campeoes_wiki.ALVO")
        saida[ano] = (cods[0], cods[1], txts[0], txts[1])
    return saida


def artilheiros() -> dict[int, list[tuple[str, str, int]]]:
    """{ano: [(jogador, código do clube, gols)]} pela lista "K League Top Scorer Award" (en_artilheiros.txt)."""
    t = (ARQ.parent / "en_artilheiros.txt").read_text(encoding="utf-8")
    t = t[:t.find("=== K League 2")] if "=== K League 2" in t else t
    saida, ano = {}, None
    for bloco in t.split("\n|-"):
        m = re.search(r"\[\[(\d{4}) K[- ]League[^\]]*\]\]", bloco)
        if m:
            ano = int(m.group(1))
        jog = re.search(r"\{\{flagicon\|[^}]*\}\}\s*\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", bloco)
        gols = re.search(r"align=center\|(\d+)", bloco)
        if not (ano and jog and gols):
            continue
        links = re.findall(r"\[\[([^|\]]+)(?:\|[^\]]+)?\]\]", bloco[jog.end():])
        alvo = next((l.split("#")[0].strip() for l in links if l.split("#")[0].strip() in ALVO), None)
        if alvo is None:
            raise SystemExit(f"artilheiro de {ano}: clube sem código ({links[:2]}); acrescente em campeoes_wiki.ALVO")
        nome = re.sub(r"\s*\(.*?\)$", "", jog.group(2) or jog.group(1)).strip()
        saida.setdefault(ano, []).append((nome, ALVO[alvo], int(gols.group(1))))
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for a, p in sorted(podio().items()):
        print(a, p)
    for a, p in sorted(artilheiros().items()):
        print(a, p)
