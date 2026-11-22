"""Cadastro dos clubes escoceses, comum a todas as divisões da Escócia.

Chave: o nome de exibição no painel (como o clube é conhecido no Brasil), com cidade e país. Nomes únicos no mundo,
conferidos no banco e nos outros pacotes ("Rangers" não colide com o Rangers de Talca, que no chi-1 tem a cidade no nome).

Identidade:
- o Rangers é um clube só, também depois da liquidação da empresa em 2012 (a liga e a lista oficial de campeões contam os
  títulos de antes e de depois juntos);
- "Morton" e "Greenock Morton" são o mesmo clube; "Hamilton" e "Hamilton Academical" também;
- o Airdrieonians de 1878 (dissolvido em 2002) é o único Airdrieonians que jogou a 1ª divisão;
- o Clydebank de 1914-1931 (extinto) e o de 1965-2002 são clubes diferentes: "Clydebank (1914)" e "Clydebank".

OGOL: código do clube no ogol -> chave, para os nomes do ogol que não resolvem pelo nome. ALIASES: grafias das fontes ->
chave (inclui os erros de digitação da RSSSF: "Hibermian", "Palkirk", "Ralth Rovers", "Kilmar.nock").
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "Rangers": ("Glasgow", "SCO"), "Celtic": ("Glasgow", "SCO"), "Aberdeen": ("Aberdeen", "SCO"), "Dundee": ("Dundee", "SCO"),
    "Dundee United": ("Dundee", "SCO"), "Hearts": ("Edimburgo", "SCO"), "Hibernian": ("Edimburgo", "SCO"),
    "Kilmarnock": ("Kilmarnock", "SCO"), "Motherwell": ("Motherwell", "SCO"), "Livingston": ("Livingston", "SCO"),
    "Falkirk": ("Falkirk", "SCO"), "Clyde": ("Glasgow", "SCO"), "Greenock Morton": ("Greenock", "SCO"),
    "Queen's Park": ("Glasgow", "SCO"), "Partick Thistle": ("Glasgow", "SCO"), "St Mirren": ("Paisley", "SCO"),
    "St Johnstone": ("Perth", "SCO"), "Ross County": ("Dingwall", "SCO"), "Hamilton Academical": ("Hamilton", "SCO"),
    "Raith Rovers": ("Kirkcaldy", "SCO"), "Third Lanark": ("Glasgow", "SCO"), "Airdrieonians": ("Airdrie", "SCO"),
    "Clydebank": ("Clydebank", "SCO"), "Clydebank (1914)": ("Clydebank", "SCO"), "Inverness CT": ("Inverness", "SCO"), "Gretna": ("Gretna", "SCO"),
    "Dunfermline": ("Dunfermline", "SCO"), "Dumbarton": ("Dumbarton", "SCO"), "Albion Rovers": ("Coatbridge", "SCO"),
    "Ayr United": ("Ayr", "SCO"), "Arbroath": ("Arbroath", "SCO"), "Cowdenbeath": ("Cowdenbeath", "SCO"),
    "East Fife": ("Methil", "SCO"), "Alloa Athletic": ("Alloa", "SCO"), "Stirling Albion": ("Stirling", "SCO"),
    "Queen of the South": ("Dumfries", "SCO"), "St Bernard's": ("Edimburgo", "SCO"), "Leith Athletic": ("Edimburgo", "SCO"),
    "Renton": ("Renton", "SCO"), "Vale of Leven": ("Alexandria", "SCO"), "Abercorn": ("Paisley", "SCO"),
    "Cowlairs": ("Glasgow", "SCO"), "Cambuslang": ("Cambuslang", "SCO"), "Port Glasgow Athletic": ("Port Glasgow", "SCO"),
    "Bo'ness": ("Bo'ness", "SCO"), "East Stirlingshire": ("Falkirk", "SCO"), "King's Park": ("Stirling", "SCO"),
}

OGOL: dict[str, str] = {
    "rangers": "Rangers", "celtic": "Celtic", "hearts": "Hearts", "1874": "Aberdeen", "8936": "Airdrieonians",
    "7847": "Clyde", "12193": "Clydebank", "1051": "Dundee", "1871": "Dundee United", "5172": "Falkirk",
    "8440": "Hamilton Academical", "1872": "Hibernian", "1873": "Kilmarnock", "1869": "Livingston", "9247": "Greenock Morton",
    "1870": "Motherwell", "1875": "Partick Thistle", "9250": "Queen's Park", "5431": "Raith Rovers", "8967": "Ross County",
    "7781": "St Johnstone", "7775": "St Mirren", "34388": "Third Lanark", "252621": "Clydebank (1914)", "48181": "Bo'ness",
}

ALIASES = {
    # engsoccerdata e football-data
    "Inverness C": "Inverness CT", "Partick": "Partick Thistle", "Raith Rvs": "Raith Rovers", "Hamilton": "Hamilton Academical",
    "Dunfermline Athletic": "Dunfermline",
    # ogol
    "Dundee FC": "Dundee", "Morton FC": "Greenock Morton", "Morton": "Greenock Morton", "Queen´s Park": "Queen's Park",
    "Airdrieonians (1878)": "Airdrieonians", "St. Johnstone": "St Johnstone", "St. Mirren": "St Mirren",
    # RSSSF
    "Heart Of Midlothian": "Hearts", "Heart of Midlothian": "Hearts", "Hibermian": "Hibernian", "Palkirk": "Falkirk",
    "Ralth Rovers": "Raith Rovers", "Kilmar.nock": "Kilmarnock", "Hamilton Academicals": "Hamilton Academical",
    "St.Johnstone": "St Johnstone", "St.Mirren": "St Mirren", "St.Bernard's": "St Bernard's", "St. Bernard's": "St Bernard's",
    "Stirling Alb.": "Stirling Albion", "Queen Of The South": "Queen of the South", "Vale Of Leven": "Vale of Leven",
    "Inverness Caledonian Thistle": "Inverness CT", "Inverness CT": "Inverness CT",
    "Inverness Caled. Th.": "Inverness CT", "Saint Johnstone": "St Johnstone", "Saint Mirren": "St Mirren",
    "Hamilton Accies": "Hamilton Academical", "Dunfermline Ath": "Dunfermline", "Alloa": "Alloa Athletic", "Dmdee": "Dundee", "3rd LRV": "Third Lanark", "3rd Lanark RV": "Third Lanark",
    "Third Lanark RV": "Third Lanark",
}

# o Clydebank de 1914-1931 (extinto) e o de 1965-2002 são clubes diferentes, como no ogol
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "Clydebank": [(1890, 1940, "Clydebank (1914)"), (1941, 9999, "Clydebank")],
    # a RSSSF põe "Stirling Albion" em 1932/33, mas o clube só existe desde 1945: ali é o East Stirlingshire
    "Stirling Albion": [(1890, 1944, "East Stirlingshire"), (1945, 9999, "Stirling Albion")],
    # a RSSSF escreve "Abercorn" no lugar do Aberdeen em 1927/28 (o Abercorn não jogou a 1ª divisão depois de 1914/15)
    "Abercorn": [(1890, 1920, "Abercorn"), (1921, 9999, "Aberdeen")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {chave(k): k for k in CLUBES}
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}

# siglas que a Wikipédia e a ESPN põem em volta do nome ("Aberdeen FC", "Heart of Midlothian F.C.")
SIGLAS = {"fc", "f", "c", "afc", "the"}


def _reduzir(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return "".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in SIGLAS)


_REDUZIDO: dict[str, str | None] = {}
for _nome, _c in [(k, k) for k in CLUBES] + list(ALIASES.items()):
    r = _reduzir(_nome)
    if not r:
        continue
    if _REDUZIDO.get(r, _c) != _c:
        _REDUZIDO[r] = None
    else:
        _REDUZIDO.setdefault(r, _c)


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer)."""
    nome = nome.replace("&nbsp;", " ").replace("\xa0", " ").strip().rstrip("*").strip()
    nome = re.sub(r"\s+", " ", nome)
    k = chave(nome)
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k) or _REDUZIDO.get(_reduzir(nome))


def ogol(codigo: str, ano: int | None = None) -> str | None:
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
