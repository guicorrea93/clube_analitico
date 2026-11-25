"""Cadastro dos clubes noruegueses (nor-1).

Chave: o nome de exibição no painel, o nome curto usado no Brasil e na Noruega ("Rosenborg", "Bodø/Glimt", "Vålerenga");
nome genérico leva a cidade ("Fram Larvik", "Sparta Sarpsborg", "Kvik Trondheim"). Nomes únicos no mundo, conferidos no
banco e nos outros pacotes.

Identidade (25/11/2026): pelo alvo do link da Wikipédia em cada temporada (LINKS), seguindo os redirecionamentos. O clube e
o seu departamento de futebol com artigos separados são o mesmo clube (Vålerengens IF e Vålerenga Fotball, como a RSSSF;
Mjøndalen, Sogndal, Ranheim, Strømsgodset, Kongsvinger, Raufoss, Strindheim, SFK Lyn e Lyn Fotball). Clubes refundados
com outro nome e artigo próprio ficam separados: Sarpsborg FK x Sarpsborg 08, Kristiansund FK x Kristiansund BK,
Sandefjord BK x Sandefjord Fotball (fundado em 1998), Hamar IL x HamKam.

Nas fontes sem link: OGOL (código do ogol -> chave, com OGOL_TEMPORADA quando o código cobre dois clubes) e PADROES
(nome normalizado -> chave), para o football-data, a ESPN e a RSSSF.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "Aalesund": ("Ålesund", "NOR"), "Asker": ("Asker", "NOR"), "Bryne": ("Bryne", "NOR"),
    "Clausenengen": ("Kristiansund", "NOR"), "Drammens BK": ("Drammen", "NOR"), "Drøbak-Frogn": ("Drøbak", "NOR"),
    "Voss": ("Vossevangen", "NOR"), "Bodø/Glimt": ("Bodø", "NOR"), "Donn": ("Kristiansand", "NOR"),
    "Eik Tønsberg": ("Tønsberg", "NOR"), "Haugesund": ("Haugesund", "NOR"), "Jerv": ("Grimstad", "NOR"),
    "Kvik Trondheim": ("Trondheim", "NOR"), "Mandalskameratene": ("Mandal", "NOR"), "Mjølner": ("Narvik", "NOR"),
    "Vidar": ("Stavanger", "NOR"), "Vigør": ("Kristiansand", "NOR"), "Ørn Horten": ("Horten", "NOR"),
    "Flekkefjord": ("Flekkefjord", "NOR"), "Fredensborg": ("Oslo", "NOR"), "Fredrikstad": ("Fredrikstad", "NOR"),
    "Frigg": ("Oslo", "NOR"), "Fyllingen": ("Bergen", "NOR"), "Geithus": ("Geithus", "NOR"),
    "Greåker": ("Sarpsborg", "NOR"), "Halsen": ("Larvik", "NOR"), "Hamar IL": ("Hamar", "NOR"), "HamKam": ("Hamar", "NOR"),
    "Hønefoss": ("Hønefoss", "NOR"), "Birkebeineren": ("Krokstadelva", "NOR"), "IF Borg": ("Skien", "NOR"),
    "Fram Larvik": ("Larvik", "NOR"), "Skiens Grane": ("Skien", "NOR"), "Tønsberg-Kameratene": ("Tønsberg", "NOR"),
    "Urædd": ("Porsgrunn", "NOR"), "Grane Arendal": ("Arendal", "NOR"), "Start": ("Kristiansand", "NOR"),
    "Braatt": ("Kristiansund", "NOR"), "Brodd": ("Stavanger", "NOR"), "Hødd": ("Ulsteinvik", "NOR"),
    "Sparta Sarpsborg": ("Sarpsborg", "NOR"), "Varegg": ("Bergen", "NOR"), "Jevnaker": ("Jevnaker", "NOR"),
    "KFUM Oslo": ("Oslo", "NOR"), "Kjelsås": ("Oslo", "NOR"), "Kongsberg": ("Kongsberg", "NOR"),
    "Kongsvinger": ("Kongsvinger", "NOR"), "Kristiansund BK": ("Kristiansund", "NOR"),
    "Kristiansund FK": ("Kristiansund", "NOR"), "Kvik Halden": ("Halden", "NOR"), "Larvik Turn": ("Larvik", "NOR"),
    "Lillestrøm": ("Lillestrøm", "NOR"), "Lisleby": ("Fredrikstad", "NOR"), "Lyn": ("Oslo", "NOR"),
    "Mjøndalen": ("Mjøndalen", "NOR"), "Moelven": ("Moelv", "NOR"), "Molde": ("Molde", "NOR"), "Moss": ("Moss", "NOR"),
    "Neset": ("Frosta", "NOR"), "Nydalen": ("Oslo", "NOR"), "Nymark": ("Bergen", "NOR"), "Odd": ("Skien", "NOR"),
    "Orkanger": ("Orkanger", "NOR"), "Os": ("Osøyro", "NOR"), "Pors": ("Porsgrunn", "NOR"), "Ranheim": ("Trondheim", "NOR"),
    "Raufoss": ("Raufoss", "NOR"), "Rosenborg": ("Trondheim", "NOR"), "Drafn": ("Drammen", "NOR"),
    "Skiold": ("Drammen", "NOR"), "Brage Trondheim": ("Trondheim", "NOR"), "Brann": ("Bergen", "NOR"),
    "Djerv Bergen": ("Bergen", "NOR"), "Djerv 1919": ("Haugesund", "NOR"), "Falken": ("Trondheim", "NOR"),
    "Freidig": ("Trondheim", "NOR"), "Gjøvik-Lyn": ("Gjøvik", "NOR"), "Hardy": ("Bergen", "NOR"),
    "Haugar": ("Haugesund", "NOR"), "Nationalkameratene": ("Trondheim", "NOR"), "Nessegutten": ("Levanger", "NOR"),
    "Rapid Moss": ("Moss", "NOR"), "Rollon": ("Ålesund", "NOR"), "Snøgg": ("Notodden", "NOR"),
    "Sprint-Jeløy": ("Moss", "NOR"), "Strong Oslo": ("Oslo", "NOR"), "Vard Haugesund": ("Haugesund", "NOR"),
    "Sandaker": ("Oslo", "NOR"), "Sandefjord BK": ("Sandefjord", "NOR"), "Sandefjord": ("Sandefjord", "NOR"),
    "Sandnes Ulf": ("Sandnes", "NOR"), "Sarpsborg 08": ("Sarpsborg", "NOR"), "Sarpsborg FK": ("Sarpsborg", "NOR"),
    "Selbak": ("Fredrikstad", "NOR"), "Skeid": ("Oslo", "NOR"), "Skiens BK": ("Skien", "NOR"),
    "Slemmestad": ("Slemmestad", "NOR"), "Sogndal": ("Sogndal", "NOR"), "Stabæk": ("Bærum", "NOR"),
    "Stavanger IF": ("Stavanger", "NOR"), "Steinkjer": ("Steinkjer", "NOR"), "Storm Skien": ("Skien", "NOR"),
    "Strindheim": ("Trondheim", "NOR"), "Strømmen": ("Strømmen", "NOR"), "Strømsgodset": ("Drammen", "NOR"),
    "Tistedalen": ("Halden", "NOR"), "Torp": ("Fredrikstad", "NOR"), "Tromsø": ("Tromsø", "NOR"),
    "Tønsberg Turn": ("Tønsberg", "NOR"), "Ullensaker/Kisa": ("Jessheim", "NOR"), "Verdal": ("Verdal", "NOR"),
    "Viking": ("Stavanger", "NOR"), "Vålerenga": ("Oslo", "NOR"), "Ålgård": ("Ålgård", "NOR"), "Årstad": ("Bergen", "NOR"),
    # sem artigo na Wikipédia em inglês
    "Berger": ("Svelvik", "NOR"), "Fremad Lillehammer": ("Lillehammer", "NOR"), "Holmestrand": ("Holmestrand", "NOR"),
    "Nordlandet": ("Kristiansund", "NOR"), "Kapp": ("Kapp", "NOR"), "Kragerø": ("Kragerø", "NOR"), "Minde": ("Bergen", "NOR"),
    "Nordnes": ("Bergen", "NOR"), "Gjøa": ("Bergen", "NOR"), "Jarl": ("Stavanger", "NOR"), "Mesna": ("Lillehammer", "NOR"),
    "Viggo": ("Trondheim", "NOR"), "Skreia": ("Skreia", "NOR"), "Ulefoss": ("Ulefoss", "NOR"), "Vardal": ("Gjøvik", "NOR"),
    "Veblungsnes": ("Åndalsnes", "NOR"), "Sørfjell": ("Arendal", "NOR"),
}

# nomes sem link nas tabelas da Wikipédia (en) -> chave, pela Wikipédia em norueguês
VISIVEIS = {"Fjell": "Sørfjell"}   # 1938/39, Distrito V: [[Idrettslaget Sørfjell|Fjell]] (Eydehavn, Arendal)

# alvo do link da Wikipédia (en), já com os redirecionamentos -> chave
LINKS = {
    "Aalesunds FK": "Aalesund", "Asker Fotball": "Asker", "Bryne FK": "Bryne", "Clausenengen FK": "Clausenengen",
    "Drammens BK": "Drammens BK", "Drøbak-Frogn IL": "Drøbak-Frogn", "Drøbak/Frogn IL": "Drøbak-Frogn",
    "FBK Voss": "Voss", "FK Bodø/Glimt": "Bodø/Glimt", "Bodø/Glimt": "Bodø/Glimt", "FK Donn": "Donn",
    "FK Eik Tønsberg": "Eik Tønsberg", "Eik-Tønsberg": "Eik Tønsberg", "FK Haugesund": "Haugesund", "FK Jerv": "Jerv",
    "FK Kvik": "Kvik Trondheim", "FK Mandalskameratene": "Mandalskameratene", "FK Mjølner": "Mjølner", "FK Vidar": "Vidar",
    "FK Vigør": "Vigør", "FK Ørn Horten": "Ørn Horten", "FK Ørn-Horten": "Ørn Horten", "Flekkefjord FK": "Flekkefjord",
    "Fredensborg": "Fredensborg", "Fredensborg SBK": "Fredensborg", "Fredrikstad FK": "Fredrikstad", "Frigg Oslo FK": "Frigg",
    "Fyllingen Fotball": "Fyllingen", "Geithus IL": "Geithus", "Greåker IF": "Greåker", "Halsen IF": "Halsen",
    "Hamar IL": "Hamar IL", "Hamarkameratene": "HamKam", "Ham-Kam": "HamKam", "HamKam": "HamKam",
    "Hønefoss BK": "Hønefoss", "IF Birkebeineren": "Birkebeineren", "IF Borg": "IF Borg", "IF Fram Larvik": "Fram Larvik",
    "Fram Larvik": "Fram Larvik", "IF Skiens Grane": "Skiens Grane", "IF Tønsberg-Kameratene": "Tønsberg-Kameratene",
    "IF Urædd": "Urædd", "IK Grane": "Grane Arendal", "IK Start": "Start", "IL Braatt": "Braatt", "IL Brodd": "Brodd",
    "BK Brodd": "Brodd", "IL Hødd": "Hødd", "IL Sparta": "Sparta Sarpsborg", "IL Varegg": "Varegg", "Jevnaker IF": "Jevnaker",
    "KFUM-Kameratene Oslo": "KFUM Oslo", "Kjelsås Fotball": "Kjelsås", "Kongsberg IF": "Kongsberg",
    "Kongsvinger IL": "Kongsvinger", "Kongsvinger IL Toppfotball": "Kongsvinger", "KIL Toppfotball": "Kongsvinger",
    "Kristiansund BK": "Kristiansund BK", "Kristiansund FK": "Kristiansund FK", "Kvik Halden FK": "Kvik Halden",
    "Larvik Turn": "Larvik Turn", "Larvik Turn & IF": "Larvik Turn", "Lillestrøm SK": "Lillestrøm", "Lisleby FK": "Lisleby",
    "Lyn Fotball": "Lyn", "FK Lyn": "Lyn", "SFK Lyn": "Lyn", "Mjøndalen IF": "Mjøndalen", "Mjøndalen IF Fotball": "Mjøndalen",
    "Moelven IL": "Moelven", "Molde FK": "Molde", "Moss FK": "Moss", "Neset FK": "Neset", "Nydalens SK": "Nydalen",
    "Nydalen SK": "Nydalen", "Nymark IL": "Nymark", "Odds BK": "Odd", "Odd Grenland": "Odd", "Orkanger IF": "Orkanger",
    "Os TF": "Os", "Pors Fotball": "Pors", "IF Pors": "Pors", "Pors Grenland": "Pors", "Ranheim Fotball": "Ranheim",
    "Ranheim IL": "Ranheim", "Raufoss IL": "Raufoss", "Raufoss Fotball": "Raufoss", "Rosenborg BK": "Rosenborg",
    "SBK Drafn": "Drafn", "SK Drafn": "Drafn", "SBK Skiold": "Skiold", "SK Brage": "Brage Trondheim", "SK Brann": "Brann",
    "SK Djerv": "Djerv Bergen", "SK Djerv 1919": "Djerv 1919", "SK Falken": "Falken", "SK Freidig": "Freidig",
    "SK Gjøvik-Lyn": "Gjøvik-Lyn", "SK Hardy": "Hardy", "SK Haugar": "Haugar", "SK Nationalkameratene": "Nationalkameratene",
    "SK Nessegutten": "Nessegutten", "SK Rapid (Norway)": "Rapid Moss", "SK Rollon": "Rollon", "SPK Rollon": "Rollon",
    "SK Snøgg": "Snøgg", "SK Sprint-Jeløy": "Sprint-Jeløy", "SK Strong": "Strong Oslo", "SK Vard Haugesund": "Vard Haugesund",
    "Sandaker SFK": "Sandaker", "Sandefjord BK": "Sandefjord BK", "Sandefjord Fotball": "Sandefjord",
    "Sandnes Ulf": "Sandnes Ulf", "Ulf-Sandnes": "Sandnes Ulf", "Sarpsborg 08 FF": "Sarpsborg 08",
    "Sarpsborg FK": "Sarpsborg FK", "Selbak TIF": "Selbak", "Skeid Fotball": "Skeid", "Skiens BK": "Skiens BK",
    "Slemmestad IF": "Slemmestad", "Sogndal Fotball": "Sogndal", "Sogndal IL": "Sogndal", "Stabæk Fotball": "Stabæk",
    "Stavanger IF Fotball": "Stavanger IF", "Steinkjer FK": "Steinkjer", "Storms BK": "Storm Skien", "Storm BK": "Storm Skien",
    "Strindheim IL": "Strindheim", "Strindheim Fotball": "Strindheim", "Strømmen IF": "Strømmen",
    "Strømsgodset IF": "Strømsgodset", "Strømsgodset Toppfotball": "Strømsgodset", "Tistedalens TIF": "Tistedalen",
    "Torp IF": "Torp", "Tromsø IL": "Tromsø", "Tønsbergs TF": "Tønsberg Turn", "Tønsberg TF": "Tønsberg Turn",
    "Ullensaker/Kisa IL": "Ullensaker/Kisa", "Verdal IL": "Verdal", "Viking FK": "Viking", "Vålerenga Fotball": "Vålerenga",
    "Vålerenga IF Fotball": "Vålerenga", "Vålerengens IF": "Vålerenga", "Ålgård FK": "Ålgård", "Årstad IL": "Årstad",
    "Berger IL": "Berger", "FK Fremad Lillehammer": "Fremad Lillehammer", "Holmestrand IF": "Holmestrand",
    "IL Nordlandet": "Nordlandet", "Kapp IF": "Kapp", "Kapp IL": "Kapp", "Kragerø TF": "Kragerø", "Minde IL": "Minde",
    "Nordnes IL": "Nordnes", "Nydalen IL": "Nydalen", "SK Gjøa": "Gjøa", "SK Jarl": "Jarl", "SK Mesna": "Mesna",
    "SK Viggo": "Viggo", "Skreia IL": "Skreia", "Ulefoss SF": "Ulefoss", "Vardal IF": "Vardal", "Veblungsnes FK": "Veblungsnes",
}

OGOL = {
    "2032": "Aalesund", "bodo-glimt": "Bodø/Glimt", "2028": "Brann", "2033": "Bryne", "41644": "Eik Tønsberg",
    "68257": "Jerv", "10847": "Gjøvik-Lyn", "4304": "Fredrikstad", "12391": "Frigg", "10616": "Fyllingen", "41672": "Greåker",
    "4305": "HamKam", "8647": "Haugesund", "10599": "Hødd", "8644": "Hønefoss", "56803": "KFUM Oslo", "8646": "Kongsvinger",
    "29819": "Kristiansund BK", "41673": "Larvik Turn", "2029": "Lillestrøm", "41670": "Lisleby", "1088": "Lyn",
    "11545": "Mjølner", "10369": "Mjøndalen", "molde": "Molde", "8641": "Moss", "2026": "Odd", "27932": "Ørn Horten",
    "41646": "Os", "10600": "Pors", "32151": "Ranheim", "8645": "Raufoss", "155": "Rosenborg", "41643": "Djerv 1919",
    "41645": "Haugar", "7317": "Sandefjord", "11376": "Sandnes Ulf", "25919": "Sarpsborg 08", "12408": "Sarpsborg FK",
    "8649": "Skeid", "2030": "Sogndal", "2025": "Stabæk", "4014": "Start", "40491": "Steinkjer", "11748": "Strindheim",
    "10704": "Strømmen", "8365": "Strømsgodset", "2031": "Tromsø", "1110": "Vålerenga", "10613": "Vard Haugesund",
    "2027": "Viking",
}
# código do ogol que vale outro clube numa temporada (conferido com a tabela da Wikipédia)
OGOL_TEMPORADA: dict[tuple, str] = {}
OGOL_ATE: dict[str, tuple[str, str]] = {
    "7317": ("1998", "Sandefjord BK"),   # o ogol junta o Sandefjord BK (até os anos 1960) e o Sandefjord Fotball (1998)
}

# (expressão sobre o nome normalizado: minúsculas, sem acento) -> chave; a primeira que casa vale
PADROES: list[tuple[str, str]] = [
    (r"^aalesund|^alesund", "Aalesund"), (r"^bodo", "Bodø/Glimt"), (r"^brann", "Brann"), (r"^sk brann", "Brann"),
    (r"^bryne", "Bryne"), (r"^eik", "Eik Tønsberg"), (r"jerv", "Jerv"), (r"gjovik", "Gjøvik-Lyn"),
    (r"^fredrikstad", "Fredrikstad"), (r"^frigg", "Frigg"), (r"fyllingen", "Fyllingen"), (r"ham ?-?kam|hamarkam", "HamKam"),
    (r"haugesund", "Haugesund"), (r"hodd", "Hødd"), (r"honefoss", "Hønefoss"), (r"^kfum", "KFUM Oslo"),
    (r"kongsvinger", "Kongsvinger"), (r"^kristiansund", "Kristiansund BK"), (r"larvik turn", "Larvik Turn"),
    (r"lillestrom", "Lillestrøm"), (r"lisleby", "Lisleby"), (r"lyn", "Lyn"), (r"mjolner", "Mjølner"),
    (r"mjondalen", "Mjøndalen"), (r"^molde", "Molde"), (r"^moss", "Moss"), (r"^odd", "Odd"), (r"orn", "Ørn Horten"),
    (r"^pors", "Pors"), (r"ranheim", "Ranheim"), (r"raufoss", "Raufoss"), (r"rosenborg", "Rosenborg"),
    (r"sandefjord", "Sandefjord"), (r"sandnes", "Sandnes Ulf"), (r"sarpsborg 08|^sarpsborg$", "Sarpsborg 08"),
    (r"^skeid", "Skeid"), (r"^freidig", "Freidig"), (r"^fram", "Fram Larvik"), (r"valereng", "Vålerenga"), (r"sogndal", "Sogndal"), (r"stabaek", "Stabæk"), (r"start", "Start"), (r"steinkjer", "Steinkjer"),
    (r"strindheim", "Strindheim"), (r"strommen", "Strømmen"), (r"stromsgodset", "Strømsgodset"), (r"tromso", "Tromsø"),
    (r"valerenga", "Vålerenga"), (r"viking", "Viking"), (r"ull.*kisa", "Ullensaker/Kisa"),
]


def _normal(s: str) -> str:
    s = s.replace("ø", "o").replace("Ø", "O").replace("æ", "ae").replace("Æ", "Ae").replace("å", "a").replace("Å", "A")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9/]", " ", s)).strip()


_INDICE = {_normal(k): k for k in CLUBES}
_PADROES = [(re.compile(p), c) for p, c in PADROES]


def link(alvo: str | None) -> str | None:
    return LINKS.get((alvo or "").strip())


_SIGLAS = {"fk", "if", "il", "sk", "bk", "ff", "tif", "sfk", "ik", "fotball", "toppfotball", "fc"}


def esd(nome: str) -> str | None:
    """Pelo nome exato do cadastro, depois sem as siglas ("FK Skeid", "Freidig FK"), depois pelos padrões."""
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
    if (codigo, temporada) in OGOL_TEMPORADA:
        return OGOL_TEMPORADA[(codigo, temporada)]
    ate = OGOL_ATE.get(codigo)
    if ate and temporada and temporada[:4] < ate[0]:
        return ate[1]
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
