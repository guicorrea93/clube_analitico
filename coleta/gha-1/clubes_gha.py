"""Identidade dos clubes ganeses: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Asante Kotoko", "Hearts of Oak", "Ashanti Gold");
- nome que já existe em outro país leva o país ("Mighty Jets (Gana)", "Highlanders (Gana)", "Aston Villa (Gana)"); os de
  Berekum levam a cidade, como são conhecidos ("Berekum Arsenal", "Berekum Chelsea");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Ashanti Gold = Goldfields = AshantiGold (a RSSSF conta os títulos juntos); Ebusua Dwarfs = Mysterious Dwarfs;
    Real Tamale United = RTU; Swedru All Blacks = All Blacks = Gamba All Blacks; Tano Bofoakwa = Bofoakwa; Brong Ahafo
    United = BA United; King Faisal Babes = King Faisal; Wa All Stars = All Stars (2007-2011); Inter Allies =
    International Allies; WAFA = West Africa Football Academy; Eleven Wonders = Techiman Eleven Wonders.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

ACC = ("Acra", "Grande Acra")
KUM = ("Kumasi", "Ashanti")
TEM = ("Tema", "Grande Acra")
SEK = ("Sekondi-Takoradi", "Ocidental")

# nome de exibição -> regex (sobre a chave do nome), cidade, região, primeiro e último ano
_DADOS: list[tuple[str, str, tuple[str, str], int, int]] = [
    ("Asante Kotoko", r"(asante )?kotoko|^asante$", KUM, 1958, 2100),
    ("Hearts of Oak", r"(accra )?hearts( of oak)?( sc| sporting club)?$", ACC, 1958, 2100),
    ("Ashanti Gold", r"(obuasi )?(ashanti ?gold|goldfields|ashgold)( sc| sporting club)?$", ("Obuasi", "Ashanti"), 1958, 2100),
    ("Great Olympics", r"(great )?olympics$", ACC, 1958, 2100),
    ("Hasaacas", r"(sekondi )?hasaacas$", SEK, 1958, 2100),
    ("Eleven Wise", r"(eleven|xi) wise$", SEK, 1958, 2100),
    ("Ebusua Dwarfs", r"(mysterious|cape coast ebusua|ebusua)? ?dwarfs$", ("Cape Coast", "Central"), 1958, 2100),
    ("Real Tamale United", r"(real )?tamale u(nited|ntd)$|^rtu$", ("Tamale", "Norte"), 1958, 2100),
    ("Swedru All Blacks", r"(swedru |gamba )?all blacks( united)?$", ("Agona Swedru", "Central"), 1958, 2100),
    ("Tano Bofoakwa", r"(tano )?b[ao]foakwa( tano)?$", ("Sunyani", "Bono"), 1958, 2100),
    ("Brong Ahafo United", r"(brong ah[ao]f[ou]|b ?a)( united| untd)$", ("Sunyani", "Bono"), 1958, 2100),
    ("Brong Ahafo Stars", r"brong ahafo stars", ("Sunyani", "Bono"), 1958, 2100),
    ("B.A. Stars", r"b ?a stars", ("Sunyani", "Bono"), 1958, 2100),
    ("Okwahu United", r"okwa[hw]u( united)?$", ("Nkawkaw", "Oriental"), 1958, 2100),
    ("Okwawu Stores", r"okwawu stores", ("Nkawkaw", "Oriental"), 1958, 2100),
    ("Cornerstones", r"corner(stone)?s$", KUM, 1958, 2100),
    ("King Faisal Babes", r"(king )?faisal( bab[ei]e?s)?$", KUM, 1958, 2100),
    ("Berekum Arsenal", r"(berekum )?arsenals?$", ("Berekum", "Bono"), 1958, 2100),
    ("Berekum Chelsea", r"(berekum )?chelsea$", ("Berekum", "Bono"), 1958, 2100),
    ("Aduana Stars", r"aduana( stars)?$", ("Dormaa Ahenkro", "Bono"), 1958, 2100),
    ("Medeama", r"medeama( sc)?$", ("Tarkwa", "Ocidental"), 1958, 2100),
    ("Wa All Stars", r"(wa |bolga )?all stars$", ("Wa", "Alto Ocidental"), 2000, 2016),
    ("Bolga All Stars", r"bolga all stars", ("Bolgatanga", "Alto Oriental"), 2017, 2100),
    ("Wa All Stars", r"wa all stars", ("Wa", "Alto Ocidental"), 2017, 2100),
    ("Liberty Professionals", r"liberty( prof\w*)?$", ACC, 1958, 2100),
    ("Heart of Lions", r"(kpando )?heart of lions$", ("Kpando", "Volta"), 1958, 2100),
    ("Power FC", r"power$", ("Koforidua", "Oriental"), 1958, 2100),
    ("Dawu Youngstars", r"dawu( young(st[ae]rs|sters))?$", ("Dawu", "Oriental"), 1958, 2100),
    ("GHAPOHA Readers", r"ghapoha( readers)?$", TEM, 1958, 2100),
    ("Neoplan Stars", r"neoplan stars?$", KUM, 1958, 2100),
    ("Kumapim Stars", r"kumap[ei]m stars?$", ("Asante Mampong", "Ashanti"), 1958, 2100),
    ("Prestea Mine Stars", r"(prestea )?mines? stars$", ("Prestea", "Ocidental"), 1958, 2100),
    ("Venomous Vipers", r"venomous vipers", ("Cape Coast", "Central"), 1958, 2100),
    ("Real Sportive", r"(real )?sportive$", TEM, 1958, 2100),
    ("Feyenoord Academy", r"feyenoord( academy)?$", ("Gomoa Fetteh", "Central"), 1958, 2100),
    ("Tema Youth", r"(tema )?youth$", TEM, 1958, 2100),
    ("Kessben", r"kessben", KUM, 1958, 2100),
    ("Mighty Jets (Gana)", r"(tudu )?mighty jets", ACC, 1958, 2100),
    ("Hotspurs", r"hotspurs", ("Kumasi", "Ashanti"), 1958, 2100),
    ("Zaytuna United", r"zaytuna( united)?$", ("Accra", "Grande Acra"), 1958, 2100),
    ("Saint Mirren (Gana)", r"saint mirren", ("Sekondi-Takoradi", "Ocidental"), 1958, 2100),
    ("Amidaus Professionals", r"amidaus", TEM, 1958, 2100),
    ("Bechem United", r"bechem( united)?$", ("Bechem", "Ahafo"), 1958, 2100),
    ("New Edubiase United", r"(new )?edubiase( united)?$", ("New Edubiase", "Ashanti"), 1958, 2100),
    ("Inter Allies", r"inter ?(national )?allies$", TEM, 1958, 2100),
    ("WAFA", r"wafa|west africa football academy", ("Sogakope", "Volta"), 1958, 2100),
    ("Dreams FC", r"dreams$", ("Dawu", "Oriental"), 1958, 2100),
    ("Elmina Sharks", r"elmina sharks", ("Elmina", "Central"), 1958, 2100),
    ("Karela United", r"karela( united)?$", ("Anyinase", "Ocidental"), 1958, 2100),
    ("Eleven Wonders", r"(techiman )?eleven wonders$", ("Techiman", "Bono Oriental"), 1958, 2100),
    ("Legon Cities", r"legon cities", ACC, 1958, 2100),
    ("Accra Lions", r"accra lions", ACC, 1958, 2100),
    ("Tamale City", r"tamale city", ("Tamale", "Norte"), 1958, 2100),
    ("Kotoku Royals", r"(oda )?kotoku royals", ("Akim Oda", "Oriental"), 1958, 2100),
    ("Nsoatreman", r"nsoatreman", ("Nsoatre", "Bono"), 1958, 2100),
    ("Samartex", r"(fc )?samartex", ("Samreboi", "Ocidental"), 1958, 2100),
    ("Bibiani Gold Stars", r"bibiani gold stars", ("Bibiani", "Ocidental Norte"), 1958, 2100),
    ("Nations FC", r"nations$", ("Abesim", "Bono"), 1958, 2100),
    ("Vision FC", r"vision$", ACC, 1958, 2100),
    ("Basake Holy Stars", r"(basake )?holy stars$", ("Wassa Akropong", "Ocidental"), 2020, 2100),
    ("Holy Stars", r"holy stars$", ("Techiman", "Bono Oriental"), 1958, 1999),
    ("Young Apostles", r"(wenchi )?young apostles$", ("Wenchi", "Bono"), 1958, 2100),
    ("Hohoe United", r"hohoe united", ("Hohoe", "Volta"), 1958, 2100),
    ("Adona Swedru Professionals", r"adona swedru", ("Agona Swedru", "Central"), 1958, 2100),
    ("Techiman City", r"techiman city", ("Techiman", "Bono Oriental"), 1958, 2100),
    ("Wassaman United", r"wassaman( united)?$", ("Tarkwa", "Ocidental"), 1958, 2100),
    ("Mighty Royals", r"mighty royals", ACC, 1958, 2100),
    ("Diamonds", r"^diamonds$", ("Akwatia", "Oriental"), 1958, 2100),
    ("Upper West Heroes", r"upper west heroes", ("Wa", "Alto Ocidental"), 1958, 2100),
    ("Soccer Missionaries", r"soccer missionaries", ("Fosu", "Central"), 1958, 2100),
    ("Voradep", r"voradep( ho)?$", ("Ho", "Volta"), 1958, 2100),
    ("Yeji Stars", r"yeji stars", ("Yeji", "Bono Oriental"), 1958, 2100),
    ("Maxbees", r"maxbees", ("Suhum", "Oriental"), 1958, 2100),
    ("Kwaebibirem United", r"kwaebibirem( united)?$", ("Asuom", "Oriental"), 1958, 2100),
    ("Stay Cool", r"stay cool", ACC, 1958, 2100),
    ("Arnold Warriors", r"arnold warriors", ("Apeguso", "Oriental"), 1958, 2100),
    ("Boye Sowahs Zebi", r"boye sowahs zebi", ACC, 1958, 2100),
    ("Complex Stars", r"complex stars", TEM, 1958, 2100),
    ("Dumas Boys", r"dumas boys", TEM, 1958, 2100),
    ("GIHOC Stars", r"gihoc stars", ("Kumasi", "Ashanti"), 1958, 2100),
    ("Great Lions", r"great lions", ACC, 1958, 2100),
    ("State Traders", r"state traders", TEM, 1958, 2100),
    ("Roadmasters", r"roadmasters", ("Tamale", "Norte"), 1958, 2100),
    ("Tarkwa Gold Stars", r"tarkwa gold stars", ("Tarkwa", "Ocidental"), 1958, 2100),
    ("Volta Juantex", r"volta juantex", ("Ho", "Volta"), 1958, 2100),
    ("Volta United", r"volta united", ("Ho", "Volta"), 1958, 2100),
    ("SS-1974", r"ss 1974", ACC, 1958, 2100),
    ("Ghanacan", r"ghanacan", ("Nsawam", "Oriental"), 1958, 2100),
    ("Obuotabiri", r"obuotabiri", ("Koforidua", "Oriental"), 1958, 2100),
    ("Fankobaah", r"fankobaah", ("Agona Swedru", "Central"), 1958, 2100),
    ("Defence Stars", r"defence stars", ACC, 1958, 2100),
    ("Susu Biribi", r"susu biribi", ("Abuakwa", "Oriental"), 1958, 2100),
    ("Standfast", r"standfast", ACC, 1958, 2100),
    ("Akotex", r"akotex", ("Akosombo", "Oriental"), 1958, 2100),
    ("Gbewaa", r"gbewaa", ("Tamale", "Norte"), 1958, 2100),
    ("Highlanders (Gana)", r"highlanders$", ACC, 1958, 2100),
    ("Northern United", r"northern united", ("Tamale", "Norte"), 1958, 2100),
    ("Eastern Rovers", r"eastern rovers|^obooma$", ("Obooma", "Oriental"), 1958, 2100),
    ("Mighty Eagles", r"mighty eagles", ("Ho", "Volta"), 1958, 2100),
    ("Ho Sunset", r"ho sunset", ("Ho", "Volta"), 1958, 2100),
    ("Tema Hurricanes", r"tema hurricanes", TEM, 1958, 2100),
    ("Akim United", r"akim united", ("Akim Oda", "Oriental"), 1958, 2100),
    ("Great Ashanti", r"great ashanti", KUM, 1958, 2100),
    ("Adansi United", r"adansi united", ("Obuasi", "Ashanti"), 1958, 2100),
    ("Adansiman", r"adansiman", ("Obuasi", "Ashanti"), 1958, 2100),
    ("Bankaman", r"bankaman", ("Banka", "Ashanti"), 1958, 2100),
    ("Abesim Royals", r"abesim royals", ("Abesim", "Bono"), 1958, 2100),
    ("Akwatia CAST", r"akwatia cast", ("Akwatia", "Oriental"), 1958, 2100),
    ("Ashanti Heroes", r"ashanti heroes", KUM, 1958, 2100),
    ("Aston Villa (Gana)", r"aston villa", ACC, 1958, 2100),
    ("Becheman", r"becheman", ("Bechem", "Ahafo"), 1958, 2100),
    ("Evergreens", r"evergreens", ACC, 1958, 2100),
    ("Gold Stars", r"^gold stars$", ("Tarkwa", "Ocidental"), 1958, 2100),
    ("Great Akans", r"(kadjebi )?great akans", ("Kadjebi", "Oti"), 1958, 2100),
    ("Independence", r"(ghana )?independence$", SEK, 1958, 2100),
    ("Islam Stars", r"islam stars", ACC, 1958, 2100),
    ("Kpandu Mulpo", r"kpandu mulpo", ("Kpando", "Volta"), 1958, 2100),
    ("Mighty Stars", r"mighty stars", ACC, 1958, 2100),
    ("Panbros", r"panbros", ACC, 1958, 2100),
    ("Proud United", r"proud united", ACC, 1958, 2100),
    ("Readers", r"^readers$", ACC, 1958, 2100),
    ("Real Manoeuvres", r"real manoeuvres", ("Bolgatanga", "Alto Oriental"), 1958, 2100),
    ("Real Rangers", r"real rangers", ACC, 1958, 2100),
    ("Savannah Stars", r"savannah stars", ("Tamale", "Norte"), 1958, 2100),
    ("Tarkwa United", r"tarkwa united", ("Tarkwa", "Ocidental"), 1958, 2100),
    ("Techiman Wonders", r"techiman wonders", ("Techiman", "Bono Oriental"), 1958, 2100),
    ("Titanics", r"titanics", ACC, 1958, 2100),
    ("Winneba Great Stars", r"winneba great stars", ("Winneba", "Central"), 1958, 2100),
    ("Yamfo Rangers", r"yamfo rangers", ("Yamfo", "Ahafo"), 1958, 2100),
    ("Adonten United", r"adonten united", ("Aburi", "Oriental"), 1958, 2100),
    ("Ahafoman", r"ahafoman", ("Goaso", "Ahafo"), 1958, 2100),
    ("Ahorsu United", r"ahorsu united", ("Akim Oda", "Oriental"), 1958, 2100),
    ("Army", r"^army$", ACC, 1958, 2100),
    ("Denkyira United", r"denkyira united", ("Dunkwa", "Central"), 1958, 2100),
    ("Harbour City", r"harbour city", TEM, 1958, 2100),
    ("Kumasi United", r"kumasi united", KUM, 1958, 2100),
    ("Real Republicans", r"real republicans", ACC, 1958, 2100),
    ("Volta Heroes", r"volta heroes", ("Ho", "Volta"), 1958, 2100),
    ("Wassaman", r"wassaman fc", ("Tarkwa", "Ocidental"), 1958, 1999),
    ("Afienya United", r"afienya( u| united)?$", ("Afienya", "Grande Acra"), 1958, 2100),
]

CLUBES: dict[str, tuple[str, str]] = {nome: lugar for nome, _, lugar, _, _ in _DADOS}
REGRAS: list[tuple[str, str, int, int]] = [(rx, nome, a0, a1) for nome, rx, _, a0, a1 in _DADOS]


def _regra(k: str, ano: int) -> str | None:
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    if not nome:
        return None
    nome = re.sub(r"\s*\((\d+ ag|[^)]*)\)\s*$", lambda m: "" if "ag" in m.group(1) else "", nome)   # "(Kumasi)"
    nome = re.sub(r"[*]+$", "", nome).strip()
    nome = re.sub(r"\s+(FC|SC)$", "", nome)
    nome = re.sub(r"\bU(n)?td\b\.?", "United", nome)   # "BA Untd", "Tamale Utd"
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)
