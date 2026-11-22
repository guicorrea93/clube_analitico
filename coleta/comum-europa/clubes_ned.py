"""Cadastro dos clubes holandeses, comum a todas as divisões da Holanda.

Chave: o nome de exibição no painel (como o clube é conhecido no Brasil), com cidade e país. Nomes únicos no mundo,
conferidos no banco e nos outros pacotes; "Sparta Rotterdam" e "Excelsior Rotterdam" já evitam o Sparta Praga e o
Excelsior Mouscron das próximas ligas.

Identidade:
- **mudança de nome é o mesmo clube:** Feijenoord e Feyenoord; ADO, FC Den Haag-ADO, FC Den Haag e ADO Den Haag; AZ '67 e
  AZ; SHS e Holland Sport; PEC Zwolle, PEC Zwolle '82 e FC Zwolle; DS '79, Dordrecht '90 e FC Dordrecht; FC Den Bosch '67, BVV Den Bosch e FC Den
  Bosch; HFC e SBV Haarlem; Heracles e Heracles Almelo; Xerxes e Xerxes/DHC; WVV e FC Wageningen;
- **fusão que criou clube novo é outro clube**, como na história dos clubes: FC Twente (1965; Sportclub Enschede fica à parte),
  FC Utrecht (1970; DOS e Elinkwijk à parte), FC Amsterdam (1972; DWS, Blauw-Wit e De Volewijckers à parte), Roda JC (1962;
  Rapid JC Heerlen à parte), Fortuna Sittard (1968; Fortuna '54 e Sittardia à parte), AZ '67 (1967; Alkmaar '54 à parte),
  FC Groningen (1971; GVAV à parte), FC Den Bosch (1965; o BVV de 1956-58 à parte).
  O ogol põe alguns desses na mesma ficha do sucessor (Rapid JC no Roda, Alkmaar '54 no AZ, GVAV no Groningen, os últimos
  anos do Sportclub Enschede no Twente, o BVV de 1957 no Den Bosch): `OGOL` aceita uma faixa de anos por código e separa.

OGOL: código do clube no ogol -> chave (ou [(ano_ini, ano_fim, chave)]). ALIASES: grafias das outras fontes -> chave.
POR_ANO: nomes que dependem da época. A ESPN é casada pelo código do clube (votação jogo a jogo em importar.py).
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "Ajax": ("Amsterdã", "NED"),
    "PSV": ("Eindhoven", "NED"),
    "Feyenoord": ("Roterdã", "NED"),
    "AZ Alkmaar": ("Alkmaar", "NED"),
    "Alkmaar '54": ("Alkmaar", "NED"),
    "Twente": ("Enschede", "NED"),
    "SC Enschede": ("Enschede", "NED"),
    "Utrecht": ("Utrecht", "NED"),
    "DOS Utrecht": ("Utrecht", "NED"),
    "Elinkwijk": ("Utrecht", "NED"),
    "Groningen": ("Groningen", "NED"),
    "GVAV": ("Groningen", "NED"),
    "Heerenveen": ("Heerenveen", "NED"),
    "Vitesse": ("Arnhem", "NED"),
    "NEC Nijmegen": ("Nijmegen", "NED"),
    "Willem II": ("Tilburg", "NED"),
    "NOAD": ("Tilburg", "NED"),
    "Sparta Rotterdam": ("Roterdã", "NED"),
    "Excelsior Rotterdam": ("Roterdã", "NED"),
    "ADO Den Haag": ("Haia", "NED"),
    "Holland Sport": ("Haia", "NED"),
    "NAC Breda": ("Breda", "NED"),
    "Roda JC": ("Kerkrade", "NED"),
    "Rapid JC Heerlen": ("Heerlen", "NED"),
    "Fortuna Sittard": ("Sittard", "NED"),
    "Fortuna '54": ("Geleen", "NED"),
    "Sittardia": ("Sittard", "NED"),
    "Go Ahead Eagles": ("Deventer", "NED"),
    "Heracles Almelo": ("Almelo", "NED"),
    "PEC Zwolle": ("Zwolle", "NED"),
    "RKC Waalwijk": ("Waalwijk", "NED"),
    "Volendam": ("Volendam", "NED"),
    "Cambuur": ("Leeuwarden", "NED"),
    "De Graafschap": ("Doetinchem", "NED"),
    "MVV Maastricht": ("Maastricht", "NED"),
    "VVV-Venlo": ("Venlo", "NED"),
    "Telstar": ("Velsen", "NED"),
    "Haarlem": ("Haarlem", "NED"),
    "Den Bosch": ("'s-Hertogenbosch", "NED"),
    "BVV": ("'s-Hertogenbosch", "NED"),
    "Emmen": ("Emmen", "NED"),
    "Almere City": ("Almere", "NED"),
    "RBC Roosendaal": ("Roosendaal", "NED"),
    "Helmond Sport": ("Helmond", "NED"),
    "Veendam": ("Veendam", "NED"),
    "Dordrecht": ("Dordrecht", "NED"),
    "SVV Schiedam": ("Schiedam", "NED"),
    "DWS Amsterdam": ("Amsterdã", "NED"),
    "Blauw-Wit Amsterdam": ("Amsterdã", "NED"),
    "De Volewijckers": ("Amsterdã", "NED"),
    "FC Amsterdam": ("Amsterdã", "NED"),
    "SC Eindhoven": ("Eindhoven", "NED"),
    "Xerxes": ("Roterdã", "NED"),
    "Wageningen": ("Wageningen", "NED"),
}

OGOL: dict[str, str | list[tuple[int, int, str]]] = {
    "ajax": "Ajax", "psv": "PSV", "feyenoord": "Feyenoord", "1104": "NAC Breda", "251213": "BVV", "13084": "Elinkwijk",
    "244692": "DOS Utrecht", "4983": "Sparta Rotterdam", "63851": "Fortuna '54", "7801": "SC Eindhoven", "13087": "NOAD",
    "9349": "DWS Amsterdam", "7429": "MVV Maastricht", "29238": "SC Enschede", "63846": "Rapid JC Heerlen", "5008": "VVV-Venlo",
    "260653": "GVAV", "1928": "Willem II", "13085": "Blauw-Wit Amsterdam", "13053": "Holland Sport", "13060": "Sittardia",
    "1935": "Volendam", "13086": "De Volewijckers", "5948": "Heracles Almelo", "5792": "Go Ahead Eagles", "8241": "Telstar",
    "16566": "Xerxes", "1120": "NEC Nijmegen", "4047": "Haarlem", "4048": "SVV Schiedam",
    "1114": "Utrecht", "5359": "Excelsior Rotterdam", "vitesse": "Vitesse", "10807": "FC Amsterdam", "4186": "De Graafschap",
    "13038": "Wageningen", "1938": "PEC Zwolle", "8667": "Helmond Sport", "7430": "Dordrecht", "7473": "Cambuur",
    "1929": "Heerenveen", "1934": "RKC Waalwijk", "1932": "RBC Roosendaal", "8910": "Emmen", "8972": "Almere City",
    "1937": "ADO Den Haag",
    # o ogol põe o antecessor na ficha do sucessor: separa pelos anos (início da temporada)
    "1931": [(1956, 1961, "Rapid JC Heerlen"), (1962, 9999, "Roda JC")],
    "az-alkmaar": [(1956, 1966, "Alkmaar '54"), (1967, 9999, "AZ Alkmaar")],
    "1933": [(1956, 1970, "GVAV"), (1971, 9999, "Groningen")],
    "fc-twente": [(1956, 1964, "SC Enschede"), (1965, 9999, "Twente")],
    "4485": [(1956, 1967, "Fortuna '54"), (1968, 9999, "Fortuna Sittard")],
    "4184": [(1956, 1964, "BVV"), (1965, 9999, "Den Bosch")],
}

ALIASES = {
    # engsoccerdata
    "AFC Ajax": "Ajax", "PSV Eindhoven": "PSV", "Feijenoord": "Feyenoord", "AZ '67 Alkmaar": "AZ Alkmaar",
    "VV Alkmaar '54": "Alkmaar '54", "FC Twente": "Twente", "Sportclub Enschede": "SC Enschede", "FC Utrecht": "Utrecht",
    "USV Elinkwijk": "Elinkwijk", "FC Groningen": "Groningen", "GVAV Groningen": "GVAV", "Groninger VAV": "GVAV",
    "sc Heerenveen": "Heerenveen", "NOAD Tilburg": "NOAD", "SBV Excelsior": "Excelsior Rotterdam",
    "FC Den Haag": "ADO Den Haag", "FC Den Haag-ADO": "ADO Den Haag", "Roda JC Kerkrade": "Roda JC", "FSC Geleen": "Fortuna Sittard",
    "Heracles": "Heracles Almelo", "PEC Zwolle '82": "PEC Zwolle", "FC Zwolle": "PEC Zwolle", "FC Volendam": "Volendam",
    "SC Cambuur": "Cambuur", "MVV": "MVV Maastricht", "HFC Haarlem": "Haarlem", "SBV Haarlem": "Haarlem",
    "FC Den Bosch": "Den Bosch", "FC Den Bosch '67": "Den Bosch", "BVV Den Bosch": "Den Bosch", "FC Emmen": "Emmen",
    "BV Veendam": "Veendam", "FC Dordrecht": "Dordrecht", "Dordrecht '90": "Dordrecht", "Drechtsteden '79": "Dordrecht",
    "S.V.V./Dordrecht '90": "Dordrecht", "DWS Amsterdam": "DWS Amsterdam", "Blauw Wit": "Blauw-Wit Amsterdam",
    "FC Xerxes": "Xerxes", "Xerxes/D.H.C.": "Xerxes", "FC Wageningen": "Wageningen", "WVV Wageningen": "Wageningen",
    "Almere City": "Almere City",
    # football-data
    "Den Haag": "ADO Den Haag", "For Sittard": "Fortuna Sittard", "Graafschap": "De Graafschap", "Nijmegen": "NEC Nijmegen",
    "Roda": "Roda JC", "Roosendaal": "RBC Roosendaal", "Sparta": "Sparta Rotterdam", "VVV Venlo": "VVV-Venlo",
    "Waalwijk": "RKC Waalwijk", "Zwolle": "PEC Zwolle", "Excelsior": "Excelsior Rotterdam", "Cambuur": "Cambuur",
    # RSSSF (formato antigo)
    "A.D.O.": "ADO Den Haag", "A.D.O. Den Haag": "ADO Den Haag", "A.Z.": "AZ Alkmaar", "A.Z. '67": "AZ Alkmaar",
    "Cambuur Lwrd.": "Cambuur", "D.O.S.": "DOS Utrecht", "D.S. '79": "Dordrecht", "D.W.S.": "DWS Amsterdam",
    "D.W.S./A": "DWS Amsterdam", "FC V.V.V.": "VVV-Venlo", "Fortuna SC": "Fortuna Sittard", "Fortuna Sitt.": "Fortuna Sittard",
    "G.V.A.V.": "GVAV", "Go Ahead": "Go Ahead Eagles", "Go Ahead Eag.": "Go Ahead Eagles", "M.V.V.": "MVV Maastricht",
    "N.A.C.": "NAC Breda", "N.E.C.": "NEC Nijmegen", "N.O.A.D.": "NOAD", "P.E.C. Zwolle": "PEC Zwolle", "P.S.V.": "PSV",
    "R.B.C.": "RBC Roosendaal", "R.B.C. Roosend.": "RBC Roosendaal", "R.K.C.": "RKC Waalwijk", "R.K.C. Waalw.": "RKC Waalwijk",
    "Rapid JC": "Rapid JC Heerlen", "Rapid J.C.": "Rapid JC Heerlen", "Roda J.C.": "Roda JC", "S.H.S.": "Holland Sport", "SHS": "Holland Sport",
    "SC Heerenveen": "Heerenveen", "SC Heracles": "Heracles Almelo", "SC Veendam": "Veendam", "SVV/Dordr.'90": "Dordrecht",
    "Sp. Enschede": "SC Enschede", "V.V.V.": "VVV-Venlo", "Volewijckers": "De Volewijckers", "Elinkwijk": "Elinkwijk",
    "Eindhoven": "SC Eindhoven", "Wageningen": "Wageningen", "Alkmaar": "Alkmaar '54",
    # RSSSF (lista de campeões e de artilheiros)
    "F.C. Twente": "Twente", "DWS": "DWS Amsterdam", "DOS": "DOS Utrecht", "NAC": "NAC Breda", "NEC": "NEC Nijmegen",
    "VVV": "VVV-Venlo", "Xerxes-DHC": "Xerxes", "ADO": "ADO Den Haag", "GVAV": "GVAV", "Go Ahead Eagles": "Go Ahead Eagles",
    # Wikipédia ("BVC Amsterdam" é o DWS de 1954 a 1958, o "D.W.S./A" da RSSSF)
    "VVV '03": "VVV-Venlo", "Vitesse Arnhem": "Vitesse", "Cambuur Leeuwarden": "Cambuur", "TSV NOAD": "NOAD",
    "BVC Amsterdam": "DWS Amsterdam",
}

# nomes que dependem da época (início da temporada)
POR_ANO = {
    # o engsoccerdata chama de "Fortuna Sittard" também o Fortuna '54 (1956/57-1966/67)
    # (a fusão com o Sittardia foi em 1968: em 1967/68 os dois ainda jogaram, como na tabela da RSSSF e da Wikipédia)
    "Fortuna Sittard": [(1956, 1967, "Fortuna '54"), (1968, 9999, "Fortuna Sittard")],
    "Fortuna": [(1956, 1967, "Fortuna '54"), (1968, 9999, "Fortuna Sittard")],
    # "Amsterdam" na RSSSF: o BVC Amsterdam (DWS) de 1956-1958 ou o FC Amsterdam de 1972-1978
    "Amsterdam": [(1956, 1958, "DWS Amsterdam"), (1972, 9999, "FC Amsterdam")],
    # "BVV" de 1956/57 e 1957/58 é o clube antigo; o "BVV Den Bosch" de 1988-1990 é o FC Den Bosch
    "BVV": [(1956, 1964, "BVV"), (1965, 9999, "Den Bosch")], "B.V.V.": [(1956, 1964, "BVV"), (1965, 9999, "Den Bosch")],
    # "Groningen" na Wikipédia e na RSSSF: GVAV até 1970/71, FC Groningen depois
    "Groningen": [(1956, 1970, "GVAV"), (1971, 9999, "Groningen")],
    # SVV: o de Schiedam até 1990/91; "SVV" depois da fusão com o Dordrecht '90 (1991/92) é o Dordrecht
    "SVV": [(1956, 1990, "SVV Schiedam"), (1991, 9999, "Dordrecht")], "S.V.V.": [(1956, 1990, "SVV Schiedam"),
                                                                              (1991, 9999, "Dordrecht")],
    "SVV Schiedam": [(1956, 1990, "SVV Schiedam"), (1991, 9999, "Dordrecht")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {chave(k): k for k in CLUBES}
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}

# siglas que a Wikipédia e a ESPN põem em volta do nome ("FC Utrecht", "SC Heerenveen", "AFC Ajax")
SIGLAS = {"fc", "sc", "afc", "sbv", "bv", "vv", "sv", "rkc", "pec", "hfc", "the", "de", "s"}


def _reduzir(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return "".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in SIGLAS)


_REDUZIDO: dict[str, str | None] = {}
for _nome, _c in [(k, k) for k in CLUBES] + list(ALIASES.items()):
    r = _reduzir(_nome)
    if not r:
        continue
    if _REDUZIDO.get(r, _c) != _c:
        _REDUZIDO[r] = None   # ambíguo
    else:
        _REDUZIDO.setdefault(r, _c)


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que dependem
    da época."""
    nome = nome.replace("&nbsp;", " ").replace("\xa0", " ").strip().rstrip("*").strip()
    k = chave(nome)
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k) or _REDUZIDO.get(_reduzir(nome))


def ogol(codigo: str, ano: int | None = None) -> str | None:
    v = OGOL.get(codigo)
    if isinstance(v, list):
        return next((c for ini, fim, c in v if ano is not None and ini <= ano <= fim), None)
    return v


def exibicao(chave_clube: str) -> str:
    return chave_clube
