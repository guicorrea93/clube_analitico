"""Cadastro dos clubes portugueses, comum a todas as divisões de Portugal.

Chave: o nome de exibição no painel (como o clube é conhecido no Brasil), com cidade e país. O nome é único no mundo,
conferido no banco e nos outros pacotes: "Nacional da Madeira" (há o Nacional do Uruguai), "Oriental de Lisboa" (há o
Oriental do Uruguai), "CD Feirense" (há o Feirense da Bahia), "Caldas SC" (há o Caldas de Goiás).

Clubes separados, como no ogol e na RSSSF:
- Belenenses (CF Os Belenenses, até 2017/18) e Belenenses SAD (a sociedade que se separou do clube em 2018 e jogou a
  1ª divisão de 2018/19 a 2021/22 como Belenenses SAD e B-SAD);
- AVS (AVS Futebol SAD, de Vila das Aves, criada em 2023) e Desportivo das Aves (CD Aves);
- SL Elvas (1945/46 e 1946/47) e O Elvas (O Elvas CAD, fundado em 1947);
- União de Lisboa, Unidos de Lisboa, União de Leiria, União da Madeira, União de Tomar e União de Coimbra;
- Académica (Coimbra), Académico do Porto e Académico de Viseu.
O Estrela da Amadora de hoje (fusão de 2020 com o Club Football Estrela) fica com a história do antigo, como no ogol.

OGOL: código do clube no ogol -> chave. ALIASES: grafias das outras fontes (RSSSF, football-data, engsoccerdata,
Wikipédia) -> chave. A ESPN é casada pelo código do clube (votação jogo a jogo em importar.py).
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "Benfica": ("Lisboa", "POR"),
    "Porto": ("Porto", "POR"),
    "Sporting": ("Lisboa", "POR"),
    "Belenenses": ("Lisboa", "POR"),
    "Belenenses SAD": ("Lisboa", "POR"),
    "Vitória de Setúbal": ("Setúbal", "POR"),
    "Vitória de Guimarães": ("Guimarães", "POR"),
    "Académica": ("Coimbra", "POR"),
    "Académico do Porto": ("Porto", "POR"),
    "Académico de Viseu": ("Viseu", "POR"),
    "União de Lisboa": ("Lisboa", "POR"),
    "Unidos de Lisboa": ("Lisboa", "POR"),
    "Carcavelinhos": ("Lisboa", "POR"),
    "Boavista": ("Porto", "POR"),
    "Leixões": ("Matosinhos", "POR"),
    "Barreirense": ("Barreiro", "POR"),
    "Casa Pia": ("Lisboa", "POR"),
    "Olhanense": ("Olhão", "POR"),
    "Leça": ("Leça da Palmeira", "POR"),
    "CUF": ("Barreiro", "POR"),
    "Atlético CP": ("Lisboa", "POR"),
    "Salgueiros": ("Porto", "POR"),
    "Estoril": ("Estoril", "POR"),
    "Oliveirense": ("Oliveira de Azeméis", "POR"),
    "SL Elvas": ("Elvas", "POR"),
    "O Elvas": ("Elvas", "POR"),
    "Famalicão": ("Vila Nova de Famalicão", "POR"),
    "Sanjoanense": ("São João da Madeira", "POR"),
    "Braga": ("Braga", "POR"),
    "Lusitano VRSA": ("Vila Real de Santo António", "POR"),
    "Lusitano de Évora": ("Évora", "POR"),
    "Sporting da Covilhã": ("Covilhã", "POR"),
    "Oriental de Lisboa": ("Lisboa", "POR"),
    "Torreense": ("Torres Vedras", "POR"),
    "Caldas SC": ("Caldas da Rainha", "POR"),
    "Beira-Mar": ("Aveiro", "POR"),
    "CD Feirense": ("Santa Maria da Feira", "POR"),
    "Varzim": ("Póvoa de Varzim", "POR"),
    "Seixal": ("Seixal", "POR"),
    "Tirsense": ("Santo Tirso", "POR"),
    "União de Tomar": ("Tomar", "POR"),
    "Farense": ("Faro", "POR"),
    "Montijo": ("Montijo", "POR"),
    "União de Coimbra": ("Coimbra", "POR"),
    "Espinho": ("Espinho", "POR"),
    "Portimonense": ("Portimão", "POR"),
    "Riopele": ("Pousada de Saramagos", "POR"),
    "Marítimo": ("Funchal", "POR"),
    "Rio Ave": ("Vila do Conde", "POR"),
    "União de Leiria": ("Leiria", "POR"),
    "Amora": ("Seixal", "POR"),
    "Penafiel": ("Penafiel", "POR"),
    "Ginásio de Alcobaça": ("Alcobaça", "POR"),
    "Recreio de Águeda": ("Águeda", "POR"),
    "Vizela": ("Vizela", "POR"),
    "Desportivo das Aves": ("Vila das Aves", "POR"),
    "Chaves": ("Chaves", "POR"),
    "Nacional da Madeira": ("Funchal", "POR"),
    "Estrela da Amadora": ("Amadora", "POR"),
    "Fafe": ("Fafe", "POR"),
    "União da Madeira": ("Funchal", "POR"),
    "Gil Vicente": ("Barcelos", "POR"),
    "Paços de Ferreira": ("Paços de Ferreira", "POR"),
    "Felgueiras": ("Felgueiras", "POR"),
    "Campomaiorense": ("Campo Maior", "POR"),
    "Alverca": ("Alverca do Ribatejo", "POR"),
    "Santa Clara": ("Ponta Delgada", "POR"),
    "Moreirense": ("Moreira de Cónegos", "POR"),
    "Naval 1º de Maio": ("Figueira da Foz", "POR"),
    "Trofense": ("Trofa", "POR"),
    "Arouca": ("Arouca", "POR"),
    "Tondela": ("Tondela", "POR"),
    "AVS": ("Vila das Aves", "POR"),
}

OGOL = {
    "benfica": "Benfica", "fc-porto": "Porto", "sporting": "Sporting", "35": "Vitória de Setúbal", "3": "Belenenses",
    "19": "Académica", "2189": "Académico do Porto", "2198": "União de Lisboa", "2187": "Carcavelinhos", "5": "Boavista",
    "1727": "Leixões", "2171": "Barreirense", "2412": "Casa Pia", "58100": "Unidos de Lisboa", "vitoria-sc": "Vitória de Guimarães",
    "2172": "Olhanense", "24": "Leça", "3585": "CUF", "2170": "Atlético CP", "14": "Salgueiros", "1734": "Estoril",
    "2199": "Oliveirense", "2190": "SL Elvas", "2175": "Famalicão", "2185": "Sanjoanense", "sc-braga": "Braga", "2180": "O Elvas",
    "2186": "Lusitano VRSA", "23": "Sporting da Covilhã", "2176": "Oriental de Lisboa", "2173": "Lusitano de Évora",
    "2178": "Torreense", "2182": "Caldas SC", "2": "Beira-Mar", "1728": "CD Feirense", "36": "Varzim", "2192": "Seixal",
    "2174": "Tirsense", "2179": "União de Tomar", "10": "Farense", "2184": "Montijo", "208772": "União de Coimbra",
    "1175": "Espinho", "33": "Portimonense", "2193": "Riopele", "maritimo": "Marítimo", "2181": "Académico de Viseu",
    "31": "Rio Ave", "17": "União de Leiria", "2183": "Amora", "30": "Penafiel", "2196": "Ginásio de Alcobaça",
    "2194": "Recreio de Águeda", "2197": "Vizela", "7": "Desportivo das Aves", "20": "Chaves", "27": "Nacional da Madeira",
    "253884": "Estrela da Amadora", "2191": "Fafe", "22": "União da Madeira", "gil-vicente": "Gil Vicente",
    "13": "Paços de Ferreira", "21": "Felgueiras", "2177": "Campomaiorense", "1": "Alverca", "32": "Santa Clara",
    "6": "Moreirense", "28": "Naval 1º de Maio", "3664": "Trofense", "3555": "Arouca", "4336": "Tondela",
    "229965": "Belenenses SAD", "296012": "AVS",
}

ALIASES = {
    # RSSSF
    "SL Benfica": "Benfica", "FC Porto": "Porto", "Sporting CP": "Sporting", "CF Belenenses": "Belenenses",
    "VFC Setúbal": "Vitória de Setúbal", "VFC Vitória Setúbal": "Vitória de Setúbal", "VSC Guimarães": "Vitória de Guimarães",
    "VSC Vitória Guimarães": "Vitória de Guimarães", "AAC Académica": "Académica", "CAF Viseu": "Académico de Viseu",
    "Leixões SC": "Leixões", "FC Barreirense": "Barreirense", "Casa Pia AC": "Casa Pia", "SC Olhanense": "Olhanense",
    "Leça FC": "Leça", "GD CUF": "CUF", "SC Salgueiros": "Salgueiros", "GD Estoril-Praia": "Estoril",
    "UD Oliveirense": "Oliveirense", "FC Famalicão": "Famalicão", "AD Sanjoanense": "Sanjoanense", "SC Braga": "Braga",
    "O Elvas CAD": "O Elvas", "Lusitano Évora": "Lusitano de Évora", "SC Covilhã": "Sporting da Covilhã",
    "Oriental": "Oriental de Lisboa", "SCU Torreense": "Torreense", "SC Caldas": "Caldas SC", "SC Beira Mar": "Beira-Mar",
    "Varzim SC": "Varzim", "Seixal FC": "Seixal", "FC Tirsense": "Tirsense", "SC Farense": "Farense", "CD Montijo": "Montijo",
    "CF União Coimbra": "União de Coimbra", "SC Espinho": "Espinho", "Portimonense SC": "Portimonense", "GD Riopele": "Riopele",
    "CS Marítimo": "Marítimo", "Rio Ave FC": "Rio Ave", "UD Leiria": "União de Leiria", "Amora FC": "Amora",
    "FC Penafiel": "Penafiel", "GC Alcobaça": "Ginásio de Alcobaça", "RD Águeda": "Recreio de Águeda", "FC Vizela": "Vizela",
    "CD Aves": "Desportivo das Aves", "GD Chaves": "Chaves", "CD Nacional": "Nacional da Madeira",
    "CD Nacional Madeira": "Nacional da Madeira", "CF Estrela Amadora": "Estrela da Amadora", "CFE Amadora": "Estrela da Amadora",
    "AD Fafe": "Fafe", "CF União Madeira": "União da Madeira", "Gil Vicente FC": "Gil Vicente",
    "FC Paços Ferreira": "Paços de Ferreira", "FC Paços de Ferreira": "Paços de Ferreira", "FC Felgueiras": "Felgueiras",
    "SC Campomaiorense": "Campomaiorense", "FC Alverca": "Alverca", "CD Santa Clara": "Santa Clara",
    "Moreirense FC": "Moreirense", "Naval 1º Maio": "Naval 1º de Maio",
    # football-data e engsoccerdata
    "Sp Lisbon": "Sporting", "Setubal": "Vitória de Setúbal", "Guimaraes": "Vitória de Guimarães", "Sp Braga": "Braga",
    "Beira Mar": "Beira-Mar", "Campomaior": "Campomaiorense", "Desp. Chaves": "Chaves", "Est Amadora": "Estrela da Amadora",
    "Estrela": "Estrela da Amadora", "Leca": "Leça", "Leiria": "União de Leiria", "Madeira": "União da Madeira",
    "Uniao Madeira": "União da Madeira", "Nacional": "Nacional da Madeira", "Naval": "Naval 1º de Maio",
    "Pacos Ferreira": "Paços de Ferreira", "Aves": "Desportivo das Aves", "AVS Futebol SAD": "AVS", "Feirense": "CD Feirense",
    # ogol
    "Vitória FC": "Vitória de Setúbal", "Vitória SC": "Vitória de Guimarães", "Académica OAF": "Académica",
    "Académico FC": "Académico do Porto", "União Lisboa": "União de Lisboa", "Estoril Praia": "Estoril", "U. Tomar": "União de Tomar",
    "U. Coimbra": "União de Coimbra", "Lusitano GC": "Lusitano de Évora", "União Madeira": "União da Madeira",
    "FC Felgueiras (Extinto)": "Felgueiras", "B SAD": "Belenenses SAD", "AFS": "AVS", "Ginásio Alcobaça": "Ginásio de Alcobaça",
    # Wikipédia
    "Académica de Coimbra": "Académica", "CUF Barreiro": "CUF", "Alcobaça": "Ginásio de Alcobaça", "Águeda": "Recreio de Águeda",
    "Covilhã": "Sporting da Covilhã", "B-SAD": "Belenenses SAD",
    # 1942/43: a Wikipédia chama de "Unidos do Barreiro" o clube que o ogol e a RSSSF dão como CUF
    "Unidos do Barreiro": "CUF",
    # lista de artilheiros da RSSSF (porttops.html)
    "GD CUF Barreiro": "CUF", "Vitória SC Guimarães": "Vitória de Guimarães", "Académica Coimbra": "Académica",
    "Boavista FC Porto": "Boavista", "SC Farense Faro": "Farense", "Vitória FC Setúbal": "Vitória de Setúbal",
    "CD Santa Clara Açores": "Santa Clara", "Vit. Guimarães": "Vitória de Guimarães", "Vit. Setúbal": "Vitória de Setúbal",
    "SC Beira-Mar": "Beira-Mar",
}

# nomes que dependem da época: o "Belenenses" do football-data e da RSSSF de 2018/19 a 2021/22 é a SAD
POR_ANO = {
    "Belenenses": [(1934, 2017, "Belenenses"), (2018, 2021, "Belenenses SAD")],
    'CF "Os Belenenses"': [(1934, 2017, "Belenenses"), (2018, 2021, "Belenenses SAD")],   # RSSSF
    "Os Belenenses": [(1934, 2017, "Belenenses"), (2018, 2021, "Belenenses SAD")],
    # "Lusitano" na Wikipédia: o de Vila Real de Santo António (1947-1949) ou o de Évora (1952-1965)
    "Lusitano": [(1947, 1949, "Lusitano VRSA"), (1952, 1965, "Lusitano de Évora")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {chave(k): k for k in CLUBES}
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}

# siglas que a RSSSF, a Wikipédia e a ESPN põem em volta do nome ("SL Benfica", "Rio Ave FC", "CD Nacional")
SIGLAS = {"fc", "sc", "cf", "cd", "sl", "gd", "ud", "cs", "ac", "ad", "aac", "oaf", "sad", "fs", "vfc", "vsc", "cp", "de", "da",
          "do", "dos", "das", "futebol", "clube", "sport", "sporting", "os", "vitoria"}


def _reduzir(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return "".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in SIGLAS)


_REDUZIDO: dict[str, str | None] = {}
for _nome, _c in [(k, k) for k in CLUBES] + list(ALIASES.items()):
    r = _reduzir(_nome)
    if not r:
        continue
    if _REDUZIDO.get(r, _c) != _c:
        _REDUZIDO[r] = None   # ambíguo ("Sporting" e "Sporting da Covilhã" não; "Vitória" sozinho sim)
    else:
        _REDUZIDO.setdefault(r, _c)


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que
    dependem da época ("Belenenses")."""
    nome = nome.replace("&nbsp;", " ").replace("\xa0", " ").strip().rstrip("*").strip()
    k = chave(nome)
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k) or _REDUZIDO.get(_reduzir(nome))


def ogol(codigo: str) -> str | None:
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube


def cidade(chave_clube: str) -> str:
    return CLUBES[chave_clube][0]


def pais(chave_clube: str) -> str:
    return CLUBES[chave_clube][1]
