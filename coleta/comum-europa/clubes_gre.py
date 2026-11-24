"""Cadastro dos clubes gregos (e dos cipriotas que jogaram a liga grega), comum a todas as divisões da Grécia.

Chave: o nome de exibição no painel (como o clube é conhecido no Brasil), com cidade e país. Nomes únicos no mundo,
conferidos no banco e nos outros pacotes ("AEK Atenas", "Aris Salônica" e "Omonia Nicosia", porque há AEK Larnaca, Aris
Limassol e outros Omonia).

Identidade (pela linhagem do clube, como na Wikipédia: o alvo do link na tabela de cada temporada):
- o mesmo clube com nomes de época vira uma chave só: Apollon Athens e Apollon Smyrnis; Apollon Salonika, Apollon
  Thessaloniki, Apollon Kalamarias e Apollon Pontou; Xanthi e Skoda Xanthi; AEL e Larissa; Pankorinthiakos, APS e AE
  Korinthos; Olympiakos Chalkida e AO Chalkida; Megas Alexandros Katerini e Pierikos; Athens Kallithea e Kallithea;
  Iraklis e Iraklis 1908;
- 2004/05: o clube da liga era o Chalkidona (Wikipédia, engsoccerdata); ele se fundiu com o Atromitos em 2005, e o ogol
  põe a temporada no código do Atromitos;
- clubes diferentes com nome parecido ficam separados: Atromitos Piraeus (1960) e Atromitos (Peristeri); Rodos FC
  (1978-1979) e AE Rodos (1981-1982); AO Kerkyra (2004-2012) e PAE Kerkyra (2014-2017); Olympiacos, Olympiacos Volos e
  Olympiakos Nicosia; Niki Volos e Volos NFC; Ethnikos Piraeus e Ethnikos Asteras.
- os campeões do Chipre jogaram a liga grega de 1967/68 a 1973/74 (Olympiakos Nicosia, AEL Limassol, EPA Larnaca,
  Omonia Nicosia e APOEL): país CYP.

Os nomes das fontes variam muito (a RSSSF abrevia: "Apollon Salo.", "Pangorinthiak.", "P.A.O.K Salo."); em vez de uma lista
de grafias, PADROES reconhece o clube por expressões, em ordem (as mais específicas antes: "Larisa" e "Kalamarias"
contêm "aris"). ALIASES: grafias que os padrões não pegam. POR_ANO: nomes que dependem da época. OGOL: código do ogol ->
chave.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    # grandes e clubes de hoje
    "Olympiacos": ("Pireu", "GRE"), "Panathinaikos": ("Atenas", "GRE"), "AEK Atenas": ("Atenas", "GRE"),
    "PAOK": ("Salônica", "GRE"), "Aris Salônica": ("Salônica", "GRE"), "OFI Creta": ("Heraclião", "GRE"),
    "Larissa": ("Larissa", "GRE"), "Atromitos": ("Peristeri", "GRE"), "Asteras Tripolis": ("Trípoli", "GRE"),
    "Panetolikos": ("Agrinio", "GRE"), "Levadiakos": ("Livadeia", "GRE"), "Volos NFC": ("Volos", "GRE"),
    "Kifisia": ("Kifisia", "GRE"), "Panserraikos": ("Serres", "GRE"), "Kalamata": ("Kalamata", "GRE"),
    "Lamia": ("Lamia", "GRE"), "PAS Giannina": ("Ioannina", "GRE"), "Iraklis": ("Salônica", "GRE"),
    "Panionios": ("Nea Smyrni", "GRE"), "Xanthi": ("Xanthi", "GRE"), "Apollon Smyrnis": ("Atenas", "GRE"),
    "Kallithea": ("Kallithea", "GRE"), "Ionikos": ("Nikaia", "GRE"),
    # outros clubes da liga nacional (1959/60 em diante)
    "Ethnikos Piraeus": ("Pireu", "GRE"), "Apollon Kalamarias": ("Kalamaria", "GRE"), "Doxa Drama": ("Drama", "GRE"),
    "Proodeftiki": ("Nikaia", "GRE"), "Panegialios": ("Aigio", "GRE"), "Korinthos": ("Corinto", "GRE"),
    "Pierikos": ("Katerini", "GRE"), "AE Nikaia": ("Nikaia", "GRE"), "Fostiras": ("Tavros", "GRE"),
    "Thermaikos": ("Salônica", "GRE"), "Atromitos Piraeus": ("Pireu", "GRE"), "Niki Volos": ("Volos", "GRE"),
    "Egaleo": ("Egaleo", "GRE"), "Panelefsiniakos": ("Elefsina", "GRE"), "Chalkida": ("Cálcis", "GRE"),
    "Trikala": ("Trikala", "GRE"), "Vyzas Megara": ("Megara", "GRE"), "Veria": ("Veria", "GRE"),
    "Olympiacos Volos": ("Volos", "GRE"), "Kavala": ("Kavala", "GRE"), "Panachaiki": ("Patras", "GRE"),
    "Kastoria": ("Kastoria", "GRE"), "Rodos": ("Rodes", "GRE"), "AE Rodos": ("Rodes", "GRE"),
    "Makedonikos": ("Salônica", "GRE"), "Diagoras": ("Rodes", "GRE"), "Athinaikos": ("Vyronas", "GRE"),
    "Edessaikos": ("Edessa", "GRE"), "Naoussa": ("Naoussa", "GRE"), "Paniliakos": ("Pyrgos", "GRE"),
    "Ethnikos Asteras": ("Kaisariani", "GRE"), "Akratitos": ("Ano Liosia", "GRE"), "Chalkidona": ("Chalkidona", "GRE"),
    "Ergotelis": ("Heraclião", "GRE"), "AO Kerkyra": ("Corfu", "GRE"), "PAE Kerkyra": ("Corfu", "GRE"),
    "Panthrakikos": ("Komotini", "GRE"), "Thrasyvoulos": ("Fyli", "GRE"), "Platanias": ("Platanias", "GRE"),
    "AEL Kalloni": ("Kalloni", "GRE"),
    # só na era antiga (fase nacional até 1958/59)
    "Panargiakos": ("Argos", "GRE"),
    # cipriotas (campeões do Chipre na liga grega, 1967/68-1973/74)
    "Olympiakos Nicosia": ("Nicósia", "CYP"), "AEL Limassol": ("Limassol", "CYP"), "EPA Larnaca": ("Larnaca", "CYP"),
    "Omonia Nicosia": ("Nicósia", "CYP"), "APOEL": ("Nicósia", "CYP"),
}

# (expressão sobre o nome normalizado: minúsculas, sem acento, pontuação virando espaço) -> chave; a primeira que casa vale
PADROES: list[tuple[str, str]] = [
    (r"olymp\w* (?:l\b|lefkos|nicosia)", "Olympiakos Nicosia"),
    (r"olymp\w* (?:v\b|vol)", "Olympiacos Volos"),
    (r"olymp\w* chalk", "Chalkida"),
    (r"olymp|olympaikos", "Olympiacos"),
    (r"panathinaikos", "Panathinaikos"),
    (r"\bael kallon|\bkallon", "AEL Kalloni"),
    (r"\bael limassol|lemess", "AEL Limassol"),
    (r"larnak|larnaca", "EPA Larnaca"),
    (r"omono|omonia", "Omonia Nicosia"),
    (r"\ba ?p ?o ?e ?l\b", "APOEL"),
    (r"\ba ?e ?k\b|konstantinoupol", "AEK Atenas"),
    (r"\bp ?a ?o ?k\b", "PAOK"),
    (r"laris|^ael$|^a e l$", "Larissa"),
    (r"apollon\w*(?: \w+)? (?:kalamar|sal|thess|pontou)|kalamaria", "Apollon Kalamarias"),
    (r"apollon", "Apollon Smyrnis"),
    (r"\baris\b", "Aris Salônica"),
    (r"iraklis|heracles", "Iraklis"),
    (r"\bo ?f ?i\b", "OFI Creta"),
    (r"panionios", "Panionios"),
    (r"\beth(?:nikos)? asteras", "Ethnikos Asteras"),
    (r"ethn?ikos", "Ethnikos Piraeus"),
    (r"atromitos p(?:ir\w*)?\b", "Atromitos Piraeus"),
    (r"atromitos", "Atromitos"),
    (r"pierikos|megas alexand", "Pierikos"),
    (r"korinth|gorinth", "Korinthos"),
    (r"kastori", "Kastoria"),
    (r"diagoras", "Diagoras"),
    (r"makedonikos", "Makedonikos"),
    (r"thermaikos", "Thermaikos"),
    (r"ionikos", "Ionikos"),
    (r"\bae nik|\ba e nik", "AE Nikaia"),
    (r"pro+de[fy]t", "Proodeftiki"),
    (r"pan[ae]gialios", "Panegialios"),
    (r"panelefsin|eleysina", "Panelefsiniakos"),
    (r"fostiras", "Fostiras"),
    (r"niki vol", "Niki Volos"),
    (r"egaleo|aigaleo", "Egaleo"),
    (r"trikala", "Trikala"),
    (r"panser+aikos", "Panserraikos"),
    (r"vizas|vyzas", "Vyzas Megara"),
    (r"veroia|veria", "Veria"),
    (r"kavala", "Kavala"),
    (r"pana[cx]?h?aiki|panahaiki", "Panachaiki"),
    (r"kalamata", "Kalamata"),
    (r"pan[ae]i?tolik", "Panetolikos"),
    (r"[jy]?i?oan+ina|giannina|jiannina|yiannina", "PAS Giannina"),
    (r"doxa", "Doxa Drama"),
    (r"levad", "Levadiakos"),
    (r"xanthi", "Xanthi"),
    (r"athinaikos", "Athinaikos"),
    (r"edessaikos", "Edessaikos"),
    (r"naou?ss?a|nausa", "Naoussa"),
    (r"paniliakos", "Paniliakos"),
    (r"akratitos", "Akratitos"),
    (r"kall?ithea", "Kallithea"),
    (r"[ck]?halkidona", "Chalkidona"),
    (r"chalkid", "Chalkida"),
    (r"ergotelis", "Ergotelis"),
    (r"asteras tripolis", "Asteras Tripolis"),
    (r"panthrakikos", "Panthrakikos"),
    (r"thrasyvoulos", "Thrasyvoulos"),
    (r"platanias", "Platanias"),
    (r"lamia", "Lamia"),
    (r"volos nfc|^volos$|^volos f c$", "Volos NFC"),
    (r"kifisi", "Kifisia"),
    (r"panargiakos", "Panargiakos"),
]

ALIASES: dict[str, str] = {}

# nomes que dependem da época: expressão sobre o nome normalizado -> [(ano inicial, ano final, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "rodos": [(1978, 1979, "Rodos"), (1981, 1982, "AE Rodos")],
    "kerk[iy]ra": [(2004, 2012, "AO Kerkyra"), (2014, 2017, "PAE Kerkyra")],
}

OGOL: dict[str, str] = {
    "olympiacos": "Olympiacos", "panathinaikos": "Panathinaikos", "aek": "AEK Atenas", "paok": "PAOK", "aris": "Aris Salônica",
    "1920": "OFI Creta", "6169": "Larissa", "8611": "Asteras Tripolis", "26397": "Panetolikos",
    "6235": "Levadiakos", "231916": "Volos NFC", "231157": "Kifisia", "12120": "Panserraikos", "9035": "Kalamata",
    "26797": "Lamia", "4173": "PAS Giannina", "279863": "Iraklis", "1105": "Panionios", "1922": "Xanthi",
    "10823": "Apollon Smyrnis", "1924": "Kallithea", "1921": "Ionikos", "9641": "Panachaiki", "43607": "Naoussa",
    "10839": "Athinaikos", "4442": "Doxa Drama", "231938": "Apollon Kalamarias", "4187": "Apollon Kalamarias",
    "28486": "Edessaikos", "7786": "Ethnikos Piraeus", "12430": "Kavala", "1923": "Paniliakos", "5713": "Kastoria",
    "9589": "Veria", "1925": "Proodeftiki", "8612": "Ethnikos Asteras", "22925": "Panelefsiniakos", "19340": "Trikala",
    "1926": "Akratitos", "1917": "Egaleo", "13772": "Chalkidona", "4188": "Ergotelis", "14308": "Panthrakikos",
    "14310": "Thrasyvoulos", "16350": "Olympiacos Volos", "49922": "Platanias", "63008": "AEL Kalloni", "8871": "Niki Volos",
}
# o mesmo código do ogol para dois clubes: código -> [(ano inicial, ano final, chave)]
OGOL_POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "4189": [(2004, 2012, "AO Kerkyra"), (2014, 2017, "PAE Kerkyra")],
    # 2004/05: o clube da liga era o Chalkidona (Wikipédia e engsoccerdata); fundiu-se com o Atromitos em 2005 e o ogol
    # põe a temporada no Atromitos
    "1918": [(2004, 2004, "Chalkidona"), (2005, 9999, "Atromitos")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


def _normal(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)|\*+", " ", s)          # "(-6)", "(1)", "**"
    s = re.sub(r"\b(f\.?c|fc|f c)\b\.?", " ", s) if "volos" not in s else s
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]", " ", s)).strip()


_INDICE: dict[str, str] = {chave(k): k for k in CLUBES}
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_PADROES = [(re.compile(p), c) for p, c in PADROES]


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que dependem
    da época."""
    nome = re.sub(r"\s+", " ", nome.replace("&nbsp;", " ").replace("\xa0", " ").strip())
    n = _normal(nome)
    for k, faixas in POR_ANO.items():
        if re.search(rf"\b{k}\b", n) and not re.search(r"diagoras", n):
            return next((c for ini, fim, c in faixas if ano is not None and ini <= ano <= fim), None)
    if chave(nome) in _INDICE:
        return _INDICE[chave(nome)]
    for p, c in _PADROES:
        if p.search(n):
            return c
    return None


def ogol(codigo: str, ano: int | None = None) -> str | None:
    if codigo in OGOL_POR_ANO:
        return next((c for ini, fim, c in OGOL_POR_ANO[codigo] if ano is not None and ini <= ano <= fim), None)
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
