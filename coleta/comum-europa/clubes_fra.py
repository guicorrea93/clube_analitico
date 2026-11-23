"""Cadastro dos clubes franceses, comum a todas as divisões da França.

Chave: um nome do engsoccerdata (o mais recente do clube). Valor: nome de exibição no painel (como o clube é
conhecido no Brasil), cidade e país (código FIFA). O mesmo clube tem o mesmo nome em fra-1, fra-2...

O engsoccerdata usa o nome da época: aqui as grafias do mesmo clube viram uma chave só (ALIASES): Red Star Olympique,
Red Star Olympique Audonien, Stade Red Star e Red Star FC; Racing Club de France e Matra Racing; Montpellier La Paillade
e Montpellier HSC; Brest Armorique e Stade Brest; UA Sedan-Torcy e CS Sedan; US Valenciennes-Anzin e Valenciennes FC;
ATAC e ESTAC Troyes; AS Cannes-Grasse e AS Cannes; Stade Français. O "RC Roubaix" do engsoccerdata de 1945 a 1955 é o CO
Roubaix-Tourcoing (fusão de 1945). Ficam separados os clubes que só têm a cidade em
comum (SO Montpellier e Montpellier; Olympique Lillois, SC Fives e Lille OSC; Troyes-Savinienne, Troyes AF e Troyes).

ALIASES: outras grafias (engsoccerdata de outras épocas, RSSSF, football-data, ESPN, Wikipédia) -> chave. O ogol e a
ESPN são casados pelo código do clube (votação jogo a jogo em importar.py), não por aqui.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "AC Ajaccio": ("Ajaccio", "Ajaccio", "FRA"),
    "AC Arles-Avignon": ("Arles-Avignon", "Arles", "FRA"),
    "GFC Ajaccio": ("Gazélec Ajaccio", "Ajaccio", "FRA"),
    "AJ Auxerre": ("Auxerre", "Auxerre", "FRA"),
    "AS Aixoise": ("Aix-en-Provence", "Aix-en-Provence", "FRA"),
    "AS Angouleme": ("Angoulême", "Angoulême", "FRA"),
    "AS Beziers": ("Béziers", "Béziers", "FRA"),
    "AS Cannes": ("Cannes", "Cannes", "FRA"),
    "AS Monaco": ("Monaco", "Mônaco", "MON"),
    "AS Nancy": ("Nancy", "Nancy", "FRA"),
    "AS Saint-Etienne": ("Saint-Étienne", "Saint-Étienne", "FRA"),
    "AS Troyes-Savinienne": ("Troyes-Savinienne", "Troyes", "FRA"),
    "Amiens SC": ("Amiens", "Amiens", "FRA"),
    "Angers SCO": ("Angers", "Angers", "FRA"),
    "Association Sportive Avignonaise": ("Avignon", "Avignon", "FRA"),
    "CA Paris (alt)": ("CA Paris", "Paris", "FRA"),
    "Club Francais": ("Club Français", "Paris", "FRA"),          # só em 1932/33, que a base não traz certo
    "CS Sedan": ("Sedan", "Sedan", "FRA"),
    "Chamois Niortais": ("Niort", "Niort", "FRA"),
    "Clermont Foot 63": ("Clermont", "Clermont-Ferrand", "FRA"),
    "Dijon FCO": ("Dijon", "Dijon", "FRA"),
    "EA Guingamp": ("Guingamp", "Guingamp", "FRA"),
    "ESTAC Troyes": ("Troyes", "Troyes", "FRA"),
    "Evian Thonon Gaillard": ("Évian", "Thonon-les-Bains", "FRA"),   # revisão FR-021
    "Excelsior Roubaix": ("Excelsior Roubaix", "Roubaix", "FRA"),
    "FC Antibes": ("Antibes", "Antibes", "FRA"),
    "FC Gueugnon": ("Gueugnon", "Gueugnon", "FRA"),
    "FC Istres": ("Istres", "Istres", "FRA"),
    "FC Lorient": ("Lorient", "Lorient", "FRA"),
    "FC Martigues": ("Martigues", "Martigues", "FRA"),
    "FC Metz": ("Metz", "Metz", "FRA"),
    "FC Mulhouse": ("Mulhouse", "Mulhouse", "FRA"),
    "FC Nantes": ("Nantes", "Nantes", "FRA"),
    "FC Rouen": ("Rouen", "Rouen", "FRA"),
    "FC Sete": ("Sète", "Sète", "FRA"),
    "FC Sochaux": ("Sochaux", "Montbéliard", "FRA"),
    "Girondins Bordeaux": ("Bordeaux", "Bordeaux", "FRA"),
    "Grenoble Foot 38": ("Grenoble", "Grenoble", "FRA"),
    "Hyeres FC": ("Hyères", "Hyères", "FRA"),                     # só em 1932/33
    "LB Chateauroux": ("Châteauroux", "Châteauroux", "FRA"),
    "Le Havre AC": ("Le Havre", "Le Havre", "FRA"),
    "Le Mans UC 72": ("Le Mans", "Le Mans", "FRA"),
    "Lille OSC": ("Lille", "Lille", "FRA"),
    "Limoges FC": ("Limoges", "Limoges", "FRA"),
    "Montpellier HSC": ("Montpellier", "Montpellier", "FRA"),
    "Nimes Olympique": ("Nîmes", "Nîmes", "FRA"),
    "OGC Nice": ("Nice", "Nice", "FRA"),
    "Olympique Ales": ("Alès", "Alès", "FRA"),
    "Olympique Lillois Lille": ("Olympique Lillois", "Lille", "FRA"),
    "Olympique Lyon": ("Lyon", "Lyon", "FRA"),
    "Olympique Marseille": ("Olympique de Marseille", "Marselha", "FRA"),
    "Paris FC": ("Paris FC", "Paris", "FRA"),
    "Paris Saint-Germain": ("PSG", "Paris", "FRA"),
    "RC Lens": ("Lens", "Lens", "FRA"),
    "RC Roubaix": ("RC Roubaix", "Roubaix", "FRA"),
    "CO Roubaix-Tourcoing": ("CO Roubaix-Tourcoing", "Roubaix", "FRA"),   # fusão de 1945 (RC Roubaix, Excelsior e US Tourcoing)
    "RC Strasbourg": ("Strasbourg", "Estrasburgo", "FRA"),
    "Racing Club de France": ("Racing Paris", "Paris", "FRA"),
    "Red Star FC": ("Red Star", "Saint-Ouen", "FRA"),
    "SC Bastia": ("Bastia", "Bastia", "FRA"),
    "SC Fives Lille": ("Fives", "Lille", "FRA"),
    "SC Nimes": ("SC Nîmes", "Nîmes", "FRA"),
    "SM Caen": ("Caen", "Caen", "FRA"),
    "SR Colmar": ("Colmar", "Colmar", "FRA"),
    "Sporting Toulon Var": ("Toulon", "Toulon", "FRA"),
    "Stade Brest": ("Brest", "Brest", "FRA"),
    "Stade Francais FC": ("Stade Français", "Paris", "FRA"),
    "Stade Laval": ("Laval", "Laval", "FRA"),
    "Stade Olympique Montpellierain": ("SO Montpellier", "Montpellier", "FRA"),
    "Stade Reims": ("Reims", "Reims", "FRA"),
    "Stade Rennes": ("Rennes", "Rennes", "FRA"),
    "Toulouse FC": ("Toulouse", "Toulouse", "FRA"),
    # o Toulouse FC de 1937, que se fundiu com o Red Star em 1967, é outro clube (revisão FR-012, decisão D-24 a)
    "Toulouse FC (1937)": ("Toulouse FC (1937)", "Toulouse", "FRA"),
    "Tours FC": ("Tours", "Tours", "FRA"),
    "Troyes AF": ("Troyes AF", "Troyes", "FRA"),
    "US Boulogne": ("Boulogne", "Boulogne-sur-Mer", "FRA"),
    "Valenciennes FC": ("Valenciennes", "Valenciennes", "FRA"),
}

# grafias de outras fontes (e nomes de outras épocas do mesmo clube) -> chave
ALIASES: dict[str, str] = {
    # o mesmo clube com outro nome no engsoccerdata
    "Red Star Olympique": "Red Star FC", "Red Star Olympique Audonien": "Red Star FC",
    "Matra Racing": "Racing Club de France", "Montpellier La Paillade SC": "Montpellier HSC", "Brest Armorique FC": "Stade Brest",
    "UA Sedan-Torcy": "CS Sedan", "US Valenciennes-Anzin": "Valenciennes FC", "ATAC Troyes": "ESTAC Troyes",
    "AS Cannes-Grasse": "AS Cannes", "Stade Francais": "Stade Francais FC", "Stade de Paris FC": "Stade Francais FC",
    # RSSSF (franfullhist), nomes em maiúsculas
    "AIX": "AS Aixoise", "EXCELSIOR": "Excelsior Roubaix", "OL. LILLOIS": "Olympique Lillois Lille", "OSC LILLE": "Lille OSC",
    "PARIS ST GERM": "Paris Saint-Germain", "PARIS ST.GERM.": "Paris Saint-Germain", "HYERES": "Hyeres FC",
    "CLUB FRANCAIS": "Club Francais", "FIVES": "SC Fives Lille", "STADE REIMS": "Stade Reims", "CA PARIS": "CA Paris (alt)",
    "FC PARIS": "Paris FC", "AMIENS": "Amiens SC", "ST ETIENNE": "AS Saint-Etienne", "ST. ETIENNE": "AS Saint-Etienne",
    "ST.ETIENNE": "AS Saint-Etienne", "SC NIMES": "SC Nimes", "ALES": "Olympique Ales",
    # football-data.co.uk, ESPN, Wikipédia
    "Paris SG": "Paris Saint-Germain", "Marseille": "Olympique Marseille", "Lyon": "Olympique Lyon", "Monaco": "AS Monaco",
    "St Etienne": "AS Saint-Etienne", "Saint-Etienne": "AS Saint-Etienne", "Bordeaux": "Girondins Bordeaux",
    "Nantes": "FC Nantes", "Rennes": "Stade Rennes", "Lens": "RC Lens", "Nice": "OGC Nice", "Strasbourg": "RC Strasbourg",
    "Toulouse": "Toulouse FC", "Montpellier": "Montpellier HSC", "Reims": "Stade Reims", "Nancy": "AS Nancy",
    "Metz": "FC Metz", "Sochaux": "FC Sochaux", "Auxerre": "AJ Auxerre", "Bastia": "SC Bastia", "Guingamp": "EA Guingamp",
    "Brest": "Stade Brest", "Lorient": "FC Lorient", "Caen": "SM Caen", "Le Havre": "Le Havre AC", "Angers": "Angers SCO",
    "Ajaccio": "AC Ajaccio", "Clermont": "Clermont Foot 63", "Troyes": "ESTAC Troyes",
    "Dijon": "Dijon FCO", "Amiens": "Amiens SC", "Nimes": "Nimes Olympique", "Lille": "Lille OSC", "Sedan": "CS Sedan",
    "Valenciennes": "Valenciennes FC", "Le Mans": "Le Mans UC 72", "Grenoble": "Grenoble Foot 38", "Evian": "Evian Thonon Gaillard",
    "Evian Thonon Gaillard": "Evian Thonon Gaillard", "Arles": "AC Arles-Avignon", "Boulogne": "US Boulogne",
    "Istres": "FC Istres", "Gueugnon": "FC Gueugnon", "Martigues": "FC Martigues", "Chateauroux": "LB Chateauroux",
    "Cannes": "AS Cannes", "Stade Rennais UC": "Stade Rennes", "FC Mulhouse 1893": "FC Mulhouse", "CAP": "CA Paris (alt)", "Gazélec Ajaccio": "GFC Ajaccio", "Gazélec Ajaccio FCO": "GFC Ajaccio", "Béziers Hérault": "AS Beziers",
    "Lyon OU": "Olympique Lyon", "RC Paris-Sedan": "CS Sedan", "AS Nancy Lorraine": "AS Nancy", "AS Nancy-Lorraine": "AS Nancy",
    "CS Sedan Ardennes": "CS Sedan", "CS Sedan-Ardennes": "CS Sedan", "Clermont Foot Auvergne 63": "Clermont Foot 63",
    "ES Troyes AC": "ESTAC Troyes", "En Avant Guingamp": "EA Guingamp", "FC Nantes Atlantique": "FC Nantes",
    "FC Sochaux-Montbéliard": "FC Sochaux", "Montpellier-Hérault": "Montpellier HSC", "Montpellier-Hérault SC": "Montpellier HSC",
    "RC Strasbourg Alsace": "RC Strasbourg", "Stade Malherbe Caen": "SM Caen", "US Boulogne-sur-mer CO": "US Boulogne", "CO Roubaix-Tourcoing": "CO Roubaix-Tourcoing", "CORT": "CO Roubaix-Tourcoing", "Roubaix–Tourcoing": "CO Roubaix-Tourcoing", "Roubaix-Tourcoing": "CO Roubaix-Tourcoing", "Toulon": "Sporting Toulon Var", "Laval": "Stade Laval", "Niort": "Chamois Niortais",
    "Tours": "Tours FC", "Mulhouse": "FC Mulhouse", "Rouen": "FC Rouen", "Red Star": "Red Star FC",
    "Paris Saint Germain": "Paris Saint-Germain", "Racing Paris": "Racing Club de France", "RC Paris": "Racing Club de France",
    "Olympique de Marseille": "Olympique Marseille", "Olympique Lyonnais": "Olympique Lyon", "Lille OSC": "Lille OSC",
    "LOSC Lille": "Lille OSC", "Stade Rennais": "Stade Rennes", "Stade de Reims": "Stade Reims", "AS Saint-Étienne": "AS Saint-Etienne",
    "Saint-Étienne": "AS Saint-Etienne", "Nîmes": "Nimes Olympique", "Brest Armorique": "Stade Brest",
    "Stade Brestois 29": "Stade Brest", "Stade Brestois": "Stade Brest", "Girondins de Bordeaux": "Girondins Bordeaux",
    "FC Girondins de Bordeaux": "Girondins Bordeaux", "Paris FC": "Paris FC", "Châteauroux": "LB Chateauroux",
}

# nomes que dependem da época: nome -> [(primeiro ano, último ano, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    # Toulouse FC de 1937 (1ª divisão de 1946/47 a 1966/67) x o de 1970 (revisão FR-012)
    **{n: [(1932, 1966, "Toulouse FC (1937)"), (1967, 9999, "Toulouse FC")] for n in ("Toulouse", "Toulouse FC", "TOULOUSE")},
    "Montpellier": [(1932, 1962, "Stade Olympique Montpellierain"), (1981, 9999, "Montpellier HSC")],
    "Troyes": [(1954, 1960, "AS Troyes-Savinienne"), (1973, 1977, "Troyes AF"), (1999, 9999, "ESTAC Troyes")],
    "Nimes": [(1932, 1934, "SC Nimes"), (1950, 9999, "Nimes Olympique")],
    "Nîmes": [(1932, 1934, "SC Nimes"), (1950, 9999, "Nimes Olympique")],
    "Roubaix": [(1935, 1938, "RC Roubaix"), (1945, 1969, "CO Roubaix-Tourcoing")],
    # erros de nome da RSSSF (franfullhist): "AMIENS" em 1937/38 é o Antibes (ogol, Wikipédia); "GRENOBLE" em 1979/80 é o Bastia
    "AMIENS": [(1937, 1937, "FC Antibes"), (1938, 9999, "Amiens SC")],
    "GRENOBLE": [(0, 1978, "Grenoble Foot 38"), (1979, 1979, "SC Bastia"), (1980, 9999, "Grenoble Foot 38")],
    # 1948/49 e 1949/50: fusão Stade Français-Red Star; a RSSSF e a Wikipédia contam como o Stade Français
    "Stade Red Star": [(1948, 1949, "Stade Francais FC")], "Stade Français-Red Star": [(1948, 1949, "Stade Francais FC")],
    # 2015/16: quem jogou a 1ª divisão foi o Gazélec Ajaccio; o engsoccerdata o chama de AC Ajaccio
    "AC Ajaccio": [(1967, 2014, "AC Ajaccio"), (2015, 2015, "GFC Ajaccio"), (2016, 9999, "AC Ajaccio")],
    "Ajaccio GFCO": [(2015, 2015, "GFC Ajaccio")],
    # o engsoccerdata chama de "RC Roubaix" também o CO Roubaix-Tourcoing (1945-1955)
    "RC Roubaix": [(1935, 1938, "RC Roubaix"), (1945, 1969, "CO Roubaix-Tourcoing")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {chave(v[0]): k for k, v in CLUBES.items()}   # o nome de exibição também serve
_INDICE.update({chave(k): k for k in CLUBES})
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}

# siglas que a RSSSF e a ESPN põem em volta do nome ("FC Nantes", "AS Monaco FC", "Olympique de Marseille")
SIGLAS = {"fc", "ac", "as", "sc", "rc", "us", "osc", "sco", "ogc", "aj", "ea", "hsc", "de", "du", "la", "le", "foot", "football",
          "club", "olympique", "stade", "sm", "cs", "ca", "fco", "29", "63", "38", "72"}


def _reduzir(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return "".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in SIGLAS)


_REDUZIDO: dict[str, str] = {}
for _nome, _c in [(k, k) for k in CLUBES] + [(v[0], k) for k, v in CLUBES.items()] + list(ALIASES.items()):
    _REDUZIDO.setdefault(_reduzir(_nome), _c)


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que
    dependem da época ("Montpellier", "Troyes", "Nîmes")."""
    nome = nome.replace("&nbsp;", " ").replace("\xa0", " ")
    k = chave(nome.strip().rstrip("*").strip())
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k) or _REDUZIDO.get(_reduzir(nome))


def exibicao(chave_clube: str) -> str:
    return CLUBES[chave_clube][0]
