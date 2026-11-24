"""Identidade dos clubes da Nova Caledônia (ncl-1): cada grafia da RSSSF vira um clube, com cidade e província (região).

Decisões aprovadas pelo Guilherme em 24/11/2026 (pesquisa em docs/coleta/ncl-1.md):
- AS Le Nickel (1969, 1970, 1976) = AS Magenta (mesmo clube com outro nome: Wikipédia fr/en e lista de fundações da RSSSF;
  a lista de campeões da RSSSF conta os dois separados);
- Gaïtcha FCN = FC Gaïtcha = "Gaïtcha FC" (RSSSF: "includes Gaïtcha FCN"); o ASC Gaïca (Lifou, 2023 em diante) é outro clube;
- "Île des Pins" (1961) = AS Kunié (o clube da ilha; Kunié é o nome kanak); "AS Baco" (3º em 1991) = JS Baco;
- Entente Gélima (1989) é outro clube que a USL Gélima (Canala); Wé-Luécilla (Lifou) como a RSSSF escreve;
- nomes oficiais ou de uso corrente: "AS Tiga Sport" (a RSSSF escreve "Tiga Sports"), "USC Nouméa", "SS Indépendante";
- AS Auteuil (até 2005) e FC Auteuil (2014-2015) ficam separados (nenhuma fonte liga os dois).

Uso: clube(nome, ano) -> nome de exibição (ou None). ano = ano de início da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-oceania"))
from rsssf_oce import chave  # noqa: E402

S, N, IL = "Sud", "Nord", "Îles Loyauté"
# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "AC La Foa": ("La Foa", S), "ACB Poya": ("Poya", N), "AGJP": ("Nouméa", S), "AS 6e km": ("Nouméa", S),
    "AS Auteuil": ("Nouméa", S), "AS Frégate": ("Nouméa", S), "AS Grand Nord": ("Koumac", N), "AS Horizon Patho": ("Maré", IL),
    "AS Kirikitr": ("Lifou", IL), "AS Kunié": ("Île des Pins", S), "AS Lössi": ("Nouméa", S), "AS Magenta": ("Nouméa", S),
    "AS Mont-Dore": ("Mont-Dore", S), "AS Mouli": ("Ouvéa", IL), "AS Païta": ("Païta", S), "AS Poum": ("Poum", N),
    "AS Qanono": ("Lifou", IL), "AS Témala-Ouélisse": ("Voh", N), "AS Tiga Sport": ("Nouméa", S), "AS Wetr": ("Lifou", IL),
    "ASC Gaïca": ("Lifou", IL), "ASLN Kouaoua": ("Kouaoua", N), "CA Saint-Louis": ("Le Mont-Dore", S),
    "Club Sportif Militaire": ("Nouméa", S), "CO Koné": ("Koné", N), "Croix Bleue": ("Nouméa", S), "CS Nékoué": ("Houaïlou", N),
    "Davène Sport": ("Nouméa", S), "Dragon Noir": ("Nouméa", S), "Dumbéa FC": ("Dumbéa", S), "Entente Gélima": ("Canala", N),
    "ES Wacaélé": ("Lifou", IL), "Essor de Canala": ("Canala", N), "FC Auteuil": ("Nouméa", S), "FC Bélep": ("Mont-Dore", S),
    "FC Koh": ("Kaala-Gomen", N), "Gaïtcha FC": ("Nouméa", S), "Groupement Sportif Ouvéa": ("Ouvéa", IL),
    "Hienghène Sport": ("Hienghène", N), "Impassible": ("Nouméa", S), "JS Baco": ("Koné", N), "JS Maré": ("Maré", IL),
    "JS Tiéta": ("Voh", N), "JS Traput": ("Lifou", IL), "JS Vallée du Tir": ("Nouméa", S), "Kehdek de Koumac": ("Koumac", N),
    "Olympique Nouméa": ("Nouméa", S), "PLGC": ("Nouméa", S), "RC Poindimié": ("Poindimié", N), "RS Koumac": ("Koumac", N),
    "Saint Jean-Baptiste Nathalo": ("Lifou", IL), "SC Ne Drehu": ("Lifou", IL), "SS Indépendante": ("Nouméa", S),
    "Stade Français de Tadine": ("Maré", IL), "Stade Koniambo": ("Koné", N), "Thio Sport": ("Thio", S),
    "Trio Kedeigne": ("Lifou", IL), "UAC Yaté": ("Yaté", S), "US Pénélo-Cuaden": ("Maré", IL), "USC Nouméa": ("Nouméa", S),
    "USJ Wédrumel": ("Lifou", IL), "USL Gélima": ("Canala", N), "Wé-Luécilla": ("Lifou", IL),
}

# (regex sobre chave(nome) sem prefixo de associação, nome de exibição, ano inicial, ano final); a primeira que casa vale
REGRAS: list[tuple[str, str, int, int]] = [
    (r"^(magenta|le nickel)$", "AS Magenta", 1900, 2100),
    (r"^(gaitcha|gaitcha fcn|gaitcha fc|fc gaitcha)$", "Gaïtcha FC", 1900, 2100),
    (r"^gaica$", "ASC Gaïca", 1900, 2100),
    (r"^(kunie|ile des pins)$", "AS Kunié", 1900, 2100),
    (r"^baco$", "JS Baco", 1900, 2100),
    (r"^auteuil$", "AS Auteuil", 1900, 2009),
    (r"^auteuil$", "FC Auteuil", 2010, 2100),
    (r"^(saint louis|st louis)$", "CA Saint-Louis", 1900, 2100),
    (r"^(tiga|tiga sports?)$", "AS Tiga Sport", 1900, 2100),
    (r"^(horizon patho)$", "AS Horizon Patho", 1900, 2100),
    (r"^ne drehu$", "SC Ne Drehu", 1900, 2100),
    (r"^(mont dore)$", "AS Mont-Dore", 1900, 2100),
    (r"^lossi$", "AS Lössi", 1900, 2100),
    (r"^hienghene( sport)?$", "Hienghène Sport", 1900, 2100),
    (r"^thio( sports?)?$", "Thio Sport", 1900, 2100),
    (r"^(poya)$", "ACB Poya", 1900, 2100),
    (r"^poum$", "AS Poum", 1900, 2100),
    (r"^nekoue$", "CS Nékoué", 1900, 2100),
    (r"^tieta$", "JS Tiéta", 1900, 2100),
    (r"^traput$", "JS Traput", 1900, 2100),
    (r"^(pen|penelo) cu[ae]den$", "US Pénélo-Cuaden", 1900, 2100),
    (r"^kirikitr$", "AS Kirikitr", 1900, 2100),
    (r"^temala ouelisse$", "AS Témala-Ouélisse", 1900, 2100),
    (r"^wedrumel$", "USJ Wédrumel", 1900, 2100),
    (r"^olympique( noumea)?$", "Olympique Nouméa", 1900, 2100),
    (r"^koh$", "FC Koh", 1900, 2100),
    (r"^kou?a?ou?a$|^kouaoua$", "ASLN Kouaoua", 1900, 2100),
    (r"^mouli( sport)?$", "AS Mouli", 1900, 2100),
    (r"^(racing de )?poindimie$", "RC Poindimié", 1900, 2100),
    (r"^(grand nord|asgn)$", "AS Grand Nord", 1900, 2100),
    (r"^belep( mont dore)?$", "FC Bélep", 1900, 2100),
    (r"^wacaele$", "ES Wacaélé", 1900, 2100),
    (r"^dumbea( fc)?$", "Dumbéa FC", 1900, 2100),
    (r"^trio( kedeigne)?$", "Trio Kedeigne", 1900, 2100),
    (r"^qanono$", "AS Qanono", 1900, 2100),
    (r"^wetr$", "AS Wetr", 1900, 2100),
    (r"^we luec?illa$", "Wé-Luécilla", 1900, 2100),
    (r"^(usc|usc noumea)$", "USC Nouméa", 1900, 2100),
    (r"^yate$", "UAC Yaté", 1900, 2100),
    (r"^fregate$", "AS Frégate", 1900, 2100),
    (r"^independante$", "SS Indépendante", 1900, 2100),
    (r"^club sportif militaire$", "Club Sportif Militaire", 1900, 2100),
]

_PREFIXO = re.compile(r"^(as|asc|js|fc|cs|ca|ac|us|usj|usl|uac|ss|rs|rc|es|sc|acb|asln|co) (?=\S)")
_NOMES_CHAVE = {chave(n): n for n in CLUBES}


def clube(nome: str, ano: int) -> str | None:
    k = chave(re.sub(r"\s*\([^)]*\)\s*$", "", nome))   # "AS Magenta (Nouméa)": a cidade sai
    if k in _NOMES_CHAVE:
        return _NOMES_CHAVE[k]
    for kk in dict.fromkeys((_PREFIXO.sub("", k), k)):
        for rx, nome_ex, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx, kk):
                return nome_ex
        if kk in _NOMES_CHAVE:
            return _NOMES_CHAVE[kk]
    return None
