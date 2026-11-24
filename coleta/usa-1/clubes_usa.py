"""Identidade dos clubes da 1ª divisão dos EUA (ASL I, 1967, NASL, MLS): cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- o mesmo clube com outro nome (renomeação na mesma cidade, como a RSSSF e a MLS contam): NY/NJ MetroStars = New York Red
  Bulls; Kansas City Wiz/Wizards = Sporting Kansas City; Dallas Burn = FC Dallas; San Jose Clash = San Jose Earthquakes (a
  MLS conta o Earthquakes de 2008 como continuação do de 1996-2005); Montreal Impact = CF Montréal; Houston Dynamos = Houston
  Dynamo; Atlanta Apollos (1973) = Atlanta Chiefs; Miami Gatos = Miami Toros; Toronto Metros = Toronto Metros-Croatia;
  Golden Bay Earthquakes (1983-1984) = San Jose Earthquakes da NASL; Boston Bears = Boston Wonder Workers; Providence
  Clamdiggers = Providence Gold Bugs; J & P Coats = Pawtucket Rangers (nome de exibição "J&P Coats"); Fall River United (1921/22)
  = Fall River Marksmen; Philadelphia Field Club de 1921/22 = Bethlehem Steel (a RSSSF: "Philadelphia changed their name to
  Bethlehem Steel"; o Philadelphia Field Club de 1922 em diante é outro clube);
- New York Giants da ASL: o de 1923-1929 virou New York Soccer Club em 1930; o New York Nationals (1927-1929) passou a se chamar
  New York Giants em 1930-1932 (RSSSF). Cada um com o último nome: "New York Soccer Club" e "New York Giants" (o campeão de 1931);
- clubes diferentes: o que mudou de cidade (Los Angeles Toros -> San Diego Toros, Denver Dynamos -> Minnesota Kicks, Miami Toros
  -> Fort Lauderdale Strikers -> Minnesota Strikers, Hartford Bicentennials -> Oakland Stompers -> Edmonton Drillers, Toronto
  Metros-Croatia -> Toronto Blizzard...); os da NASL e os da MLS com o mesmo nome (Seattle Sounders, Portland Timbers, Vancouver
  Whitecaps, San Jose Earthquakes: os da NASL levam "(NASL)"; o Vancouver Whitecaps da MLS conta 1974 como fundação, mas a
  franquia da NASL acabou em 1984); Atlanta Chiefs de 1967-1973 e o de 1979-1981 (ex-Colorado Caribous);
- os times de 1967 da United Soccer Association eram clubes europeus e sul-americanos com nome de cidade americana (Wolves =
  Wolverhampton, Stokers = Stoke City...): entram com o nome da cidade, como na tabela;
- país: os clubes do Canadá (Toronto, Vancouver, Montreal, Edmonton, Calgary) com `CAN`.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

# nome de exibição -> (cidade, estado ou província, país)
_U = lambda c, e: (c, e, "USA")   # noqa: E731
_C = lambda c, e: (c, e, "CAN")   # noqa: E731
CLUBES: dict[str, tuple[str, str, str]] = {
    # ASL I
    "Bethlehem Steel": _U("Bethlehem", "Pensilvânia"), "New York Field Club": _U("Nova York", "Nova York"),
    "Todd Shipyards": _U("Brooklyn", "Nova York"), "Harrison Field Club": _U("Harrison", "Nova Jersey"),
    "J&P Coats": _U("Pawtucket", "Rhode Island"), "Fall River Marksmen": _U("Fall River", "Massachusetts"),
    "Holyoke Falcos": _U("Holyoke", "Massachusetts"), "Jersey City Celtics": _U("Jersey City", "Nova Jersey"),
    "Philadelphia Field Club": _U("Filadélfia", "Pensilvânia"), "Paterson Silk Sox": _U("Paterson", "Nova Jersey"),
    "Brooklyn Wanderers": _U("Brooklyn", "Nova York"), "New York Soccer Club": _U("Nova York", "Nova York"),
    "Newark Skeeters": _U("Newark", "Nova Jersey"), "Boston Wonder Workers": _U("Boston", "Massachusetts"),
    "New Bedford Whalers": _U("New Bedford", "Massachusetts"), "Providence Gold Bugs": _U("Providence", "Rhode Island"),
    "Indiana Flooring": _U("Nova York", "Nova York"), "Fleisher Yarn": _U("Filadélfia", "Pensilvânia"),
    "Shawsheen Indians": _U("Andover", "Massachusetts"), "Springfield Babes": _U("Springfield", "Massachusetts"),
    "New York Giants": _U("Nova York", "Nova York"), "Hartford Americans": _U("Hartford", "Connecticut"),
    "Philadelphia Celtic": _U("Filadélfia", "Pensilvânia"), "Jersey City": _U("Jersey City", "Nova Jersey"),
    "Brooklyn Hakoah": _U("Brooklyn", "Nova York"), "Hakoah All-Stars": _U("Nova York", "Nova York"),
    "Newark Americans": _U("Newark", "Nova Jersey"), "New York Yankees": _U("Nova York", "Nova York"),
    "Fall River FC": _U("Fall River", "Massachusetts"), "New York Americans": _U("Nova York", "Nova York"),
    "Queens Bohemians": _U("Nova York", "Nova York"), "Brookhattan": _U("Nova York", "Nova York"),
    "Prague Americans": _U("Nova York", "Nova York"),
    # 1967 e NASL
    "Washington Whips": _U("Washington", "Distrito de Colúmbia"), "Cleveland Stokers": _U("Cleveland", "Ohio"),
    "Toronto City": _C("Toronto", "Ontário"), "Detroit Cougars": _U("Detroit", "Michigan"),
    "New York Skyliners": _U("Nova York", "Nova York"), "Boston Rovers": _U("Boston", "Massachusetts"),
    "Los Angeles Wolves": _U("Los Angeles", "Califórnia"), "San Francisco Gales": _U("San Francisco", "Califórnia"),
    "Chicago Mustangs": _U("Chicago", "Illinois"), "Houston Stars": _U("Houston", "Texas"),
    "Vancouver Royals": _C("Vancouver", "Colúmbia Britânica"), "Dallas Tornado": _U("Dallas", "Texas"),
    "Baltimore Bays": _U("Baltimore", "Maryland"), "Philadelphia Spartans": _U("Filadélfia", "Pensilvânia"),
    "New York Generals": _U("Nova York", "Nova York"), "Atlanta Chiefs": _U("Atlanta", "Geórgia"),
    "Pittsburgh Phantoms": _U("Pittsburgh", "Pensilvânia"), "Oakland Clippers": _U("Oakland", "Califórnia"),
    "St. Louis Stars": _U("St. Louis", "Missouri"), "Chicago Spurs": _U("Chicago", "Illinois"),
    "Toronto Falcons": _C("Toronto", "Ontário"), "Los Angeles Toros": _U("Los Angeles", "Califórnia"),
    "Boston Beacons": _U("Boston", "Massachusetts"), "Kansas City Spurs": _U("Kansas City", "Missouri"),
    "San Diego Toros": _U("San Diego", "Califórnia"), "Rochester Lancers": _U("Rochester", "Nova York"),
    "Washington Darts": _U("Washington", "Distrito de Colúmbia"), "Montreal Olympique": _C("Montreal", "Quebec"),
    "Toronto Metros-Croatia": _C("Toronto", "Ontário"), "New York Cosmos": _U("Nova York", "Nova York"),
    "Miami Toros": _U("Miami", "Flórida"), "Philadelphia Atoms": _U("Filadélfia", "Pensilvânia"),
    "Los Angeles Aztecs": _U("Los Angeles", "Califórnia"), "Baltimore Comets": _U("Baltimore", "Maryland"),
    "Boston Minutemen": _U("Boston", "Massachusetts"), "Denver Dynamos": _U("Denver", "Colorado"),
    "Seattle Sounders (NASL)": _U("Seattle", "Washington"), "Vancouver Whitecaps (NASL)": _C("Vancouver", "Colúmbia Britânica"),
    "San Jose Earthquakes (NASL)": _U("San Jose", "Califórnia"), "Washington Diplomats": _U("Washington", "Distrito de Colúmbia"),
    "Hartford Bicentennials": _U("Hartford", "Connecticut"), "Chicago Sting": _U("Chicago", "Illinois"),
    "Tampa Bay Rowdies": _U("Tampa", "Flórida"), "Portland Timbers (NASL)": _U("Portland", "Oregon"),
    "San Antonio Thunder": _U("San Antonio", "Texas"), "Minnesota Kicks": _U("Minneapolis", "Minnesota"),
    "San Diego Jaws": _U("San Diego", "Califórnia"), "Fort Lauderdale Strikers": _U("Fort Lauderdale", "Flórida"),
    "Team Hawaii": _U("Honolulu", "Havaí"), "Las Vegas Quicksilver": _U("Las Vegas", "Nevada"),
    "Connecticut Bicentennials": _U("New Haven", "Connecticut"), "New England Tea Men": _U("Foxborough", "Massachusetts"),
    "Philadelphia Fury": _U("Filadélfia", "Pensilvânia"), "Detroit Express": _U("Detroit", "Michigan"),
    "Memphis Rogues": _U("Memphis", "Tennessee"), "Houston Hurricane": _U("Houston", "Texas"),
    "Colorado Caribous": _U("Denver", "Colorado"), "Oakland Stompers": _U("Oakland", "Califórnia"),
    "San Diego Sockers": _U("San Diego", "Califórnia"), "Tulsa Roughnecks": _U("Tulsa", "Oklahoma"),
    "California Surf": _U("Anaheim", "Califórnia"), "Toronto Blizzard": _C("Toronto", "Ontário"),
    "Edmonton Drillers": _C("Edmonton", "Alberta"), "Atlanta Chiefs (1979)": _U("Atlanta", "Geórgia"),
    "Calgary Boomers": _C("Calgary", "Alberta"), "Jacksonville Tea Men": _U("Jacksonville", "Flórida"),
    "Montreal Manic": _C("Montreal", "Quebec"), "Team America": _U("Washington", "Distrito de Colúmbia"),
    "Minnesota Strikers": _U("Minneapolis", "Minnesota"),
    # MLS
    "DC United": _U("Washington", "Distrito de Colúmbia"), "Los Angeles Galaxy": _U("Carson", "Califórnia"),
    "New York Red Bulls": _U("Harrison", "Nova Jersey"), "New England Revolution": _U("Foxborough", "Massachusetts"),
    "Columbus Crew": _U("Columbus", "Ohio"), "Tampa Bay Mutiny": _U("Tampa", "Flórida"),
    "FC Dallas": _U("Frisco", "Texas"), "Sporting Kansas City": _U("Kansas City", "Kansas"),
    "San Jose Earthquakes": _U("San Jose", "Califórnia"), "Colorado Rapids": _U("Commerce City", "Colorado"),
    "Chicago Fire": _U("Chicago", "Illinois"), "Miami Fusion": _U("Fort Lauderdale", "Flórida"),
    "Real Salt Lake": _U("Sandy", "Utah"), "Chivas USA": _U("Carson", "Califórnia"), "Houston Dynamo": _U("Houston", "Texas"),
    "Toronto FC": _C("Toronto", "Ontário"), "Seattle Sounders": _U("Seattle", "Washington"),
    "Philadelphia Union": _U("Chester", "Pensilvânia"), "Portland Timbers": _U("Portland", "Oregon"),
    "Vancouver Whitecaps": _C("Vancouver", "Colúmbia Britânica"), "CF Montréal": _C("Montreal", "Quebec"),
    "Orlando City": _U("Orlando", "Flórida"), "New York City FC": _U("Nova York", "Nova York"),
    "Atlanta United": _U("Atlanta", "Geórgia"), "Minnesota United": _U("Saint Paul", "Minnesota"),
    "Los Angeles FC": _U("Los Angeles", "Califórnia"), "FC Cincinnati": _U("Cincinnati", "Ohio"),
    "Nashville SC": _U("Nashville", "Tennessee"), "Inter Miami": _U("Fort Lauderdale", "Flórida"),
    "Austin FC": _U("Austin", "Texas"), "Charlotte FC": _U("Charlotte", "Carolina do Norte"),
    "St. Louis City SC": _U("St. Louis", "Missouri"), "San Diego FC": _U("San Diego", "Califórnia"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    # ASL I
    (r"(philadelphia (field|football) club|philadelphia)", "Bethlehem Steel", 1921, 1921),
    (r"bethlehem( steel)?", "Bethlehem Steel", 1921, 1935),
    (r"new york field club|ny field club", "New York Field Club", 1921, 1935),
    (r"todd shipyards( bkln)?", "Todd Shipyards", 1921, 1922),
    (r"harrison (soccer|field) club|harrison", "Harrison Field Club", 1921, 1923),
    (r"j ?(and )?p coats( pawtucket)?|j p coates|pawtucket( rangers)?", "J&P Coats", 1921, 1935),
    (r"fall river (united|marksmen)|fall river", "Fall River Marksmen", 1921, 1930),
    (r"fall river (football club|fc)|fall river", "Fall River FC", 1931, 1935),
    (r"holyoke falcos", "Holyoke Falcos", 1921, 1922),
    (r"jersey city celtics", "Jersey City Celtics", 1921, 1922),
    (r"philadelphia (field|football) club", "Philadelphia Field Club", 1922, 1935),
    (r"paterson( silk sox)?", "Paterson Silk Sox", 1921, 1925),
    (r"brooklyn wanderers|brooklyn", "Brooklyn Wanderers", 1921, 1935),
    (r"new york (giants|soccer club)|new york", "New York Soccer Club", 1923, 1929),
    (r"new york soccer club", "New York Soccer Club", 1930, 1930),
    (r"new york (nationals|giants)", "New York Giants", 1927, 1935),
    (r"newark skeeters", "Newark Skeeters", 1922, 1929),
    (r"newark( americans)?", "Newark Americans", 1929, 1935),
    (r"boston ?(wonder ?workers| bears)?", "Boston Wonder Workers", 1924, 1935),
    (r"new bedford( whalers)?", "New Bedford Whalers", 1924, 1935),
    (r"provi?dence( clamdiggers| gold bugs)?", "Providence Gold Bugs", 1924, 1935),
    (r"indiana flooring( n y)?", "Indiana Flooring", 1924, 1927),
    (r"fleisher( yarn)?( phil)?", "Fleisher Yarn", 1924, 1926),
    (r"shawsheen( ma)? ?indians", "Shawsheen Indians", 1925, 1926),
    (r"springfield babes", "Springfield Babes", 1926, 1927),
    (r"hartford( americans)?", "Hartford Americans", 1927, 1928),
    (r"philadelphia celtic", "Philadelphia Celtic", 1927, 1928),
    (r"jersey city", "Jersey City", 1928, 1929),
    (r"brooklyn hakoah", "Brooklyn Hakoah", 1929, 1929),
    (r"hakoah all ?stars", "Hakoah All-Stars", 1929, 1935),
    (r"new york yankees", "New York Yankees", 1931, 1931),
    (r"new york americans", "New York Americans", 1931, 1935),
    (r"(queens bohemians|bohemian queens)", "Queens Bohemians", 1932, 1935),
    (r"brookhattan", "Brookhattan", 1932, 1935),
    (r"prague( americans)?", "Prague Americans", 1932, 1935),
    # 1967 e NASL (o nome curto da cidade, nas finais, resolve pelo ano)
    (r"washington( whips)?", "Washington Whips", 1967, 1968),
    (r"cleveland( stokers)?", "Cleveland Stokers", 1967, 1968),
    (r"toronto city", "Toronto City", 1967, 1967),
    (r"detroit( cougars)?", "Detroit Cougars", 1967, 1968),
    (r"new york skyliners", "New York Skyliners", 1967, 1967),
    (r"boston rovers", "Boston Rovers", 1967, 1967),
    (r"los angeles wolves", "Los Angeles Wolves", 1967, 1968),
    (r"los angeles toros", "Los Angeles Toros", 1967, 1967),
    (r"los angeles", "Los Angeles Wolves", 1967, 1967),
    (r"san francisco( gales)?", "San Francisco Gales", 1967, 1967),
    (r"chicago mustangs", "Chicago Mustangs", 1967, 1968),
    (r"chicago spurs", "Chicago Spurs", 1967, 1967),
    (r"houston( stars)?", "Houston Stars", 1967, 1968),
    (r"vancouver royal canadians|vancouver( royals)?", "Vancouver Royals", 1967, 1968),
    (r"dallas( tornado)?", "Dallas Tornado", 1967, 1981),
    (r"baltimore( bays)?", "Baltimore Bays", 1967, 1969),
    (r"philadelphia( spartans)?", "Philadelphia Spartans", 1967, 1967),
    (r"new york generals", "New York Generals", 1967, 1968),
    (r"atlanta( chiefs| apollos)?", "Atlanta Chiefs", 1967, 1973),
    (r"pittsburgh( phantoms)?", "Pittsburgh Phantoms", 1967, 1967),
    (r"oakland( clippers)?", "Oakland Clippers", 1967, 1968),
    (r"st ?louis( stars)?", "St. Louis Stars", 1967, 1977),
    (r"toronto( falcons)?", "Toronto Falcons", 1967, 1968),
    (r"boston( beacons)?", "Boston Beacons", 1968, 1968),
    (r"kansas city( spurs)?", "Kansas City Spurs", 1968, 1970),
    (r"san diego( toros)?", "San Diego Toros", 1968, 1968),
    (r"rochester( lancers)?", "Rochester Lancers", 1970, 1980),
    (r"washington( darts)?", "Washington Darts", 1970, 1971),
    (r"montreal( olympique)?", "Montreal Olympique", 1971, 1973),
    (r"toronto( metros( croatia)?)?", "Toronto Metros-Croatia", 1971, 1978),
    (r"(new york )?cosmos|new york", "New York Cosmos", 1971, 1984),
    (r"miami( gatos| toros)?", "Miami Toros", 1972, 1976),
    (r"philadelphia( atoms)?", "Philadelphia Atoms", 1973, 1976),
    (r"los angeles( aztecs)?", "Los Angeles Aztecs", 1974, 1981),
    (r"baltimore( comets)?", "Baltimore Comets", 1974, 1975),
    (r"boston( minutemen)?", "Boston Minutemen", 1974, 1976),
    (r"denver( dynamos)?", "Denver Dynamos", 1974, 1975),
    (r"seattle( sounders)?", "Seattle Sounders (NASL)", 1974, 1983),
    (r"vancouver( whitecaps)?", "Vancouver Whitecaps (NASL)", 1974, 1984),
    (r"(san jose|golden bay)( earthquakes)?", "San Jose Earthquakes (NASL)", 1974, 1984),
    (r"washington( diplomats)?", "Washington Diplomats", 1974, 1981),
    (r"hartford( bicentennials)?", "Hartford Bicentennials", 1975, 1976),
    (r"chicago( sting)?", "Chicago Sting", 1975, 1984),
    (r"tampa bay( rowdies)?", "Tampa Bay Rowdies", 1975, 1984),
    (r"portland( timbers)?", "Portland Timbers (NASL)", 1975, 1982),
    (r"san antonio( thunder)?", "San Antonio Thunder", 1975, 1976),
    (r"minnesota( kicks)?", "Minnesota Kicks", 1976, 1981),
    (r"san diego( jaws)?", "San Diego Jaws", 1976, 1976),
    (r"(ft|fort) lauderdale( strikers)?", "Fort Lauderdale Strikers", 1977, 1983),
    (r"(team )?hawaii", "Team Hawaii", 1977, 1977),
    (r"las vegas( quicksilver)?", "Las Vegas Quicksilver", 1977, 1977),
    (r"connecticut( bicentennials)?", "Connecticut Bicentennials", 1977, 1977),
    (r"new england( tea men)?", "New England Tea Men", 1978, 1980),
    (r"philadelphia( fury)?", "Philadelphia Fury", 1978, 1980),
    (r"detroit( express)?", "Detroit Express", 1978, 1980),
    (r"memphis( rogues)?", "Memphis Rogues", 1978, 1980),
    (r"houston( hurricane)?", "Houston Hurricane", 1978, 1980),
    (r"colorado( caribous)?", "Colorado Caribous", 1978, 1978),
    (r"oakland( stompers)?", "Oakland Stompers", 1978, 1978),
    (r"san diego( sockers)?", "San Diego Sockers", 1978, 1984),
    (r"tulsa( roughnecks)?", "Tulsa Roughnecks", 1978, 1984),
    (r"california( surf)?", "California Surf", 1978, 1981),
    (r"toronto( blizzard)?", "Toronto Blizzard", 1979, 1984),
    (r"edmonton( drillers)?", "Edmonton Drillers", 1979, 1982),
    (r"atlanta( chiefs)?", "Atlanta Chiefs (1979)", 1979, 1981),
    (r"calgary( boomers)?", "Calgary Boomers", 1981, 1981),
    (r"jacksonville( tea men)?", "Jacksonville Tea Men", 1981, 1982),
    (r"montreal( manic)?", "Montreal Manic", 1981, 1983),
    (r"team america", "Team America", 1983, 1983),
    (r"minnesota( strikers)?", "Minnesota Strikers", 1984, 1984),
    # MLS
    (r"d ?c( united)?|dc united defeated.*", "DC United", 1996, 2100),
    (r"(la|l|los angeles|l angeles)( galaxy| galay| g)?", "Los Angeles Galaxy", 1996, 2017),
    (r"los angeles fc|lafc|los angeles football club", "Los Angeles FC", 2018, 2100),
    (r"(la|los angeles)( galaxy| galay| g)?", "Los Angeles Galaxy", 2018, 2100),
    (r"(ny ?nj|new york ?new jersey|ny ?nj metrostars|new york ?new jersey metrostars|metro ?stars|new york m|"
     r"new york red bulls|ny red bulls|red bull new york|new york rb)( metrostars)?", "New York Red Bulls", 1996, 2100),
    (r"new england( revolution| rev| r)?|n england|ne revolution", "New England Revolution", 1996, 2100),
    (r"col(o|u)mbus( crew( sc)?| c)?", "Columbus Crew", 1996, 2100),
    (r"tampa bay( mutiny| m)?", "Tampa Bay Mutiny", 1996, 2001),
    (r"(fc )?dallas( burn| b)?", "FC Dallas", 1996, 2100),
    (r"(kansas city|kansas c|kc)( wiz| wizards| w)?|kansas cw|sporting kansas city|sporting kc", "Sporting Kansas City", 1996, 2100),
    (r"(san jose|s jose|sj)( clash| earthquakes| c)?", "San Jose Earthquakes", 1996, 2100),
    (r"colorado( rapids| r)?", "Colorado Rapids", 1996, 2100),
    (r"chicago( fire( fc)?| f)?", "Chicago Fire", 1998, 2100),
    (r"miami( fusion| f)?", "Miami Fusion", 1998, 2001),
    (r"real salt lake|rsl", "Real Salt Lake", 2005, 2100),
    (r"chivas usa", "Chivas USA", 2005, 2014),
    (r"houston( dynamo| dynamos)?( fc)?", "Houston Dynamo", 2006, 2100),
    (r"toronto( fc)?", "Toronto FC", 2007, 2100),
    (r"seattle( sounders)?( fc)?", "Seattle Sounders", 2009, 2100),
    (r"philadelphia( union)?", "Philadelphia Union", 2010, 2100),
    (r"portland( timbers)?", "Portland Timbers", 2011, 2100),
    (r"vancouver( whitecaps)?( fc)?", "Vancouver Whitecaps", 2011, 2100),
    (r"(montreal|montréal)( impact)?|(cf )?montreal( cf)?|club de foot montreal", "CF Montréal", 2012, 2100),
    (r"orlando( city)?( sc)?", "Orlando City", 2015, 2100),
    (r"new york city( fc)?|nycfc|ny city fc", "New York City FC", 2015, 2100),
    (r"atlanta( united)?( fc)?", "Atlanta United", 2017, 2100),
    (r"minnesota( united)?( fc)?", "Minnesota United", 2017, 2100),
    (r"(fc )?cincinnati", "FC Cincinnati", 2019, 2100),
    (r"nashville( sc)?", "Nashville SC", 2020, 2100),
    (r"inter miami( cf)?", "Inter Miami", 2020, 2100),
    (r"austin( fc)?", "Austin FC", 2021, 2100),
    (r"charlotte( fc)?", "Charlotte FC", 2022, 2100),
    (r"(st|saint) ?louis( city)?( sc)?", "St. Louis City SC", 2023, 2100),
    (r"san diego( fc)?", "San Diego FC", 2025, 2100),
]

# o que nunca é clube da liga: jogos de exibição (All-Star, amistosos) que a ESPN traz no calendário da MLS
_NAO_CLUBE = re.compile(r"(all ?stars?$|^mls all|^east all|^west all|^fulham|^(ny|new york) yankees)")
# lixo: público entre parênteses ("Kansas City (11,041)"), "(aet)", "(SO)"
_LIXO = re.compile(r"\s*\((\d{1,3},\d{3}|aet|so|n\.y\.|phil\.?|bkln|pawtucket)\)|\[\[|\]\]", re.I)


def _regra(k: str, ano: int) -> str | None:
    if ano >= 1996 and _NAO_CLUBE.search(k):
        return None
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", nome.strip())), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
