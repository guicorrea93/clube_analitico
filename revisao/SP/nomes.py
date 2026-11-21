"""Mapa de nomes da Wikipédia para os nomes do banco (Paulista)."""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import unicodedata

MAPA = {
    "spac": "São Paulo Athletic", "sao paulo athletic": "São Paulo Athletic", "paulistano": "Paulistano-SP",
    "sc internacional": "SC Internacional-SP", "s.c. internacional": "SC Internacional-SP",
    "sc americano": "Americano-SP", "s.c. americano": "Americano-SP", "a.a. das palmeiras": "AA das Palmeiras",
    "mackenzie": "Mackenzie-SP", "ypiranga": "Ypiranga-SP", "a.a. sao bento": "AA São Bento",
    "campos eliseos": "Campos Elyseos", "palestra italia": "Palmeiras", "auto": "Auto Audax", "hespanha": "Jabaquara",
    "sao jose": "São José-SP", "novorizontino": "GE Novorizontino", "gremio novorizontino": "GE Novorizontino",
    "botafogo": "Botafogo-SP", "audax": "Osasco Audax", "go audax": "Osasco Audax", "agua santa": "EC Água Santa",
    "minas gerais": "Minas Gerais FC", "luzitano": "Luzitano-SP", "alumni": "Alumni-SP", "sirio": "EC Sírio",
    "independencia": "Independência-SP", "estudantes": "Estudantes de São Paulo", "e.c. sao caetano": "São Caetano EC",
    "ferroviaria": "Ferroviária-SP", "e.c. sao bento": "São Bento", "red bull bragantino": "Bragantino",
    "sao paulo railway": "São Paulo Railway",
}


def chave(x):
    x = x.strip().lstrip("|").strip()
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower().strip()
    return x


def norm(x):
    k = chave(x)
    return MAPA.get(k, x.strip().lstrip("|").strip())


