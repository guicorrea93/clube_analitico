"""Cadastro dos clubes italianos, comum a todas as divisões da Itália.

Chave: um nome do engsoccerdata (o mais recente do clube). Valor: nome de exibição no painel (como o clube é
conhecido no Brasil), cidade e país (código FIFA). O mesmo clube tem o mesmo nome em ita-1, ita-2...

O engsoccerdata usa o nome da época: aqui as grafias do mesmo clube viram uma chave só (ALIASES), como Genova 1893
e Genoa CFC, AC Liguria e Sampierdarenese, Lanerossi Vicenza e Vicenza Calcio, US e AS Livorno, Parma AC e Parma FC.
A Sampdoria (fusão de 1946) fica separada da Sampierdarenese e da Andrea Doria, que a formaram.
"Palermo" já é um clube argentino no banco: o italiano fica "Palermo FC" (nome oficial atual).

ALIASES: outras grafias (engsoccerdata de outras épocas, RSSSF, football-data, ESPN, Wikipédia) -> chave. O ogol e a
ESPN são casados pelo código do clube (votação jogo a jogo em importar.py), não por aqui.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "A.C.R. Messina": ("Messina", "Messina", "ITA"),
    "AC Cesena": ("Cesena", "Cesena", "ITA"),
    "AC Mantova": ("Mantova", "Mântua", "ITA"),
    "AC Milan": ("Milan", "Milão", "ITA"),
    "AC Monza": ("Monza", "Monza", "ITA"),
    "AC Perugia": ("Perugia", "Perúgia", "ITA"),
    "AC Pistoiese": ("Pistoiese", "Pistoia", "ITA"),
    "AC Reggiana": ("Reggiana", "Reggio Emilia", "ITA"),
    "AC Siena": ("Siena", "Siena", "ITA"),
    "AC Venezia": ("Venezia", "Veneza", "ITA"),
    "ACF Fiorentina": ("Fiorentina", "Florença", "ITA"),
    "AS Bari": ("Bari", "Bari", "ITA"),
    "AS Livorno": ("Livorno", "Livorno", "ITA"),
    "AS Roma": ("Roma", "Roma", "ITA"),
    "AS Varese 1910": ("Varese", "Varese", "ITA"),
    "Ancona Calcio": ("Ancona", "Ancona", "ITA"),
    "Andrea Doria": ("Andrea Doria", "Gênova", "ITA"),
    "Ascoli Calcio": ("Ascoli", "Ascoli Piceno", "ITA"),
    "Atalanta": ("Atalanta", "Bérgamo", "ITA"),
    "Benevento": ("Benevento", "Benevento", "ITA"),
    "Bologna FC": ("Bologna", "Bolonha", "ITA"),
    "Brescia Calcio": ("Brescia", "Brescia", "ITA"),
    "Cagliari Calcio": ("Cagliari", "Cagliari", "ITA"),
    "Calcio Catania": ("Catania", "Catânia", "ITA"),
    "Calcio Lecco 1912": ("Lecco", "Lecco", "ITA"),
    "Calcio Padova": ("Padova", "Pádua", "ITA"),
    "Carpi FC": ("Carpi", "Carpi", "ITA"),
    "Casale": ("Casale", "Casale Monferrato", "ITA"),
    "Chievo Verona": ("Chievo", "Verona", "ITA"),
    "Como Calcio": ("Como", "Como", "ITA"),
    "Empoli FC": ("Empoli", "Empoli", "ITA"),
    "FC Crotone": ("Crotone", "Crotone", "ITA"),
    "Frosinone Calcio": ("Frosinone", "Frosinone", "ITA"),
    "Genoa CFC": ("Genoa", "Gênova", "ITA"),
    "Hellas Verona": ("Verona", "Verona", "ITA"),
    "Inter": ("Inter de Milão", "Milão", "ITA"),
    "Juventus": ("Juventus", "Turim", "ITA"),
    "Lazio Roma": ("Lazio", "Roma", "ITA"),
    "Legnano": ("Legnano", "Legnano", "ITA"),
    "Lucchese": ("Lucchese", "Lucca", "ITA"),
    "Modena FC": ("Modena", "Módena", "ITA"),
    "Novara Calcio": ("Novara", "Novara", "ITA"),
    "Parma FC": ("Parma", "Parma", "ITA"),
    "Pescara Calcio": ("Pescara", "Pescara", "ITA"),
    "Piacenza Calcio": ("Piacenza", "Piacenza", "ITA"),
    "Pisa SC": ("Pisa", "Pisa", "ITA"),
    "Pro Patria": ("Pro Patria", "Busto Arsizio", "ITA"),
    "Pro Vercelli": ("Pro Vercelli", "Vercelli", "ITA"),
    "Reggina Calcio": ("Reggina", "Reggio Calabria", "ITA"),
    "SPAL 1907 Ferrara": ("SPAL", "Ferrara", "ITA"),
    "SSC Napoli": ("Napoli", "Nápoles", "ITA"),
    "Salernitana Calcio 1919": ("Salernitana", "Salerno", "ITA"),
    "Sampdoria": ("Sampdoria", "Gênova", "ITA"),
    "Sampierdarenese": ("Sampierdarenese", "Gênova", "ITA"),
    "Sassuolo Calcio": ("Sassuolo", "Sassuolo", "ITA"),
    "Spezia Calcio": ("Spezia", "La Spezia", "ITA"),
    "Ternana Calcio": ("Ternana", "Terni", "ITA"),
    "Torino FC": ("Torino", "Turim", "ITA"),
    "Treviso FBC": ("Treviso", "Treviso", "ITA"),
    "US Alessandria 1912": ("Alessandria", "Alessandria", "ITA"),
    "US Avellino": ("Avellino", "Avellino", "ITA"),
    "US Catanzaro": ("Catanzaro", "Catanzaro", "ITA"),
    "US Cremonese": ("Cremonese", "Cremona", "ITA"),
    "US Foggia": ("Foggia", "Foggia", "ITA"),
    "US Lecce": ("Lecce", "Lecce", "ITA"),
    "US Palermo": ("Palermo FC", "Palermo", "ITA"),
    "Udinese Calcio": ("Udinese", "Udine", "ITA"),
    "Unione Triestina": ("Triestina", "Trieste", "ITA"),
    "Vicenza Calcio": ("Vicenza", "Vicenza", "ITA"),
}

# grafias de outras fontes (e nomes de outras épocas do mesmo clube) -> chave
# Era antiga (1898 a 1928/29, IT-017): clubes que só aparecem nela. A identidade é a da Wikipédia em italiano: cada
# clube tem um modelo {{Calcio X}}, e a Wikipédia separa as entidades diferentes com o mesmo nome ("Hellas (1907-1918)",
# "Mantova (1911-1956)", "Piemonte (1910-1915)"). Chave = nome do modelo; valor = (exibição, cidade, país).
_ANTIGOS = {
    "A.M.C. Milanese": ("A.M.C. Milanese", "Milão", "ITA"),
    # só nas fichas de mata-mata (sem classificação de grupo na Wikipédia it)
    "Internazionale Torino": ("Internazionale Torino", "Turim", "ITA"), "Lambro": ("Lambro", "Milão", "ITA"),
    "Mediolanum": ("Mediolanum", "Milão", "ITA"), "Tebro Roma": ("Tebro Roma", "Roma", "ITA"),
    "Audace Ferrara": ("Audace Ferrara", "Ferrara", "ITA"), "Bergamasca": ("Bergamasca", "Bérgamo", "ITA"),
    "Brasiliano": ("Brasiliano", "Nápoles", "ITA"),
    "Tiberis": ("Tiberis", "Roma", "ITA"), "Vigor Trapani": ("Vigor Trapani", "Trapani", "ITA"),
    "AC Libertas": ("AC Libertas", "Milão", "ITA"),
    "AC Ligure": ("AC Ligure", "Gênova", "ITA"),
    "Acqui": ("Acqui", "Acqui Terme", "ITA"),
    "Alba Roma": ("Alba Roma", "Roma", "ITA"),
    "Alessandrina": ("Alessandrina", "Alessandria", "ITA"),
    "Amatori Torino": ("Amatori Torino", "Turim", "ITA"),
    "Audace Roma": ("Audace Roma", "Roma", "ITA"),
    "Audace Taranto": ("Audace Taranto", "Taranto", "ITA"),
    "Audace Torino": ("Audace Torino", "Turim", "ITA"),
    "Audacia Napoli": ("Audacia Napoli", "Nápoles", "ITA"),
    "Audax Modena": ("Audax Modena", "Módena", "ITA"),
    "Ausonia": ("Ausonia", "Milão", "ITA"),
    "Ausonia Pro Gorla": ("Ausonia Pro Gorla", "Milão", "ITA"),
    "Bagnolese Napoli": ("Bagnolese Napoli", "Nápoles", "ITA"),
    "Bentegodi": ("Bentegodi", "Verona", "ITA"),
    "Biellese": ("Biellese", "Biella", "ITA"),
    "C.S. Firenze": ("C.S. Firenze", "Florença", "ITA"),
    "Carignano": ("Carignano", "Carignano", "ITA"),
    "Casertana": ("Casertana", "Caserta", "ITA"),
    "Casteggio": ("Casteggio", "Casteggio", "ITA"),
    "Cavese": ("Cavese", "Cava de' Tirreni", "ITA"),
    "Chiasso": ("Chiasso", "Chiasso", "SUI"),
    "Derthona": ("Derthona", "Tortona", "ITA"),
    "Dolo": ("Dolo", "Dolo", "ITA"),
    "Enotria Goliardo": ("Enotria Goliardo", "Milão", "ITA"),
    "Enotria Taranto": ("Enotria Taranto", "Taranto", "ITA"),
    "Esperia": ("Esperia", "Como", "ITA"),
    "FC Torinese": ("FC Torinese", "Turim", "ITA"),
    "Firenze FBC": ("Firenze FBC", "Florença", "ITA"),
    "Fiumana": ("Fiumana", "Fiume (Rijeka)", "ITA"),
    "Folgore Ancona": ("Folgore Ancona", "Ancona", "ITA"),
    "Fortitudo": ("Fortitudo", "Roma", "ITA"),
    "Fortitudo Pro Roma": ("Fortitudo Pro Roma", "Roma", "ITA"),
    "GS Bolognese": ("GS Bolognese", "Bolonha", "ITA"),
    "Ginnastica Torino": ("Ginnastica Torino", "Turim", "ITA"),
    "Giovani Calciatori": ("Giovani Calciatori", None, "ITA"),
    "Giovani Calciatori Grifone": ("Giovani Calciatori Grifone", "Gênova", "ITA"),
    "Giovani Calciatori Legnanesi": ("Giovani Calciatori Legnanesi", "Legnano", "ITA"),
    "Giovani Cappuccini": ("Giovani Cappuccini", None, "ITA"),
    "Giovanni Gerbi Pisa": ("Giovanni Gerbi Pisa", "Pisa", "ITA"),
    "Hellas (1907-1918)": ("Hellas Verona (1907)", "Verona", "ITA"),
    "Helvia Recina": ("Helvia Recina", "Macerata", "ITA"),
    "Ideale Bari": ("Ideale Bari", "Bari", "ITA"),
    "Internazionale Napoli": ("Internazionale Napoli", "Nápoles", "ITA"),
    "Itala Firenze": ("Itala Firenze", "Florença", "ITA"),
    "Juventus Audax": ("Juventus Audax", "Roma", "ITA"),
    "Juventus Italia": ("Juventus Italia", "Milão", "ITA"),
    "Juventus Roma": ("Juventus Roma", "Roma", "ITA"),
    "Legnaghese": ("Legnaghese", "Legnago", "ITA"),
    "Libertas Firenze": ("Libertas Firenze", "Florença", "ITA"),
    "Libertas Palermo": ("Libertas Palermo", "Palermo", "ITA"),
    "Liberty Bari": ("Liberty Bari", "Prima Divisione 1923-1924#Sezione pugliese", "ITA"),
    "Liguria FBC": ("Liguria FBC", "Gênova", "ITA"),
    "Macerata (1919)": ("Macerata", "Macerata", "ITA"),
    "Maceratese": ("Maceratese", "Macerata", "ITA"),
    "Messina FC (1922)": ("Messina FC", "Messina", "ITA"),
    "Messina SC": ("Messina SC", "Messina", "ITA"),
    "Messinese": ("Messinese", "Messina", "ITA"),
    "Naples": ("Naples", "Nápoles", "ITA"),
    "Nazionale Emilia": ("Nazionale Emilia", "Bolonha", "ITA"),
    "Nazionale Lombardia": ("Nazionale Lombardia", "Milão", "ITA"),
    "Novese": ("Novese", "Novi Ligure", "ITA"),
    "Olympia Fiume": ("Olympia Fiume", "Fiume (Rijeka)", "ITA"),
    "Pastore": ("Pastore", "Turim", "ITA"),
    "Pavia": ("Pavia", "Pavia", "ITA"),
    "Petrarca Padova": ("Petrarca Padova", "Pádua", "ITA"),
    "Piemonte (1910-1915)": ("Piemonte FC", "Turim", "ITA"),
    "Prato": ("Prato", "Prato", "ITA"),
    "Pro Caserta": ("Pro Caserta", "Caserta", "ITA"),
    "Pro Italia Taranto": ("Pro Italia Taranto", "Taranto", "ITA"),
    "Pro Livorno 1919-1922": ("Pro Livorno", "Livorno", "ITA"),
    "Pro Napoli": ("Pro Napoli", "Nápoles", "ITA"),
    "Pro Roma": ("Pro Roma", "Roma", "ITA"),
    "Pro Sesto": ("Pro Sesto", "Sesto San Giovanni", "ITA"),
    "Puteolana": ("Puteolana", "Pozzuoli", "ITA"),
    "Racing Libertas": ("Racing Libertas", "Milão", "ITA"),
    "Rivarolese": ("Rivarolese", "Gênova", "ITA"),
    "Roman": ("Roman", "Roma", "ITA"),
    "SPES Livorno": ("SPES Livorno", "Livorno", "ITA"),
    "Saronno": ("Saronno", "Saronno", "ITA"),
    "Savoia": ("Savoia", "Torre Annunziata", "ITA"),
    "Savoia Milano": ("Savoia Milano", "Milão", "ITA"),
    "Savona": ("Savona", "Savona", "ITA"),
    "Savonese": ("Savonese", "Savona", "ITA"),
    "Schio": ("Schio", "Schio", "ITA"),
    "Sestrese": ("Sestrese", "Gênova", "ITA"),
    "Speranza Savona": ("Speranza Savona", "Savona", "ITA"),
    "Spes Genova": ("Spes Genova", "Gênova", "ITA"),
    "Stabiese": ("Stabiese", "Castellammare di Stabia", "ITA"),
    "Stelvio Milano": ("Stelvio Milano", "Milão", "ITA"),
    "Tarantina": ("Tarantina", "Prima Divisione 1923-1924#Sezione pugliese", "ITA"),
    "Tivoli": ("Tivoli", "Tivoli", "ITA"),
    "Trevigliese": ("Trevigliese", "Treviglio", "ITA"),
    "US Bagnolese": ("US Bagnolese", "Nápoles", "ITA"),
    "US Mantovana": ("US Mantovana", "Mântua", "ITA"),
    "US Milanese": ("US Milanese", "Milão", "ITA"),
    "US Romana": ("US Romana", "Roma", "ITA"),
    "US Torinese": ("US Torinese", "Turim", "ITA"),
    "Udine": ("Udine", "Udine", "ITA"),
    "Umberto I Messina": ("Umberto I Messina", "Messina", "ITA"),
    "Valenzana": ("Valenzana", "Valenza", "ITA"),
    "Veloce Taranto": ("Veloce Taranto", "Taranto", "ITA"),
    "Veloces Biella": ("Veloces Biella", "Biella", "ITA"),
    "Viareggio": ("Viareggio", "Viareggio", "ITA"),
    "Vigor Senigallia": ("Vigor Senigallia", "Senigallia", "ITA"),
    "Vigor Torino": ("Vigor Torino", "Turim", "ITA"),
    "Virtus Bologna": ("Virtus Bologna", "Bolonha", "ITA"),
    "Virtus Bolognese": ("Virtus Bolognese", "Bolonha", "ITA"),
    "Virtus Juventusque": ("Virtus Juventusque", "Livorno", "ITA"),
    "Virtus Macerata": ("Virtus Macerata", "Macerata", "ITA"),
    "Vittoria Roma": ("Vittoria Roma", "Roma", "ITA"),
    "Volontari Venezia": ("Volontari Venezia", "Veneza", "ITA"),
}
CLUBES.update(_ANTIGOS)

# modelo {{Calcio X}} da Wikipédia em italiano -> chave do cadastro (era antiga). Os clubes de hoje vão para a chave de
# sempre; renomeações do mesmo clube também (Internaples -> Napoli em 1926, Salernitanaudax -> Salernitana, La Dominante
# -> Liguria -> Sampierdarenese). Os outros modelos são a própria chave (CLUBES.update acima).
MODELOS_IT: dict[str, str] = {
    "Alessandria": "US Alessandria 1912", "Ancona": "Ancona Calcio", "Anconitana": "Ancona Calcio",
    "Andrea Doria": "Andrea Doria", "Atalanta": "Atalanta", "Bari": "AS Bari",
    "Bologna": "Bologna FC", "Brescia": "Brescia Calcio", "Carpi": "Carpi FC",
    "Casale": "Casale", "Como": "Como Calcio", "Cremonese": "US Cremonese",
    "Dominante": "Sampierdarenese", "FBC Bari": "AS Bari", "Fiorentina": "ACF Fiorentina",
    "Foggia": "US Foggia", "Genoa": "Genoa CFC", "Hellas Verona": "Hellas Verona",
    "Inter": "Inter", "Internaples": "SSC Napoli", "Juventus": "Juventus",
    "Lazio": "Lazio Roma", "Lecce": "US Lecce", "Legnano": "Legnano",
    "Livorno": "AS Livorno", "Lucchese": "Lucchese", "Mantova": "AC Mantova",
    "Mantova (1911-1956)": "AC Mantova", "Milan": "AC Milan", "Modena": "Modena FC",
    "Monza": "AC Monza", "Napoli": "SSC Napoli", "Novara": "Novara Calcio",
    "Padova": "Calcio Padova", "Palermo": "US Palermo", "Parma": "Parma FC",
    "Piacenza": "Piacenza Calcio", "Pisa": "Pisa SC", "Pistoiese": "AC Pistoiese",
    "Pro Patria": "Pro Patria", "Pro Vercelli": "Pro Vercelli", "Reggiana": "AC Reggiana",
    "Roma": "AS Roma", "SPAL": "SPAL 1907 Ferrara", "Salernitana": "Salernitana Calcio 1919",
    "Salernitanaudax": "Salernitana Calcio 1919", "Sampierdarenese": "Sampierdarenese", "Spezia": "Spezia Calcio",
    "Torino": "Torino FC", "Treviso": "Treviso FBC", "Triestina": "Unione Triestina",
    "Udinese": "Udinese Calcio", "Varese": "AS Varese 1910", "Venezia": "AC Venezia",
    "Venezia (1907-1987)": "AC Venezia", "Verona": "Hellas Verona", "Vicenza": "Vicenza Calcio",
}
MODELOS_IT.update({m: m for m in CLUBES if m not in MODELOS_IT and m in _ANTIGOS})

ALIASES: dict[str, str] = {
    # o mesmo clube com outro nome no engsoccerdata
    "Genova 1893 Circolo del Calcio": "Genoa CFC", "AC Liguria": "Sampierdarenese", "Lanerossi Vicenza": "Vicenza Calcio",
    "US Livorno": "AS Livorno", "Parma AC": "Parma FC", "FC Messina": "A.C.R. Messina", "US Anconitana": "Ancona Calcio",
    "Salernitana Sport": "Salernitana Calcio 1919",
    # nomes de época (Wikipédia, RSSSF)
    "Ambrosiana": "Inter", "Ambrosiana-Inter": "Inter", "Internazionale": "Inter", "Inter Milan": "Inter",
    "FC Internazionale": "Inter", "Milano": "AC Milan", "Juventus Cisitalia": "Juventus", "Genova 1893": "Genoa CFC",
    "Genova": "Genoa CFC", "Liguria": "Sampierdarenese", "Pro Livorno": "AS Livorno", "Lanerossi": "Vicenza Calcio",
    "L.R. Vicenza": "Vicenza Calcio", "Hellas Verona": "Hellas Verona", "Anconitana": "Ancona Calcio",
    "Palermo": "US Palermo", "Spal": "SPAL 1907 Ferrara",
}

# nomes que dependem da época: nome -> [(primeiro ano, último ano, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {chave(v[0]): k for k, v in CLUBES.items()}   # o nome de exibição também serve ("Napoli")
_INDICE.update({chave(k): k for k in CLUBES})
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}

# siglas e palavras que a RSSSF e a ESPN põem em volta do nome ("Juventus FC", "SS Lazio", "US Città di Palermo")
SIGLAS = {"ac", "acf", "as", "fc", "fbc", "ss", "ssc", "us", "uc", "bc", "cfc", "sc", "ssd", "calcio", "citta", "di", "de",
          "spa", "football", "club", "1907", "1909", "1910", "1912", "1913", "1919", "1893"}


def _reduzir(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return "".join(w for w in re.split(r"[^a-z0-9]+", s.replace(".", "")) if w and w not in SIGLAS)


_REDUZIDO: dict[str, str] = {}
for _nome, _c in [(k, k) for k in CLUBES] + [(v[0], k) for k, v in CLUBES.items()] + list(ALIASES.items()):
    _REDUZIDO.setdefault(_reduzir(_nome), _c)


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que
    dependem da época."""
    k = chave(nome.strip().rstrip("*").strip())
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k) or _REDUZIDO.get(_reduzir(nome))


def exibicao(chave_clube: str) -> str:
    return CLUBES[chave_clube][0]
