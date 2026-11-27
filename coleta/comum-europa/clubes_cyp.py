"""Cadastro dos clubes cipriotas (cyp-1).

Chave: o nome de exibição no painel, o nome usado no Brasil ("APOEL", "Omonia", "Anorthosis", "AEL Limassol"). Nomes únicos
no mundo, conferidos no banco e nos outros pacotes.

Identidade (27/11/2026): pelo alvo do link da Wikipédia em cada temporada (LINKS), seguindo os redirecionamentos. O AEK
Larnaca (1994) fica separado do EPA e do Pezoporikos, que se fundiram nele (artigos próprios); o AEP Paphos (2000) fica
separado do Evagoras e do APOP Paphos; o Lefkoşa Türk é o Çetinkaya (redirecionamento); o "Trast" de 1934/35 é o Enosis
Neon Trust; o Omonia 29M fica separado do Omonia.

Nas fontes sem link: OGOL (código do ogol -> chave, com OGOL_ATE quando o código cobre dois clubes) e PADROES (nome
normalizado -> chave), para a RSSSF.
"""
from __future__ import annotations

import re
import unicodedata

NIC, LIM, LAR, FAM, PAF = "Nicósia", "Limassol", "Larnaca", "Famagusta", "Pafos"
CLUBES = {
    "APOEL": (NIC, "CYP"), "Omonia": (NIC, "CYP"), "Olympiakos Nicosia": (NIC, "CYP"), "Çetinkaya": (NIC, "CYP"),
    "Enosis Neon Trust": (NIC, "CYP"), "AYMA Nicosia": (NIC, "CYP"), "Orfeas Nicosia": (NIC, "CYP"),
    "Keravnos Strovolou": ("Strovolos", "CYP"), "ENTHOI Lakatamia": ("Lakatamia", "CYP"), "PAEEK": ("Lakatamia", "CYP"),
    "Omonia 29M": (NIC, "CYP"), "Digenis Morphou": ("Morphou", "CYP"), "ASIL Lysi": ("Lysi", "CYP"),
    "Chalkanoras Idaliou": ("Dali", "CYP"), "Othellos Athienou": ("Athienou", "CYP"),
    "AEL Limassol": (LIM, "CYP"), "Apollon Limassol": (LIM, "CYP"), "Aris Limassol": (LIM, "CYP"),
    "APEP": ("Pitsilia", "CYP"), "AEZ Zakakiou": (LIM, "CYP"), "Karmiotissa": ("Polemidia", "CYP"),
    "Krasava ENY Ypsonas": ("Ypsonas", "CYP"), "AEK Larnaca": (LAR, "CYP"), "EPA Larnaca": (LAR, "CYP"),
    "Pezoporikos Larnaca": (LAR, "CYP"), "Alki Larnaca": (LAR, "CYP"), "Alki Oroklini": ("Oroklini", "CYP"),
    "Ermis Aradippou": ("Aradippou", "CYP"), "Omonia Aradippou": ("Aradippou", "CYP"), "Doxa Katokopias": ("Katokopia", "CYP"),
    "Anorthosis": (FAM, "CYP"), "Nea Salamina": (FAM, "CYP"), "Enosis Paralimni": ("Paralimni", "CYP"),
    "Ethnikos Achna": ("Achna", "CYP"), "Anagennisi Deryneia": ("Deryneia", "CYP"), "Ayia Napa": ("Ayia Napa", "CYP"),
    "Onisilos Sotira": ("Sotira", "CYP"), "Ethnikos Assia": ("Assia", "CYP"), "Pafos FC": (PAF, "CYP"),
    "AEP Paphos": (PAF, "CYP"), "Evagoras Paphos": (PAF, "CYP"), "APOP Paphos": (PAF, "CYP"), "APOP Kinyras": ("Peyia", "CYP"),
    "AEK Kouklia": ("Kouklia", "CYP"), "Akritas Chlorakas": ("Chloraka", "CYP"), "Atromitos Yeroskipou": ("Yeroskipou", "CYP"),
}

LINKS = {
    "AC Omonia": "Omonia", "AEK Kouklia": "AEK Kouklia", "AEK Kouklia F.C.": "AEK Kouklia", "AEK Larnaca FC": "AEK Larnaca",
    "AEK Larnaca": "AEK Larnaca", "AEK Larnaca F.C.": "AEK Larnaca", "AEL Limassol": "AEL Limassol",
    "AEL Limassol FC": "AEL Limassol", "AEP Paphos FC": "AEP Paphos", "AEP Paphos F.C.": "AEP Paphos",
    "AEZ Zakakiou": "AEZ Zakakiou", "APEP FC": "APEP", "APEP F.C.": "APEP", "APEP Limassol": "APEP", "APOEL FC": "APOEL",
    "APOEL F.C.": "APOEL", "APOP Kinyras FC": "APOP Kinyras", "APOP Kinyras Peyias FC": "APOP Kinyras",
    "APOP Paphos FC": "APOP Paphos", "APOP Paphos": "APOP Paphos", "ASIL Lysi": "ASIL Lysi",
    "Akritas Chlorakas": "Akritas Chlorakas", "Alki Larnaca FC": "Alki Larnaca", "Alki Larnaca F.C.": "Alki Larnaca",
    "Alki Oroklini": "Alki Oroklini", "Anagennisi Deryneia FC": "Anagennisi Deryneia",
    "Anagennisi Deryneia": "Anagennisi Deryneia", "Anagennisi Dherynia": "Anagennisi Deryneia",
    "Anorthosis Famagusta FC": "Anorthosis", "Anorthosis Famagusta": "Anorthosis", "Anorthosis Famagusta F.C.": "Anorthosis",
    "Apollon Limassol FC": "Apollon Limassol", "Apollon Limassol": "Apollon Limassol", "Aris Limassol FC": "Aris Limassol",
    "Aris Limassol F.C.": "Aris Limassol", "Armenian Young Men's Association": "AYMA Nicosia", "AYMA, Nicosia": "AYMA Nicosia",
    "Atromitos Yeroskipou": "Atromitos Yeroskipou", "Ayia Napa FC": "Ayia Napa", "Ayia Napa F.C.": "Ayia Napa",
    "Chalkanoras Idaliou": "Chalkanoras Idaliou", "Digenis Akritas Morphou FC": "Digenis Morphou",
    "Digenis Akritas Morphou": "Digenis Morphou", "Doxa Katokopias FC": "Doxa Katokopias",
    "Doxa Katokopias F.C.": "Doxa Katokopias", "EPA Larnaca FC": "EPA Larnaca", "EPA Larnaca": "EPA Larnaca",
    "Enosis Neon Paralimni FC": "Enosis Paralimni", "Enosis Neon THOI Lakatamia": "ENTHOI Lakatamia",
    "ENTHOI Lakatamia FC": "ENTHOI Lakatamia", "Enosis Neon Trust": "Enosis Neon Trust",
    "Ermis Aradippou FC": "Ermis Aradippou", "Ermis Aradippou": "Ermis Aradippou", "Ethnikos Achna FC": "Ethnikos Achna",
    "Ethnikos Assia FC": "Ethnikos Assia", "Ethnikos Assia F.C.": "Ethnikos Assia", "Evagoras Paphos": "Evagoras Paphos",
    "Karmiotissa FC": "Karmiotissa", "Karmiotissa Polemidion FC": "Karmiotissa", "Keravnos Strovolou FC": "Keravnos Strovolou",
    "Krasava ENY Ypsonas FC": "Krasava ENY Ypsonas", "Nea Salamis Famagusta FC": "Nea Salamina",
    "Nea Salamis FC": "Nea Salamina", "Olympiakos Nicosia": "Olympiakos Nicosia", "Omonia Aradippou": "Omonia Aradippou",
    "Onisilos Sotira": "Onisilos Sotira", "Orfeas Nicosia": "Orfeas Nicosia", "Othellos Athienou FC": "Othellos Athienou",
    "PAC Omonia 29M": "Omonia 29M", "PAEEK Kyrenia": "PAEEK", "PAEEK": "PAEEK", "Pafos FC": "Pafos FC",
    "Pezoporikos Larnaca FC": "Pezoporikos Larnaca", "Pezoporikos Larnaca": "Pezoporikos Larnaca",
    "Çetinkaya Türk S.K.": "Çetinkaya", "Lefkoşa Türk Spor Kulübü": "Çetinkaya",
}

OGOL = {
    "17558": "AEK Kouklia", "aek-larnaca": "AEK Larnaca", "1843": "AEL Limassol", "1848": "AEP Paphos",
    "64093": "AEZ Zakakiou", "5893": "APEP", "1044": "APOEL", "5892": "APOP Kinyras", "44613": "Akritas Chlorakas",
    "5813": "Alki Larnaca", "105708": "Alki Oroklini", "1850": "Anagennisi Deryneia", "anorthosis": "Anorthosis",
    "1842": "Apollon Limassol", "4268": "Aris Limassol", "11617": "Atromitos Yeroskipou", "7889": "Ayia Napa",
    "1852": "Doxa Katokopias", "1847": "Digenis Morphou", "5894": "ENTHOI Lakatamia", "1846": "Enosis Paralimni",
    "13720": "Ermis Aradippou", "1844": "Ethnikos Achna", "51643": "Ethnikos Assia", "56869": "Evagoras Paphos",
    "64106": "Karmiotissa", "4269": "Nea Salamina", "1845": "Olympiakos Nicosia", "omonia": "Omonia",
    "256452": "Omonia 29M", "11616": "Omonia Aradippou", "1851": "Onisilos Sotira", "32407": "Othellos Athienou",
    "26426": "PAEEK", "95985": "Pafos FC", "105705": "Krasava ENY Ypsonas",
}
# código do ogol que cobre dois clubes: código -> (temporada em que passa a valer o da tabela OGOL, clube antes)
OGOL_ATE = {"5892": ("2001/02", "APOP Paphos")}   # o APOP Paphos (até 2000) e o APOP Kinyras (desde 2003)

PADROES: list[tuple[str, str]] = [
    (r"apoel", "APOEL"), (r"omonia aradippou", "Omonia Aradippou"), (r"omonia 29|29is", "Omonia 29M"), (r"omonia", "Omonia"),
    (r"anorthosis", "Anorthosis"), (r"^ael|ael limassol", "AEL Limassol"), (r"apollon", "Apollon Limassol"),
    (r"^aris", "Aris Limassol"), (r"aek larnaca", "AEK Larnaca"), (r"^epa", "EPA Larnaca"), (r"pezoporikos", "Pezoporikos Larnaca"),
    (r"olympiakos", "Olympiakos Nicosia"), (r"nea salami", "Nea Salamina"), (r"paralimni|^enp$", "Enosis Paralimni"),
    (r"achna", "Ethnikos Achna"), (r"alki oroklini", "Alki Oroklini"), (r"alki", "Alki Larnaca"), (r"doxa", "Doxa Katokopias"),
    (r"ermis", "Ermis Aradippou"), (r"pafos fc|paphos fc", "Pafos FC"), (r"^aep", "AEP Paphos"),
    (r"evagoras", "Evagoras Paphos"), (r"kinyras|kinyras", "APOP Kinyras"), (r"apop", "APOP Paphos"), (r"apep", "APEP"),
    (r"cetin|lefkosa turk", "Çetinkaya"), (r"trast|trust", "Enosis Neon Trust"), (r"karmiotissa", "Karmiotissa"),
    (r"deryneia|dherynia", "Anagennisi Deryneia"), (r"digenis", "Digenis Morphou"), (r"ayia napa", "Ayia Napa"),
    (r"keravnos", "Keravnos Strovolou"), (r"paeek", "PAEEK"), (r"othellos", "Othellos Athienou"), (r"zakakiou", "AEZ Zakakiou"),
]


def _normal(s: str) -> str:
    s = s.replace("ı", "i").replace("ş", "s").replace("Ş", "S").replace("ç", "c").replace("Ç", "C")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]", " ", s)).strip()


_INDICE = {_normal(k): k for k in CLUBES}
_PADROES = [(re.compile(p), c) for p, c in PADROES]


def link(alvo: str | None) -> str | None:
    return LINKS.get((alvo or "").strip())


def esd(nome: str) -> str | None:
    n = _normal(nome)
    if n in _INDICE:
        return _INDICE[n]
    for p, c in _PADROES:
        if p.search(n):
            return c
    return None


def ogol(codigo: str, temporada: str | None = None) -> str | None:
    ate = OGOL_ATE.get(codigo)
    if ate and temporada and temporada < ate[0]:
        return ate[1]
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
