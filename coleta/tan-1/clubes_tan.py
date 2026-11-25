"""Identidade dos clubes tanzanianos: cada grafia de cada fonte (RSSSF, ogol, Wikipédia) -> um nome de exibição.

- nome pelo qual o clube é conhecido: Young Africans (Yanga), Simba, Azam, Mtibwa Sugar, Coastal Union...;
- nome que já existe em outro país leva primeiro a cidade e, sem cidade que resolva, o país entre parênteses;
- o mesmo clube com outro nome, na mesma cidade, é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Simba = Sunderland (até 1971; "Sunderland changed name to Simba in 1971");
  - Young Africans = Yanga;
  - Tanzania Prisons = Prisons = Mbeya Prisons;
  - Moro United = Kajumulo World Soccer = Sigara (TCC Sigara): a RSSSF registra as duas trocas ("Kajumulo were formerly
    known as Sigara", 1999; "Kajumulo World Soccer were renamed Moro United", 2001);
  - Singida United = Mto (Singida) ("Mto (Singida) apparently changed name to Singida United", 1999);
  - RTC Mwanza = Biashara (1986/87: "RTC Mwanza also listed as Biashara"); o Biashara United de Musoma (2018 em
    diante) é outro clube;
  - JKT Tanzania = JKT Ruvu = JKT Ruvu Stars = Ruvu JKT (o clube do exército de Ruvu, rebatizado em 2018);
  - Arusha FC = AFC; Tabora United = Kitayosce (rebatizado em 2023); Singida Fountain Gate = Singida Big Stars
    (rebatizado em 2023); Pamba = Pamba Jiji; Dodoma Jiji = "Dodoma"; Azam = Azzam United;
  - os clubes do exército com número: KJ977 (Meru Warriors, de Arusha), KJ44 (Karume Rangers);
  - Kahama United = KJ82 Rangers = Kahama Rangers (em 2003 a tabela do grupo só tem o "Kahama 82 Rangers", e os jogos
    chamam o clube de "Kahama U." e de "Kahama Rangers");
- mudança de cidade, compra de vaga ou refundação geram outro clube: o Singida Black Stars (2024/25 em diante) é o
  Ihefu (de Mbarali) depois de comprado e levado para Singida; o Reli de Kigoma (2004) não é o Reli de Morogoro.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

DAR = ("Dar es Salaam", "Dar es Salaam")
TANGA = ("Tanga", "Tanga")
MORO = ("Morogoro", "Morogoro")
MBEYA = ("Mbeya", "Mbeya")
MWANZA = ("Mwanza", "Mwanza")
ARUSHA = ("Arusha", "Arusha")
DODOMA = ("Dodoma", "Dodoma")

# nome de exibição -> regex (sobre a chave do nome), cidade e região, primeiro e último ano
_DADOS: list[tuple[str, str, tuple[str, str], int, int]] = [
    ("Young Africans", r"(young afric\w*|yanga)( sc)?( dar es sal\w*)?$", DAR, 1900, 2100),
    ("Simba", r"sim(b|ab)a( sc| sports)?( dar es sal\w*)?$|(dar )?sunderland$", DAR, 1900, 2100),
    ("Azam", r"azz?am( fc| united)?$", DAR, 1900, 2100),
    ("Mtibwa Sugar", r"mti(bw|wb)a( s(ugar)?)?( fc)?( morogoro| turiani)?$", ("Turiani", "Morogoro"), 1900, 2100),
    ("Coastal Union", r"coastal u(nion)?( fc)?( tanga)?$", TANGA, 1900, 2100),
    ("African Sports", r"african sports( tanga)?$", TANGA, 1900, 2100),
    ("Tanzania Prisons", r"(tanzania |mbeya )?prisons( sc| fc)?( mbeya)?$", MBEYA, 1900, 2100),
    ("Kagera Sugar", r"kagera sugar( fc)?$", ("Bukoba", "Kagera"), 1900, 2100),
    ("Kagera Stars", r"kagera stars( bukoba)?$", ("Bukoba", "Kagera"), 1900, 2100),
    ("Maji Maji", r"ma(ji|ju) ?maji( songea)?$", ("Songea", "Ruvuma"), 1900, 2100),
    ("Pamba", r"pamba( sc| lira| jiji)?( fc)?( mwanza| shinyanga)?$", MWANZA, 1900, 2100),
    ("Moro United", r"moro( u| utd| united)?$|kajumulo( world soccer)?$|(tcc )?sigara$|tcc$", MORO, 1900, 2100),
    ("Singida United", r"singida( u| united)?$|mto( singida)?$", ("Singida", "Singida"), 1900, 2100),
    ("Singida Fountain Gate", r"singida (big stars|bs|fountain gate)$|fountain gate$", ("Singida", "Singida"), 1900, 2100),
    ("Singida Black Stars", r"singida black stars$", ("Singida", "Singida"), 1900, 2100),
    ("Ihefu", r"ihefu( fc| sc)?$", ("Mbarali", "Mbeya"), 1900, 2100),
    ("JKT Tanzania", r"(jkt )?ruvu( jkt| stars)?$|jkt ruvu( stars)?( ruvu s)?$|jkt tanzania( fc)?$", ("Ruvu", "Pwani"),
     1900, 2100),
    ("Ruvu Shooting", r"ruvu shooting( stars| fc)?$", ("Mlandizi", "Pwani"), 1900, 2100),
    ("JKT Mgambo", r"(jkt )?mgambo( jkt)?$", TANGA, 1900, 2100),
    ("JKT Oljoro", r"(jkt )?oljoro$", ARUSHA, 1900, 2100),
    ("Arusha FC", r"(arusha( fc)?|afc)( arusha)?$", ARUSHA, 1900, 2100),
    ("Pan African", r"pan africans?( arusha)?$", DAR, 1900, 2100),
    ("Ashanti United", r"ashanti( u| united| fc)?( sc)?$", DAR, 1900, 2100),
    ("Bandari", r"bandari$", ("Mtwara", "Mtwara"), 1900, 2100),
    ("CDA Dodoma", r"cda( dodoma)?( capital dev authority)?$", DODOMA, 1900, 2100),
    ("Kariakoo", r"kariakoo( fc)?( lindi)?$", ("Lindi", "Lindi"), 1900, 2100),
    ("Lipuli", r"l[iu]puli( fc)?( iringa)?$", ("Iringa", "Iringa"), 1900, 2100),
    ("Milambo", r"milambo( tabora)?$", ("Tabora", "Tabora"), 1900, 2100),
    ("Mji Mpwapwa", r"mji( mp\w+)?$", ("Mpwapwa", "Dodoma"), 1900, 2100),
    ("Mmbanga", r"mmbanga$", ("Kigoma", "Kigoma"), 1900, 2100),
    ("Msimbazi Rovers", r"msimbazi( r| rovers)?$|mismbazi r$", DAR, 1900, 2100),
    ("Nazareth", r"nazareth$", ("Njombe", "Njombe"), 1900, 2100),
    ("Pallsons", r"pallsons$", ARUSHA, 1900, 2100),
    ("Polisi Morogoro", r"pol(ice|isi) moro(goro)?$", MORO, 1900, 2100),
    ("Polisi Morogoro", r"police$", MORO, 2002, 2003),
    ("Polisi Dodoma", r"pol(ice|isi) dodoma$", DODOMA, 1900, 2100),
    ("Polisi Dodoma", r"police$", DODOMA, 2004, 2004),
    ("Polisi Kagera", r"pol(ice|isi) kagera$", ("Bukoba", "Kagera"), 1900, 2100),
    ("Polisi Mara", r"pol(ice|isi) mara$", ("Musoma", "Mara"), 1900, 2100),
    ("Polisi Tanzania", r"polisi tanzania( fc)?$", ("Moshi", "Kilimanjaro"), 1900, 2100),
    ("Reli Morogoro", r"(reli|railways)( railways)?( morogoro)?$", MORO, 1900, 2003),
    ("Reli Kigoma", r"reli( kigoma)?$", ("Kigoma", "Kigoma"), 2004, 2004),
    ("Tukuyu Stars", r"tukuy[au]( stars)?( mbeya)?$", ("Tukuyu", "Mbeya"), 1900, 2100),
    ("Twiga Sports", r"twiga( sports?| stars)?$", DAR, 1900, 2100),
    ("Transit Camp", r"trans(it)? camp( fc)?$", DAR, 1900, 2100),
    ("Vijana", r"vijana$", DAR, 1900, 2100),
    ("Toto Africans", r"toto africa(n|ns)?( mwanza)?$", MWANZA, 1900, 2100),
    ("KJ977 Meru Warriors", r"kj977( meru warriors| arusha)?$|meru w(arriors)?$", ARUSHA, 1900, 2100),
    ("Kahama United", r"(kahama )?kj82 rangers$|kahama( u| united| rangers)?( kagera)?$", ("Kahama", "Shinyanga"),
     1900, 2100),
    ("KJ44 Karume Rangers", r"kj44( karume rangers)?$|karume rangers$", ("Vwawa", "Songwe"), 1900, 2100),
    ("Kiltex", r"kiltex$", ARUSHA, 1900, 2100),
    ("Nyota Nyekundu", r"nyota nyekund[ue]( dar es sal\w*)?$", DAR, 1900, 2100),
    ("Pilsner", r"pilsner( dar es salaam)?$", DAR, 1900, 2100),
    ("RTC Kigoma", r"rtc( kigoma)?$", ("Kigoma", "Kigoma"), 1900, 2100),
    ("RTC Mwanza", r"rtc mwanza$|biashara( mwanza)?$", MWANZA, 1900, 2000),
    ("RTC Kagera", r"rtc kagera( bukoba)?$", ("Bukoba", "Kagera"), 1900, 2100),
    ("Mwadui", r"mwadui( fc)?( shinyanga)?$", ("Mwadui", "Shinyanga"), 1900, 2100),
    ("Ndovu", r"ndovu( arusha)?$", ARUSHA, 1900, 2100),
    ("Ushirika", r"ushirika( moshi)?$", ("Moshi", "Kilimanjaro"), 1900, 2100),
    ("MECCO", r"mecco( mbeya)?$", MBEYA, 1900, 2100),
    ("Kurugenzi", r"kurugenzi( dodoma)?$", DODOMA, 1900, 2100),
    ("Cosmopolitans", r"cosmopolitans$", DAR, 1900, 2100),
    ("Mseto Sports", r"mseto( sports)?$", MORO, 1900, 2100),
    ("Biashara United", r"biashara united( fc)?$|biashara$", ("Musoma", "Mara"), 2001, 2100),
    ("Alliance", r"alliance( schools| fc)?$", MWANZA, 1900, 2100),
    ("African Lyon", r"african lyon( fc)?$", DAR, 1900, 2100),
    ("Villa Squad", r"villa squad$", DAR, 1900, 2100),
    ("Manyema Rangers", r"manyema rangers( fc)?$", DAR, 1900, 2100),
    ("Rhino Rangers", r"rhino rangers$", ("Tabora", "Tabora"), 1900, 2100),
    ("Mbeya City", r"mbeya city( fc)?$", MBEYA, 1900, 2100),
    ("Mbeya Kwanza", r"mbeya kwanza( fc)?$", MBEYA, 1900, 2100),
    ("Ndanda", r"ndanda( fc)?$", ("Mtwara", "Mtwara"), 1900, 2100),
    ("Stand United", r"stand united$", ("Shinyanga", "Shinyanga"), 1900, 2100),
    ("Mbao", r"mbao( fc)?$", MWANZA, 1900, 2100),
    ("Njombe Mji", r"njombe mji$", ("Njombe", "Njombe"), 1900, 2100),
    ("KMC", r"kmc( fc)?$", DAR, 1900, 2100),
    ("Namungo", r"namungo( fc)?$", ("Ruangwa", "Lindi"), 1900, 2100),
    ("Dodoma Jiji", r"dodoma( jiji)?( fc)?$", DODOMA, 2019, 2100),
    ("Gwambina", r"gwambina( fc)?$", ("Misungwi", "Mwanza"), 1900, 2100),
    ("Geita Gold", r"geita gold( fc| sc)?$", ("Geita", "Geita"), 1900, 2100),
    ("KenGold", r"ken ?gold( fc)?$", ("Chunya", "Mbeya"), 1900, 2100),
    ("Mashujaa", r"mashujaa( fc)?$", ("Kigoma", "Kigoma"), 1900, 2100),
    ("Tabora United", r"tabora united( fc)?$|kitayosce( fc)?$", ("Tabora", "Tabora"), 1900, 2100),
    ("TRA United", r"tra united( sc)?$", ("Tabora", "Tabora"), 1900, 2100),
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
    nome = re.sub(r"\s*\([^)]*\)\s*$", "", nome)   # "(Dar-es-Salaam)", "(Kagera?)"
    nome = re.sub(r"[*]+$", "", nome).strip()
    nome = re.sub(r"\s+(FC|SC)$", "", nome)
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)
