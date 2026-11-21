"""Cadastro dos clubes alemães, comum a todas as divisões da Alemanha.

Chave: um nome do engsoccerdata (o mais recente do clube). Valor: nome de exibição no painel (como o clube é
conhecido no Brasil), cidade e país (código FIFA). O mesmo clube tem o mesmo nome em ger-1, ger-2...

O engsoccerdata usa o nome da época: aqui as grafias do mesmo clube viram uma chave só (ALIASES), como Meidericher SV
e MSV Duisburg, Frankfurter SG Eintracht e Eintracht Frankfurt, SV Bayer 04 e Bayer Leverkusen.

ALIASES: outras grafias (engsoccerdata de outras épocas, RSSSF, football-data, ESPN, Wikipédia) -> chave. O ogol e a
ESPN são casados pelo código do clube (votação jogo a jogo em importar.py), não por aqui.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "1. FC Heidenheim": ("Heidenheim", "Heidenheim", "GER"),
    "1. FC Kaiserslautern": ("Kaiserslautern", "Kaiserslautern", "GER"),
    "1. FC Koln": ("Colônia", "Colônia", "GER"),
    "1. FC Nurnberg": ("Nuremberg", "Nuremberg", "GER"),
    "1. FC Saarbrucken": ("Saarbrücken", "Saarbrücken", "GER"),
    "1. FC Union Berlin": ("Union Berlin", "Berlim", "GER"),
    "1. FSV Mainz 05": ("Mainz 05", "Mainz", "GER"),
    "1899 Hoffenheim": ("Hoffenheim", "Sinsheim", "GER"),
    "Alemannia Aachen": ("Alemannia Aachen", "Aachen", "GER"),
    "Arminia Bielefeld": ("Arminia Bielefeld", "Bielefeld", "GER"),
    "Bayer 05 Uerdingen": ("Uerdingen", "Krefeld", "GER"),
    "Bayer Leverkusen": ("Bayer Leverkusen", "Leverkusen", "GER"),
    "Bayern Munchen": ("Bayern de Munique", "Munique", "GER"),
    "Blau-Weiss 90 Berlin": ("Blau-Weiß 90 Berlin", "Berlim", "GER"),
    "Bor. Monchengladbach": ("Borussia Mönchengladbach", "Mönchengladbach", "GER"),
    "Borussia Dortmund": ("Borussia Dortmund", "Dortmund", "GER"),
    "Borussia Neunkirchen": ("Borussia Neunkirchen", "Neunkirchen", "GER"),
    "Dynamo Dresden": ("Dynamo Dresden", "Dresden", "GER"),
    "Eintracht Braunschweig": ("Eintracht Braunschweig", "Braunschweig", "GER"),
    "Eintracht Frankfurt": ("Eintracht Frankfurt", "Frankfurt", "GER"),
    "Energie Cottbus": ("Energie Cottbus", "Cottbus", "GER"),
    "FC 08 Homburg": ("Homburg", "Homburg", "GER"),
    "FC Augsburg": ("Augsburg", "Augsburg", "GER"),
    "FC Ingolstadt 04": ("Ingolstadt", "Ingolstadt", "GER"),
    "FC Schalke 04": ("Schalke 04", "Gelsenkirchen", "GER"),
    "FC St. Pauli": ("St. Pauli", "Hamburgo", "GER"),
    "Fortuna Dusseldorf": ("Fortuna Düsseldorf", "Düsseldorf", "GER"),
    "Fortuna Koln": ("Fortuna Köln", "Colônia", "GER"),
    "Hamburger SV": ("Hamburgo", "Hamburgo", "GER"),
    "Hannover 96": ("Hannover 96", "Hannover", "GER"),
    "Hansa Rostock": ("Hansa Rostock", "Rostock", "GER"),
    "Hertha BSC": ("Hertha Berlin", "Berlim", "GER"),
    "Holstein Kiel": ("Holstein Kiel", "Kiel", "GER"),
    "Karlsruher SC": ("Karlsruhe", "Karlsruhe", "GER"),
    "Kickers Offenbach": ("Kickers Offenbach", "Offenbach", "GER"),
    "MSV Duisburg": ("Duisburg", "Duisburg", "GER"),
    "Preussen Munster": ("Preußen Münster", "Münster", "GER"),
    "RasenBallsport Leipzig": ("RB Leipzig", "Leipzig", "GER"),
    "Rot-Weiss Essen": ("Rot-Weiss Essen", "Essen", "GER"),
    "Rot-Weiss Oberhausen": ("Rot-Weiß Oberhausen", "Oberhausen", "GER"),
    "SC Freiburg": ("Freiburg", "Freiburg", "GER"),
    "SC Paderborn 07": ("Paderborn", "Paderborn", "GER"),
    "SG Wattenscheid 09": ("Wattenscheid 09", "Bochum", "GER"),
    "SSV Ulm 1846": ("Ulm", "Ulm", "GER"),
    "SV Darmstadt 98": ("Darmstadt 98", "Darmstadt", "GER"),
    "SpVgg Greuther Furth": ("Greuther Fürth", "Fürth", "GER"),
    "SpVgg Unterhaching": ("Unterhaching", "Unterhaching", "GER"),
    "Stuttgarter Kickers": ("Stuttgarter Kickers", "Stuttgart", "GER"),
    "TSV 1860 Munchen": ("1860 Munique", "Munique", "GER"),
    "Tasmania 1900 Berlin": ("Tasmania Berlin", "Berlim", "GER"),
    "TeBe Berlin": ("Tennis Borussia Berlin", "Berlim", "GER"),
    "VfB Leipzig": ("VfB Leipzig", "Leipzig", "GER"),
    "VfB Stuttgart": ("Stuttgart", "Stuttgart", "GER"),
    "VfL Bochum": ("Bochum", "Bochum", "GER"),
    "VfL Wolfsburg": ("Wolfsburg", "Wolfsburg", "GER"),
    "Waldhof Mannheim": ("Waldhof Mannheim", "Mannheim", "GER"),
    "Werder Bremen": ("Werder Bremen", "Bremen", "GER"),
    "Wuppertaler SV": ("Wuppertal", "Wuppertal", "GER"),
}

# grafias de outras fontes (e nomes de outras épocas do mesmo clube) -> chave
ALIASES: dict[str, str] = {
    # o mesmo clube com outro nome no engsoccerdata
    "Meidericher SV": "MSV Duisburg", "Frankfurter SG Eintracht": "Eintracht Frankfurt",
    "SV Bayer 04 Leverkusen": "Bayer Leverkusen",
    # RSSSF, football-data, ESPN, Wikipédia
    "1. FC Köln": "1. FC Koln", "FC Köln": "1. FC Koln", "Köln": "1. FC Koln", "Koln": "1. FC Koln", "FC Koln": "1. FC Koln",
    "1. FC Nürnberg": "1. FC Nurnberg", "Nürnberg": "1. FC Nurnberg", "Nurnberg": "1. FC Nurnberg",
    "1. FC Saarbrücken": "1. FC Saarbrucken", "Saarbrücken": "1. FC Saarbrucken", "Union Berlin": "1. FC Union Berlin",
    "Mainz": "1. FSV Mainz 05", "Mainz 05": "1. FSV Mainz 05", "FSV Mainz 05": "1. FSV Mainz 05",
    "Hoffenheim": "1899 Hoffenheim", "TSG 1899 Hoffenheim": "1899 Hoffenheim", "TSG Hoffenheim": "1899 Hoffenheim",
    "Aachen": "Alemannia Aachen", "Bielefeld": "Arminia Bielefeld", "Uerdingen": "Bayer 05 Uerdingen",
    "Bayer Uerdingen": "Bayer 05 Uerdingen", "KFC Uerdingen 05": "Bayer 05 Uerdingen", "KFC Uerdingen": "Bayer 05 Uerdingen",
    "Leverkusen": "Bayer Leverkusen", "Bayer 04 Leverkusen": "Bayer Leverkusen", "Bayern Munich": "Bayern Munchen",
    "Bayern München": "Bayern Munchen", "FC Bayern München": "Bayern Munchen", "FC Bayern Munich": "Bayern Munchen",
    "Blau-Weiß 90 Berlin": "Blau-Weiss 90 Berlin", "Blau-Weiß Berlin": "Blau-Weiss 90 Berlin",
    "M'gladbach": "Bor. Monchengladbach", "M'Gladbach": "Bor. Monchengladbach", "Borussia Mönchengladbach": "Bor. Monchengladbach",
    "Borussia Monchengladbach": "Bor. Monchengladbach", "Mönchengladbach": "Bor. Monchengladbach",
    "Dortmund": "Borussia Dortmund", "Dresden": "Dynamo Dresden", "Braunschweig": "Eintracht Braunschweig",
    "Ein Frankfurt": "Eintracht Frankfurt", "Frankfurt": "Eintracht Frankfurt", "Cottbus": "Energie Cottbus",
    "FC Energie Cottbus": "Energie Cottbus", "Homburg": "FC 08 Homburg", "Augsburg": "FC Augsburg", "Ingolstadt": "FC Ingolstadt 04",
    "Schalke 04": "FC Schalke 04", "Schalke": "FC Schalke 04", "FC Schalke 04 Gelsenkirchen": "FC Schalke 04",
    "St Pauli": "FC St. Pauli", "St. Pauli": "FC St. Pauli", "Fortuna Düsseldorf": "Fortuna Dusseldorf",
    "Dusseldorf": "Fortuna Dusseldorf", "Düsseldorf": "Fortuna Dusseldorf", "Fortuna Köln": "Fortuna Koln", "SC Fortuna Köln": "Fortuna Koln",
    "Hamburg": "Hamburger SV", "Hannover": "Hannover 96", "Hansa Rostock": "Hansa Rostock", "FC Hansa Rostock": "Hansa Rostock",
    "Hertha": "Hertha BSC", "Hertha BSC Berlin": "Hertha BSC", "Hertha Berlin": "Hertha BSC", "Kiel": "Holstein Kiel",
    "Karlsruhe": "Karlsruher SC", "Offenbach": "Kickers Offenbach", "Duisburg": "MSV Duisburg", "Preußen Münster": "Preussen Munster",
    "RB Leipzig": "RasenBallsport Leipzig", "RasenBallsport": "RasenBallsport Leipzig", "Rot-Weiß Essen": "Rot-Weiss Essen",
    "Rot-Weiß Oberhausen": "Rot-Weiss Oberhausen", "Freiburg": "SC Freiburg", "Paderborn": "SC Paderborn 07",
    "Wattenscheid": "SG Wattenscheid 09", "Ulm": "SSV Ulm 1846", "SSV Ulm": "SSV Ulm 1846", "Darmstadt": "SV Darmstadt 98",
    "Darmstadt 98": "SV Darmstadt 98", "Greuther Furth": "SpVgg Greuther Furth", "Greuther Fürth": "SpVgg Greuther Furth",
    "Furth": "SpVgg Greuther Furth", "Unterhaching": "SpVgg Unterhaching", "1860 Munich": "TSV 1860 Munchen",
    "1860 München": "TSV 1860 Munchen", "TSV 1860 München": "TSV 1860 Munchen", "Munich 1860": "TSV 1860 Munchen",
    "Tasmania Berlin": "Tasmania 1900 Berlin", "SC Tasmania 1900 Berlin": "Tasmania 1900 Berlin",
    "Tennis Borussia Berlin": "TeBe Berlin", "Leipzig": "RasenBallsport Leipzig", "Stuttgart": "VfB Stuttgart",
    "Bochum": "VfL Bochum", "Wolfsburg": "VfL Wolfsburg", "Mannheim": "Waldhof Mannheim", "SV Waldhof Mannheim": "Waldhof Mannheim",
    "Bremen": "Werder Bremen", "SV Werder Bremen": "Werder Bremen", "Wuppertal": "Wuppertaler SV", "Heidenheim": "1. FC Heidenheim",
    "Meiderich": "MSV Duisburg",
    # nomes completos da RSSSF
    "Hannover 1896": "Hannover 96", "BV 09 Borussia Dortmund": "Borussia Dortmund", "BV Borussia 09 Dortmund": "Borussia Dortmund",
    "DSC Arminia Bielefeld": "Arminia Bielefeld", "Berl. Tennis-Club Borussia": "TeBe Berlin", "FC Sankt Pauli": "FC St. Pauli",
    "Offenbacher Kickers": "Kickers Offenbach", "Offenbacher FC Kickers": "Kickers Offenbach",
    "Braunschweiger TSV Eintracht": "Eintracht Braunschweig", "Kieler SV Holstein": "Holstein Kiel",
    "Düsseldorfer TSV Fortuna": "Fortuna Dusseldorf", "Krefelder FC Uerdingen 05": "Bayer 05 Uerdingen",
    "VfL Borussia M'gladbach": "Bor. Monchengladbach", "Borussia M'gladbach": "Bor. Monchengladbach",
    "VfL Borussia Mönchengladbach": "Bor. Monchengladbach", "Wuppertaler SV Borussia": "Wuppertaler SV",
    "SG Eintracht Frankfurt": "Eintracht Frankfurt", "TSV München 1860": "TSV 1860 Munchen", "München 1860": "TSV 1860 Munchen",
    "Eintracht Frankfurt/Main": "Eintracht Frankfurt",
}

# nomes que dependem da época: nome -> [(primeiro ano, último ano, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "Leipzig": [(1993, 1993, "VfB Leipzig"), (2016, 9999, "RasenBallsport Leipzig")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and").replace("ß", "ss"))


_INDICE: dict[str, str] = {chave(v[0]): k for k, v in CLUBES.items()}   # o nome de exibição também serve
_INDICE.update({chave(k): k for k in CLUBES})
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}

# siglas que a RSSSF e a ESPN põem em volta do nome ("FC Schalke 04", "SV Werder Bremen", "1.FSV Mainz 05")
SIGLAS = {"fc", "sv", "vfb", "vfl", "tsv", "tsg", "fsv", "sc", "spvgg", "bsc", "ev", "1", "e", "v", "kfc", "msv", "ssv", "sg"}


def _reduzir(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome.replace("ß", "ss")).encode("ascii", "ignore").decode().lower()
    return "".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in SIGLAS)


_REDUZIDO: dict[str, str] = {}
for _nome, _c in [(k, k) for k in CLUBES] + [(v[0], k) for k, v in CLUBES.items()] + list(ALIASES.items()):
    _REDUZIDO.setdefault(_reduzir(_nome), _c)


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que
    dependem da época ("Leipzig")."""
    nome = nome.replace("&nbsp;", " ").replace("\xa0", " ")
    k = chave(nome.strip().rstrip("*").strip())
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k) or _REDUZIDO.get(_reduzir(nome))


def exibicao(chave_clube: str) -> str:
    return CLUBES[chave_clube][0]
