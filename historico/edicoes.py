"""Configuracao de todas as edicoes do Brasileiro antigo e o comando que as importa.

Cada edicao declara so o que muda de ano para ano: a pagina-fonte, os cortes do
texto (fases), quantos jogos cada fase tem, os nomes de clube daquele ano e os
ajustes de erros da fonte. Leitura, conferencias e gravacao ficam em base.py.

Uso (na raiz do projeto):
    python historico/edicoes.py 1977              # uma edicao (ou varias)
    python historico/edicoes.py 1967              # as duas edicoes de 1967
    python historico/edicoes.py --todos           # todas, em ordem
    python historico/edicoes.py --lista           # lista as chaves

Os nomes de `nomes` valem so enquanto a propria edicao roda (o dicionario
CANONICAL e compartilhado; ex.: "santa cruz" e o de Sergipe so em 1961).
Depois de importar, rode `python -u build.py` (enriquece e gera o dashboard).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from base import (  # noqa: E402
    CANONICAL,
    ROOT,
    SCORE_RE,
    Fase,
    Game,
    canonical_name,
    corrigir_placar,
    gravar,
    key,
    norm,
    parse_ano,
    parse_date_token,
    read_pre,
    renomear_clube,
    separar_jogo,
    trocar_clube,
)


@dataclass
class Edicao:
    ano: int
    fonte: str
    fases: list[Fase] = field(default_factory=list)
    total: int = 0
    edicao: str | None = None        # dim_edicao_nacional.edicao_id quando nao e o "Campeonato Brasileiro" do ano
    arquivo: str | None = None       # pagina em data/ (padrao: rsssf_brazAA.html)
    corte_final: str | None = "Final Table"  # None: le a pagina inteira
    virada: int | None = None        # meses antes deste sao do ano seguinte
    blocos_pre: list[int] | None = None
    ignorar: tuple[str, ...] = ()    # comecos de linha de texto corrido a pular
    nomes: dict[str, str] = field(default_factory=dict)
    ajustar: Callable | None = None  # correcoes de erros da fonte
    jogos: list | None = None        # edicoes sem pagina de texto (1937): jogos escritos aqui
    ler: Callable | None = None      # leitor proprio quando o texto foge do padrao (1994): devolve os jogos


EDICOES: dict[str, Edicao] = {}

# ----------------------------------------------------------------------
# 1937
# Importa jogos da Copa dos Campeoes Estaduais 1937 (Torneio dos Campeoes).
#
# Reconhecida pela CBF como Campeonato Brasileiro em agosto de 2023 (Atletico-MG
# campeao). Fase preliminar com Alianca, Liga de Sports da Marinha e Rio Branco
# (ES); quadrangular em turno e returno com Atletico-MG, Fluminense, Rio Branco
# e Portuguesa.
#
# Fonte: Wikipedia PT, "Campeonato Brasileiro de Futebol de 1937" (a mesma da
# classificacao final ja no banco), que cita O Globo, Jornal do Brasil e
# Correio da Manha de janeiro e fevereiro de 1937. A RSSSF e o RSSSF Brasil nao
# tem pagina de jogos desta edicao. Os jogos da Wikipedia PT fecham exatamente
# com a tabela do quadrangular dela; a versao em ingles diverge em datas e
# traz Rio Branco 3-1 Portuguesa (aqui 3-2), que nao fecha com a tabela.
# Mandante = clube da casa (o estadio de cada jogo esta na fonte).

JOGOS_1937 = [
    ("Fase preliminar", 1, "mata_mata", "1937-01-06", "Aliança", 0, 2, "Liga da Marinha", "Campo da Usina, Campos dos Goytacazes."),
    ("Fase preliminar", 1, "mata_mata", "1937-01-11", "Rio Branco-ES", 2, 0, "Liga da Marinha", "Estadio Governador Bley, Vitoria. Apos prorrogacao."),
    ("Quadrangular final", 2, "grupo", "1937-01-10", "Portuguesa", 4, 1, "Fluminense", "Campo do Cambuci, Sao Paulo."),
    ("Quadrangular final", 2, "grupo", "1937-01-13", "Fluminense", 6, 0, "Atletico-MG", "Estadio das Laranjeiras, Rio de Janeiro."),
    ("Quadrangular final", 2, "grupo", "1937-01-13", "Rio Branco-ES", 3, 2, "Portuguesa", "Estadio Governador Bley, Vitoria."),
    ("Quadrangular final", 2, "grupo", "1937-01-17", "Rio Branco-ES", 1, 1, "Atletico-MG", "Estadio Governador Bley, Vitoria."),
    ("Quadrangular final", 2, "grupo", "1937-01-20", "Fluminense", 6, 2, "Portuguesa", "Estadio das Laranjeiras, Rio de Janeiro."),
    ("Quadrangular final", 2, "grupo", "1937-01-24", "Rio Branco-ES", 4, 3, "Fluminense", "Estadio Governador Bley, Vitoria."),
    ("Quadrangular final", 2, "grupo", "1937-01-24", "Atletico-MG", 5, 0, "Portuguesa", "Estadio de Lourdes, Belo Horizonte."),
    ("Quadrangular final", 2, "grupo", "1937-01-28", "Fluminense", 5, 2, "Rio Branco-ES", "Estadio das Laranjeiras, Rio de Janeiro."),
    ("Quadrangular final", 2, "grupo", "1937-01-31", "Atletico-MG", 4, 1, "Fluminense", "Estadio de Lourdes, Belo Horizonte."),
    ("Quadrangular final", 2, "grupo", "1937-01-31", "Portuguesa", 4, 0, "Rio Branco-ES", "Campo do Cambuci, Sao Paulo."),
    ("Quadrangular final", 2, "grupo", "1937-02-03", "Atletico-MG", 5, 1, "Rio Branco-ES", "Estadio de Lourdes, Belo Horizonte."),
    ("Quadrangular final", 2, "grupo", "1937-02-14", "Portuguesa", 2, 3, "Atletico-MG", "Campo do Cambuci, Sao Paulo."),
]

EDICOES["1937"] = Edicao(
    ano=1937,
    edicao="1937",
    fonte="https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_1937",
    jogos=JOGOS_1937,
)

# ----------------------------------------------------------------------
# 1959
# Importa jogos da Taca Brasil 1959 (16 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate quando cada clube vencia uma
# vez: grupos regionais nas zonas Norte e Sul, decisao de cada zona,
# semifinais (Santos e Vasco entraram direto) e final. Bahia campeao no
# terceiro jogo contra o Santos, em marco de 1960.

EDICOES["1959"] = Edicao(
    ano=1959,
    edicao="1959",
    fonte="https://www.rsssf.org/tablesb/brazcup59.html",
    arquivo="rsssf_brazcup59.html",
    corte_final="Taça Brasil champions",
    virada=7,
    nomes={
        "auto esporte": "Auto Esporte",  # Joao Pessoa-PB
        "ferroviario": "Ferroviário-MA",  # Sao Luis-MA
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 17, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 10, misto=True),
        Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 3, misto=True),
    ],
    total=35,
)

# ----------------------------------------------------------------------
# 1960
# Importa jogos da Taca Brasil 1960 (17 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
# Norte e Sul, decisao de cada zona, semifinais e final (Palmeiras campeao
# contra o Fortaleza).

EDICOES["1960"] = Edicao(
    ano=1960,
    edicao="1960",
    fonte="https://www.rsssf.org/tablesb/brazcup60.html",
    arquivo="rsssf_brazcup60.html",
    corte_final="Taça Brasil Champions",
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 16, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 15, misto=True),
        Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 4, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
    ],
    total=37,
)

# ----------------------------------------------------------------------
# 1961
# Importa jogos da Taca Brasil 1961 (18 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
# Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao contra
# o Bahia).

EDICOES["1961"] = Edicao(
    ano=1961,
    edicao="1961",
    fonte="https://www.rsssf.org/tablesb/brazcup61.html",
    arquivo="rsssf_brazcup61.html",
    corte_final="Taça Brasil champions",
    nomes={
        "america": "America-RJ",  # a fonte escreve so "America" (Rio de Janeiro-GB)
        "santa cruz": "Santa Cruz-SE",  # o de Aracaju; o de Recife nao jogou em 1961
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 15, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 16, misto=True),
        Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
    ],
    total=38,
)

# ----------------------------------------------------------------------
# 1962
# Importa jogos da Taca Brasil 1962 (18 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
# Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao no terceiro jogo contra o Botafogo (4-3, 1-3 e 5-0), em abril de 1963).

EDICOES["1962"] = Edicao(
    ano=1962,
    edicao="1962",
    fonte="https://www.rsssf.org/tablesb/brazcup62.html",
    arquivo="rsssf_brazcup62.html",
    corte_final="Taça Brasil champions",
    virada=7,  # a final foi em 1963
    nomes={
        "comercial": "Comercial-PR",
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 21, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 10, misto=True),
        Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 3, misto=True),
    ],
    total=39,
)

# ----------------------------------------------------------------------
# 1963
# Importa jogos da Taca Brasil 1963 (20 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
# Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao contra o Bahia).

EDICOES["1963"] = Edicao(
    ano=1963,
    edicao="1963",
    fonte="https://www.rsssf.org/tablesb/brazcup63.html",
    arquivo="rsssf_brazcup63.html",
    corte_final="Taça Brasil champions",
    virada=7,  # a final foi em janeiro de 1964
    nomes={
        "atletico": "Atletico-MG",
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 23, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 16, misto=True),
        Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 4, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
    ],
    total=45,
)

# ----------------------------------------------------------------------
# 1964
# Importa jogos da Taca Brasil 1964 (22 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
# Norte e Sul, decisao de cada zona, semifinais e final (Santos campeao contra o Flamengo).

EDICOES["1964"] = Edicao(
    ano=1964,
    edicao="1964",
    fonte="https://www.rsssf.org/tablesb/brazcup64.html",
    arquivo="rsssf_brazcup64.html",
    corte_final="Taça Brasil champions",
    nomes={
        "atletico": "Atletico-MG",
        "gremio maringa": "GE Maringá",
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 23, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 20, misto=True),
        Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 4, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
    ],
    total=49,
)

# ----------------------------------------------------------------------
# 1965
# Importa jogos da Taca Brasil 1965 (22 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
# Norte e Sul, decisao de cada zona, quartas de final, semifinais e final
# (Santos campeao contra o Vasco). Nesta pagina as fases nacionais vem como
# "QUARTERFINALS", "Semifinal" e "Final".

EDICOES["1965"] = Edicao(
    ano=1965,
    edicao="1965",
    fonte="https://www.rsssf.org/tablesb/brazcup65.html",
    arquivo="rsssf_brazcup65.html",
    corte_final="Taça Brasil champions",
    nomes={
        "eletrovapo": "Eletrovapo-RJ",
        "gremio maringa": "GE Maringá",
        "guanabara": "Guanabara-DF",
        "olimpico": "Olímpico-AM",
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 21, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "QUARTERFINALS", "mata_mata", 16, misto=True),
        Fase("Quartas de final", "QUARTERFINALS", "\nSemifinal", "mata_mata", 5, misto=True),
        Fase("Semifinal", "\nSemifinal", "\nFinal", "mata_mata", 4, misto=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, misto=True),
    ],
    total=48,
)

# ----------------------------------------------------------------------
# 1966
# Importa jogos da Taca Brasil 1966 (22 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Mata-mata em ida e volta, com jogo de desempate: grupos regionais nas zonas
# Norte e Sul, decisao de cada zona, semifinais e final (Cruzeiro campeao
# contra o Santos, 6-2 e 3-2).

EDICOES["1966"] = Edicao(
    ano=1966,
    edicao="1966",
    fonte="https://www.rsssf.org/tablesb/brazcup66.html",
    arquivo="rsssf_brazcup66.html",
    corte_final="Taça Brasil champions",
    nomes={
        "ferroviario": "Ferroviário-PR",  # o de Curitiba
        "rabello": "Rabello-DF",
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "SOUTHERN ZONE", "mata_mata", 21, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "\nSEMIFINAL", "mata_mata", 19, misto=True),
        Fase("Semifinal", "\nSEMIFINAL", "\nFINAL", "mata_mata", 5, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 2, misto=True),
    ],
    total=47,
)

# ----------------------------------------------------------------------
# 1967_taca_brasil
# Importa jogos da Taca Brasil 1967 (21 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1967
# houve tambem o Robertao, outro campeonato reconhecido (edicao 1967_robertao).
# Mata-mata em ida e volta, com jogo de desempate: zonas Norte, Central e Sul,
# quartas de final, semifinais e final (Palmeiras campeao).

EDICOES["1967_taca_brasil"] = Edicao(
    ano=1967,
    edicao="1967_taca_brasil",
    fonte="https://www.rsssf.org/tablesb/brazcup67.html",
    arquivo="rsssf_brazcup67.html",
    corte_final="Taça Brasil champions",
    nomes={
        "atletico": "Atletico-MG",
        "ferroviario": "Ferroviário-PR",  # o de Curitiba
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "CENTRAL ZONE", "mata_mata", 26, misto=True),
        Fase("Zona Central", "CENTRAL ZONE", "SOUTHERN ZONE", "mata_mata", 17, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "QUARTERFINALS", "mata_mata", 6, misto=True),
        Fase("Quartas de final", "QUARTERFINALS", "SEMIFINALS", "mata_mata", 3, misto=True),
        Fase("Semifinal", "SEMIFINALS", "\nFINAL", "mata_mata", 6, misto=True),
        Fase("Final", "\nFINAL", "", "mata_mata", 3, misto=True),
    ],
    total=61,
)

# ----------------------------------------------------------------------
# 1967_robertao
# Importa jogos do Robertao 1967 (Torneio Roberto Gomes Pedrosa, 15 clubes).
#
# Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1967
# houve tambem a Taca Brasil (edicao 1967_taca_brasil).
# Primeira fase: turno unico entre os 15 clubes, com a classificacao em dois
# grupos (A e B); os 2 primeiros de cada grupo vao ao quadrangular final, em
# turno e returno (Palmeiras campeao).
#
# Fonte: RSSSF Brasil, em portugues e em varios blocos <pre>: le os blocos 0
# (primeira fase) e 2 (quadrangular). O bloco 3 ("Title match") repete o jogo
# decisivo Palmeiras 2 x 1 Gremio e fica de fora.

EDICOES["1967_robertao"] = Edicao(
    ano=1967,
    edicao="1967_robertao",
    fonte="https://rsssfbrasil.com/tablesr/rgp1967.htm",
    arquivo="rsssfbrasil_rgp1967.htm",
    blocos_pre=[0, 2],
    nomes={
        "atletico mineiro": "Atletico-MG",
        "ferroviario": "Ferroviário-PR",
        "portuguesa de desportos": "Portuguesa",
    },
    fases=[
        Fase("Primeira fase", "1ª FASE", "CLASSIFICAÇÃO", "liga", 105),
        Fase("Quadrangular final", "QUADRANGULAR FINAL", "", "grupo", 12),
    ],
    total=117,
)

# ----------------------------------------------------------------------
# 1968_taca_brasil
# Importa jogos da Taca Brasil 1968 (21 clubes).
#
# Reconhecida pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1968
# houve tambem o Robertao, outro campeonato reconhecido (edicao 1968_robertao).
# Zonas Norte, Central e Sul (com triangulares regionais em turno e returno,
# que no painel aparecem como confrontos), quartas de final, semifinais e final
# (Botafogo campeao). A edicao terminou em 1969; as datas trazem "/69".

EDICOES["1968_taca_brasil"] = Edicao(
    ano=1968,
    edicao="1968_taca_brasil",
    fonte="https://www.rsssf.org/tablesb/brazcup68.html",
    arquivo="rsssf_brazcup68.html",
    corte_final="Taça Brasil champions",
    nomes={
        "operario": "Operário-MT",  # a classificacao do banco usa o de Mato Grosso
    },
    fases=[
        Fase("Zona Norte", "NORTHERN ZONE", "CENTRAL ZONE", "mata_mata", 25, misto=True),
        Fase("Zona Central", "CENTRAL ZONE", "SOUTHERN ZONE", "mata_mata", 13, misto=True),
        Fase("Zona Sul", "SOUTHERN ZONE", "QUARTERFINALS", "mata_mata", 6, misto=True),
        Fase("Quartas de final", "QUARTERFINALS", "SEMIFINAL", "mata_mata", 2, misto=True),
        Fase("Semifinal", "SEMIFINAL", "\nFinal", "mata_mata", 5, misto=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, misto=True),
    ],
    total=53,
)

# ----------------------------------------------------------------------
# 1968_robertao
# Importa jogos do Robertao 1968 (Torneio Roberto Gomes Pedrosa, 17 clubes).
#
# Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010). Em 1968
# houve tambem a Taca Brasil (edicao 1968_taca_brasil).
# Primeira fase: turno unico entre os 17 clubes, com a classificacao em dois
# grupos (A e B); os 2 primeiros de cada grupo vao ao quadrangular final, em
# turno unico (Santos campeao).
#
# Fonte: RSSSF Brasil ("TIME 1 x 0 TIME", datas 06.09.1968). A pagina repete
# as tabelas e a fase final depois do quadro do campeao; a leitura para no
# primeiro "Table" da fase final.

EDICOES["1968_robertao"] = Edicao(
    ano=1968,
    edicao="1968_robertao",
    fonte="https://rsssfbrasil.com/tablesr/rgp1968.htm",
    arquivo="rsssfbrasil_rgp1968.htm",
    nomes={
        "atletico mineiro": "Atletico-MG",
        "portuguesa de desportos": "Portuguesa",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Tables", "liga", 136),
        Fase("Fase final", "Final Phase", "Table", "grupo", 6),
    ],
    total=142,
)

# ----------------------------------------------------------------------
# 1969
# Importa jogos do Robertao 1969 (Torneio Roberto Gomes Pedrosa, 17 clubes).
#
# Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Primeira fase: turno unico entre os 17 clubes, com a classificacao em dois
# grupos (A e B); os 2 primeiros de cada grupo vao a fase final. Fase final:
# quadrangular em turno unico (Palmeiras campeao).
#
# Fonte: RSSSF Brasil (a pagina da RSSSF de 1969 so traz as tabelas). Formato
# "TIME 1 x 0 TIME" e datas 06.09.1969; a leitura para no "Title Match", que
# repete o ultimo jogo.

EDICOES["1969"] = Edicao(
    ano=1969,
    edicao="1969",
    fonte="https://rsssfbrasil.com/tablesr/rgp1969.htm",
    arquivo="rsssfbrasil_rgp1969.htm",
    corte_final="Title Match",
    nomes={
        "america": "America-RJ",
        "atletico mineiro": "Atletico-MG",
        "portuguesa de desportos": "Portuguesa",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Tables", "liga", 136),
        Fase("Fase final", "Final Phase", "", "grupo", 6),
    ],
    total=142,
)

# ----------------------------------------------------------------------
# 1970
# Importa jogos do Robertao 1970 (Torneio Roberto Gomes Pedrosa, 17 clubes).
#
# Reconhecido pela CBF como Campeonato Brasileiro (unificacao de 2010).
# Primeira fase: turno unico entre os 17 clubes, com a classificacao em dois
# grupos (A e B); os 2 primeiros de cada grupo vao a fase final. Fase final:
# quadrangular em turno unico (Fluminense campeao).
#
# Fonte: RSSSF Brasil. A lista de jogos da RSSSF (braz70.html) tem placares que
# nao fecham com a tabela dela mesma (ex.: Sao Paulo 1-0 Palmeiras, que no RSSSF
# Brasil e 0-2, com os autores dos gols); a do RSSSF Brasil fecha.

EDICOES["1970"] = Edicao(
    ano=1970,
    edicao="1970",
    fonte="https://rsssfbrasil.com/tablesr/rgp1970.htm",
    arquivo="rsssfbrasil_rgp1970.htm",
    nomes={
        "america": "America-RJ",  # a fonte escreve so "America"
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Tables", "liga", 136),
        Fase("Fase final", "Final Phase", "", "grupo", 6),
    ],
    total=142,
)

# ----------------------------------------------------------------------
# 1971
# Importa jogos do Brasileiro 1971 (1o Campeonato Nacional, 20 clubes).
#
# Primeira fase: turno unico entre os 20 clubes, com a classificacao em dois
# grupos (A e B). Segunda fase: tres grupos de 4 (turno e returno). Triangular
# final em turno unico (Atletico-MG campeao, sobre Sao Paulo e Botafogo).

EDICOES["1971"] = Edicao(
    ano=1971,
    fonte="https://www.rsssf.org/tablesb/braz71.html",
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "liga", 190),
        Fase("Segunda fase", "Second Phase", "Final Playoff", "grupo", 36),
        Fase("Triangular final", "Final Playoff", "", "grupo", 3),
    ],
    total=229,
)

# ----------------------------------------------------------------------
# 1972
# Importa jogos do Brasileiro 1972 (2o Campeonato Nacional, 26 clubes).
#
# Primeira fase: turno unico entre os 26 clubes, com a classificacao em quatro
# grupos (A a D). Segunda fase: quatro grupos de 4 (turno unico). Semifinais e
# final em jogo unico (0-0 com o Botafogo; Palmeiras campeao pela campanha).
# A pagina da RSSSF nao tem "Final Table".

def _ajustar_1972(games):
    # ABC 2-1 Botafogo: o ABC escalou tres jogadores irregulares e os pontos
    # foram dados ao Botafogo (a fonte nao marca "awd"). Gravado 0-1, como os
    # outros jogos decididos no tribunal sem placar atribuido.
    return corrigir_placar(games, "Primeira fase", "ABC", "Botafogo", 0, 1,
                           "Pontos dados ao Botafogo no tribunal (ABC com tres jogadores irregulares); em campo, 2-1 para o ABC. Placar tratado como 0-1.")

EDICOES["1972"] = Edicao(
    ano=1972,
    fonte="https://www.rsssf.org/tablesb/braz72.html",
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "liga", 325),
        Fase("Segunda fase", "Second Phase", "Semifinals", "grupo", 24),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 2),
        Fase("Final", "\nFinal", "", "mata_mata", 1),
    ],
    total=352,
    ajustar=_ajustar_1972,
)

# ----------------------------------------------------------------------
# 1973
# Importa jogos do Brasileiro 1973 (3o Campeonato Nacional, 40 clubes).
#
# Primeira fase em dois estagios (28 jogos por clube). Segunda fase: dois
# grupos de 10 (turno unico), em janeiro e fevereiro de 1974. Quadrangular
# final em turno unico (Palmeiras campeao). A pagina da RSSSF nao tem
# "Final Table".

EDICOES["1973"] = Edicao(
    ano=1973,
    fonte="https://www.rsssf.org/tablesb/braz73.html",
    virada=7,  # jogos de janeiro a junho sao de 1974
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "liga", 560),
        Fase("Segunda fase", "Second Phase", "Final Playoff", "grupo", 90),
        Fase("Quadrangular final", "Final Playoff", "", "grupo", 6),
    ],
    total=656,
)

# ----------------------------------------------------------------------
# 1974
# Importa jogos do Brasileiro 1974 (Campeonato Nacional, 40 clubes).
#
# Primeira fase: dois grupos de 20 (A e B), turno unico. Fase semifinal:
# quatro grupos (1 a 4). Fase final: quadrangular em turno unico com Cruzeiro,
# Vasco, Santos e Internacional; Cruzeiro e Vasco empataram em pontos e
# fizeram um jogo extra no Maracana (Vasco campeao, 2-1).

EDICOES["1974"] = Edicao(
    ano=1974,
    fonte="https://www.rsssf.org/tablesb/braz74.html",
    fases=[
        Fase("Primeira fase", "First Phase", "Semifinal Phase", "grupo", 380),
        Fase("Fase semifinal", "Semifinal Phase", "Final Phase", "grupo", 60),
        Fase("Fase final", "Final Phase", "Final Match", "grupo", 6),
        Fase("Final", "Final Match", "", "mata_mata", 1),
    ],
    total=447,
)

# ----------------------------------------------------------------------
# 1975
# Importa jogos do Brasileiro 1975 (Copa Brasil, 42 clubes).
#
# Primeira fase: grupos A e B (10 clubes cada, jogando contra o outro grupo)
# e grupos C e D (11 clubes cada, tambem jogando contra o outro grupo). Segunda fase: grupos 1 e
# 2 (20 clubes, jogando contra o outro grupo) e repescagem nos grupos 3 a 6.
# Terceira fase: dois grupos de 8. Semifinais e final em jogo unico
# (Internacional campeao contra o Cruzeiro). Vitoria por 2 gols ou mais valia
# 3 pontos; as demais, 2. A pagina da RSSSF nao tem "Final Table": a tabela
# final vem logo depois da frase do campeao.

EDICOES["1975"] = Edicao(
    ano=1975,
    fonte="https://www.rsssf.org/tablesb/braz75.html",
    corte_final="are the 1975 Brazilian champions",
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 221),
        Fase("Segunda fase", "Groups 1 and 2", "Group 3", "grupo", 100),
        Fase("Repescagem", "Group 3", "Third Phase", "grupo", 50),
        Fase("Terceira fase", "Third Phase", "Semifinals", "grupo", 56),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 2),
        Fase("Final", "\nFinal", "", "mata_mata", 1),
    ],
    total=430,
)

# ----------------------------------------------------------------------
# 1976
# Importa jogos do Brasileiro 1976 (Copa Brasil, 54 clubes).
#
# Primeira fase: seis grupos (A a F). Os 4 primeiros de cada grupo vao a
# segunda fase (grupos G a J); os demais, a repescagem (grupos K a P), que
# tambem da vagas a terceira fase. Terceira fase: dois grupos (Q e R).
# Semifinais e final em jogo unico (Internacional campeao contra o
# Corinthians). Vitoria por 3 gols ou mais valia 3 pontos; as demais, 2.

EDICOES["1976"] = Edicao(
    ano=1976,
    fonte="https://www.rsssf.org/tablesb/braz76.html",
    nomes={
        "operario": "Operário-MS",  # Operario de Campo Grande
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 216),
        Fase("Segunda fase", "Second Phase", "Group K", "grupo", 60),
        Fase("Repescagem", "Group K", "Third Phase", "grupo", 60),
        Fase("Terceira fase", "Third Phase", "Semifinal", "grupo", 72),
        Fase("Semifinal", "Semifinal", "\nFinal", "mata_mata", 2),
        Fase("Final", "\nFinal", "", "mata_mata", 1),
    ],
    total=411,
)

# ----------------------------------------------------------------------
# 1977
# Importa jogos do Brasileiro 1977 (Copa Brasil, 62 clubes).
#
# Primeira fase: seis grupos (A a F). Os 5 primeiros de cada grupo vao aos
# grupos de vencedores da segunda fase (G a L); os demais, aos grupos de
# perdedores (M a R), que tambem dao vagas a fase final. Fase final: quatro
# grupos (S a V). Semifinais em ida e volta e final em jogo unico (Sao Paulo
# campeao nos penaltis contra o Atletico-MG, em marco de 1978). Vitoria por
# 3 gols ou mais valia 3 pontos; as demais, 2.

def _ajustar_1977(games):
    # Desportiva x Fluminense-BA (grupo de perdedores): o Fluminense-BA
    # abandonou o jogo, subornado pela federacao baiana, para a Desportiva nao
    # tirar a vaga do Vitoria-BA. A RSSSF conta o jogo como 0-0. A CBD mandou
    # fazer um jogo extra Desportiva x Vitoria-BA; o Vitoria nao foi e a vaga
    # ficou com a Desportiva (jogo nao disputado, fora da base).
    return corrigir_placar(games, "Repescagem", "Desportiva-ES", "Fluminense-BA", 0, 0,
                           "Jogo abandonado pelo Fluminense-BA (suborno da federacao baiana); contado como 0-0, como na RSSSF.")

EDICOES["1977"] = Edicao(
    ano=1977,
    fonte="https://www.rsssf.org/tablesb/braz77.html",
    virada=7,  # jogos de janeiro a junho sao de 1978
    nomes={
        "xv de novembro": "XV de Piracicaba",
        "operario": "Operário-MS",  # Operario de Campo Grande
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 290),
        Fase("Segunda fase", "Winners Groups", "Losers Groups", "grupo", 60),
        Fase("Repescagem", "Losers Groups", "Final Phase", "grupo", 70),
        Fase("Fase final", "Final Phase", "Semifinals", "grupo", 60),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 1),
    ],
    total=485,
    ajustar=_ajustar_1977,
)

# ----------------------------------------------------------------------
# 1978
# Importa jogos do Brasileiro 1978 (Copa Brasil, 74 clubes).
#
# Primeira fase: seis grupos (A a F). Os 6 primeiros de cada grupo vao a
# segunda fase (grupos G a J); os demais disputam a repescagem (grupos K a P),
# em paralelo, que devolve um clube. Terceira fase: quatro grupos (Q a T).
# Quartas, semifinais e final em ida e volta (Guarani campeao contra o
# Palmeiras). Vitoria por 3 gols ou mais valia 3 pontos; as demais, 2.

def _ajustar_1978(games):
    # Operario de Campo Grande aparece como "-MT" (o Mato Grosso do Sul so
    # passou a valer em 1979); no banco e o Operario-MS.
    games = renomear_clube(games, "Operario-MT", "Operário-MS")
    # Quartas: "Internacional 1-0 1-2 Santa Cruz" - a volta veio do ponto de
    # vista do mandante. O Inter venceu por 2-1 em Recife e foi a semifinal;
    # a tabela final da RSSSF confirma.
    games = corrigir_placar(games, "Quartas de final", "Santa Cruz", "Internacional", 1, 2,
                            "Volta corrigida: a RSSSF escreve 1-2 do ponto de vista do mandante.")
    # Segunda fase: "Juventude 1-1 America-SP" esta no grupo do America-RJ.
    return trocar_clube(games, "Segunda fase", "Juventude", "1-1", "America-SP", "America-SP", "America-RJ",
                        "Na RSSSF aparece 'America-SP'; o adversario do grupo era o America-RJ.")

EDICOES["1978"] = Edicao(
    ano=1978,
    fonte="https://www.rsssf.org/tablesb/braz78.html",
    nomes={
        "xv de novembro": "XV de Piracicaba",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 420),
        Fase("Segunda fase", "Second Phase", "Respescagem", "grupo", 144),
        Fase("Repescagem", "Respescagem", "Third Phase", "grupo", 102),
        Fase("Terceira fase", "Third Phase", "Quarterfinals", "grupo", 112),
        Fase("Quartas de final", "Quarterfinals", "Semifinal", "mata_mata", 8, ida_volta=True),
        Fase("Semifinal", "Semifinal", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
    ],
    total=792,
    ajustar=_ajustar_1978,
)

# ----------------------------------------------------------------------
# 1979
# Importa jogos do Brasileiro 1979 (Copa Brasil, 94 clubes).
#
# Primeira fase: oito grupos (A a H); 14 clubes entram direto na segunda fase.
# Segunda fase: sete grupos (I a O), com Palmeiras e Guarani de folga. Terceira
# fase: quatro grupos de 4 (P a S), turno unico. Semifinais e final em ida e
# volta (Internacional campeao invicto contra o Vasco).

def _ajustar_1979(games):
    # Jogos sem placar na fonte ficam 1-0 para quem recebeu os pontos (mesma
    # regra do importador de 1986). A RSSSF conta esses jogos sem gols, entao
    # os gols destes clubes ficam 1 acima da tabela dela.
    # Sao Paulo-RS x Operario-PR (grupo B): em campo 0-1, mas o Operario ficou
    # com 6 jogadores aos 85' e os pontos foram dados ao Sao Paulo-RS.
    games = corrigir_placar(games, "Primeira fase", "Sao Paulo-RS", "Operario-PR", 1, 0,
                            "Pontos dados ao Sao Paulo-RS no tribunal (Operario com 6 jogadores aos 85'); em campo, 0-1. Placar tratado como 1-0.")
    # Atletico-MG abandonou a terceira fase: W.O. para Goias e Internacional.
    games = corrigir_placar(games, "Terceira fase", "Goias", "Atletico-MG", 1, 0,
                            "Nao disputado: o Atletico-MG abandonou a terceira fase; pontos ao Goias. Placar tratado como 1-0.")
    games = corrigir_placar(games, "Terceira fase", "Atletico-MG", "Internacional-RS", 0, 1,
                            "Nao disputado: o Atletico-MG abandonou a terceira fase; pontos ao Internacional. Placar tratado como 0-1.")
    # Segunda fase: "Sao Paulo-RS 1-0 Goias" e do grupo do Goytacaz (o Goias
    # estava em outro grupo); erro de digitacao da fonte.
    return trocar_clube(games, "Segunda fase", "Sao Paulo-RS", "1-0", "Goias", "Goias", "Goytacaz",
                        "Na RSSSF aparece 'Goias'; o adversario do grupo era o Goytacaz.")

EDICOES["1979"] = Edicao(
    ano=1979,
    fonte="https://www.rsssf.org/tablesb/braz79.html",
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 359),
        Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 194),
        Fase("Terceira fase", "Third Phase", "Semifinal", "grupo", 24),
        Fase("Semifinal", "Semifinal", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
    ],
    total=583,
    ajustar=_ajustar_1979,
)

# ----------------------------------------------------------------------
# 1980
# Importa jogos do Brasileiro 1980 (Taca de Ouro, 44 clubes).
#
# Primeira fase: quatro grupos de 10 (A a D), turno unico. Segunda fase: oito
# grupos de 4 (E a L), com quatro clubes vindos da Taca de Prata (America-SP,
# Americano, Bangu e Sport). Terceira fase: quatro grupos de 4 (M a P), turno
# unico. Semifinais e final em ida e volta (Flamengo campeao contra o
# Atletico-MG, pela melhor campanha na semifinal).

def _ajustar_1980(games):
    # O desempate Guarani 3-2 America-RJ (2o lugar do grupo I) esta no meio
    # da segunda fase; separado para nao entrar na tabela do grupo. A RSSSF
    # tambem nao o soma na tabela final.
    return separar_jogo(games, "Segunda fase", "Guarani", "3-2", "America-RJ", "Desempate",
                        "Desempate pelo 2o lugar do grupo I da segunda fase.")

EDICOES["1980"] = Edicao(
    ano=1980,
    fonte="https://www.rsssf.org/tablesb/braz80.html",
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 180),
        Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 97),
        Fase("Terceira fase", "Third Phase", "Semifinals", "grupo", 24),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
    ],
    total=307,
    ajustar=_ajustar_1980,
)

# ----------------------------------------------------------------------
# 1981
# Importa jogos do Brasileiro 1981 (Taca de Ouro, 44 clubes).
#
# Primeira fase: quatro grupos de 10 (A a D), turno unico. Segunda fase: oito
# grupos de 4 (E a L), com quatro clubes vindos da Taca de Prata (Nautico,
# Bahia, Palmeiras e Uberaba). Oitavas, quartas, semifinais e final em ida e
# volta (Gremio campeao contra o Sao Paulo).

EDICOES["1981"] = Edicao(
    ano=1981,
    fonte="https://www.rsssf.org/tablesb/braz81.html",
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 180),
        Fase("Segunda fase", "Second Phase", "1/8 Finals", "grupo", 96),
        Fase("Oitavas de final", "1/8 Finals", "Quarterfinals", "mata_mata", 16, ida_volta=True),
        Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
    ],
    total=306,
)

# ----------------------------------------------------------------------
# 1982
# Importa jogos do Brasileiro 1982 (Taca de Ouro, 44 clubes).
#
# Primeira fase: oito grupos de 5 (A a H), turno e returno. Os quartos
# colocados disputam a repescagem (jogo unico, fora da tabela final da RSSSF).
# Segunda fase: oito grupos de 4 (J a Q), com quatro clubes vindos da Taca de
# Prata (America-RJ, Athletico-PR, Corinthians e Sao Paulo-RS). Terceira e
# quarta fases, semifinais em ida e volta e final em melhor de 3 (Flamengo
# campeao no terceiro jogo, contra o Gremio).

EDICOES["1982"] = Edicao(
    ano=1982,
    fonte="https://www.rsssf.org/tablesb/braz82.html",
    nomes={
        "xv de novembro": "XV de Jaú",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Playoff (Repescagem)", "grupo", 160),
        Fase("Repescagem", "Playoff (Repescagem)", "Second Phase", "mata_mata", 4),
        Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 96),
        Fase("Terceira fase", "Third Phase", "Fourth Phase", "mata_mata", 16, ida_volta=True),
        Fase("Quarta fase", "Fourth Phase", "Semifinals", "mata_mata", 8, ida_volta=True),
        Fase("Semifinal", "Semifinals", "\nFinals", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinals", "", "mata_mata", 3),
    ],
    total=291,
)

# ----------------------------------------------------------------------
# 1983
# Importa jogos do Brasileiro 1983 (Taca de Ouro, 44 clubes).
#
# Primeira fase: oito grupos de 5 (A a H), turno e returno. Os quartos
# colocados disputam o playoff (jogo unico, fora da tabela final da RSSSF);
# os quintos e os eliminados no playoff vao para a Taca de Prata. Quatro clubes
# da Taca de Prata (Americano, Botafogo-SP, Guarani e Uberaba) entram na
# segunda fase: oito grupos de 4 (I a P). Terceira fase: quatro grupos de 4.
# Quartas, semifinais e final em ida e volta (Flamengo campeao contra o Santos).
# A Taca de Prata, no fim da pagina, fica de fora.

def _ajustar_1983(games):
    # "Atletico-PR 2-1 0-1 Sao Paulo": a volta veio do ponto de vista do
    # mandante. O Athletico venceu por 1-0 no Morumbi (gol de Assis) e foi a
    # semifinal; a tabela final da propria RSSSF (11 V, 32-28) confirma.
    return corrigir_placar(games, "Quartas de final", "Sao Paulo", "Atletico-PR", 0, 1,
                           "Volta corrigida: a RSSSF escreve 0-1 do ponto de vista do mandante.")

EDICOES["1983"] = Edicao(
    ano=1983,
    fonte="https://www.rsssf.org/tablesb/braz83.html",
    fases=[
        Fase("Primeira fase", "First Phase", "\nPlayoff\n", "grupo", 160),
        Fase("Playoff", "\nPlayoff\n", "Second Phase", "mata_mata", 4),
        Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 96),
        Fase("Terceira fase", "Third Phase", "Quarterfinals", "grupo", 48),
        Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
    ],
    total=322,
    ajustar=_ajustar_1983,
)

# ----------------------------------------------------------------------
# 1984
# Importa jogos do Brasileiro 1984 (Copa Brasil, 41 clubes).
#
# Primeira fase: oito grupos de 5 (A a H), turno e returno. Os quartos
# colocados disputam a repescagem (jogo unico, fora da tabela final da RSSSF).
# Segunda fase: sete grupos de 4 (I a O). Terceira fase: quatro grupos de 4,
# com o Uberlandia vindo da Taca CBF. Quartas, semifinais e final em ida e
# volta (Fluminense campeao contra o Vasco).

EDICOES["1984"] = Edicao(
    ano=1984,
    fonte="https://www.rsssf.org/tablesb/braz84.html",
    fases=[
        Fase("Primeira fase", "First Phase", "\nRepescagem\n", "grupo", 160),
        Fase("Repescagem", "\nRepescagem\n", "Second Phase", "mata_mata", 4),
        Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 84),
        Fase("Terceira fase", "Third Phase", "Quarterfinals", "grupo", 48),
        Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
    ],
    total=310,
)

# ----------------------------------------------------------------------
# 1985
# Importa jogos do Brasileiro 1985 (Copa Brasil, 44 clubes).
#
# Primeira fase: grupos A e B (10 clubes cada, jogando contra o outro grupo nos
# dois estagios) e grupos C e D (12 clubes cada, turno e returno no proprio
# grupo). Segunda fase: quatro quadrangulares (E a H). Semifinais em ida e
# volta e final em jogo unico (Coritiba campeao nos penaltis contra o Bangu).
# A Taca CBF (2a divisao), no fim da pagina, fica de fora.

EDICOES["1985"] = Edicao(
    ano=1985,
    fonte="https://www.rsssf.org/tablesb/braz85.html",
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 464),
        Fase("Segunda fase", "Second Phase", "Semifinals", "grupo", 48),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 1),
    ],
    total=517,
)

# ----------------------------------------------------------------------
# 1986
# Copa Brasil 1986 no recorte de 48 clubes usado no projeto. A RSSSF lista
# tambem grupos inferiores/regionais; o banco e a classificacao final usam 48
# clubes: os grupos A-D da primeira fase e os quatro vencedores dos grupos E-H
# que entram na segunda fase (Treze, Central, Internacional-SP e Criciuma).

def _ajustar_1986(games):
    # Joinville x Sergipe: vitoria dada ao Joinville no tribunal (doping), sem
    # placar atribuido na fonte.
    return corrigir_placar(games, "Primeira fase", "Joinville", "Sergipe", 1, 0,
                           "Resultado atribuido por W.O.; placar tratado como 1-0 para fechar a tabela oficial.")

EDICOES["1986"] = Edicao(
    ano=1986,
    fonte="https://www.rsssf.org/tablesb/braz86.html",
    virada=3,  # jogos de janeiro e fevereiro sao de 1987
    ignorar=("but ", "protested", "It then decided", "Central won"),
    nomes={
        "america rj": "America-RJ",
        "atletico go": "Atletico-GO",
        "atletico pr": "Athletico-PR",
        "botafogo rj": "Botafogo-RJ",
        "botafogo pb": "Botafogo-PB",
        "comercial": "Comercial-MS",
        "fluminense rj": "Fluminense",
        "internacional rs": "Internacional",
        "internacional sp": "Inter de Limeira",
        "nacional": "Nacional-AM",
        "operario ms": "Operário-MS",
        "operario mt": "Operário-MT",
        "rio branco es": "Rio Branco-ES",
        "vasco da gama": "Vasco",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Group E", "grupo", 220),
        Fase("Segunda fase", "Second Phase", "Third Phase", "grupo", 288),
        Fase("Terceira fase", "Third Phase", "Quarterfinals", "mata_mata", 16, ida_volta=True),
        Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
        Fase("Semifinal", "Semifinals", "Final\n", "mata_mata", 4, ida_volta=True),
        Fase("Final", "Final\n", "", "mata_mata", 2, ida_volta=True),
    ],
    total=538,
    ajustar=_ajustar_1986,
)


# ----------------------------------------------------------------------
# 1987
# Modelagem: Modulo Verde/Copa Uniao completo (16 clubes, primeira fase,
# semifinais e final) mais a Final CBF entre os dois classificados do Modulo
# Amarelo (Guarani e Sport). A propria RSSSF registra esses dois jogos como
# provaveis e explica que Flamengo e Internacional nao disputaram o cruzamento
# imposto pela CBF. Isso preserva a classificacao final do banco: Sport,
# Guarani, Flamengo, Internacional e os demais 14 clubes do Modulo Verde.
# Formato da fonte: "PALMEIRAS 2 x CRUZEIRO 0", datas "11/sep/87".

def _ajustar_1987(games):
    # a Final CBF nao tem jogos na pagina: os dois sao acrescentados aqui
    return games + [
        Game(1987, "Final CBF", 4, "mata_mata", None, 1, None, "Guarani", "Sport", 0, 0,
             "https://www.rsssf.org/tablesb/braz87.html",
             "Final CBF entre campeoes do Modulo Amarelo; RSSSF registra placar como provavel."),
        Game(1987, "Final CBF", 4, "mata_mata", None, 1, None, "Sport", "Guarani", 1, 0,
             "https://www.rsssf.org/tablesb/braz87.html",
             "Final CBF entre campeoes do Modulo Amarelo; Sport campeao oficial pela CBF."),
    ]

EDICOES["1987"] = Edicao(
    ano=1987,
    fonte="https://www.rsssf.org/tablesb/braz87.html",
    corte_final="CR Flamengo were",
    ignorar=("Goal",),
    nomes={
        "atletico mg": "Atletico-MG",
        "botafogo": "Botafogo-RJ",
        "goias": "Goias",
        "vasco": "Vasco",
    },
    fases=[
        Fase("Primeira fase", "FIRST PHASE", "SEMIFINALS", "liga", 120, obs="Módulo Verde/Copa União."),
        Fase("Semifinal", "SEMIFINALS", "FINAL\n", "mata_mata", 4, obs="Módulo Verde/Copa União."),
        Fase("Final Copa Uniao", "FINAL\n", "", "mata_mata", 2, obs="Módulo Verde/Copa União."),
    ],
    total=128,
    ajustar=_ajustar_1987,
)


# ----------------------------------------------------------------------
# 1988
# Copa Uniao 1988, 24 clubes. Primeira fase em dois estagios: vitoria valia 3
# pontos; empate ia aos penaltis, com 2 pontos ao vencedor e 1 ao perdedor (a
# observacao "Penaltis: x-y" guarda a disputa). Quartas, semifinais e final em
# ida e volta (Bahia campeao contra o Internacional).

def _ajustar_1988(games):
    # Athletico-PR x Corinthians (6a rodada) nao esta na RSSSF; incluido pelo
    # oGol para fechar a tabela final. A fase e reordenada por rodada e data.
    fase1 = [g for g in games if g.fase == "Primeira fase"]
    resto = [g for g in games if g.fase != "Primeira fase"]
    fase1.append(Game(1988, "Primeira fase", 1, "liga", 6, len(fase1) + 1, "1988-10-02",
                      "Athletico-PR", "Corinthians", 0, 0,
                      "https://www.ogol.com.br/equipe/corinthians/todos-os-jogos?epoca_id=117&type=season",
                      "Jogo ausente na RSSSF; incluido por fechamento da tabela final. Penaltis: 6-5"))
    fase1.sort(key=lambda g: (g.rodada or 999, g.data or "", g.jogo or 999))
    return [replace(g, jogo=i + 1) for i, g in enumerate(fase1)] + resto

EDICOES["1988"] = Edicao(
    ano=1988,
    fonte="https://www.rsssf.org/tablesb/braz88.html",
    corte_final=None,  # a "Final Table" desta pagina fica antes das quartas
    nomes={
        "america": "America-RJ",
        "america rj": "America-RJ",
        "atletico mg": "Atletico-MG",
        "atletico pr": "Athletico-PR",
        "bangu": "Bangu",
        "criciuma": "Criciuma",
        "vasco da gama": "Vasco",
        "vitoria": "Vitoria",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Quarterfinals", "liga", 275),
        Fase("Quartas de final", "Quarterfinals", "Semifinals", "mata_mata", 8, ida_volta=True),
        Fase("Semifinal", "Semifinals", "Finals", "mata_mata", 4, ida_volta=True),
        Fase("Final", "Finals", "", "mata_mata", 2, ida_volta=True),
    ],
    total=290,
    ajustar=_ajustar_1988,
)


# ----------------------------------------------------------------------
# apoio dos ajustes de 1989-2002
def _rodadas_seguidas(games, fase, offset):
    """Segundo estagio que recomeca a contagem ("Round 1" de novo): soma
    `offset` a partir da primeira queda de rodada (1990: rodadas 11 a 19)."""
    out, maior, somar = [], 0, 0
    for g in games:
        if g.fase == fase and g.rodada:
            if g.rodada < maior and not somar:
                somar = offset
            maior = max(maior, g.rodada)
            g = replace(g, rodada=g.rodada + somar)
        out.append(g)
    return out


def _numerar_por_confronto(games, fases):
    """Mata-mata em linhas de jogo unico: o numero do jogo vira o do confronto
    (os dois jogos do mesmo par recebem o mesmo numero), por fase."""
    out, numero, conta = [], {}, {}
    for g in games:
        if g.fase in fases:
            par = (g.fase, frozenset((g.mandante, g.visitante)))
            if par not in numero:
                conta[g.fase] = conta.get(g.fase, 0) + 1
                numero[par] = conta[g.fase]
            g = replace(g, jogo=numero[par])
        out.append(g)
    return out


# ----------------------------------------------------------------------
# 1989
# 22 clubes; primeira fase em dois grupos de 11 (8 classificados por grupo);
# segunda fase com 16 clubes em dois grupos cruzados, com Sao Paulo e Vasco
# indo a final; torneio de rebaixamento entre 5 clubes apos a eliminacao do
# Coritiba; final em jogo unico porque o Vasco entrou com ponto bonus e venceu
# o Sao Paulo por 1-0. A pagina tambem traz a 2a divisao: a leitura para em
# "CAMPEONATO BRASILEIRO 1989".

def _ajustar_1989(games):
    games = corrigir_placar(games, "Primeira fase", "Coritiba", "Santos", 0, 1,
                            "Resultado atribuido por W.O.; Coritiba nao compareceu e foi eliminado.")
    # a RSSSF lista "Bahia 0-0 Vitoria" na 1a rodada do rebaixamento; a tabela
    # final e fontes cruzadas apontam Guarani
    games = trocar_clube(games, "Torneio de rebaixamento", "Bahia", "0-0", "Vitoria", "Vitoria", "Guarani",
                         "Fonte RSSSF traz Vitoria por engano; corrigido para Guarani por cruzamento com tabela final e calendarios externos.")
    # "Guarani 0-0 Athletico-PR" (22/11) falta na RSSSF e fecha a tabela
    rebaixamento = [g for g in games if g.fase == "Torneio de rebaixamento"]
    extra = Game(1989, "Torneio de rebaixamento", 3, "grupo", 5, len(rebaixamento) + 1, "1989-11-22",
                 "Guarani", "Athletico-PR", 0, 0, "https://rsssfbrasil.com/tablesae/br1989.htm",
                 "Jogo ausente no bloco RSSSF principal; incluido por cruzamento com tabela final e calendario externo.")
    i = max(k for k, g in enumerate(games) if g.fase == "Torneio de rebaixamento")
    return games[:i + 1] + [extra] + games[i + 1:]

EDICOES["1989"] = Edicao(
    ano=1989,
    fonte="https://www.rsssf.org/tablesb/braz89.html",
    corte_final="CAMPEONATO BRASILEIRO 1989",
    nomes={
        "atletico mg": "Atletico-MG",
        "atletico pr": "Athletico-PR",
        "botafogo": "Botafogo-RJ",
        "internacional sp": "Inter de Limeira",
        "internacional rs": "Internacional",
        "nautico": "Nautico",
        "vasco da gama": "Vasco",
        "vitoria": "Vitoria",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "Second Phase", "grupo", 110),
        Fase("Segunda fase", "Second Phase", "Relegation Tournament", "grupo", 64),
        Fase("Torneio de rebaixamento", "Relegation Tournament", "<strong>Final", "grupo", 19),
        Fase("Final", "<strong>Final", "", "mata_mata", 1,
             obs="Final em jogo unico; Vasco entrou com ponto bonus e foi campeao ao vencer."),
    ],
    total=195,
    ajustar=_ajustar_1989,
)


# ----------------------------------------------------------------------
# 1990
# 20 clubes em 2 grupos de 10, em 2 estagios (1o = contra o outro grupo; 2o =
# contra o proprio grupo); combinado, turno unico de 190 jogos, com as
# rodadas do 2o estagio numeradas de 11 a 19. Vencedores de grupo de cada
# estagio + 4 melhores campanhas vao as quartas; quartas, semi e final em ida
# e volta. Corinthians campeao (2-0 no agregado sobre o Sao Paulo). A fonte
# tem o typo "INERNACIONAL-SP" (= Inter de Limeira); Sao Jose e o de SP. A
# pagina tambem traz a 2a divisao (corte em "SEGUNDA DIVIS").

def _ajustar_1990(games):
    games = _rodadas_seguidas(games, "Primeira fase", 10)
    return _numerar_por_confronto(games, {"Quartas de final", "Semifinal", "Final"})

EDICOES["1990"] = Edicao(
    ano=1990,
    fonte="https://www.rsssf.org/tablesb/braz90.html",
    corte_final="SEGUNDA DIVIS",
    nomes={
        "atletico mg": "Atletico-MG",
        "botafogo": "Botafogo-RJ",
        "bragantino": "Bragantino",
        "goias": "Goias",
        "gremio": "Gremio",
        "inernacional sp": "Inter de Limeira",  # typo da fonte
        "internacional sp": "Inter de Limeira",
        "internacional rs": "Internacional",
        "nautico": "Nautico",
        "sao jose": "Sao Jose-SP",
        "sao paulo": "Sao Paulo",
        "vasco": "Vasco",
        "vitoria": "Vitoria",
    },
    fases=[
        Fase("Primeira fase", "FIRST STAGE", "QUARTERFINALS", "liga", 190),
        Fase("Quartas de final", "QUARTERFINALS", "SEMIFINALS", "mata_mata", 8),
        Fase("Semifinal", "SEMIFINALS", "FINALS", "mata_mata", 4),
        Fase("Final", "FINALS", "", "mata_mata", 2),
    ],
    total=204,
    ajustar=_ajustar_1990,
)


# ----------------------------------------------------------------------
# 1991
# 20 clubes, turno unico (190 jogos), 4 melhores as semifinais (ida e volta) e
# final (ida e volta). Sao Paulo campeao (1-0 no agregado sobre o Bragantino).

def _ajustar_1991(games):
    return corrigir_placar(games, "Primeira fase", "Fluminense", "Botafogo-RJ", 1, 0,
                           "Resultado dado pelo tribunal (jogo abandonado em 0-0 no 1o tempo por invasao de campo)")

EDICOES["1991"] = Edicao(
    ano=1991,
    fonte="https://www.rsssf.org/tablesb/braz91.html",
    nomes={
        "atletico mg": "Atletico-MG",
        "atletico mineiro": "Atletico-MG",
        "atletico pr": "Athletico-PR",
        "atletico paranaense": "Athletico-PR",
        "botafogo": "Botafogo-RJ",
        "bragantino": "Bragantino",
        "goias": "Goias",
        "gremio": "Gremio",
        "nautico": "Nautico",
        "sao paulo": "Sao Paulo",
        "vasco da gama": "Vasco",
        "vitoria": "Vitoria",
    },
    fases=[
        Fase("Primeira fase", "First Phase", "\nTable", "liga", 190),
        Fase("Semifinal", "Semifinals", "\nFinal", "mata_mata", 4, ida_volta=True),
        Fase("Final", "\nFinal", "", "mata_mata", 2, ida_volta=True),
    ],
    total=196,
    ajustar=_ajustar_1991,
)


# ----------------------------------------------------------------------
# 1992
# 20 clubes, turno unico (190 jogos); 8 melhores em 2 grupos de 4 (24 jogos);
# final em ida e volta. Flamengo campeao sobre o Botafogo. Formato
# "TIME 2 x TIME 0" com datas "11/sep/92" (como 1987).

EDICOES["1992"] = Edicao(
    ano=1992,
    fonte="https://www.rsssf.org/tablesb/braz92.html",
    nomes={
        "atletico mg": "Atletico-MG",
        "atletico pr": "Athletico-PR",
        "botafogo": "Botafogo-RJ",
        "goias": "Goias",
        "nautico": "Nautico",
        "sao paulo": "Sao Paulo",
        "sport": "Sport",
    },
    fases=[
        Fase("Primeira fase", "FIRST PHASE", "FINAL TABLE - FIRST PHASE", "liga", 190),
        Fase("Segunda fase", "SECOND PHASE", "FINAL TABLE - SECOND PHASE", "grupo", 24),
        Fase("Final", "FINALS", "CR FLAMENGO", "mata_mata", 2),
    ],
    total=216,
)


# ----------------------------------------------------------------------
# 1993
# 32 clubes em 4 grupos de 8 (224 jogos); repescagem dos grupos C e D
# (4 jogos; Remo e Vitoria passaram por melhor campanha); 8 clubes em 2
# grupos de 4 (24 jogos); final em ida e volta. Palmeiras campeao sobre o
# Vitoria. A fonte tem o typo "Coritnhians".

EDICOES["1993"] = Edicao(
    ano=1993,
    fonte="https://www.rsssf.org/tablesb/braz93.html",
    nomes={
        "america mg": "America-MG",
        "atletico mg": "Atletico-MG",
        "atletico pr": "Athletico-PR",
        "botafogo": "Botafogo-RJ",
        "ceara": "Ceara",
        "coritnhians": "Corinthians",  # typo da fonte
        "criciuma": "Criciuma",
        # a fonte escreve "DEPORTIVA" e "DESPORTIVA-ES"; e a mesma Desportiva-ES
        # dos outros anos (o importador antigo criava um clube "Desportiva" so de 1993)
        "deportiva": "Desportiva-ES",
        "desportiva": "Desportiva-ES",
        "desportiva es": "Desportiva-ES",
        "fortaleza": "Fortaleza",
        "gremio": "Gremio",
        "nautico": "Nautico",
        "parana": "Parana",
        "paysandu": "Paysandu",
        "sao paulo": "Sao Paulo",
        "sport": "Sport",
        "uniao s joao": "Uniao Sao Joao",
        "uniao sao joao": "Uniao Sao Joao",
        "uniao sao joao sp": "Uniao Sao Joao",
        "vitoria ba": "Vitoria",
    },
    fases=[
        Fase("Primeira fase", "FIRST STAGE", "FINAL TABLE - FIRST PHASE", "grupo", 224),
        Fase("Playoff", "GROUPS C and D - PLAYOFF", "SECOND PHASE", "mata_mata", 4,
             obs="Remo e Vitoria classificados por melhor campanha na primeira fase"),
        Fase("Segunda fase", "SECOND PHASE", "FINAL TABLE - SECOND PHASE", "grupo", 24),
        Fase("Final", "FINALS", "SE Palmeiras", "mata_mata", 2),
    ],
    total=254,
)


# ----------------------------------------------------------------------
# 1994
# 24 clubes em 4 grupos de 6 (120 jogos); 2a fase com 4 grupos de 8
# (176 jogos) e, no meio dela, a repescagem ("QUALIFY"); quartas, semi e
# final em ida e volta. Palmeiras campeao sobre o Corinthians. Leitor
# proprio: a repescagem vem misturada as rodadas da 2a fase e o mata-mata
# vem em colunas ("Palmeiras 3    Guarani 1      Pacaembu"), datas "30/11/94".

_XG_1994 = re.compile(r"^(.+?)\s+(\d+)\s+x\s+(.+?)\s+(\d+)\s*$", re.I)
_KO_1994 = re.compile(r"^(.+?)\s+(\d+)\s+(.+?)\s+(\d+)(?:\s+.+)?$")
_MESES = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
          "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
_FONTE_1994 = "https://www.rsssf.org/tablesb/braz94.html"


def _data_1994(line: str) -> str | None:
    s = line.strip()
    m = re.match(r"^(\d{1,2})/([a-z]{3})/(\d{2})$", s, flags=re.I)
    if m:
        return f"19{m.group(3)}-{_MESES[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2})", s)
    if m:
        return f"19{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
    return None


def _time_1994(value: str) -> str:
    s = value.strip().replace("(MG)", " MG").replace("-BA", " BA").replace("-SP", "")
    return canonical_name(re.sub(r"\s+", " ", s))


def _grupos_1994(bloco: str, fase: str, ordem: int, esperado: int) -> list[Game]:
    games: list[Game] = []
    rodada = data = None
    atual = fase
    contagem: dict[str, int] = {}
    for line in bloco.splitlines():
        rm = re.match(r"ROUND\s+(\d+)", line, flags=re.I)
        if rm:
            rodada, atual = int(rm.group(1)), fase
            continue
        if line.strip() == "QUALIFY":
            atual = "Repescagem"
            continue
        if re.match(r"GROUP", line.strip(), flags=re.I):
            atual = fase
            continue
        d = _data_1994(line)
        if d:
            data = d
            continue
        m = _XG_1994.match(line.strip())
        if not m:
            continue
        contagem[atual] = contagem.get(atual, 0) + 1
        games.append(Game(1994, atual, 3 if atual == "Repescagem" else ordem, "grupo", rodada, contagem[atual],
                          data, _time_1994(m.group(1)), _time_1994(m.group(3)),
                          int(m.group(2)), int(m.group(4)), _FONTE_1994, ""))
    if len(games) != esperado:
        raise SystemExit(f"1994 {fase}: esperava {esperado} jogos, encontrei {len(games)}")
    return games


def _mata_mata_1994(bloco: str, fase: str, ordem: int, esperado: int) -> list[Game]:
    games: list[Game] = []
    data = None
    confronto: dict[tuple[str, str], int] = {}
    for line in bloco.splitlines():
        d = _data_1994(line)
        if d:
            data = d
            continue
        m = _KO_1994.match(line.strip())
        if not m:
            continue
        casa, fora = _time_1994(m.group(1)), _time_1994(m.group(3))
        par = tuple(sorted([norm(casa), norm(fora)]))
        confronto.setdefault(par, len(confronto) + 1)
        games.append(Game(1994, fase, ordem, "mata_mata", None, confronto[par], data, casa, fora,
                          int(m.group(2)), int(m.group(4)), _FONTE_1994, ""))
    if len(games) != esperado:
        raise SystemExit(f"1994 {fase}: esperava {esperado} jogos, encontrei {len(games)}")
    return games


def _ler_1994() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz94.html")
    serie_a = text[:text.find("Brazil 1994 Second Division")]
    primeira = serie_a[serie_a.find("FIRST STAGE"):serie_a.find("TABLES\nFirst stage")]
    segunda = serie_a[serie_a.find("SECOND STAGE"):serie_a.find("THIRD STAGE")]
    terceira = serie_a[serie_a.find("THIRD STAGE"):serie_a.find("FINAL TABLE - 1994")]
    q = terceira.find("Quarter-finals")
    s = terceira.find("SEMIFINALS")
    f = terceira.find("FINALS", s + len("SEMIFINALS"))
    return (_grupos_1994(primeira, "Primeira fase", 1, 120)
            + _grupos_1994(segunda, "Segunda fase", 2, 176)
            + _mata_mata_1994(terceira[q:s], "Quartas de final", 4, 8)
            + _mata_mata_1994(terceira[s:f], "Semifinal", 5, 4)
            + _mata_mata_1994(terceira[f:], "Final", 6, 2))


EDICOES["1994"] = Edicao(
    ano=1994,
    fonte=_FONTE_1994,
    nomes={
        "atletico mg": "Atletico-MG",
        "botafogo": "Botafogo-RJ",
        "criciuma": "Criciuma",
        "gremio": "Gremio",
        "nautico": "Nautico",
        "parana": "Parana",
        "remô": "Remo",
        "remo": "Remo",
        "sao paulo": "Sao Paulo",
        "sport": "Sport",
        "uniao s joao": "Uniao Sao Joao",
        "uniao sao joao": "Uniao Sao Joao",
        "vitoria ba": "Vitoria",
    },
    ler=_ler_1994,
    total=310,
)


# ----------------------------------------------------------------------
# 1995
# 24 clubes em 2 turnos (132 + 144 jogos, com cruzamento de grupos);
# semifinais e final em ida e volta (Botafogo e Santos passaram por melhor
# campanha). Botafogo campeao sobre o Santos. Leitor proprio: a pagina mistura
# "PALMEIRAS 2x1 GOIAS" com data compacta na frente ("2408 ...") e datas "24/08/95".

_FONTE_1995 = "https://www.rsssf.org/tablesb/braz95.html"
_JOGO_1995 = re.compile(r"^(?:\s*(\d{4})\s+)?\s*([A-Z0-9 .()]+?)\s+(\d+)\s*[xX]\s*(\d+)\s+([A-Z0-9 .()]+?)\s*$")
_DATA_1995 = re.compile(r"^(\d{2})/(\d{2})/(\d{2})\s+")


def _time_1995(value: str) -> str:
    s = re.sub(r"\s+", " ", value.strip().replace(".", " "))
    return canonical_name(s.replace("(MG)", " MG").replace("(RS)", " RS").replace("(PE)", " PE"))


def _fase_1995(bloco: str, fase: str, ordem: int, tipo: str, esperado: int) -> list[Game]:
    games: list[Game] = []
    rodada = data = None
    for line in bloco.splitlines():
        rm = re.search(r"(?:Round|RODADA:)\s+(\d+)", line, flags=re.I)
        if rm:
            rodada = int(rm.group(1))
            continue
        dm = _DATA_1995.match(line.strip())
        if dm:
            data = f"19{dm.group(3)}-{int(dm.group(2)):02d}-{int(dm.group(1)):02d}"
            continue
        m = _JOGO_1995.match(line)
        if not m:
            continue
        d = f"1995-{int(m.group(1)[2:4]):02d}-{int(m.group(1)[:2]):02d}" if m.group(1) else data
        games.append(Game(1995, fase, ordem, tipo, rodada, len(games) + 1, d, _time_1995(m.group(2)),
                          _time_1995(m.group(5)), int(m.group(3)), int(m.group(4)), _FONTE_1995, ""))
    if len(games) != esperado:
        raise SystemExit(f"1995 {fase}: esperava {esperado} jogos, encontrei {len(games)}")
    return games


def _ler_1995() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz95.html")
    serie_a = text[:text.find("Brazil 1995 Second Division")]
    games = _fase_1995(serie_a[:serie_a.find("GROUP A")], "Primeiro turno", 1, "liga", 132)
    games += _fase_1995(serie_a[serie_a.find("SEGUNDO TURNO"):serie_a.find("TABELA DE CLASSIFICACAO - SEGUNDO TURNO")],
                        "Segundo turno", 2, "liga", 144)
    finais = _fase_1995(serie_a[serie_a.find("SEMIFINAIS E FINAL"):], "Semifinal", 3, "mata_mata", 6)
    games += [replace(g, jogo=1 if i < 2 else 2, observacao="Botafogo e Santos classificados por melhor campanha")
              for i, g in enumerate(finais[:4])]
    games += [replace(g, fase="Final", fase_ordem=4, jogo=1) for g in finais[4:]]
    return games


EDICOES["1995"] = Edicao(
    ano=1995,
    fonte=_FONTE_1995,
    nomes={
        "atletico": "Atletico-MG",
        "atletico mg": "Atletico-MG",
        "botafogo": "Botafogo-RJ",
        "criciuma": "Criciuma",
        "inter": "Internacional",
        "inter rs": "Internacional",
        "internacional": "Internacional",
        "paysandu": "Paysandu",
        "sao paulo": "Sao Paulo",
        "sport": "Sport",
        "sport pe": "Sport",
        "u s joao": "Uniao Sao Joao",
        "uniao s joao": "Uniao Sao Joao",
        "uniao sao joao": "Uniao Sao Joao",
    },
    ler=_ler_1995,
    total=282,
)


# ----------------------------------------------------------------------
# 1996 e 1997: turno unico com "Round N [Aug 4]" e "A 2-1 B [nota]" (como
# 1998-2001). A nota entre colchetes vai inteira para a observacao.

def _rodadas(bloco: str, ano: int, fonte: str, fase: str, ordem: int, tipo: str, abd: bool = False) -> list[Game]:
    """`abd`: le "A abd B [abandoned at 1-0" com o placar do abandono (1998-1999)."""
    games: list[Game] = []
    rodada = data = None
    for line in bloco.splitlines():
        rm = re.match(r"Round\s+(\d+)(?:\s+\[(.*?)\])?", line)
        if rm:
            rodada = int(rm.group(1))
            data = parse_date_token(rm.group(2).split(",")[0], ano) if rm.group(2) else None
            continue
        dm = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if dm:
            data = parse_date_token(dm.group(1), ano)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        am = abd and re.match(r"^(.+?)\s+abd\s+(.+?)\s+\[abandoned at\s+(\d+)-(\d+)", line)
        if am:
            games.append(Game(ano, fase, ordem, tipo, rodada, len(games) + 1, data, canonical_name(am.group(1)),
                              canonical_name(am.group(2)), int(am.group(3)), int(am.group(4)), fonte,
                              "abandoned; result apparently stood"))
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        games.append(Game(ano, fase, ordem, tipo, rodada, len(games) + 1, data,
                          canonical_name(re.sub(r"\s{2,}.*$", "", m.group(1)).strip()),
                          canonical_name(re.sub(r"\s{2,}.*$", "", m.group(4)).strip()),
                          int(m.group(2)), int(m.group(3)), fonte, m.group(5) or ""))
    return games


def _conferir(games: list[Game], esperado: int, onde: str) -> list[Game]:
    if len(games) != esperado:
        raise SystemExit(f"{onde}: esperava {esperado} jogos, encontrei {len(games)}")
    return games


def _secao(text: str, inicio: str, fim: str | None = None) -> str:
    """Trecho entre dois marcadores de comeco de linha (regex)."""
    i = re.search(inicio, text, flags=re.M)
    if not i:
        raise SystemExit(f"Secao nao encontrada: {inicio}")
    if not fim:
        return text[i.start():]
    j = re.search(fim, text[i.end():], flags=re.M)
    return text[i.start(): i.end() + j.start()] if j else text[i.start():]


# ----------------------------------------------------------------------
# 1996
# 24 clubes, turno unico (276 jogos); quartas, semi e final em ida e volta,
# em linhas compactas ("Gremio 0-2 2-0 Portuguesa") com as datas no
# cabecalho ("1st leg Dec 8; 2nd leg Dec 15"). Gremio campeao por melhor
# campanha (2-2 no agregado com a Portuguesa).

_FONTE_1996 = "https://www.rsssf.org/tablesb/braz96.html"


def _ida_volta_1996(bloco: str, fase: str, ordem: int, obs: str = "") -> list[Game]:
    linhas = bloco.splitlines()
    cab = linhas[0] if linhas else ""
    m = re.search(r"1st leg ([A-Z][a-z]{2} \d{1,2})(?:,\d{1,2})?; 2nd leg ([A-Z][a-z]{2} \d{1,2})(?:, [A-Z][a-z]{2} \d{1,2})?", cab)
    ida, volta = (parse_date_token(m.group(1), 1996), parse_date_token(m.group(2), 1996)) if m else (None, None)
    games: list[Game] = []
    confronto = 0
    for line in linhas[1:]:
        mm = re.match(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)\s*$", line)
        if not line.strip() or not mm:
            continue
        confronto += 1
        a = canonical_name(re.sub(r"\s{2,}.*$", "", mm.group(1)).strip())
        b = canonical_name(re.sub(r"\s{2,}.*$", "", mm.group(6)).strip())
        games.append(Game(1996, fase, ordem, "mata_mata", None, confronto, ida, a, b,
                          int(mm.group(2)), int(mm.group(3)), _FONTE_1996, obs))
        games.append(Game(1996, fase, ordem, "mata_mata", None, confronto, volta, b, a,
                          int(mm.group(5)), int(mm.group(4)), _FONTE_1996, obs))
    return games


def _ler_1996() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz96.html")
    i = text.find("Round 1")
    games = _conferir(_rodadas(text[i:text.find("\nTable:", i)], 1996, _FONTE_1996, "Primeira fase", 1, "liga"),
                      276, "1996 Primeira fase")
    mm = text[text.find("Quarterfinals"):text.find("Scorers")]
    games += _ida_volta_1996(_secao(mm, r"^Quarterfinals", r"^Semifinals"), "Quartas de final", 2)
    games += _ida_volta_1996(_secao(mm, r"^Semifinals", r"^FINAL"), "Semifinal", 3)
    games += _ida_volta_1996(_secao(mm, r"^FINAL"), "Final", 4, "Gremio campeao por melhor campanha")
    return games


EDICOES["1996"] = Edicao(
    ano=1996,
    fonte=_FONTE_1996,
    nomes={
        "atletico mineiro": "Atletico-MG",
        "atletico paranaense": "Athletico-PR",
        "atletico pr": "Athletico-PR",
        "botafogo": "Botafogo-RJ",
        "criciuma": "Criciuma",
        "gremio": "Gremio",
        "parana": "Parana",
        "sao paulo": "Sao Paulo",
        "sport club recife": "Sport",
    },
    ler=_ler_1996,
    total=290,
)


# ----------------------------------------------------------------------
# 1997
# 26 clubes, turno unico (325 jogos); 8 melhores em 2 grupos de 4 (24 jogos);
# final em ida e volta (0-0 e 0-0). Vasco campeao por melhor campanha.

_FONTE_1997 = "https://www.rsssf.org/tablesb/braz97.html"


def _ler_1997() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz97.html")
    i = text.find("Round 1")
    games = _conferir(_rodadas(text[i:text.find("\nTable:", i)], 1997, _FONTE_1997, "Primeira fase", 1, "liga"),
                      325, "1997 Primeira fase")
    s = text.find("Second Stage:")
    f = text.find("Final [Dec", s)
    games += _conferir(_rodadas(text[s:f], 1997, _FONTE_1997, "Grupo semifinal", 2, "grupo"), 24, "1997 Grupo semifinal")
    final = _rodadas("Round 1\n" + text[f:text.find("Topscorer", f)], 1997, _FONTE_1997, "Final", 3, "mata_mata")
    games += _conferir([replace(g, rodada=None, jogo=1,
                                observacao=(g.observacao + "; " if g.observacao else "") + "Vasco campeao por melhor campanha")
                        for g in final], 2, "1997 Final")
    return games


EDICOES["1997"] = Edicao(
    ano=1997,
    fonte=_FONTE_1997,
    nomes={
        "america rn": "America-RN",
        "america": "America-RN",
        "atletico mg": "Atletico-MG",
        "atletico pr": "Athletico-PR",
        "atletico paranaense": "Athletico-PR",
        "botafogo": "Botafogo-RJ",
        "criciuma": "Criciuma",
        "uniao sao joao": "União São João",
    },
    ler=_ler_1997,
    total=351,
)


# ----------------------------------------------------------------------
# 1998 e 1999: turno unico e mata-mata em series de ate 3 jogos
# ("First Leg [Nov 22]" ... "Third Leg"), numeradas por confronto.

def _series(bloco: str, ano: int, fonte: str, fase: str, ordem: int) -> list[Game]:
    games: list[Game] = []
    data = None
    confronto: dict[tuple[str, str], int] = {}
    for line in bloco.splitlines():
        lm = re.match(r"(First|Second|Third) Legs?\s*(?:\[(.*?)\])?", line.strip())
        if lm:
            data = parse_date_token(lm.group(2), ano) if lm.group(2) else data
            continue
        dm = re.match(r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]", line.strip())
        if dm:
            data = parse_date_token(dm.group(1), ano)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if not m:
            continue
        casa, fora = canonical_name(m.group(1)), canonical_name(m.group(4))
        par = tuple(sorted([norm(casa), norm(fora)]))
        confronto.setdefault(par, len(confronto) + 1)
        games.append(Game(ano, fase, ordem, "mata_mata", None, confronto[par], data, casa, fora,
                          int(m.group(2)), int(m.group(3)), fonte, m.group(5) or ""))
    return games


def _turno_unico(text: str, ano: int, fonte: str, clubes: int) -> list[Game]:
    i = text.find("Round 1")
    return _conferir(_rodadas(text[i:text.find("\nTable", i)], ano, fonte, "Primeira fase", 1, "liga", abd=True),
                     clubes * (clubes - 1) // 2, f"{ano} Primeira fase")


# 1998: 24 clubes (276 jogos); quartas, semi e final em series de ate 3 jogos.
# Corinthians campeao sobre o Cruzeiro.

_FONTE_1998 = "https://www.rsssf.org/tablesb/braz98.html"


def _ler_1998() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz98.html")
    games = _turno_unico(text, 1998, _FONTE_1998, 24)
    mm = _secao(text, r"^Championship Playoff", r"^Topscorers")
    games += _series(_secao(mm, r"^Quarterfinals", r"^Semifinals"), 1998, _FONTE_1998, "Quartas de final", 2)
    games += _series(_secao(mm, r"^Semifinals", r"^Final$"), 1998, _FONTE_1998, "Semifinal", 3)
    games += _series(_secao(mm, r"^Final$"), 1998, _FONTE_1998, "Final", 4)
    return games


# 1999: 22 clubes (231 jogos); quartas, semi e final em series de ate 3 jogos.
# Corinthians campeao sobre o Atletico-MG.

_FONTE_1999 = "https://www.rsssf.org/tablesb/braz99.html"


def _ler_1999() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz99.html")
    games = _turno_unico(text, 1999, _FONTE_1999, 22)
    mm = _secao(text, r"^Championship Playoff", r"^M.dias de rebaixamento")
    games += _series(_secao(mm, r"^First Round", r"^Second Round"), 1999, _FONTE_1999, "Quartas de final", 2)
    games += _series(_secao(mm, r"^Second Round", r"^Final$"), 1999, _FONTE_1999, "Semifinal", 3)
    games += _series(_secao(mm, r"^Final$"), 1999, _FONTE_1999, "Final", 4)
    return games


EDICOES["1998"] = Edicao(ano=1998, fonte=_FONTE_1998, ler=_ler_1998, total=297)
EDICOES["1999"] = Edicao(ano=1999, fonte=_FONTE_1999, ler=_ler_1999, total=250)


# ----------------------------------------------------------------------
# 2000 (Copa Joao Havelange)
# Modulo Azul com 25 clubes em turno unico (300 jogos, rodadas contadas pelas
# datas); oitavas, quartas, semi e final em ida e volta, com clubes dos
# modulos Amarelo e Verde/Branco. Vasco campeao sobre o Sao Caetano.

_FONTE_2000 = "https://www.rsssf.org/tablesb/braz-joao00.html"
_DATA_COLCHETE = r"\[(\w{3}\s+\d{1,2}(?:,\s*\d{4})?)\]"


def _ida_e_volta_2000(bloco: str, fase: str, ordem: int) -> list[Game]:
    games: list[Game] = []
    data = None
    perna = 0
    jogo = {1: 0, 2: 0}
    for line in bloco.splitlines():
        cab = re.match(r"First Legs?", line) and 1 or re.match(r"Second Leg", line) and 2
        if cab:
            perna = cab
            dm = re.search(_DATA_COLCHETE, line)
            if dm:
                data = parse_date_token(dm.group(1), 2000)
            continue
        dm = re.match(_DATA_COLCHETE, line.strip())
        if dm:
            data = parse_date_token(dm.group(1), 2000)
            continue
        if line.startswith(" ") or not line.strip() or " abd " in line or "aggregate winners" in line:
            continue
        m = SCORE_RE.match(line)
        if not m or perna not in (1, 2):
            continue
        jogo[perna] += 1
        games.append(Game(2000, fase, ordem, "mata_mata", None, jogo[perna], data, canonical_name(m.group(1)),
                          canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), _FONTE_2000, m.group(5) or ""))
    return games


def _ler_2000() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz_joao00.html")
    tabela = text.find("Table:", text.find("Blue Module"))
    primeira_data = re.search(r"^\[\w{3}\s+\d{1,2}", text[tabela:], flags=re.M)
    if not primeira_data:
        raise SystemExit("2000: primeira data do Modulo Azul nao encontrada")
    i = tabela + primeira_data.start()
    games: list[Game] = []
    data = None
    rodada = 0
    for line in text[i:text.find("\nTable:", i)].splitlines():
        dm = re.match(_DATA_COLCHETE, line.strip())
        if dm:
            data = parse_date_token(dm.group(1), 2000)
            rodada += 1
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if m:
            games.append(Game(2000, "Modulo Azul", 1, "liga", rodada, len(games) + 1, data, canonical_name(m.group(1)),
                              canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), _FONTE_2000, m.group(5) or ""))
    _conferir(games, 300, "2000 Modulo Azul")
    mm = text[text.find("Championship Playoffs"):text.find("Topscorers", text.find("Championship Playoffs"))]
    fases = [("1/8 Finals", "Oitavas de final"), ("Quarterfinals", "Quartas de final"),
             ("Semifinals", "Semifinal"), ("Final$", "Final")]
    pos = [re.search(rf"^{marca}", mm, flags=re.M).start() for marca, _ in fases] + [len(mm)]
    for ordem, (_, fase) in enumerate(fases, start=2):
        games += _ida_e_volta_2000(mm[pos[ordem - 2]:pos[ordem - 1]], fase, ordem)
    return games


EDICOES["2000"] = Edicao(ano=2000, fonte=_FONTE_2000, ler=_ler_2000, total=330)


# ----------------------------------------------------------------------
# 2001 e 2002: turno unico; mata-mata em jogo unico (quartas e semi de 2001) ou
# em linhas de ida e volta "A 1-2 3-1 B" com datas "[Dec 16 and 23]".

def _jogos_unicos(bloco: str, ano: int, fonte: str, fase: str, ordem: int) -> list[Game]:
    games: list[Game] = []
    data = None
    for line in bloco.splitlines():
        dm = re.match(_DATA_COLCHETE, line.strip())
        if dm:
            data = parse_date_token(dm.group(1), ano)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if m:
            games.append(Game(ano, fase, ordem, "mata_mata", None, len(games) + 1, data, canonical_name(m.group(1)),
                              canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), fonte, m.group(5) or ""))
    return games


def _linhas_ida_volta(bloco: str, ano: int, fonte: str, fase: str, ordem: int, nome=canonical_name) -> list[Game]:
    games: list[Game] = []
    datas: list[str] = []
    jogo = 0
    for line in bloco.splitlines():
        dm = re.match(r"\[(\w{3})\s+(\d{1,2})\s+and\s+(\d{1,2})\]", line.strip())
        if dm:
            datas = [parse_date_token(f"{dm.group(1)} {dm.group(2)}", ano),
                     parse_date_token(f"{dm.group(1)} {dm.group(3)}", ano)]
            continue
        m = re.match(r"^(.+?)\s+(\d+)-(\d+)\s+(\d+)-(\d+)\s+(.+?)\s*$", line)
        if not m:
            continue
        jogo += 1
        a, b = nome(m.group(1)), nome(m.group(6))
        a1, b1, a2, b2 = (int(m.group(i)) for i in range(2, 6))
        games.append(Game(ano, fase, ordem, "mata_mata", None, jogo, datas[0] if datas else None, a, b, a1, b1, fonte))
        games.append(Game(ano, fase, ordem, "mata_mata", None, jogo, datas[1] if len(datas) > 1 else None, b, a, b2, a2, fonte))
    return games


# 2001: 28 clubes (378 jogos); quartas e semi em jogo unico; final em ida e
# volta. Athletico-PR campeao sobre o Sao Caetano.

_FONTE_2001 = "https://www.rsssf.org/tablesb/braz01.html"


def _ler_2001() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz01.html")
    i = text.find("Round 1")
    games: list[Game] = []
    rodada = data = None
    for line in text[i:text.find("\nTable", i)].splitlines():
        rm = re.match(r"Round\s+(\d+)", line)
        if rm:
            rodada, data = int(rm.group(1)), None
            continue
        dm = re.match(_DATA_COLCHETE, line.strip())
        if dm:
            data = parse_date_token(dm.group(1), 2001)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = SCORE_RE.match(line)
        if m:
            games.append(Game(2001, "Primeira fase", 1, "liga", rodada, len(games) + 1, data, canonical_name(m.group(1)),
                              canonical_name(m.group(4)), int(m.group(2)), int(m.group(3)), _FONTE_2001, m.group(5) or ""))
    _conferir(games, 378, "2001 Primeira fase")
    q, s, f = text.find("Quarterfinals"), text.find("Semifinals"), text.find("Finals")
    games += _jogos_unicos(text[q:s], 2001, _FONTE_2001, "Quartas de final", 2)
    games += _jogos_unicos(text[s:f], 2001, _FONTE_2001, "Semifinal", 3)
    games += _linhas_ida_volta(text[f:text.find("First Leg")], 2001, _FONTE_2001, "Final", 4)
    return games


EDICOES["2001"] = Edicao(ano=2001, fonte=_FONTE_2001, ler=_ler_2001, total=386)


# 2002: 26 clubes (325 jogos); quartas, semi e final em ida e volta. Santos
# campeao sobre o Corinthians. Tem dicionario de nomes proprio (nao usa o
# CANONICAL comum): "Botafogo-RJ" na fonte vira "Botafogo" antes da busca.

_FONTE_2002 = "https://www.rsssf.org/tablesb/braz02.html"
_NOMES_2002 = {
    "atletico mg": "Atletico-MG", "atletico mineiro": "Atletico-MG",
    "atletico pr": "Athletico-PR", "atletico paranaense": "Athletico-PR",
    "athletico pr": "Athletico-PR", "bahia": "Bahia",
    "botafogo": "Botafogo-RJ", "botafogo rj": "Botafogo-RJ",
    "corinthians": "Corinthians", "coritiba": "Coritiba",
    "cruzeiro": "Cruzeiro", "figueirense": "Figueirense",
    "flamengo": "Flamengo", "fluminense": "Fluminense",
    "gama": "Gama", "goias": "Goias", "gremio": "Gremio",
    "guarani": "Guarani", "internacional": "Internacional",
    "juventude": "Juventude", "palmeiras": "Palmeiras",
    "parana": "Parana", "paysandu": "Paysandu",
    "ponte preta": "Ponte Preta", "portuguesa": "Portuguesa",
    "santos": "Santos", "sao caetano": "Sao Caetano",
    "sao paulo": "Sao Paulo", "vasco da gama": "Vasco",
    "vasco": "Vasco", "vitoria": "Vitoria",
}


def _nome_2002(nome: str) -> str:
    s = re.sub(r"\s+\[.*?\]\s*$", "", nome).strip().replace("Botafogo-RJ", "Botafogo")
    return _NOMES_2002.get(key(s), s)


def _ler_2002() -> list[Game]:
    text = read_pre(ROOT / "data" / "rsssf_braz02.html")
    i = text.find("Round 1")
    games: list[Game] = []
    rodada = data = None
    for line in text[i:text.find("\nTable", i)].splitlines():
        rm = re.match(r"Round\s+(\d+)", line)
        if rm:
            rodada, data = int(rm.group(1)), None
            continue
        dm = re.match(r"\[(\w{3}\s+\d{1,2})\]", line.strip())
        if dm:
            data = parse_date_token(dm.group(1), 2002)
            continue
        if line.startswith(" ") or not line.strip():
            continue
        m = re.match(r"^(.+?)\s{2,}(\d+)-(\d+)\s{2,}(.+?)(?:\s+\[(.*?)\])?\s*$", line)
        if m:
            games.append(Game(2002, "Primeira fase", 1, "liga", rodada, len(games) + 1, data, _nome_2002(m.group(1)),
                              _nome_2002(m.group(4)), int(m.group(2)), int(m.group(3)), _FONTE_2002, m.group(5) or ""))
    _conferir(games, 325, "2002 Primeira fase")
    fases = [("Quarterfinals", "Quartas de final"), ("Semi-finals", "Semifinal"), ("Finals", "Final")]
    pos = [text.find(marca) for marca, _ in fases] + [text.find("First Leg")]
    mm: list[Game] = []
    for ordem, (_, fase) in enumerate(fases, start=2):
        mm += _linhas_ida_volta(text[pos[ordem - 2]:pos[ordem - 1]], 2002, _FONTE_2002, fase, ordem, nome=_nome_2002)
    return games + _conferir(mm, 14, "2002 mata-mata")


EDICOES["2002"] = Edicao(ano=2002, fonte=_FONTE_2002, ler=_ler_2002, total=339)


# ----------------------------------------------------------------------
def montar(ed: Edicao) -> list[Game]:
    """Jogos da edicao, ja com os ajustes, sem gravar nada. Os nomes da edicao
    valem so aqui dentro."""
    antes = dict(CANONICAL)
    CANONICAL.update(ed.nomes)
    try:
        if ed.jogos is not None:
            games = [Game(ed.ano, fase, ordem, tipo, None, i, data, mand, vis, gm, gv, ed.fonte, obs)
                     for i, (fase, ordem, tipo, data, mand, gm, gv, vis, obs) in enumerate(ed.jogos, start=1)]
        elif ed.ler:
            games = ed.ler()
        else:
            games = parse_ano(ed.ano, ed.fonte, ed.fases, corte_final=ed.corte_final, virada=ed.virada,
                              arquivo=ed.arquivo, blocos_pre=ed.blocos_pre, ignorar=ed.ignorar)
        return ed.ajustar(games) if ed.ajustar else games
    finally:
        CANONICAL.clear()
        CANONICAL.update(antes)


def importar(chave: str) -> None:
    ed = EDICOES[chave]
    antes = dict(CANONICAL)
    CANONICAL.update(ed.nomes)  # import_year tambem resolve nomes
    try:
        gravar(ed.ano, ed.fonte, montar(ed), total=ed.total, edicao=ed.edicao)
    finally:
        CANONICAL.clear()
        CANONICAL.update(antes)


def main(args: list[str]) -> None:
    if not args or args == ["--lista"]:
        print("\n".join(EDICOES))
        return
    chaves = list(EDICOES) if args == ["--todos"] else [
        k for a in args for k in EDICOES if k == a or k.split("_")[0] == a]
    faltam = [a for a in args if a != "--todos" and not any(k == a or k.split("_")[0] == a for k in EDICOES)]
    if faltam:
        raise SystemExit(f"edicao desconhecida: {faltam}")
    for k in chaves:
        importar(k)


if __name__ == "__main__":
    main(sys.argv[1:])
