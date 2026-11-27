"""Gera a documentação completa da coleta Brasil (agente 2) em coleta/comum/documentacao/.

Uma ficha por competição (<slug>.md) e o índice (README.md). Tudo sai do que existe de fato:
- do pacote (data/coleta/<slug>/pacote/): o que cada campo cobre, década a década; formato ao longo do tempo (clubes,
  pontos por vitória, nome oficial, fases e grupos); campeões, acessos, rebaixados, punições; artilheiros; conferência
  com as tabelas publicadas;
- dos módulos da competição (coleta/<slug>/: importar.py, explicacoes.py, rsssf_*.py, clubes_*.py e os leitores extras):
  todas as correções e decisões, com o motivo (CORRIGE_OGOL, NOME_MANUAL, JOGOS_ANULADOS, AJUSTE_MANUAL, EXPLICACOES,
  MANUAL_NOVO, as correções das páginas da RSSSF...);
- do relatório (docs/coleta/<slug>.md): fontes, regras e o que não deu para coletar;
- do banco (db/futebol.db, só leitura): se a competição já está carregada;
- de PENDENCIAS, abaixo: o que falta, mantido à mão.

Rode depois de cada importação ou correção: python coleta/comum/documentar.py
"""
from __future__ import annotations

import csv
import importlib
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
SAIDA = AQUI / "documentacao"
COMPETICOES = ["bra-serie-c", "bra-serie-d", "bra-copa-do-brasil", "bra-sp-1", "bra-sp-2", "bra-rj-1", "bra-mg-1", "bra-rs-1",
               "bra-pr-1", "bra-ce-1", "bra-go-1", "bra-sc-1", "bra-ba-1", "bra-pe-1"]

# o que falta em cada competição (manter à mão; a ordem geral está em COMECE-AQUI.md)
PENDENCIAS: dict[str, list[str]] = {
    "bra-serie-c": [
        "Achados da revisão SC-001 a SC-023 e CL-002/CL-004/CL-005/CL-012: tratados (docs/coleta/pedidos.md, partes 2 e 4, "
        "edições de 2026 e identidade). A revisão ainda não reconferiu (docs/revisao/achados.csv segue com 'aberto').",
        "Autores dos gols antes de 2012 e cartões: só jogo a jogo, pela ficha do ogol (~8 mil pedidos, ~3 h). Prioridade "
        "baixa (cartões, mais baixa ainda), decisão do Guilherme (20/11/2026).",
    ],
    "bra-serie-d": [
        "Achados da revisão SD-001 a SD-021: tratados (docs/coleta/pedidos.md, parte 3, parte 4 e edições de 2026). A "
        "revisão ainda não reconferiu.",
        "Cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).",
    ],
    "bra-copa-do-brasil": [
        "Achados da revisão CB-001 a CB-015: tratados (docs/coleta/pedidos.md, partes 1 e 4). Plano da revisão (24/11): "
        "QC-005, QC-004 (datas_corrigidas.csv), CB-007 e QC-008 (D-14 C), CL-028 (Alegrense). A revisão ainda não reconferiu.",
        "Jogo preliminar de 1999: entrou Náutico 0-1 Santa Cruz em 28/01/1999, pelo Futebol Nacional (D-14 C); a Wikipédia "
        "pt dá o mando ao contrário (Santa Cruz 1-0). Conferir no Diario de Pernambuco de 29/01/1999 só se o Guilherme pedir.",
        "CB-005 (D-13): 1990 (volta Santa Cruz x América-RN) e 1991 (Vitória x Remo) ficam como estão até um jornal da época.",
        "Autores dos gols antes de 2013 e cartões: jogo a jogo, pela ficha do ogol (prioridade baixa).",
    ],
    "bra-sp-1": [
        "Plano da revisão (docs/revisao/plano-coleta-brasil.md) concluído em 24/11, em 5 commits (ERRADO NO AR, jogos, FPF e "
        "2026, pacote.py, pódio); detalhes em docs/coleta/pedidos.md.",
        "Ficam como estão, com o motivo: 3º lugar de 1917 e 1954 (o FN confirma o pacote; a Wikipédia diverge), 1927 LAF, "
        "1928 LAF e 1930 (3º dividido na RSSSF), 1959 (empate sem regra da época); 44 casos de clube com dois jogos no "
        "mesmo dia de 1906 a 1983 (conferir com o Futebol Nacional); artilheiro de 1927 APEA, 1928 LAF e 1936 LPF.",
        "Autores dos gols e cartões nos anos sem RSSSF com autores: jogo a jogo, pela ficha do ogol (prioridade baixa).",
    ],
    "bra-sp-2": [
        "Plano da revisão concluído em 24/11 (ERRADO NO AR, A2-001 e as partes A, B e C); detalhes em docs/coleta/pedidos.md.",
        "1967-1984: só os jogos que a Wikipédia traz (finais e fases finais); os jogos dos campeões nas páginas da RSSSF "
        "de 1968, 1969, 1971, 1976, 1980 e 1984 ainda não entraram. Clubes novos a conferir pela revisão: Vasco da Gama (1969) "
        "e Americana (1976), os dois de Americana; Presidente Prudente FC (1974).",
        "Datas que a própria página dá impossíveis (1985, 1986, 1987 e 1988, A2-027): sem 2ª fonte; ficam anotadas.",
        "Jogos que faltam (1947-1966 fora o que a Wikipédia traz; 1988: 69 sem placar; 1989: 2ª e 3ª fases; 1990: 1ª a 3ª; "
        "1991: 1ª fase; 1992: 1ª fase; 1993 e 1994): só em jornais da época (Hemeroteca Digital, acervos do Estadão e da "
        "Folha), em imagem. Só se o Guilherme pedir.",
    ],
    "bra-rj-1": [
        "Autores dos gols: só 3.383 (quase todos de 2010 em diante). Nas outras décadas a página não traz os autores ou traz "
        "num formato que o leitor ainda não junta ao jogo (\"Gols: ...\" na linha de baixo, nos anos 1900).",
        "127 tabelas divergentes a explicar (ou corrigir) uma a uma no relatório; jogos avulsos do fim das páginas (súmulas sem "
        "par na lista: 1915, 1917-1919, 1924 AMEA, 1925, 1938, 1944, 1959, 1976) a conferir.",
        "Artilheiros de 2015 em diante: a lista da RSSSF (rjtops.htm) parou em 2014; a Wikipédia em português tem a tabela "
        "ano a ano (pt_lista.txt), ainda não lida.",
    ],
    "bra-mg-1": [
        "196 tabelas divergentes a explicar no relatório. Boa parte não é erro de jogo: a tabela publicada conta o W.O. "
        "com gols (D-15: sem gols), traz um turno por tabela quando a página junta os jogos (1983-1987), ou erra a soma "
        "(RSSSF e ogol com os mesmos placares).",
        "Vices em que as fontes discordam: 1934 (pacote Tupynambás, que perdeu a final estadual; RSSSF Palestra Itália; "
        "Wikipédia Tupynambás no estadual e Atlético na cidade), 1942 (RSSSF América; Wikipédia e pacote Palestra Mineiro, "
        "o Cruzeiro) e 1950 (RSSSF Cruzeiro; Wikipédia e pacote Siderúrgica).",
        "1924 e 1925 incompletos na própria fonte (1924: \"Incomplete scores\"; 1925: 4 jogos, campeonato anulado na época "
        "e título homologado pela FMF em 2012). Pontos extras de 1975 (Atlético e Cruzeiro, +1 na fase final) não entram "
        "na classificação calculada.",
        "Autores dos gols: 24.324 de 31.081; cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).",
    ],
    "bra-rs-1": [
        "1918 (campeonato suspenso pela gripe espanhola): edição sem jogos, com os três campeões honoríficos que a FGF "
        "reconheceu em 2021 (Brasil de Pelotas em campeao; Cruzeiro e 14 de Julho em co_campeao, que o carregador ainda não "
        "aceita com dois clubes). Decisão do Guilherme em 25/11, a mesma das edições sem jogos do Cearense.",
        "De 1925 a 1976 o ogol não tem os jogos: a identidade dos clubes vem dos nomes (importar.NOME_CODIGO e NOME_ANO; "
        "\"Riograndense\", \"Guarany\", \"Guarani\", \"Cruzeiro\" e \"Nacional\" sem cidade mudam de clube conforme a "
        "época). As páginas dos anos 1960-1990 vêm de texto escaneado (grafias em rsssf_rs1.GRAFIAS).",
        "Identidade a revisar: SE São Borja (241325, antes de 2009) x AE São Borja (70071) - as fontes discordam se é a "
        "mesma linhagem; Flamengo de Alegrete com ficha de 1963 e jogos em 1961-1962; AE Santo Ângelo (antes da fusão de "
        "1989) separado da SER Santo Ângelo.",
        "Vices de 1986 e 1993: o pacote segue a classificação publicada/final; a Wikipédia dá o Internacional.",
        "Tabelas divergentes a explicar no relatório (muitas nos anos de página escaneada, 1963-1996). Autores dos gols: as "
        "páginas quase não trazem (cerca de 12% dos gols). Cartões: só jogo a jogo, pela ficha do ogol.",
    ],
    "bra-pr-1": [
        "2002 Supercampeonato: edição não oficial (coluna oficial = \"não\"), com os clubes da Copa Sul-Minas; o Athletico "
        "conta o título, mas a lista oficial da FPF não foi achada. 1980: título dividido (Colorado e Cascavel, co_campeao).",
        "De 1915 a 2000 o ogol não tem os jogos (só 1965 e 1967): a identidade dos clubes vem dos nomes (importar.NOME_CODIGO "
        "e NOME_ANO). \"Paraná\" (Paraná SC até 1926, Paraná EC de Londrina em 1968-1969, Paraná Clube de 1990), "
        "\"Cascavel\" (Cascavel FC em 1971-1972, Cascavel EC de 1980 a 2000, Cascavel CR de 2003), \"Maringá\" (Grêmio "
        "Maringá até 1996, Maringá FC 1995 em 1997-1998, Maringá FC de 2010), \"Toledo\", \"Foz do Iguaçu\", \"Arapongas\", "
        "\"Cianorte\" (CAFE até 2001) e \"Nacional\" mudam de clube conforme a época.",
        "Identidade a revisar: o EC Água Verde (39780: Savóia, Savóia Água Verde, EC Brasil e Água Verde, 1916-1971) e o EC "
        "Pinheiros (17224, 1972-1989) são a mesma linhagem (RSSSF, prcamp.htm), mas o ogol, o cadastro comum e o banco os "
        "separam; o pacote segue o cadastro. O Palestra Itália leva os nomes da II Guerra (Paranaense 1942, Comercial "
        "1943-1945, Palmeiras 1946-1949). Cambaraense (1952-1962) e Cambará (1963-1965) ficam separados.",
        "Vices diferentes da Wikipédia: 1923-1926 e 1940 (a Wikipédia dá o Operário Ferroviário; as páginas da RSSSF não têm "
        "jogo com ele) e 1941 (a página dá a final Coritiba 6-1 Antoninense; a Wikipédia, Jacarezinho). Fica o da página.",
        "Fora do pacote: o jogo de 24/08/1924 \"Atlético 2-1 Atlético\" (a página não diz o adversário) e a Final do "
        "Interior de 2015 e 2016 (título à parte, como o Troféu do Interior do Gaúcho).",
        "Tabelas divergentes a explicar no relatório (225, contra 209 que batem). Autores dos gols: as páginas quase não "
        "trazem (6% dos gols; 2021-2026 sem autor). Cartões: só jogo a jogo, pela ficha do ogol.",
    ],
    "bra-ce-1": [
        "17 edições sem jogos em nenhuma fonte (1916-1919, 1924-1927, 1929-1932, 1934-1938) entram só com campeão e vice "
        "(importar.PODIO_SEM_JOGOS; decisão do Guilherme em 25/11). 1915 tem só a final. O Orion, campeão de 1930, só "
        "aparece nessas edições.",
        "1992: título dividido entre Fortaleza, Ceará, Tiradentes e Icasa. `co_campeao` traz os três outros separados por "
        "\" / \"; o carregador aceita um clube só (pedido ao agente 1). 2004: sem final (liminar; o STJD deu o título ao "
        "Fortaleza); a linha \"n/p\" da página fica fora.",
        "A RSSSF Brasil parou de responder em 25/11: 87 páginas vieram do Internet Archive (rsssfbrasil/origem.json). Sem "
        "página: 2025 e 2026 (jogos só do ogol). As páginas de 1988-1990 perderam os acentos (rsssf_ce1._acentos).",
        "Identidade a revisar: \"Iguatu 1996\" (o Iguatu de 1996-1997; a ficha do ogol é de 2010), \"América-R\" (1996) e "
        "\"Russas\" (1997), talvez o mesmo clube; Esporte Clube Limoeiro (1995-2000) separado do Limoeiro do ogol (2001).",
        "Fora do pacote: a Taça Padre Cícero de 2012 (título à parte). Tabelas divergentes a explicar no relatório (95, contra "
        "185 que batem). Autores dos gols: 11% (as páginas quase não trazem). Cartões: só jogo a jogo, pela ficha do ogol.",
    ],
    "bra-go-1": [
        "8 edições sem jogos (1945, 1946, 1950, 1951, 1960, 1963, 1965, 1966) entram só com campeão e vice "
        "(importar.PODIO_SEM_JOGOS). Ficam fora os campeonatos de Goiânia de 1940 e 1943 e o \"Campeonato Estadual de "
        "Goiás\" amador, que a FGF não reconhece.",
        "Vices diferentes da Wikipédia: 1958 (pacote Vila Nova, pela tabela; Wikipédia Atlético) e 2000 (pacote Vila Nova, "
        "que perdeu as duas finais de turno para o Goiás; Wikipédia Anapolina, talvez pela campanha geral).",
        "Jogos corrigidos pela tabela de confrontos (a página dá o mesmo clube aos dois lados): 1978 Anápolis 1-0 Anapolina "
        "e 1993 Mineiros 2-1 Anapolina. Outros confrontos trocados na 1ª fase de 1993 (CRAC x Goiânia duas vezes, Itumbiara "
        "x Mineiros duas vezes) ficam como a página traz.",
        "Fora do pacote: os dois amistosos de 1995 e a repetição sem data da final de 2021. Tabelas divergentes a explicar "
        "no relatório (99, contra 180 que batem). Autores dos gols: 13%. Cartões: só jogo a jogo, pela ficha do ogol.",
    ],
    "bra-sc-1": [
        "7 edições sem jogos (1925, 1926, 1928, 1933, 1934, 1943, 1945): a página só traz participantes, campeão e um ou outro "
        "jogo solto; entram com o pódio (importar.PODIO_SEM_JOGOS). 1933 não terminou: sem campeão nem vice. Muitas edições "
        "antigas (até os anos 1970) só trazem a fase estadual e as decisões de zona; 1980 só traz da 1ª fase os jogos do "
        "Joinville.",
        "Identidade a revisar: o EC Ferroviário de Tubarão (campeão de 1970) aparece na Wikipédia como \"Tubarão\"; fica "
        "separado do Tubarão FC (ficha de 1992). O Atlético Catarinense de Florianópolis (campeão de 1934) é outro clube que o "
        "de Criciúma (2020). Blumenau EC = Brasil FC e Palmeiras EC.",
        "Vices: 1967, 1969 e 2004 dados à mão (importar.VICES_MANUAIS). Diferentes da Wikipédia: 1960 (a final da página é "
        "Metropol x Avaí; a Wikipédia dá o Marcílio Dias) e 1973 e 1976 (a Wikipédia dá o Atlético Alto Vale, fundado em 1995).",
        "Fora do pacote: o Torneio Início, os amistosos com clubes de outros estados (1941), as linhas de classificação lidas "
        "como jogo e as notas lidas como jogo (1938, 1963, 1998). Tabelas divergentes a explicar (90, contra 114 que batem). "
        "Autores dos gols: 16%. Cartões: só jogo a jogo, pela ficha do ogol.",
    ],
    "bra-ba-1": [
        "23 edições sem jogos entram só com campeão e vice (importar.PODIO_SEM_JOGOS): 1922-1935, 1970 e 1982 (a lista da "
        "RSSSF Brasil tem o link, mas a página nunca foi criada: 404 no site e no Internet Archive), 1938, 1961-1963, 1969, "
        "1971 e 1974 (sem página). 1991 só tem o jogo final (Bahia 1x1 Vitória).",
        "Títulos divididos (D-07): 1938 (Bahia e Botafogo, sem jogos) e 1999 (Bahia e Vitória; vice o Conquista, pela "
        "tabela; a Wikipédia dá o Poções). 1991: vice o Vitória, pela final da RSSSF; a Wikipédia dá o Fluminense de Feira. "
        "1946: campeão (Guarany) e vice (Ypiranga) à mão, como a página dá.",
        "Mesmo nome, clubes diferentes, separados por ano (importar.NOME_ANO): \"Atlético\" (Atlético FC de Salvador, o "
        "ex-Santos Dumont, até 1969; o Alagoinhas Atlético Clube depois), \"Fluminense\" (de Salvador até 1940; o de Feira "
        "depois), \"Conquista\" (1960-1977, antes do Conquista FC do ogol) e \"São Francisco\" (1996-1998). O Vitória de "
        "Ilhéus (1967-1968) é outro clube que o Vitória. A revisar: o Guarany SC de 1915 e o de 1942-1943 ficam juntos com "
        "a AD Guarany (1944-1966; \"Guarani\" em 1944 e 1964-1966), e o Internacional de Cricket (1905) com o SC "
        "Internacional (campeão de 1914), só pelo nome.",
        "A RSSSF Brasil parou de responder: 43 páginas vieram do Internet Archive (rsssfbrasil/origem.json). As páginas de "
        "1951 a 1994 perderam os acentos (rsssf_ba1._acentos). 1975-1996: turnos com fases dentro; o turno vai na frente "
        "do título (rsssf_ba1._turno_nos_titulos).",
        "Fora do pacote: o Torneio Início e as preliminares. Tabelas divergentes a explicar (121, contra 241 que batem; "
        "a maioria em 1976-1977, 1984-1988 e 1996, turnos com mais de uma fase). Autores dos gols: 14%. Cartões: só jogo a "
        "jogo, pela ficha do ogol.",
    ],
    "bra-pe-1": [
        "2 edições sem jogos (1992 e 1993: a RSSSF Brasil nunca teve a página e o ogol não tem os jogos) entram só com "
        "campeão e vice (importar.PODIO_SEM_JOGOS). 1991 também não tem página, mas o ogol tem a final (Sport x Náutico): "
        "entra com ela. A edição 2026/27 (Turno Forró em 2026, Turno Frevo em 2027) fica de fora até terminar.",
        "1915: cinco jogos só com o vencedor (\"awd\", placar desconhecido, como no Mineiro); o empate América x Peres, "
        "sem placar na RSSSF, entra com o 0-0 do ogol, que fecha com a tabela. 1976: a página traz turno e returno lado a "
        "lado, com as datas misturadas; as datas vêm do ogol.",
        "Identidade, pelo ogol: a AA Santo Amaro, o \"Recife\" da RSSSF (1997-2004) e o Manchete são o mesmo clube "
        "(ficha 3422). A revisar: \"Vitória\" até 1998 é o Vitória de Santo Antão do cadastro (16927) e depois o Vitória "
        "das Tabocas (18691, que o ogol diz fundado em 2008); o Varzeano FC (1919-1921) e o Varzeano SC (1933) ficam juntos.",
        "Páginas da RSSSF incompletas: 2023 para na 4ª rodada e 2025 não tem a final (o resto vem do ogol). Formatos de um ano "
        "só, cada um com o seu conversor (rsssf_pe1): 1974, 1976, 1981, 2022, 2024 e 2025. 1978-1997: turnos com fases "
        "dentro (rsssf_pe1.ANOS_TURNOS).",
        "Tabelas divergentes a explicar (132, contra 241 que batem; a maioria nos turnos de 1979-1998). Autores dos gols: "
        "8%. Cartões: só jogo a jogo, pela ficha do ogol.",
    ],
}

# dicionários de decisões dos módulos de cada competição -> rótulo da seção
DICIONARIOS = {
    "BASE_OGOL": "Temporadas com o ogol como base dos jogos",
    "TABELAS_PARCIAIS": "Tabelas publicadas parciais (fora da conferência)",
    "SO_CLASSIFICACAO": "Temporadas sem os jogos na RSSSF (só as tabelas)",
    "WIKI_JUNTAR": "Temporadas completadas com jogos da Wikipédia",
    "FORMATO_INCOMPLETO": "Temporadas com parte dos jogos",
    "OBS_EDICAO": "Observações das edições",
    "CORRIGE_OGOL": "Clube trocado pelo ogol numa temporada (código -> código)",
    "CORRIGE_OGOL_JOGO": "Clube trocado pelo ogol num jogo",
    "NOME_MANUAL": "Nome da página casado à mão com o clube",
    "NOME_MANUAL_GRUPO": "Nome da página casado à mão, por grupo",
    "MANUAL_ANTIGO": "Clube das edições antigas casado à mão",
    "NOME_ANTIGO": "Nome curto das fases seguintes casado à mão (edições antigas)",
    "NOME_WIKI": "Nome da Wikipédia casado à mão",
    "NOME_CORRIGIDO": "Grafias da página corrigidas",
    "CIDADES": "Cidades abreviadas nas tabelas antigas",
    "CIDADE_DO_CLUBE": "Cidade de um clube corrigida",
    "CIDADE_DA_LINHA": "Cidade de uma linha de tabela corrigida",
    "JOGOS_FORA": "Jogos que ficam fora",
    "JOGOS_ANULADOS": "Jogos anulados",
    "RSSSF_FORA": "Clubes com todos os jogos fora",
    "OGOL_IGNORAR": "Jogos do ogol ignorados",
    "PLACAR_MANUAL": "Placares e jogos corrigidos à mão",
    "CORRECAO_JOGO": "Jogos corrigidos (placar, data, mando)",
    "AJUSTE_MANUAL": "Punições em pontos",
    "AJUSTE_FORA": "Punições que não valem",
    "FASE_ANO": "Fases da página renomeadas (por temporada)",
    "GRUPO_ANO": "Grupos montados à mão (por temporada)",
    "FASE": "Seções da Wikipédia -> fase e grupo",
    "EXPLICACOES": "Ocorrências explicadas, por temporada",
    "MANUAL_DB": "Clube do ogol casado à mão com o nome do banco",
    "MANUAL_NOVO": "Nome de exibição de clube novo, dado à mão",
    "FICHA_CORRIGIDA": "Fichas do ogol com cidade ou estado errados",
    "ANOS_A_PARTE": "Anos com torneio à parte na página (fica fora)",
    "TURNOS": "Anos com turnos (Taça Guanabara, Taça Rio) nos títulos das fases",
    "LETRAS": "Letras trocadas na página da RSSSF",
    "SEM_VICE": "Edições sem vice",
    "NOME_CODIGO": "Nomes da página casados à mão com o clube (todas as temporadas)",
    "NOME_ANO": "Nomes ambíguos casados à mão, por temporada",
    "GRAFIAS": "Grafias erradas da página (texto escaneado)",
    "CAMPEOES_DIVIDIDOS": "Títulos divididos (D-07)",
}

CAMPOS_COBERTURA = [("data", "data"), ("hora", "hora"), ("rodada", "rodada"), ("estadio", "estádio"), ("cidade", "cidade"),
                    ("publico", "público")]


def ler(slug: str, nome: str) -> list[dict]:
    arq = RAIZ / "data" / "coleta" / slug / "pacote" / f"{nome}.csv"
    if not arq.exists():
        return []
    with arq.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def modulos(slug: str) -> list:
    """Carrega os módulos de coleta/<slug>/ sem rodar a importação. Os módulos das competições têm os mesmos nomes
    (importar, edicoes, pacote...) e o leitor comum da RSSSF guarda as correções de quem o carregou: limpa entre uma e
    outra."""
    pasta = RAIZ / "coleta" / slug
    nomes = {p.stem for d in COMPETICOES for p in (RAIZ / "coleta" / d).glob("*.py")} | {"rsssf", "gols", "ogol", "registro"}
    for m in [m for m in sys.modules if m in nomes]:
        del sys.modules[m]
    sys.path[:] = [p for p in sys.path if Path(p).name not in COMPETICOES]
    sys.path.insert(0, str(pasta))
    if str(AQUI) not in sys.path:
        sys.path.insert(1, str(AQUI))
    saida = []
    for arq in sorted(pasta.glob("*.py")):
        if arq.stem.startswith("baixar") or arq.stem in ("pacote",):
            continue
        saida.append(importlib.import_module(arq.stem))
    return saida


def pct(a: int, b: int) -> str:
    return "—" if not b else f"{100 * a / b:.0f}%"


def num(x) -> int:
    try:
        return int(x)
    except (TypeError, ValueError):
        return 0


def texto_valor(v) -> str:
    """Valor de um dicionário de decisões: o motivo (texto mais longo) e os códigos/números curtos antes."""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        motivo = v.get("motivo", "")
        resto = ", ".join(f"{k}={x}" for k, x in v.items() if k != "motivo")
        return (f"[{resto}] " if resto else "") + str(motivo)
    if isinstance(v, (tuple, list)):
        textos = [x for x in v if isinstance(x, str)]
        motivo = max(textos, key=len) if textos else ""
        outros = [str(x) for x in v if x is not None and not (isinstance(x, str) and x == motivo)]
        return (f"[{', '.join(outros)}] " if outros else "") + motivo
    return str(v)


def texto_chave(k) -> str:
    return " · ".join(str(x) for x in k) if isinstance(k, tuple) else str(k)


def decada(t: str) -> str:
    return f"{t[:3]}0s"


def no_banco(slug: str) -> str:
    """Edições e jogos da competição no db/futebol.db (só leitura)."""
    con = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    r = con.execute("SELECT (SELECT count(*) FROM edicao e WHERE e.competicao_id = c.competicao_id), (SELECT count(*) FROM partida p "
                    "JOIN edicao e ON p.edicao_id = e.edicao_id WHERE e.competicao_id = c.competicao_id) FROM competicao c "
                    "WHERE c.slug = ?", (slug,)).fetchone()
    con.close()
    return f"sim ({r[0]} edições, {r[1]} jogos)" if r else "não"


def paragrafo(rel: str, rotulo: str) -> str | None:
    m = re.search(rf"\*\*{rotulo}:\*\*\s*(.*?)\n\s*\n", rel, re.S)
    return re.sub(r"\s*\n\s*", " ", m.group(1)).strip() if m else None


def ficha(slug: str) -> tuple[str, dict]:
    mods = modulos(slug)
    comp = json.loads((RAIZ / "data" / "coleta" / slug / "pacote" / "competicao.json").read_text(encoding="utf-8"))
    ed, part, gols, cart = ler(slug, "edicoes"), ler(slug, "partidas"), ler(slug, "gols"), ler(slug, "cartoes")
    clf, fases, art, conf = ler(slug, "classificacao_final"), ler(slug, "fases"), ler(slug, "artilheiros"), ler(slug, "conferencia")
    clubes, pub, rod = ler(slug, "clubes"), ler(slug, "tabelas_publicadas"), ler(slug, "classificacao_rodada")
    temporada_de = {p["id"]: p["temporada"] for p in part}
    gols_por_t = Counter(temporada_de.get(g["partida_id"]) for g in gols)
    cart_por_t = Counter(temporada_de.get(c["partida_id"]) for c in cart)
    total_gols = sum(num(p["gols_mandante"]) + num(p["gols_visitante"]) for p in part)
    jogos_t = Counter(p["temporada"] for p in part)
    copa = comp.get("tipo") == "copa" or "copa" in slug
    banco = no_banco(slug)

    out = [f"# {comp['nome']} (`{slug}`) — documentação", "",
           f"Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/{slug}/pacote/` e dos módulos de "
           f"`coleta/{slug}/`. O relatório da importação, com as ocorrências temporada a temporada, está em "
           f"`docs/coleta/{slug}.md`.", ""]

    # ---- 1. o que temos
    sem_jogos = [e["temporada"] for e in ed if not jogos_t.get(e["temporada"])]
    incompletas = [e["temporada"] for e in ed if "incomplet" in (e["formato"] or "") and jogos_t.get(e["temporada"])]
    out += ["## 1. O que temos", "",
            f"- **Edições:** {len(ed)}, de {ed[0]['temporada']} a {ed[-1]['temporada']}"
            + (f"; sem nenhum jogo: {', '.join(sem_jogos)}" if sem_jogos else "")
            + (f"; com parte dos jogos: {', '.join(incompletas)}" if incompletas else "") + ".",
            f"- **Jogos:** {len(part)}; **gols:** {total_gols}; **gols com autor:** {len(gols)} ({pct(len(gols), total_gols)}); "
            f"**cartões:** {len(cart)}.",
            f"- **Clubes:** {len(clubes)}; **artilheiros:** {len({a['temporada'] for a in art})} temporadas com artilheiro "
            f"({len(art)} linhas, com empates).",
            f"- **Classificação final:** {len({c['temporada'] for c in clf})} temporadas; **rodada a rodada:** "
            f"{len({r['temporada'] for r in rod})} temporadas.",
            f"- **Tabelas publicadas guardadas para conferência:** {len(pub)} linhas.",
            f"- **No banco (`db/futebol.db`):** {banco}.",
            f"- **Observação da competição:** {comp.get('observacao') or '—'}", ""]

    # ---- 2. fontes e regras (do relatório)
    rel = (RAIZ / "docs" / "coleta" / f"{slug}.md").read_text(encoding="utf-8")
    out += ["## 2. Fontes e regras", ""]
    for rot in ("Temporadas", "Fontes", "Regras", "Desempate", "Edições sem os jogos"):
        if (p := paragrafo(rel, rot)):
            out += [f"**{rot}:** {p}", ""]

    # ---- 3. conferência
    ok = sum(num(c["tabelas_conferidas"]) for c in conf)
    div = sum(num(c["tabelas_divergentes"]) for c in conf)
    com_div = [c["temporada"] for c in conf if num(c["tabelas_divergentes"]) > 0]
    sem_tab = [c["temporada"] for c in conf if not num(c["tabelas_conferidas"]) and not num(c["tabelas_divergentes"])]
    faltam = [f"{c['temporada']} ({c['jogos']} de {c['jogos_esperados']})" for c in conf
              if c["jogos_esperados"] and num(c["jogos"]) < num(c["jogos_esperados"])]
    out += ["## 3. Conferência", "",
            f"- Cada temporada é comparada com as tabelas publicadas ({'RSSSF; Wikipédia em 1965 e 1990' if slug == 'bra-sp-2' else 'RSSSF'}): {ok} tabelas "
            f"fecham com os jogos e {div} divergem (cada divergência é explicada no relatório, na temporada).",
            f"- Temporadas com alguma tabela divergente: {', '.join(com_div) or 'nenhuma'}.",
            f"- Temporadas sem tabela para conferir: {', '.join(sem_tab) or 'nenhuma'}.",
            f"- Temporadas com menos jogos do que o ogol: {', '.join(faltam) or 'nenhuma'}.", ""]

    # ---- 4. cobertura por década
    por_dec = defaultdict(list)
    for p in part:
        por_dec[decada(p["temporada"])].append(p)
    gols_dec, golsaut_dec, cart_dec = Counter(), Counter(), Counter()
    for p in part:
        gols_dec[decada(p["temporada"])] += num(p["gols_mandante"]) + num(p["gols_visitante"])
    for t, n in gols_por_t.items():
        if t:
            golsaut_dec[decada(t)] += n
    for t, n in cart_por_t.items():
        if t:
            cart_dec[decada(t)] += n
    out += ["## 4. Cobertura de cada campo, por década", "",
            "Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).", "",
            "| Década | Jogos | " + " | ".join(r for _, r in CAMPOS_COBERTURA) + " | gols c/ autor | cartões/jogo |",
            "|" + "---|" * (len(CAMPOS_COBERTURA) + 4)]
    for d in sorted(por_dec):
        ps = por_dec[d]
        cel = [pct(sum(1 for p in ps if p.get(c)), len(ps)) for c, _ in CAMPOS_COBERTURA]
        out.append(f"| {d} | {len(ps)} | " + " | ".join(cel) + f" | {pct(golsaut_dec[d], gols_dec[d])} | {cart_dec[d] / len(ps):.1f} |")
    fontes_j = Counter(p["fonte"] for p in part)
    out += ["", "**Fonte de cada jogo:** " + "; ".join(f"{f or '—'}: {n}" for f, n in fontes_j.most_common()) + ".", ""]

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
    out += ["## 5. Formato ao longo do tempo", "", "**Número de clubes:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v} clubes" for v, a, b in faixas(lambda e: e["num_clubes"])]
    out += ["", "**Pontos por vitória:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["pontos_vitoria"])]
    out += ["", "**Nome oficial:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["nome_oficial"])]
    out += ["", "**Formato de cada edição** (fases na ordem; grupos; mata-mata):", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["formato"])]
    por_t = defaultdict(list)
    for f in fases:
        por_t[f["temporada"]].append(f)
    nomes_fases = Counter(f["fase"] for f in fases)
    out += ["", "**Fases que aparecem** (número de temporadas): " + "; ".join(f"{f} ({n})" for f, n in nomes_fases.most_common()) + "."]
    crit = Counter(f["criterio"] for f in fases if f["criterio"])
    if crit:
        out += ["", "**Critério de desempate:** " + "; ".join(f"{c} ({n} fases)" for c, n in crit.most_common()) + "."]
    obs = [(e["temporada"], e["observacao"]) for e in ed if e["observacao"]]
    out += ["", "**Observações das edições:**", ""]
    out += [f"- {t}: {o}" for t, o in obs] or ["- nenhuma"]
    out.append("")

    # ---- 6. campeões, acessos, rebaixados e punições
    camp = Counter(e["campeao"] for e in ed if e["campeao"])
    sem_campeao = [e["temporada"] for e in ed if not e["campeao"]]
    sit = defaultdict(Counter)
    for c in clf:
        if c["situacao"]:
            sit[c["situacao"]][c["clube"]] += 1
    puni = [(c["temporada"], c["clube"], c["ajuste_pontos"]) for c in clf if c["ajuste_pontos"] not in ("", "0")]
    out += ["## 6. Campeões, acessos, rebaixados e punições", "", "**Títulos:**", ""]
    out += [f"- {c}: {n}" for c, n in camp.most_common()]
    if sem_campeao:
        out += [f"- Sem campeão: {', '.join(sem_campeao)}"]
    for s, rot in (("acesso", "Acessos"), ("rebaixado", "Rebaixamentos")):
        if sit.get(s):
            out += ["", f"**{rot}:** {sum(sit[s].values())} no total; quem mais teve: "
                    + ", ".join(f"{c} ({n})" for c, n in sit[s].most_common(8)) + "."]
        elif not copa:
            out += ["", f"**{rot}:** nenhum marcado no pacote."]
    out += ["", "**Punições em pontos:**", ""]
    out += [f"- {t}: {c} {a}" for t, c, a in puni] or ["- nenhuma"]
    out.append("")

    # ---- 7. correções e decisões
    out += ["## 7. Correções e decisões (com o motivo)", "",
            f"Registradas nos módulos de `coleta/{slug}/`; cada uma também aparece no relatório, na temporada.", ""]
    achou = False
    for nome, rotulo in DICIONARIOS.items():
        for mod in mods:
            v = getattr(mod, nome, None)
            if not v or not isinstance(v, (dict, set, frozenset, list)):
                continue
            achou = True
            out += [f"### {rotulo} (`{mod.__name__}.{nome}`)", ""]
            if isinstance(v, dict) and len(v) > 40 and all(isinstance(k, tuple) and str(k[0])[:4].isdigit() for k in v):
                # muitas entradas por temporada (faixas de anos geradas): uma linha por valor, com os anos juntos
                grupos: dict[tuple, list] = {}
                for k, x in v.items():
                    grupos.setdefault((k[1:], texto_valor(x)), []).append(int(str(k[0])[:4]))
                for (resto, valor), anos in grupos.items():
                    anos = sorted(set(anos))
                    faixa = f"{anos[0]}-{anos[-1]}" if len(anos) > 1 and anos[-1] - anos[0] + 1 == len(anos) else \
                        ", ".join(map(str, anos))
                    out += [f"- **{faixa} · {' · '.join(map(str, resto))}:** {valor}"]
            elif isinstance(v, dict):
                for k, x in v.items():
                    if isinstance(x, list) and all(isinstance(i, str) for i in x):
                        out += [f"- **{texto_chave(k)}:** " + " / ".join(x)]
                    elif isinstance(x, dict) and "motivo" not in x:
                        out += [f"- **{texto_chave(k)}:** " + "; ".join(f"{a} → {b}" for a, b in x.items())]
                    else:
                        out += [f"- **{texto_chave(k)}:** {texto_valor(x)}"]
            else:
                out += [f"- {', '.join(map(str, sorted(v)))}"]
            out.append("")
            break
    rs = sys.modules.get("rsssf")
    if rs is not None and getattr(rs, "CORRECOES", None):
        out += [f"### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/{slug}/rsssf_*.py`)", ""]
        for arq, lista in sorted(rs.CORRECOES.items()):
            motivos = list(dict.fromkeys(m for *_, m in lista if m))
            out += [f"- **{arq}:** " + "; ".join(motivos)]
        out.append("")
        achou = True
    if not achou:
        out += ["- nenhuma", ""]

    # ---- 8. limites e pendências
    m = re.search(r"## O que não deu para coletar\s*\n(.*?)(?:\n## |\Z)", rel, re.S)
    out += ["## 8. O que não deu para coletar", "", (m.group(1).strip() if m else "- (ver relatório)"), "",
            "## 9. Pendências e próximos passos", ""]
    out += [f"- {p}" for p in PENDENCIAS.get(slug, [])] or ["- nenhuma"]

    # ---- 10. arquivos e comandos
    pasta = RAIZ / "coleta" / slug
    def doc1(arq: Path) -> str:
        m = re.match(r'\s*(?:from __future__[^\n]*\n\s*)?"""(.*?)(?:\n\n|""")', arq.read_text(encoding="utf-8"), re.S)
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    out += ["", "## 10. Arquivos e comandos", "", "| Arquivo | O que faz |", "|---|---|"]
    out += [f"| `coleta/{slug}/{a.name}` | {doc1(a)[:220]} |" for a in sorted(pasta.glob("*.py"))]
    fontes_dir = sorted(p.name for p in (RAIZ / "data" / "coleta" / slug).iterdir() if p.is_dir() and p.name != "pacote")
    baixar = sorted(a.name for a in pasta.glob("baixar*.py"))
    out += ["",
            f"- Fontes baixadas: `data/coleta/{slug}/` ({', '.join(fontes_dir)}). Pacote: `data/coleta/{slug}/pacote/`. "
            f"Relatório: `docs/coleta/{slug}.md`.",
            "- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, "
            "`gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` "
            "download educado).",
            "- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):",
            ""]
    out += [f"  - `python coleta/{slug}/{b}` (ver o docstring)" for b in baixar]
    out += [f"  - `python coleta/{slug}/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)",
            f"  - `python coleta/comum/testar_carga.py {slug} <pasta temporária>` (deve terminar com `-> OK`)",
            "  - `python coleta/comum/documentar.py`", ""]
    resumo = {"slug": slug, "nome": comp["nome"], "edicoes": len(ed), "de": ed[0]["temporada"], "ate": ed[-1]["temporada"],
              "jogos": len(part), "gols_autor": len(gols), "cartoes": len(cart), "clubes": len(clubes), "tabelas_ok": ok,
              "tabelas_div": div, "pendencias": len(PENDENCIAS.get(slug, [])), "banco": banco}
    return "\n".join(out) + "\n", resumo


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    SAIDA.mkdir(exist_ok=True)
    resumos = []
    for slug in COMPETICOES:
        txt, r = ficha(slug)
        (SAIDA / f"{slug}.md").write_text(txt, encoding="utf-8")
        resumos.append(r)
        print(f"{slug}: {r['edicoes']} edições, {r['jogos']} jogos", flush=True)
    idx = ["# Coleta Brasil (agente 2) — documentação", "",
           "Gerado por `python coleta/comum/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, a cobertura "
           "de cada campo década a década, o formato ao longo do tempo, campeões, acessos, rebaixados e punições, todas as "
           "correções e decisões com o motivo, o que não deu para coletar, as pendências e os comandos para refazer.", "",
           "Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum/COMECE-AQUI.md`. "
           "Recados ao agente do banco e respostas dele: `docs/coleta/pedidos.md`. Achados da revisão: "
           "`docs/revisao/achados.csv` (`quem_corrige` = `coleta-brasil`).", "",
           "| Competição | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | No banco | Pendências | Ficha |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in resumos:
        idx.append(f"| {r['nome']} | {r['edicoes']} ({r['de']}–{r['ate']}) | {r['jogos']} | {r['gols_autor']} | {r['cartoes']} | "
                   f"{r['clubes']} | {r['tabelas_ok']} / {r['tabelas_div']} | {r['banco']} | {r['pendencias']} | "
                   f"[{r['slug']}]({r['slug']}.md) |")
    idx += ["", "Fora das fichas: `bra-serie-a-artilheiros` (artilheiros oficiais da Série A, 1937-2025, pedido do agente 1; "
            "`coleta/bra-serie-a-artilheiros/montar.py`, relatório `docs/coleta/bra-serie-a-artilheiros.md`). A Série A e a "
            "Série B são do agente 1 (`serie_b/`).", "",
            "## Pendências de todas as competições", ""]
    for slug in COMPETICOES:
        for p in PENDENCIAS.get(slug, []):
            idx.append(f"- **{slug}:** {p}")
    idx += ["", "## Próximas competições", "",
            "- Ordem dada pelo Guilherme (22/11/2026): Mineiro (`bra-mg-1`), Gaúcho (`bra-rs-1`), Paulista A3 (`bra-sp-3`). "
            "Cada uma com o ok dele.", ""]
    (SAIDA / "README.md").write_text("\n".join(idx), encoding="utf-8")


if __name__ == "__main__":
    main()
