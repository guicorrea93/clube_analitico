"""Cadastro dos clubes dinamarqueses (den-1).

Chave: o nome de exibição no painel, o nome curto usado no Brasil e na Dinamarca ("Copenhague", "Brøndby", "AGF", "AaB",
"KB", "B.93"). Nomes únicos no mundo, conferidos no banco e nos outros pacotes.

Identidade (27/11/2026): pelo alvo do link da Wikipédia em cada temporada (LINKS), seguindo os redirecionamentos. Pelos
links, são o mesmo clube: Horsens fS e AC Horsens; Farum BK e FC Nordsjælland; Haderslev FK e SønderjyskE; B 1901 e
Nykøbing FC; Helsingør IF e FC Helsingør; Næstved IF e Næstved BK. Ficam separados: KB, B 1903 e FC København (a fusão de
1992; a RSSSF conta os títulos à parte); Køge BK e HB Køge; Herfølge e HB Køge.

Nas fontes sem link: OGOL (código do ogol -> chave) e PADROES (nome normalizado -> chave), para o football-data, a ESPN e a
RSSSF.
"""
from __future__ import annotations

import re
import unicodedata

CPH = "Copenhague"
CLUBES = {
    "Copenhague": (CPH, "DEN"), "KB": (CPH, "DEN"), "B 1903": (CPH, "DEN"), "B.93": (CPH, "DEN"), "AB": ("Gladsaxe", "DEN"),
    "Frem": (CPH, "DEN"), "Fremad Amager": (CPH, "DEN"), "B 1908": (CPH, "DEN"), "BK Union": (CPH, "DEN"),
    "Brønshøj": (CPH, "DEN"), "Vanløse": (CPH, "DEN"), "KFUM København": (CPH, "DEN"), "Østerbro BK": (CPH, "DEN"),
    "Hvidovre": ("Hvidovre", "DEN"), "Kastrup": ("Kastrup", "DEN"), "Dragør": ("Dragør", "DEN"),
    "Hellerup": ("Hellerup", "DEN"), "Skovshoved": ("Klampenborg", "DEN"), "Brøndby": ("Brøndby", "DEN"),
    "Lyngby": ("Lyngby", "DEN"), "Nordsjælland": ("Farum", "DEN"), "Helsingør": ("Helsingør", "DEN"),
    "Køge": ("Køge", "DEN"), "HB Køge": ("Køge", "DEN"), "Herfølge": ("Herfølge", "DEN"), "Næstved": ("Næstved", "DEN"),
    "Holbæk": ("Holbæk", "DEN"), "Slagelse": ("Slagelse", "DEN"), "Vestsjælland": ("Slagelse", "DEN"),
    "Nykøbing FC": ("Nykøbing Falster", "DEN"), "Haslev": ("Haslev", "DEN"), "Nakskov": ("Nakskov", "DEN"),
    "OB": ("Odense", "DEN"), "B 1909": ("Odense", "DEN"), "B 1913": ("Odense", "DEN"), "AGF": ("Aarhus", "DEN"),
    "Aarhus Fremad": ("Aarhus", "DEN"), "VSK Aarhus": ("Aarhus", "DEN"), "AaB": ("Aalborg", "DEN"),
    "Aalborg Chang": ("Aalborg", "DEN"), "Esbjerg": ("Esbjerg", "DEN"), "Vejle": ("Vejle", "DEN"),
    "AC Horsens": ("Horsens", "DEN"), "Silkeborg": ("Silkeborg", "DEN"), "Ikast": ("Ikast", "DEN"),
    "Midtjylland": ("Herning", "DEN"), "Herning Fremad": ("Herning", "DEN"), "Viborg": ("Viborg", "DEN"),
    "Randers": ("Randers", "DEN"), "Randers Freja": ("Randers", "DEN"), "Hobro": ("Hobro", "DEN"),
    "Vendsyssel": ("Hjørring", "DEN"), "Frederikshavn": ("Frederikshavn", "DEN"), "SønderjyskE": ("Haderslev", "DEN"),
    "Kolding": ("Kolding", "DEN"), "Fredericia": ("Fredericia", "DEN"), "Ringkøbing": ("Ringkøbing", "DEN"),
    # sem artigo na Wikipédia em inglês
    "AIA Aarhus": ("Aarhus", "DEN"), "Velo": (CPH, "DEN"), "Frederiksborg IF": ("Hillerød", "DEN"),
    "Holbæk IF": ("Holbæk", "DEN"), "Viking Rønne": ("Rønne", "DEN"), "Korsør": ("Korsør", "DEN"),
    "Roskilde": ("Roskilde", "DEN"), "Rønne BK": ("Rønne", "DEN"), "Svendborg": ("Svendborg", "DEN"),
    "Toreby-Grænge": ("Toreby", "DEN"), "Vejen": ("Vejen", "DEN"),
    # só na tabela da RSSSF de 1928/29 (BK Viktoria: Copenhague provável, sem confirmação na fonte)
    "Aalborg Freja": ("Aalborg", "DEN"), "Fredericia BK": ("Fredericia", "DEN"), "Frem Saxkøbing": ("Sakskøbing", "DEN"),
    "BK Viktoria": (CPH, "DEN"),
}

# alvo do link da Wikipédia (en), já com os redirecionamentos -> chave
LINKS = {
    "AC Horsens": "AC Horsens", "Horsens fS": "AC Horsens", "Horsens Forenede Sportsklubber": "AC Horsens",
    "AaB Fodbold": "AaB", "Aalborg BK": "AaB", "Aalborg Chang": "Aalborg Chang", "Aarhus Fremad": "Aarhus Fremad",
    "Aarhus Gymnastikforening": "AGF", "Aarhus GF": "AGF", "Aarhus Gymnastik Forening": "AGF", "AGF Aarhus": "AGF",
    "Akademisk Boldklub": "AB", "Akademisk Boldklub Gladsaxe": "AB", "BK Herning Fremad": "Herning Fremad",
    "Herning Fremad": "Herning Fremad", "Boldklubben 1903": "B 1903", "B 1903": "B 1903", "Boldklubben 1908": "B 1908",
    "Boldklubben 1909": "B 1909", "B 1909": "B 1909", "Boldklubben 1913": "B 1913", "Boldklubben Frem": "Frem",
    "BK Frem": "Frem", "Boldklubben Union": "BK Union", "BK Union": "BK Union", "Boldklubben af 1893": "B.93",
    "B.93": "B.93", "Boldklubben 1893": "B.93", "Brøndby IF": "Brøndby", "Brønshøj Boldklub": "Brønshøj",
    "Brønshøj BK": "Brønshøj", "Dragør Boldklub": "Dragør", "Esbjerg fB": "Esbjerg", "Esbjerg FB": "Esbjerg",
    "F.C. Copenhagen": "Copenhague", "FC Copenhagen": "Copenhague", "FC København": "Copenhague",
    "FC Fredericia": "Fredericia", "FC Helsingør": "Helsingør", "Helsingør IF": "Helsingør", "FC Midtjylland": "Midtjylland",
    "FC Nordsjælland": "Nordsjælland", "Farum BK": "Nordsjælland", "FC Vestsjælland": "Vestsjælland",
    "Frederikshavn fI": "Frederikshavn", "Fremad Amager": "Fremad Amager", "BK Fremad Amager": "Fremad Amager",
    "HB Køge": "HB Køge", "Haslev": "Haslev", "Hellerup IK": "Hellerup", "Herfølge Boldklub": "Herfølge",
    "Herfølge BK": "Herfølge", "Hobro IK": "Hobro", "Holbæk B&I": "Holbæk", "Hvidovre IF": "Hvidovre", "Ikast FS": "Ikast",
    "Ikast fS": "Ikast", "KFUMs Boldklub København": "KFUM København", "KFUM's Boldklub (Copenhagen)": "KFUM København",
    "KFUMs Boldklub": "KFUM København", "Kastrup Boldklub": "Kastrup", "Kastrup BK": "Kastrup",
    "Kjøbenhavns Boldklub": "KB", "Kolding IF": "Kolding", "Køge Boldklub": "Køge", "Køge BK": "Køge", "Koge BK": "Køge",
    "Lyngby Boldklub": "Lyngby", "Lyngby BK": "Lyngby", "Lyngby FC": "Lyngby", "Nakskov": "Nakskov",
    "Nykøbing FC": "Nykøbing FC", "B 1901": "Nykøbing FC", "Boldklubben 1901": "Nykøbing FC",
    "Boldklubben_1901": "Nykøbing FC", "Nykøbing Falster Boldklub af 1901": "Nykøbing FC", "Næstved Boldklub": "Næstved",
    "Naestved IF": "Næstved", "Næstved BK": "Næstved", "Næstved IF": "Næstved", "Odense Boldklub": "OB", "Odense BK": "OB",
    "Randers FC": "Randers", "Randers Sportsklub Freja": "Randers Freja", "Randers Freja": "Randers Freja",
    "Ringkøbing IF": "Ringkøbing", "Silkeborg IF": "Silkeborg", "Skovshoved IF": "Skovshoved", "Slagelse B&I": "Slagelse",
    "Sønderjyske Fodbold": "SønderjyskE", "SønderjyskE Fodbold": "SønderjyskE", "Haderslev FK": "SønderjyskE",
    "VSK Aarhus": "VSK Aarhus", "IK Skovbakken": "VSK Aarhus", "Vanløse IF": "Vanløse", "Vejle Boldklub": "Vejle",
    "Vejle BK": "Vejle", "Vendsyssel FF": "Vendsyssel", "Viborg FF": "Viborg", "Østerbros Boldklub": "Østerbro BK",
    "Arbejdernes Idrætsklub Aarhus": "AIA Aarhus", "Boldklubben Velo": "Velo", "Frederiksborg IF": "Frederiksborg IF",
    "Holbæk IF": "Holbæk IF", "IK Viking Rønne": "Viking Rønne", "Korsør Boldklub": "Korsør",
    "Roskilde Boldklub af 1906": "Roskilde", "Rønne BK": "Rønne BK", "Rønne Boldklub": "Rønne BK",
    "Svendborg Boldklub": "Svendborg", "Toreby-Grænge BK": "Toreby-Grænge", "Vejen SF": "Vejen",
}

OGOL = {
    "1867": "AB", "5888": "AC Horsens", "1863": "AGF", "1861": "AaB", "8709": "Aarhus Fremad", "9279": "B 1903",
    "9348": "B 1909", "3795": "B.93", "brondby-if": "Brøndby", "1048": "Esbjerg", "44501": "Helsingør",
    "fc-kobenhavn": "Copenhague", "30247": "Vestsjælland", "1050": "Nordsjælland", "8712": "Fredericia", "1866": "Frem",
    "8711": "Fremad Amager", "29943": "HB Køge", "5889": "SønderjyskE", "1865": "Herfølge", "42093": "Hobro",
    "5363": "Hvidovre", "5246": "Ikast", "8708": "Køge", "5093": "Lyngby", "midtjylland": "Midtjylland", "8706": "Næstved",
    "1049": "OB", "randers": "Randers", "4271": "Silkeborg", "7784": "Vejle", "31132": "Vendsyssel", "viborg": "Viborg",
}

# (expressão sobre o nome normalizado: minúsculas, sem acento) -> chave; a primeira que casa vale
PADROES: list[tuple[str, str]] = [
    (r"copenhagen|kobenhavn$|^fck", "Copenhague"), (r"brondby", "Brøndby"), (r"midtjylland", "Midtjylland"),
    (r"nordsjaelland|farum", "Nordsjælland"), (r"aarhus fremad", "Aarhus Fremad"), (r"aarhus|^agf", "AGF"),
    (r"aalborg|^aab", "AaB"), (r"odense|^ob$", "OB"), (r"silkeborg", "Silkeborg"), (r"randers", "Randers"),
    (r"viborg", "Viborg"), (r"vejle", "Vejle"), (r"esbjerg", "Esbjerg"), (r"lyngby", "Lyngby"), (r"horsens", "AC Horsens"),
    (r"sonderjysk|haderslev", "SønderjyskE"), (r"hobro", "Hobro"), (r"vendsyssel", "Vendsyssel"),
    (r"helsingor", "Helsingør"), (r"fredericia", "Fredericia"), (r"hvidovre", "Hvidovre"), (r"^hb koge", "HB Køge"),
    (r"koge", "Køge"), (r"herfolge", "Herfølge"), (r"naestved", "Næstved"), (r"ikast", "Ikast"),
    (r"vestsjaelland", "Vestsjælland"), (r"fremad amager", "Fremad Amager"), (r"^frem$|bk frem", "Frem"),
    (r"^ab$|akademisk", "AB"), (r"^kb$", "KB"), (r"b ?1903", "B 1903"), (r"b ?1909", "B 1909"), (r"b ?1913", "B 1913"),
    (r"b ?93", "B.93"),
]


def _normal(s: str) -> str:
    s = s.replace("ø", "o").replace("Ø", "O").replace("æ", "ae").replace("Æ", "Ae").replace("å", "a").replace("Å", "A")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9/]", " ", s)).strip()


_INDICE = {_normal(k): k for k in CLUBES}
_PADROES = [(re.compile(p), c) for p, c in PADROES]
_SIGLAS = {"fc", "bk", "if", "fb", "ff", "ik", "fs", "boldklub", "fodbold"}


def link(alvo: str | None) -> str | None:
    return LINKS.get((alvo or "").strip())


def esd(nome: str) -> str | None:
    n = _normal(nome)
    sem = " ".join(w for w in n.split() if w not in _SIGLAS)
    for x in (n, sem):
        if x in _INDICE:
            return _INDICE[x]
    for p, c in _PADROES:
        if p.search(n) or p.search(sem):
            return c
    return None


def ogol(codigo: str, temporada: str | None = None) -> str | None:
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
