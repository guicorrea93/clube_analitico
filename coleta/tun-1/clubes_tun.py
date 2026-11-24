"""Identidade dos clubes tunisianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4) e do recado do agente 1:
- nome pelo qual o clube é conhecido no Brasil ("Espérance de Tunis", "Club Africain", "Étoile du Sahel", "CS Sfaxien");
- nomes árabes com hífen; o Al-Ahly puro é o do Egito: o de Mateur é "Al-Ahly de Mateur";
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Railway Sports (Sfax), campeão de 1933/34 e 1952/53, = Sfax Railways Sports (a RSSSF conta os títulos juntos);
  - US Tunisienne (campeã de 1929/30 a 1932/33) = Union Sportive Tunisienne (1949-1970);
  - Union Sportive Ferryville = USM Bourguiba (a lista de tabelas finais: "US Ferryville changed name for USM Bourguiba",
    1956); Olympique Tunis = US Musulmane Olympique ("changed name", 1957);
  - Patrie Football Club Bizertin = Patrie et Football Club Bizertin; Club Sportif Cheminots = CS Cheminots; Avenir
    Sportif de Gabès = AS Gabès; FC Jérissa = Football Club Djerissa; FC Bizerte (1907) = Stade maritime de Bizerte;
  - Stade Africain Menzel Bourguiba = SA Menzel Bourguiba (fica separado da USM Bourguiba).
- nomes curtos dos anos 1990 ("Sahel", "Stade", "Transports", "Esperance") resolvem pelo clube da 1ª divisão do ano.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

TUN = ("Túnis", "Túnis")
SOU = ("Sousse", "Sousse")
SFA = ("Sfax", "Sfax")
BIZ = ("Bizerte", "Bizerte")

# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "Espérance de Tunis": TUN, "Club Africain": TUN, "Stade Tunisien": ("Le Bardo", "Túnis"), "Club Tunisien": TUN,
    "US Tunisienne": TUN, "Avenir Musulman": TUN, "Stade Populaire": TUN, "US Musulmane Olympique": TUN, "CO Transports": TUN,
    "CS Cheminots": TUN, "AS Marsa": ("La Marsa", "Túnis"), "EOG Kram": ("Le Kram", "Túnis"), "Racing Club de Tunis": TUN,
    "Sporting Club de Tunis": TUN, "Stade Gaulois": TUN, "Avant-Garde de Tunis": TUN, "Italia de Tunis": TUN,
    "Savoia de La Goulette": ("La Goulette", "Túnis"), "Lycée Carnot": TUN, "Collège Alaoui": TUN,
    "Association Sportive Française": TUN, "JS Omrane": TUN,
    "CS Hammam-Lif": ("Hammam-Lif", "Ben Arous"), "Vaillante-Jeunesse de Hammam-Lif": ("Hammam-Lif", "Ben Arous"),
    "AS Mégrine": ("Mégrine", "Ben Arous"), "AS Ariana": ("Ariana", "Ariana"), "US Sidi Thabet": ("Sidi Thabet", "Ariana"),
    "AS Oued Ellil": ("Oued Ellil", "Manouba"), "JS Methouienne": ("Métouia", "Gabès"),
    "Étoile du Sahel": SOU, "Stade Soussien": SOU, "Patriote de Sousse": SOU, "STIA Sousse": SOU, "Athlétic Club de Sousse": SOU,
    "ES Hammam-Sousse": ("Hammam Sousse", "Sousse"),
    "CS Sfaxien": SFA, "Sfax Railways Sports": SFA, "Stade Sportif Sfaxien": SFA, "Océan Club de Kerkennah": ("Kerkennah", "Sfax"),
    "CA Bizertin": BIZ, "Patrie FC Bizertin": BIZ, "Stade Maritime de Bizerte": BIZ,
    "USM Bourguiba": ("Menzel Bourguiba", "Bizerte"), "SA Menzel Bourguiba": ("Menzel Bourguiba", "Bizerte"),
    "Sporting Club de Ferryville": ("Menzel Bourguiba", "Bizerte"), "Al-Ahly de Mateur": ("Mateur", "Bizerte"),
    "US Monastir": ("Monastir", "Monastir"), "CS Chebba": ("Chebba", "Mahdia"), "El Makarem de Mahdia": ("Mahdia", "Mahdia"),
    "AS Rejiche": ("Rejiche", "Mahdia"),
    "JS Kairouan": ("Kairouan", "Kairouan"), "AS Kairouan": ("Kairouan", "Kairouan"),
    "Olympique Béja": ("Béja", "Béja"), "Olympique du Kef": ("Le Kef", "Le Kef"), "Jendouba Sport": ("Jendouba", "Jendouba"),
    "FC Djerissa": ("Jérissa", "Le Kef"), "AS Kasserine": ("Kasserine", "Kasserine"),
    "AS Gabès": ("Gabès", "Gabès"), "Stade Gabésien": ("Gabès", "Gabès"), "CS Gabésien": ("Gabès", "Gabès"),
    "ES Zarzis": ("Zarzis", "Médenine"), "AS Djerba": ("Djerba", "Médenine"), "CO Médenine": ("Médenine", "Médenine"),
    "US Ben Guerdane": ("Ben Guerdane", "Médenine"), "Espoir Jerba": ("Djerba", "Médenine"),
    "US Tataouine": ("Tataouine", "Tataouine"), "EGS Gafsa": ("Gafsa", "Gafsa"), "ES Métlaoui": ("Métlaoui", "Gafsa"),
    "Khanfous Club": ("Redeyef", "Gafsa"), "LPS Tozeur": ("Tozeur", "Tozeur"), "EO Sidi Bouzid": ("Sidi Bouzid", "Sidi Bouzid"),
    "CO Sidi Bouzid": ("Sidi Bouzid", "Sidi Bouzid"),
    "ES Béni Khalled": ("Béni Khalled", "Nabeul"), "Grombalia Sports": ("Grombalia", "Nabeul"), "CS Korba": ("Korba", "Nabeul"),
    "CS Menzel Bouzelfa": ("Menzel Bouzelfa", "Nabeul"), "AS Solimane": ("Soliman", "Nabeul"),
    "US Maghrébine": ("", ""),
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(esperance|est|es tunis)( sportive)?( de)?( st)?( s)?( tunis)?$|esperance (sportive )?(de )?tunis|esperance st|esperance s tunis",
     "Espérance de Tunis", 1919, 2100),
    (r"(club )?africai?n|c africain|club africian", "Club Africain", 1920, 2100),
    (r"(etoile|es)( sportive)?( du)? sahel|sahel$|ess$", "Étoile du Sahel", 1925, 2100),
    (r"(cs|club sportif) sfax(ien)?|sfaxien$|cs sfax$", "CS Sfaxien", 1928, 2100),
    (r"(stade|st) tunisien|stade t$|stade$", "Stade Tunisien", 1948, 2100),
    (r"(ca|club athl\w*) bizert(in|e)|bizertin$|bizerte$", "CA Bizertin", 1928, 2100),
    (r"(us|union sportive) monastir(ienne)?|monastir$", "US Monastir", 1923, 2100),
    (r"(cs|club sportif( de)?) ham+a[mn]+[ -]?lif|ham+a[mn]+ lif$", "CS Hammam-Lif", 1944, 2100),
    (r"(js|jeunesse sportive)( de)? kairouan(aise)?|^js$|kairouan$", "JS Kairouan", 1942, 2100),
    (r"(o|ol|olympique)( de)? b[e]ja|beja$", "Olympique Béja", 1929, 2100),
    (r"(o|olympique)( du)? kef|kef$", "Olympique du Kef", 1950, 2100),
    (r"(as|avenir( sportif)?)( de)?( la)? marsa|marsa$", "AS Marsa", 1939, 2100),
    (r"(es|esperance( sportive)?)( de)? zarzis|zarzis$", "ES Zarzis", 1934, 2100),
    (r"(sfax )?railways? sports?( sfax)?|sfax rs", "Sfax Railways Sports", 1920, 2100),
    (r"(co|club olympique)( des)? transports|transports$", "CO Transports", 1950, 2100),
    (r"(cs|club sportif) cheminots", "CS Cheminots", 1950, 2100),
    (r"(as|avenir sportif)( de)? gabes", "AS Gabès", 1950, 2100),
    (r"stade gabesien", "Stade Gabésien", 1950, 2100),
    (r"(cs|club sportif) gabesien", "CS Gabésien", 1920, 2100),
    (r"(as|avenir( s(portif)?)?)( de)? kasserine", "AS Kasserine", 1950, 2100),
    (r"(as|association sportive)( de)? djerba|djerba$", "AS Djerba", 1950, 2100),
    (r"espoir jerba", "Espoir Jerba", 1950, 2100),
    (r"(co|o|club olympique)( de)? medenine|medenine$", "CO Médenine", 1950, 2100),
    (r"(egs|el gawafel( sportives)?( de)?) gafsa", "EGS Gafsa", 1950, 2100),
    (r"es (hama?m )?(sousse|hamam sousse)|es hamm?am sousse", "ES Hammam-Sousse", 1950, 2100),
    (r"((es|etoile sportive) )?b[e]ni khall?ed", "ES Béni Khalled", 1950, 2100),
    (r"es metlaoui", "ES Métlaoui", 1950, 2100),
    (r"us ben guerdane", "US Ben Guerdane", 1950, 2100),
    (r"us tataouine", "US Tataouine", 1950, 2100),
    (r"as solimane|as slimane", "AS Solimane", 1950, 2100),
    (r"cs chebba", "CS Chebba", 1950, 2100),
    (r"as rejiche", "AS Rejiche", 1950, 2100),
    (r"js omrane", "JS Omrane", 1950, 2100),
    (r"eo sidi bouzid", "EO Sidi Bouzid", 1950, 2100),
    (r"co sidi bouzid", "CO Sidi Bouzid", 1950, 2100),
    (r"lps tozeur", "LPS Tozeur", 1950, 2100),
    (r"jendouba sport", "Jendouba Sport", 1950, 2100),
    (r"grombalia sports?", "Grombalia Sports", 1950, 2100),
    (r"(oc|ocean club)( de)? kerkenn?ah", "Océan Club de Kerkennah", 1950, 2100),
    (r"(eog|eo goulette|etoile olympique de la goulette)( et)?( kram)?", "EOG Kram", 1950, 2100),
    (r"(el )?ma[kd]arem( de)? mahdia|emm$", "El Makarem de Mahdia", 1950, 2100),
    (r"stade soussien", "Stade Soussien", 1950, 2100),
    (r"stia sousse", "STIA Sousse", 1950, 2100),
    (r"patriote de sousse|ps$", "Patriote de Sousse", 1920, 2100),
    (r"stade sportif sfaxien", "Stade Sportif Sfaxien", 1950, 2100),
    (r"(as|association sportive|avenir sportif) (oued ellil)", "AS Oued Ellil", 1950, 2100),
    (r"(as|association sportive) ariana|asa$", "AS Ariana", 1950, 2100),
    (r"association sportive megrine", "AS Mégrine", 1950, 2100),
    (r"club sportif korba", "CS Korba", 1950, 2100),
    (r"club sportif menzel bouzelfa", "CS Menzel Bouzelfa", 1950, 2100),
    (r"us sidi thabet", "US Sidi Thabet", 1950, 2100),
    (r"(stade africain|sa) menzel[ -]?bourguiba", "SA Menzel Bourguiba", 1950, 2100),
    (r"(en nadi )?(al )?ahly mateur", "Al-Ahly de Mateur", 1950, 2100),
    (r"union sportive maghre[hb]ine", "US Maghrébine", 1950, 2100),
    (r"as kairouan", "AS Kairouan", 1950, 2100),
    # era colonial e anos 1950
    (r"(union sportive|us) ferryville|union sportive musulmane menzel bourguiba|usm bourguiba", "USM Bourguiba", 1920, 1990),
    (r"(us|union sportive) tunisienne|ust$|us tunis$", "US Tunisienne", 1920, 1990),
    (r"olympique (de )?tunis|union sportive musulmane olympique", "US Musulmane Olympique", 1920, 1990),
    (r"club tunisien", "Club Tunisien", 1920, 1990),
    (r"avenir musulman", "Avenir Musulman", 1920, 1990),
    (r"stade populaire", "Stade Populaire", 1920, 1990),
    (r"patrie (et )?(football club|fc) bizertin", "Patrie FC Bizertin", 1920, 1990),
    (r"jeunesse sportive methouienne|js metouia", "JS Methouienne", 1920, 1990),
    (r"association sportive francaise", "Association Sportive Française", 1920, 1990),
    (r"(fc|football club) d?j[e]rissa", "FC Djerissa", 1920, 1990),
    (r"khanfous club", "Khanfous Club", 1920, 1990),
    (r"vaillante jeunesse", "Vaillante-Jeunesse de Hammam-Lif", 1920, 1990),
    (r"racing (club )?(de )?tunis|racing club$|racing de tunis", "Racing Club de Tunis", 1906, 1960),
    (r"sporting (club )?(de )?ferryville", "Sporting Club de Ferryville", 1906, 1960),
    (r"sporting club( de)?( tunis)?$", "Sporting Club de Tunis", 1906, 1960),
    (r"stade gaulois", "Stade Gaulois", 1906, 1960),
    (r"avant garde", "Avant-Garde de Tunis", 1906, 1960),
    (r"italia( de)?( tunis)?$", "Italia de Tunis", 1906, 1960),
    (r"savoia", "Savoia de La Goulette", 1906, 1960),
    (r"athletic club de sousse", "Athlétic Club de Sousse", 1906, 1960),
    (r"(fc bizerte|stade maritime( de)? bizerte)", "Stade Maritime de Bizerte", 1906, 1960),
    (r"lycee carnot", "Lycée Carnot", 1906, 1960),
    (r"college alaoui", "Collège Alaoui", 1906, 1960),
]


def _regra(k: str, ano: int) -> str | None:
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    if not nome:
        return None
    nome = re.sub(r"\s*\((\d+ ag|[^)]*)\)\s*$", lambda m: "" if "ag" in m.group(1) else m.group(0), nome)   # "(0 ag)"
    nome = re.sub(r"\s+b\)\s*$", "", nome)
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
