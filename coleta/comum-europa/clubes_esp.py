"""Cadastro dos clubes espanhóis, comum a todas as divisões da Espanha.

Chave: o nome do engsoccerdata. Valor: nome de exibição no painel (como o clube é conhecido no Brasil), cidade e
país (código FIFA). O mesmo clube tem o mesmo nome em esp-1, esp-2...

Clubes que o engsoccerdata separa ficam separados: CD Málaga (até 1992) e Málaga CF (o sucessor, de 1994);
AD Almería (1971-1982) e UD Almería (1989); Burgos CF (1946-1983) e Real Burgos (1983-1995).
"Athletic Club" já é o clube de São João del-Rei (MG): o de Bilbao fica "Athletic Bilbao".

ALIASES: outras grafias (RSSSF, football-data, ESPN, Wikipédia) -> chave do engsoccerdata. O ogol e a ESPN
são casados pelo código do clube (votação jogo a jogo em importar.py), não por aqui.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "AD Almeria": ("AD Almería", "Almería", "ESP"),
    "Albacete": ("Albacete", "Albacete", "ESP"),
    "Arenas de Getxo": ("Arenas de Getxo", "Getxo", "ESP"),
    "Athletic Bilbao": ("Athletic Bilbao", "Bilbao", "ESP"),
    "Atletico Madrid": ("Atlético de Madrid", "Madri", "ESP"),
    "Atletico Tetuan": ("Atlético Tetuán", "Tetuán", "ESP"),       # Marrocos espanhol (protetorado) em 1951/52
    "Burgos CF": ("Burgos", "Burgos", "ESP"),
    "CA Osasuna": ("Osasuna", "Pamplona", "ESP"),
    "CD Alaves": ("Alavés", "Vitoria-Gasteiz", "ESP"),
    "CD Alcoyano": ("Alcoyano", "Alcoy", "ESP"),
    "CD Castellon": ("Castellón", "Castellón de la Plana", "ESP"),
    "CD Condal": ("Condal", "Barcelona", "ESP"),
    "CD Leganes": ("Leganés", "Leganés", "ESP"),
    "CD Leonesa": ("Cultural Leonesa", "León", "ESP"),
    "CD Logrones": ("Logroñés", "Logroño", "ESP"),
    "CD Malaga": ("CD Málaga", "Málaga", "ESP"),
    "CD Numancia": ("Numancia", "Soria", "ESP"),
    "CD Tenerife": ("Tenerife", "Santa Cruz de Tenerife", "ESP"),
    "CE Europa": ("Europa", "Barcelona", "ESP"),
    "CE Sabadell": ("Sabadell", "Sabadell", "ESP"),
    "CF Extremadura": ("Extremadura", "Almendralejo", "ESP"),
    "CP Merida": ("Mérida", "Mérida", "ESP"),
    "Cadiz CF": ("Cádiz", "Cádiz", "ESP"),
    "Celta Vigo": ("Celta", "Vigo", "ESP"),
    "Cordoba CF": ("Córdoba", "Córdoba", "ESP"),
    "Deportivo La Coruna": ("Deportivo La Coruña", "La Coruña", "ESP"),
    "Elche CF": ("Elche", "Elche", "ESP"),
    "Espanyol Barcelona": ("Espanyol", "Barcelona", "ESP"),
    "FC Barcelona": ("Barcelona", "Barcelona", "ESP"),
    "Getafe CF": ("Getafe", "Getafe", "ESP"),
    "Gimnastic": ("Gimnàstic", "Tarragona", "ESP"),
    "Girona": ("Girona", "Girona", "ESP"),
    "Granada CF": ("Granada", "Granada", "ESP"),
    "Hercules CF": ("Hércules", "Alicante", "ESP"),
    "Levante UD": ("Levante", "Valência", "ESP"),
    "Malaga CF": ("Málaga", "Málaga", "ESP"),
    "Pontevedra CF": ("Pontevedra", "Pontevedra", "ESP"),
    "RCD Mallorca": ("Mallorca", "Palma de Mallorca", "ESP"),
    "Racing Santander": ("Racing Santander", "Santander", "ESP"),
    "Rayo Vallecano": ("Rayo Vallecano", "Madri", "ESP"),
    "Real Betis": ("Betis", "Sevilha", "ESP"),
    "Real Burgos": ("Real Burgos", "Burgos", "ESP"),
    "Real Jaen": ("Jaén", "Jaén", "ESP"),
    "Real Madrid": ("Real Madrid", "Madri", "ESP"),
    "Real Murcia": ("Murcia", "Múrcia", "ESP"),
    "Real Oviedo": ("Real Oviedo", "Oviedo", "ESP"),
    "Real Sociedad": ("Real Sociedad", "San Sebastián", "ESP"),
    "Real Union": ("Real Unión", "Irún", "ESP"),
    "Real Valladolid": ("Valladolid", "Valladolid", "ESP"),
    "Real Zaragoza": ("Zaragoza", "Zaragoza", "ESP"),
    "Recreativo Huelva": ("Recreativo Huelva", "Huelva", "ESP"),
    "SD Compostela": ("Compostela", "Santiago de Compostela", "ESP"),
    "SD Eibar": ("Eibar", "Eibar", "ESP"),
    "SD Huesca": ("Huesca", "Huesca", "ESP"),
    "Sevilla FC": ("Sevilla", "Sevilha", "ESP"),
    "Sporting Gijon": ("Sporting de Gijón", "Gijón", "ESP"),
    "UD Almeria": ("Almería", "Almería", "ESP"),
    "UD Las Palmas": ("Las Palmas", "Las Palmas de Gran Canaria", "ESP"),
    "UD Salamanca": ("Salamanca", "Salamanca", "ESP"),
    "UE Lleida": ("Lleida", "Lleida", "ESP"),
    "Valencia CF": ("Valencia", "Valência", "ESP"),
    "Villarreal CF": ("Villarreal", "Vila-real", "ESP"),
    "Xerez CD": ("Xerez", "Jerez de la Frontera", "ESP"),
}

# grafias de outras fontes -> chave do engsoccerdata
ALIASES: dict[str, str] = {
    # nomes antigos (RSSSF e Wikipédia)
    "Athletic de Bilbao": "Athletic Bilbao", "Atletico Bilbao": "Athletic Bilbao", "Athletic Club": "Athletic Bilbao",
    "Athletic Madrid": "Atletico Madrid", "Atletico de Madrid": "Atletico Madrid", "Atletico Aviacion": "Atletico Madrid",
    "Madrid FC": "Real Madrid", "Real Madrid CF": "Real Madrid", "Donostia": "Real Sociedad",
    "Donostia San Sebastian": "Real Sociedad", "Real Santander": "Racing Santander", "Racing de Santander": "Racing Santander",
    "Racing": "Racing Santander",
    "Real Gijon": "Sporting Gijon", "Sporting de Gijon": "Sporting Gijon", "Union Club": "Real Union",
    "Real Union de Irun": "Real Union", "Arenas": "Arenas de Getxo", "Arenas de Guecho": "Arenas de Getxo",
    "Arenas Club de Guecho": "Arenas de Getxo", "Europa": "CE Europa", "CD Europa": "CE Europa",
    "CD Europa de Barcelona": "CE Europa", "Espanol": "Espanyol Barcelona", "RCD Espanol": "Espanyol Barcelona",
    "RCD Espaqol": "Espanyol Barcelona", "RCD Espanyol": "Espanyol Barcelona", "Espanyol": "Espanyol Barcelona",
    "Atletico Osasuna": "CA Osasuna", "Osasuna": "CA Osasuna", "Deportivo Alaves": "CD Alaves", "Alaves": "CD Alaves",
    "RC Celta": "Celta Vigo", "Celta": "Celta Vigo", "Celta de Vigo": "Celta Vigo", "RC Deportivo": "Deportivo La Coruna",
    "Deportivo de La Coruna": "Deportivo La Coruna", "Deportivo": "Deportivo La Coruna", "La Coruna": "Deportivo La Coruna",
    "Gimnastico": "Gimnastic", "Gimnastico de Tarragona": "Gimnastic", "Club Gimnastic de Tarragona": "Gimnastic",
    "Gimnastic de Tarragona": "Gimnastic", "Merida CP": "CP Merida", "Merida": "CP Merida", "UD Lerida": "UE Lleida",
    "Lerida": "UE Lleida", "Lleida": "UE Lleida", "Recreativo": "Recreativo Huelva", "Recreativo de Huelva": "Recreativo Huelva",
    "RC Recreativo de Huelva": "Recreativo Huelva", "Albacete Balompie": "Albacete", "Girona FC": "Girona",
    "Real Betis Balompie": "Real Betis", "Betis": "Real Betis", "Real Murcia CF": "Real Murcia", "Murcia": "Real Murcia",
    "Cultural Leonesa": "CD Leonesa", "Numancia": "CD Numancia", "Sabadell": "CE Sabadell", "CD Sabadell": "CE Sabadell",
    "Villarreal": "Villarreal CF", "Villareal": "Villarreal CF", "Oviedo": "Real Oviedo", "Valladolid": "Real Valladolid",
    "Zaragoza": "Real Zaragoza", "Sevilla": "Sevilla FC", "Valencia": "Valencia CF", "Barcelona": "FC Barcelona",
    "Granada": "Granada CF", "Hercules": "Hercules CF", "Elche": "Elche CF", "Castellon": "CD Castellon", "Cadiz": "Cadiz CF",
    "Cordoba": "Cordoba CF", "Levante": "Levante UD", "Mallorca": "RCD Mallorca", "Las Palmas": "UD Las Palmas",
    "Salamanca": "UD Salamanca", "Tenerife": "CD Tenerife", "Jaen": "Real Jaen", "Pontevedra": "Pontevedra CF",
    "Condal": "CD Condal", "Alcoyano": "CD Alcoyano", "Getafe": "Getafe CF", "Leganes": "CD Leganes", "Eibar": "SD Eibar",
    "Huesca": "SD Huesca", "Compostela": "SD Compostela", "Extremadura": "CF Extremadura", "Logrones": "CD Logrones",
    "Xerez": "Xerez CD", "Atletico Tetuan": "Atletico Tetuan",
    # football-data.co.uk
    "Ath Bilbao": "Athletic Bilbao", "Ath Madrid": "Atletico Madrid", "Santander": "Racing Santander",
    "Sp Gijon": "Sporting Gijon", "Vallecano": "Rayo Vallecano", "Sociedad": "Real Sociedad",
}

# nomes que dependem da época: nome -> [(primeiro ano, último ano, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "Malaga": [(0, 1993, "CD Malaga"), (1994, 9999, "Malaga CF")],
    "Almeria": [(0, 1985, "AD Almeria"), (1986, 9999, "UD Almeria")],
    "Burgos": [(0, 1983, "Burgos CF"), (1984, 1995, "Real Burgos")],
    # 1941/42: o Hércules jogou com o nome de Alicante CF
    "Alicante CF": [(1941, 1941, "Hercules CF")], "Alicante": [(1941, 1941, "Hercules CF")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {}


def _indexar() -> None:
    _INDICE.clear()
    _INDICE.update({chave(k): k for k in CLUBES})
    _INDICE.update({chave(k): v for k, v in ALIASES.items()})


_indexar()


_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave do engsoccerdata (None se não conhecer). `ano` (início da temporada) resolve os
    nomes que dependem da época ("Málaga", "Almería", "Burgos")."""
    k = chave(nome.strip().rstrip("*").strip())
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k)


def exibicao(nome_esd: str) -> str:
    return CLUBES[nome_esd][0]
