"""Identidade dos times de Fiji (fij-1): os times da liga são as associações dos distritos; cada grafia vira um time, com
cidade e ilha (região).

Decisões aprovadas pelo Guilherme em 24/11/2026 (pesquisa em docs/coleta/fij-1.md):
- nome do distrito puro, como a RSSSF e a própria liga escrevem ("Nadi", "Lautoka", "Rewa", "Tailevu Naitasiri"...); só o
  "Ba FC" leva o "FC" (o nome curto demais se confunde com outras coisas, como a sigla da Bahia);
- nenhum distrito mudou de identidade: "FC", "FA" e "Football Association" são formas do mesmo nome; "Tailevu-Naitasiri",
  "Tailevu/Naitasiri" = Tailevu Naitasiri; Tailevu North (Northland Tailevu) é outro time e não jogou a 1ª divisão;
- seleções de base que jogaram a liga: "Fiji Olympians" (a seleção olímpica: um time só, 1998-2006, como "Olympians",
  "U-21", "U-23" ou "Fiji U-20" nas páginas), "Fiji U-20" (2010) e "Fiji Youth Teams" (2011: a RSSSF soma numa linha a
  campanha de várias seleções de base).

Uso: clube(nome, ano) -> nome de exibição (ou None).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-oceania"))
from rsssf_oce import chave  # noqa: E402

VL, VA = "Viti Levu", "Vanua Levu"
# nome de exibição -> (cidade, ilha)
CLUBES: dict[str, tuple[str, str]] = {
    "Ba FC": ("Ba", VL), "Nadi": ("Nadi", VL), "Lautoka": ("Lautoka", VL), "Suva": ("Suva", VL), "Rewa": ("Nausori", VL),
    "Labasa": ("Labasa", VA), "Nadroga": ("Sigatoka", VL), "Navua": ("Navua", VL), "Tavua": ("Tavua", VL),
    "Nasinu": ("Nasinu", VL), "Tailevu Naitasiri": ("Nausori", VL), "Savusavu": ("Savusavu", VA), "Dreketi": ("Dreketi", VA),
    "Rakiraki": ("Rakiraki", VL), "Fiji Olympians": ("Suva", VL), "Fiji U-20": ("Suva", VL), "Fiji Youth Teams": ("Suva", VL),
}

# (regex sobre chave(nome), nome de exibição, ano inicial, ano final); a primeira que casa vale
REGRAS: list[tuple[str, str, int, int]] = [
    (r"^ba( fc| fa| fsc)?$", "Ba FC", 1900, 2100),
    (r"^(fiji )?(olympians?|u 2[0-3]|under 2[0-3])$", "Fiji Olympians", 1997, 2009),
    (r"^(fiji )?(u 20|under 20)$", "Fiji U-20", 2010, 2010),
    (r"^(fiji youth teams?|(ilhas )?fiji s ?2[03])$", "Fiji Youth Teams", 2011, 2011),   # ogol: "Ilhas Fiji S23"
    (r"^tailevu ?naitasiri$|^tailevu naitasiri$", "Tailevu Naitasiri", 1900, 2100),
    (r"^(sigatoka)$", "Nadroga", 1900, 2100),
]
_NOMES_CHAVE = {chave(n): n for n in CLUBES}


def clube(nome: str, ano: int) -> str | None:
    k = chave(re.sub(r"\s*\([^)]*\)\s*$", "", nome))
    for kk in dict.fromkeys((k, re.sub(r" (fc|fa|football (club|association))$", "", k))):
        for rx, nome_ex, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx, kk):
                return nome_ex
        if kk in _NOMES_CHAVE:
            return _NOMES_CHAVE[kk]
    return None
