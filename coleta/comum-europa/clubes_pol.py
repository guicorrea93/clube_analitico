"""Cadastro dos clubes poloneses (pol-1).

Chave: o nome de exibição no painel (como o clube é conhecido no Brasil, com Varsóvia e Cracóvia em português: "Legia
Varsóvia", "Wisła Cracóvia"), com cidade e país. Nomes únicos no mundo, conferidos no banco e nos outros pacotes.

Identidade: pelo alvo do link da Wikipédia em cada temporada (LINKS), seguindo os redirecionamentos (25/11/2026):
Petrochemia e Orlen Płock = Wisła Płock; Unia Chorzów = Ruch Chorzów; Gwardia Kraków = Wisła; KKS Poznań e Kolejarz =
Lech; Sokół Tychy = GKS Tychy; Energetyk ROW = ROW Rybnik; LKS Nieciecza = Termalica; Stomil = OKS Olsztyn; as três
Cracovia e as duas Warszawianka; o 22 pp Siedlce, que virou Strzelec Siedlce (RSSSF). Clubes de Lwów e Wilno (hoje Ucrânia e Lituânia) com o país de hoje.

Nas fontes sem link: OGOL (código do ogol -> chave) e PADROES (nome normalizado -> chave), para o football-data e os jogos
avulsos da RSSSF.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "Legia Varsóvia": ("Varsóvia", "POL"), "Polonia Varsóvia": ("Varsóvia", "POL"), "Gwardia Varsóvia": ("Varsóvia", "POL"),
    "Warszawianka": ("Varsóvia", "POL"), "Wisła Cracóvia": ("Cracóvia", "POL"), "Cracovia": ("Cracóvia", "POL"),
    "Garbarnia Cracóvia": ("Cracóvia", "POL"), "Hutnik Cracóvia": ("Cracóvia", "POL"), "Wawel Cracóvia": ("Cracóvia", "POL"),
    "Podgórze Cracóvia": ("Cracóvia", "POL"), "Jutrzenka Cracóvia": ("Cracóvia", "POL"), "Wieczysta Cracóvia": ("Cracóvia", "POL"),
    "Lech Poznań": ("Poznań", "POL"), "Warta Poznań": ("Poznań", "POL"), "Olimpia Poznań": ("Poznań", "POL"),
    "Ruch Chorzów": ("Chorzów", "POL"), "AKS Chorzów": ("Chorzów", "POL"), "Górnik Zabrze": ("Zabrze", "POL"),
    "ŁKS Łódź": ("Łódź", "POL"), "Widzew Łódź": ("Łódź", "POL"), "Turyści Łódź": ("Łódź", "POL"), "ŁTSG Łódź": ("Łódź", "POL"),
    "Polonia Bytom": ("Bytom", "POL"), "Szombierki Bytom": ("Bytom", "POL"), "Pogoń Szczecin": ("Szczecin", "POL"),
    "Arkonia Szczecin": ("Szczecin", "POL"), "Śląsk Wrocław": ("Wrocław", "POL"), "Lechia Gdańsk": ("Gdańsk", "POL"),
    "Olimpia-Lechia Gdańsk": ("Gdańsk", "POL"), "Gedania Gdańsk": ("Gdańsk", "POL"), "Arka Gdynia": ("Gdynia", "POL"),
    "Bałtyk Gdynia": ("Gdynia", "POL"), "Zagłębie Sosnowiec": ("Sosnowiec", "POL"), "Zagłębie Lubin": ("Lubin", "POL"),
    "Zagłębie Wałbrzych": ("Wałbrzych", "POL"), "Górnik Wałbrzych": ("Wałbrzych", "POL"), "GKS Katowice": ("Katowice", "POL"),
    "1. FC Kattowitz": ("Katowice", "POL"), "Dąb Katowice": ("Katowice", "POL"), "Gwardia Katowice": ("Katowice", "POL"),
    "Jagiellonia Białystok": ("Białystok", "POL"), "Raków Częstochowa": ("Częstochowa", "POL"),
    "Skra Częstochowa": ("Częstochowa", "POL"), "Piast Gliwice": ("Gliwice", "POL"), "Korona Kielce": ("Kielce", "POL"),
    "Wisła Płock": ("Płock", "POL"), "Stal Mielec": ("Mielec", "POL"), "Stal Rzeszów": ("Rzeszów", "POL"),
    "Stal Stalowa Wola": ("Stalowa Wola", "POL"), "Odra Opole": ("Opole", "POL"), "Odra Wodzisław": ("Wodzisław Śląski", "POL"),
    "Zawisza Bydgoszcz": ("Bydgoszcz", "POL"), "Polonia Bydgoszcz": ("Bydgoszcz", "POL"), "Motor Lublin": ("Lublin", "POL"),
    "Lublinianka": ("Lublin", "POL"), "Radomiak Radom": ("Radom", "POL"), "GKS Tychy": ("Tychy", "POL"),
    "ROW Rybnik": ("Rybnik", "POL"), "Rymer Rybnik": ("Rybnik", "POL"), "Górnik Radlin": ("Radlin", "POL"),
    "Unia Racibórz": ("Racibórz", "POL"), "GKS Jastrzębie": ("Jastrzębie-Zdrój", "POL"), "Igloopol Dębica": ("Dębica", "POL"),
    "Siarka Tarnobrzeg": ("Tarnobrzeg", "POL"), "Sokół Pniewy": ("Pniewy", "POL"), "Stomil Olsztyn": ("Olsztyn", "POL"),
    "KKS Olsztyn": ("Olsztyn", "POL"), "Amica Wronki": ("Wronki", "POL"), "GKS Bełchatów": ("Bełchatów", "POL"),
    "Dyskobolia": ("Grodzisk Wielkopolski", "POL"), "KSZO Ostrowiec": ("Ostrowiec Świętokrzyski", "POL"),
    "Ruch Radzionków": ("Radzionków", "POL"), "RKS Radomsko": ("Radomsko", "POL"), "Szczakowianka": ("Jaworzno", "POL"),
    "Górnik Łęczna": ("Łęczna", "POL"), "Górnik Polkowice": ("Polkowice", "POL"), "Świt Nowy Dwór": ("Nowy Dwór Mazowiecki", "POL"),
    "Podbeskidzie": ("Bielsko-Biała", "POL"), "Termalica Nieciecza": ("Nieciecza", "POL"), "Sandecja Nowy Sącz": ("Nowy Sącz", "POL"),
    "Miedź Legnica": ("Legnica", "POL"), "Puszcza Niepołomice": ("Niepołomice", "POL"), "TKS Toruń": ("Toruń", "POL"),
    "Pomorzanin Toruń": ("Toruń", "POL"), "Śląsk Świętochłowice": ("Świętochłowice", "POL"),
    "Strzelec Siedlce": ("Siedlce", "POL"), "Pogoń Siedlce": ("Siedlce", "POL"), "Polonia Świdnica": ("Świdnica", "POL"),
    "Glinik Gorlice": ("Gorlice", "POL"), "Czuwaj Przemyśl": ("Przemyśl", "POL"), "Tarnovia Tarnów": ("Tarnów", "POL"),
    "Iskra Siemianowice": ("Siemianowice Śląskie", "POL"), "Tęcza Kielce": ("Kielce", "POL"), "ZZK Łódź": ("Łódź", "POL"),
    "Burza Wrocław": ("Wrocław", "POL"),
    # hoje na Ucrânia (Lviv) e na Lituânia (Vilnius)
    "Pogoń Lwów": ("Lviv", "UKR"), "Czarni Lwów": ("Lviv", "UKR"), "Hasmonea Lwów": ("Lviv", "UKR"), "Lechia Lwów": ("Lviv", "UKR"),
    "Śmigły Wilno": ("Vilnius", "LTU"), "Lauda Wilno": ("Vilnius", "LTU"), "Pogoń Wilno": ("Vilnius", "LTU"),
    "Strzelec Wilno": ("Vilnius", "LTU"), "1 PP Leg. Wilno": ("Vilnius", "LTU"),
}

LINKS = {
    "KS Cracovia (football)": "Cracovia", "Cracovia (football club)": "Cracovia", "KS Cracovia": "Cracovia",
    "Polonia Warsaw": "Polonia Varsóvia", "Warta Poznań": "Warta Poznań", "Pogoń Lwów (1904)": "Pogoń Lwów",
    "Pogoń Lwów": "Pogoń Lwów", "ŁKS Łódź": "ŁKS Łódź", "KS Lublinianka": "Lublinianka", "Ruch Chorzów": "Ruch Chorzów",
    "Unia Chorzów": "Ruch Chorzów", "Wisła Kraków": "Wisła Cracóvia", "TKS Toruń": "TKS Toruń", "AKS Chorzów": "AKS Chorzów",
    "Union Touring Łódź": "Turyści Łódź", "Klub Turystów Łódź": "Turyści Łódź", "1. FC Kattowitz": "1. FC Kattowitz",
    "Legia Warsaw": "Legia Varsóvia", "Legia Warsaw (football)": "Legia Varsóvia", "Czarni Lwów": "Czarni Lwów",
    "Hasmonea Lwów": "Hasmonea Lwów", "KS Warszawianka": "Warszawianka", "Warszawianka Warszawa": "Warszawianka",
    "Jutrzenka Kraków": "Jutrzenka Cracóvia", "Śląsk Świętochłowice": "Śląsk Świętochłowice",
    "Garbarnia Kraków": "Garbarnia Cracóvia", "ŁTSG Łódź": "ŁTSG Łódź", "Lechia Lwów": "Lechia Lwów",
    "WKS 22 pp Siedlce": "Strzelec Siedlce", "22 pp Siedlce": "Strzelec Siedlce", "Podgórze Kraków": "Podgórze Cracóvia",
    "Śmigły Wilno": "Śmigły Wilno", "Strzelec Siedlce": "Strzelec Siedlce", "Dąb Katowice": "Dąb Katowice",
    "Polonia Bytom": "Polonia Bytom", "Lech Poznań": "Lech Poznań", "Polonia Świdnica": "Polonia Świdnica",
    "Szombierki Bytom": "Szombierki Bytom", "Skra Częstochowa": "Skra Częstochowa", "MKP Pogoń Siedlce": "Pogoń Siedlce",
    "Jagiellonia Białystok": "Jagiellonia Białystok", "Zagłębie Sosnowiec": "Zagłębie Sosnowiec",
    "Radomiak Radom": "Radomiak Radom", "Gedania Danzig": "Gedania Gdańsk", "Gedania 1922 Gdańsk": "Gedania Gdańsk", "Glinik Gorlice": "Glinik Gorlice",
    "Gwardia Warszawa": "Gwardia Varsóvia", "Gwardia Warsaw": "Gwardia Varsóvia", "Czuwaj Przemyśl": "Czuwaj Przemyśl",
    "Gwardia Katowice": "Gwardia Katowice", "Pogoń Szczecin": "Pogoń Szczecin", "Tarnovia Tarnów": "Tarnovia Tarnów",
    "Rymer Rybnik": "Rymer Rybnik", "Widzew Łódź": "Widzew Łódź", "Lechia Gdańsk": "Lechia Gdańsk",
    "Górnik Radlin": "Górnik Radlin", "Arkonia Szczecin": "Arkonia Szczecin", "Wawel Kraków": "Wawel Cracóvia",
    "Odra Opole": "Odra Opole", "Polonia Bydgoszcz": "Polonia Bydgoszcz", "Górnik Zabrze": "Górnik Zabrze",
    "Stal Mielec": "Stal Mielec", "FKS Stal Mielec": "Stal Mielec", "Zawisza Bydgoszcz": "Zawisza Bydgoszcz",
    "Stal Rzeszów (football)": "Stal Rzeszów", "KP Unia Racibórz": "Unia Racibórz", "Śląsk Wrocław": "Śląsk Wrocław",
    "GKS Katowice": "GKS Katowice", "Zagłębie Wałbrzych": "Zagłębie Wałbrzych", "Energetyk ROW Rybnik": "ROW Rybnik",
    "KS ROW 1964 Rybnik": "ROW Rybnik", "GKS Tychy": "GKS Tychy", "Sokół Tychy": "GKS Tychy", "Arka Gdynia": "Arka Gdynia",
    "Bałtyk Gdynia": "Bałtyk Gdynia", "Motor Lublin": "Motor Lublin", "Górnik Wałbrzych": "Górnik Wałbrzych",
    "Zagłębie Lubin": "Zagłębie Lubin", "Olimpia Poznań": "Olimpia Poznań", "Stal Stalowa Wola": "Stal Stalowa Wola",
    "GKS Jastrzębie": "GKS Jastrzębie", "Hutnik Kraków": "Hutnik Cracóvia", "Igloopol Dębica": "Igloopol Dębica",
    "Siarka Tarnobrzeg": "Siarka Tarnobrzeg", "Miliarder Pniewy": "Sokół Pniewy", "Raków Częstochowa": "Raków Częstochowa",
    "OKS 1945 Olsztyn": "Stomil Olsztyn", "Petrochemia Płock": "Wisła Płock", "Orlen Płock": "Wisła Płock",
    "Wisła Płock": "Wisła Płock", "Amica Wronki": "Amica Wronki", "GKS Bełchatów": "GKS Bełchatów",
    "Olimpia/Lechia Gdańsk": "Olimpia-Lechia Gdańsk", "Odra Wodzisław": "Odra Wodzisław",
    "Dyskobolia Grodzisk Wielkopolski": "Dyskobolia", "KSZO Ostrowiec Świętokrzyski": "KSZO Ostrowiec",
    "Ruch Radzionków": "Ruch Radzionków", "RKS Radomsko": "RKS Radomsko", "Szczakowianka Jaworzno": "Szczakowianka",
    "Górnik Łęczna": "Górnik Łęczna", "Górnik Polkowice": "Górnik Polkowice", "Świt Nowy Dwór Mazowiecki": "Świt Nowy Dwór",
    "Korona Kielce": "Korona Kielce", "Piast Gliwice": "Piast Gliwice", "Podbeskidzie Bielsko-Biała": "Podbeskidzie",
    "LKS Nieciecza": "Termalica Nieciecza", "Bruk-Bet Termalica Nieciecza": "Termalica Nieciecza",
    "Sandecja Nowy Sącz": "Sandecja Nowy Sącz", "Miedź Legnica": "Miedź Legnica", "Puszcza Niepołomice": "Puszcza Niepołomice",
}

OGOL = {
    "101406": "Arkonia Szczecin", "108125": "Górnik Łęczna", "10827": "GKS Tychy", "10835": "Zagłębie Wałbrzych",
    "10843": "Stal Rzeszów", "1089": "GKS Katowice", "1090": "Dyskobolia", "1091": "Wisła Płock", "13168": "RKS Radomsko",
    "13696": "Piast Gliwice", "154": "Wisła Cracóvia", "15618": "Warta Poznań", "18766": "Szczakowianka",
    "18767": "Stal Stalowa Wola", "19080": "Siarka Tarnobrzeg", "19183": "GKS Jastrzębie", "19287": "Radomiak Radom",
    "19288": "Zawisza Bydgoszcz", "19341": "Sokół Pniewy", "19626": "Podbeskidzie", "2048": "Amica Wronki",
    "2049": "Legia Varsóvia", "2051": "Górnik Zabrze", "2052": "Odra Wodzisław", "2054": "Polonia Varsóvia",
    "2055": "Widzew Łódź", "2056": "Górnik Polkowice", "2057": "Świt Nowy Dwór", "20886": "Bałtyk Gdynia",
    "21024": "Ruch Radzionków", "21080": "Sandecja Nowy Sącz", "248180": "Wieczysta Cracóvia", "27526": "Górnik Wałbrzych",
    "30241": "Stomil Olsztyn", "30912": "Unia Racibórz", "31021": "Termalica Nieciecza", "39635": "Igloopol Dębica",
    "4257": "Cracovia", "4258": "Pogoń Szczecin", "4259": "Zagłębie Lubin", "44206": "Puszcza Niepołomice",
    "5215": "Olimpia Poznań", "5884": "Arka Gdynia", "5885": "GKS Bełchatów", "5886": "Korona Kielce",
    "7787": "Śląsk Wrocław", "7836": "ŁKS Łódź", "7846": "Stal Mielec", "8364": "Hutnik Cracóvia", "8483": "KSZO Ostrowiec",
    "8885": "Motor Lublin", "8886": "Lechia Gdańsk", "8887": "Miedź Legnica", "9017": "Odra Opole", "9018": "ROW Rybnik",
    "9020": "Gwardia Varsóvia", "9093": "Jagiellonia Białystok", "9159": "Zagłębie Sosnowiec", "9359": "Ruch Chorzów",
    "9376": "Szombierki Bytom", "9443": "Polonia Bytom", "lech-poznan": "Lech Poznań", "rks-rakow": "Raków Częstochowa",
    "61081": "ŁKS Łódź", "19359": "GKS Katowice",   # conferidos pela tabela da Wikipédia de cada temporada
}

# código do ogol que vale outro clube numa temporada (conferido com a tabela e a matriz da Wikipédia)
OGOL_TEMPORADA = {
    ("10835", "1985/86"): "Zagłębie Sosnowiec",   # o ogol rotula "Zagłębie Wałbrzych"; os 30 placares são os do Sosnowiec
    ("8886", "1995/96"): "Olimpia-Lechia Gdańsk",   # a fusão do Olimpia Poznań com o Lechia (artigo próprio na Wikipédia)
}

# (expressão sobre o nome normalizado: minúsculas, sem acento) -> chave; a primeira que casa vale
PADROES: list[tuple[str, str]] = [
    (r"^legia|cwks", "Legia Varsóvia"), (r"polonia (warsz|warsaw)|^polonia$", "Polonia Varsóvia"),
    (r"gwardia (warsz|warsaw)|^gwardia$", "Gwardia Varsóvia"), (r"warszawianka", "Warszawianka"),
    (r"wisla p|plock|petrochemia|orlen", "Wisła Płock"), (r"^wisla|gwardia krak", "Wisła Cracóvia"), (r"cracovia", "Cracovia"),
    (r"garbarnia", "Garbarnia Cracóvia"), (r"hutnik", "Hutnik Cracóvia"), (r"wawel", "Wawel Cracóvia"),
    (r"podgorze", "Podgórze Cracóvia"), (r"jutrzenka", "Jutrzenka Cracóvia"), (r"wieczysta", "Wieczysta Cracóvia"),
    (r"^lech( |$)|kks poznan|kolejarz poznan", "Lech Poznań"), (r"warta", "Warta Poznań"), (r"olimpia poznan", "Olimpia Poznań"),
    (r"^akr?s chorzow|^aks", "AKS Chorzów"), (r"ruch radz", "Ruch Radzionków"), (r"^ruch|unia chorzow", "Ruch Chorzów"),
    (r"gornik z", "Górnik Zabrze"), (r"gornik walb", "Górnik Wałbrzych"), (r"gornik lecz|^leczna", "Górnik Łęczna"),
    (r"gornik polk", "Górnik Polkowice"), (r"gornik radl", "Górnik Radlin"), (r"widzew", "Widzew Łódź"),
    (r"^l?ks( ptak)? lodz|^lodzki|^lks$", "ŁKS Łódź"), (r"turys|union touring", "Turyści Łódź"),
    (r"polonia bytom|ogniwo bytom", "Polonia Bytom"), (r"szombierki", "Szombierki Bytom"), (r"pogon szcz|^pogon$|pks szczecin", "Pogoń Szczecin"),
    (r"pogon lw", "Pogoń Lwów"), (r"arkonia", "Arkonia Szczecin"), (r"slask wroc|^slask$", "Śląsk Wrocław"),
    (r"lechia gd|^lechia$", "Lechia Gdańsk"), (r"arka", "Arka Gdynia"), (r"baltyk", "Bałtyk Gdynia"),
    (r"zaglebie s|sosnowiec", "Zagłębie Sosnowiec"), (r"zaglebie l|^zaglebie$", "Zagłębie Lubin"),
    (r"zaglebie w", "Zagłębie Wałbrzych"), (r"gks kat|^gks katowice", "GKS Katowice"), (r"jagiellonia", "Jagiellonia Białystok"),
    (r"rakow", "Raków Częstochowa"), (r"piast", "Piast Gliwice"), (r"korona", "Korona Kielce"), (r"stal miel|^stal$", "Stal Mielec"),
    (r"stal rzesz", "Stal Rzeszów"), (r"stal stal", "Stal Stalowa Wola"), (r"odra op", "Odra Opole"), (r"odra wodz", "Odra Wodzisław"),
    (r"zawisza", "Zawisza Bydgoszcz"), (r"motor lub", "Motor Lublin"), (r"radomiak", "Radomiak Radom"),
    (r"gks tychy|sokol tychy", "GKS Tychy"), (r"row rybnik", "ROW Rybnik"), (r"belchatow", "GKS Bełchatów"),
    (r"podbeskidzie", "Podbeskidzie"), (r"termalica|nieciecza", "Termalica Nieciecza"), (r"sandecja", "Sandecja Nowy Sącz"),
    (r"legnica|miedz", "Miedź Legnica"), (r"puszcza", "Puszcza Niepołomice"), (r"lublinianka|wks lublin", "Lublinianka"),
]

# nomes sem link nas tabelas e fichas da Wikipédia (nome visível -> chave)
VISIVEIS = {
    "Strzelec Wilno": "Strzelec Wilno", "Lauda Wilno": "Lauda Wilno", "Iskra Siemianowice": "Iskra Siemianowice",
    "Pogoń Wilno": "Pogoń Wilno", "WKS 1 ppLeg Wilno": "1 PP Leg. Wilno", "Polonia Warsaw": "Polonia Varsóvia",
    "Rymer Niedobczyce": "Rymer Rybnik", "Pomorzanin Toruń": "Pomorzanin Toruń", "ZZK Łódź": "ZZK Łódź",
    "Tęcza Kielce": "Tęcza Kielce", "KKS Olsztyn": "KKS Olsztyn", "Burza Wrocław": "Burza Wrocław",
    "RKU Sosnowiec": "Zagłębie Sosnowiec",
}


def _normal(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.replace("ł", "l").replace("Ł", "L")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]", " ", s)).strip()


_INDICE = {_normal(k): k for k in CLUBES}
_PADROES = [(re.compile(p), c) for p, c in PADROES]


def link(alvo: str | None) -> str | None:
    return LINKS.get((alvo or "").strip())


def esd(nome: str) -> str | None:
    n = _normal(nome)
    if n in _INDICE:
        return _INDICE[n]
    for p, c in _PADROES:
        if p.search(n):
            return c
    return None


def ogol(codigo: str, temporada: str | None = None) -> str | None:
    return OGOL_TEMPORADA.get((codigo, temporada)) or OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
