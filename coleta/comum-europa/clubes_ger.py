"""Cadastro dos clubes alemães, comum a todas as divisões da Alemanha.

Chave: um nome do engsoccerdata (o mais recente do clube). Valor: nome de exibição no painel (como o clube é
conhecido no Brasil), cidade e país (código FIFA). O mesmo clube tem o mesmo nome em ger-1, ger-2...

O engsoccerdata usa o nome da época: aqui as grafias do mesmo clube viram uma chave só (ALIASES), como Meidericher SV
e MSV Duisburg, Frankfurter SG Eintracht e Eintracht Frankfurt, SV Bayer 04 e Bayer Leverkusen.

ALIASES: outras grafias (engsoccerdata de outras épocas, RSSSF, football-data, ESPN, Wikipédia) -> chave. O ogol e a
ESPN são casados pelo código do clube (votação jogo a jogo em importar.py), não por aqui.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "1. FC Heidenheim": ("Heidenheim", "Heidenheim", "GER"),
    "1. FC Kaiserslautern": ("Kaiserslautern", "Kaiserslautern", "GER"),
    "1. FC Koln": ("Colônia", "Colônia", "GER"),
    "1. FC Nurnberg": ("Nuremberg", "Nuremberg", "GER"),
    "1. FC Saarbrucken": ("Saarbrücken", "Saarbrücken", "GER"),
    "1. FC Union Berlin": ("Union Berlin", "Berlim", "GER"),
    "1. FSV Mainz 05": ("Mainz 05", "Mainz", "GER"),
    "1899 Hoffenheim": ("Hoffenheim", "Sinsheim", "GER"),
    "Alemannia Aachen": ("Alemannia Aachen", "Aachen", "GER"),
    "Arminia Bielefeld": ("Arminia Bielefeld", "Bielefeld", "GER"),
    "Bayer 05 Uerdingen": ("Uerdingen", "Krefeld", "GER"),
    "Bayer Leverkusen": ("Bayer Leverkusen", "Leverkusen", "GER"),
    "Bayern Munchen": ("Bayern de Munique", "Munique", "GER"),
    "Blau-Weiss 90 Berlin": ("Blau-Weiß 90 Berlin", "Berlim", "GER"),
    "Bor. Monchengladbach": ("Borussia Mönchengladbach", "Mönchengladbach", "GER"),
    "Borussia Dortmund": ("Borussia Dortmund", "Dortmund", "GER"),
    "Borussia Neunkirchen": ("Borussia Neunkirchen", "Neunkirchen", "GER"),
    "Dynamo Dresden": ("Dynamo Dresden", "Dresden", "GER"),
    "Eintracht Braunschweig": ("Eintracht Braunschweig", "Braunschweig", "GER"),
    "Eintracht Frankfurt": ("Eintracht Frankfurt", "Frankfurt", "GER"),
    "Energie Cottbus": ("Energie Cottbus", "Cottbus", "GER"),
    "FC 08 Homburg": ("Homburg", "Homburg", "GER"),
    "FC Augsburg": ("Augsburg", "Augsburg", "GER"),
    "FC Ingolstadt 04": ("Ingolstadt", "Ingolstadt", "GER"),
    "FC Schalke 04": ("Schalke 04", "Gelsenkirchen", "GER"),
    "FC St. Pauli": ("St. Pauli", "Hamburgo", "GER"),
    "Fortuna Dusseldorf": ("Fortuna Düsseldorf", "Düsseldorf", "GER"),
    "Fortuna Koln": ("Fortuna Köln", "Colônia", "GER"),
    "Hamburger SV": ("Hamburgo", "Hamburgo", "GER"),
    "Hannover 96": ("Hannover 96", "Hannover", "GER"),
    "Hansa Rostock": ("Hansa Rostock", "Rostock", "GER"),
    "Hertha BSC": ("Hertha Berlin", "Berlim", "GER"),
    "Holstein Kiel": ("Holstein Kiel", "Kiel", "GER"),
    "Karlsruher SC": ("Karlsruhe", "Karlsruhe", "GER"),
    "Kickers Offenbach": ("Kickers Offenbach", "Offenbach", "GER"),
    "MSV Duisburg": ("Duisburg", "Duisburg", "GER"),
    "Preussen Munster": ("Preußen Münster", "Münster", "GER"),
    "RasenBallsport Leipzig": ("RB Leipzig", "Leipzig", "GER"),
    "Rot-Weiss Essen": ("Rot-Weiss Essen", "Essen", "GER"),
    "Rot-Weiss Oberhausen": ("Rot-Weiß Oberhausen", "Oberhausen", "GER"),
    "SC Freiburg": ("Freiburg", "Freiburg", "GER"),
    "SC Paderborn 07": ("Paderborn", "Paderborn", "GER"),
    "SG Wattenscheid 09": ("Wattenscheid 09", "Bochum", "GER"),
    "SSV Ulm 1846": ("Ulm", "Ulm", "GER"),
    "SV Darmstadt 98": ("Darmstadt 98", "Darmstadt", "GER"),
    "SpVgg Greuther Furth": ("Greuther Fürth", "Fürth", "GER"),
    "SpVgg Unterhaching": ("Unterhaching", "Unterhaching", "GER"),
    "Stuttgarter Kickers": ("Stuttgarter Kickers", "Stuttgart", "GER"),
    "TSV 1860 Munchen": ("1860 Munique", "Munique", "GER"),
    "Tasmania 1900 Berlin": ("Tasmania Berlin", "Berlim", "GER"),
    "TeBe Berlin": ("Tennis Borussia Berlin", "Berlim", "GER"),
    "VfB Leipzig": ("VfB Leipzig", "Leipzig", "GER"),
    "VfB Stuttgart": ("Stuttgart", "Stuttgart", "GER"),
    "VfL Bochum": ("Bochum", "Bochum", "GER"),
    "VfL Wolfsburg": ("Wolfsburg", "Wolfsburg", "GER"),
    "Waldhof Mannheim": ("Waldhof Mannheim", "Mannheim", "GER"),
    "Werder Bremen": ("Werder Bremen", "Bremen", "GER"),
    "Wuppertaler SV": ("Wuppertal", "Wuppertal", "GER"),
}

# grafias de outras fontes (e nomes de outras épocas do mesmo clube) -> chave
ALIASES: dict[str, str] = {
    # o mesmo clube com outro nome no engsoccerdata
    "Meidericher SV": "MSV Duisburg", "Frankfurter SG Eintracht": "Eintracht Frankfurt",
    "SV Bayer 04 Leverkusen": "Bayer Leverkusen",
    # RSSSF, football-data, ESPN, Wikipédia
    "1. FC Köln": "1. FC Koln", "FC Köln": "1. FC Koln", "Köln": "1. FC Koln", "Koln": "1. FC Koln", "FC Koln": "1. FC Koln",
    "1. FC Nürnberg": "1. FC Nurnberg", "Nürnberg": "1. FC Nurnberg", "Nurnberg": "1. FC Nurnberg",
    "1. FC Saarbrücken": "1. FC Saarbrucken", "Saarbrücken": "1. FC Saarbrucken", "Union Berlin": "1. FC Union Berlin",
    "Mainz": "1. FSV Mainz 05", "Mainz 05": "1. FSV Mainz 05", "FSV Mainz 05": "1. FSV Mainz 05",
    "Hoffenheim": "1899 Hoffenheim", "TSG 1899 Hoffenheim": "1899 Hoffenheim", "TSG Hoffenheim": "1899 Hoffenheim",
    "Aachen": "Alemannia Aachen", "Bielefeld": "Arminia Bielefeld", "Uerdingen": "Bayer 05 Uerdingen",
    "Bayer Uerdingen": "Bayer 05 Uerdingen", "KFC Uerdingen 05": "Bayer 05 Uerdingen", "KFC Uerdingen": "Bayer 05 Uerdingen",
    "Leverkusen": "Bayer Leverkusen", "Bayer 04 Leverkusen": "Bayer Leverkusen", "Bayern Munich": "Bayern Munchen",
    "Bayern München": "Bayern Munchen", "FC Bayern München": "Bayern Munchen", "FC Bayern Munich": "Bayern Munchen",
    "Blau-Weiß 90 Berlin": "Blau-Weiss 90 Berlin", "Blau-Weiß Berlin": "Blau-Weiss 90 Berlin",
    "M'gladbach": "Bor. Monchengladbach", "M'Gladbach": "Bor. Monchengladbach", "Borussia Mönchengladbach": "Bor. Monchengladbach",
    "Borussia Monchengladbach": "Bor. Monchengladbach", "Mönchengladbach": "Bor. Monchengladbach",
    "Dortmund": "Borussia Dortmund", "Dresden": "Dynamo Dresden", "Braunschweig": "Eintracht Braunschweig",
    "Ein Frankfurt": "Eintracht Frankfurt", "Frankfurt": "Eintracht Frankfurt", "Cottbus": "Energie Cottbus",
    "FC Energie Cottbus": "Energie Cottbus", "Homburg": "FC 08 Homburg", "Augsburg": "FC Augsburg", "Ingolstadt": "FC Ingolstadt 04",
    "Schalke 04": "FC Schalke 04", "Schalke": "FC Schalke 04", "FC Schalke 04 Gelsenkirchen": "FC Schalke 04",
    "St Pauli": "FC St. Pauli", "St. Pauli": "FC St. Pauli", "Fortuna Düsseldorf": "Fortuna Dusseldorf",
    "Dusseldorf": "Fortuna Dusseldorf", "Düsseldorf": "Fortuna Dusseldorf", "Fortuna Köln": "Fortuna Koln", "SC Fortuna Köln": "Fortuna Koln",
    "Hamburg": "Hamburger SV", "Hannover": "Hannover 96", "Hansa Rostock": "Hansa Rostock", "FC Hansa Rostock": "Hansa Rostock",
    "Hertha": "Hertha BSC", "Hertha BSC Berlin": "Hertha BSC", "Hertha Berlin": "Hertha BSC", "Kiel": "Holstein Kiel",
    "Karlsruhe": "Karlsruher SC", "Offenbach": "Kickers Offenbach", "Duisburg": "MSV Duisburg", "Preußen Münster": "Preussen Munster",
    "RB Leipzig": "RasenBallsport Leipzig", "RasenBallsport": "RasenBallsport Leipzig", "Rot-Weiß Essen": "Rot-Weiss Essen",
    "Rot-Weiß Oberhausen": "Rot-Weiss Oberhausen", "Freiburg": "SC Freiburg", "Paderborn": "SC Paderborn 07",
    "Wattenscheid": "SG Wattenscheid 09", "Ulm": "SSV Ulm 1846", "SSV Ulm": "SSV Ulm 1846", "Darmstadt": "SV Darmstadt 98",
    "Darmstadt 98": "SV Darmstadt 98", "Greuther Furth": "SpVgg Greuther Furth", "Greuther Fürth": "SpVgg Greuther Furth",
    "Furth": "SpVgg Greuther Furth", "Unterhaching": "SpVgg Unterhaching", "1860 Munich": "TSV 1860 Munchen",
    "1860 München": "TSV 1860 Munchen", "TSV 1860 München": "TSV 1860 Munchen", "Munich 1860": "TSV 1860 Munchen",
    "Tasmania Berlin": "Tasmania 1900 Berlin", "SC Tasmania 1900 Berlin": "Tasmania 1900 Berlin",
    "Tennis Borussia Berlin": "TeBe Berlin", "Leipzig": "RasenBallsport Leipzig", "Stuttgart": "VfB Stuttgart",
    "Bochum": "VfL Bochum", "Wolfsburg": "VfL Wolfsburg", "Mannheim": "Waldhof Mannheim", "SV Waldhof Mannheim": "Waldhof Mannheim",
    "Bremen": "Werder Bremen", "SV Werder Bremen": "Werder Bremen", "Wuppertal": "Wuppertaler SV", "Heidenheim": "1. FC Heidenheim",
    "Meiderich": "MSV Duisburg",
    # nomes completos da RSSSF
    "Hannover 1896": "Hannover 96", "BV 09 Borussia Dortmund": "Borussia Dortmund", "BV Borussia 09 Dortmund": "Borussia Dortmund",
    "DSC Arminia Bielefeld": "Arminia Bielefeld", "Berl. Tennis-Club Borussia": "TeBe Berlin", "FC Sankt Pauli": "FC St. Pauli",
    "Offenbacher Kickers": "Kickers Offenbach", "Offenbacher FC Kickers": "Kickers Offenbach",
    "Braunschweiger TSV Eintracht": "Eintracht Braunschweig", "Kieler SV Holstein": "Holstein Kiel",
    "Düsseldorfer TSV Fortuna": "Fortuna Dusseldorf", "Krefelder FC Uerdingen 05": "Bayer 05 Uerdingen",
    "VfL Borussia M'gladbach": "Bor. Monchengladbach", "Borussia M'gladbach": "Bor. Monchengladbach",
    "VfL Borussia Mönchengladbach": "Bor. Monchengladbach", "Wuppertaler SV Borussia": "Wuppertaler SV",
    "SG Eintracht Frankfurt": "Eintracht Frankfurt", "TSV München 1860": "TSV 1860 Munchen", "München 1860": "TSV 1860 Munchen",
    "Eintracht Frankfurt/Main": "Eintracht Frankfurt",
}

# nomes que dependem da época: nome -> [(primeiro ano, último ano, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "Leipzig": [(1993, 1993, "VfB Leipzig"), (2016, 9999, "RasenBallsport Leipzig")],
}


# ---- era antiga (1902/03-1962/63: fase final do campeonato alemão; coleta/ger-1/antigo.py)
# Clube que existe até hoje fica com o nome atual (SpVgg Fürth = Greuther Fürth, 1. SV Jena = Carl Zeiss Jena, TuS Neuendorf =
# TuS Koblenz, FV Saarbrücken = Saarbrücken, Union Oberschöneweide = Union Berlin, Britannia 1892 = Berliner SV 92). Clube
# extinto fica com o nome da época e a cidade da época. País: GER para clubes do território alemão da época (Breslau,
# Königsberg, Stettin, Danzig...); AUT para os clubes de Viena (1938-44); CZE, POL e FRA para os clubes das regiões
# anexadas ou ocupadas (Praga, Sudetos, Cracóvia, Varsóvia, Posen, Estrasburgo, Mulhouse).
CLUBES.update({
    "ABRV Hannover": ("ABRV Hannover", "Hannover", "GER"), "Admira Wien": ("Admira Wacker", "Viena", "AUT"),
    "Alemannia 90 Berlin": ("Alemannia 90 Berlin", "Berlim", "GER"), "Alemannia Cottbus": ("Alemannia Cottbus", "Cottbus", "GER"),
    "Altona 93": ("Altona 93", "Hamburgo", "GER"), "Arminia Hannover": ("Arminia Hannover", "Hannover", "GER"),
    "Askania Forst": ("Askania Forst", "Forst", "GER"), "ATV Liegnitz": ("ATV Liegnitz", "Liegnitz", "GER"),
    "BC Hartha": ("BC Hartha", "Hartha", "GER"), "Berliner BC 03": ("Berliner BC 03", "Berlim", "GER"),
    "Berliner SV 92": ("Berliner SV 92", "Berlim", "GER"), "Beuthen 09": ("Beuthen 09", "Beuthen", "GER"),
    "Borussia Fulda": ("Borussia Fulda", "Fulda", "GER"), "Bremerhaven 93": ("Bremerhaven 93", "Bremerhaven", "GER"),
    "Breslauer SC 08": ("Breslauer SC 08", "Breslau", "GER"), "BuEV Danzig": ("BuEV Danzig", "Danzig", "GER"),
    "BV Altenessen": ("BV Altenessen", "Essen", "GER"), "Carl Zeiss Jena": ("Carl Zeiss Jena", "Jena", "GER"),
    "CfR Köln": ("CfR Köln", "Colônia", "GER"), "Chemnitzer BC": ("Chemnitzer BC", "Chemnitz", "GER"),
    "CSC 03 Kassel": ("CSC 03 Kassel", "Kassel", "GER"), "DFC Prag": ("DFC Praga", "Praga", "CZE"),
    "Dessau 05": ("Dessau 05", "Dessau", "GER"), "Dresdner SC": ("Dresdner SC", "Dresden", "GER"),
    "Duisburger SpV": ("Duisburger SpV", "Duisburg", "GER"), "Düsseldorfer FC 99": ("Düsseldorfer FC 99", "Düsseldorf", "GER"),
    "DWM Posen": ("DWM Posen", "Poznań", "POL"), "Eimsbütteler TV": ("Eimsbütteler TV", "Hamburgo", "GER"),
    "First Vienna": ("First Vienna", "Viena", "AUT"), "FK Pirmasens": ("Pirmasens", "Pirmasens", "GER"),
    "Fortuna Leipzig": ("Fortuna Leipzig", "Leipzig", "GER"), "Freiburger FC": ("Freiburger FC", "Freiburg", "GER"),
    "FSV Frankfurt": ("FSV Frankfurt", "Frankfurt", "GER"), "Germania Hamburg": ("Germania Hamburg", "Hamburgo", "GER"),
    "Germania Königshütte": ("Germania Königshütte", "Königshütte", "GER"), "Guts Muts Dresden": ("Guts Muts Dresden", "Dresden", "GER"),
    "Hamborn 07": ("Hamborn 07", "Duisburg", "GER"), "Hanau 93": ("Hanau 93", "Hanau", "GER"),
    "Helene Altenessen": ("Helene Altenessen", "Essen", "GER"), "Hindenburg Allenstein": ("Hindenburg Allenstein", "Allenstein", "GER"),
    "HSV Groß Born": ("HSV Groß Born", "Groß Born", "GER"), "Karlsruher FV": ("Karlsruher FV", "Karlsruhe", "GER"),
    "Kasseler FV": ("Kasseler FV", "Kassel", "GER"), "Kassel-Rothenditmold": ("Kassel-Rothenditmold", "Kassel", "GER"),
    "Kölner BC": ("Kölner BC", "Colônia", "GER"), "Kölner FC 99": ("Kölner FC 99", "Colônia", "GER"),
    "Lituania Tilsit": ("Lituania Tilsit", "Tilsit", "GER"), "LSV Danzig": ("LSV Danzig", "Danzig", "GER"),
    "LSV Hamburg": ("LSV Hamburg", "Hamburgo", "GER"), "LSV Mölders Krakau": ("LSV Mölders Krakau", "Cracóvia", "POL"),
    "LSV Pütnitz": ("LSV Pütnitz", "Ribnitz-Damgarten", "GER"), "LSV Reinecke Brieg": ("LSV Reinecke Brieg", "Brieg", "GER"),
    "LSV Rerick": ("LSV Rerick", "Rerik", "GER"), "LSV Stettin": ("LSV Stettin", "Stettin", "GER"),
    "Minerva 93 Berlin": ("Minerva 93 Berlin", "Berlim", "GER"), "MSV Brünn": ("MSV Brünn", "Brno", "CZE"),
    "Mülheimer SV 06": ("Mülheimer SV 06", "Colônia", "GER"), "München-Gladbach 1894": ("FC München-Gladbach", "Mönchengladbach", "GER"),
    "Neufahrwasser": ("SV Neufahrwasser", "Danzig", "GER"), "Norden-Nordwest Berlin": ("Norden-Nordwest Berlin", "Berlim", "GER"),
    "NSTG Brüx": ("NSTG Brüx", "Most", "CZE"), "NSTG Graslitz": ("NSTG Graslitz", "Kraslice", "CZE"),
    "NSTG Prag": ("NSTG Praga", "Praga", "CZE"), "Ordnungspolizei Warschau": ("Ordnungspolizei Warschau", "Varsóvia", "POL"),
    "Pforzheim": ("Pforzheim", "Pforzheim", "GER"), "Phönix Karlsruhe": ("Phönix Karlsruhe", "Karlsruhe", "GER"),
    "Phönix Ludwigshafen": ("Phönix Ludwigshafen", "Ludwigshafen", "GER"), "Planitzer SC": ("Planitzer SC", "Zwickau", "GER"),
    "Plauener SuBC": ("Plauener SuBC", "Plauen", "GER"), "Polizei Chemnitz": ("Polizei Chemnitz", "Chemnitz", "GER"),
    "Preußen Berlin": ("Preußen Berlin", "Berlim", "GER"), "Preußen Danzig": ("Preußen Danzig", "Danzig", "GER"),
    "Preußen Dellbrück": ("Preußen Dellbrück", "Colônia", "GER"), "Preußen Krefeld": ("Preußen Krefeld", "Krefeld", "GER"),
    "Preußen Stettin": ("Preußen Stettin", "Stettin", "GER"), "Preußen Zaborze": ("Preußen Zaborze", "Zaborze", "GER"),
    "Prussia-Samland": ("Prussia-Samland", "Königsberg", "GER"), "Rapid Wien": ("Rapid Viena", "Viena", "AUT"),
    "Schlesien Breslau": ("Schlesien Breslau", "Breslau", "GER"), "Schöneberger Kickers": ("Schöneberger Kickers", "Berlim", "GER"),
    "Schwarz-Weiß Essen": ("Schwarz-Weiß Essen", "Essen", "GER"), "Schweinfurt 05": ("Schweinfurt 05", "Schweinfurt", "GER"),
    "SC Erfurt 1895": ("SC Erfurt 1895", "Erfurt", "GER"), "SDW Posen": ("SDW Posen", "Poznań", "POL"),
    "SG SS Straßburg": ("SG SS Straßburg", "Estrasburgo", "FRA"), "Sportfreunde Breslau": ("Sportfreunde Breslau", "Breslau", "GER"),
    "Sportfreunde Katernberg": ("Sportfreunde Katernberg", "Essen", "GER"), "SpV/48/99 Duisburg": ("KSG SpV/48/99 Duisburg", "Duisburg", "GER"),
    "SpVgg Leipzig": ("SpVgg Leipzig", "Leipzig", "GER"), "SSV Reutlingen": ("SSV Reutlingen", "Reutlingen", "GER"),
    "STC Hirschberg": ("STC Hirschberg", "Hirschberg", "GER"), "Stern Breslau": ("Stern Breslau", "Breslau", "GER"),
    "Stettiner SC": ("Stettiner SC", "Stettin", "GER"), "STV Horst-Emscher": ("STV Horst-Emscher", "Gelsenkirchen", "GER"),
    "SV Göppingen": ("SV Göppingen", "Göppingen", "GER"), "SV Sodingen": ("SV Sodingen", "Herne", "GER"),
    "Sülz 07": ("Sülz 07", "Colônia", "GER"), "Titania Stettin": ("Titania Stettin", "Stettin", "GER"),
    "TSG Rostock": ("TSG Rostock", "Rostock", "GER"), "TuRU Düsseldorf": ("TuRU Düsseldorf", "Düsseldorf", "GER"),
    "TuS Koblenz": ("TuS Koblenz", "Koblenz", "GER"), "Union 06 Berlin": ("Union 06 Berlin", "Berlim", "GER"),
    "Union 92 Berlin": ("Union 92 Berlin", "Berlim", "GER"), "Union Böckingen": ("Union Böckingen", "Heilbronn", "GER"),
    "VfB Bielefeld": ("VfB Bielefeld", "Bielefeld", "GER"), "VfB Königsberg": ("VfB Königsberg", "Königsberg", "GER"),
    "VfB Liegnitz": ("VfB Liegnitz", "Liegnitz", "GER"), "VfL 99/Sülz 07 Köln": ("KSG VfL 99/Sülz 07 Köln", "Colônia", "GER"),
    "VfL Benrath": ("VfL Benrath", "Düsseldorf", "GER"), "VfL Köln 99": ("VfL Köln 99", "Colônia", "GER"),
    "VfL Neckarau": ("VfL Neckarau", "Mannheim", "GER"), "VfL Osnabrück": ("VfL Osnabrück", "Osnabrück", "GER"),
    "VfL Stettin": ("VfL Stettin", "Stettin", "GER"), "VfR Breslau": ("VfR Breslau", "Breslau", "GER"),
    "VfR Köln": ("VfR Köln", "Colônia", "GER"), "VfR Mannheim": ("VfR Mannheim", "Mannheim", "GER"),
    "VfTuR München-Gladbach": ("VfTuR München-Gladbach", "Mönchengladbach", "GER"), "Victoria Hamburg": ("Victoria Hamburg", "Hamburgo", "GER"),
    "Victoria Köln": ("Victoria Köln 1911", "Colônia", "GER"), "Viktoria Berlin": ("Viktoria Berlin", "Berlim", "GER"),
    "Viktoria Forst": ("Viktoria Forst", "Forst", "GER"), "Viktoria Magdeburg": ("Viktoria Magdeburg", "Magdeburg", "GER"),
    "Viktoria Stolp": ("Viktoria Stolp", "Stolp", "GER"), "Vorwärts 1890 Berlin": ("Vorwärts 1890 Berlin", "Berlim", "GER"),
    "Vorwärts-Rasensport Gleiwitz": ("Vorwärts-Rasensport Gleiwitz", "Gleiwitz", "GER"), "Wacker Halle": ("Wacker Halle", "Halle", "GER"),
    "Wacker Leipzig": ("Wacker Leipzig", "Leipzig", "GER"), "Wacker München": ("Wacker München", "Munique", "GER"),
    "Warnsdorfer FK": ("Warnsdorfer FK", "Varnsdorf", "CZE"), "Westende Hamborn": ("Westende Hamborn", "Duisburg", "GER"),
    "Westfalia Herne": ("Westfalia Herne", "Herne", "GER"), "Wilhelmshaven 05": ("Wilhelmshaven 05", "Wilhelmshaven", "GER"),
    "Wormatia Worms": ("Wormatia Worms", "Worms", "GER"), "WSV Celle": ("WSV Celle", "Celle", "GER"),
    "Yorck-Boyen Insterburg": ("Yorck-Boyen Insterburg", "Insterburg", "GER"),
    "FC Mulhouse": ("Mulhouse", "Mulhouse", "FRA"),   # o mesmo do fra-1 (FC Mühlhausen 93 na anexação)
})
ALIASES.update({
    # grafias da RSSSF (duit1903...duit1944, duithist4763) e da Wikipédia, era antiga
    "ABRV 1898 Hannover": "ABRV Hannover", "SK Admira Wien": "Admira Wien", "Admira Wien": "Admira Wien", "Admira": "Admira Wien",
    "BTuFC Alemannia 1890": "Alemannia 90 Berlin", "SC Alemannia Cottbus": "Alemannia Cottbus", "TSV Alemannia Aachen": "Alemannia Aachen",
    "FC Altona 93": "Altona 93", "Altona 93": "Altona 93", "1.FC Arminia Bielefeld": "Arminia Bielefeld",
    "TG Arminia Bielefeld": "Arminia Bielefeld", "SV Arminia Hannover": "Arminia Hannover", "FC Askania 1901 Forst": "Askania Forst",
    "BC 01 Hartha": "BC Hartha", "Berliner BC 1903": "Berliner BC 03", "BSV 92 Berlin": "Berliner SV 92",
    "BTuFC Britannia 1892": "Berliner SV 92", "Berliner FC Viktoria 89": "Viktoria Berlin", "Viktoria 89 Berlin": "Viktoria Berlin",
    "Beuthener SuSV 09": "Beuthen 09", "BFC Hertha 1892": "Hertha BSC", "BFC Norden-Nordwest 98": "Norden-Nordwest Berlin",
    "BSV Norden-Nordwest 98": "Norden-Nordwest Berlin", "SV Norden-Nordwest": "Norden-Nordwest Berlin",
    "SV Norden-Nordwest Berlin": "Norden-Nordwest Berlin", "BFC Preußen 1894": "Preußen Berlin",
    "BFC Schöneberger Kickers": "Schöneberger Kickers", "BFC Vorwärts 1890": "Vorwärts 1890 Berlin", "Vorwärts Berlin": "Vorwärts 1890 Berlin",
    "SV Blau-Weiß 90 Berlin": "Blau-Weiss 90 Berlin", "Bor. Neunkirchen": "Borussia Neunkirchen", "1.SV Borussia 04 Fulda": "Borussia Fulda",
    "Reichsb./Borussia Fulda": "Borussia Fulda", "SV Bremerhaven 93": "Bremerhaven 93", "TuS Bremerhaven": "Bremerhaven 93",
    "TuS Bremerhaven 93": "Bremerhaven 93", "Breslauer SC 1908": "Breslauer SC 08", "Breslauer FV Stern 1906": "Stern Breslau",
    "BSG DWM Posen": "DWM Posen", "BSG SDW Posen": "SDW Posen", "BSG Westende Hamborn": "Westende Hamborn",
    "BTuFC Union 1892": "Union 92 Berlin", "BTuFC Union 1892 Berlin": "Union 92 Berlin", "BUeV 1903 Danzig": "BuEV Danzig",
    "BV Altenessen 06": "BV Altenessen", "1.SV Jena 03": "Carl Zeiss Jena", "CfR 1899 Köln": "CfR Köln",
    "Chemnitzer BC 1899": "Chemnitzer BC", "CSC Kassel 03": "CSC 03 Kassel", "SV Dessau 05": "Dessau 05",
    "DFC 1892 Prag": "DFC Prag", "Deutscher FC Prag": "DFC Prag", "Duisburger SpV 1900": "Duisburger SpV",
    "Düsseldorfer FC 1899": "Düsseldorfer FC 99", "Eimsbutteler TV": "Eimsbütteler TV", "Eintr. Braunschweig": "Eintracht Braunschweig",
    "Eintr. Frankfurt": "Eintracht Frankfurt", "First Vienna FC Wien": "First Vienna", "First Vienna FC": "First Vienna",
    "SV Fortuna 1902 Leipzig": "Fortuna Leipzig", "FV Saarbrücken": "1. FC Saarbrucken", "FV/Altenk. Saarbrücken": "1. FC Saarbrucken",
    "FV Holstein Kiel": "Holstein Kiel", "FV Holstein Kiel 1902": "Holstein Kiel", "FV Sportfreunde Breslau": "Sportfreunde Breslau",
    "FV Union 08 Böckingen": "Union Böckingen", "SC Germania Hamburg": "Germania Hamburg", "SV Göppingen": "SV Göppingen",
    "SV Guts Muts Dresden": "Guts Muts Dresden", "1.FC Hanau 93": "Hanau 93", "FC Hanau 93": "Hanau 93",
    "SV Hannover 96": "Hannover 96", "Hannoverscher SV 96": "Hannover 96", "Heeres SV Groß Born": "HSV Groß Born",
    "SV Hindenburg Allenstein": "Hindenburg Allenstein", "MSV Hindenburg Allenstein": "Hindenburg Allenstein",
    "Horst Emscher": "STV Horst-Emscher", "STV Horst-Emscher": "STV Horst-Emscher", "Kasseler FV 1895": "Kasseler FV",
    "SV Kassel-Rothenditmold": "Kassel-Rothenditmold", "SV 06 Kassel-Rothenditm.": "Kassel-Rothenditmold",
    "OFC Kickers Offenbach": "Kickers Offenbach", "Offenbacher FC Kickers": "Kickers Offenbach", "Kölner BC 01": "Kölner BC",
    "Kölner FC 1899": "Kölner FC 99", "KSG SpV/48/99 Duisburg": "SpV/48/99 Duisburg", "KSG VfL 99 Köln/Sülz 07": "VfL 99/Sülz 07 Köln",
    "SpVgg Leipzig-Lindenau": "SpVgg Leipzig", "SpVgg 1899 Leipzig": "SpVgg Leipzig", "SC Lituania Tilsit": "Lituania Tilsit",
    "LSV Groß Hamburg": "LSV Hamburg", "Luftwaffen SV Hamburg": "LSV Hamburg", "Luftwaffen SV Pütnitz": "LSV Pütnitz",
    "Luftwaffen SV Rerick": "LSV Rerick", "Luftwaffen SV Stettin": "LSV Stettin", "Magdeburger FC Viktoria": "Viktoria Magdeburg",
    "SV Viktoria Magdeburg 96": "Viktoria Magdeburg", "Meidericher SV 02": "MSV Duisburg", "Meidericher SV 1902": "MSV Duisburg",
    "Militär SV Brünn": "MSV Brünn", "SC Minerva Berlin": "Minerva 93 Berlin", "SC Minerva 93 Berlin": "Minerva 93 Berlin",
    "FC Mühlhausen 93": "FC Mulhouse", "Mühlheimer SV 06": "Mülheimer SV 06", "FC 1894 München-Gladbach": "München-Gladbach 1894",
    "SV 1919 Neufahrwasser": "Neufahrwasser", "NTSG Prag": "NSTG Prag", "NSTG Prag": "NSTG Prag",
    "SG Ordnungspolizei W.": "Ordnungspolizei Warschau", "SG Ordnungspolizei Warschau": "Ordnungspolizei Warschau",
    "1.FC Pforzheim": "Pforzheim", "FC Phönix Karlsruhe": "Phönix Karlsruhe", "Phönix Karlsruhe": "Phönix Karlsruhe",
    "FC Phönix Ludwigshafen": "Phönix Ludwigshafen", "Planitz": "Planitzer SC", "Planitzer SC 1912": "Planitzer SC",
    "SG Planitz": "Planitzer SC", "Polizei SV Chemnitz": "Polizei Chemnitz", "SC Preußen 01 Stettin": "Preußen Stettin",
    "SC Preußen 09 Danzig": "Preußen Danzig", "FC Preußen 1895 Krefeld": "Preußen Krefeld", "SC Preußen Zaborze": "Preußen Zaborze",
    "SC Preußen Münster": "Preussen Munster", "SV Prussia-Samland": "Prussia-Samland", "SK Rapid Wien": "Rapid Wien",
    "Rapid Wien": "Rapid Wien", "SC Rot-Weiß Essen": "Rot-Weiss Essen", "SC Schlesien 01 Breslau": "Schlesien Breslau",
    "1.FC Schweinfurt 05": "Schweinfurt 05", "SK Schwarz-Weiß Essen": "Schwarz-Weiß Essen", "SC 95 Erfurt": "SC Erfurt 1895",
    "Sportfreunde Hamborn 07": "Hamborn 07", "SpVgg Sülz 07": "Sülz 07", "STC Hirschberg 1919": "STC Hirschberg",
    "FC Titania 02 Stettin": "Titania Stettin", "TuFC Tasmania Rixdorf": "Tasmania 1900 Berlin",
    "TuFC Tasmania Rixdorf Berlin": "Tasmania 1900 Berlin", "Tennis Bor. Berlin": "TeBe Berlin", "TuRU 1880 Düsseldorf": "TuRU Düsseldorf",
    "TuS Helene Altenessen": "Helene Altenessen", "TuS Neuendorf": "TuS Koblenz", "SpVgg Neuendorf": "TuS Koblenz",
    "SC Union 06 Berlin": "Union 06 Berlin", "SC Union Oberschöneweide": "1. FC Union Berlin",
    "Union Oberschönweide": "1. FC Union Berlin", "Union Oberschöneweide": "1. FC Union Berlin", "VfB 1903 Bielefeld": "VfB Bielefeld",
    "VfL 06 Benrath": "VfL Benrath", "VfL 1884 Neckarau": "VfL Neckarau", "VfR 1897 Breslau": "VfR Breslau", "VfR 04 Köln": "VfR Köln",
    "VfR 1904 Köln": "VfR Köln", "VfR Mannheim 1896": "VfR Mannheim", "VfR Wormatia Worms": "Wormatia Worms",
    "SV Victoria 11 Köln": "Victoria Köln", "FC Victoria Hamburg": "Victoria Hamburg", "SC Victoria Hamburg": "Victoria Hamburg",
    "SV Viktoria 09 Stolp": "Viktoria Stolp", "SV Viktoria Stolp": "Viktoria Stolp", "FC Viktoria 1901 Forst": "Viktoria Forst",
    "SpVgg Vorwärts Gleiwitz": "Vorwärts-Rasensport Gleiwitz", "Vorwärts Rasensport Gl.": "Vorwärts-Rasensport Gleiwitz",
    "SpVgg Vorwärts Rasensport Gleiwitz": "Vorwärts-Rasensport Gleiwitz", "SC Wacker 95 Leipzig": "Wacker Leipzig",
    "FC Wacker 95 Leipzig": "Wacker Leipzig", "FC Wacker Halle": "Wacker Halle", "FC Wacker München": "Wacker München",
    "Wehrmacht SV Celle": "WSV Celle", "SpVgg Wilhelmshaven 05": "Wilhelmshaven 05", "MSV Yorck-Boyen Insterb.": "Yorck-Boyen Insterburg",
    "MSV York-Boyen Insterb.": "Yorck-Boyen Insterburg", "Karlsruher FV": "Karlsruher FV", "FSV Frankfurt": "FSV Frankfurt",
    "Freiburger FC": "Freiburger FC", "BV Borussia Dortmund": "Borussia Dortmund",
    "Altonaer FC von 1893": "Altona 93", "SV Victoria 96 Magdeburg": "Viktoria Magdeburg", "Viktoria 96 Magdeburg": "Viktoria Magdeburg",
    "Britannia Berlin": "Berliner SV 92", "FV Kassel": "Kasseler FV", "Duisburger SV": "Duisburger SpV",
    "BFC Vorwärts 90": "Vorwärts 1890 Berlin", "SC Koln 99": "Kölner FC 99", "SC Köln 99": "Kölner FC 99",
    "Berliner FC Hertha 92": "Hertha BSC", "SG Oberschöneweide": "1. FC Union Berlin",
})
# "Union Berlin" na tabela de 1952/53 da RSSSF é o SC Union 06 (Berlim Ocidental)
POR_ANO["Union Berlin"] = [(1945, 1962, "Union 06 Berlin"), (1963, 9999, "1. FC Union Berlin")]


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and").replace("ß", "ss"))


_INDICE: dict[str, str] = {chave(v[0]): k for k, v in CLUBES.items()}   # o nome de exibição também serve
_INDICE.update({chave(k): k for k in CLUBES})
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}

# siglas que a RSSSF e a ESPN põem em volta do nome ("FC Schalke 04", "SV Werder Bremen", "1.FSV Mainz 05")
SIGLAS = {"fc", "sv", "vfb", "vfl", "tsv", "tsg", "fsv", "sc", "spvgg", "bsc", "ev", "1", "e", "v", "kfc", "msv", "ssv", "sg"}


def _reduzir(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome.replace("ß", "ss")).encode("ascii", "ignore").decode().lower()
    return "".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in SIGLAS)


_REDUZIDO: dict[str, str] = {}
for _nome, _c in [(k, k) for k in CLUBES] + [(v[0], k) for k, v in CLUBES.items()] + list(ALIASES.items()):
    _REDUZIDO.setdefault(_reduzir(_nome), _c)


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que
    dependem da época ("Leipzig")."""
    nome = nome.replace("&nbsp;", " ").replace("\xa0", " ")
    k = chave(nome.strip().rstrip("*").strip())
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k) or _REDUZIDO.get(_reduzir(nome))


def exibicao(chave_clube: str) -> str:
    return CLUBES[chave_clube][0]
