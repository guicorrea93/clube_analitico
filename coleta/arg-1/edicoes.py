"""Edições da 1ª divisão argentina (arg-1): uma por torneio que deu título de campeão da Primera División.

Lista de títulos: RSSSF (argchamp.html, "Argentine Amateur/Professional First Division Champions"), conferida com a
Wikipédia. Regra do guia internacional: ano com mais de um campeão oficial (ligas rivais de 1912-1914, 1919-1926 e
1931-1934; Copa de Honor, Campeonato e Copa de Oro de 1936; Metropolitano e Nacional de 1967 a 1985; Apertura e Clausura
de 1991/92 a 2013/14 e de 2025) vira uma edição por torneio.

Ficam de fora, como na lista de campeões da RSSSF:
- as "copas da liga" (Copa de la Superliga 2019, Copa de la Liga Profesional 2020 a 2024): copas, não campeonatos;
- a Copa Campeonato 2013/14 (jogo entre os campeões do Inicial e do Final, que a AFA tratou como copa nacional);
- os torneios de reclassificação, de promoção e as liguillas pré-Libertadores (não davam título).
A tabela anual de 2025 (Rosario Central, "campeão da Liga" pela AFA em 20/11/2025) entra como edição sem jogos próprios
("2025 Liga"): a classificação é a tabela anual, conferida com a soma das fases de grupos do Apertura e do Clausura.

Cada edição diz onde estão os jogos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro
(rsssf_sul.texto). Linha final None: até o primeiro título de outra competição (FIM_PADRAO).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "arg-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(?:\d{4} )?(Friendly|Friendlies|Regional combined|National teams?\b|Results of the competitions|About this document|"
              r"list of 2nd level|list of champions|\d{4}(/\d{2})? \((2nd|second) level|PRIMERA\s+(DIVISION\s+)?B\b|Primera B\b|"
              r"Second (level|Division)|Segunda Divisi|Intermedia|Copa de Competencia|Copa Ibarguren|Torneo Reclasificat|"
              r"Reclasificat|Liguilla|Pre[- ]Libertadores|Copa Argentina|Promotion/Relegation|Matches played in upcountry|"
              r"\d{4}\.$)")


@dataclass
class Edicao:
    temporada: str                      # "1931 Liga", "1967 Metropolitano", "1991/92 Apertura", "2016/17"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str                  # como está em argchamp.html
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)   # (regex do título, nome da fase), além do padrão
    nomes: dict[str, str] = field(default_factory=dict)          # grafia da página -> clube, quando a regra geral erra nesta edição
    soma_de: list[str] = field(default_factory=list)              # edição sem jogos próprios: a tabela soma estas edições

    @property
    def pontos_vitoria(self) -> int:
        """2 pontos até 1994/95; 3 a partir do Apertura 1995. Em 1988/89, 3 pela vitória e 2 ou 1 no empate com pênaltis."""
        return 3 if self.ano_inicio >= 1995 or self.temporada == "1988/89" else 2


def _e(temporada, ini, fim, trechos, nome, campeao, obs="", fases=None, nomes=None):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, fases or [], nomes or {})


# nas ligas da Federación (1912-1914) o "Estudiantes" sem cidade é o de La Plata (o de Buenos Aires jogava a Asociación)
_EST_LP = {"Estudiantes": "Estudiantes"}


EDICOES: list[Edicao] = [
    _e("1891", 1891, 1891, [("arg1891", 18, 123)], "Argentine Association Football League 1891", "Saint Andrew's Athletic Club",
       "título dividido entre Saint Andrew's e Caledonians pela liga da época; a AFA só cita o Saint Andrew's (RSSSF)"),
]
# 1893-1911: uma liga
for _a in [*range(1893, 1912)]:
    _p = f"arg{_a}" if _a < 1910 else f"arg{_a % 100:02d}"
    EDICOES.append(_e(str(_a), _a, _a, [(_p, 0, None)],
                      ("Championship" if _a <= 1905 else "Campeonato") + f" {_a}", ""))
EDICOES += [
    _e("1912 Asociación", 1912, 1912, [("arg12", 11, 175)], "Asociación Argentina de Football – Copa Campeonato 1912", "Quilmes Athletic Club"),
    _e("1912 Federación", 1912, 1912, [("arg12", 175, None)], "Federación Argentina de Football – Campeonato 1912", "Club Atlético Porteño", nomes=_EST_LP),
    _e("1913 Asociación", 1913, 1913, [("arg13", 15, 377)], "Asociación Argentina de Football – Copa Campeonato 1913", "Racing Football Club"),
    _e("1913 Federación", 1913, 1913, [("arg13", 377, None)], "Federación Argentina de Football – Primera División 1913", "Club Estudiantes (La Plata)", nomes=_EST_LP),
    _e("1914 Asociación", 1914, 1914, [("arg14", 262, None)], "Asociación Argentina de Football – Copa Campeonato 1914", "Racing Football Club"),
    _e("1914 Federación", 1914, 1914, [("arg14", 29, 262)], "Federación Argentina de Football – Primera División 1914", "Club Atlético Porteño", nomes=_EST_LP),
]
for _a in range(1915, 1919):
    EDICOES.append(_e(str(_a), _a, _a, [(f"arg{_a % 100}", 0, None)], f"Copa Campeonato {_a}", ""))
EDICOES += [
    _e("1919 Asociación", 1919, 1919, [("arg19", 14, 323)], "Asociación Argentina de Football – Copa Campeonato 1919", "Club Atlético Boca Juniors"),
    _e("1919 Amateurs", 1919, 1919, [("arg19", 323, None)], "Asociación Amateurs de Football – Primera División 1919", "Racing Club"),
    _e("1920 Asociación", 1920, 1920, [("arg20", 497, None)], "Asociación Argentina de Football – Copa Campeonato 1920", "Club Atlético Boca Juniors"),
    _e("1920 Amateurs", 1920, 1920, [("arg20", 22, 497)], "Asociación Amateurs de Football – Primera División 1920", "Club Atlético River Plate"),
    _e("1921 Asociación", 1921, 1921, [("arg21", 14, 368)], "Asociación Argentina de Football – Copa Campeonato 1921", "Club Atlético Huracán"),
    _e("1921 Amateurs", 1921, 1921, [("arg21", 368, None)], "Asociación Amateurs de Football – Primera División 1921", "Racing Club"),
    _e("1922 Asociación", 1922, 1922, [("arg22", 17, 387)], "Asociación Argentina de Football – Copa Campeonato 1922", "Club Atlético Huracán",
       nomes={"Platense": "Universal"}),
    _e("1922 Amateurs", 1922, 1922, [("arg22", 387, None)], "Asociación Amateurs de Football – Primera División 1922", "Club Atlético Independiente"),
    _e("1923 Asociación", 1923, 1923, [("arg23", 363, None)], "Asociación Argentina de Football – Copa Campeonato 1923", "Club Atlético Boca Juniors",
       nomes={"Platense": "Universal"}),
    _e("1923 Amateurs", 1923, 1923, [("arg23", 12, 363)], "Asociación Amateurs de Football – Primera División 1923", "Club Atlético San Lorenzo de Almagro"),
    _e("1924 Asociación", 1924, 1924, [("arg24", 23, 564)], "Asociación Argentina de Football – Campeonato 1924", "Club Atlético Boca Juniors",
       nomes={"Platense": "Universal"}),
    _e("1924 Amateurs", 1924, 1924, [("arg24", 564, None)], "Asociación Amateurs de Football – Primera División 1924", "Club Atlético San Lorenzo de Almagro"),
    _e("1925 Asociación", 1925, 1925, [("arg25", 14, 617)], "Asociación Argentina de Football – Copa Campeonato 1925", "Club Atlético Huracán",
       nomes={"Platense": "Universal"}),   # o Platense da Asociación (virou Retiro e depois Universal); o de Vicente López jogava a Amateurs
    _e("1925 Amateurs", 1925, 1925, [("arg25", 617, None)], "Asociación Amateurs de Football – Primera División 1925", "Racing Club"),
    _e("1926 Asociación", 1926, 1926, [("arg26", 22, 340)], "Asociación Argentina de Football – Copa Campeonato 1926", "Club Atlético Boca Juniors"),
    _e("1926 Amateurs", 1926, 1926, [("arg26", 340, None)], "Asociación Amateurs de Football – Primera División 1926", "Club Atlético Independiente"),
    _e("1927", 1927, 1927, [("arg27", 0, None)], "Asociación Amateurs Argentina de Football – Primera División 1927", "Club Atlético San Lorenzo de Almagro"),
    _e("1928", 1928, 1928, [("arg28", 0, None)], "Asociación Amateurs Argentina de Football – Primera División 1928", "Club Atlético Huracán"),
    _e("1929", 1929, 1929, [("arg29", 0, 764)], "Campeonato Estímulo 1929", "Club de Gimnasia y Esgrima (La Plata)"),
    _e("1930", 1930, 1930, [("arg30", 0, None)], "Asociación Amateurs Argentina de Football – Primera División 1930", "Club Atlético Boca Juniors"),
    _e("1931 Liga", 1931, 1931, [("arg31", 0, 790)], "Liga Argentina de Football – Campeonato 1931", "Club Atlético Boca Juniors"),
    _e("1931 Asociación", 1931, 1931, [("arg31a", 125, 391)], "Asociación Argentina de Football (Amateurs y Profesionales) – Copa Campeonato 1931",
       "Club Atlético Estudiantil Porteño",
       "o campeonato da Asociación Amateurs, começado antes da saída dos clubes profissionais, foi anulado e recomeçado"),
    _e("1932 Liga", 1932, 1932, [("arg32", 0, None)], "Liga Argentina de Football – Campeonato 1932", "Club Atlético River Plate"),
    _e("1932 Asociación", 1932, 1932, [("arg32a", 19, 884)], "Asociación Argentina de Football – Primera División 1932", "Club Sportivo Barracas"),
    _e("1933 Liga", 1933, 1933, [("arg33", 0, None)], "Liga Argentina de Football – Campeonato 1933", "Club Atlético San Lorenzo de Almagro"),
    _e("1933 Asociación", 1933, 1933, [("arg33a", 19, 588)], "Asociación Argentina de Football – Primera División 1933", "Club Sportivo Dock Sud"),
    _e("1934 Liga", 1934, 1934, [("arg34", 30, None)], "Liga Argentina de Football – Campeonato 1934", "Club Atlético Boca Juniors",
       "a Liga e a Asociación se fundiram em 3/11/1934, com o campeonato em andamento"),
    _e("1934 Asociación", 1934, 1934, [("arg34a", 13, 747)], "Asociación Argentina de Football – Primera División 1934", "Club Atlético Estudiantil Porteño"),
    _e("1935", 1935, 1935, [("arg35", 0, None)], "Campeonato de Primera División 1935", "Club Atlético Boca Juniors"),
    _e("1936 Copa de Honor", 1936, 1936, [("arg-hon36", 0, None)], "Copa de Honor Municipalidad de Buenos Aires 1936", "Club Atlético San Lorenzo de Almagro",
       "título de Primera División reconhecido pela AFA em 4/7/2013"),
    _e("1936 Campeonato", 1936, 1936, [("arg36", 0, None)], "Copa Campeonato 1936", "Club Atlético River Plate"),
    _e("1936 Copa de Oro", 1936, 1936, [("arg-oro36", 0, None)], "Copa de Oro 1936", "Club Atlético River Plate",
       "jogo entre os campeões da Copa de Honor e da Copa Campeonato; título reconhecido pela AFA em 4/7/2013"),
]
_FIM = {1953: 395, 1965: 928}   # o trecho da 1ª divisão acaba antes das tabelas da 2ª divisão
for _a in range(1937, 1967):
    EDICOES.append(_e(str(_a), _a, _a, [(f"arg{_a % 100}", 0, _FIM.get(_a))], f"Campeonato de Primera División {_a}", ""))

_MN = {  # Metropolitano e Nacional, 1967-1985: (página, início e fim de cada torneio); None = não houve
    1967: ("arg67", (13, 578), (578, 831)), 1968: ("arg68", (10, 602), (790, 1072)), 1969: ("arg69", (10, 585), (813, 1121)),
    1970: ("arg70", (11, 383), (536, 945)), 1971: ("arg71", (14, 1016), (1016, 1692)), 1972: ("arg72", (13, 523), (523, 935)),
    1973: ("arg73", (12, 466), (466, 889)), 1974: ("arg74", (12, 422), (422, 1172)), 1975: ("arg75", (18, 610), (610, 1214)),
    1976: ("arg76", (10, 1186), (1186, 2237)), 1977: ("arg77", (17, 1395), (1395, 2256)), 1978: ("arg78", (17, 798), (798, 1444)),
    1979: ("arg79", (10, 455), (455, 991)), 1980: ("arg80", (12, 584), (584, 1116)), 1981: ("arg81", (12, 474), (474, 976)),
    1982: ("arg82", (710, 1383), (13, 710)), 1983: ("arg83", (628, 1179), (12, 628)), 1984: ("arg84", (575, 1250), (14, 575)),
    1985: ("arg85", None, (0, 491)),
}
_CAMPEOES_MN = {
    1967: ("Club Estudiantes de La Plata", "Club Atlético Independiente"), 1968: ("Club Atlético San Lorenzo de Almagro", "Club Atlético Vélez Sarsfield"),
    1969: ("Club Atlético Chacarita Juniors", "Club Atlético Boca Juniors"), 1970: ("Club Atlético Independiente", "Club Atlético Boca Juniors"),
    1971: ("Club Atlético Independiente", "Club Atlético Rosario Central"), 1972: ("Club Atlético San Lorenzo de Almagro", "Club Atlético San Lorenzo de Almagro"),
    1973: ("Club Atlético Huracán", "Club Atlético Rosario Central"), 1974: ("Club Atlético Newell's Old Boys", "Club Atlético San Lorenzo de Almagro"),
    1975: ("Club Atlético River Plate", "Club Atlético River Plate"), 1976: ("Club Atlético Boca Juniors", "Club Atlético Boca Juniors"),
    1977: ("Club Atlético River Plate", "Club Atlético Independiente"), 1978: ("Quilmes Atlético Club", "Club Atlético Independiente"),
    1979: ("Club Atlético River Plate", "Club Atlético River Plate"), 1980: ("Club Atlético River Plate", "Club Atlético Rosario Central"),
    1981: ("Club Atlético Boca Juniors", "Club Atlético River Plate"), 1982: ("Club Estudiantes de La Plata", "Club Ferro Carril Oeste"),
    1983: ("Club Atlético Independiente", "Club Estudiantes de La Plata"), 1984: ("Asociación Atlética Argentinos Juniors", "Club Ferro Carril Oeste"),
    1985: (None, "Asociación Atlética Argentinos Juniors"),
}
for _a, (_p, _m, _n) in _MN.items():
    _cm, _cn = _CAMPEOES_MN[_a]
    if _m:
        EDICOES.append(_e(f"{_a} Metropolitano", _a, _a, [(_p, *_m)],
                          f"Campeonato Metropolitano {_a}" if _a < 1980 else f"Campeonato de Primera División {_a} (Metropolitano)", _cm))
    if _n:
        EDICOES.append(_e(f"{_a} Nacional", _a, _a, [(_p, *_n)], f"Campeonato Nacional {_a}", _cn))

EDICOES += [
    _e("1985/86", 1985, 1986, [("arg86", 13, 687)], "Campeonato de Primera División 1985/86", "Club Atlético River Plate"),
    _e("1986/87", 1986, 1987, [("arg87", 0, 603)], "Campeonato de Primera División 1986/87", "Club Atlético Rosario Central"),
    _e("1987/88", 1987, 1988, [("arg88", 0, 607)], "Campeonato de Primera División 1987/88", "Club Atlético Newell's Old Boys"),
    _e("1988/89", 1988, 1989, [("arg89", 12, 818)], "Campeonato de Primera División 1988/89", "Club Atlético Independiente",
       "empate decidido nos pênaltis: 2 pontos para o vencedor e 1 para o perdedor; vitória no tempo normal, 3 pontos"),
    _e("1989/90", 1989, 1990, [("arg90", 16, 744)], "Campeonato de Primera División 1989/90", "Club Atlético River Plate"),
    _e("1990/91", 1990, 1991, [("arg91", 12, 1081)], "Campeonato de Primera División 1990/91", "Club Atlético Newell's Old Boys",
       "Apertura 1990 (Newell's) e Clausura 1991 (Boca) eram fases; o título saiu da final entre os dois",
       [(r"^Torneo Apertura", "Apertura"), (r"^Torneo Clausura", "Clausura"), (r"^Championship$|^Playoff$", "Final")]),
]
# Apertura e Clausura, 1991/92 a 2011/12: (página, Apertura, Clausura)
_AC = {
    1991: ("arg92", (12, 394), (394, 807)), 1992: ("arg93", (12, 421), (421, 825)), 1993: ("arg94", (12, 415), (415, 815)),
    1994: ("arg95", (12, 437), (437, 861)), 1995: ("arg96", (11, 552), (552, 1166)), 1996: ("arg97", (12, 409), (409, 761)),
    1997: ("arg98", (12, 370), (370, 723)), 1998: ("arg99", (12, 373), (373, 727)), 1999: ("arg00", (12, 561), (561, 1269)),
    2000: ("arg01", (12, 563), (563, 1096)), 2001: ("arg02", (12, 538), (538, 1083)), 2002: ("arg03", (12, 541), (541, 1091)),
    2003: ("arg04", (12, 532), (532, 1068)), 2004: ("arg05", (12, 533), (533, 1114)), 2005: ("arg06", (12, 543), (569, 1124)),
    2006: ("arg07", (12, 562), (562, 946)), 2007: ("arg08", (12, 574), (574, 1131)), 2008: ("arg09", (12, 593), (593, 1138)),
    2009: ("arg2010", (14, 367), (367, 721)), 2010: ("arg2011", (28, 379), (379, 732)), 2011: ("arg2012", (29, 407), (407, 791)),
}
_CAMPEOES_AC = {
    1991: ("Club Atlético River Plate", "Club Atlético Newell's Old Boys"), 1992: ("Club Atlético Boca Juniors", "Club Atlético Vélez Sarsfield"),
    1993: ("Club Atlético River Plate", "Club Atlético Independiente"), 1994: ("Club Atlético River Plate", "Club Atlético San Lorenzo de Almagro"),
    1995: ("Club Atlético Vélez Sarsfield", "Club Atlético Vélez Sarsfield"), 1996: ("Club Atlético River Plate", "Club Atlético River Plate"),
    1997: ("Club Atlético River Plate", "Club Atlético Vélez Sarsfield"), 1998: ("Club Atlético Boca Juniors", "Club Atlético Boca Juniors"),
    1999: ("Club Atlético River Plate", "Club Atlético River Plate"), 2000: ("Club Atlético Boca Juniors", "Club Atlético San Lorenzo de Almagro"),
    2001: ("Racing Club", "Club Atlético River Plate"), 2002: ("Club Atlético Independiente", "Club Atlético River Plate"),
    2003: ("Club Atlético Boca Juniors", "Club Atlético River Plate"), 2004: ("Club Atlético Newell's Old Boys", "Club Atlético Vélez Sarsfield"),
    2005: ("Club Atlético Boca Juniors", "Club Atlético Boca Juniors"), 2006: ("Club Estudiantes de La Plata", "Club Atlético San Lorenzo de Almagro"),
    2007: ("Club Atlético Lanús", "Club Atlético River Plate"), 2008: ("Club Atlético Boca Juniors", "Club Atlético Vélez Sarsfield"),
    2009: ("Club Atlético Banfield", "Asociación Atlética Argentinos Juniors"), 2010: ("Club Estudiantes de La Plata", "Club Atlético Vélez Sarsfield"),
    2011: ("Club Atlético Boca Juniors", "Arsenal Fútbol Club"),
}
for _a, (_p, _ap, _cl) in _AC.items():
    _t = f"{_a}/{(_a + 1) % 100:02d}"
    _ca, _cc = _CAMPEOES_AC[_a]
    EDICOES.append(_e(f"{_t} Apertura", _a, _a, [(_p, *_ap)], f"Torneo Apertura {_a}", _ca))
    EDICOES.append(_e(f"{_t} Clausura", _a, _a + 1, [(_p, *_cl)], f"Torneo Clausura {_a + 1}", _cc))

EDICOES += [
    _e("2012/13 Inicial", 2012, 2012, [("arg2013", 31, 397)], "Torneo Inicial 2012", "Club Atlético Vélez Sarsfield"),
    _e("2012/13 Final", 2012, 2013, [("arg2013", 397, 778)], "Torneo Final 2013", "Club Atlético Newell's Old Boys"),
    _e("2012/13 Campeonato", 2012, 2013, [("arg2013", 778, 811)], "Campeonato de Primera División 2012/13", "Club Atlético Vélez Sarsfield",
       "jogo único entre os campeões do Inicial (Vélez Sarsfield) e do Final (Newell's Old Boys)"),
    _e("2013/14 Inicial", 2013, 2013, [("arg2014", 40, 421)], "Torneo Inicial 2013", "Club Atlético San Lorenzo de Almagro"),
    _e("2013/14 Final", 2013, 2014, [("arg2014", 421, 792)], "Torneo Final 2014", "Club Atlético River Plate"),
    _e("2014", 2014, 2014, [("arg2015", 34, 450)], "Campeonato de Primera División 2014", "Racing Club"),
    _e("2015", 2015, 2015, [("arg2015a", 40, 796)], "Campeonato de Primera División 2015", "Club Atlético Boca Juniors"),
    _e("2016", 2016, 2016, [("arg2016", 39, 621)], "Campeonato de Primera División 2016", "Club Atlético Lanús"),
    _e("2016/17", 2016, 2017, [("arg2017", 43, 732)], "Campeonato de Primera División 2016/17", "Club Atlético Boca Juniors"),
    _e("2017/18", 2017, 2018, [("arg2018", 39, 645)], "Superliga Argentina 2017/18", "Club Atlético Boca Juniors"),
    _e("2018/19", 2018, 2019, [("arg2019", 44, 587)], "Superliga Argentina 2018/19", "Racing Club"),
    _e("2019/20", 2019, 2020, [("arg2020", 35, 486)], "Superliga Argentina 2019/20", "Club Atlético Boca Juniors",
       "campeonato de 23 rodadas; a temporada parou na pandemia durante a Copa de la Superliga (fora do pacote)"),
    _e("2021", 2021, 2021, [("arg2021", 353, 859)], "Torneo de la Liga Profesional de Fútbol 2021", "Club Atlético River Plate"),
    _e("2022", 2022, 2022, [("arg2022", 397, 973)], "Torneo de la Liga Profesional de Fútbol 2022", "Club Atlético Boca Juniors"),
    _e("2023", 2023, 2023, [("arg2023", 37, 667)], "Torneo de la Liga Profesional de Fútbol 2023", "Club Atlético River Plate"),
    _e("2024", 2024, 2024, [("arg2024", 411, 1004)], "Torneo de la Liga Profesional de Fútbol 2024", "Club Atlético Vélez Sarsfield"),
    _e("2025 Apertura", 2025, 2025, [("arg2025", 39, 485)], "Torneo Apertura 2025", "Club Atlético Platense"),
    _e("2025 Clausura", 2025, 2025, [("arg2025", 485, 934)], "Torneo Clausura 2025", "Club Estudiantes de La Plata"),
    Edicao("2025 Liga", 2025, 2025, [("arg2025", 970, 1006)], "Tabla Anual de la LPF 2025 (Campeón de Liga)", "Club Atlético Rosario Central",
           "título dado pela AFA em 20/11/2025 ao 1º da tabela anual (soma das fases de grupos do Apertura e do Clausura); "
           "sem jogos próprios: os jogos estão nas edições 2025 Apertura e 2025 Clausura",
           soma_de=["2025 Apertura", "2025 Clausura"]),
]
