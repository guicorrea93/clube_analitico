"""Cadastro dos clubes belgas, comum a todas as divisões da Bélgica.

Chave: o nome de exibição no painel (como o clube é conhecido no Brasil), com cidade e país. Nomes únicos no mundo,
conferidos no banco e nos outros pacotes.

Identidade (pela linhagem legal do clube, a matrícula da federação belga, como na Wikipédia):
- o mesmo clube com nomes de época vira uma chave só: FC Brugeois e Club Brugge; CS Brugeois e Cercle Brugge; FC Liégeois
  e RFC Liège; La Gantoise e Gent; FC Malinois e KV Mechelen; SC Courtraisien e Kortrijk; White Star, Racing White e
  RWD Molenbeek (1909-2002); Olympic Charleroi (Montignies, Marchienne); Winterslag e Genk (o KRC Genk de 1988 ficou com a
  matrícula do Winterslag; o Waterschei é outro clube); Boom FC e Rupel Boom (fusão de 1987 com a matrícula 61; a
  Wikipédia usa o mesmo artigo);
- clubes diferentes com nome parecido ficam separados:
  - o Beerschot de 1899 ("Beerschot VAC", dissolvido em 1999), o Germinal Ekeren/Germinal Beerschot/Beerschot AC
    (1999-2013) e o Beerschot VA de hoje ("Beerschot");
  - o Seraing de 1904 (RFC Sérésien, 1982-1996) e o de hoje ("Seraing");
  - o Excelsior Mouscron (1996-2009) e o Royal Excel Mouscron (2014-2020); o KFC Lommel SK (1992-2002) e o Lommel SK de
    hoje;
  - o RWD Molenbeek de 1909 e o RWDM de 2015 ("RWDM Brussels"); o FC Brussels (2004-2007) à parte;
  - o KSK Beveren e o Waasland-Beveren; o KSV Waregem e o Zulte Waregem; o Racing Mechelen e o KV Mechelen; o Racing Gent
    e o Gent; o Racing Club de Bruxelles e o Daring;
  - o AS Oostende (1969-1976) e o KV Oostende (fusão de 1981); a RAA Louviéroise (até 2009) e a RAAL La Louvière de hoje.

OGOL: código do clube no ogol -> chave (os nomes do calendário do ogol não são confiáveis na Bélgica: o mesmo código aparece
como "RFC Bressoux" e "Union Liegeoise", e é o Seraing de 1904); os códigos foram identificados pelos números da campanha
de cada temporada, iguais aos das tabelas da RSSSF e da Wikipédia. OGOL_POR_ANO: códigos que o ogol usa para dois clubes.
ALIASES: grafias das fontes -> chave. POR_ANO: nomes que dependem da época ("Beerschot", "Mouscron", "Waregem").
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    # grandes e clubes de hoje
    "Anderlecht": ("Bruxelas", "BEL"), "Club Brugge": ("Bruges", "BEL"), "Standard Liège": ("Liège", "BEL"),
    "Genk": ("Genk", "BEL"), "Gent": ("Gante", "BEL"), "Antwerp": ("Antuérpia", "BEL"), "Union Saint-Gilloise": ("Bruxelas", "BEL"),
    "KV Mechelen": ("Mechelen", "BEL"), "Cercle Brugge": ("Bruges", "BEL"), "Charleroi": ("Charleroi", "BEL"),
    "Sint-Truiden": ("Sint-Truiden", "BEL"), "Westerlo": ("Westerlo", "BEL"), "OH Leuven": ("Leuven", "BEL"),
    "Kortrijk": ("Kortrijk", "BEL"), "Zulte Waregem": ("Waregem", "BEL"), "Eupen": ("Eupen", "BEL"), "Lokeren": ("Lokeren", "BEL"),
    "Lierse": ("Lier", "BEL"), "KSK Beveren": ("Beveren", "BEL"), "Waasland-Beveren": ("Beveren", "BEL"), "Mons": ("Mons", "BEL"),
    "Excelsior Mouscron": ("Mouscron", "BEL"), "Royal Excel Mouscron": ("Mouscron", "BEL"), "Dender": ("Denderleeuw", "BEL"),
    "Oostende": ("Ostende", "BEL"), "AS Oostende": ("Ostende", "BEL"), "RAA Louviéroise": ("La Louvière", "BEL"),
    "RAAL La Louvière": ("La Louvière", "BEL"), "Beerschot": ("Antuérpia", "BEL"), "Germinal Beerschot": ("Antuérpia", "BEL"),
    "Beerschot VAC": ("Antuérpia", "BEL"), "RWD Molenbeek": ("Bruxelas", "BEL"), "RWDM Brussels": ("Bruxelas", "BEL"),
    "FC Brussels": ("Bruxelas", "BEL"), "Seraing": ("Seraing", "BEL"), "RFC Seraing (1904)": ("Seraing", "BEL"),
    "Roeselare": ("Roeselare", "BEL"), "Tubize": ("Tubize", "BEL"), "Heusden-Zolder": ("Heusden-Zolder", "BEL"),
    "Geel": ("Geel", "BEL"), "Harelbeke": ("Harelbeke", "BEL"), "KFC Lommel SK": ("Lommel", "BEL"), "Lommel SK": ("Lommel", "BEL"),
    "Eendracht Aalst": ("Aalst", "BEL"), "KSV Waregem": ("Waregem", "BEL"), "RFC Liège": ("Liège", "BEL"),
    # clubes que saíram da 1ª divisão antes dos anos 2000
    "Waterschei": ("Genk", "BEL"), "Racing Mechelen": ("Mechelen", "BEL"), "Racing Gent": ("Gante", "BEL"),
    "Daring Club de Bruxelles": ("Bruxelas", "BEL"), "Racing Club de Bruxelles": ("Bruxelas", "BEL"),
    "Olympic Charleroi": ("Charleroi", "BEL"), "Berchem Sport": ("Antuérpia", "BEL"), "Beringen": ("Beringen", "BEL"),
    "Tilleur": ("Liège", "BEL"), "CS Verviétois": ("Verviers", "BEL"), "Lyra": ("Lier", "BEL"), "Boom": ("Boom", "BEL"),
    "Turnhout": ("Turnhout", "BEL"), "Sint-Niklaas": ("Sint-Niklaas", "BEL"),
    "Diest": ("Diest", "BEL"), "Patro Eisden": ("Maasmechelen", "BEL"), "Tienen": ("Tienen", "BEL"),
    "Crossing Schaerbeek": ("Bruxelas", "BEL"), "Hasselt": ("Hasselt", "BEL"), "Tongeren": ("Tongeren", "BEL"),
    "Racing Jet de Bruxelles": ("Bruxelas", "BEL"), "Uccle Sport": ("Bruxelas", "BEL"), "La Forestoise": ("Bruxelas", "BEL"),
    "Léopold Club": ("Bruxelas", "BEL"), "Excelsior SC de Bruxelles": ("Bruxelas", "BEL"), "Tubantia": ("Antuérpia", "BEL"),
    "Montegnée": ("Saint-Nicolas", "BEL"), "Belgica Edegem": ("Edegem", "BEL"), "Stade Leuven": ("Leuven", "BEL"),
    "US Tournai": ("Tournai", "BEL"), "Racing Tournai": ("Tournai", "BEL"),
    # pioneiros (1895-1913)
    "Sporting Club de Bruxelles": ("Bruxelas", "BEL"), "Union d'Ixelles": ("Bruxelas", "BEL"),
    "Athletic & Running Club de Bruxelles": ("Bruxelas", "BEL"), "Skill FC de Bruxelles": ("Bruxelas", "BEL"),
    "Olympia Club de Bruxelles": ("Bruxelas", "BEL"), "Sport Pédestre de Gand": ("Gante", "BEL"),
    "Oostendensche FC": ("Ostende", "BEL"),
}

OGOL: dict[str, str] = {
    "9518": "Waterschei", "1783": "Lierse", "1778": "Sint-Truiden", "1775": "Standard Liège", "13903": "Olympic Charleroi",
    "anderlecht": "Anderlecht", "4198": "RFC Liège", "gent": "Gent", "8673": "Eendracht Aalst", "royal-antwerp": "Antwerp",
    "63428": "Daring Club de Bruxelles", "22077": "Patro Eisden", "club-brugge": "Club Brugge", "63429": "Beerschot VAC",
    "27931": "CS Verviétois", "union-st-gilloise": "Union Saint-Gilloise", "1784": "Cercle Brugge", "84825": "Diest",
    "12457": "Beringen", "28759": "Berchem Sport", "5083": "KV Mechelen", "262360": "Turnhout", "56656": "Tilleur",
    "10831": "RWD Molenbeek", "42444": "KSV Waregem", "1788": "Charleroi", "1781": "KSK Beveren", "67950": "Crossing Schaerbeek",
    "1034": "Lokeren", "110554": "Genk", "15773": "Racing Mechelen", "7809": "Kortrijk", "110552": "Boom", "43308": "Hasselt",
    "22076": "Tongeren", "7803": "RFC Seraing (1904)", "30136": "Sint-Niklaas", "270086": "Racing Jet de Bruxelles", "genk": "Genk",
    "1782": "Germinal Beerschot", "63820": "Germinal Beerschot", "6382": "KFC Lommel SK", "33016": "Boom",
    "8433": "Harelbeke", "1777": "Excelsior Mouscron", "1780": "Westerlo", "8955": "Geel", "1786": "Mons", "1785": "Heusden-Zolder",
    "4192": "FC Brussels", "5870": "Zulte Waregem", "5871": "Roeselare", "9579": "Dender", "8934": "Tubize", "8927": "Eupen",
    "8929": "OH Leuven", "8930": "Waasland-Beveren", "58667": "Royal Excel Mouscron", "84679": "Beerschot", "21035": "Seraing",
    "360443": "RWDM Brussels", "13732": "Lommel SK",
}
# códigos que o ogol usa para dois clubes: código -> [(primeiro ano, último ano, chave)]
OGOL_POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "4190": [(1960, 1980, "AS Oostende"), (1981, 9999, "Oostende")],
    "1118": [(1960, 2008, "RAA Louviéroise"), (2009, 9999, "RAAL La Louvière")],
}

ALIASES = {
    # Anderlecht, Brugge, Standard, Liège
    "SC Anderlechtois": "Anderlecht", "RSC Anderlechtois": "Anderlecht", "RSC Anderlecht": "Anderlecht",
    "R.S.C. Anderlecht": "Anderlecht", "SC Anderlecht": "Anderlecht",
    "FC Brugeois": "Club Brugge", "F.C. Brugeois": "Club Brugge", "FC Bruges": "Club Brugge", "FC Brugge": "Club Brugge",
    "RFC Brugeois": "Club Brugge", "Club Brugge KV": "Club Brugge", "Club Brugge K.V.": "Club Brugge",
    "CS Brugeois": "Cercle Brugge", "C.S. Brugeois": "Cercle Brugge", "CS Bruges": "Cercle Brugge", "RCS Brugeois": "Cercle Brugge",
    "KSV Cercle Brugge": "Cercle Brugge", "Cercle Bruges": "Cercle Brugge", "Cercle Brügge": "Cercle Brugge",
    "Cercle Brugge KSV": "Cercle Brugge", "Cercle Brugge K.S.V.": "Cercle Brugge",
    "Standard Club Liégeois": "Standard Liège", "R. Standard Club Liégeois": "Standard Liège",
    "R. Standard Club Liegeois": "Standard Liège", "R. Standard de Liège": "Standard Liège", "Standard": "Standard Liège",
    "Standard CL (Liège)": "Standard Liège",
    "FC Liégeois": "RFC Liège", "F.C. Liégeois": "RFC Liège", "Liège": "RFC Liège", "Liége": "RFC Liège", "RFC Liegeois": "RFC Liège",
    "RFC Liégeois": "RFC Liège", "R. FC Liégeois": "RFC Liège", "FC Liège": "RFC Liège", "RFC de Liège": "RFC Liège",
    "R.F.C. de Liège": "RFC Liège", "R. FC de Liège": "RFC Liège", "RC Liégeois": "RFC Liège", "Club Liégeois": "RFC Liège",
    # Antwerp, Beerschot, Berchem, Lyra, Tubantia
    "Antwerp FC": "Antwerp", "Antwerp F.C.": "Antwerp", "Royal Antwerp FC": "Antwerp", "R. Antwerp FC": "Antwerp",
    "R. Antwerp F.C.": "Antwerp", "Royal Antwerp": "Antwerp",
    "Beerschot AC": "Beerschot VAC", "Beerschot A.C.": "Beerschot VAC", "R. Beerschot AC": "Beerschot VAC",
    "Beerschot VAV": "Beerschot VAC", "R. Beerschot VAC": "Beerschot VAC", "K. Beerschot V.A.C.": "Beerschot VAC",
    "Germinal Ekeren": "Germinal Beerschot", "KFC Germinal Ekeren": "Germinal Beerschot",
    "K.F.C. Germinal Ekeren": "Germinal Beerschot", "K.F.C. Germinal Beerschot": "Germinal Beerschot",
    "Germinal Beerschot Antwerpen": "Germinal Beerschot", "KFC Germinal Beerschot": "Germinal Beerschot", "Germinal": "Germinal Beerschot",
    "Beerschot VA": "Beerschot", "Beerschot Wilrijk": "Beerschot", "K Beerschot VA": "Beerschot",
    "K Berchem Sport": "Berchem Sport", "K. Berchem Sport": "Berchem Sport", "R. Berchem Sport": "Berchem Sport",
    "R. Berchem Sp.": "Berchem Sport", "Berchem": "Berchem Sport",
    "TSV Lyra": "Lyra", "KM Lyra": "Lyra", "K. Lyra": "Lyra", "K.Lyra": "Lyra",
    "Tubantia AC": "Tubantia", "K. Tubantia Borgerhout V.K.": "Tubantia",
    "Belgica FC Edegem": "Belgica Edegem", "Edegem": "Belgica Edegem",
    # Gent
    "AA La Gantoise": "Gent", "A.A. La Gantoise": "Gent", "ARA La Gantoise": "Gent", "La Gantoise": "Gent", "KAA Gent": "Gent",
    "K.A.A. Gent": "Gent", "AA Gent": "Gent", "RAA Gent": "Gent",
    "RC Gantois": "Racing Gent", "Racing Gand": "Racing Gent", "Racing Club Gantois": "Racing Gent", "R.C. Gantois": "Racing Gent",
    "RC de Gand": "Racing Gent", "RC Gand": "Racing Gent", "R. Racing Club Gand": "Racing Gent", "Racing Club Gand": "Racing Gent",
    "RRC Gand": "Racing Gent", "Gantois": "Racing Gent",
    # Mechelen
    "FC Malinois": "KV Mechelen", "RFC Malinois": "KV Mechelen", "KFC Malinois": "KV Mechelen", "Mechelen": "KV Mechelen",
    "Y.R. K.V. Mechelen": "KV Mechelen",
    "RC Malines": "Racing Mechelen", "R.C. Malines": "Racing Mechelen", "KRC Malines": "Racing Mechelen", "RC Malinois": "Racing Mechelen",
    "RRC Malines": "Racing Mechelen", "RRC Malinois": "Racing Mechelen", "KRC Mechelen": "Racing Mechelen",
    "K.R.C. Mechelen": "Racing Mechelen", "Racing Club de Malines": "Racing Mechelen", "RC Mechelen": "Racing Mechelen",
    # Bruxelas
    "Union St.-Gilloise": "Union Saint-Gilloise", "Union St.-Gill.": "Union Saint-Gilloise", "RC de Bruxelles": "Racing Club de Bruxelles", "Union SG": "Union Saint-Gilloise", "Royale Union Saint-Gilloise": "Union Saint-Gilloise",
    "St. Gilloise": "Union Saint-Gilloise", "Royal Union Saint-Gilloise": "Union Saint-Gilloise",
    "Daring Club": "Daring Club de Bruxelles", "R. Daring Club de Bruxelles": "Daring Club de Bruxelles",
    "R. Daring club de Bruxelles": "Daring Club de Bruxelles", "Daring Club Bruxelles": "Daring Club de Bruxelles",
    "Racing Bruxelles": "Racing Club de Bruxelles", "R. Racing Club de Bruxelles": "Racing Club de Bruxelles",
    "RC Brussel": "Racing Club de Bruxelles", "R.R.C. Bruxelles": "Racing Club de Bruxelles",
    "White Star": "RWD Molenbeek", "White Star AC": "RWD Molenbeek", "White Star Woluwé A.C.": "RWD Molenbeek",
    "Racing White": "RWD Molenbeek", "R. Racing White": "RWD Molenbeek", "R.W.D. Molenbeek": "RWD Molenbeek", "RWDM": "RWD Molenbeek",
    "Molenbeek Brussels Strombeek": "FC Brussels", "Brussels": "FC Brussels",
    "Uccle": "Uccle Sport", "R. Uccle Sport": "Uccle Sport", "Ukkel Sport": "Uccle Sport",
    "CS La Forestoise": "La Forestoise", "CS Vorst": "La Forestoise",
    "Léopold": "Léopold Club", "Léopold Club de Bruxelles": "Léopold Club",
    "Excelsior SC Forest": "Excelsior SC de Bruxelles", "Excelsior S.C. de Bruxelles": "Excelsior SC de Bruxelles",
    "Excelsior Bruxelles": "Excelsior SC de Bruxelles",
    "R. Crossing Cl de Schaerbeek": "Crossing Schaerbeek", "Crossing Club Schaerbeek": "Crossing Schaerbeek",
    "RJ Bruxelles": "Racing Jet de Bruxelles", "RC Jet de Bruxelles": "Racing Jet de Bruxelles",
    "Sporting CB": "Sporting Club de Bruxelles", "Union FC d'Ixelles": "Union d'Ixelles", "Union F.C. d'Ixelles": "Union d'Ixelles",
    "Union FC d\x92Ixelles": "Union d'Ixelles",
    "Athl. & Running Cl. de Bruxelles": "Athletic & Running Club de Bruxelles",
    "Athletic and Running Club de Bruxelles": "Athletic & Running Club de Bruxelles", "Athletic Club Bruxelles": "Athletic & Running Club de Bruxelles",
    "Skill FC Bruxelles": "Skill FC de Bruxelles", "Skill Bruxelles": "Skill FC de Bruxelles", "Skill F.C. de Bruxelles": "Skill FC de Bruxelles",
    "Olympia Bruxelles": "Olympia Club de Bruxelles", "Oostendensche": "Oostendensche FC",
    # Charleroi
    "OC Charleroi": "Olympic Charleroi", "ROC Charleroi": "Olympic Charleroi", "R. OC Charleroi": "Olympic Charleroi",
    "R.O.C. de Charleroi-Marchienne": "Olympic Charleroi", "Olympic Montignies-sur-Sambre": "Olympic Charleroi",
    "Olympic M.-s.-S.": "Olympic Charleroi",
    "RSC Charleroi": "Charleroi", "R. Charleroi SC": "Charleroi", "R. Charleroi S.C.": "Charleroi",
    "Sporting du Pays de Charleroi": "Charleroi", "Sporting Charleroi": "Charleroi", "Royal Charleroi S.C.": "Charleroi",
    # outros
    "SC Courtraisien": "Kortrijk", "S.C. Courtraisien": "Kortrijk", "FC Courtraisien": "Kortrijk", "Courtraisien": "Kortrijk",
    "KV Kortrijk": "Kortrijk", "K.V. Kortrijk": "Kortrijk",
    "Verviers FC": "CS Verviétois", "Verviers F.C.": "CS Verviétois", "Verviers": "CS Verviétois", "C.S. Verviétois": "CS Verviétois",
    "Verviétois": "CS Verviétois", "RCS Verviers": "CS Verviétois", "R.C.S. Verviétois": "CS Verviétois", "RCS Verviétois": "CS Verviétois",
    "R. Tilleur FC": "Tilleur", "Tilleur FC": "Tilleur", "R.F.C. Tilleur-Saint-Nicolas": "Tilleur",
    "Liersche SK": "Lierse", "R. Liersche SK": "Lierse", "Lierse SK": "Lierse", "Lierse S.K.": "Lierse", "K.Lierse SK": "Lierse",
    "K. Lierse SK": "Lierse",
    "FC Turnhout": "Turnhout", "K.V. Turnhout": "Turnhout",
    "RC Tirlemont": "Tienen", "K.V.K. Tienen": "Tienen",
    "St-Niklaas": "Sint-Niklaas", "Sint-Niklase": "Sint-Niklaas", "K.St.-Niklase SK": "Sint-Niklaas", "K. Sint-Niklase S.K.E.": "Sint-Niklaas",
    "Eendracht Alost": "Eendracht Aalst", "KSC Eendracht Aalst": "Eendracht Aalst", "K.S.C. Eendracht Aalst": "Eendracht Aalst",
    "Aalst": "Eendracht Aalst",
    "Stade Louvain": "Stade Leuven",
    "Beringen FC": "Beringen", "K.Beeringen FC": "Beringen", "R. Beringen FC": "Beringen", "K. Beringen F.C.": "Beringen",
    "K.Waterschei SV Thor Genk": "Waterschei", "K. Waterschei S.V. Thor Genk": "Waterschei", "Waterschei Thor": "Waterschei",
    "St.Truidense VV": "Sint-Truiden", "K.St.-Truidense VV": "Sint-Truiden", "R. St.-Truidense VV": "Sint-Truiden",
    "K. Sint-Truidense V.V.": "Sint-Truiden", "Sint-Truidense V.V.": "Sint-Truiden", "Sint Truidense VV": "Sint-Truiden",
    "K.Sint-Truiden": "Sint-Truiden", "K. Sint-Truiden VV": "Sint-Truiden", "St Truiden": "Sint-Truiden",
    "FC Diest": "Diest", "KFC Diest": "Diest",
    "K.S.V. Waregem": "KSV Waregem",
    "SK Beveren": "KSK Beveren", "K.S.K. Beveren": "KSK Beveren", "SK Beveren-Waas": "KSK Beveren",
    "A.S.V. Oostende K.M.": "AS Oostende", "KV Oostende": "Oostende", "K.V. Oostende": "Oostende",
    "KSC Lokeren": "Lokeren", "K.S.C. Lokeren Oost-Vlaanderen": "Lokeren", "Sporting Lokeren": "Lokeren",
    "Sp. Lokeren St-Nikl. Waasland": "Lokeren", "Sporting Lokeren SNW": "Lokeren", "KSC Lokeren OV": "Lokeren",
    "FC Winterslag": "Genk", "KFC Winterslag": "Genk", "Winterslag": "Genk", "KRC Genk": "Genk", "K.R.C. Genk": "Genk",
    "Racing Club Genk": "Genk",
    "AA Louviéroise": "RAA Louviéroise", "R.A.A. Louviéroise": "RAA Louviéroise", "R. AA Louviéroise": "RAA Louviéroise",
    "RAA Louvièroise": "RAA Louviéroise", "Louvieroise": "RAA Louviéroise", "RAAL La Louviere": "RAAL La Louvière",
    "SC Hasselt": "Hasselt", "KSC Hasselt": "Hasselt", "SK Tongeren": "Tongeren", "K.S.K. Tongeren": "Tongeren",
    "RFC Sérésien": "RFC Seraing (1904)", "R.F.C. Seraing": "RFC Seraing (1904)",
    "KFC Lommel": "KFC Lommel SK", "K.F.C. Lommel S.K.": "KFC Lommel SK", "KFC Lommelse SK": "KFC Lommel SK",
    "KRC Harelbeke": "Harelbeke", "K.R.C. Zuid-West-Vlaanderen": "Harelbeke", "Racing Club Harelbeke": "Harelbeke",
    "R. Excelsior Mouscron": "Excelsior Mouscron", "R.E. Mouscron": "Excelsior Mouscron",
    "Mouscron-Péruwelz": "Royal Excel Mouscron", "Mouscron-Peruwelz": "Royal Excel Mouscron", "Excel Mouscron": "Royal Excel Mouscron",
    "VC Westerlo": "Westerlo", "KVC Westerlo": "Westerlo", "K.V.C. Westerlo": "Westerlo",
    "KFC Verbroedering Geel": "Geel", "RAEC Mons": "Mons", "Bergen": "Mons", "K.Heusden-Zolder": "Heusden-Zolder",
    "Heusden Zolder": "Heusden-Zolder", "SV Zulte-Waregem": "Zulte Waregem", "Zulte-Waregem": "Zulte Waregem",
    "KSV Roeselare": "Roeselare", "FC Verbroedering Dender EH": "Dender", "Dender EH": "Dender", "Oud-Heverlee Leuven": "OH Leuven",
    "KAS Eupen": "Eupen", "K Boom FC": "Boom", "K. Boom F.C.": "Boom", "Rupel Boom": "Boom", "K. Rupel Boom FC": "Boom",
    "FC Boom": "Boom", "Boom FC": "Boom",
    "US Doornik": "US Tournai", "R.U.S. Tournai": "US Tournai",
    "FC Mechelen": "KV Mechelen", "Standard CL": "Standard Liège", "Lierse SV": "Lierse", "RC Genk": "Genk",
    "SC Charleroi": "Charleroi", "AA Gent": "Gent", "Sint-Truidense VV": "Sint-Truiden", "RRC Tournaissien": "Racing Tournai", "R.F.C. Tournai": "Racing Tournai", "Montegnée": "Montegnée", "RC Montegneé": "Montegnée",
}

# nomes que dependem da época: nome -> [(primeiro ano, último ano, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "Beerschot": [(1900, 1998, "Beerschot VAC"), (1999, 2012, "Germinal Beerschot"), (2013, 9999, "Beerschot")],
    "Mouscron": [(1996, 2012, "Excelsior Mouscron"), (2013, 9999, "Royal Excel Mouscron")],
    "Seraing": [(1982, 1996, "RFC Seraing (1904)"), (1997, 9999, "Seraing")],
    "RFC Seraing": [(1982, 1996, "RFC Seraing (1904)"), (1997, 9999, "Seraing")],
    "FC Seraing": [(1982, 1996, "RFC Seraing (1904)"), (1997, 9999, "Seraing")],
    "Lommel": [(1992, 2002, "KFC Lommel SK"), (2003, 9999, "Lommel SK")],
    "Waregem": [(1966, 2000, "KSV Waregem"), (2001, 9999, "Zulte Waregem")],
    "Molenbeek": [(1924, 2002, "RWD Molenbeek"), (2003, 2014, "FC Brussels"), (2015, 9999, "RWDM Brussels")],
    "RWD Molenbeek": [(1924, 2002, "RWD Molenbeek"), (2015, 9999, "RWDM Brussels")],
    "La Louvière": [(1960, 2008, "RAA Louviéroise"), (2009, 9999, "RAAL La Louvière")],
    "Oostende": [(1960, 1980, "AS Oostende"), (1981, 9999, "Oostende")],
    "Beveren": [(1935, 2009, "KSK Beveren"), (2010, 9999, "Waasland-Beveren")],
    "Tournai": [(1951, 1951, "US Tournai"), (1958, 1958, "Racing Tournai")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {chave(k): k for k in CLUBES}
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que dependem
    da época."""
    nome = re.sub(r"\s+", " ", nome.replace("&nbsp;", " ").replace("\xa0", " ").strip().rstrip("*").strip())
    k = chave(nome)
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k)


def ogol(codigo: str, ano: int | None = None) -> str | None:
    if codigo in OGOL_POR_ANO:
        return next((c for ini, fim, c in OGOL_POR_ANO[codigo] if ano is not None and ini <= ano <= fim), None)
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
