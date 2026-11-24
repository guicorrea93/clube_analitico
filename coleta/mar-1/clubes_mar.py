"""Identidade dos clubes marroquinos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Wydad Casablanca", "Raja Casablanca", "FAR Rabat", "RS Berkane");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Racing Casablanca (era colonial), Racing Athletic Club (RAC) e ADM Casablanca (Association des Douanes Marocaines,
    1968-1972) são um clube só, como a RSSSF conta os títulos ("3 Racing (ADM) Casablanca");
  - US Safi (colonial) = Union Sportive de Safi (1957/58); AS Tanger-Fès (colonial) = Association Sportive de Tanger-Fès
    (1957/58); Stade Marocain (Rabat) é o mesmo antes e depois de 1956;
  - AS Salé = SA Salé = Sporting Salé (as três grafias nunca aparecem juntas);
  - Tihad Athletic Sport = TAS Casablanca = Tihad Sportif;
- clubes diferentes com nome parecido ficam separados: o Olympique Casablanca da era colonial (ligas de 1939 a 1945) e o
  Olympique de Casablanca (OC, campeão de 1993/94, fundido ao Raja em 1995); o Racing Club Marocain (1915-1922) e o Racing
  Casablanca; a Union Athlétique de Kénitra (1915-1931) e o KAC Kénitra; o US Safi e o Olympic Safi.
- siglas e nomes curtos dos anos 1990 ("Fes", "Raja", "KAC", "Marrakesh") resolvem pelo clube da 1ª divisão do ano: "KAC"
  sozinho é o Kénitra e "KACM" o Kawkab de Marrakech.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

CAS = ("Casablanca", "Casablanca-Settat")
RAB = ("Rabat", "Rabat-Salé-Kénitra")
FES = ("Fès", "Fès-Meknès")
MEK = ("Meknès", "Fès-Meknès")
MAR = ("Marrakech", "Marrakech-Safi")
TAN = ("Tânger", "Tanger-Tétouan-Al Hoceïma")
KEN = ("Kénitra", "Rabat-Salé-Kénitra")

# nome de exibição -> (cidade, região)
CLUBES: dict[str, tuple[str, str]] = {
    # Casablanca
    "Wydad Casablanca": CAS, "Raja Casablanca": CAS, "Racing Casablanca": CAS, "US Marocaine": CAS, "USA Casablanca": CAS,
    "CA Marocain": CAS, "Racing Club Marocain": CAS, "Club Sportif Colonial": CAS, "ASPTT Casablanca": CAS, "Roches Noires": CAS,
    "Ideal Casablanca": CAS, "AS Casablanca": CAS, "Olympique Casablanca": CAS, "Racing Universitaire": CAS,
    "Moghreb Casablanca": CAS, "Cheminots Casablanca": CAS, "TAS Casablanca": CAS, "EJS Casablanca": CAS, "Quartier Industriel": CAS,
    "ASCOM": CAS, "ASM": ("", ""), "Olympique de Casablanca": CAS, "CLAS Casablanca": CAS, "Rachad Bernoussi": CAS, "IS Casablanca": CAS,
    "Crédit Agricole Rabat": RAB,
    "Chabab Mohammédia": ("Mohammédia", "Casablanca-Settat"), "US Mohammédia": ("Mohammédia", "Casablanca-Settat"),
    "Fedala Sport": ("Mohammédia", "Casablanca-Settat"),
    "RS Settat": ("Settat", "Casablanca-Settat"), "SA Settat": ("Settat", "Casablanca-Settat"),
    "DH El Jadida": ("El Jadida", "Casablanca-Settat"), "Sporting Mazagan": ("El Jadida", "Casablanca-Settat"),
    "CAY Berrechid": ("Berrechid", "Casablanca-Settat"), "JS Soualem": ("Soualem", "Casablanca-Settat"),
    "RCA Zemamra": ("Zemamra", "Casablanca-Settat"),
    # Rabat, Salé, Kénitra
    "FAR Rabat": RAB, "FUS Rabat": RAB, "Stade Marocain": RAB, "Olympique Marocain": RAB, "ASPTT Rabat": RAB,
    "Rabat FC": RAB, "Sporting Club de Rabat": RAB, "Cheminots Rabat": RAB, "AS Rabat": RAB, "Stade Rabat": RAB,
    "Moghreb Sportif de Rabat": RAB, "Barid Mohammedi": RAB, "Youssoufia Rabat": RAB, "Union Touarga": RAB,
    "US Rabat Salé": RAB, "AS Salé": ("Salé", "Rabat-Salé-Kénitra"),
    "KAC Kénitra": KEN, "Union Athlétique de Kénitra": KEN, "CA Port Lyautey": KEN, "RS Kénitra": KEN,
    "US Sidi Kacem": ("Sidi Kacem", "Rabat-Salé-Kénitra"), "IZ Khémisset": ("Khémisset", "Rabat-Salé-Kénitra"),
    "Amal Belksiri": ("Belksiri", "Rabat-Salé-Kénitra"),
    # Fès, Meknès
    "MAS Fès": FES, "Wydad Fès": FES, "US Fès": FES, "ASPTT Fès": FES, "AS Tanger-Fès": FES,
    "CODM Meknès": MEK, "USD Meknès": MEK, "Meknès Sports": MEK, "Rachad de Meknès": MEK, "Olympique Meknès": MEK,
    "Stade Meknès": MEK, "US Petitjean": ("Sidi Kacem", "Rabat-Salé-Kénitra"), "SC Taza": ("Taza", "Fès-Meknès"),
    # Marrakech, Safi
    "Kawkab Marrakech": MAR, "SA Marrakech": MAR, "AS Marrakech": MAR, "MC Marrakech": MAR,
    "US Safi": ("Safi", "Marrakech-Safi"), "SC Safi": ("Safi", "Marrakech-Safi"), "Olympic Safi": ("Safi", "Marrakech-Safi"),
    "AS Mogador": ("Essaouira", "Marrakech-Safi"),
    # Norte
    "IR Tanger": TAN, "Moghreb Tanger": TAN, "Hilal Tanger": TAN, "ASF Tanger": TAN, "Moghreb Tétouan": ("Tétouan", TAN[1]),
    "Chabab Larache": ("Larache", TAN[1]), "Chabab Rif Hoceima": ("Al Hoceïma", TAN[1]),
    # Oriental
    "MC Oujda": ("Oujda", "Oriental"), "US Oujda": ("Oujda", "Oriental"), "USM Oujda": ("Oujda", "Oriental"),
    "RS Berkane": ("Berkane", "Oriental"), "Hilal Nador": ("Nador", "Oriental"),
    # Centro e Sul
    "OC Khouribga": ("Khouribga", "Béni Mellal-Khénifra"), "Raja Béni Mellal": ("Béni Mellal", "Béni Mellal-Khénifra"),
    "IR Fkih Ben Salah": ("Fkih Ben Salah", "Béni Mellal-Khénifra"), "Chabab Kasba Tadla": ("Kasba Tadla", "Béni Mellal-Khénifra"),
    "CA Khénifra": ("Khénifra", "Béni Mellal-Khénifra"), "Rapide Oued Zem": ("Oued Zem", "Béni Mellal-Khénifra"),
    "Hassania Agadir": ("Agadir", "Souss-Massa"), "Raja Agadir": ("Agadir", "Souss-Massa"), "SO Agadir": ("Agadir", "Souss-Massa"),
    "Olympique Dcheira": ("Dcheira El Jihadia", "Souss-Massa"), "JS Massira": ("Laâyoune", "Laâyoune-Sakia El Hamra"),
    "Chabab Sakia El Hamra": ("Laâyoune", "Laâyoune-Sakia El Hamra"), "US Yacoub El Mansour": RAB,
}

REGRAS: list[tuple[str, str, int, int]] = [
    # siglas e nomes curtos (anos 1990 e tabelas de confrontos)
    (r"(wac|wa|widad|wydad)( ac| a c| athletic club)?( de)?( casablanca| casblanca)?$|wydad athletic club casablanca|wydad casablanca",
     "Wydad Casablanca", 1937, 2100),
    (r"(waf( fes)?|wa fes|wydad (a |athletic )?(de )?fes)", "Wydad Fès", 1980, 2100),
    (r"(raja|rca)( c| ca| club athl\w* casablanca| casablanca| de casablanca| casablanca rca| club athletic)?$|raja casablanca|raja club athl",
     "Raja Casablanca", 1949, 2100),
    (r"raja (de )?b(eni|m)|raja bm|r beni|raja beni|beni mellal", "Raja Béni Mellal", 1956, 2100),
    (r"raja (agadir|cercle)", "Raja Agadir", 1956, 2100),
    (r"(as )?(far|forces armees royales)( de)?( rabat| ranat)?$|jaish malaki|as forces armees", "FAR Rabat", 1958, 2100),
    (r"(fus|fath)( de)?( rabat| ribatti| union sport)?( rabat)?$|fath us|fath union", "FUS Rabat", 1946, 2100),
    (r"(mas|maghreb fassi|maghrib as|maghreb association sportive|moghreb (de )?fes|maghreb fes|maghreb fez|fes$)( fes)?", "MAS Fès", 1946, 2100),
    (r"(kacm|kawkab|kac (de )?marrak\w*|marrakesh$|marrakech$)", "Kawkab Marrakech", 1947, 2100),
    (r"(kac|nadi kenitra|kenitra ac|kenitra athletic( club)?|kac kenitra|kac de kenitra)", "KAC Kénitra", 1938, 2100),
    (r"(mco|mouloudia (club )?oujda|mc oujda|oujda$|0ujda)", "MC Oujda", 1946, 2100),
    (r"(hus|husa|hassania|h agadir|agadir$)", "Hassania Agadir", 1946, 2100),
    (r"(dhj|difa+ ?h(assani)?( el)?( j?dj?idi| jadida| jdidi)?|difah hassani jadidi|dh (el )?jadid[ia]|dh el jadida|el jadida$)",
     "DH El Jadida", 1956, 2100),
    (r"(mat|maghreb athletic tetouan|moghreb (athletic )?(de )?tetouan|mohgreb|maghrib association tetouan|ma tetouan|tetouan$|maghreb tetouan|athletic tetouan)",
     "Moghreb Tétouan", 1922, 2100),
    (r"(irt|ittihad (riadh?i|ryadi|riyadi) (de )?tanger|ittihad tan(ger|gier|ja)|ir tanger|i tanger|tanger$|tangier$|ittihad de tanger|ir tangier|tihad tangiers?)",
     "IR Tanger", 1956, 2100),
    (r"(rss|renaissance (sportive )?(de )?settat|nehdat settat|rs settat|settat$|rss settat)", "RS Settat", 1946, 2100),
    (r"(rsb|renaissance (sportive )?(de )?berkane|nehdat berkane|rs berkane|rsb berkane)", "RS Berkane", 1938, 2100),
    (r"(cod|codm|club omnisports? de meknes|nadi meknassi|meknes$|cod meknes|codm (de )?meknes)", "CODM Meknès", 1962, 2100),
    (r"(scc|sccm|sporting club chabab|sc chabab|chabab mohammedia|mohammedia$|scc mohammedia)", "Chabab Mohammédia", 1948, 2100),
    (r"(ock|oc khouribga|ol khouribga|olympi(c|que) (club )?(de )?khouribga|olympique c khouribga|o khouribga|khour[i]?gba$|khouribga$)", "OC Khouribga", 1923, 2100),
    (r"(oc safi|ocs safi|olympi(c|que) (club )?(de )?safi|olympique c safi|r safi)", "Olympic Safi", 1921, 2100),
    (r"(tas|tihad|ts ittihad|ts casablanca|tsc|ir casablanca tas|ittihad ryadi casablanca)", "TAS Casablanca", 1947, 2100),
    (r"(usk|union sidi kacem|us sidi kacem|u sidi kacem|sidi kacem$)", "US Sidi Kacem", 1927, 2100),
    (r"(as|sa|ass|sporting) sale|association sportive de sale|sale$|sas", "AS Salé", 1928, 2100),
    # JS Massira = Forces Auxiliaires (Ben Slimane): a página de 1994/95 diz que o "Auxiliary Forces" mudou para El Ayoun
    # e passou a se chamar Jeunesse Sportive Massira
    (r"(jsm|asfa|as forces auxiliaires|forces auxiliaires|auxiliary forces|js (el )?massira|jeunesse (s(portive)? )?(de la |el )?massira|jsm el ayoun|j el ayoun|jeunesse el ayoun|massira$|jeunesse$|el ayoun$)",
     "JS Massira", 1975, 2100),
    (r"(izk|iz khemisset|ittihad (zemmouri )?(de )?khemisset|i khemisset|khemisset$|izk khemisset|cmk khemisset)", "IZ Khémisset", 1940, 2100),
    (r"(ejs|ejsc|esjc|etoile jeunesse|etoile casablanca|etoile de casablanca)", "EJS Casablanca", 1940, 2100),
    (r"(adm|association des douanes|racing athletic|rac|racing ac|racing casablanca|racing$)", "Racing Casablanca", 1917, 2100),
    (r"(cr al hoceima|chabab rif|al hoceima)", "Chabab Rif Hoceima", 1950, 2100),
    (r"(chabab )?kasba?h? tadla", "Chabab Kasba Tadla", 1950, 2100),
    (r"ca khenifra|chabab atlas", "CA Khénifra", 1950, 2100),
    (r"rapide oued zem|rc oued zem", "Rapide Oued Zem", 1950, 2100),
    (r"rca zemamra|cr khemis zemamra", "RCA Zemamra", 1950, 2100),
    (r"cay berrechid", "CAY Berrechid", 1950, 2100),
    (r"js soualem|cr salmi", "JS Soualem", 1950, 2100),
    (r"(union|us) (sportive |de )?touarga|ust", "Union Touarga", 1950, 2100),
    (r"olympique dcheira", "Olympique Dcheira", 1950, 2100),
    (r"us yaacub mansour|us yacoub|yacoub el mansour", "US Yacoub El Mansour", 1950, 2100),
    (r"youssoufia berrechid", "CAY Berrechid", 1950, 2100),
    (r"youssoufia", "Youssoufia Rabat", 1950, 2100),
    (r"rachad bernou?ssi", "Rachad Bernoussi", 1950, 2100),
    (r"(tfb|ittihad riadi fkih|ir fkih)", "IR Fkih Ben Salah", 1950, 2100),
    (r"(mcm|mouloudia club de marrakech|mc marrakech|m marrakech)", "MC Marrakech", 1950, 2100),
    (r"(usm|union sportive( de)? mohammedia)$|union sportive (de )?mohammedia", "US Mohammédia", 1975, 1990),
    (r"(clas|cla)( casablanca)?$", "CLAS Casablanca", 1950, 2100),
    (r"amal (club de )?belksiri", "Amal Belksiri", 1950, 2100),
    (r"chabab sakia", "Chabab Sakia El Hamra", 1950, 2100),
    (r"hilal (association de )?nador", "Hilal Nador", 1950, 2100),
    (r"renaissance sportive de kenitra|rsk|nehda kenitra", "RS Kénitra", 1950, 2100),
    (r"\W*union sportive musulmane d ?oujda", "USM Oujda", 1950, 2100),
    (r"(club )?olympique (club )?(de )?casablanca|ocasablanca", "Olympique de Casablanca", 1980, 2100),
    (r"is casablanca", "IS Casablanca", 1950, 2100),
    (r"credit agricole", "Crédit Agricole Rabat", 1950, 2100),
    (r"(rsm|rachad de meknes)", "Rachad de Meknès", 1950, 2100),
    (r"(lar|chabab larache)", "Chabab Larache", 1950, 2100),
    (r"(msr|moghreb sportif de rabat)", "Moghreb Sportif de Rabat", 1950, 2100),
    (r"(brr|as barid mohammedi)", "Barid Mohammedi", 1950, 2100),
    (r"(qi|quartier industriel)", "Quartier Industriel", 1950, 2100),
    (r"ascom", "ASCOM", 1950, 2100),
    (r"(asm)$", "ASM", 1950, 2100),
    # era colonial
    (r"(sm|stade ?marocain|club stade marocain)( de)?( rabat)?$", "Stade Marocain", 1915, 2100),
    (r"(us marocaine?|usm casab?l?anca|union sportive marocaine?)( casablanca)?$|usm$", "US Marocaine", 1915, 1960),
    # "US Casablanca" é a mesma US Athlétique: em 1929/30 o "US Casablanca" que se classifica na Ligue de Chaouia aparece no
    # mata-mata como "USA Casablanca"; em 1935/36 a tabela diz "US Casablanca" e os jogos "USA Casablanca"
    (r"(usa casablanca|us athletique|usa$|us casablanca)", "USA Casablanca", 1915, 1960),
    (r"(ca marocain|club athletique marocain|ca casablanca)", "CA Marocain", 1915, 1930),
    (r"(rc marocain|rc maroquin|racing club marocain|racing cm)", "Racing Club Marocain", 1915, 1925),
    (r"club sportif colonial", "Club Sportif Colonial", 1915, 1930),
    # (o título de 1923/24, "Olympique Marocaine (Casablanca)" na lista da RSSSF, entra na conta dos 6 do Olympique Marocain)
    (r"olympique marocaine?( rabat| casablanca)?$", "Olympique Marocain", 1915, 1960),
    (r"(rabat (fc|football club))", "Rabat FC", 1915, 1930),
    (r"sporting club de rabat", "Sporting Club de Rabat", 1915, 1930),
    (r"union (athletique )?(de )?ke?n?t?itra|union kentitra", "Union Athlétique de Kénitra", 1915, 1935),
    (r"ca port lyautey", "CA Port Lyautey", 1930, 1955),
    (r"us fes( usa)?$|us fes$", "US Fès", 1915, 1960),
    (r"aspt+ ?f[e]s|asptt fes", "ASPTT Fès", 1915, 1960),
    (r"(as )?tanger ?f(d)?es|association sportif de tanger fes|as tanger fes|ast$", "AS Tanger-Fès", 1915, 1960),
    (r"aspt+ ?(\(?casablanca\)?|csablanca)?$|aspttcasablanca|asptt casablanca", "ASPTT Casablanca", 1915, 1960),
    (r"aspp?tt rabat|asppt rabat", "ASPTT Rabat", 1915, 1960),
    (r"(scc )?roches noire?s|sc club des roches noires", "Roches Noires", 1915, 1960),
    (r"ideal casablanca", "Ideal Casablanca", 1915, 1960),
    (r"as casablanca", "AS Casablanca", 1915, 1960),
    (r"olympique casablanca", "Olympique Casablanca", 1915, 1960),
    (r"racing universitaire", "Racing Universitaire", 1915, 1960),
    (r"moghreb casablanca", "Moghreb Casablanca", 1915, 1960),
    (r"cheminots( casablanca)?$", "Cheminots Casablanca", 1915, 1960),
    (r"cheminots rabat", "Cheminots Rabat", 1915, 1960),
    (r"fedala sport", "Fedala Sport", 1915, 1960),
    (r"(sporting|sc) mazagan", "Sporting Mazagan", 1915, 1960),
    (r"sa marrakech", "SA Marrakech", 1915, 1960),
    (r"as marrakech", "AS Marrakech", 1915, 1960),
    (r"(us|union sportive de) safi", "US Safi", 1915, 1960),
    (r"sc safi", "SC Safi", 1915, 1960),
    (r"usd? mekn[e]s|usd meknes|us de meknes", "USD Meknès", 1915, 1960),
    (r"meknes sports", "Meknès Sports", 1915, 1960),
    (r"olympique meknes", "Olympique Meknès", 1915, 1960),
    (r"stade meknes", "Stade Meknès", 1915, 1960),
    (r"stade rabat", "Stade Rabat", 1915, 1960),
    (r"as rabat", "AS Rabat", 1915, 1960),
    (r"us rabat sale", "US Rabat Salé", 1915, 1960),
    (r"us oujda", "US Oujda", 1915, 1960),
    (r"us petitjean", "US Petitjean", 1915, 1960),
    (r"sc taza", "SC Taza", 1915, 1960),
    (r"as mogador", "AS Mogador", 1915, 1960),
    (r"so agadir", "SO Agadir", 1915, 1960),
    (r"sa settat", "SA Settat", 1915, 1960),
    (r"asf tanger", "ASF Tanger", 1915, 1960),
    (r"moghreb tanger", "Moghreb Tanger", 1915, 1960),
    (r"hilal tanger", "Hilal Tanger", 1915, 1960),
]


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"\s+\d+$", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    if not nome:
        return None
    nome = re.sub(r"\s*\((\d|[A-Z]{2,5}(\s*\(\d\))?)\)\s*$", "", nome)   # "Union Sidi Kacem (USK)", "AS Salé (2)"
    nome = re.sub(r"\s*\[[^\]]*\]\s*$", "", nome).rstrip("*")
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
