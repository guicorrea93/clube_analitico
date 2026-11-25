"""Gera a documentação completa da coleta Europa em coleta/comum-europa/documentacao/.

Uma ficha por liga (<slug>.md) e o índice (README.md). Tudo sai do que existe de fato:
- do pacote (data/coleta/<slug>/pacote/): o que cada campo cobre, década a década; formato do campeonato ao longo do
  tempo; campeões; punições; rebaixados; artilheiros; conferência com as tabelas publicadas;
- do importador (coleta/<slug>/importar.py): todas as correções e decisões tomadas, com o motivo (CORRECOES, TRIBUNAL,
  ACRESCIMOS, NAO_REBAIXADOS, EXPLICACOES...);
- do relatório (docs/coleta/<slug>.md): o que não deu para coletar;
- de PENDENCIAS, LIMITES e REVISAO, abaixo (à mão): o que falta, o que é limite de fonte e o que está com a
  revisão.

Rode depois de cada importação: python coleta/comum-europa/documentar.py
"""
from __future__ import annotations

import csv
import importlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
SAIDA = AQUI / "documentacao"
LIGAS = ["eng-1", "esp-1", "ita-1", "ger-1", "fra-1", "por-1", "ned-1", "sco-1", "bel-1", "tur-1", "gdr-1", "gre-1", "cze-1", "tch-1", "pol-1"]

# o que falta em cada liga (manter à mão; a ordem geral está em COMECE-AQUI.md). Rodada de 24/11/2026: nada em aberto na
# coleta; o que sobrou ou é limite de fonte (LIMITES, fechado) ou está com o agente de revisão (REVISAO)
PENDENCIAS: dict[str, list[str]] = {}

# limites de fonte: nenhuma fonte em lote tem o dado; fechado na coleta (só volta com uma fonte nova, jogo a jogo)
LIMITES: dict[str, list[str]] = {
    "eng-1": [
        "Autores dos gols e cartões antes de 2001/02: nenhuma fonte em lote; seria jogo a jogo (ficha do ogol).",
        "Nomes de jogadores da ESPN: os casos em formato de documento (sobrenomes na frente) que repetem um jogador com o "
        "nome de jogo no mesmo clube e temporada foram trocados (coleta/comum-europa/nomes_jogadores.py, aplicado em todas "
        "as ligas; varredura de 24/11/2026). Os outros ~2 mil nomes de 3 palavras ou mais são quase todos nomes de verdade "
        "(\"Kevin De Bruyne\"); a ESPN não dá o código do jogador para conferir um a um.",
    ],
    "esp-1": [
        "Autores dos gols e cartões antes de 2001/02: a RSSSF tem de 2000/01 em diante; antes, jogo a jogo (ficha do ogol).",
    ],
    "ita-1": [
        "Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).",
        "Era antiga (1898 a 1928/29, IT-017, em antigo.py): 29 edições pela Wikipédia em italiano. 713 jogos vêm só do "
        "Tabellone (sem data); 37 classificações de grupo diferem dos jogos (quase todas em 1 ou 2 gols, ou um jogo que o "
        "calendário não traz), listadas no relatório. A RSSSF (italhist98-25.html e ital24-29.html, em "
        "data/coleta/ita-1/rsssf-antigo/) só tem tabelas a partir de 1909/10; o próximo passo seria o Almanacco Illustrato.",
        "Era antiga: a classificação final de cada edição é montada (campeão do albo d'oro, depois a fase alcançada e a "
        "posição no grupo); não há classificação oficial além do campeão.",
    ],
    "ger-1": [
        "Autores dos gols: RSSSF (1963/64-1998/99, só os jogos em que a soma fecha, cerca de 97%), ficha do ogol (1999/00, "
        "2000/01 e os jogos em que a ESPN falta ou não fecha) e ESPN (2001/02+). Os jogos que nenhuma das três fecha ficam sem "
        "autor; cartões só pela ESPN.",
        "Era antiga (1902/03-1962/63, em antigo.py): entra só a fase final; as ligas regionais (Oberligen, Gauligen e as "
        "ligas de antes) ficam de fora (são outras competições, por região).",
        "Era antiga: gols com autor só nas partidas com ficha (football box) na Wikipédia, quase sempre a final; não há lista "
        "de artilheiros da fase final.",
        "Era antiga: a classificação final é o campeão, o vice e depois a fase alcançada (na mesma fase, posição no grupo e "
        "campanha); não existe classificação oficial além do campeão e do vice.",
    ],
    "fra-1": [
        "Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).",
        "Datas dos 356 jogos dos anos 1930 que nenhuma fonte tem.",
        "Revisão FR-009: 99 jogos (1948/49-1998/99) em que o transfermarkt e o ogol diferem da base por 1 ou 2 dias; só os 41 de "
        "3 dias ou mais foram corrigidos. Os outros só com o jornal (L'Équipe na Gallica), jogo a jogo.",
        "Revisão FR-017: 4 pares de jogos em que a Wikipédia fr dá outro mando ou placar (1935/36, 1937/38, 1945/46, 1950/51); "
        "fica a base, que fecha com as tabelas (anotado em EXPLICACOES). Só o jornal da época decidiria.",
        "Revisão FR-005: a vitória do Marseille sobre o Bordeaux em 27/10/1946 (0-0 no tribunal) vem das tabelas das Wikipédias "
        "e fecha com elas; só o L'Équipe de 28/10/1946 decidiria.",
        "Árbitro: os arquivos do football-data da França não trazem (revisão FR-022); seria jogo a jogo pelo transfermarkt.",
    ],
    "por-1": [
        "Autores dos gols: RSSSF (1999/00-2005/06, onde a soma fecha), ficha do ogol (2001/02, que a RSSSF não traz, e os jogos "
        "em que a ESPN falta ou não fecha) e ESPN (2006/07+). Antes de 1999/00, nenhuma fonte em lote. Sem autor ficam 103 jogos "
        "de 2001/02 e 27 de 2010/11 (a ficha do ogol também não fecha).",
        "Revisão PT-020: árbitro e público só jogo a jogo (transfermarkt, ~11 mil páginas, ou a ficha do ogol); o "
        "football-data de Portugal não traz árbitro.",
        "Revisão PT-010: Belenenses x Sporting (1938/39) e os dois jogos do Académico do Porto em 04/02/1940 (1939/40) ficam "
        "com a data do ogol; o transfermarkt repete o ogol e não há terceira fonte (anotado em EXPLICACOES).",
    ],
    "sco-1": [
        "Autores dos gols e cartões antes da ESPN (2001/02): jogo a jogo (ficha do ogol).",
        "Rodada vazia até os anos 1930 em várias temporadas: não havia rodadas fixas (como no Inglês) e o ogol não traz.",
    ],
    "ned-1": [
        "Era antiga (1888/89-1955/56, em antigo.py): de 1888/89 a 1896/97 e nas temporadas sem a fase final legível na "
        "RSSSF, só o campeão e a tabela da Eerste Klasse, sem jogos; os jogos da fase final vêm da matriz da RSSSF, sem data "
        "(datados só em 1954/55 e 1955/56). As ligas regionais ficam de fora.",
        "Era antiga: tabelas da fase final que não fecham com os jogos por erro de digitação da RSSSF (1906/07, 1922/23, "
        "1923/24); ficam anotadas no relatório.",
        "Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).",
    ],
    "bel-1": [
        "Antes de 1960/61: jogos só pela matriz da Wikipédia, sem data nem rodada (o ogol não tem); quando a soma não fecha com "
        "a tabela da RSSSF, a classificação final fica com os números publicados (observação na linha).",
        "1898/99, 1899/00, 1901/02, 1902/03 e 1903/04 (grupos): só as tabelas da RSSSF e os jogos finais e de desempate; sem "
        "os jogos dos grupos e sem classificação oficial além do campeão e do torneio final.",
        "Autores dos gols e cartões: só com a ESPN (2006/07+), que não tem lances de 2011/12 a 2014/15 nem dos play-offs; "
        "antes e nesses anos, jogo a jogo (ficha do ogol).",
        "Jogos de play-off de acesso e rebaixamento contra clubes da 2ª divisão (até 2008/09) ficam de fora; desde 2016/17 os "
        "clubes da 2ª divisão no play-off europeu entram nos jogos, mas não na classificação final.",
        "Artilheiros só desde 1945/46 (lista da RSSSF).",
    ],
    "gdr-1": [
        "Autores dos gols, público e estádio dos jogos da Oberliga: a RSSSF traz só o placar; fonte possível: as fichas "
        "do weltfussball.de ou o arquivo do jornal Neues Deutschland, jogo a jogo.",
        "1948 e 1949: só a fase final (mata-mata entre os campeões estaduais); os campeonatos estaduais ficam de fora.",
        "Punições de pontos que só a tabela da RSSSF traz (1966/67, 1967/68, 1973/74, 1990/91): os pontos oficiais vão para "
        "a classificação e a diferença para ajuste_pontos; o motivo de cada uma não está nas fontes.",
    ],
    "tur-1": [
        "Era antiga (antes de 1959, em antigo.py): os jogos do Şampiyonası de 1924 a 1935 e as matrizes da Millî Küme não "
        "têm data (só as fichas trazem).",
        "1962/63: os jogos do grupo de classificação (7º a 9º de cada grupo) não estão no ogol nem na Wikipédia (en e tr); "
        "entra a tabela.",
        "Autores dos gols e cartões: só com a ESPN (2006/07+), que quase não tem lances de 2011/12 a 2014/15 nem dos "
        "play-offs de 2011/12; antes e nesses anos, jogo a jogo (ficha do ogol).",
        "Placares do ogol que só a matriz da Wikipédia contesta nas temporadas antigas (sem football-data nem engsoccerdata "
        "antes de 1994/95): ficam os do ogol, que fecham com as tabelas.",
    ],
    "gre-1": [
        "1959/60 a 1992/93: jogos sem data nem rodada (só a matriz da RSSSF e a da Wikipédia; o ogol não tem esses jogos). "
        "Rodadas de 1994/95 a 1996/97: o ogol não traz.",
        "Era antiga (1927/28-1958/59, em antigo.py): só a fase nacional entre os campeões regionais; as ligas regionais, a "
        "fase semifinal de 1955/56 e as eliminatórias inter-regionais ficam de fora. Datas só nas finais e em 1929/30 e "
        "1945/46.",
        "Era antiga: em 1954/55 e 1955/56 as tabelas da RSSSF e da Wikipédia concordam entre si e não fecham com nenhuma "
        "matriz (diferenças de 1 a 4 gols); só o jornal da época decidiria.",
        "Autores dos gols e cartões: só com a ESPN (2006/07+), que quase não tem lances de 2011/12 a 2014/15; antes, só as "
        "fichas dos jogos-desempate da Wikipédia.",
        "Jogos de acesso e rebaixamento contra clubes da 2ª divisão ficam de fora (1959/60, 1967/68, 1968/69, 2000/01 a "
        "2003/04, 2013/14, 2018/19 a 2021/22).",
        "Play-off europeu de 2015/16: a tabela da Wikipédia dá 1 gol a menos a AEK (pró) e Panionios (contra) que os jogos "
        "do ogol; sem terceira fonte (a ESPN e o football-data não têm os play-offs), fica o ogol.",
    ],
    "cze-1": [
        "Autores dos gols só de 1998/99 a 2011/12 (página da RSSSF, quando a conta fecha com o placar: 7.121 gols); antes e "
        "depois, nenhuma fonte em lote (a ESPN e o football-data não cobrem a Tchéquia). Sem cartões, público, estádio e "
        "árbitro: só a ficha de cada jogo no ogol, jogo a jogo.",
        "Jogos de acesso e rebaixamento contra clubes da 2ª divisão ficam de fora.",
        "A liga tchecoslovaca (1925-1993) e a do Protetorado (1938/39-1943/44) ficam na competição da Tchecoslováquia "
        "(decisão do Guilherme, 25/11/2026).",
    ],
    "tch-1": [
        "Sem datas, rodadas, autores dos gols, cartões e público: a base é a matriz da Wikipédia (en); o ogol, a ESPN e o "
        "football-data não têm esta liga.",
        "10 temporadas em que a matriz da Wikipédia não fecha com as tabelas (que concordam entre si): a classificação fica "
        "com os números publicados; só um jornal da época diria qual jogo está errado.",
        "Fora do escopo (decisão do Guilherme, 25/11/2026): Boêmia Central antes de 1925, campeonato amador, 1944/45 e liga "
        "eslovaca da guerra.",
    ],
    "pol-1": [
        "Sem datas e rodadas de 1921 a 1962 (só as matrizes de resultados da Wikipédia e da RSSSF, fora as fichas das finais "
        "e do mata-mata de 1946); sem autores dos gols, cartões e público em toda a liga (sem ESPN; o football-data não traz "
        "cartões da Polônia).",
        "Grupo final de 1926 sem os jogos em nenhuma fonte (RSSSF, Wikipédia em inglês e em polonês): fica a tabela publicada.",
        "9 temporadas antigas em que a matriz não fecha com as tabelas (que concordam entre si): a classificação fica com os "
        "números publicados.",
        "Fora do escopo (decisão do Guilherme, 25/11/2026): 1920 (abandonado), 1924 (não disputado), 1939 (interrompido) e "
        "as ligas municipais da guerra; os jogos de acesso contra a 2ª divisão.",
    ],
}

# decisões que a coleta tomou e entregou ao agente de revisão para conferir (não é pendência da coleta)
REVISAO: dict[str, list[str]] = {
    "ita-1": [
        "Era antiga: as 37 classificações de grupo que diferem dos jogos e a identidade dos clubes antigos (clubes_ita.py, "
        "_ANTIGOS).",
    ],
    "sco-1": [
        "Temporadas em que as duas tabelas publicadas erram em clubes diferentes: o ogol fecha com uma delas em cada clube; "
        "conferir com uma terceira fonte (jornais da época, fitbastats.com, statto.com).",
    ],
    "ned-1": [
        "Identidade de clubes em fusões (GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x AZ, "
        "BVV x FC Den Bosch): separados como clubes diferentes, contra o ogol, que junta alguns na ficha do sucessor.",
    ],
    "gdr-1": [
        "Identidade dos clubes (coleta/comum-europa/clubes_gdr.py), sobretudo Chemie Leipzig, e o título de 1952/53 (Dynamo "
        "Dresden, como a RSSSF); as 19 tabelas que diferem dos jogos.",
    ],
    "gre-1": [
        "1959/60 a 1992/93: onde a matriz da RSSSF e a da Wikipédia discordam, ficou o placar que fecha com as duas tabelas "
        "publicadas (a maioria é da Wikipédia; trocas jogo a jogo e em pares, anotadas no relatório e na observação do jogo).",
        "Era antiga: o mesmo critério na fase nacional (1930/31, 1931/32, 1953/54, 1956/57, 1957/58, 1958/59 com trocas).",
        "Identidade: Chalkidona em 2004/05 (o ogol põe no Atromitos, que absorveu o clube em 2005); Rodos x AE Rodos e AO "
        "Kerkyra x PAE Kerkyra separados como na Wikipédia; Megas Alexandros (1959/60) como Pierikos.",
        "Desempates de posição que só estão nas notas da Wikipédia (1959/60 a 1966/67, 1973/74, 1982/83, 1983/84), sem data.",
    ],
    "cze-1": [
        "Identidade: o Dukla Praha histórico (1993/94) separado do 1. FK Příbram (o ogol usa o mesmo código) e do FK Dukla "
        "Praha de hoje; Bohemians 1905 x Bohemians de Střížkov (2008/09 e 2009/10).",
        "Classificação com grupos (2018/19, 2019/20, desde 2021/22): do 7º ao 10º pela fase regular (o play-off europeu não "
        "muda a posição).",
    ],
    "tch-1": [
        "Identidade pelos links da Wikipédia através das trocas de nome da era comunista; o Dukla Praha histórico é o "
        "mesmo do `cze-1` em 1993/94, mas a RSSSF diz que ele é hoje o Marila Příbram (no `cze-1`, Příbram ficou à parte, "
        "pela Wikipédia).",
        "Classificação de 1945/46: a final (Sparta x Slavia) e depois a posição nos grupos; títulos do Protetorado contados "
        "(Sparta 21, Slavia 13 no total).",
    ],
    "pol-1": [
        "Identidade pelos links da Wikipédia: o PKS Szczecin de 1946-47 como o Pogoń Szczecin, o Motor Białystok (1947) como "
        "o Jagiellonia, o Grochów (1947) como o Gwardia Varsóvia, o RKU Sosnowiec como o Zagłębie; o Olimpia/Lechia Gdańsk "
        "de 1995/96 à parte do Lechia (o ogol junta) e o Sokół Tychy como o GKS Tychy; o 22 pp Siedlce e o Strzelec Siedlce "
        "como um clube só (a RSSSF diz que mudou de nome).",
        "1922: a RSSSF trocou as matrizes dos dois grupos; os jogos vêm da matriz certa, e os números fecham com a Wikipédia "
        "polonesa. 1951: campeão o Ruch (6º na liga, pela Copa); 1992/93: os dois jogos anulados ficam fora.",
        "Placares do ogol trocados pela matriz da Wikipédia só quando ela fecha melhor com as tabelas, ou empatada com o "
        "football-data ou a RSSSF a favor (2004/05, 2006/07, 2007/08, 2022/23, 2025/26); o ogol rotula o Zagłębie Sosnowiec "
        "de 1985/86 como Zagłębie Wałbrzych (os 30 placares são os do Sosnowiec).",
    ],
    "tur-1": [
        "Kayseri: o Kayserispor de 1966 a 2004 está como Kayseri Erciyesspor (troca de nomes de 2004, como na Wikipédia); o "
        "ogol e boa parte da imprensa contam a história no Kayserispor de hoje.",
    ],
}

# rótulo de cada dicionário de decisões dos importadores
DICIONARIOS = {
    "CORRECOES": "Placares corrigidos",
    "TRIBUNAL": "Resultados decididos fora de campo",
    "CAMPO": "Jogos sem placar na base em que valeu o placar de campo",
    "ACRESCIMOS": "Jogos que faltavam na base e foram acrescentados",
    "INVERTIDOS": "Mando de campo corrigido",
    "DATAS": "Datas corrigidas",
    "GOLS_ARTILHEIRO": "Gols de artilheiro corrigidos",
    "NAO_REBAIXADOS": "Fora da temporada seguinte sem ter sido rebaixado",
    "NAO_REELEITOS": "Não reeleitos (sem rebaixamento na época)",
    "REBAIXADOS_EXTRA": "Rebaixados que a regra geral não pega",
    "FORCAR_OGOL": "Temporadas montadas pelo calendário do ogol",
    "INTERROMPIDAS": "Temporadas interrompidas",
    "SEM_REBAIXAMENTO": "Temporadas sem rebaixamento",
    "LIGUILLA": "Liguilla / jogos extras fora da tabela",
    "WIKI_TROCADA": "Wikipédia com linhas trocadas",
    "OGOL_WIKI": "Ogol x Wikipédia",
    "WIKI_GOLS": "Gols da Wikipédia",
    "DECLASSADOS": "Declassados para o último lugar fora de campo",
    "ORDEM_RSSSF": "Temporadas com a ordem oficial da RSSSF",
    "READMITIDOS": "Rebaixados em campo e readmitidos",
    "SUSPENSOS": "Jogos suspensos e completados em outro dia",
    "GOLS_MANUAIS": "Autores dos gols pela ficha do BDFutbol (a ESPN não fecha)",
    "NOTA_ARTILHEIRO": "Artilheiros com divergência entre fontes anotada",
    "FUSOES": "Fora da temporada seguinte por fusão",
    "ADMINISTRATIVOS": "Rebaixamentos fora de campo (observação na classificação)",
    "IGNORAR_AJUSTE": "Ajustes da Wikipédia que não são punição",
    "NAO_PUNIR": "Punições que só a RSSSF traz e não se confirmam",
    "ORDEM_PELO_CRITERIO": "Ordem pelo critério de desempate da época",
    "ARTILHEIROS_EXTRA": "Artilheiros empatados que a RSSSF não lista",
    "NOMES_ARTILHEIRO": "Nomes de artilheiros acertados",
    "GOLS_ARTILHEIRO": "Gols de artilheiro corrigidos",
    "PUNICOES": "Punições que nenhuma tabela usada traz",
    "FORA_DE_CAMPO": "Rebaixamentos fora de campo e casos especiais (observação da edição)",
    "ORDEM_FIXA": "Posições fixadas por decisão de tribunal",
    "AJUSTES": "Ajustes de pontos que valem hoje",
    "OBS_CLASSIF": "Observações na classificação final",
    "ORDEM_RSSSF": "Temporadas com a ordem oficial da RSSSF",
    "ORDEM_ITWIKI": "Ordem entre empatados pela Wikipédia it (classifica avulsa)",
    "NOMES_ESPN": "Nomes de jogadores da ESPN acertados",
    "NOTAS_MATRIZ": "Células da matriz da RSSSF com nota (placar dado na nota)",
    "DERROTA_DOIS_OGOL": "Jogos que valeram derrota para os dois",
    "DECIDIDOS": "Jogos decididos fora de campo, com o placar oficial dado à mão",
    "EXPLICACOES": "Divergências entre fontes já explicadas",
    "EXCLUIDOS": "Clubes excluídos no meio da temporada (jogos anulados)",
    "DESEMPATES": "Desempates pelo título fora da tabela",
    "TABELA_OFICIAL": "Classificação pelos números da tabela publicada (punição só para um lado)",
    "DADOS_FORA": "Jogos dados pela federação (o ogol traz o placar; marcados awd)",
    "SEM_TITULO": "Edições sem título oficial",
    "PONTOS_2_1_0": "Edições com 2 pontos por vitória, 1 por empate e 0 por derrota",
}

CAMPOS_COBERTURA = [("data", "data"), ("hora", "hora"), ("rodada", "rodada"), ("estadio", "estádio"), ("publico", "público"),
                    ("arbitro", "árbitro")]


def ler(slug: str, nome: str) -> list[dict]:
    arq = RAIZ / "data" / "coleta" / slug / "pacote" / f"{nome}.csv"
    if not arq.exists():
        return []
    with arq.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def importador(slug: str):
    """Carrega coleta/<slug>/importar.py sem rodar (os importadores têm o mesmo nome de módulo: limpa entre um e outro)."""
    for m in [m for m in sys.modules if m in ("importar", "edicoes") or m.startswith("rsssf_")]:
        del sys.modules[m]
    sys.path[:] = [p for p in sys.path if not p.replace("\\", "/").rstrip("/").split("/")[-1] in LIGAS]
    sys.path.insert(0, str(RAIZ / "coleta" / slug))
    sys.path.insert(1, str(AQUI))
    return importlib.import_module("importar")


def pct(a: int, b: int) -> str:
    return "—" if not b else f"{100 * a / b:.0f}%"


def texto_valor(v) -> str:
    """Valor de um dicionário de decisões: o motivo (texto mais longo) e os números/rótulos curtos antes."""
    if isinstance(v, str):
        return v
    if isinstance(v, (tuple, list)):
        textos = [x for x in v if isinstance(x, str)]
        motivo = max(textos, key=len) if textos else ""
        outros = [str(x) for x in v if x is not None and not (isinstance(x, str) and x == motivo)]
        return (f"[{', '.join(outros)}] " if outros else "") + motivo
    if isinstance(v, list):
        return "; ".join(map(str, v))
    return str(v)


ROTULO_TEMPORADA = None   # temporada() do importador da liga em curso (a Turquia chama a de 1959 de "1959")


def texto_chave(k) -> str:
    """(1994, "Benfica", "Sporting") -> "1994/95 · Benfica · Sporting": o ano de início vira a temporada."""
    partes = list(k) if isinstance(k, tuple) else [k]
    if partes and isinstance(partes[0], int) and 1850 < partes[0] < 2100:
        partes[0] = ROTULO_TEMPORADA(partes[0]) if ROTULO_TEMPORADA else f"{partes[0]}/{str(partes[0] + 1)[-2:]}"
    return " · ".join(str(x) for x in partes)


def decada(t: str) -> str:
    return f"{t[:3]}0s"


def ficha(slug: str) -> tuple[str, dict]:
    global ROTULO_TEMPORADA
    imp = importador(slug)
    ROTULO_TEMPORADA = getattr(imp, "temporada", None)
    comp = json.loads((RAIZ / "data" / "coleta" / slug / "pacote" / "competicao.json").read_text(encoding="utf-8"))
    ed, part, gols, cart = ler(slug, "edicoes"), ler(slug, "partidas"), ler(slug, "gols"), ler(slug, "cartoes")
    # a era antiga vem depois no arquivo: a primeira e a última temporada saem do ano, não da ordem das linhas
    por_ano = sorted(ed, key=lambda e: e["temporada"][:4])
    primeira, ultima = por_ano[0]["temporada"], por_ano[-1]["temporada"]
    clf, fases, art, conf = ler(slug, "classificacao_final"), ler(slug, "fases"), ler(slug, "artilheiros"), ler(slug, "conferencia")
    est, clubes, pub = ler(slug, "estatisticas"), ler(slug, "clubes"), ler(slug, "tabelas_publicadas")
    rod = ler(slug, "classificacao_rodada")
    temporada_de = {p["id"]: p["temporada"] for p in part}
    gols_por_t = Counter(temporada_de.get(g["partida_id"]) for g in gols)
    cart_por_t = Counter(temporada_de.get(c["partida_id"]) for c in cart)
    est_jogos = {e["partida_id"] for e in est}
    total_gols = sum(int(p["gols_mandante"] or 0) + int(p["gols_visitante"] or 0) for p in part)

    out = [f"# {comp['nome']} (`{slug}`) — documentação", "",
           f"Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/{slug}/pacote/` e do "
           f"importador `coleta/{slug}/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, "
           f"está em `docs/coleta/{slug}.md`.", ""]

    # ---- 1. visão geral
    out += ["## 1. O que temos", "",
            f"- **Edições:** {len(ed)}, de {primeira} a {ultima}.",
            f"- **Jogos:** {len(part)}; **gols:** {total_gols}; **gols com autor:** {len(gols)} ({pct(len(gols), total_gols)}); "
            f"**cartões:** {len(cart)}; **jogos com estatísticas** (chutes, faltas, escanteios): {len(est_jogos)}.",
            f"- **Clubes:** {len(clubes)}; **artilheiros:** {len({a['temporada'] for a in art})} temporadas com artilheiro "
            f"({len(art)} linhas, com empates).",
            f"- **Classificação final:** {len({c['temporada'] for c in clf})} temporadas; **rodada a rodada:** "
            f"{len({r['temporada'] for r in rod})} temporadas.",
            f"- **Tabelas publicadas guardadas para conferência:** {len(pub)} linhas, de "
            f"{len({(p['temporada'], p['fonte']) for p in pub})} tabelas.",
            f"- **Observação da competição:** {comp.get('observacao') or '—'}", ""]

    # ---- 2. fontes e regras (do relatório da importação)
    rel = (RAIZ / "docs" / "coleta" / f"{slug}.md").read_text(encoding="utf-8")
    fontes = re.search(r"\*\*Fontes:\*\*\s*\n(.*?)\n\s*\n", rel, re.S)
    regras = re.search(r"\*\*Regras:\*\*\s*(.*?)\n\s*\n", rel, re.S)
    desempate = re.search(r"\*\*Desempate:\*\*\s*(.*?)\n\s*\n", rel, re.S)
    out += ["## 2. Fontes e regras", "", "**Fontes:**", "", fontes.group(1).strip() if fontes else "- (ver relatório)", "",
            "**Regras da importação:** " + (regras.group(1).strip() if regras else "(ver relatório)"), ""]
    if desempate:
        out += ["**Desempate:** " + desempate.group(1).strip(), ""]

    # ---- 3. conferência
    ok = sum(int(c["tabelas_conferidas"] or 0) for c in conf)
    div = sum(int(c["tabelas_divergentes"] or 0) for c in conf)
    sem_ok = [c["temporada"] for c in conf if int(c["tabelas_conferidas"] or 0) == 0]
    com_div = [c["temporada"] for c in conf if int(c["tabelas_divergentes"] or 0) > 0]
    incompletas = [f"{c['temporada']} ({c['jogos']} de {c['jogos_esperados']})" for c in conf
                   if c["jogos_esperados"] and c["jogos"] != c["jogos_esperados"]]
    out += ["## 3. Conferência", "",
            f"- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): {ok} tabelas fecham com os jogos e {div} "
            f"divergem (divergência sempre explicada no relatório).",
            f"- Temporadas em que nenhuma tabela publicada fecha: {', '.join(sem_ok) or 'nenhuma'}.",
            f"- Temporadas com alguma tabela divergente: {', '.join(com_div) or 'nenhuma'}.",
            f"- Temporadas com número de jogos diferente do turno e returno completo: {', '.join(incompletas) or 'nenhuma'}.", ""]

    # ---- 4. cobertura por década
    por_dec = defaultdict(list)
    for p in part:
        por_dec[decada(p["temporada"])].append(p)
    gols_dec, cart_dec, golsaut_dec, est_dec = Counter(), Counter(), Counter(), Counter()
    for p in part:
        gols_dec[decada(p["temporada"])] += int(p["gols_mandante"] or 0) + int(p["gols_visitante"] or 0)
        if p["id"] in est_jogos:
            est_dec[decada(p["temporada"])] += 1
    for t, n in gols_por_t.items():
        if t:
            golsaut_dec[decada(t)] += n
    for t, n in cart_por_t.items():
        if t:
            cart_dec[decada(t)] += n
    cab = "| Década | Jogos | " + " | ".join(r for _, r in CAMPOS_COBERTURA) + " | estatísticas | gols c/ autor | cartões/jogo |"
    out += ["## 4. Cobertura de cada campo, por década", "",
            "Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).", "", cab,
            "|" + "---|" * (len(CAMPOS_COBERTURA) + 5)]
    for d in sorted(por_dec):
        ps = por_dec[d]
        cel = [pct(sum(1 for p in ps if p[c]), len(ps)) for c, _ in CAMPOS_COBERTURA]
        out.append(f"| {d} | {len(ps)} | " + " | ".join(cel) + f" | {pct(est_dec[d], len(ps))} | {pct(golsaut_dec[d], gols_dec[d])} | "
                   f"{cart_dec[d] / len(ps):.1f} |")
    out.append("")

    # ---- 5. formato ao longo do tempo
    def faixas(chave_fn):
        res, atual = [], None
        for e in ed:
            v = chave_fn(e)
            if atual and atual[0] == v:
                atual[2] = e["temporada"]
            else:
                atual = [v, e["temporada"], e["temporada"]]
                res.append(atual)
        return res
    out += ["## 5. Formato do campeonato ao longo do tempo", "", "**Número de clubes:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v} clubes" for v, a, b in faixas(lambda e: e["num_clubes"])]
    out += ["", "**Pontos por vitória:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["pontos_vitoria"])]
    out += ["", "**Nome oficial:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["nome_oficial"])]
    multi = defaultdict(list)
    for f in fases:
        multi[f["temporada"]].append(f)
    especiais = {t: fs for t, fs in multi.items() if len(fs) > 1 or fs[0]["tipo"] != "liga"}
    out += ["", "**Temporadas com mais de uma fase ou fora dos pontos corridos:**", ""]
    out += [f"- {t}: " + "; ".join(f"{f['fase']} ({f['tipo']}, {f['formato_serie']})" for f in fs) for t, fs in especiais.items()] \
        or ["- nenhuma"]
    crit = Counter(f["criterio"] for f in fases if f["criterio"])
    out += ["", "**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):", ""]
    out += [f"- {c}: {n} temporadas" for c, n in crit.most_common()]
    obs = [(e["temporada"], e["observacao"]) for e in ed if e["observacao"]]
    out += ["", "**Observações das edições** (formato, punições, casos especiais):", ""]
    out += [f"- {t}: {o}" for t, o in obs] or ["- nenhuma"]
    out.append("")

    # ---- 6. campeões e rebaixados
    camp = Counter(e["campeao"] for e in ed if e["campeao"])
    sem_campeao = [e["temporada"] for e in ed if not e["campeao"]]
    reb = Counter(c["clube"] for c in clf if c["situacao"] == "rebaixado")
    puni = [(c["temporada"], c["clube"], c["ajuste_pontos"]) for c in clf if c["ajuste_pontos"] not in ("", "0")]
    out += ["## 6. Campeões, rebaixados e punições", "", "**Títulos:**", ""]
    out += [f"- {c}: {n}" for c, n in camp.most_common()]
    if sem_campeao:
        out += [f"- Sem campeão: {', '.join(sem_campeao)}"]
    out += ["", f"**Rebaixamentos:** {sum(reb.values())} no total; quem mais caiu: "
            + ", ".join(f"{c} ({n})" for c, n in reb.most_common(5)) + ".", "",
            "**Punições em pontos:**", ""]
    out += [f"- {t}: {c} {a}" for t, c, a in puni] or ["- nenhuma"]
    out.append("")

    # ---- 7. correções e decisões
    out += ["## 7. Correções e decisões (com o motivo)", "",
            f"Registradas em `coleta/{slug}/importar.py`; cada uma também aparece no relatório, na temporada.", ""]
    achou = False
    for nome, rotulo in DICIONARIOS.items():
        v = getattr(imp, nome, None)
        if not v:
            continue
        achou = True
        out += [f"### {rotulo} (`{nome}`)", ""]
        if isinstance(v, dict):
            for k, x in v.items():
                if isinstance(x, list) and all(isinstance(i, str) for i in x):
                    out += [f"- **{texto_chave(k)}:** " + " / ".join(x)]
                else:
                    out += [f"- **{texto_chave(k)}:** {texto_valor(x)}"]
        elif isinstance(v, (set, frozenset, list, tuple, range)):
            out += [f"- {', '.join(map(str, sorted(v)))}"]
        else:
            out += [f"- {v}"]
        out.append("")
    if not achou:
        out += ["- nenhuma", ""]

    # ---- 8. limites e pendências
    m = re.search(r"## O que não deu para coletar\s*\n(.*?)(?:\n## |\Z)", rel, re.S)
    out += ["## 8. O que não deu para coletar", "", (m.group(1).strip() if m else "- (ver relatório)"), "",
            "## 9. Pendências", ""]
    out += [f"- {p}" for p in PENDENCIAS.get(slug, [])] or ["- nenhuma em aberto na coleta."]
    out += ["", "**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.", ""]
    out += [f"- {p}" for p in LIMITES.get(slug, [])] or ["- nenhum"]
    if REVISAO.get(slug):
        out += ["", "**Com o agente de revisão:** decisões da coleta que ele confere.", ""]
        out += [f"- {p}" for p in REVISAO[slug]]
    out += ["", "## 10. Arquivos", "",
            f"- Código: `coleta/{slug}/` (`edicoes.py`, `baixar.py`, `importar.py`" + (", leitor da RSSSF" if list((RAIZ / 'coleta' / slug).glob('rsssf_*.py')) else "")
            + f"); cadastro dos clubes em `coleta/comum-europa/clubes_{slug[:3]}.py`.",
            f"- Fontes baixadas: `data/coleta/{slug}/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-{slug}/`.",
            f"- Pacote: `data/coleta/{slug}/pacote/`; relatório: `docs/coleta/{slug}.md`.",
            f"- Refazer do zero: `python coleta/{slug}/baixar.py ...` (ver o docstring), `python coleta/{slug}/importar.py`, "
            f"`python coleta/comum-europa/testar_carga.py {slug} <pasta temporária>` e `python coleta/comum-europa/documentar.py`.", ""]
    resumo = {"slug": slug, "nome": comp["nome"], "edicoes": len(ed), "de": primeira, "ate": ultima,
              "jogos": len(part), "gols_autor": len(gols), "cartoes": len(cart), "clubes": len(clubes), "tabelas_ok": ok,
              "tabelas_div": div, "pendencias": len(PENDENCIAS.get(slug, []))}
    return "\n".join(out) + "\n", resumo


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    SAIDA.mkdir(exist_ok=True)
    resumos = []
    for slug in LIGAS:
        txt, r = ficha(slug)
        (SAIDA / f"{slug}.md").write_text(txt, encoding="utf-8")
        resumos.append(r)
        print(f"{slug}: {r['edicoes']} edições, {r['jogos']} jogos", flush=True)
    idx = ["# Coleta Europa — documentação", "",
           "Gerado por `python coleta/comum-europa/documentar.py`. Uma ficha por liga, com tudo o que o pacote tem, a "
           "cobertura de cada campo década a década, o formato do campeonato ao longo do tempo, campeões, punições, todas "
           "as correções e decisões com o motivo, o que não deu para coletar e as pendências.", "",
           "Regras de trabalho, ordem das pendências e como fazer uma liga nova: `coleta/comum-europa/COMECE-AQUI.md`. "
           "Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-europa.md`. Achados da revisão: "
           "`docs/revisao/achados.csv` (`quem_corrige` = `coleta-europa`).", "",
           "| Liga | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | Pendências | Ficha |",
           "|---|---|---|---|---|---|---|---|---|"]
    for r in resumos:
        idx.append(f"| {r['nome']} | {r['edicoes']} ({r['de']}–{r['ate']}) | {r['jogos']} | {r['gols_autor']} | {r['cartoes']} | "
                   f"{r['clubes']} | {r['tabelas_ok']} / {r['tabelas_div']} | {r['pendencias']} | [{r['slug']}]({r['slug']}.md) |")
    idx += ["", "## Pendências de todas as ligas", ""]
    abertas = [f"- **{slug}:** {p}" for slug in LIGAS for p in PENDENCIAS.get(slug, [])]
    idx += abertas or ["Nenhuma em aberto na coleta (rodada de 24/11/2026). O que sobrou está abaixo."]
    idx += ["", "## Limites de fonte (fechados)", "", "Nenhuma fonte em lote tem o dado; só volta com uma fonte nova.", ""]
    idx += [f"- **{slug}:** {p}" for slug in LIGAS for p in LIMITES.get(slug, [])]
    idx += ["", "## Com o agente de revisão", "", "Decisões da coleta que a revisão confere.", ""]
    idx += [f"- **{slug}:** {p}" for slug in LIGAS for p in REVISAO.get(slug, [])]
    idx += ["", "## Próximas ligas", "",
            "- Na ordem do ranking de coeficientes da UEFA (foto de 24/11/2026), da mais bem colocada à menos: a tabela "
            "está em `COMECE-AQUI.md`, seção 3. Prontas desde a nova ordem: Grécia (`gre-1`), Tchéquia (`cze-1`), "
            "Tchecoslováquia (`tch-1`) e Polônia (`pol-1`); a próxima é a Noruega. Uma por vez, com o escopo antes.", ""]
    (SAIDA / "README.md").write_text("\n".join(idx), encoding="utf-8")


if __name__ == "__main__":
    main()
