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
