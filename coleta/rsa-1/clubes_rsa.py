"""Identidade dos clubes sul-africanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Kaizer Chiefs", "Orlando Pirates", "Mamelodi Sundowns");
- nome que já existe em outro país leva o país ("Santos (África do Sul)", "Rangers (África do Sul)", "Dynamos (África do
  Sul)", "Leeds United (África do Sul)", "Vasco da Gama (África do Sul)"); clube refundado com o nome de um antigo, o ano
  de fundação do antigo ("Durban City (1959)", "Cape Town City (1962)", "Highlands Park (1959)");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - AmaZulu = Zulu Royals; Bloemfontein Celtic = Frasers Celtic; SuperSport United = Pretoria City (comprado e renomeado
    em 1994); Jomo Cosmos = Dion Cosmos; Free State Stars = Qwa Qwa Stars; Platinum Stars = Silver Stars; Mpumalanga Black
    Aces = Witbank (Black) Aces; Wits University = Bidvest Wits; Tembisa Classic = Thembisa Classic;
  - Cape Town Spurs = Ajax Cape Town (fusão do Cape Town Spurs com o Seven Stars em 1999; voltou ao nome Cape Town Spurs
    em 2020);
  - 1993 (notas da página): Score Stars = Qwa Qwa Stars (Free State Stars); Ratanang (Mahlosians) = "Rangers" =
    Chatsworth Rangers; Albany City = Pretoria City (SuperSport United); Welkom Eagles = Highlands Park (1959), que mudou de
    dono e foi para Welkom no meio da temporada;
  - Thanda Royal Zulu = Benoni Premier United (mudou de nome no meio de 2007/08); "Rangers" nos jogos de 1996/97 em
    diante é o Manning Rangers (o Rangers de Joanesburgo, campeão de 1986, só até 1995);
  - Bush Bucks: o "Bush Bucks" de Durban (campeão de 1985) até 1987 é o Durban Bush Bucks; de 1988 em diante, o Bush Bucks
    de Umtata ("Umtata Bucks").
- clubes que compraram a vaga de outro (Marumo Gallants, Royal AM, TS Galaxy, Cape Town City de 2016, Siwelele) são clubes
  próprios, com o nome deles.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

GAU = "Gauteng"
KZN = "KwaZulu-Natal"
WC = "Cabo Ocidental"
EC = "Cabo Oriental"
FS = "Estado Livre"
JNB = ("Joanesburgo", GAU)
SOW = ("Soweto", GAU)
PTA = ("Pretória", GAU)
DBN = ("Durban", KZN)
CPT = ("Cidade do Cabo", WC)

# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "Kaizer Chiefs": JNB, "Orlando Pirates": SOW, "Moroka Swallows": SOW, "Wits University": JNB,
    "Jomo Cosmos": JNB, "Highlands Park (1959)": JNB, "Highlands Park": JNB, "Rangers (África do Sul)": JNB,
    "Dynamos (África do Sul)": JNB, "African Wanderers": DBN, "Pimville United Brothers": SOW,
    "Pilkington United Brothers": JNB, "Moroka Lions": SOW, "Real Katlehong City": ("Katlehong", GAU),
    "Vaal Professionals": ("Vereeniging", GAU), "Benoni United": ("Benoni", GAU),
    "Tembisa Classic": ("Tembisa", GAU), "Winners Park": ("Pretória", GAU), 
    "Mamelodi Sundowns": PTA, "SuperSport United": PTA, "Arcadia Shepherds": PTA, "Pretoria Callies": PTA,
    "Mamelodi United": PTA, "Mamelodi XI": PTA, "University of Pretoria": PTA, "Siwelele": PTA,
    "AmaZulu": DBN, "Golden Arrows": DBN, "Manning Rangers": DBN, "Durban City (1959)": DBN, "Durban City": DBN,
    "Durban Bush Bucks": DBN, "Thanda Royal Zulu": ("Richards Bay", KZN), "Richards Bay": ("Richards Bay", KZN),
    "Maritzburg United": ("Pietermaritzburg", KZN), "Maritzburg": ("Pietermaritzburg", KZN),
    "Royal AM": ("Pietermaritzburg", KZN), "Crusaders United": ("Stanger", KZN), "Chatsworth Rangers": DBN,
    "Umlazi Citizens": ("Umlazi", KZN), "Sobantu Manchester United": ("Pietermaritzburg", KZN), "Natal United": DBN,
    "Real Taj": DBN, "Lamontville Golden Arrows": DBN,
    "Cape Town Spurs": CPT, "Santos (África do Sul)": CPT, "Hellenic": CPT, "Cape Town City (1962)": CPT,
    "Cape Town City": CPT, "Seven Stars": CPT, "Vasco da Gama (África do Sul)": CPT, "Mother City": CPT,
    "Stellenbosch": ("Stellenbosch", WC), "Bosmont Chelsea": JNB,
    "Bloemfontein Celtic": ("Bloemfontein", FS), "Free State Stars": ("Bethlehem", FS), "Welkom Real Hearts": ("Welkom", FS),
    "Welkom Hungry Lions": ("Welkom", FS), "Mangaung United": ("Bloemfontein", FS),
    "Fairway Stars": ("Witsieshoek", FS), "Royal Tigers": ("Bloemfontein", FS),
    "Bush Bucks": ("Mthatha", EC), "Chippa United": ("Gqeberha", EC), "Bay United": ("Gqeberha", EC),
    "Giant Blackpool": ("Gqeberha", EC), "Michau Warriors": ("Gqeberha", EC), "Albany City": ("Makhanda", EC),
    "Albany Celtic": ("Makhanda", EC),
    "Mpumalanga Black Aces": ("Witbank", "Mpumalanga"), "TS Galaxy": ("KaNyamazane", "Mpumalanga"),
    "Dangerous Darkies": ("Nelspruit", "Mpumalanga"), "Ria Stars": ("Rustenburg", "Noroeste"),
    "Black Leopards": ("Thohoyandou", "Limpopo"), "Baroka": ("Ga-Mphahlele", "Limpopo"),
    "Polokwane City": ("Polokwane", "Limpopo"), "Sekhukhune United": ("Sekhukhune", "Limpopo"),
    "Marumo Gallants": ("Polokwane", "Limpopo"), "Magesi": ("Polokwane", "Limpopo"),
    "Tshakhuma Tsha Madzivhandila": ("Tshakhuma", "Limpopo"), "Platinum Stars": ("Rustenburg", "Noroeste"),
    "Vaal Reef Stars": ("Orkney", "Noroeste"), "Klerksdorp City": ("Klerksdorp", "Noroeste"),
    "D'Alberton Callies": ("Alberton", GAU), "Real Rovers": JNB, "Lusitano": JNB,
    "Imperial Callies": PTA, "Kimberley Dalton Brothers": ("Kimberley", "Cabo Setentrional"),
    "Leeds United (África do Sul)": ("Rustenburg", "Noroeste"), "Leicester City (África do Sul)": ("Durban", KZN),
    "Colchester United (África do Sul)": ("Durban", KZN), "Ireland United": JNB, "Orbit College": ("Rustenburg", "Noroeste"),
    "FC AK": JNB, "Stilfontein Big XI": ("Stilfontein", "Noroeste"), "Western Tigers": CPT,
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(mamelodi )?sundowns", "Mamelodi Sundowns", 1971, 2100),
    (r"(kaizer )?chiefs", "Kaizer Chiefs", 1971, 2100),
    (r"(orlando )?pira?ates|orlando piarates", "Orlando Pirates", 1971, 2100),
    (r"(moroka )?swallows( big xv| ltd)?|swallows fc", "Moroka Swallows", 1971, 2100),
    (r"ama ?zulu|zulu royals( amazulu)?", "AmaZulu", 1971, 2100),
    (r"(lamontville )?golden arr(ows)?", "Golden Arrows", 1971, 2100),
    (r"bloemfontein celtic|frasers celtic|^celtic$", "Bloemfontein Celtic", 1971, 2100),
    (r"(bidvest )?wits( univers\w*)?$|wits university", "Wits University", 1971, 2100),
    (r"super ?sport( united| utd)?|pretoria city", "SuperSport United", 1971, 2100),
    (r"(jomo|dion) co\w*mos|jomo comos|^cosmos$", "Jomo Cosmos", 1971, 2100),
    (r"cape towns? spurs|^ajax( cape town)?$|^spurs$", "Cape Town Spurs", 1971, 2100),
    (r"cape town city", "Cape Town City (1962)", 1971, 2000),
    (r"cape town city", "Cape Town City", 2001, 2100),
    (r"durban city", "Durban City (1959)", 1971, 2000),
    (r"durban city", "Durban City", 2001, 2100),
    (r"highlands park", "Highlands Park (1959)", 1971, 2000),
    (r"highlands park", "Highlands Park", 2001, 2100),
    (r"(lightbodys |cape town )?santos", "Santos (África do Sul)", 1971, 2100),
    (r"^rangers( jo ?burg)?$", "Rangers (África do Sul)", 1971, 1995),
    (r"^rangers$", "Manning Rangers", 1996, 2100),
    (r"manning rangers", "Manning Rangers", 1971, 2100),
    (r"chatsworth rangers", "Chatsworth Rangers", 1971, 2100),
    (r"(durban )?bush bucks", "Durban Bush Bucks", 1971, 1987),
    (r"(umtata )?bu[sc]h bucks|umtata bucks|^bucks$", "Bush Bucks", 1988, 2100),
    (r"(witbank|wtbank|ukhamba|mpumalanga|total)( black)? aces", "Mpumalanga Black Aces", 1971, 2100),
    (r"free (st(ate)?|stars)( st(ars)?)?$|qwa ?qwa stars", "Free State Stars", 1971, 2100),
    (r"platinum stars|silver stars", "Platinum Stars", 1971, 2100),
    (r"t?h?embisa classic|^classic$", "Tembisa Classic", 1971, 2100),
    (r"vaal pro(fessional)?s|vaal profs", "Vaal Professionals", 1971, 2100),
    (r"vaal reefs? stars", "Vaal Reef Stars", 1971, 2100),
    (r"^(pretoria )?(bantu )?callies$", "Pretoria Callies", 1971, 2100),
    (r"arcadia( shepherds)?$", "Arcadia Shepherds", 1971, 2100),
    (r"(cape town )?hellenic", "Hellenic", 1971, 2100),
    (r"(halls |stallions )?dynamos", "Dynamos (África do Sul)", 1971, 2100),
    (r"leeds united", "Leeds United (África do Sul)", 1971, 2100),
    (r"leicester city", "Leicester City (África do Sul)", 1971, 2100),
    (r"colchester united", "Colchester United (África do Sul)", 1971, 2100),
    (r"(giant|pe) blackpool", "Giant Blackpool", 1971, 2100),
    (r"(african )?wanderers", "African Wanderers", 1971, 2100),
    (r"benoni premier united", "Thanda Royal Zulu", 1971, 2100),
    (r"benoni( united)?$|kwikot benoni", "Benoni United", 1971, 2100),
    (r"welkom real hearts", "Welkom Real Hearts", 1971, 2100),
    (r"welkom eagles", "Highlands Park (1959)", 1971, 2100),
    (r"welkom hungry lions", "Welkom Hungry Lions", 1971, 2100),
    (r"crusade?r?s( united)?", "Crusaders United", 1971, 2100),
    (r"fairways? stars", "Fairway Stars", 1971, 2100),
    (r"dangerous darkies", "Dangerous Darkies", 1971, 2100),
    (r"dalberton callies", "D'Alberton Callies", 1971, 2100),
    (r"score stars", "Free State Stars", 1971, 2100),
    (r"ratanang( mahlosians)?", "Chatsworth Rangers", 1971, 2100),
    (r"royal tigers", "Royal Tigers", 1971, 2100),
    (r"real rovers", "Real Rovers", 1971, 2100),
    (r"natal united", "Natal United", 1971, 2100),
    (r"klerksdorp city", "Klerksdorp City", 1971, 2100),
    (r"mangaung united", "Mangaung United", 1971, 2100),
    (r"real katlehong city", "Real Katlehong City", 1971, 2100),
    (r"kimberl[e]?y dalton bros", "Kimberley Dalton Brothers", 1971, 2100),
    (r"mamelodi united", "Mamelodi United", 1971, 2100),
    (r"mamelodi xi", "Mamelodi XI", 1971, 2100),
    (r"pimville united bros|^pubs$", "Pimville United Brothers", 1971, 2100),
    (r"pilkington united bros", "Pilkington United Brothers", 1971, 2100),
    (r"lusitano( club)?", "Lusitano", 1971, 2100),
    (r"moroka lions", "Moroka Lions", 1971, 2100),
    (r"imperial callies", "Imperial Callies", 1971, 2100),
    (r"sobantu manchester utd", "Sobantu Manchester United", 1971, 2100),
    (r"umlazi citizens( ltd)?", "Umlazi Citizens", 1971, 2100),
    (r"albany (city|celtic)", "SuperSport United", 1971, 2100),
    (r"real taj", "Real Taj", 1971, 2100),
    (r"bosmont chelsea", "Bosmont Chelsea", 1971, 2100),
    (r"ireland united", "Ireland United", 1971, 2100),
    (r"^maritzburg$", "Maritzburg", 1971, 2000),
    (r"maritzburg united", "Maritzburg United", 1971, 2100),
    (r"black leopards", "Black Leopards", 1971, 2100),
    (r"baroka( fc)?", "Baroka", 1971, 2100),
    (r"bay united", "Bay United", 1971, 2100),
    (r"chippa (united|utd)", "Chippa United", 1971, 2100),
    (r"fc ak", "FC AK", 1971, 2100),
    (r"marumo gallants", "Marumo Gallants", 1971, 2100),
    (r"tshakhuma\w*|^ttm$", "Tshakhuma Tsha Madzivhandila", 1971, 2100),
    (r"polokwane city", "Polokwane City", 1971, 2100),
    (r"royal am", "Royal AM", 1971, 2100),
    (r"sekhukhune united", "Sekhukhune United", 1971, 2100),
    (r"stellenbosch( fc)?", "Stellenbosch", 1971, 2100),
    (r"ts galaxy( fc)?", "TS Galaxy", 1971, 2100),
    (r"richards? bay( fc)?", "Richards Bay", 1971, 2100),
    (r"magesi( fc)?", "Magesi", 1971, 2100),
    (r"orbit college( fc)?", "Orbit College", 1971, 2100),
    (r"siwelele( fc)?", "Siwelele", 1971, 2100),
    (r"thanda roya?l zulu", "Thanda Royal Zulu", 1971, 2100),
    (r"university of pretoria|pretoria university", "University of Pretoria", 1971, 2100),
    (r"vasco da gama", "Vasco da Gama (África do Sul)", 1971, 2100),
    (r"winners park", "Winners Park", 1971, 2100),
    (r"ria stars", "Ria Stars", 1971, 2100),
    (r"mother city", "Mother City", 1971, 2100),
    (r"(michau )?warriors", "Michau Warriors", 1971, 2100),
    (r"seven stars", "Seven Stars", 1971, 2100),
    (r"stilfontein big xi", "Stilfontein Big XI", 1971, 2100),
    (r"western tigers", "Western Tigers", 1971, 2100),
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
    nome = re.sub(r"\s*\((\d+ ag|[^)]*)\)\s*$", lambda m: "" if "ag" in m.group(1) else "", nome)   # "(Johannesburg)"
    nome = re.sub(r"\s+b\)\s*$", "", nome)
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
