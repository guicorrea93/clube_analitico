"""Copa Venezuela (ven-copa): copa nacional da FVF. Última das sete copas da América do Sul (decisões do Guilherme de
24/11/2026 em coleta/comum-sulamerica/copas-nacionais.md): contagem da Wikipédia em espanhol ("Anexo:Temporadas de la Copa
Venezuela", guardado em data/coleta/ven-copa/wikipedia/), 66 edições com campeão: 17 da era amadora (1932-1953, com a
Copa del Distrito Federal 1948, a Copa Junta Militar 1949/50, a Copa Ciudad de Caracas 1952 e a Copa IND 1953) e 49 de
1959 em diante (Copa Liga Mayor, de las Naciones, Caracas, Cuatricentenario, Valencia e Bicentenario contam; não houve
1974, 1984, 1986, 1996-2006 e 2020-2023). A pesquisa de 23/11 falava em 63; o anexo lista 66.

Fonte dos jogos: RSSSF, a seção da copa nas páginas do ven-1 (data/coleta/ven-1/rsssf), às vezes na página da temporada
seguinte (a de 1987 está em venez88, a de 2009 em venez2010...); lista de campeões em venezcuphist.html. Muitas edições
antigas só têm a tabela (pontos corridos) ou só os jogos de um clube; sem página: 1938, 1949/50, 1989, 1990 e 1992. Quando
os jogos não decidem, campeão e vice são os da Wikipédia (CAMPEOES).

Uso: python coleta/ven-copa/importar.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(1, str(AQUI.parent / "ven-1"))
import autores  # noqa: E402  (o do ven-1)
import ler_rsssf  # noqa: E402  (o do ven-1: páginas em data/coleta/ven-1/rsssf)
import rsssf_sul  # noqa: E402
from clubes_copa import CLUBES, clube  # noqa: E402
from copa_rsssf import Copa, EdicaoCopa, importar  # noqa: E402
from ler_rsssf import linhas  # noqa: E402

SLUG = "ven-copa"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

PRE, GRU, GR2, FFIN = "Fase preliminar", "Fase de grupos", "Segunda fase de grupos", "Fase final (pontos corridos)"
P1, P2, P3 = "Primeira fase", "Segunda fase", "Terceira fase"
D16, OIT, QUA, SEM, FIN = "Dezesseis-avos de final", "Oitavas de final", "Quartas de final", "Semifinal", "Final"
FASES = [(r"^NUNCA$", f) for f in (PRE, GRU, GR2, P1, P2, P3, D16, OIT, QUA, SEM, FFIN)] + [(r"^NUNCA$", FIN)]
KO = [(r"^1/16 Finals", D16), (r"^1/8 Finals", OIT), (r"^Quarter-?finals?", QUA), (r"^Semi-?finals?|^Semifinal", SEM),
      (r"^(Final|Replay|Second Replay)\b(?! Tables?| Table| Group| Round| Phase| Stage)", FIN)]
RODADAS = [(r"^Round 1\b", P1), (r"^Round 2\b", P2), (r"^Round 3\b", P3)]
FASES3 = [(r"^Preliminary Round", PRE), (r"^First (Phase|Stage)", P1), (r"^Second (Phase|Stage)", P2),
          (r"^Third (Phase|Stage)", P3)]
_FIM = (r"^(list of champions|list of cup winners|Source for cup|Main source|\d{4}(/\d{2,4})?$|Segunda Divisi|"
        r"Tercera Divisi|Barinas League|Torneo Iniciacion|Second Level|Copa Venezuela \d{4}|Copa de Campeones|Torneo Clausura)")


def _secao(pagina: str, titulo: str) -> tuple[str, int, int]:
    """Da última linha que começa com `titulo` (a primeira costuma ser o índice) até o fim da seção da copa."""
    ls = linhas(pagina)
    a = [i for i, l in enumerate(ls) if l.strip().startswith(titulo)][-1]
    b = next((i for i in range(a + 1, len(ls)) if re.match(_FIM, ls[i].strip())), len(ls))
    return pagina, a, b


def _ate(trecho: tuple[str, int, int], fim: str) -> tuple[str, int, int]:
    """O trecho cortado na primeira linha que começa com `fim`."""
    pagina, a, b = trecho
    ls = linhas(pagina)
    return pagina, a, next((i for i in range(a + 1, b) if ls[i].strip().startswith(fim)), b)


def _cruzadas_1995():
    """Jogos de 1995 (Torneo Apertura 1995/96) nas tabelas de confrontos dos grupos Oriental e Occidental (mandante na
    linha, visitante na coluna), pelo leitor do ven-1; as linhas "xxx" ficam fora do leitor comum (Copa.ignorar)."""
    pagina, a, b = _secao("venez96", "Torneo Apertura (Copa")
    ls = list(linhas(pagina))
    jogos, _ = ler_rsssf.confrontos(ls, a, b)
    cortes = [i for i in range(a, b) if re.match(r"^\s*Cross-?Table", ls[i], re.I)]
    return [rsssf_sul.Jogo(linha=k, mandante=m, visitante=v, gm=gm, gv=gv, fase=GRU, texto=f"{pagina}:{k}",
                           grupo="Oriental" if len(cortes) < 2 or k < cortes[1] else "Occidental")
            for k, m, v, gm, gv, _dado in jogos]


# Wikipédia em espanhol, "Anexo:Temporadas de la Copa Venezuela" (Historial): (campeão, vice)
CAMPEOES = {
    "1932": ("Unión", "Deportivo Venezuela"), "1933": ("Dos Caminos", "Deportivo Venezuela"), "1934": ("Unión", "Dos Caminos"),
    "1935": ("Unión", "Dos Caminos"), "1936": ("Unión", "Deportivo Venezuela"), "1937": ("Litoral", "Deportivo Venezuela"),
    "1938": ("Unión", "Dos Caminos"), "1940": ("Unión", "Litoral"), "1941": ("Litoral", "Dos Caminos"), "1942": ("Loyola", "Litoral"),
    "1943/44": ("Loyola", "Dos Caminos"), "1945": ("Dos Caminos", "Deportivo Venezuela"), "1947": ("La Salle", "Unión"),
    "1948": ("Pampero", "La Salle"), "1949/50": ("Deportivo Italia", "Centro Atlético"), "1952": ("Universidad Central", "Unión"),
    "1953": ("Deportivo Vasco", "Nuevos del Este"), "1959": ("Deportivo Portugués", "Deportivo Español"),
    "1960": ("Banco Agrícola y Pecuario", "Deportivo Portugués"), "1961": ("Deportivo Italia", "Dos Caminos"),
    "1962": ("Deportivo Italia", "Canarias"), "1963": ("Canarias", "La Salle"), "1964": ("Tiquire Flores", "Canarias"),
    "1965": ("Valencia", "Lara"), "1966": ("Deportivo Galicia", "Canarias"), "1967": ("Deportivo Galicia", "Deportivo Portugués"),
    "1968": ("Canarias", "Lara"), "1969": ("Deportivo Galicia", "Canarias"), "1970": ("Deportivo Italia", "Deportivo Galicia"),
    "1971": ("Estudiantes de Mérida", "Anzoátegui"), "1972": ("Deportivo Portugués", "Estudiantes de Mérida"),
    "1973": ("Portuguesa", "Estudiantes de Mérida"), "1975": ("Estudiantes de Mérida", "Deportivo San Cristóbal"),
    "1976": ("Portuguesa", "Deportivo Italia"), "1977": ("Portuguesa", "Valencia"), "1978": ("Valencia", "Universidad de Los Andes"),
    "1979": ("Deportivo Galicia", "Deportivo Lara (1978)"), "1980": ("Atlético Zamora", "Valencia"),
    "1981": ("Deportivo Galicia", "Deportivo Táchira"), "1982": ("Deportivo Táchira", "Atlético Zamora"),
    "1983": ("Deportivo Táchira", "Atlético Zamora"), "1985": ("Mineros de Guayana", "Deportivo Táchira"),
    "1987": ("Caracas", "Mineros de Guayana"), "1988": ("Marítimo", "Estudiantes de Mérida"), "1989": ("Marítimo", "Mineros de Guayana"),
    "1990": ("Internacional de Puerto La Cruz", "Portuguesa"), "1991": ("Anzoátegui", "Caracas"), "1992": ("Trujillanos", "Caracas"),
    "1993": ("Caracas", "Minerven"), "1994": ("Caracas", "Trujillanos"), "1995": ("Universidad de Los Andes", "Caracas"),
    "2007": ("Aragua", "U. A. Maracaibo"), "2008": ("Deportivo Anzoátegui", "Estudiantes de Mérida"), "2009": ("Caracas", "Trujillanos"),
    "2010": ("Trujillanos", "Zamora"), "2011": ("Mineros de Guayana", "Trujillanos"),
    "2012": ("Deportivo Anzoátegui", "Estudiantes de Mérida"), "2013": ("Caracas", "Deportivo Táchira"),
    "2014": ("Deportivo La Guaira", "Trujillanos"), "2015": ("Deportivo La Guaira", "Deportivo Lara"),
    "2016": ("Zulia", "Estudiantes de Caracas"), "2017": ("Mineros de Guayana", "Zamora"), "2018": ("Zulia", "Aragua"),
    "2019": ("Zamora", "Monagas"), "2024": ("Deportivo La Guaira", "Metropolitanos"), "2025": ("Universidad Central", "Carabobo")}
NOMES = {"1943/44": "Copa Venezuela 1943-44", "1948": "Copa del Distrito Federal 1948", "1949/50": "Copa Junta Militar de Gobierno 1949-50",
         "1952": "Copa Ciudad de Caracas 1952", "1953": "Copa IND 1953", "1959": "Copa Liga Mayor 1959",
         "1960": "Copa de las Naciones 1960", "1961": "Copa Caracas 1961", "1962": "Copa Caracas 1962", "1963": "Copa Caracas 1963",
         "1964": "Copa Caracas 1964", "1966": "Copa Caracas 1966", "1967": "Copa Cuatricentenario 1967", "1972": "Copa Valencia 1972",
         "1983": "Copa Bicentenario 1983"}


def ed(temporada: str, a0: int, a1: int, trechos: list, fases: list | None = None, **kw) -> EdicaoCopa:
    c, v = CAMPEOES[temporada]
    return EdicaoCopa(temporada, a0, a1, NOMES.get(temporada, f"Copa Venezuela {temporada.replace('/', '-')}"), trechos,
                      fases=fases or KO, campeao_fonte=c, vice_fonte=v, **kw)


_SO_UM = "a RSSSF só traz os jogos de alguns clubes"
_SEM_JOGOS = "sem jogos na RSSSF: campeão e vice da Wikipédia"
_TABELA = "a RSSSF só traz a tabela (pontos corridos); campeão e vice da Wikipédia"
EDICOES = [ed(str(a), a, a, [_secao(f"venez{a % 100:02d}", f"Copa Venezuela {a}")], RODADAS + KO)
           for a in (1932, 1933, 1934, 1935, 1936, 1937)]
EDICOES += [
    ed("1938", 1938, 1938, [], obs=_SEM_JOGOS),
    ed("1940", 1940, 1940, [_secao("venez40", "Copa Venezuela 1940")], RODADAS + KO),
    ed("1941", 1941, 1941, [_secao("venez41", "Copa Venezuela 1941")], RODADAS + KO, obs=_SO_UM + " (Litoral)"),
    ed("1942", 1942, 1942, [_secao("venez42", "Copa Venezuela 1942")], RODADAS + KO, obs=_SO_UM + " (Loyola)"),
    ed("1943/44", 1943, 1944, [_secao("venez43", "Copa Venezuela 1943/44")], [(r"^Group Stage", GRU)] + KO,
       obs="fase de grupos com os resultados conhecidos; sem final"),
    ed("1945", 1945, 1945, [_secao("venez45", "Copa Venezuela 1945")], [(r"^Grupo A", GRU)] + KO),
    ed("1947", 1947, 1947, [_secao("venez47", "Copa Venezuela 1947")], [(r"^Primera Fase", GRU), (r"^Ronda Final", FFIN)] + KO,
       obs=_SO_UM + " (La Salle e Catalonia); fase final em pontos corridos"),
    ed("1948", 1948, 1948, [_secao("venez48", "Copa del Distrito")], KO, fase_padrao=GRU,
       obs="Copa del Distrito Federal: pontos corridos e uma final"),
    ed("1949/50", 1949, 1950, [], obs="Copa Junta Militar de Gobierno; " + _SEM_JOGOS),
    ed("1952", 1952, 1952, [_secao("venez52", "Copa Ciudad")], KO, fase_padrao=GRU,
       obs="Copa Ciudad de Caracas; " + _SO_UM + " (Universidad)"),
    ed("1953", 1953, 1953, [_secao("venez53", "Copa IND")], [(r"^Primera Ronda", GRU)] + KO, obs="Copa IND"),
    ed("1959", 1959, 1959, [_secao("venez59", "Copa Liga Mayor")], KO, fase_padrao=GRU, obs="Copa Liga Mayor; " + _TABELA),
    ed("1960", 1960, 1960, [_secao("venez60", "Copa de las Naciones")], [(r"^Group Stage", GRU)] + KO, obs="Copa de las Naciones"),
    ed("1961", 1961, 1961, [_secao("venez61", "Copa Caracas")], [(r"^Group Stage", GRU)] + KO, obs="Copa Caracas"),
    ed("1962", 1962, 1962, [_secao("venez62", "Copa Caracas")], [(r"^Group Stage", GRU)] + KO, obs="Copa Caracas"),
    ed("1963", 1963, 1963, [_secao("venez63", "Copa Caracas")], KO, fase_padrao=GRU, obs="Copa Caracas; " + _TABELA),
    ed("1964", 1964, 1964, [_secao("venez64", "Copa Caracas")], KO, fase_padrao=GRU, obs="Copa Caracas"),
    ed("1965", 1965, 1965, [_secao("venez65", "Copa Venezuela 1965")], [(r"^First round", GRU), (r"^Second round", GR2)] + KO),
    ed("1966", 1966, 1966, [_secao("venez66", "Copa Caracas")], [(r"^Group Stage", GRU)] + KO, final_desempate=True,
       obs="Copa Caracas; final com dois desempates, decidida no último (2-2, 3-2 nos pênaltis)"),
    ed("1967", 1967, 1967, [_secao("venez67", "Copa Cuatri")], [(r"^Grupo A", GRU), (r"^Triangular Final", FFIN)] + KO,
       obs="Copa Cuatricentenario; triangular final em pontos corridos"),
    ed("1968", 1968, 1969, [_secao("venez68", "Copa Venezuela 1968")], [(r"^Group Stage", GRU)] + KO,
       final_desempate=True, obs="a RSSSF chama de 1968/69 (final e dois desempates em janeiro de 1969, decidida no último)"),
    ed("1969", 1969, 1969, [_secao("venez69", "Copa Venezuela 1969")], [(r"^Group Stage", GRU)] + KO),
    ed("1970", 1970, 1970, [_secao("venez70", "Copa Venezuela 1970")], [(r"^Group Stage", GRU)] + KO,
       obs="campeão Deportivo Galicia pelos jogos da final da RSSSF (2-0 e 1-1, de jornais de Caracas) e pela lista de campeões "
           "da RSSSF; a Wikipédia em espanhol dá o Deportivo Italia com os mesmos placares (decisão C3 do Guilherme, 24/11/2026: "
           "fica o Galicia)"),
    ed("1971", 1971, 1971, [_secao("venez71", "Copa Venezuela 1971")], [(r"^First Stage", GRU), (r"^Cuadrangular Final", FFIN)] + KO,
       obs=_TABELA),
    ed("1972", 1972, 1972, [_secao("venez72", "Copa Valencia")], KO, fase_padrao=GRU, obs="Copa Valencia; " + _TABELA),
    ed("1973", 1973, 1973, [_secao("venez73", "Copa Venezuela 1973")], [(r"^Group Stage", GRU)] + KO),
    ed("1975", 1975, 1975, [_secao("venez75", "Copa Venezuela 1975")], KO, fase_padrao=GRU, obs=_TABELA),
]
EDICOES += [ed(str(a), a, a, [_secao(f"venez{a % 100:02d}", f"Copa Venezuela {a}")], [(r"^Group Stage", GRU)] + KO)
            for a in (1976, 1977, 1978, 1979, 1980, 1981, 1982)]
EDICOES += [
    ed("1983", 1983, 1983, [_secao("venez83", "Copa Bicentenario")], [(r"^Group Stage", GRU), (r"^Cuadrangular", FFIN)] + KO,
       obs="Copa Bicentenario; " + _TABELA),
    ed("1985", 1985, 1985, [_secao("venez85", "Copa Venezuela 1985")], [(r"^Group Stage", GRU)] + KO),
    ed("1987", 1987, 1987, [_secao("venez88", "Copa Venezuela 1987")], KO, obs="a RSSSF só traz a final"),
    ed("1988", 1988, 1988, [_secao("venez89", "Copa Venezuela 1988")], KO, obs="a RSSSF só traz resultados conhecidos do mata-mata"),
    ed("1989", 1989, 1989, [], obs=_SEM_JOGOS),
    ed("1990", 1990, 1990, [], obs=_SEM_JOGOS),
    ed("1991", 1991, 1991, [_secao("venez92", "Copa Venezuela 1991")], [(r"^Group Stage", GRU)] + KO),
    ed("1992", 1992, 1992, [], obs=_SEM_JOGOS),
    ed("1993", 1993, 1994, [_ate(_secao("venez94", "Torneo Apertura (Copa"), "Overall Table")],
       [(r"^Group 1", GRU), (r"^Final Group", FFIN)] + KO,
       obs="Torneo Apertura da temporada 1993/94, que valia como Copa Venezuela; a RSSSF só traz as tabelas (os jogos da "
           "página são os do campeonato inteiro); campeão e vice da Wikipédia"),
    ed("1994", 1994, 1995, [_secao("venez95", "Torneo Apertura (Copa")], [(r"^First Stage", GRU), (r"^Final Round", FFIN)] + KO,
       obs="Torneo Apertura da temporada 1994/95, que valia como Copa Venezuela"),
    ed("1995", 1995, 1996, [_secao("venez96", "Torneo Apertura (Copa")], [(r"^Final Tables", GRU)] + KO,
       extras=_cruzadas_1995, obs="Torneo Apertura da temporada 1995/96, que valia como Copa Venezuela; jogos dos grupos "
                                  "pelas tabelas de confrontos (sem datas)"),
    ed("2007", 2007, 2008, [_secao("venez08", "Copa Venezuela 2007/08")], FASES3 + KO, fase_padrao=P1,
       obs="a RSSSF chama de 2007/08 (final em abril de 2008)"),
    ed("2008", 2008, 2008, [_secao("venez09", "Copa Venezuela 2008")], FASES3 + KO),
    ed("2009", 2009, 2009, [_secao("venez2010", "Copa venezuela")], FASES3 + KO),
    ed("2010", 2010, 2010, [_secao("venez2011", "Copa Venezuela 2010")], FASES3 + KO),
    ed("2011", 2011, 2011, [_secao("venez2012", "Copa Venezuela 2011")], RODADAS + KO),
    ed("2012", 2012, 2012, [_secao("venez2013", "Copa Venezuela 2012")], RODADAS + KO),
    ed("2013", 2013, 2013, [_secao("venez2014", "Copa Venezuela 2013")], RODADAS + KO),
    ed("2014", 2014, 2014, [_secao("venez2015", "Copa Venezuela 2014")], [(r"^Preliminary Round", PRE)] + RODADAS + KO),
    ed("2015", 2015, 2015, [_secao("venez2016", "Copa Venezuela 2015")], RODADAS + KO),
    ed("2016", 2016, 2016, [_secao("venez2016", "Copa Venezuela 2016")], RODADAS + KO),
    ed("2017", 2017, 2017, [_secao("venez2017", "Copa Venezuela 2017")], [(r"^Group Stage", GRU)] + FASES3[2:] + KO),
    ed("2018", 2018, 2018, [_secao("venez2018", "Copa Venezuela 2018")], [(r"^Final Tables", GRU)] + KO),
    ed("2019", 2019, 2019, [_secao("venez2019", "Copa Venezuela 2019")], FASES3 + KO),
    ed("2024", 2024, 2024, [_secao("venez2024", "Copa Venezuela 2024")], KO, obs="a RSSSF só traz das oitavas de final em diante"),
    ed("2025", 2025, 2025, [_secao("venez2025", "Copa Venezuela 2025")], [(r"^Group Stage", GRU)] + KO),
]
EDICOES.sort(key=lambda e: e.ano_inicio)

COMPETICAO = {
    "slug": SLUG, "nome": "Copa Venezuela", "nome_curto": "Copa Venezuela", "tipo": "copa", "nivel": None, "pais": "VEN",
    "pais_nome": "Venezuela", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Copa Venezuela",
    "menu_painel": "Venezuela · Copa Venezuela", "do_painel": "da Copa Venezuela", "o_painel": "a Copa Venezuela",
    "observacao": "Copa nacional da FVF pela contagem da Wikipédia: era amadora (1932-1953) e de 1959 em diante, com os nomes "
                  "de cada época (Copa Caracas, Cuatricentenario, Valencia, Bicentenario). Muitas edições antigas só têm a tabela "
                  "ou parte dos jogos; cinco não têm jogos (1938, 1949/50, 1989, 1990, 1992)."}

CAMPEOES_WIKI = {t: c for t, (c, _) in CAMPEOES.items()}

COPA = Copa(slug=SLUG, competicao=COMPETICAO, edicoes=EDICOES, fases=FASES, linhas=linhas, clube=clube, clubes=CLUBES,
            autores=autores, campeoes_wiki=CAMPEOES_WIKI, fonte_pagina="https://www.rsssf.org/tablesv/{pagina}.html",
            fases_pontos=[GRU, GR2, FFIN], ignorar=[r"\bxxx\b"])   # linhas das tabelas de confrontos (lidas à parte)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    importar(COPA, RELATORIO)
