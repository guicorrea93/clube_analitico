"""Identidade dos clubes nigerianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Enugu Rangers", "Enyimba", "Kano Pillars", "Shooting Stars");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Enugu Rangers = Rangers = Rangers International; Heartland = Iwuanyanwu Nationale (a RSSSF: "now called Heartland FC");
    Dolphin = Eagle Cement (a RSSSF conta os títulos juntos); Shooting Stars = IICC = 3SC; Nigerian Ports Authority =
    NPA = Port Authority; NITEL Vasco = P&T Vasco da Gama (os Correios e Telégrafos viraram NITEL em 1985);
  - ABS (Ilorin) = Bukola Babes (o ogol já dá ABS FC em 2010/11);
  - Ifeanyi Ubah = Gabros International (comprado e renomeado em 2015; em 2015 a página ainda usa "Gabros United");
  - o Rivers United (fusão do Dolphin com o Sharks em 2016) é um clube próprio, como a RSSSF conta.
- "Kwara" sozinho é o Kwara United, fora 1998 a 2000, quando o Kwara Stars também jogava (ver as edições).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

LAG = ("Lagos", "Lagos")
PH = ("Port Harcourt", "Rivers")
OW = ("Owerri", "Imo")
JOS = ("Jos", "Plateau")
KAN = ("Kano", "Kano")
IBA = ("Ibadan", "Oyo")
BEN = ("Benin City", "Edo")
ILO = ("Ilorin", "Kwara")
UYO = ("Uyo", "Akwa Ibom")

# nome de exibição -> (cidade, estado)
CLUBES: dict[str, tuple[str, str]] = {
    "Enugu Rangers": ("Enugu", "Enugu"), "Enyimba": ("Aba", "Abia"), "Heartland": OW, "Kun Khalifat": OW,
    "Shooting Stars": IBA, "Leventis United": IBA, "Kano Pillars": KAN, "Barau": KAN, "Racca Rovers": KAN,
    "Dolphin": PH, "Sharks": PH, "Rivers United": PH, "Go Round": ("Omoku", "Rivers"),
    "Bendel Insurance": BEN, "Bendel United": BEN, "New Nigerian Bank": BEN,
    "Julius Berger": LAG, "Stationery Stores": LAG, "ACB": LAG, "MFM": LAG, "Ikorodu City": LAG, "Ikorodu United": LAG,
    "Sporting Lagos": LAG, "NEPA": LAG, "NITEL Vasco": ("Enugu", "Enugu"), "Leventis Lagos": LAG, "Abiola Babes": ("Abeokuta", "Ogun"),
    "Mighty Jets": JOS, "Plateau United": JOS, "JUTH": JOS, "Giwa": JOS, "Highlanders": JOS, "JIB Rock Strikers": JOS,
    "BCC Lions": ("Gboko", "Benue"), "Lobi Stars": ("Makurdi", "Benue"),
    "El-Kanemi Warriors": ("Maiduguri", "Borno"), "Gombe United": ("Gombe", "Gombe"), "Doma United": ("Gombe", "Gombe"),
    "Wikki Tourists": ("Bauchi", "Bauchi"), "Wunti": ("Bauchi", "Bauchi"), "Udoji United": ("Awka", "Anambra"),
    "Jasper United": ("Onitsha", "Anambra"), "Ifeanyi Ubah": ("Nnewi", "Anambra"),
    "Katsina United": ("Katsina", "Katsina"), "Kwara United": ILO, "Kwara Stars": ILO, "ABS": ILO,
    "Niger Tornadoes": ("Minna", "Níger"), "Nasarawa United": ("Lafia", "Nasarawa"),
    "Akwa United": UYO, "Akwa Starlets": UYO, "Dakkada": UYO, "Calabar Rovers": ("Calabar", "Cross River"),
    "Nigerian Ports Authority": ("Warri", "Delta"), "Warri Wolves": ("Warri", "Delta"), "Delta Force": ("Asaba", "Delta"),
    "Delta United": ("Asaba", "Delta"), "Bayelsa United": ("Yenagoa", "Bayelsa"), "Ocean Boys": ("Brass", "Bayelsa"),
    "Nembe City": ("Nembe", "Bayelsa"), "Sunshine Stars": ("Akure", "Ondo"), "Rising Stars": ("Akure", "Ondo"),
    "Gateway": ("Abeokuta", "Ogun"), "Remo Stars": ("Sagamu", "Ogun"), "Obanta United": ("Ijebu-Ode", "Ogun"),
    "Crown": ("Ogbomosho", "Oyo"), "Prime": ("Oshogbo", "Osun"), "Abia Warriors": ("Umuahia", "Abia"),
    "Kaduna United": ("Kaduna", "Kaduna"), "Ranchers Bees": ("Kaduna", "Kaduna"), "New Nigeria Kaduna": ("Kaduna", "Kaduna"),
    "Kada City": ("Kaduna", "Kaduna"), "DIC Bees": ("Kaduna", "Kaduna"), "Jigawa Golden Stars": ("Dutse", "Jigawa"),
    "Adamawa United": ("Yola", "Adamawa"), "Yobe Desert Stars": ("Damaturu", "Yobe"), "Zamfara United": ("Gusau", "Zamfara"),
    "FC Taraba": ("Jalingo", "Taraba"), "FC Abuja": ("Abuja", "Território da Capital Federal"), "Concord": ("Abeokuta", "Ogun"),
    "VIP": ("Port Harcourt", "Rivers"), "Nigerdock": LAG, "Flash Flamingoes": BEN, "NNPC": ("Warri", "Delta"),
    "Octopus": PH, "WNDC": IBA, "Nigerian Army XI": LAG, "IBI": ("Ibadan", "Oyo"), "MFM Lagos": LAG,
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(enugu )?rangers( int\w*)?( fc)?$|rangers intern|rangers intl|rangers int l", "Enugu Rangers", 1972, 2100),
    (r"enyimba( fc| international)?", "Enyimba", 1972, 2100),
    (r"heartland|iwuanyanwu( nationale)?|^nationale$", "Heartland", 1972, 2100),
    (r"shooting( s| stars)?( industrial| fc)?$|^3sc$|iicc shooting stars", "Shooting Stars", 1972, 2100),
    (r"(kano )?pillars( fc)?$", "Kano Pillars", 1972, 2100),
    (r"dolphins?( fc)?$|eagle c(ement)?$", "Dolphin", 1972, 2100),
    (r"(port harcourt )?sharks( p h| fc)?$", "Sharks", 1972, 2100),
    (r"rivers united", "Rivers United", 1972, 2100),
    (r"(bendel )?insurance", "Bendel Insurance", 1972, 2100),
    (r"bendel united", "Bendel United", 1972, 2100),
    (r"(julius |j )?berger", "Julius Berger", 1972, 2100),
    (r"b ?c ?c lions", "BCC Lions", 1972, 2100),
    (r"station[ae]ry stores|^stores$", "Stationery Stores", 1972, 2100),
    (r"a ?c ?b( lagos)?( fc)?$", "ACB", 1972, 2100),
    (r"(mighty )?jets$", "Mighty Jets", 1972, 2100),
    (r"plateau( u| utd| united)?$", "Plateau United", 1972, 2100),
    (r"el ?kanemi( w| warriors)?", "El-Kanemi Warriors", 1972, 2100),
    (r"gombe ?(united|utd)?$|gombeunited", "Gombe United", 1972, 2100),
    (r"udoji( utd| united)?( awka)?$", "Udoji United", 1972, 2100),
    (r"jasper( utd| united)?$", "Jasper United", 1972, 2100),
    (r"katsina( utd| united)?$", "Katsina United", 1972, 2100),
    (r"kwara stars", "Kwara Stars", 1972, 2100),
    (r"kawara$|kwara( utd| united)?$", "Kwara United", 1972, 2100),
    (r"(niger )?tornadoe?s?$", "Niger Tornadoes", 1972, 2100),
    (r"wikki( tourists)?$", "Wikki Tourists", 1972, 2100),
    (r"lobi( stars)?$", "Lobi Stars", 1972, 2100),
    (r"gabros( international| utd| united)?$", "Ifeanyi Ubah", 1972, 2100),
    (r"nigerian ports authority|^npa$|port authority", "Nigerian Ports Authority", 1972, 2100),
    (r"^nepa$", "NEPA", 1972, 2100),
    (r"new nigerian bank|^nnb$", "New Nigerian Bank", 1972, 2100),
    (r"new nigeria$", "New Nigeria Kaduna", 1972, 2100),
    (r"nitel( vasco)?$|p t vasco da gama|^vasco da gama$", "NITEL Vasco", 1972, 2100),
    (r"leventis$", "Leventis Lagos", 1972, 1979),
    (r"leventis united$", "Leventis United", 1980, 2100),
    (r"abiola babes", "Abiola Babes", 1972, 2100),
    (r"abs( fc)?$", "ABS", 1972, 2100),
    (r"abia warriors", "Abia Warriors", 1972, 2100),
    (r"adamawa( united)?$", "Adamawa United", 1972, 2100),
    (r"akwa starlets", "Akwa Starlets", 1972, 2100),
    (r"akwa( united)?( fc)?$", "Akwa United", 1972, 2100),
    (r"barau( fc)?$", "Barau", 1972, 2100),
    (r"bayelsa( united)?( fc)?$", "Bayelsa United", 1972, 2100),
    (r"bukola babes", "ABS", 1972, 2100),
    (r"calabar rovers", "Calabar Rovers", 1972, 2100),
    (r"^concord$", "Concord", 1972, 2100),
    (r"crown( fc)?$", "Crown", 1972, 2100),
    (r"dakkada", "Dakkada", 1972, 2100),
    (r"delta force", "Delta Force", 1972, 2100),
    (r"delta( united)?$", "Delta United", 1972, 2100),
    (r"dic bees", "DIC Bees", 1972, 2100),
    (r"doma united", "Doma United", 1972, 2100),
    (r"^flash$", "Flash Flamingoes", 1972, 2100),
    (r"gateway", "Gateway", 1972, 2100),
    (r"giwa", "Giwa", 1972, 2100),
    (r"go ?round", "Go Round", 1972, 2100),
    (r"(jos )?highlanders", "Highlanders", 1972, 2100),
    (r"^i b i$", "IBI", 1972, 2100),
    (r"ifeanyi ubah?", "Ifeanyi Ubah", 1972, 2100),
    (r"ikorodu city", "Ikorodu City", 1972, 2100),
    (r"ikorodu united", "Ikorodu United", 1972, 2100),
    (r"j i b rock strikers", "JIB Rock Strikers", 1972, 2100),
    (r"jigaw?wa( golden stars)?( fc)?$", "Jigawa Golden Stars", 1972, 2100),
    (r"juth", "JUTH", 1972, 2100),
    (r"kada city", "Kada City", 1972, 2100),
    (r"kaduna( united)?( fc)?$", "Kaduna United", 1972, 2100),
    (r"kun khalifat", "Kun Khalifat", 1972, 2100),
    (r"mfm", "MFM", 1972, 2100),
    (r"nasarawa( united)?( fc)?$", "Nasarawa United", 1972, 2100),
    (r"nembe city", "Nembe City", 1972, 2100),
    (r"nnpc", "NNPC", 1972, 2100),
    (r"nigerdock", "Nigerdock", 1972, 2100),
    (r"nigerian army", "Nigerian Army XI", 1972, 2100),
    (r"obanta u\w*", "Obanta United", 1972, 2100),
    (r"ocean( boys)?( fc)?$", "Ocean Boys", 1972, 2100),
    (r"octopus", "Octopus", 1972, 2100),
    (r"prime( fc)?$", "Prime", 1972, 2100),
    (r"ranchers bees", "Ranchers Bees", 1972, 2100),
    (r"remo stars", "Remo Stars", 1972, 2100),
    (r"rising stars", "Rising Stars", 1972, 2100),
    (r"sporting lagos", "Sporting Lagos", 1972, 2100),
    (r"sunshine( stars)?( fc)?$", "Sunshine Stars", 1972, 2100),
    (r"(fc )?taraba( united)?$", "FC Taraba", 1972, 2100),
    (r"^vip$", "VIP", 1972, 2100),
    (r"warri wolves", "Warri Wolves", 1972, 2100),
    (r"wndc", "WNDC", 1972, 2100),
    (r"wunti", "Wunti", 1972, 2100),
    (r"yobe( desert)?( stars)?( fc)?$", "Yobe Desert Stars", 1972, 2100),
    (r"zamfara( united)?( fc)?$", "Zamfara United", 1972, 2100),
    (r"fc abuja|abuja fc", "FC Abuja", 1972, 2100),
    (r"racca rovers", "Racca Rovers", 1972, 2100),
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
    nome = re.sub(r"\s*\((\d+ ag|[^)]*)\)\s*$", lambda m: "" if "ag" in m.group(1) else "", nome)   # "(Aba)"
    nome = re.sub(r"[*]+$", "", nome).strip()
    nome = re.sub(r"\s+FC$", "", nome)   # "Lobi Stars FC (Makurdi)"
    nome = re.sub(r"\bUtd\b\.?", "United", nome)            # "Kaduna Utd" (ogol)
    nome = re.sub(r"\bGold\.\s*", "Golden ", nome)          # "Jigawa Gold. Stars" (ogol)
    nome = re.sub(r"^(.+?)\s+\1\b", r"\1", nome)           # "Shooting Stars Shooting Stars" (tabela da RSSSF)
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
