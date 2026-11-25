"""Cadastro dos clubes tchecos, comum a todas as divisões da Tchéquia (e da Tchecoslováquia, depois).

Chave: o nome de exibição no painel (como o clube é conhecido no Brasil: "Sparta Praga", "Slavia Praga"), com cidade e
país. Nomes únicos no mundo, conferidos no banco e nos outros pacotes.

Identidade (pela linhagem do clube, como na Wikipédia: o alvo do link na tabela de cada temporada):
- o mesmo clube com nomes de patrocinador ou de época vira uma chave só: Bohemians Praha (até 2002) e Bohemians 1905; Svit,
  Tescoma, Fastav e Trinity Zlín; Boby e Zbrojovka Brno; Olpran, Petra e FK Drnovice; Dukla Příbram, Marila Příbram e
  1. FK Příbram; SK e FC Hradec Králové; FC e MFK Karviná; SIAD Most e Baník Most; Hvězda e Union Cheb;
- clubes diferentes com nome parecido ficam separados: o Dukla Praha histórico (o clube do exército, 1993/94; mudou-se
  para Příbram em 1996, e o ogol usa o mesmo código) e o FK Dukla Praha de hoje (2001); o Bohemians 1905 e o Bohemians
  de Střížkov (2008/09); o Slovácká Slavia Uherské Hradiště (1995/96) e o 1. FC Slovácko.

Os nomes das fontes trazem patrocinadores e prefixos ("SK Fomei Hradec Kralove", "FC Olpran Drnovice"); PADROES
reconhece o clube por expressões sobre o nome normalizado (minúsculas, sem acento), em ordem. OGOL: código do ogol ->
chave; OGOL_POR_ANO: códigos que o ogol usa para dois clubes.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "Sparta Praga": ("Praga", "CZE"), "Slavia Praga": ("Praga", "CZE"), "Viktoria Plzeň": ("Plzeň", "CZE"),
    "Baník Ostrava": ("Ostrava", "CZE"), "Slovan Liberec": ("Liberec", "CZE"), "Sigma Olomouc": ("Olomouc", "CZE"),
    "Zbrojovka Brno": ("Brno", "CZE"), "Mladá Boleslav": ("Mladá Boleslav", "CZE"), "Jablonec": ("Jablonec nad Nisou", "CZE"),
    "Teplice": ("Teplice", "CZE"), "Zlín": ("Zlín", "CZE"), "Hradec Králové": ("Hradec Králové", "CZE"),
    "Bohemians 1905": ("Praga", "CZE"), "FK Dukla Praga": ("Praga", "CZE"), "Dukla Praga": ("Praga", "CZE"),
    "Příbram": ("Příbram", "CZE"), "Slovácko": ("Uherské Hradiště", "CZE"), "Opava": ("Opava", "CZE"),
    "Karviná": ("Karviná", "CZE"), "Pardubice": ("Pardubice", "CZE"), "Vysočina Jihlava": ("Jihlava", "CZE"),
    "Kladno": ("Kladno", "CZE"), "Baník Most": ("Most", "CZE"), "Ústí nad Labem": ("Ústí nad Labem", "CZE"),
    "Znojmo": ("Znojmo", "CZE"), "Drnovice": ("Drnovice", "CZE"), "Chmel Blšany": ("Blšany", "CZE"),
    "Viktoria Žižkov": ("Praga", "CZE"), "Dynamo České Budějovice": ("České Budějovice", "CZE"),
    "Union Cheb": ("Cheb", "CZE"), "Vítkovice": ("Ostrava", "CZE"), "Benešov": ("Benešov", "CZE"),
    "Slovácká Slavia": ("Uherské Hradiště", "CZE"), "Lázně Bohdaneč": ("Lázně Bohdaneč", "CZE"),
    "Bohemians Střížkov": ("Praga", "CZE"), "Artis Brno": ("Brno", "CZE"),
}

# (expressão sobre o nome normalizado) -> chave; a primeira que casa vale
PADROES: list[tuple[str, str]] = [
    (r"sparta", "Sparta Praga"),
    (r"slovacka slavia|uherske hradiste|slovacka hradiste", "Slovácká Slavia"),
    (r"slavia", "Slavia Praga"),
    (r"zizkov", "Viktoria Zizkov"),
    (r"plzen", "Viktoria Plzeň"),
    (r"vitkovice", "Vítkovice"),
    (r"banik most|siad most|\bmost\b", "Baník Most"),
    (r"ostrava|\bbanik\b", "Baník Ostrava"),
    (r"liberec", "Slovan Liberec"),
    (r"olomouc|sigma", "Sigma Olomouc"),
    (r"artis", "Artis Brno"),
    (r"brno|zbrojovka", "Zbrojovka Brno"),
    (r"boleslav", "Mladá Boleslav"),
    (r"jablonec", "Jablonec"),
    (r"teplice", "Teplice"),
    (r"zlin", "Zlín"),
    (r"hradec|kralove", "Hradec Králové"),
    (r"strizkov", "Bohemians Střížkov"),
    (r"bohemians", "Bohemians 1905"),
    (r"pribram|marila", "Příbram"),
    (r"slovacko|synot", "Slovácko"),
    (r"opava", "Opava"),
    (r"karvina", "Karviná"),
    (r"pardubice", "Pardubice"),
    (r"jihlava|vysocina", "Vysočina Jihlava"),
    (r"kladno", "Kladno"),
    (r"usti", "Ústí nad Labem"),
    (r"znojmo", "Znojmo"),
    (r"drnovice", "Drnovice"),
    (r"blsany|chmel", "Chmel Blšany"),
    (r"budejovice|dynamo cb", "Dynamo České Budějovice"),
    (r"cheb", "Union Cheb"),
    (r"benesov", "Benešov"),
    (r"bohdanec", "Lázně Bohdaneč"),
]

ALIASES: dict[str, str] = {}

# nomes que dependem da época: expressão sobre o nome normalizado -> [(ano inicial, ano final, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "dukla": [(1900, 1995, "Dukla Praga"), (1996, 2000, "Příbram"), (2001, 9999, "FK Dukla Praga")],
    # "Bohemians" sozinho (RSSSF): em 2008/09 só o de Střížkov estava na liga
    "^bohemians$": [(1900, 2007, "Bohemians 1905"), (2008, 2008, "Bohemians Střížkov"), (2009, 9999, "Bohemians 1905")],
}

OGOL: dict[str, str] = {
    "sparta-praha": "Sparta Praga", "slavia-praha": "Slavia Praga", "plzen": "Viktoria Plzeň", "2058": "Baník Ostrava",
    "2061": "Slovan Liberec", "2059": "Sigma Olomouc", "2064": "Zbrojovka Brno", "4213": "Mladá Boleslav",
    "fk-jablonec": "Jablonec", "1125": "Teplice", "2060": "Zlín", "9381": "Hradec Králové", "8216": "Bohemians 1905",
    "8269": "FK Dukla Praga", "1-fc-slovacko": "Slovácko", "2065": "Opava", "15248": "Karviná", "72856": "Pardubice",
    "5880": "Vysočina Jihlava", "7837": "Kladno", "5879": "Baník Most", "9489": "Ústí nad Labem", "58803": "Znojmo",
    "4212": "Drnovice", "2069": "Chmel Blšany", "1092": "Viktoria Žižkov", "2063": "Dynamo České Budějovice",
    "34209": "Union Cheb", "268516": "Vítkovice", "93319": "Benešov", "268515": "Slovácká Slavia",
    "72407": "Lázně Bohdaneč", "9955": "Bohemians Střížkov", "72404": "Artis Brno",
}
# o mesmo código do ogol para dois clubes: o Dukla Praha histórico (1993/94) e o 1. FK Příbram (1996/97 em diante)
OGOL_POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "2066": [(1993, 1995, "Dukla Praga"), (1996, 9999, "Příbram")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


def _normal(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)|\*+|\[.*?\]", " ", s) if "strizkov" not in s else s
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]", " ", s)).strip()


_INDICE: dict[str, str] = {chave(k): k for k in CLUBES}
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_PADROES = [(re.compile(p), c) for p, c in PADROES]


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que dependem
    da época."""
    nome = re.sub(r"\s+", " ", nome.replace("&nbsp;", " ").replace("\xa0", " ").strip())
    n = _normal(nome)
    if chave(nome) in _INDICE:
        return _INDICE[chave(nome)]
    for k, faixas in POR_ANO.items():
        if re.search(rf"\b{k}\b", n) and not re.search(r"pribram|marila", n):
            return next((c for ini, fim, c in faixas if ano is not None and ini <= ano <= fim), None)
    for p, c in _PADROES:
        if p.search(n):
            return c if c in CLUBES else next(k for k in CLUBES if chave(k) == chave(c))
    return None


def ogol(codigo: str, ano: int | None = None) -> str | None:
    if codigo in OGOL_POR_ANO:
        return next((c for ini, fim, c in OGOL_POR_ANO[codigo] if ano is not None and ini <= ano <= fim), None)
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
