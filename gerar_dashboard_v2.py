"""Dashboard v2: uma informação por vez, cada bloco respondendo uma pergunta.

Gera dashboard_v2.html a partir do banco genérico db/futebol.db (futebol/esquema.sql), no mesmo
visual do dashboard antigo (tema "estádio à noite", claro/escuro). O dashboard antigo
(gerar_dashboard_html.py -> dashboard.html) continua igual até a v2 cobrir o que importa.

Competições: as de COMPETICOES (hoje Séries A e B), escolhidas no seletor da barra lateral; cada uma
leva todos os seus dados na página e a escolha fica no endereço (?c=bra-serie-b) e no navegador.
abrir(slug) monta, em memória, as tabelas que as funções de dados leem, só com aquela competição;
edição com tabela rodada a rodada conta como pontos corridos (corrida por rodada, recordes de pontos).
Os textos que mudam com a competição (cabeçalho, legendas, avisos) vêm de textos() e vão nos [data-t].
Nova competição: entrar no banco, ganhar uma linha em COMPETICOES e rodar este script.

Abas (barra de navegação lateral): História (os blocos abaixo), Por campeonato e
Por clube (ainda em branco).

Sub-abas da História (na barra lateral, abaixo de "História"; uma por vez):
1. Corrida dos títulos: posição de cada clube no ranking de títulos (1º no
   topo), ano a ano, animada (botão e barra de tempo); as linhas se cruzam nas
   ultrapassagens; escudo, nome e total na ponta de cada linha.
2. Pódio por clube: uma linha por clube, com um bloco por título (com o ano,
   na cor do clube; Taça Brasil, Robertão e 1937 listrados), embaixo um bloco
   de contorno por vice e, por último, um pontilhado por 3º lugar. Escudo de
   cada clube (data/escudos/, de baixar_escudos.py) ao lado do nome.
3. Participações: uma faixa por clube com um quadradinho por edição (cheio =
   jogou; pontinho ouro/prata/bronze = 1º/2º/3º); 30 primeiros e botão para ver todos.
   Botão Quadro | Corrida: corrida (posições) das participações acumuladas, com as medalhas.
4. Jogos e vitórias: por clube, uma barra do tamanho dos jogos dividida em
   vitórias, empates e derrotas (todas as partidas: edições antigas + Série A desde 2003), com os
   dois totais e o % de vitórias; ordena por vitórias, jogos ou % (só 100+ jogos).
   Botão Barras | Corrida: corrida (posições) dos jogos ou das vitórias acumuladas,
   de 1937 a hoje, com o top 20 de cada edição ou todos os clubes.
5. Gols: por clube, uma barra com todos os gols dos seus jogos dividida em feitos
   e tomados; ordena por feitos, tomados, saldo ou média por jogo (só 100+ jogos).
   Botão Barras | Corrida: corrida (posições) dos gols feitos, tomados ou do saldo acumulados.
6. Pontuação histórica: vitória vale 3 e empate 1, em todas as partidas; barra do tamanho dos
   pontos possíveis (3 por jogo) com os pontos das vitórias, dos empates e os perdidos; ordena por
   pontos ou aproveitamento (só 100+ jogos). Botão Barras | Corrida: corrida dos pontos acumulados.
7. Estatísticas e curiosidades: recordes em cartões, em quatro partes (Jogos | Clubes | Campeões |
   Edições), com mando de campo e placares mais comuns, títulos por estado e campeões por década,
   e gols por jogo em cada edição.

Aba Por campeonato: escolhe a edição (lista por década ou setas; fica no endereço,
#campeonato/resumo/2019) e vê os números dela no topo. Sub-abas na lateral:
- Resumo: pódio, destaques (ataque, defesa, vitórias, empates, jogo com mais gols, mando de campo,
  melhor mandante e visitante, vantagem do campeão, artilheiro, lanterna) e como foi a disputa (fases);
- Classificação: classificação final com a campanha de cada clube;
- Corrida: posição rodada a rodada (de 2003 em diante), com as faixas de título, Libertadores,
  Sul-Americana e rebaixamento;
- Jogos: todos os resultados, por rodada (desde 2003) ou por fase (antes);
- Artilharia: os 10 maiores artilheiros (desde 2003).

Aba Por clube: escolhe o clube (lista ou setas; #clube/resumo/palmeiras) e vê os números dele no topo.
Sub-abas: Resumo (trajetória da posição final em cada edição, pódios e destaques), Campanhas (edição a
edição; a linha leva à edição), Confrontos (retrospecto contra cada adversário), Jogos (os jogos do clube
em cada edição) e Artilharia (desde 2003). Na classificação de uma edição, o nome do clube leva à aba dele.

Uso: python gerar_dashboard_v2.py
"""
from __future__ import annotations

import base64
import io
import json
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "db" / "futebol.db"   # banco genérico (futebol/esquema.sql)
# competições do seletor, na ordem: rótulo das edições sem nome próprio (a Série A soma Taça Brasil, Robertão...),
# nome curto, nome completo, "do/da ..." (títulos) e "o/a ..." (frases)
COMPETICOES = {
    "bra-serie-a": {"menu": "Brasileirão Série A", "rotulo": "Campeonato Brasileiro", "curto": "Brasileirão", "nome": "Campeonato Brasileiro", "do": "do Brasileirão", "o": "o Brasileiro"},
    "bra-serie-b": {"menu": "Brasileirão Série B", "rotulo": "Série B", "curto": "Série B", "nome": "Campeonato Brasileiro Série B", "do": "da Série B", "o": "a Série B"},
}


# bandeiras (data/worldcup_wikipedia/flags/<iso>.png, da parte da Copa do Mundo): código FIFA -> arquivo
BANDEIRA = {"BRA": "br", "ARG": "ar", "URU": "uy", "CHI": "cl", "COL": "co", "PAR": "py", "PER": "pe", "ECU": "ec", "BOL": "bo", "VEN": "ve",
            "ENG": "gb-eng", "SCO": "gb-sct", "WAL": "gb-wls", "NIR": "gb-nir", "ESP": "es", "ITA": "it", "GER": "de", "FRA": "fr",
            "POR": "pt", "NED": "nl", "BEL": "be", "TUR": "tr", "MEX": "mx", "USA": "us", "EGY": "eg", "NZL": "nz", "JPN": "jp", "GDR": "dd", "MAR": "ma", "TAH": "pf", "CAN": "ca", "ALG": "dz", "HON": "hn", "KOR": "kr", "CRC": "cr", "TUN": "tn", "NCL": "nc", "RSA": "za", "FIJ": "fj", "GUA": "gt", "NGA": "ng"}
CONTINENTE = {"CONMEBOL": "América do Sul", "UEFA": "Europa", "CONCACAF": "América do Norte e Central", "CAF": "África",
              "AFC": "Ásia", "OFC": "Oceania"}
GRUPO = {"liga": "Ligas", "copa": "Copas", "estadual": "Estaduais"}


def catalogo(dados: dict) -> list[dict]:
    """Uma entrada por competição do seletor: slug, nome, rótulo dentro do país ("Série A", "1ª divisão", "Paulista"),
    país, bandeira, continente, grupo (Ligas, Copas, Estaduais) e período. Copia as bandeiras para painel/bandeiras/."""
    import shutil
    pasta = PAINEL / "bandeiras"
    pasta.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    saida = []
    for slug, c in COMPETICOES.items():
        tipo, nivel, curto, pcod, pnome, conf = con.execute(
            """SELECT k.tipo, k.nivel, k.nome_curto, pa.codigo, pa.nome, coalesce(k.confederacao, pa.confederacao)
               FROM competicao k LEFT JOIN pais pa USING (pais_id) WHERE k.slug = ?""", (slug,)).fetchone()
        band = ""
        if BANDEIRA.get(pcod):
            origem = ROOT / "data" / "worldcup_wikipedia" / "flags" / f"{BANDEIRA[pcod]}.png"
            if origem.exists():
                destino = pasta / origem.name
                if not destino.exists() or destino.read_bytes() != origem.read_bytes():
                    shutil.copyfile(origem, destino)
                band = "bandeiras/" + origem.name
        eds = dados[slug]["EDP"]
        rot = (curto if pcod == "BRA" else f"{nivel}ª divisão") if tipo == "liga" and nivel else c["curto"]
        saida.append({"s": slug, "nome": c["nome"], "curto": rot, "pais": pcod or "", "pn": pnome or "", "band": band,
                      "cont": CONTINENTE.get(conf, "Outros"), "grupo": GRUPO.get(tipo, "Outras"),
                      "per": f"{eds[0].get('t') or eds[0]['ano']} a {eds[-1].get('t') or eds[-1]['ano']}"})
    con.close()
    return saida


# pacotes que o Guilherme liberou para o painel (pacote em andamento fica no banco, mas não aparece no seletor)
LIBERADAS = {"bra-serie-c", "bra-serie-d", "bra-copa-do-brasil", "bra-sp-1", "arg-1", "eng-1", "esp-1", "uru-1", "ita-1", "chi-1", "col-1", "ger-1", "par-1", "per-1", "ecu-1", "bra-sp-2", "bol-1", "por-1", "ned-1", "ven-1", "fra-1", "sco-1", "bra-rj-1", "egy-1", "nzl-1", "bel-1", "tur-1", "usa-1", "gdr-1", "uru-copa", "par-copa", "ecu-copa", "col-copa", "arg-copa", "hon-1", "tah-1", "ncl-1", "mex-1", "jpn-1", "mar-1", "alg-1", "crc-1", "tun-1", "chi-copa", "rsa-1", "fij-1", "gua-1", "ven-copa", "kor-1"}


def competicoes_dos_pacotes() -> None:
    """Acrescenta a COMPETICOES as competições dos pacotes do agente de coleta que já estão no banco
    (data/coleta/<slug>/pacote/competicao.json: menu_painel, rotulo_painel, do_painel, o_painel)."""
    no_banco = {s for (s,) in sqlite3.connect(DB).execute("SELECT slug FROM competicao")}
    achadas = []
    for f in sorted((ROOT / "data" / "coleta").glob("*/pacote/competicao.json")):
        c = json.loads(f.read_text(encoding="utf-8"))
        if c["slug"] in COMPETICOES or c["slug"] not in no_banco or c["slug"] not in LIBERADAS:
            continue
        rot = c.get("rotulo_painel") or c.get("nome_curto") or c["nome"]
        achadas.append(((c.get("pais") != "BRA", c.get("pais") or "", c.get("tipo") != "liga", c.get("nivel") or 99, c["slug"]), c["slug"], {
            "menu": c.get("menu_painel") or c["nome"], "rotulo": rot, "curto": rot, "nome": c["nome"],
            "do": c.get("do_painel") or f"da {rot}", "o": c.get("o_painel") or f"a {rot}"}))
    for _, slug, conf in sorted(achadas):   # Brasil primeiro; depois por país, ligas antes de copas, por divisão
        COMPETICOES[slug] = conf
PAINEL = ROOT / "painel"   # index.html + dados/<competição>.js + escudos/ (abre com duplo clique e vai assim para a internet)
ATALHO = ROOT / "dashboard_v2.html"   # só leva para painel/index.html
ESCUDOS = ROOT / "data" / "escudos"   # baixados por baixar_escudos.py (Wikipédia)

# nomes do banco (sem acento, com sufixo de estado) -> nome para exibir
NOMES_EXIBICAO = {
    "America-MG": "América-MG",
    "America-RN": "América-RN",
    "Atletico-GO": "Atlético-GO",
    "Avai": "Avaí",
    "Criciuma": "Criciúma",
    "Cuiaba": "Cuiabá",
    "Gremio Prudente": "Grêmio Prudente",
    "Parana": "Paraná",
    "Santo Andre": "Santo André",
    "America-RJ": "América-RJ",
    "Atletico-MG": "Atlético-MG",
    "Botafogo-RJ": "Botafogo",
    "Ceara": "Ceará",
    "Goias": "Goiás",
    "Gremio": "Grêmio",
    "Nautico": "Náutico",
    "Sao Caetano": "São Caetano",
    "Sao Paulo": "São Paulo",
    "Vitoria": "Vitória",
}
# cores do clube (principal, segunda), escritas à mão; os outros clubes têm a cor tirada do escudo (cores_auto)
CORES = {
    "América-RJ": ("#c8102e", "#f5f5f5"), "Brasil de Pelotas": ("#d50000", "#111111"), "Ceará": ("#111111", "#f5f5f5"),
    "Goiás": ("#00703c", "#f5f5f5"), "Operário-MS": ("#111111", "#f5f5f5"), "Ponte Preta": ("#111111", "#f5f5f5"), "Rio Branco-ES": ("#111111", "#f5f5f5"),
    "Paysandu": ("#00a1e4", "#f5f5f5"), "Santa Cruz": ("#e30613", "#111111"), "Juventude": ("#00843d", "#f5f5f5"),
    "América-MG": ("#00843d", "#111111"), "CSA": ("#0033a0", "#f5f5f5"), "Figueirense": ("#111111", "#f5f5f5"),
    "Athletico-PR": ("#c8102e", "#111111"), "Atlético-MG": ("#111111", "#f5f5f5"), "Bahia": ("#0067b1", "#e2001a"),
    "Bangu": ("#e30613", "#f5f5f5"), "Botafogo": ("#111111", "#f5f5f5"), "Bragantino": ("#f5f5f5", "#d50032"),
    "Corinthians": ("#111111", "#f5f5f5"), "Coritiba": ("#00544e", "#f5f5f5"), "Cruzeiro": ("#003da5", "#f5f5f5"),
    "Flamengo": ("#c4161c", "#111111"), "Fluminense": ("#7a1631", "#00613c"), "Fortaleza": ("#0a3a87", "#e30613"),
    "Grêmio": ("#0d80bf", "#111111"), "Guarani": ("#00843d", "#f5f5f5"), "Internacional": ("#e30613", "#f5f5f5"),
    "Náutico": ("#e30613", "#f5f5f5"), "Palmeiras": ("#006437", "#f5f5f5"), "Portuguesa": ("#e30613", "#006437"),
    "Santos": ("#f5f5f5", "#111111"), "São Caetano": ("#00529b", "#f5f5f5"), "São Paulo": ("#e30613", "#111111"),
    "Sport": ("#e30613", "#111111"), "Vasco": ("#111111", "#e30613"), "Vitória": ("#e30613", "#111111"),
}
# competição -> etiqueta (o Brasileiro não leva)
COMPETICAO_CURTA = {
    "Taça Brasil": "Taça Brasil",
    "Torneio Roberto Gomes Pedrosa": "Robertão",
    "Torneio dos Campeões": "Torneio dos Campeões",
    "Taça de Prata": "Taça de Prata",
    "Taça de Bronze": "Taça de Bronze",
    "Copa João Havelange": "Copa João Havelange",
}
NOTAS = {   # competição -> edição -> nota
    "bra-serie-a": {
        "2005": "11 jogos foram anulados e disputados de novo (escândalo da Máfia do Apito); o banco tem os jogos refeitos.",
        "2016": "Chapecoense x Atlético-MG, da última rodada, não foi disputado, por causa do acidente aéreo da Chapecoense.",
        "1987": "A CBF reconhece o Sport. O Flamengo venceu a Copa União (Módulo Verde) e não disputou o quadrangular final com Sport e Guarani.",
    },
}


def notas(con: sqlite3.Connection) -> dict[str, str]:
    (slug,) = con.execute("SELECT slug FROM rotulo").fetchone()
    return NOTAS.get(slug, {})


def abrir(slug: str) -> sqlite3.Connection:
    """Banco em memória com as tabelas que as funções abaixo leem, só com a competição `slug` de db/futebol.db.
    Edição com tabela rodada a rodada (pontos corridos) é "moderna": os jogos vão para fato_partida, por temporada;
    os das outras, para fato_partida_nacional_historica, por fase."""
    con = sqlite3.connect(":memory:")
    con.execute("ATTACH DATABASE ? AS f", (str(DB),))
    (cid,) = con.execute("SELECT competicao_id FROM f.competicao WHERE slug = ?", (slug,)).fetchone()
    con.execute("CREATE TABLE rotulo AS SELECT ? AS padrao, ? AS slug, (SELECT tipo FROM f.competicao WHERE slug = ?) AS tipo",
                (COMPETICOES[slug]["rotulo"], slug, slug))
    con.execute("CREATE TABLE curta (nome TEXT)")
    con.executemany("INSERT INTO curta VALUES (?)", [(n,) for n in COMPETICAO_CURTA])
    con.executescript(f"""
        CREATE TABLE dim_clube AS SELECT clube_id, nome, regiao AS uf FROM f.clube;
        CREATE TABLE dim_edicao_nacional AS
          SELECT e.edicao_id AS edicao_nacional_id, e.chave AS edicao_id, CASE WHEN e.nome_oficial IN (SELECT nome FROM curta) THEN e.nome_oficial
                      WHEN instr(e.temporada, ' ') > 0 THEN substr(e.temporada, instr(e.temporada, ' ') + 1)
                      ELSE (SELECT padrao FROM rotulo) END AS competicao_nome,
                 CASE WHEN e.formato = 'mata-mata' THEN 'mata' ELSE '' END AS tipo,
                 e.pontos_vitoria, coalesce(e.pontos_empate, 1) AS pontos_empate, coalesce(e.pontos_derrota, 0) AS pontos_derrota,
                 e.ano_inicio AS temporada_id, e.temporada, e.campeao_id IS NOT NULL AS tem_campeao, e.observacao, e.nome_oficial,
                 coalesce(e.formato, '') LIKE 'jogos incompletos%' AS incompleta,
                 coalesce(e.oficial, 1) AS oficial,   -- 0: edição não oficial (D-10), sem título
                 (SELECT nome FROM f.clube WHERE clube_id = e.co_campeao_id) AS co_campeao,   -- título dividido (D-07): o outro campeão   -- só parte dos jogos (ex.: Paulista A2 antiga)
                 -- pontos corridos: tabela rodada a rodada, fase única e todo jogo com rodada (senão fica por fase);
                 -- jogos-desempate (fase "Desempate...") ficam fora da tabela e não contam aqui (IT-018)
                 EXISTS (SELECT 1 FROM f.classificacao_rodada r WHERE r.edicao_id = e.edicao_id)
                 AND (SELECT count(*) FROM f.fase x WHERE x.edicao_id = e.edicao_id AND x.nome NOT LIKE 'Desempate%') = 1
                 AND NOT EXISTS (SELECT 1 FROM f.partida x JOIN f.fase y ON y.fase_id = x.fase_id
                                 WHERE x.edicao_id = e.edicao_id AND x.rodada IS NULL AND y.nome NOT LIKE 'Desempate%') AS moderna
          FROM f.edicao e WHERE e.competicao_id = {cid}
            -- edição vazia (ano sem campeonato, ou sem tabela e sem jogos na fonte) fica fora do painel
            AND (EXISTS (SELECT 1 FROM f.classificacao_final x WHERE x.edicao_id = e.edicao_id)
                 OR EXISTS (SELECT 1 FROM f.partida x WHERE x.edicao_id = e.edicao_id)
                 OR EXISTS (SELECT 1 FROM f.tabela_publicada x WHERE x.edicao_id = e.edicao_id));
        CREATE TABLE dim_fase_nacional_historica AS
          SELECT x.fase_id AS fase_nacional_id, x.edicao_id AS edicao_nacional_id, x.ordem AS fase_ordem, x.nome AS fase_nome,
                 x.tipo AS fase_tipo, x.num_grupos, x.formato_serie
          FROM f.fase x JOIN dim_edicao_nacional d ON d.edicao_nacional_id = x.edicao_id WHERE NOT d.moderna OR x.nome LIKE 'Desempate%';
        CREATE TABLE fato_partida_nacional_historica AS
          SELECT p.fase_id AS fase_nacional_id, p.edicao_id AS edicao_nacional_id, d.temporada_id, p.mandante_id, p.visitante_id,
                 p.gols_mandante, p.gols_visitante, p.grupo, p.data, p.partida_id AS jogo, p.penaltis_mandante, p.penaltis_visitante
          FROM f.partida p JOIN dim_edicao_nacional d ON d.edicao_nacional_id = p.edicao_id JOIN f.fase y ON y.fase_id = p.fase_id
          WHERE (NOT d.moderna OR y.nome LIKE 'Desempate%') AND p.gols_mandante IS NOT NULL;
        CREATE TABLE fato_partida AS
          SELECT d.temporada_id, p.rodada, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante, p.data
          FROM f.partida p JOIN dim_edicao_nacional d ON d.edicao_nacional_id = p.edicao_id JOIN f.fase y ON y.fase_id = p.fase_id
          WHERE d.moderna AND y.nome NOT LIKE 'Desempate%';
        CREATE TABLE fato_classificacao_final_nacional AS
          SELECT c.edicao_id AS edicao_nacional_id, c.clube_id, c.posicao,
                 c.jogos, c.vitorias, c.empates, c.derrotas, c.gols_pro, c.gols_contra, c.ajuste_pontos, c.situacao, c.pontos
          FROM f.classificacao_final c JOIN dim_edicao_nacional d ON d.edicao_nacional_id = c.edicao_id;
        CREATE TABLE fato_classificacao_rodada AS
          SELECT d.temporada_id, r.rodada, r.clube_id, r.posicao, r.pontos, r.zona
          FROM f.classificacao_rodada r JOIN dim_edicao_nacional d ON d.edicao_nacional_id = r.edicao_id WHERE d.moderna;
        CREATE TABLE fato_artilheiro AS
          SELECT a.edicao_id AS edicao_nacional_id, a.jogador, a.clube_id, a.gols
          FROM f.artilheiro a JOIN dim_edicao_nacional d ON d.edicao_nacional_id = a.edicao_id WHERE a.gols IS NOT NULL;
        CREATE TABLE fato_gol AS
          SELECT p.edicao_id AS edicao_nacional_id, d.temporada_id, g.jogador, g.clube_id, g.tipo
          FROM f.gol g JOIN f.partida p USING (partida_id) JOIN dim_edicao_nacional d ON d.edicao_nacional_id = p.edicao_id
          WHERE g.jogador IS NOT NULL AND g.jogador <> '' AND g.jogador NOT LIKE 'Nao informado%';
    """)
    return con


def temporada_texto(temporada: str) -> str | None:
    """"1992/93" (temporada que cruza o ano; "1991/92 Apertura" -> "1991/92"); None quando é só o ano."""
    t = (temporada or "").split(" ")[0]
    return t if "/" in t else None


def rotulo_ed(con: sqlite3.Connection, comp: str) -> str:
    """Etiqueta da edição ao lado do ano: vazia quando é a própria competição ("2019"), senão "Taça Brasil", "Apertura"..."""
    (padrao,) = con.execute("SELECT padrao FROM rotulo").fetchone()
    return "" if comp == padrao else COMPETICAO_CURTA.get(comp, comp)


def nome(n: str) -> str:
    return NOMES_EXIBICAO.get(n, n)


def cores_do_escudo(f: Path) -> tuple[str, str] | None:
    """(principal, segunda) a partir do escudo: as cores mais frequentes, sem o branco do fundo.
    Preferência a uma cor viva sobre o preto quando ela ocupa pelo menos um quinto do escudo."""
    try:
        from PIL import Image
    except ImportError:
        return None
    img = Image.open(f).convert("RGBA")
    img.thumbnail((48, 48))
    cont: dict[tuple[int, int, int], int] = {}
    for r, g, b, a in (img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata()):
        if a < 160:
            continue
        q = (r // 32 * 32 + 16, g // 32 * 32 + 16, b // 32 * 32 + 16)   # agrupa tons parecidos
        cont[q] = cont.get(q, 0) + 1
    if not cont:
        return None
    hexa = lambda c: "#%02x%02x%02x" % c
    branco = lambda c: min(c) > 205
    preto = lambda c: max(c) < 60
    viva = lambda c: max(c) - min(c) > 60
    ordem = sorted(cont, key=cont.get, reverse=True)
    total = sum(cont.values())
    sem_branco = [c for c in ordem if not branco(c)]
    if not sem_branco:
        return ("#f5f5f5", "#111111")
    principal = sem_branco[0]
    if preto(principal):
        vivas = [c for c in sem_branco if viva(c) and cont[c] >= total / 5]
        if vivas:
            principal = vivas[0]
    if preto(principal):            # escudo preto e branco: a segunda cor é o branco (é a que aparece no tema escuro)
        return "#111111", "#f5f5f5"
    if not viva(principal):         # cinza: vira branco ou preto
        return ("#f5f5f5", "#111111") if sum(principal) / 3 > 128 else ("#111111", "#f5f5f5")
    outras = [c for c in ordem if c != principal and (abs(c[0] - principal[0]) + abs(c[1] - principal[1]) + abs(c[2] - principal[2])) > 90]
    return hexa(principal), hexa(outras[0] if outras else (245, 245, 245))


def escudos(clubes: set[str]) -> dict[str, str]:
    """Escudo de cada clube em painel/escudos/ (até 160 px em WebP: nítido no pódio e leve); devolve clube -> caminho.
    Só regrava o arquivo que mudou (o git não vê diferença à toa)."""
    from baixar_escudos import arquivo
    from PIL import Image
    pasta = PAINEL / "escudos"
    pasta.mkdir(parents=True, exist_ok=True)
    saida = {}
    for c in sorted(clubes):
        f = arquivo(c)
        if not f.exists():
            continue
        img = Image.open(f).convert("RGBA")
        img.thumbnail((160, 160), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, "WEBP", quality=88, method=6)
        destino = pasta / (f.stem + ".webp")
        if not destino.exists() or destino.read_bytes() != buf.getvalue():
            destino.write_bytes(buf.getvalue())
        saida[c] = "escudos/" + destino.name
    for velho in set(pasta.glob("*.webp")) - {pasta / Path(x).name for x in saida.values()}:   # escudo que saiu (errado ou clube fora)
        velho.unlink()
    return saida


def participacoes(con: sqlite3.Connection) -> tuple[list[dict], dict[str, list[list[int]]]]:
    """Edições em ordem (ano, competição, nº de clubes, se foi de pontos corridos) e, por clube, [índice da edição, posição final]."""
    eds = con.execute("SELECT edicao_nacional_id, temporada_id, competicao_nome, moderna, temporada, pontos_vitoria, pontos_empate, pontos_derrota "
                      "FROM dim_edicao_nacional ORDER BY temporada_id, edicao_id").fetchall()
    idx = {eid: i for i, (eid, *_) in enumerate(eds)}
    lista = [{"ano": ano, "comp": rotulo_ed(con, comp), "n": 0, "pc": bool(pc), "t": temporada_texto(t), "pv": pv or 3}
             | ({"pe": pe} if pe != 1 else {}) | ({"pd": pd} if pd else {})
             for _, ano, comp, pc, t, pv, pe, pd in eds]
    part: dict[str, list[list[int]]] = {}
    for eid, clube, pos in con.execute(
        "SELECT f.edicao_nacional_id, cl.nome, f.posicao FROM fato_classificacao_final_nacional f JOIN dim_clube cl USING (clube_id)"
    ):
        lista[idx[eid]]["n"] += 1
        part.setdefault(nome(clube), []).append([idx[eid], pos])
    for v in part.values():
        v.sort()
    return lista, part


def gols(con: sqlite3.Connection) -> tuple[int, int]:
    """(jogos, gols) de todas as edições: partidas antigas (1937-2002) + Série A desde 2003."""
    j1, g1 = con.execute("SELECT count(*), sum(gols_mandante + gols_visitante) FROM fato_partida_nacional_historica").fetchone()
    j2, g2 = con.execute("SELECT count(*), sum(gols_mandante + gols_visitante) FROM fato_partida WHERE gols_mandante IS NOT NULL").fetchone()
    return j1 + j2, (g1 or 0) + (g2 or 0)


def campanhas(con: sqlite3.Connection) -> list[list]:
    """[clube, jogos, vitórias, empates, derrotas, gols marcados, gols sofridos] em todas as partidas, da mais vitoriosa à menos."""
    linhas = con.execute(
        """
        WITH p AS (
          SELECT mandante_id m, visitante_id v, gols_mandante gm, gols_visitante gv FROM fato_partida_nacional_historica
          UNION ALL
          SELECT mandante_id, visitante_id, gols_mandante, gols_visitante FROM fato_partida WHERE gols_mandante IS NOT NULL),
        t AS (SELECT m c, gm gp, gv gc FROM p UNION ALL SELECT v, gv, gm FROM p)
        SELECT cl.nome, count(*), sum(gp > gc), sum(gp = gc), sum(gp < gc), sum(gp), sum(gc)
        FROM t JOIN dim_clube cl ON cl.clube_id = t.c GROUP BY cl.clube_id
        """
    ).fetchall()
    # mais vitórias; empate: quem precisou de menos jogos; depois o nome
    return sorted(([nome(n), j, v, e, d, gp, gc] for n, j, v, e, d, gp, gc in linhas), key=lambda x: (-x[2], x[1], x[0]))


def corridas_jv(con: sqlite3.Connection) -> dict:
    """Jogos, vitórias, gols feitos e tomados de cada clube em cada edição, na ordem de `participacoes()`
    (a página acumula e calcula a posição)."""
    eds = [eid for (eid,) in con.execute("SELECT edicao_nacional_id FROM dim_edicao_nacional ORDER BY temporada_id, edicao_id")]
    idx = {eid: i for i, eid in enumerate(eds)}
    nomes = {cid: nome(nm) for cid, nm in con.execute("SELECT clube_id, nome FROM dim_clube")}
    # nas edições modernas (pontos corridos) as partidas vêm por temporada
    ed_do_ano = {ano: eid for eid, ano in con.execute("SELECT edicao_nacional_id, temporada_id FROM dim_edicao_nacional WHERE moderna")}
    partidas = list(con.execute("""SELECT h.edicao_nacional_id, h.mandante_id, h.visitante_id, h.gols_mandante, h.gols_visitante
                                   FROM fato_partida_nacional_historica h JOIN dim_fase_nacional_historica x USING (fase_nacional_id)
                                   WHERE x.fase_nome NOT LIKE 'Desempate%'"""))   # desempate fica fora da campanha da edição (IT-018)
    partidas += [(ed_do_ano[t], m, v, gm, gv) for t, m, v, gm, gv in con.execute(
        "SELECT temporada_id, mandante_id, visitante_id, gols_mandante, gols_visitante FROM fato_partida WHERE gols_mandante IS NOT NULL")]
    jogos = {c: [0] * len(eds) for c in nomes.values()}
    vits = {c: [0] * len(eds) for c in nomes.values()}
    emp = {c: [0] * len(eds) for c in nomes.values()}
    gp = {c: [0] * len(eds) for c in nomes.values()}
    gc = {c: [0] * len(eds) for c in nomes.values()}
    for eid, m, v, gm, gv in partidas:
        i = idx[eid]
        for clube, a, b in ((nomes[m], gm, gv), (nomes[v], gv, gm)):
            jogos[clube][i] += 1
            vits[clube][i] += a > b
            emp[clube][i] += a == b
            gp[clube][i] += a
            gc[clube][i] += b
    com_jogos = [c for c, xs in jogos.items() if any(xs)]
    return {k: {c: serie[c] for c in com_jogos} for k, serie in (("j", jogos), ("v", vits), ("e", emp), ("gp", gp), ("gc", gc))}


def curiosidades(con: sqlite3.Connection, ed: list[dict], edp: list[dict], part: dict, cjv: dict) -> dict:
    """Recordes e números curiosos em quatro grupos: jogos, clubes, campeões e edições.
    Campanhas (de clube ou de campeão) só com 20+ jogos: na Taça Brasil houve campeão com 4 partidas."""
    partidas = [(ano, nome(m), nome(v), gm, gv) for ano, m, v, gm, gv in con.execute(
        """
        SELECT h.temporada_id, m.nome, v.nome, h.gols_mandante, h.gols_visitante FROM fato_partida_nacional_historica h
        JOIN dim_clube m ON m.clube_id = h.mandante_id JOIN dim_clube v ON v.clube_id = h.visitante_id
        UNION ALL
        SELECT p.temporada_id, m.nome, v.nome, p.gols_mandante, p.gols_visitante FROM fato_partida p
        JOIN dim_clube m ON m.clube_id = p.mandante_id JOIN dim_clube v ON v.clube_id = p.visitante_id
        WHERE p.gols_mandante IS NOT NULL
        """)]
    jogo = lambda x: {"ano": x[0], "m": x[1], "v": x[2], "gm": x[3], "gv": x[4]}
    dif = lambda x: abs(x[3] - x[4])
    quatro = lambda t: dict(zip(("n", "c", "de", "ate"), t))
    n = len(partidas)

    # ---- jogos
    gol = sorted(partidas, key=lambda x: (-dif(x), -(x[3] + x[4]), x[0]))   # maior diferença; empate, mais gols
    goleada = {**jogo(gol[0]), "tb": [jogo(x) for x in gol[1:] if dif(x) == dif(gol[0])]}
    empates = [x for x in partidas if x[3] == x[4]]
    maior_empate = max(x[3] for x in empates)
    h2h: dict[tuple, list[int]] = defaultdict(lambda: [0, 0, 0])   # (a, b) em ordem: vitórias de a, empates, vitórias de b
    for _, m, v, a, b in partidas:
        k = tuple(sorted((m, v)))
        r = h2h[k]
        if a == b:
            r[1] += 1
        elif (a > b) == (m == k[0]):
            r[0] += 1
        else:
            r[2] += 1
    mais_jogado = max(sum(r) for r in h2h.values())
    limiar = min(30, mais_jogado // 2)   # freguesia: só confrontos com 30+ jogos (ou metade do mais jogado, se nenhum chegou a 30)
    _, (fa, fb), fr = max(((max(r[0], r[2]) / sum(r), k, r) for k, r in h2h.items() if sum(r) >= limiar), key=lambda t: t[0])
    jogos = {
        "goleada": goleada,
        "fora": jogo(max(partidas, key=lambda x: (x[4] - x[3], x[4], -x[0]))),
        "mais_gols": jogo(min(partidas, key=lambda x: (-(x[3] + x[4]), x[0]))),
        "empates": [jogo(x) for x in sorted(empates) if x[3] == maior_empate],
        "confrontos": [{"a": a, "b": b, "va": r[0], "e": r[1], "vb": r[2]} for (a, b), r in sorted(h2h.items()) if sum(r) == mais_jogado],
        "freguesia": {**({"a": fa, "b": fb, "v": fr[0], "e": fr[1], "d": fr[2]} if fr[0] >= fr[2] else {"a": fb, "b": fa, "v": fr[2], "e": fr[1], "d": fr[0]}), "min": limiar},
        "mando": [sum(a > b for *_, a, b in partidas) / n, sum(a == b for *_, a, b in partidas) / n, sum(a < b for *_, a, b in partidas) / n],
        "placar": [[a, b, q] for (a, b), q in Counter((a, b) for *_, a, b in partidas).items() if a <= 5 and b <= 5],
        "n": n,
    }

    # ---- clubes (campanhas de 20+ jogos numa edição)
    j, v, e_, gp, gc = cjv["j"], cjv["v"], cjv["e"], cjv["gp"], cjv["gc"]

    def pontos(i: int, jj: int, vv: int, ee: int) -> int:   # pontos da época (empate e derrota valem 1 e 0, salvo pe/pd)
        x = edp[i]
        return x["pv"] * vv + x.get("pe", 1) * ee + x.get("pd", 0) * (jj - vv - ee)

    def campanha(c: str, i: int) -> dict:
        jj, vv, ee = j[c][i], v[c][i], e_[c][i]
        return {"c": c, "ano": edp[i]["ano"], "t": edp[i]["t"], "j": jj, "v": vv, "e": ee, "d": jj - vv - ee, "gp": gp[c][i], "gc": gc[c][i],
                "pts": pontos(i, jj, vv, ee), "ap": pontos(i, jj, vv, ee) / (edp[i]["pv"] * jj)}

    maior = max(max(xs) for xs in j.values())   # mais jogos de um clube numa edição (na Série D, menos de 30)
    min_camp, min_def = min(20, maior // 2), min(30, maior)
    camps = [campanha(c, i) for c in j for i in range(len(edp)) if j[c][i] >= min_camp]
    anos_tit = defaultdict(list)
    for x in ed:
        for c in filter(None, (x["campeao"], x.get("co"))):   # título dividido (D-07) conta para os dois
            anos_tit[c].append(x["ano"])
    seguidas = (0, "", 0, 0)   # temporadas seguidas: anos em que a competição houve, sem faltar a nenhum
    anos_comp = sorted({x["ano"] for x in edp})
    k_ano = {a: k for k, a in enumerate(anos_comp)}
    for c, ps in part.items():
        ix = sorted({k_ano[edp[i]["ano"]] for i, _ in ps})
        ini = ix[0]
        for a, b in zip([None] + ix, ix):
            if a is None or b != a + 1:
                ini = b
            if b - ini + 1 > seguidas[0]:
                seguidas = (b - ini + 1, c, anos_comp[ini], anos_comp[b])
    ultimo: dict[int, int] = {}
    for ps in part.values():
        for i, pos in ps:
            ultimo[i] = max(ultimo.get(i, 0), pos)
    lanterna = Counter(c for c, ps in part.items() for i, pos in ps if pos == ultimo[i])
    mais_lant = max(lanterna.values())
    sem_tit = max((len(ps), c) for c, ps in part.items() if c not in anos_tit)
    clubes = {
        "seguidas": quatro(seguidas),
        "sem_titulo": {"n": sem_tit[0], "c": sem_tit[1]},
        "vit": max(camps, key=lambda x: (x["v"], -x["j"])),
        "gols": max(camps, key=lambda x: (x["gp"], -x["j"])),
        "saldo": max(camps, key=lambda x: x["gp"] - x["gc"]),
        "defesa": {**min((x for x in camps if x["j"] >= min_def), key=lambda x: x["gc"] / x["j"]), "min": min_def},
        "der": max(camps, key=lambda x: (x["d"], -x["j"])),
        "pior": min(camps, key=lambda x: x["ap"]),
        "lanterna": {"n": mais_lant, "c": sorted(c for c, q in lanterna.items() if q == mais_lant)},
        "volta": quatro(max((edp[b]["ano"] - edp[a]["ano"], c, edp[a]["ano"], edp[b]["ano"])
                            for c, ps in part.items() for (a, _), (b, _) in zip(ps, ps[1:]))),
        "uma_vez": sum(len(ps) == 1 for ps in part.values()),
    }

    # ---- campeões
    seq, i = (0, "", 0, 0), 0
    while i < len(ed):
        k = i
        while ed[i]["campeao"] and k + 1 < len(ed) and ed[k + 1]["campeao"] == ed[i]["campeao"]:
            k += 1
        if k - i + 1 > seq[0]:
            seq = (k - i + 1, ed[i]["campeao"], ed[i]["ano"], ed[k]["ano"])
        i = k + 1
    camp = [campanha(x["campeao"], i) for i, x in enumerate(ed) if x["campeao"] in j and j[x["campeao"]][i] >= min_camp]
    pc = []   # pontos corridos: pontos do campeão e vantagem sobre o vice
    for i, x in enumerate(ed):
        if edp[i]["pc"] and x["campeao"] and x.get("vice") and x["campeao"] in j and j[x["campeao"]][i]:   # edição sem jogos fica de fora
            k, vc = campanha(x["campeao"], i), x["vice"]
            pc.append({**k, "vice": vc, "vant": k["pts"] - pontos(i, j[vc][i], v[vc][i], e_[vc][i]), "n": edp[i]["n"]})
    menor_vant = min((x["vant"] for x in pc), default=0)
    pc20 = [x for x in pc if x["n"] == 20]
    vices = Counter(x["vice"] for x in ed if x.get("vice"))
    uf = {nome(nm): u for nm, u in con.execute("SELECT nome, uf FROM dim_clube")}
    por_uf: dict[str, Counter] = defaultdict(Counter)
    decadas: dict[int, set] = defaultdict(set)
    for x in ed:
        for c in filter(None, (x["campeao"], x.get("co"))):   # título dividido (D-07) conta para os dois
            if uf.get(c):   # clube sem estado (liga estrangeira) fica de fora (ES-010, EN-012)
                por_uf[uf[c]][c] += 1
            decadas[x["ano"] // 10 * 10].add(c)
    campeoes = {
        "seq": quatro(seq),
        "jejum": quatro(max((b - a, c, a, b) for c, xs in anos_tit.items() for a, b in zip(xs, xs[1:]))),
        "invictos": [campanha(x["campeao"], i) for i, x in enumerate(ed) if x["campeao"] in j and j[x["campeao"]][i] >= 10
                     and campanha(x["campeao"], i)["d"] == 0],
        "melhor": max(camp, key=lambda x: x["ap"]), "pior": min(camp, key=lambda x: x["ap"]),
        "pontos": max(pc, key=lambda x: x["pts"], default=None),
        "pontos20": max(pc20, key=lambda x: x["pts"], default=None),
        "pc_desde": pc[0]["ano"] if pc else None, "pc20_desde": pc20[0]["ano"] if pc20 else None,
        "vantagem": max(pc, key=lambda x: x["vant"], default=None),
        "apertados": [x for x in pc if x["vant"] == menor_vant],
        "vices_sem": sorted(([c, q] for c, q in vices.items() if c not in anos_tit), key=lambda x: (-x[1], x[0])),
        "uf": sorted(([u, sum(q.values()), sorted(q.items(), key=lambda t: (-t[1], t[0]))] for u, q in por_uf.items()), key=lambda x: -x[1]),
        "decadas": [[d, len(cs), [[c, 1] for c in sorted(cs)]] for d, cs in sorted(decadas.items())],
    }

    # ---- edições
    por_ed = [{"ano": x["ano"], "t": x["t"], "comp": x["comp"], "n": x["n"], "j": sum(j[c][i] for c in j) // 2, "g": sum(gp[c][i] for c in gp)}
              for i, x in enumerate(edp)]
    estreias = Counter(ps[0][0] for ps in part.values())
    i_est = max(estreias, key=lambda i: (estreias[i], -i))
    edicoes = {
        "mais_clubes": max(por_ed, key=lambda x: x["n"]), "menos_clubes": min(por_ed, key=lambda x: x["n"]),
        "mais_jogos": max(por_ed, key=lambda x: x["j"]), "menos_jogos": min((x for x in por_ed if x["j"]), key=lambda x: x["j"]),   # edição só com a tabela final não conta
        "mais_gols": max(por_ed, key=lambda x: x["g"]),
        "duplos": [[a, [x["campeao"] for x in ed if x["ano"] == a and x["campeao"]]] for a, q in sorted(Counter(x["ano"] for x in ed).items()) if q > 1],
        "formatos": [[c or con.execute("SELECT padrao FROM rotulo").fetchone()[0], q] for c, q in Counter(x["comp"] for x in edp).most_common()],
        "estreantes": {**por_ed[i_est], "est": estreias[i_est]},
        "por_ed": por_ed,
    }
    return {"jogos": jogos, "clubes": clubes, "campeoes": campeoes, "edicoes": edicoes}


def edicoes_detalhe(con: sqlite3.Connection, edp: list[dict], part: dict, cjv: dict) -> list[dict]:
    """Por edição, na ordem de `participacoes()`: chave (vai no endereço), nome, pontos por vitória, números
    (estreantes, jogos, gols, maior goleada), classificação final [clube, posição, J, V, E, D, GP, GC],
    fases, jogos [grupo, mandante, visitante, gols, gols, subgrupo] (clubes pelo índice na classificação;
    grupo = rodada desde 2003 ou fase antes) e, desde 2003, a corrida rodada a rodada e os artilheiros."""
    nome_of = {eid: n for eid, n in con.execute("SELECT edicao_nacional_id, nome_oficial FROM dim_edicao_nacional")}
    eds = con.execute("SELECT edicao_nacional_id, edicao_id, competicao_nome, tipo, pontos_vitoria, temporada_id, moderna FROM dim_edicao_nacional "
                      "ORDER BY temporada_id, edicao_id").fetchall()
    idx = {eid: i for i, (eid, *_) in enumerate(eds)}
    nomes = {cid: nome(nm) for cid, nm in con.execute("SELECT clube_id, nome FROM dim_clube")}
    # jogos antigos: por fase (e grupo); desde 2003: por rodada
    fases = defaultdict(list)   # edição -> [(ordem, nome, tipo, formato, grupos, id)]
    for fid, eid, ordem, fn, ft, ng, fs in con.execute(
            "SELECT fase_nacional_id, edicao_nacional_id, fase_ordem, fase_nome, fase_tipo, num_grupos, formato_serie FROM dim_fase_nacional_historica"):
        fases[idx[eid]].append((ordem, fn, ft, fs, ng, fid))
    jogos = defaultdict(list)   # edição -> [(chave de ordem, grupo, m, v, gm, gv, subgrupo)]
    # edição de pontos corridos: os desempates vêm depois das rodadas (grupo = nº de rodadas + ordem da fase)
    ult_rod = dict(con.execute("SELECT temporada_id, max(rodada) FROM fato_classificacao_rodada GROUP BY 1"))
    desloc = {idx[eid]: ult_rod.get(ano, 0) for eid, _, _, _, _, ano, moderna in eds if moderna}
    ordem_fase = {f[5]: (i, k + desloc.get(i, 0)) for i, fs in fases.items() for k, f in enumerate(sorted(fs))}
    extra = defaultdict(set)   # edição -> grupos que são desempate (fora da tabela, da corrida e das contas da edição)
    for i, fs in fases.items():
        for k, f in enumerate(sorted(fs)):
            if f[1].startswith("Desempate"):
                extra[i].add(k + desloc.get(i, 0))
    pen: dict[tuple, str] = {}   # (edição, ordem, m, v, gm, gv, grupo) -> "4-3" (pênaltis, do ponto de vista do mandante)
    for fid, m, v, gm, gv, grupo, data, jogo, pm, pv_ in con.execute(
            """SELECT fase_nacional_id, mandante_id, visitante_id, gols_mandante, gols_visitante, grupo, data, jogo,
                      penaltis_mandante, penaltis_visitante FROM fato_partida_nacional_historica"""):
        i, k = ordem_fase[fid]
        x = ((k, str(grupo or ""), data or "", jogo or 0), k, nomes[m], nomes[v], gm, gv, str(grupo or ""))
        jogos[i].append(x)
        if pm is not None and pv_ is not None:
            pen[(i, x[0])] = f"{pm}-{pv_}"
    ed_do_ano = {ano: idx[eid] for eid, _, _, _, _, ano, moderna in eds if moderna}
    for t, r, m, v, gm, gv, data in con.execute(
            "SELECT temporada_id, rodada, mandante_id, visitante_id, gols_mandante, gols_visitante, data FROM fato_partida WHERE gols_mandante IS NOT NULL"):
        jogos[ed_do_ano[t]].append(((r, data or ""), r - 1, nomes[m], nomes[v], gm, gv, ""))
    # corrida rodada a rodada e faixas da tabela (zona de cada posição na última rodada)
    rodadas = defaultdict(lambda: defaultdict(dict))   # edição -> clube -> rodada -> (posição, pontos)
    zona_final: dict[int, dict[int, str]] = defaultdict(dict)
    ultima = dict(con.execute("SELECT temporada_id, max(rodada) FROM fato_classificacao_rodada GROUP BY 1"))
    for t, r, c, pos, pts, zona in con.execute("SELECT temporada_id, rodada, clube_id, posicao, pontos, zona FROM fato_classificacao_rodada"):
        rodadas[ed_do_ano[t]][nomes[c]][r] = (pos, pts)
        if r == ultima[t]:
            zona_final[ed_do_ano[t]][pos] = zona or "meio"
    artilheiros = defaultdict(list)
    for eid, jog, c, n in con.execute(
            "SELECT edicao_nacional_id, jogador, clube_id, count(*) FROM fato_gol WHERE coalesce(tipo, '') <> 'contra' GROUP BY 1, 2, 3"):
        artilheiros[idx[eid]].append([jog, nomes[c], n])
    goleada: dict[int, tuple] = {}   # maior diferença; empate, mais gols
    for i, js in jogos.items():
        for _, _, m, v, a, b, _ in js:
            k = (abs(a - b), a + b)
            if i not in goleada or k > goleada[i][0]:
                goleada[i] = (k, {"m": m, "v": v, "gm": a, "gv": b})
    estreia = Counter(ps[0][0] for ps in part.values())
    j, v, e_, gp, gc = cjv["j"], cjv["v"], cjv["e"], cjv["gp"], cjv["gc"]
    publicada = {(idx[eid], nomes[c]): x for eid, c, *x in con.execute(
        "SELECT edicao_nacional_id, clube_id, jogos, vitorias, empates, derrotas, gols_pro, gols_contra FROM fato_classificacao_final_nacional")}
    pontos_pub = {(idx[eid], nomes[c]): pt for eid, c, pt in con.execute(
        "SELECT edicao_nacional_id, clube_id, pontos FROM fato_classificacao_final_nacional WHERE pontos IS NOT NULL")}
    ajuste = {(idx[eid], nomes[c]): aj for eid, c, aj in con.execute(
        "SELECT edicao_nacional_id, clube_id, ajuste_pontos FROM fato_classificacao_final_nacional WHERE ajuste_pontos <> 0")}
    oficiais = defaultdict(list)   # artilheiros da lista oficial (a tabela artilheiro do banco)
    for eid, jog, c, n in con.execute("SELECT edicao_nacional_id, jogador, clube_id, gols FROM fato_artilheiro ORDER BY gols DESC, jogador"):
        oficiais[idx[eid]].append([jog, nomes.get(c, "") if c else "", n])
    (tipo_comp,) = con.execute("SELECT tipo FROM rotulo").fetchone()
    # quem subiu, quando a fonte diz (situação acesso/campeão): sem isso, o painel deduz pela divisão do ano seguinte
    subiu = defaultdict(set)
    tem_acesso = False
    for eid, c, sit in con.execute("SELECT edicao_nacional_id, clube_id, situacao FROM fato_classificacao_final_nacional"):
        tem_acesso |= sit == "acesso"
        if sit in ("acesso", "campeao"):
            subiu[idx[eid]].add(nomes[c])
    sem_tit = {idx[eid]: obs or "título não atribuído" for eid, tem, obs in con.execute(
        "SELECT edicao_nacional_id, tem_campeao, observacao FROM dim_edicao_nacional") if not tem}
    nao_oficial = {idx[eid]: nota_nao_oficial(obs) for eid, obs in con.execute(
        "SELECT edicao_nacional_id, observacao FROM dim_edicao_nacional WHERE NOT oficial")}   # D-10
    # edição com só parte dos jogos: a tabela é a da fonte (como nas edições sem jogos), não a soma dos jogos que temos
    incompletas = {idx[eid] for eid, inc in con.execute("SELECT edicao_nacional_id, incompleta FROM dim_edicao_nacional") if inc}
    fechados = Counter()   # linhas em que o ajuste foi refeito para dar os pontos oficiais
    comp_slug = "pontos oficiais"
    co_ed = {idx[eid]: nome(c) for eid, c in con.execute("SELECT edicao_nacional_id, co_campeao FROM dim_edicao_nacional WHERE co_campeao IS NOT NULL")}   # D-07
    saida = []
    for i, (_, chave, comp, tipo, pv, ano, _) in enumerate(eds):
        do_i = [c for c, ps in part.items() for k, _ in ps if k == i]
        da_fonte = True   # a tabela vem da fonte (linhas sem números ficam parciais), não da soma dos jogos
        if i in incompletas:
            tab = sorted(([c, pos, *[n or 0 for n in publicada.get((i, c), [0] * 6)]] for c, ps in part.items() for k, pos in ps if k == i),
                         key=lambda r: r[1])
        elif jogos[i] and do_i and any(publicada.get((i, c), [None])[0] is not None for c in do_i):
            # (com "any": edição com só parte dos jogos em que a fonte publica a tabela de quase todos, ex.: Bolívia 1978)
            # o pacote traz a tabela oficial (pontos de W.O. sem os gols, jogos anulados etc.): vale ela
            tab = sorted(([c, pos, *[n or 0 for n in publicada.get((i, c), [0] * 6)]] for c, ps in part.items() for k, pos in ps if k == i), key=lambda r: r[1])
        elif jogos[i]:
            da_fonte = False
            q = lambda d, c: d[c][i] if c in d else 0   # clube só com jogos sem placar (W.O.) não está nas somas
            tab = sorted(([c, pos, q(j, c), q(v, c), q(e_, c), q(j, c) - q(v, c) - q(e_, c), q(gp, c), q(gc, c)]
                          for c, ps in part.items() for k, pos in ps if k == i), key=lambda r: r[1])
        else:   # sem jogos no banco: a tabela como a fonte publicou (os jogos já contam nas edições de onde ela sai)
            tab = sorted(([c, pos, *[n or 0 for n in publicada.get((i, c), [0] * 6)]] for c, ps in part.items() for k, pos in ps if k == i),
                         key=lambda r: r[1])
        for r in tab:
            r.append(ajuste.get((i, r[0]), 0))   # r[8]: pontos ganhos ou perdidos no tribunal
        pe, pd = edp[i].get("pe", 1), edp[i].get("pd", 0)
        if da_fonte and pv:   # tabela da fonte com pontos oficiais (ponto por gol, shootout, 3-2-1): o ajuste fecha a conta
            for r in tab:
                pp = pontos_pub.get((i, r[0]))
                if pp is not None and (publicada.get((i, r[0])) or [None])[0] is not None:
                    conta = pv * r[3] + pe * r[4] + pd * r[5]
                    if conta + r[8] != pp:
                        r[8] = pp - conta
                        fechados[comp_slug] += 1
        if da_fonte:   # tabela parcial da fonte (só posição e pontos, ou só campeão e vice): r[9] pontos publicados, r[10] = 1
            for r in tab:
                if (publicada.get((i, r[0])) or [None])[0] is None:
                    r += [pontos_pub.get((i, r[0])), 1]
        ci = {r[0]: k for k, r in enumerate(tab)}
        xj = sorted(x for x in jogos[i] if x[1] in extra[i])   # desempates: só na aba Jogos
        jogos[i] = [x for x in jogos[i] if x[1] not in extra[i]]
        fora = sorted({x for _, _, m, vv, *_ in jogos[i] for x in (m, vv)} - ci.keys())
        if fora:   # jogou e não está na classificação final do pacote: entra no fim, sem posição nem números
            print(f"  aviso: {chave}: clubes com jogos e fora da classificação final: {', '.join(fora)}")
            for c in fora:
                ci[c] = len(tab)
                tab.append([c, None, 0, 0, 0, 0, 0, 0, 0, None, 1])
        js = sorted(jogos[i])
        if i in rodadas:
            n_rod = max(max(rs) for rs in rodadas[i].values())
            grupos = [f"Rodada {r}" for r in range(1, n_rod + 1)] + [f[1] for f in sorted(fases[i])]   # + desempates
            disputa = [["Pontos corridos", "liga", "pontos_corridos", 1, len(js), len(tab)]]
            for k, (_, fn, ft, fsr, ng, _) in enumerate(sorted(fases[i])):
                jk = [x for x in xj if x[1] == n_rod + k]
                disputa.append([fn, ft, fsr, ng or 1, len(jk), len({x[2] for x in jk} | {x[3] for x in jk})])
            cl = sorted(rodadas[i], key=lambda c: ci[c])
            zf = zona_final[i]
            faixas = []   # posições seguidas na mesma zona (o meio da tabela fica sem faixa)
            for pos in sorted(zf):
                if zf[pos] == "meio":
                    continue
                if faixas and faixas[-1][2] == zf[pos] and faixas[-1][1] == pos - 1:
                    faixas[-1][1] = pos
                else:
                    faixas.append([pos, pos, zf[pos]])
            corrida = {"pos": [[rodadas[i][c].get(r, (999, 0))[0] for r in range(1, n_rod + 1)] for c in cl],
                       "pts": [[rodadas[i][c].get(r, (999, 0))[1] for r in range(1, n_rod + 1)] for c in cl],
                       "cl": [ci[c] for c in cl], "faixas": faixas}
        else:
            fs = sorted(fases[i])
            grupos = [f[1] for f in fs]
            disputa = []
            for k, (_, fn, ft, fsr, ng, _) in enumerate(fs):
                jk = [x for x in js + xj if x[1] == k]
                disputa.append([fn, ft, fsr, ng or 1, len(jk), len({x[2] for x in jk} | {x[3] for x in jk})])
            corrida = None
        nof = nome_of.get(eds[i][0])   # nome oficial da época ("Premier League", "First Division"), quando não tem o ano no meio (EN-015)
        saida.append({"id": chave, "ano": edp[i]["ano"], "t": edp[i]["t"], "nome": nof if nof and not any(ch.isdigit() for ch in nof) else comp, "mata": tipo == "mata" or tipo_comp == "copa",
                      "pv": pv, "nota": notas(con).get(chave, "") or nao_oficial.get(i) or ("" if sem_tit.get(i) is None else "Sem campeão: " + sem_tit[i] + "."), "est": estreia.get(i, 0), "j": len(js) + len(xj),
                      "g": sum(x[4] + x[5] for x in js + xj), "gol": goleada.get(i, (None, None))[1], "tab": tab,
                      "grupos": grupos, "disputa": disputa, "jogos": [[g, ci[m], ci[vv], a, b, sg] + ([pen[(i, o)]] if (i, o) in pen else []) for o, g, m, vv, a, b, sg in js],
                      "cor": corrida, "art": sorted(artilheiros[i], key=lambda x: (-x[2], x[0]))[:10], "artof": oficiais[i][:10], "ac": sorted(subiu[i]) if tem_acesso else None,
                      "cob": round(sum(x[2] for x in artilheiros[i]) / max(1, sum(x[4] + x[5] for x in js)), 2)}
                     | ({"inc": 1} if i in incompletas else {}) | ({"co": co_ed[i]} if i in co_ed else {})
                     | ({"pe": pe} if pe != 1 else {}) | ({"pd": pd} if pd else {})
                     | ({"xj": [[g, m, vv, a, b, sg] + ([pen[(i, o)]] if (i, o) in pen else []) for o, g, m, vv, a, b, sg in xj]} if xj else {}))
    if fechados:
        print(f"  pontos oficiais da fonte no lugar da conta: {fechados[comp_slug]} linhas")
    return saida


def artilharia_clubes(con: sqlite3.Connection, todos: bool = False) -> dict[str, list]:
    """Os 10 maiores artilheiros de cada clube desde 2003: [jogador, gols, primeiro ano, último ano]."""
    por: dict[str, list] = defaultdict(list)
    for c, jog, n, a1, a2 in con.execute(
            """SELECT cl.nome, g.jogador, count(*), min(g.temporada_id), max(g.temporada_id) FROM fato_gol g
               JOIN dim_clube cl ON cl.clube_id = g.clube_id WHERE coalesce(g.tipo, '') <> 'contra' GROUP BY 1, 2"""):
        por[nome(c)].append([jog, n, a1, a2])
    return {c: sorted(xs, key=lambda x: (-x[1], x[0]))[:None if todos else 10] for c, xs in por.items()}


def milhar(n: float, casas: int = 0) -> str:
    return f"{n:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def controles_corrida(id_: str, rotulo: str) -> str:
    """Play, barra do tempo, ano, Top 20 | Todos e o gráfico de uma corrida de posições."""
    return (f'<div class="corrida-ctl" style="margin-top:14px"><button id="{id_}-play" type="button">▶ Ver a corrida</button>'
            f'<input id="{id_}-ano" type="range" min="0" step="0.01" aria-label="Ano"><output id="{id_}-saida"></output>'
            f'<div class="alterna" id="{id_}-quantos" role="group" aria-label="Clubes"><button type="button" data-q="top" class="ativo">Top 20</button>'
            f'<button type="button" data-q="todos">Todos</button></div></div>'
            f'<div class="corrida-rolar"><svg id="{id_}" class="grafico-corrida" role="img" aria-label="{rotulo}"></svg></div>')


def cartoes(eds: list[dict], edp: list[dict], part: dict, jogos: int, total_gols: int, com_jogos: int = 0) -> str:
    """Números do cabeçalho: edições, campeões, vices, terceiros, clubes participantes, jogos e gols."""
    dif = lambda k: len({e[k] for e in eds if e.get(k)})
    com_jogos = com_jogos or len(eds)
    itens = [
        (milhar(len(eds)), "Edições", f"de {eds[0].get('t') or eds[0]['ano']} a {eds[-1].get('t') or eds[-1]['ano']}"),
        (len({c for e in eds for c in (e.get("campeao"), e.get("co")) if c}), "Campeões", "clubes diferentes"),
        (dif("vice"), "Vices", "clubes diferentes"),
        (dif("terceiro"), "Terceiros", "clubes diferentes"),
        (milhar(len(part)), "Participantes", "clubes diferentes"),
        (milhar(jogos), "Jogos", f"em {com_jogos} edições" + ("" if com_jogos == len(eds) else " com jogos")),
        (milhar(total_gols), "Gols", f"{milhar(total_gols / jogos, 2)} por jogo"),
    ]
    return '<div class="cartoes-topo">' + "".join(
        f'<div class="kpi"><b>{v}</b><span>{rot}</span><small>{sub}</small></div>' for v, rot, sub in itens) + "</div>"


def movimentos(dados: dict) -> None:
    """Em cada edição, de onde cada clube chegou e para onde foi: a divisão (nível) dele no ano anterior e no
    seguinte, olhando todas as ligas do banco do mesmo país. Põe em EDS[i]["mv"] um [veio, foi] por linha da
    classificação: o nível, 0 se não jogou nenhuma delas naquele ano e null se o banco não tem aquele ano.
    Numa copa (sem nível) é [divisão no próprio ano, null]."""
    con = sqlite3.connect(DB)
    try:
        nivel = {slug: n for slug, n in con.execute("SELECT slug, nivel FROM competicao")}
        # sistema de divisões: as ligas nacionais do país, ou as divisões do estadual do mesmo estado (copa usa as ligas)
        sistema = {slug: (p_, "estadual", r) if t == "estadual" else (p_, "liga", None)
                   for slug, p_, t, r in con.execute("SELECT slug, pais_id, tipo, regiao FROM competicao")}
        onde: dict[tuple, int] = {}   # (sistema, clube, ano) -> menor nível jogado
        anos: dict[tuple, set] = defaultdict(set)   # sistema -> anos com alguma divisão no banco
        for p_, t, r, c, ano, n in con.execute("""SELECT k.pais_id, k.tipo, k.regiao, cl.nome, e.ano_inicio, k.nivel FROM classificacao_final f
                                                  JOIN edicao e USING (edicao_id) JOIN competicao k USING (competicao_id)
                                                  JOIN clube cl USING (clube_id) WHERE k.tipo IN ('liga', 'estadual') AND k.nivel IS NOT NULL"""):
            sis = (p_, t, r if t == "estadual" else None)
            k = (sis, nome(c), ano)
            onde[k] = min(onde.get(k, n), n)
            anos[sis].add(ano)
    finally:
        con.close()
    for slug, d in dados.items():
        sis = sistema[slug]
        d["CONF"]["nivel"] = nivel[slug]
        for e in d["EDS"]:
            ano = e["ano"]
            lado = lambda a, c: onde.get((sis, c, a), 0) if a in anos[sis] else None
            ant = max((a for a in anos[sis] if a < ano), default=None)   # a temporada anterior que houve (guerras, paradas)
            seg = min((a for a in anos[sis] if a > ano), default=None)
            if nivel[slug] is None:
                e["mv"] = [[lado(ano, r[0]), None] for r in e["tab"]]
            else:
                e["mv"] = [[lado(ant, r[0]) if ant else None, lado(seg, r[0]) if seg else None] for r in e["tab"]]


def textos(slug: str, eds: list[dict], edp: list[dict], part: dict, jogos: int, total_gols: int, det: list[dict], artc: dict) -> tuple[dict, dict]:
    """(trechos de HTML que a página põe nos [data-t], valores que o JavaScript usa nos textos) da competição."""
    c = COMPETICOES[slug]
    ano0 = edp[0]["ano"]
    pc = [e["ano"] for e in edp if e["pc"]]
    art = [e["ano"] for e in det if e["art"]]
    zonas = {f[2] for e in det if e["cor"] for f in e["cor"]["faixas"]}
    nomes_zona = [("titulo", "#f5c518", "título"), ("libertadores", "var(--accent)", "Libertadores"), ("acesso", "var(--accent)", "acesso"),
                  ("sula", "#4aa3df", "Sul-Americana"), ("rebaixamento", "#ef4444", "rebaixamento")]
    tx = {
        "marca": c["curto"],
        "selo": f"{c['nome']} · {ano0} a hoje",
        "h1": f"História {c['do']} — Clube Analítico",
        "cartoes": cartoes(eds, edp, part, jogos, total_gols, sum(1 for e in det if e["j"])),
        "pt-info": f"{len(edp)} edições, de {ano0} a hoje · passe o mouse para ver a posição final",
        "jv-info": f"barra do tamanho dos jogos · todas as partidas, de {ano0} a hoje ({milhar(jogos)} jogos)",
        "gl-info": f"barra com todos os gols dos jogos do clube · {milhar(total_gols)} gols, de {ano0} a hoje",
        "cpc-sem": (f"A tabela rodada a rodada existe nas edições de pontos corridos, de {pc[0]} em diante. Escolha uma delas." if pc
                    else "Nenhuma edição tem a tabela rodada a rodada."),
        "cpc-legenda": "".join(f'<span><i style="background:{cor}"></i>{rot}</span>' for z, cor, rot in nomes_zona if z in zonas),
        "cpa-sem": "Sem gols por jogador registrados nesta edição.",
        "cla-sem": "Sem gols por jogador registrados para este clube.",
    }
    conf = {"curto": c["curto"], "o": c["o"], "art": art[0] if art else None,
            "tipo": sqlite3.connect(DB).execute("SELECT tipo FROM competicao WHERE slug = ?", (slug,)).fetchone()[0],
            "niveis": {n: x for n, x in sqlite3.connect(DB).execute(
                """SELECT nivel, nome_curto FROM competicao k WHERE nivel IS NOT NULL AND EXISTS (SELECT 1 FROM competicao x WHERE x.slug = ?
                   AND x.pais_id = k.pais_id AND (CASE WHEN x.tipo = 'estadual' THEN k.tipo = 'estadual' AND k.regiao = x.regiao ELSE k.tipo = 'liga' END))""",
                (slug,))}}
    return tx, conf


def cores_auto(clubes: set[str]) -> dict[str, list[str]]:
    """Cor dos clubes que não estão em CORES, tirada do escudo (quem não tem escudo fica com o verde do tema)."""
    from baixar_escudos import arquivo
    saida = {}
    for c in sorted(clubes - set(CORES)):
        f = arquivo(c)
        par = cores_do_escudo(f) if f.exists() else None
        if par:
            saida[c] = list(par)
    return saida


def nota_nao_oficial(obs: str | None) -> str:
    """Aviso da edição não oficial (D-10): a observação do pacote já começa por "edição não oficial: ..."."""
    t = (obs or "").strip()
    return (t[0].upper() + t[1:] if t.lower().startswith("edição não oficial") else "Edição não oficial: " + (t or "não conta título")).rstrip(".") + "."


def campeoes(con: sqlite3.Connection) -> list[dict]:
    """Uma linha por edição: ano, competição, campeão, vice e 3º colocado."""
    linhas = con.execute(
        """
        SELECT e.temporada_id, e.edicao_id, e.competicao_nome, f.posicao, cl.nome, e.temporada, e.tem_campeao, e.observacao, e.co_campeao, e.oficial
        FROM fato_classificacao_final_nacional f
        JOIN dim_edicao_nacional e USING (edicao_nacional_id)
        JOIN dim_clube cl USING (clube_id)
        WHERE f.posicao <= 4
        ORDER BY e.temporada_id, e.edicao_id, f.posicao
        """
    ).fetchall()
    edicoes: dict[str, dict] = {}
    for ano, edicao, comp, pos, clube, temporada, tem_campeao, obs, co, oficial in linhas:
        e = edicoes.setdefault(edicao, {"ano": ano, "t": temporada_texto(temporada), "comp": rotulo_ed(con, comp),
                                        "nota": notas(con).get(edicao, "") or ("" if tem_campeao else "Sem campeão: " + (obs or "título não atribuído") + ".")})
        if not oficial:   # edição não oficial (D-10): fica fora do Pódio, da Corrida e das contagens de títulos
            e.update({"campeao": None, "nof": 1, "nota": nota_nao_oficial(obs)})
            continue
        if co:   # título dividido (D-07): o outro campeão não é vice; quem vem depois dele sobe uma posição
            e["co"] = nome(co)
            if clube == co:
                e["_pula"] = 1
                continue
            pos -= e.get("_pula", 0)
        if pos <= 3:
            e[{1: "campeao", 2: "vice", 3: "terceiro"}[pos]] = nome(clube) if pos > 1 or tem_campeao else None   # título tirado ou não disputado
    for e in edicoes.values():
        e.pop("_pula", None)
    return list(edicoes.values())


CSS = """
:root[data-theme="dark"]{
  --bg:#06100b; --panel:#0e1b14; --panel-2:#132519; --border:#2e4d39; --pitch-line:rgba(241,255,245,.10);
  --text:#f1f7f1; --muted:#9bb6a7; --accent:#1ecb74; --champ:#fbbf24; --trilho:#11241a;
  --header-text:#f8fff8; --header-muted:#b9d3c2; --shadow-sm:0 8px 22px rgba(0,0,0,.28);
}
:root[data-theme="light"]{
  --bg:#eef5eb; --panel:#ffffff; --panel-2:#f6faf3; --border:#cfdcc9; --pitch-line:rgba(20,80,40,.08);
  --text:#15241c; --muted:#5b7568; --accent:#087c43; --champ:#b46f00; --trilho:#eef4ea;
  --header-text:#f7fff7; --header-muted:#c5ddcf; --shadow-sm:0 8px 22px rgba(20,60,30,.10);
}
*{box-sizing:border-box}
html,body{margin:0;font-family:'Inter','SF Pro Text',-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.5}
body{background-image:repeating-linear-gradient(90deg,transparent 0 90px,rgba(255,255,255,.012) 90px 180px)}
/* cabeçalho: placar sobre o gramado, com a faixa verde-amarela embaixo */
.topo{position:relative;overflow:hidden;padding:26px 28px 22px;color:var(--header-text);
  background:radial-gradient(circle at 50% 120%,rgba(30,203,116,.18),transparent 55%),linear-gradient(180deg,#0d2a19,#06140c);
  border-bottom:4px solid transparent;border-image:repeating-linear-gradient(90deg,#1ecb74 0 40px,#fbbf24 40px 52px,#1ecb74 52px 92px) 1}
.topo::before{content:"";position:absolute;left:50%;top:-40px;width:180px;height:180px;margin-left:-90px;border:2px solid var(--pitch-line);border-radius:50%}
.topo::after{content:"";position:absolute;left:50%;top:0;bottom:0;border-left:2px solid var(--pitch-line)}
.topo .selo{display:inline-block;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;padding:5px 10px;border-radius:6px;
  border:1.5px solid #1ecb74;color:#eafff2;background:rgba(5,11,8,.55)}
.topo h1{position:relative;z-index:1;margin:12px 0 2px;font-size:28px;font-weight:900;letter-spacing:.01em;text-transform:uppercase}
.topo p{position:relative;z-index:1;margin:0;color:var(--header-muted);font-size:13px;font-weight:600}
.tema{position:absolute;z-index:2;right:24px;top:24px;font-family:inherit;font-size:13px;font-weight:600;color:var(--header-text);background:rgba(5,11,8,.55);
  border:1px solid rgba(255,255,255,.18);border-radius:8px;padding:7px 12px;cursor:pointer}
/* cartões do cabeçalho (como os do dashboard antigo: número, rótulo e a faixa verde-amarela na lateral) */
.cartoes-topo{position:relative;z-index:1;display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:12px;margin-top:18px}
.kpi{position:relative;overflow:hidden;background:linear-gradient(135deg,rgba(14,27,20,.92),rgba(5,11,8,.88));border:1px solid #2e4d39;border-radius:10px;padding:12px 14px 12px 18px}
.kpi::before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;background:repeating-linear-gradient(180deg,#1ecb74 0 14px,#fbbf24 14px 20px)}
.kpi b{display:block;font-size:26px;font-weight:900;line-height:1.1;color:#1ecb74;font-variant-numeric:tabular-nums}
.kpi span{display:block;margin-top:4px;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#eafff2}
.kpi small{display:block;font-size:11.5px;color:#b9d3c2;line-height:1.3}
@media (max-width:1000px){.cartoes-topo{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media (max-width:640px){.cartoes-topo{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}.kpi{padding:9px 7px 9px 12px}
  .kpi b{font-size:18px}.kpi span{font-size:9.5px;letter-spacing:.03em}.kpi small{font-size:10px}}
/* barra de navegação lateral (no celular vira uma faixa no topo) */
.lateral{position:fixed;left:0;top:0;bottom:0;width:224px;z-index:20;display:flex;flex-direction:column;gap:6px;padding:20px 14px;
  background:linear-gradient(180deg,#0b2215,#050b08);border-right:1px solid #2e4d39}
.lateral .marca{display:flex;align-items:center;gap:8px;margin:0 6px 18px;font-size:15px;font-weight:900;letter-spacing:.04em;text-transform:uppercase;color:#f8fff8}
.comp-escolha{margin:0 2px 14px}
.comp-btn{display:flex;align-items:center;gap:10px;width:100%;font-family:inherit;text-align:left;color:#f8fff8;cursor:pointer;
  background:rgba(5,11,8,.55);border:1px solid #2e4d39;border-radius:10px;padding:8px 10px}
.comp-btn:hover{border-color:var(--accent)}
.comp-btn .cb-txt{display:flex;flex-direction:column;flex:1;min-width:0}
.comp-btn b{font-size:13.5px;font-weight:900;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.comp-btn small{font-size:11px;font-weight:700;color:#9bb6a7}
.cpn-band{width:26px;height:18px;flex:none;object-fit:cover;border-radius:3px;box-shadow:0 0 0 1px rgba(255,255,255,.18)}
.cpn-band.vazio{display:inline-block;background:#2e4d39}
/* cabeçalho da competição: bandeira, país/divisão/período e o nome */
.comp-cab{position:relative;z-index:1;display:flex;align-items:center;gap:16px}
.comp-band{width:64px;height:44px;object-fit:cover;border-radius:6px;box-shadow:0 0 0 2px rgba(255,255,255,.22),0 6px 16px rgba(0,0,0,.35)}
.comp-cab-txt{min-width:0}
.comp-sobre{display:block;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#9fe7bf}
.comp-cab h1{margin:4px 0 0}
/* painel de competições */
.comp-painel{position:fixed;inset:0;z-index:60;display:flex;align-items:flex-start;justify-content:center;padding:6vh 16px;background:rgba(2,8,5,.72)}
.comp-painel[hidden]{display:none}
body.sem-rolar{overflow:hidden}
.cpn-caixa{width:min(860px,100%);max-height:84vh;display:flex;flex-direction:column;background:#0c1d14;border:1px solid #2e4d39;border-radius:16px;
  box-shadow:0 24px 60px rgba(0,0,0,.55);overflow:hidden;color:#eafff2}
.cpn-topo{display:flex;gap:10px;padding:14px;border-bottom:1px solid #2e4d39}
.cpn-topo input{flex:1;font:inherit;font-size:14px;color:#eafff2;background:rgba(5,11,8,.7);border:1px solid #2e4d39;border-radius:10px;padding:10px 12px}
.cpn-topo input:focus{outline:none;border-color:var(--accent)}
.cpn-fechar{font:inherit;font-weight:900;color:#9bb6a7;background:transparent;border:1px solid #2e4d39;border-radius:10px;padding:0 14px;cursor:pointer}
.cpn-corpo{display:grid;grid-template-columns:240px 1fr;min-height:0;flex:1}
.cpn-paises{overflow-y:auto;padding:10px;border-right:1px solid #2e4d39}
.cpn-cont{font-size:10.5px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:#6f8f7d;margin:10px 8px 6px}
.cpn-cont:first-child{margin-top:2px}
.cpn-pais{display:flex;align-items:center;gap:10px;width:100%;font:inherit;font-size:13.5px;font-weight:700;color:#cfe4d6;background:transparent;
  border:0;border-radius:9px;padding:8px;cursor:pointer;text-align:left}
.cpn-pais span{flex:1}
.cpn-pais small{font-size:11px;color:#6f8f7d}
.cpn-pais:hover{background:rgba(30,203,116,.08)}
.cpn-pais.ativo{background:rgba(30,203,116,.14);color:#32d57f}
.cpn-lista{overflow-y:auto;padding:14px}
.cpn-titulo{display:flex;align-items:center;gap:10px;font-size:18px;font-weight:900;margin:2px 4px 8px}
.cpn-grupo{font-size:10.5px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:#fbbf24;margin:14px 4px 6px}
.cpn-comp{display:flex;align-items:center;gap:10px;width:100%;font:inherit;text-align:left;color:#eafff2;background:rgba(255,255,255,.02);
  border:1px solid #1d3528;border-radius:10px;padding:10px 12px;margin-bottom:6px;cursor:pointer}
.cpn-comp span{display:flex;flex-direction:column;min-width:0}
.cpn-comp b{font-size:14px;font-weight:800}
.cpn-comp small{font-size:11.5px;color:#9bb6a7}
.cpn-comp:hover{border-color:var(--accent)}
.cpn-comp.ativo{border-color:var(--accent);background:rgba(30,203,116,.1)}
.cpn-nada{color:#9bb6a7;margin:8px 4px}
@media (max-width:700px){
  .comp-painel{padding:0}
  .cpn-caixa{max-height:100vh;height:100%;border-radius:0}
  .cpn-corpo{grid-template-columns:1fr;grid-template-rows:auto 1fr}
  .cpn-paises{display:flex;gap:6px;overflow-x:auto;overflow-y:hidden;border-right:0;border-bottom:1px solid #2e4d39;padding:10px}
  .cpn-cont{display:none}
  .cpn-pais{width:auto;flex:none;white-space:nowrap;border:1px solid #2e4d39;border-radius:999px;padding:6px 10px}
  .comp-band{width:48px;height:33px}
  .comp-cab{gap:12px}
}
.lateral .marca img{flex:none;display:block;filter:drop-shadow(0 3px 6px rgba(0,0,0,.35))}
.lateral .marca small{display:block;font-size:10.5px;font-weight:700;letter-spacing:.08em;color:#9bb6a7}
.nav{display:flex;align-items:center;gap:10px;width:100%;font-family:inherit;font-size:14px;font-weight:700;text-align:left;color:#b9d3c2;background:transparent;
  border:1px solid transparent;border-radius:10px;padding:10px 12px;cursor:pointer;transition:background .12s,color .12s}
.nav:hover{color:#f8fff8;background:rgba(30,203,116,.08)}
.nav.ativo{color:#06100b;background:#1ecb74;box-shadow:0 6px 18px rgba(30,203,116,.25)}
.nav .ico{width:20px;text-align:center}
.lateral .tema{position:static;margin-top:auto;width:100%}
.area{margin-left:224px;min-height:100vh}
.em-breve{text-align:center;padding:60px 20px;color:var(--muted)}
.em-breve b{display:block;margin-bottom:6px;font-size:20px;color:var(--champ)}
@media (max-width:900px){   /* celular: 1ª linha competição e tema; 2ª as três abas; 3ª as sub-abas da aba aberta */
  .lateral{position:relative;bottom:auto;width:auto;flex-direction:row;flex-wrap:wrap;align-items:center;gap:8px;padding:10px 12px;overflow:visible;border-right:0;border-bottom:1px solid #2e4d39}
  .lateral .marca{order:0;flex:none;margin:0}.lateral .marca span{display:none}.lateral .marca img{width:36px;height:auto}
  .comp-escolha{order:1;flex:1 1 calc(100% - 140px);margin:0;min-width:0}
  .lateral .tema{order:2;flex:0 0 80px;margin:0;width:auto;white-space:nowrap}
  .nav{order:3;flex:1 1 0;min-width:0;justify-content:center;white-space:nowrap;padding:9px 6px;font-size:13px}
  .area{margin-left:0}
}
@media (max-width:480px){.nav .ico{display:none}.nav{font-size:12.5px}}
/* sub-abas: itens recuados na barra lateral, abaixo da aba (só aparecem com a aba aberta) */
.subnav-lat{display:flex;flex-direction:column;gap:2px;margin:2px 0 8px 22px;padding-left:10px;border-left:2px solid #2e4d39}
.subnav-lat[hidden]{display:none}
.sub{font-family:inherit;font-size:13px;font-weight:600;text-align:left;color:#9bb6a7;background:transparent;border:0;border-radius:8px;padding:7px 10px;cursor:pointer;position:relative}
.sub:hover{color:#f8fff8;background:rgba(30,203,116,.08)}
.sub.ativo{color:#32d57f;font-weight:800;background:rgba(30,203,116,.10)}
.sub.ativo::before{content:"";position:absolute;left:-12px;top:6px;bottom:6px;width:2px;background:#1ecb74;border-radius:2px}
@media (max-width:900px){.subnav-lat{order:4;flex:1 1 100%;flex-direction:row;gap:6px;overflow-x:auto;margin:0;padding:0;border-left:0;scrollbar-width:none}
  .subnav-lat::-webkit-scrollbar{display:none}
  .sub{flex:none;white-space:nowrap;border:1px solid #2e4d39;border-radius:999px;padding:6px 12px}.sub.ativo{border-color:#1ecb74}.sub.ativo::before{display:none}}
main{max-width:1240px;margin:0 auto;padding:26px 24px 70px}
.painel{background:linear-gradient(180deg,var(--panel-2),var(--panel));border:1px solid var(--border);border-radius:14px;padding:22px 22px 18px;box-shadow:var(--shadow-sm)}
.titulo-bloco{margin:0 0 4px;font-size:22px;font-weight:800;color:var(--champ)}
.pergunta{margin:0 0 14px;color:var(--muted);max-width:860px}
.legenda{display:flex;flex-wrap:wrap;gap:16px;margin:0 0 16px;font-size:12.5px;color:var(--muted)}
.legenda i{display:inline-block;width:22px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px;background:var(--muted)}
.legenda i.listra{background:repeating-linear-gradient(135deg,var(--muted) 0 3px,transparent 3px 6px);box-shadow:inset 0 0 0 1px var(--muted)}
/* gráfico: uma linha por clube */
.linha{display:grid;grid-template-columns:150px 1fr 162px;align-items:center;gap:12px;padding:7px 0;border-top:1px solid var(--border)}
.linha:first-of-type{border-top:0}
.clube{display:flex;align-items:center;gap:8px;font-weight:700;font-size:14px;min-width:0}
.clube .bola{width:14px;height:14px;border-radius:50%;flex:none;box-shadow:0 0 0 1px rgba(255,255,255,.25)}
/* escudo sobre um disco claro: os escudos escuros não somem no tema escuro */
.clube .escudo{width:40px;height:40px;flex:none;border-radius:50%;background:#eef4ee;padding:6px;object-fit:contain;box-shadow:0 0 0 2px var(--c1,transparent),0 2px 6px rgba(0,0,0,.3)}
.clube span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.trilhos{display:grid;gap:4px}
.trilho{display:flex;flex-wrap:wrap;gap:3px;padding:3px;border-radius:8px;background:var(--trilho);min-height:34px}
.trilho.vices,.trilho.terc{min-height:26px;background:transparent;padding:0 3px}
.bloco{position:relative;width:46px;height:28px;border-radius:5px;display:grid;place-items:center;font-size:11px;font-weight:800;letter-spacing:.01em;
  font-variant-numeric:tabular-nums;color:var(--fg);background:var(--c1);box-shadow:inset 0 -3px 0 var(--c2);cursor:default;
  transition:transform .12s;animation:entra .5s ease-out both}
.bloco:hover{transform:translateY(-2px);outline:2px solid var(--champ);outline-offset:1px;z-index:1}
.bloco.antigo{background-color:var(--c1);background-image:repeating-linear-gradient(135deg,var(--risca) 0 2px,transparent 2px 7px);text-shadow:0 0 3px var(--c1),0 0 2px var(--c1)}
.totais{display:flex;justify-content:flex-end;gap:14px;text-align:right;font-variant-numeric:tabular-nums}
.total{font-size:22px;font-weight:900;color:var(--champ);line-height:1.15}
.total.v{color:var(--muted);font-size:18px}
.total.r{color:var(--muted);font-size:16px;opacity:.8}
.total small{display:block;font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
/* vice: só o contorno na cor do clube */
.bloco.vice{height:22px;font-size:10.5px;color:var(--text);background:transparent;box-shadow:none;border:2px solid var(--borda);opacity:.85}
.bloco.vice.antigo{background:transparent;border-style:dashed;text-shadow:none}
/* 3º lugar: contorno pontilhado, mais discreto que o vice */
.bloco.terc{height:20px;font-size:10px;color:var(--muted);background:transparent;box-shadow:none;border:2px dotted var(--borda);opacity:.75;text-shadow:none}
.legenda i.ponto{background:transparent;box-shadow:none;border:2px dotted var(--muted)}
.legenda i.contorno{background:transparent;box-shadow:inset 0 0 0 2px var(--muted)}
.nota-rodape{margin:16px 0 0;font-size:12.5px;color:var(--muted)}
.painel + .painel{margin-top:22px}
/* corrida dos títulos */
.corrida-ctl{display:flex;align-items:center;gap:12px;margin:0 0 8px}
.titulo-bloco + .corrida-ctl,.titulo-bloco + #grafico{margin-top:14px}
.corrida-ctl button{font-family:inherit;font-weight:800;font-size:13px;color:#06100b;background:var(--accent);border:0;border-radius:8px;padding:8px 14px;cursor:pointer;min-width:132px}
.corrida-ctl input[type=range]{flex:1;accent-color:var(--accent);min-width:0}
.corrida-ctl output{font-weight:900;font-size:18px;color:var(--champ);font-variant-numeric:tabular-nums;min-width:48px;text-align:right}
#corrida,.grafico-corrida{width:100%;height:auto;max-height:calc(100vh - 150px);display:block}   /* cabe na tela junto com os botões */
.corrida-rolar{overflow-x:auto}
.cr-grade{stroke:var(--border);stroke-width:1}
.cr-eixo{fill:var(--muted);font-size:12px;font-weight:600}
#cr-anogrande,.cr-anogrande{fill:var(--text);opacity:.06;font-size:150px;font-weight:900}
.cr-ponta{stroke:var(--panel);stroke-width:2}
.cr-linha{fill:none;stroke-width:3.5;stroke-linejoin:round;stroke-linecap:round;transition:opacity .15s}
.cr-rot{cursor:pointer;transition:opacity .15s}
.cr-rot text{fill:var(--text);font-size:13px;font-weight:800;paint-order:stroke;stroke:var(--panel);stroke-width:3px}
.cr-rot text tspan{fill:var(--champ)}
/* quem pontuou no ano da corrida: nome dourado com brilho e ponta que cresce e volta */
.cr-rot.pulsa text{fill:var(--champ);animation:pulsar-nome 1s ease-in-out infinite}
.cr-rot.pulsa .cr-ponta{transform-box:fill-box;transform-origin:center;animation:pulsar-ponta 1s ease-in-out infinite}
@keyframes pulsar-nome{0%,100%{filter:none}50%{filter:drop-shadow(0 0 5px rgba(251,191,36,.95))}}
@keyframes pulsar-ponta{0%,100%{transform:scale(1)}50%{transform:scale(1.9)}}
@media (prefers-reduced-motion:reduce){.cr-rot.pulsa text,.cr-rot.pulsa .cr-ponta{animation:none}}
svg.foco .cr-linha:not(.ativo),svg.foco .cr-rot:not(.ativo),svg.foco .cr-med:not(.ativo){opacity:.12}
svg.foco .cr-linha.ativo{stroke-width:4.5}
/* participações: uma faixa por clube, um quadradinho por edição */
.pt-cab,.pt-linha{display:grid;grid-template-columns:190px 1fr 74px;align-items:center;gap:12px}
.pt-cab{margin:0 0 4px}
.pt-linha{padding:5px 0;border-top:1px solid var(--border)}
.pt-eixo,.pt-faixa{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:2px}
.pt-eixo span{font-size:10.5px;font-weight:700;color:var(--muted);white-space:nowrap;overflow:visible;height:14px}
.pt-faixa i{height:18px;border-radius:2px;background:var(--trilho)}
.pt-faixa i.on{background:var(--c);cursor:default}
.pt-faixa i.on:hover{outline:2px solid var(--text);outline-offset:1px}
.pt-faixa i.tit{box-shadow:inset 0 0 0 2px var(--champ)}
.pt-linha .clube .escudo{width:32px;height:32px;padding:5px}
.pt-linha .total{font-size:19px;text-align:right}
.pt-legenda{display:flex;flex-wrap:wrap;gap:16px;margin:0 0 14px;font-size:12.5px;color:var(--muted)}
.pt-legenda i{display:inline-block;width:12px;height:14px;border-radius:2px;margin-right:6px;vertical-align:-2px;background:var(--muted)}
.pt-legenda i.vazio{background:var(--trilho);box-shadow:inset 0 0 0 1px var(--border)}
.pt-legenda i.tit{box-shadow:inset 0 0 0 2px var(--champ)}
.pt-mais{margin-top:14px;font-family:inherit;font-size:13px;font-weight:700;color:var(--text);background:var(--panel);border:1px solid var(--border);border-radius:999px;padding:7px 14px;cursor:pointer}
.pt-mais:hover{border-color:var(--accent)}
.pt-rolar{overflow-x:auto}
.cab-bloco{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.alterna{display:inline-flex;border:1px solid var(--border);border-radius:9px;overflow:hidden}
.alterna button{font-family:inherit;font-size:13px;font-weight:800;color:var(--muted);background:transparent;border:0;padding:7px 16px;cursor:pointer}
.alterna button+button{border-left:1px solid var(--border)}
.alterna button.ativo{color:#06100b;background:var(--accent)}
.cab-bloco .botoes{display:flex;gap:8px;flex-wrap:wrap}
.jv-corrida[hidden],.alterna[hidden]{display:none}
/* por campeonato */
.cp-escolha{position:relative;z-index:1;display:flex;align-items:center;gap:8px;margin-top:14px;flex-wrap:wrap}
.cp-escolha select{font-family:inherit;font-size:14px;font-weight:800;color:var(--header-text);background:rgba(5,11,8,.7);border:1px solid #2e4d39;border-radius:9px;padding:8px 12px;cursor:pointer;max-width:100%}
.cp-escolha select option,.cp-escolha select optgroup{color:#111;background:#fff}
.cp-seta{font-family:inherit;font-size:14px;font-weight:900;color:var(--header-text);background:rgba(5,11,8,.7);border:1px solid #2e4d39;border-radius:9px;width:38px;height:38px;cursor:pointer}
.cp-seta:hover:not(:disabled),.cp-escolha select:hover{border-color:var(--accent)}
.cp-seta:disabled{opacity:.35;cursor:default}
.cp-nota{margin:10px 0 0;font-size:13px;color:var(--muted)}
.podio{display:flex;align-items:flex-end;justify-content:center;gap:16px;margin-top:18px}
.pd{display:flex;flex-direction:column;align-items:center;gap:6px;width:200px;min-width:0;text-align:center}
.podio.dividido .pd{width:170px}
.pd .cp-esc{width:72px;height:72px;padding:10px}
.pd1 .cp-esc{width:100px;height:100px;padding:14px}
.pd b{font-size:16px;font-weight:900;color:var(--text);max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pd1 b{font-size:19px}
.pd small{font-size:12px;color:var(--muted);font-weight:700}
.degrau{width:100%;margin-top:6px;border-radius:10px 10px 0 0;display:flex;justify-content:center;padding-top:10px;font-size:26px;font-weight:900;color:#06100b}
.pd1 .degrau{height:120px;background:linear-gradient(#f7d046,#c99a06)}
.pd2 .degrau{height:86px;background:linear-gradient(#e7edf2,#9aa5b1)}
.pd3 .degrau{height:62px;background:linear-gradient(#e6a96b,#a8652a)}
/* escudo no círculo claro: margem interna de ~14% do diâmetro, para o escudo caber inteiro */
.cp-esc{width:30px;height:30px;flex:none;border-radius:50%;background:#eef4ee;padding:4px;object-fit:contain;box-shadow:0 2px 6px rgba(0,0,0,.3)}
span.cp-esc{display:inline-block}
.cp-rolar{overflow-x:auto;margin-top:12px}
.cp-tab{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums;min-width:640px}
.cp-tab th{font-size:11px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);text-align:right;padding:6px 8px;border-bottom:1px solid var(--border)}
.cp-tab th:nth-child(2){text-align:left}
.cp-tab td{padding:6px 8px;text-align:right;font-size:14px;font-weight:700;color:var(--text);border-top:1px solid var(--border)}
.cp-tab td.pos{font-weight:900;color:var(--muted);width:44px;border-left:4px solid transparent}
.cp-tab tr.p1 td.pos{border-left-color:#f5c518;color:var(--champ)}
.cp-tab tr.p2 td.pos{border-left-color:#c9d1d9}
.cp-tab tr.p3 td.pos{border-left-color:#cd7f32}
.cp-tab td.clube{text-align:left}
.cp-tab th:nth-child(n+3),.cp-tab td:nth-child(n+3){width:60px}
.cp-tab td.clube div,.cl-link{display:flex;align-items:center;gap:10px;font-weight:800}
.cl-link{color:inherit;text-decoration:none}.cl-link:hover{color:var(--accent)}
.cp-tab td.pts{font-weight:900;color:var(--champ);font-size:15px}
.cp-tab td.neg{color:#ef6b6b}
.cpp-tab th:nth-child(n+3),.cpp-tab td:nth-child(n+3){width:auto;text-align:left;white-space:nowrap}
.cpp-tab{margin-top:16px}
.curto{display:none}
.cpp-tab td b{font-weight:800}
.cp-jogo b small.pen{display:block;font-size:10.5px;font-weight:700;color:var(--muted);text-align:center}.cpp-tab .n-novo{color:#32d57f}.cpp-tab .n-vet{color:var(--champ)}
.mv{font-size:12.5px;font-weight:700;color:var(--muted)}
.mv.sobe{color:#32d57f}.mv.cai{color:#ef6b6b}.mv.fora{opacity:.6}
.mv.novo,.mv.vet{display:inline-block;margin-left:6px;padding:1px 7px;border-radius:999px;font-size:11px;font-weight:900;letter-spacing:.03em}
.mv.novo{color:#0b2616;background:#32d57f}.mv.vet{color:#2a1d00;background:#f5c518}
.cp-tab tbody tr:hover td{background:color-mix(in srgb,var(--accent) 8%,transparent)}
@media (max-width:640px){.pd{width:110px}.pd .cp-esc{width:52px;height:52px;padding:7px}.pd1 .cp-esc{width:66px;height:66px;padding:9px}.pd b{font-size:13px}.pd1 b{font-size:14px}
  .podio.dividido{gap:6px}.podio.dividido .pd{width:84px}.podio.dividido .pd1 .cp-esc{width:56px;height:56px;padding:8px}.podio.dividido .pd b{font-size:12px}}
.cr-faixa{opacity:.10}
.cr-faixa.titulo{fill:#f5c518;opacity:.16}.cr-faixa.libertadores{fill:var(--accent)}.cr-faixa.sula{fill:#4aa3df}.cr-faixa.rebaixamento{fill:#ef4444;opacity:.12}.cr-faixa.acesso{fill:var(--accent)}
.cp-legenda-faixa i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.cp-fases{list-style:none;counter-reset:f;margin:14px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px}
.cp-fases li{counter-increment:f;flex:1 1 200px;background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:12px 14px 12px 46px;position:relative}
.cp-fases li::before{content:counter(f);position:absolute;left:12px;top:12px;width:24px;height:24px;border-radius:50%;background:var(--accent);color:#06100b;font-weight:900;font-size:13px;display:grid;place-items:center}
.cp-fases b{display:block;font-weight:900;color:var(--text)}
.cp-fases span{font-size:12.5px;color:var(--muted)}
.cp-nav{display:flex;align-items:center;gap:8px;margin:14px 0 6px}
.cp-nav select{font-family:inherit;font-size:14px;font-weight:800;color:var(--text);background:var(--panel);border:1px solid var(--border);border-radius:9px;padding:8px 12px}
.cp-nav .cp-seta{color:var(--text);background:var(--panel);border-color:var(--border)}
.cp-subgrupo{margin:16px 0 6px;font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.cp-jogos{display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:6px 18px}
.cp-jogo{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:10px;padding:7px 10px;border-radius:9px;background:var(--panel);border:1px solid var(--border)}
.cp-jogo span{display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:700;color:var(--muted);min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cp-jogo .m{justify-content:flex-end}
.cp-jogo.vm .m,.cp-jogo.vv .v{color:var(--text);font-weight:900}
.cp-jogo b{font-size:16px;font-weight:900;color:var(--champ);font-variant-numeric:tabular-nums;min-width:56px;text-align:center}
.dl-escolha{flex-wrap:wrap}.dl-escolha select{min-width:0;max-width:calc(50% - 30px)}
.dl-placar{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;margin:10px 0 2px;font-size:15px}
.dl-placar .dl-num{font-size:26px;font-weight:900;font-variant-numeric:tabular-nums}
.dl-q{display:flex;align-items:center;gap:6px;font-weight:800;min-width:0}
.dl-linha{display:grid;grid-template-columns:1fr minmax(130px,220px) 1fr;align-items:center;gap:10px;padding:5px 0;border-top:1px solid var(--border)}
.dl-cab{border-top:0;padding-bottom:8px}.dl-cab .dl-q.a{justify-content:flex-end}
.dl-entre{background:color-mix(in srgb,var(--accent) 8%,transparent);border-radius:8px}
.dl-entre .dl-adv{justify-content:center;text-transform:uppercase;letter-spacing:.08em;font-size:12px}
.dl-adv{display:flex;align-items:center;gap:6px;min-width:0;font-size:13px}
.dl-adv b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dl-adv .n{color:var(--muted);font-size:12px;width:28px;text-align:right;flex:none;font-variant-numeric:tabular-nums}
.dl-barra{display:flex;align-items:center;gap:6px;height:18px;min-width:0}
.dl-barra.a{flex-direction:row-reverse}
.dl-barra i{display:block;height:100%;border-radius:3px;min-width:3px}
.dl-barra b{font-size:13px;font-variant-numeric:tabular-nums}
.dl-barra.vazio span{font-size:11px;color:var(--muted)}
@media (max-width:640px){.dl-linha{grid-template-columns:1fr 1fr;row-gap:3px}.dl-adv{grid-column:1 / -1;order:-1}.dl-cab .dl-adv{display:none}}
.cp-art{display:grid;grid-template-columns:34px 260px 1fr 44px;align-items:center;gap:12px;padding:7px 0;border-top:1px solid var(--border)}
.cp-art:first-child{border-top:0}
.cp-art .n{font-weight:900;color:var(--muted)}
.cp-art .quem b{display:block;font-weight:900;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cp-art .quem span{display:flex;align-items:center;gap:6px;font-size:12.5px;color:var(--muted)}
.cp-art .trilho{height:20px;border-radius:5px;background:var(--trilho)}
.cp-art .trilho i{display:block;height:100%;border-radius:5px;background:var(--c)}
.cp-art .gols{font-size:20px;font-weight:900;color:var(--champ);text-align:right}
@media (max-width:640px){.cp-art{grid-template-columns:28px 1fr 36px}.cp-art .trilho{grid-column:2 / -1;grid-row:2}.cp-jogos{grid-template-columns:1fr}}
/* por clube */
.cl-nome{position:relative;z-index:1;display:flex;align-items:center;gap:14px;margin-top:12px}
.cl-nome .cu-esc{width:64px;height:64px;padding:9px}
.cl-nome h1{margin:0}
.cl-traj-svg{width:100%;height:auto;display:block;margin-top:10px}
.cl-traj{fill:none;stroke-width:2.5;opacity:.85;stroke-linejoin:round}
.cl-ponto{fill:var(--c);stroke:var(--panel);stroke-width:1.5}
.cl-ponto.ouro{fill:#f5c518}.cl-ponto.prata{fill:#c9d1d9}.cl-ponto.bronze{fill:#cd7f32}
.cl-ponto:hover{stroke:var(--text);stroke-width:2.5}
.cl-pods{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.cl-pod{font-size:13px;font-weight:900;padding:5px 10px;border-radius:7px;color:#06100b;font-variant-numeric:tabular-nums}
.cl-pod.ouro{background:linear-gradient(#f7d046,#c99a06)}.cl-pod.prata{background:linear-gradient(#e7edf2,#9aa5b1)}.cl-pod.bronze{background:linear-gradient(#e6a96b,#a8652a)}
.cl-tab tbody tr{cursor:pointer}
.cl-tab td.comp{text-align:left;color:var(--muted);font-weight:700}
.cl-tab td.clube{font-weight:900}
.cl-tab th:nth-child(3){text-align:left}
.cl-tab th:nth-child(2),.cl-tab td:nth-child(2){width:70px;text-align:left}
.cl-tab th:nth-child(3),.cl-tab td:nth-child(3){width:auto}
.cl-conf{display:grid;grid-template-columns:220px 1fr 190px;align-items:center;gap:12px;padding:6px 0;border-top:1px solid var(--border)}
.cl-conf .quem{display:flex;align-items:center;gap:8px;min-width:0;font-weight:800}
.cl-conf .barra{display:flex;gap:2px;height:20px;border-radius:5px;overflow:hidden;min-width:6px}
.cl-conf .barra i{display:block;height:100%}
.cl-conf .num{text-align:right;font-size:13px;color:var(--muted)}
.cl-conf .num b{font-size:17px;font-weight:900;color:var(--champ)}
.cl-conf .num small{display:block;font-size:11.5px}
.cl-conf .v,.cl-leg.v,.cl-res.v{background:var(--accent)}
.cl-conf .e,.cl-leg.e,.cl-res.e{background:#8a9a90}
.cl-conf .d,.cl-leg.d,.cl-res.d{background:#ef6b6b}
.cl-leg{display:inline-block;width:14px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.cl-jogo{display:grid;grid-template-columns:110px 1fr 30px;align-items:center;gap:8px}
.cl-jogo .rot{font-size:11.5px;font-weight:800;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cl-res{font-style:normal;font-weight:900;font-size:12px;color:#06100b;border-radius:6px;height:26px;display:grid;place-items:center}
@media (max-width:640px){.cl-conf{grid-template-columns:1fr auto}.cl-conf .barra{grid-column:1 / -1;grid-row:2}.cl-jogo{grid-template-columns:1fr 30px}.cl-jogo .rot{grid-column:1 / -1}}
/* seletor próprio (lista no tema do painel) */
.esc-oculto{display:none}
.esc-box{position:relative;display:inline-flex;min-width:0;max-width:100%}
.esc-btn{display:flex;align-items:center;gap:10px;font-family:inherit;font-size:14px;font-weight:800;cursor:pointer;border-radius:9px;padding:6px 12px;min-height:38px;min-width:240px;max-width:100%;text-align:left}
.esc-txt{display:flex;align-items:center;gap:8px;flex:1;min-width:0}
.esc-txt span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.esc-seta{font-style:normal;font-size:12px;opacity:.75;transition:transform .15s}
.esc-box.aberto .esc-seta{transform:rotate(180deg)}
.cp-escolha .esc-btn{color:var(--header-text);background:rgba(5,11,8,.7);border:1px solid #2e4d39}
.cp-nav .esc-btn{color:var(--text);background:var(--panel);border:1px solid var(--border)}
.esc-btn:hover,.esc-box.aberto .esc-btn{border-color:var(--accent)}
.esc-painel{position:fixed;z-index:60;display:flex;flex-direction:column;gap:6px;padding:8px;background:var(--panel);border:1px solid var(--border);border-radius:12px;box-shadow:0 18px 44px rgba(0,0,0,.45)}
.esc-painel[hidden]{display:none}
.esc-busca{font-family:inherit;font-size:14px;font-weight:700;color:var(--text);background:var(--panel-2);border:1px solid var(--border);border-radius:8px;padding:8px 10px;outline:none}
.esc-busca:focus{border-color:var(--accent)}
.esc-lista{position:relative;overflow-y:auto;display:flex;flex-direction:column;gap:1px;scrollbar-width:thin;scrollbar-color:var(--border) transparent}
.esc-grupo{font-size:10.5px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:10px 10px 4px}
.esc-op{display:flex;align-items:center;gap:10px;flex:none;font-family:inherit;font-size:14px;font-weight:700;color:var(--text);background:transparent;border:0;border-radius:8px;padding:7px 10px;text-align:left;cursor:pointer}
.esc-op:hover,.esc-op:focus-visible{background:color-mix(in srgb,var(--accent) 14%,transparent);outline:none}
.esc-op.ativo{background:var(--accent);color:#06100b}
.esc-op[hidden],.esc-grupo[hidden]{display:none}
.esc-ico{width:22px;height:22px;object-fit:contain;flex:none;border-radius:50%;background:#eef4ee;padding:2px}
/* estatísticas e curiosidades */
.cu-cartoes{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:12px;margin-top:14px}
.cu-card{display:flex;flex-direction:column;gap:8px;background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:14px 16px;min-width:0}
.cu-rot{font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.cu-card small{font-size:12.5px;color:var(--muted);line-height:1.4}
.cu-card small b{color:var(--text)}
.cu-esc{width:38px;height:38px;flex:none;border-radius:50%;background:#eef4ee;padding:5px;object-fit:contain;box-shadow:0 2px 6px rgba(0,0,0,.3)}
.cu-esc.p{width:26px;height:26px;padding:4px}
span.cu-esc{display:inline-block}
.cu-jogo,.cu-um{display:flex;align-items:center;gap:10px}
.cu-jogo b,.cu-um b{font-size:28px;font-weight:900;color:var(--champ);font-variant-numeric:tabular-nums;white-space:nowrap}
.cu-um span{font-size:13px;font-weight:700;color:var(--text);line-height:1.25}
.cu-escudos{display:flex;flex-wrap:wrap;gap:6px}
.cu-grade{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
.cu-bloco{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:14px 16px;min-width:0}
.cu-bloco.largo{grid-column:1 / -1}
.cu-bloco h3{margin:0 0 10px;font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
#cu-gols{width:100%;height:auto;display:block}
.cu-barra-g{fill:var(--accent);opacity:.55}
.cu-barra-g.max,.cu-barra-g.min{fill:var(--champ);opacity:1}
.cu-barra-g:hover{opacity:1}
.cu-media{stroke:var(--text);stroke-dasharray:4 4;opacity:.5}
.cu-txt{fill:var(--text);font-size:12px;font-weight:800}
.cu-mando{display:flex;height:40px;border-radius:8px;overflow:hidden;gap:2px}
.cu-mando i{display:flex;align-items:center;justify-content:center;font-style:normal;font-weight:900;font-size:14px;color:#06100b}
.cu-mando .m{background:var(--accent)}.cu-mando .e{background:color-mix(in srgb,var(--accent) 50%,transparent);color:var(--text)}.cu-mando .v{background:var(--champ)}
.cu-mando-leg{display:flex;justify-content:space-between;margin-top:8px;font-size:12.5px;color:var(--muted)}
.cu-placar{display:grid;grid-template-columns:28px repeat(6,1fr);gap:3px;font-variant-numeric:tabular-nums}
.cu-placar span{font-size:11px;font-weight:800;color:var(--muted);display:flex;align-items:center;justify-content:center}
.cu-placar i{font-style:normal;height:34px;border-radius:5px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;font-weight:900;color:var(--text);
  background:color-mix(in srgb,var(--accent) var(--a),transparent);box-shadow:inset 0 0 0 1px var(--border)}
.cu-placar i small{font-size:10px;font-weight:700;color:var(--text);opacity:.7}
.cu-placar i.top{box-shadow:inset 0 0 0 2px var(--champ)}
.cu-uf{display:grid;grid-template-columns:44px 1fr auto;align-items:center;gap:10px;padding:5px 0;border-top:1px solid var(--border)}
.cu-uf:first-of-type{border-top:0}
.cu-uf b{font-weight:900;color:var(--text)}
.cu-uf .trilho-uf{height:22px;border-radius:5px;background:var(--accent);min-width:4px}
.cu-uf .n{font-weight:900;font-size:17px;color:var(--champ);text-align:right}
.cu-uf .meio{display:flex;align-items:center;gap:8px;min-width:0}
.cu-uf .esc{display:flex;gap:4px;flex-wrap:wrap}
.cu-par{display:flex;align-items:center;gap:6px;font-size:12.5px;color:var(--muted);flex-wrap:wrap}
.cu-par b{color:var(--text)}
.cu-um span small{display:block;font-size:11.5px;font-weight:600;color:var(--muted)}
@media (max-width:760px){.cu-grade{grid-template-columns:1fr}}
.grafico-corrida.alto{max-height:none}   /* todos os clubes: o gráfico cresce e a página rola */
.corrida-ctl .alterna{flex:none}
.corrida-ctl .alterna button{min-width:0;color:var(--muted);background:transparent;padding:7px 14px}
.corrida-ctl .alterna button.ativo{color:#06100b;background:var(--accent)}
.jv-corrida .corrida-ctl{position:sticky;top:0;z-index:3;background:var(--panel);padding:8px 0}   /* com todos os clubes, os controles acompanham a rolagem */
.cr-med{transition:opacity .15s}
.cr-med circle{stroke:#06100b;stroke-width:1.5}
.cr-med .ouro{fill:#f5c518}.cr-med .prata{fill:#c9d1d9}.cr-med .bronze{fill:#cd7f32}
.med{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px;box-shadow:0 0 0 1px rgba(0,0,0,.45)}
.med.ouro{background:#f5c518}.med.prata{background:#c9d1d9}.med.bronze{background:#cd7f32}
.pt-faixa i{position:relative}
.pt-faixa i.m-ouro::after,.pt-faixa i.m-prata::after,.pt-faixa i.m-bronze::after{content:'';position:absolute;left:50%;top:50%;width:6px;height:6px;margin:-3px 0 0 -3px;border-radius:50%;box-shadow:0 0 0 1.5px rgba(0,0,0,.55)}
.pt-faixa i.m-ouro::after{background:#f5c518}.pt-faixa i.m-prata::after{background:#c9d1d9}.pt-faixa i.m-bronze::after{background:#cd7f32}
/* jogos e vitórias: trilho do tamanho dos jogos (cor clara) preenchido pelas vitórias (cor cheia) */
.jv-linha{display:grid;grid-template-columns:190px 1fr 230px;align-items:center;gap:12px;padding:6px 0;border-top:1px solid var(--border)}
.jv-linha:first-child{border-top:0}
.jv-linha .clube .escudo{width:32px;height:32px;padding:5px}
.jv-area{height:24px}
.jv-jogos{display:flex;gap:2px;height:100%;border-radius:6px;overflow:hidden;transform-origin:left;animation:cresce .6s ease-out both}
.jv-jogos i{height:100%;box-shadow:inset 0 -3px 0 rgba(0,0,0,.18)}
.jv-jogos .v{background:var(--c)}
.jv-jogos .e{background:color-mix(in srgb,var(--c) 52%,transparent)}
.jv-jogos .d{background:color-mix(in srgb,var(--c) 22%,transparent);box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--c) 40%,transparent)}
.jv-num{text-align:right;line-height:1.15;font-variant-numeric:tabular-nums}
.jv-num b{font-size:18px;font-weight:900;color:var(--champ)}
.jv-num span{font-size:13px;font-weight:700;color:var(--muted)}
.jv-num small{display:block;font-size:11.5px;font-weight:700;color:var(--muted)}
.legenda-jv{display:inline-flex;align-items:center;gap:6px;margin-right:14px}
.legenda-jv i{display:inline-block;width:22px;height:12px;border-radius:3px;background:var(--muted)}
.legenda-jv i.meio{background:color-mix(in srgb,var(--muted) 52%,transparent)}
.legenda-jv i.claro{background:color-mix(in srgb,var(--muted) 22%,transparent);box-shadow:inset 0 0 0 1px var(--muted)}
@media (max-width:640px){.jv-linha{grid-template-columns:1fr auto;gap:6px 10px}.jv-area{grid-column:1 / -1;grid-row:2}}
@keyframes cresce{from{transform:scaleX(0)}to{transform:none}}
@media (prefers-reduced-motion:reduce){.jv-jogos{animation:none}}
@keyframes entra{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.bloco{animation:none}}
/* dica ao passar o mouse */
#dica{position:fixed;z-index:9;pointer-events:none;background:#050b08;color:#f1f7f1;border:1px solid #2e4d39;border-radius:8px;padding:7px 10px;font-size:12.5px;
  box-shadow:0 8px 22px rgba(0,0,0,.35);max-width:280px}
#dica b{color:#fbbf24}
@media (max-width:640px){
  .topo{padding:20px 16px 18px} .topo h1{font-size:21px} .tema{right:12px;top:12px}
  main{padding:16px 12px 60px} .painel{padding:16px 12px}
  .linha{grid-template-columns:1fr auto;gap:6px 10px} .trilhos{grid-column:1 / -1;grid-row:2} .total{font-size:19px} .total.v{font-size:16px} .total.r{font-size:15px} .totais{gap:10px}
  .bloco{width:42px}
  #corrida,.grafico-corrida{min-width:760px}   /* no celular o gráfico rola de lado em vez de encolher (e acompanha o ano) */
  .corrida-ctl{flex-wrap:wrap;gap:8px 10px}.corrida-ctl button{min-width:0}.corrida-ctl output{font-size:16px;min-width:0;text-align:left}
  .corrida-ctl input[type=range]{order:5;flex:1 1 100%}.corrida-ctl .alterna{margin-left:auto}
  .pt-tabela{min-width:760px}.pt-cab,.pt-linha{grid-template-columns:128px 1fr 40px;gap:8px}
  .pt-linha .clube,.pt-cab>span:first-child{position:sticky;left:0;z-index:1;background:var(--panel)}   /* o nome fica e as edições rolam */
  .cp-tab{min-width:0}.cp-tab .gpgc{display:none}.cp-tab th,.cp-tab td{padding:6px 4px;font-size:13px}
  .cp-tab th:nth-child(n+3),.cp-tab td:nth-child(n+3){width:30px}.cp-tab td.pos{width:34px}.cp-tab .cp-esc{width:22px;height:22px}
  .cpp-tab th:nth-child(n+3),.cpp-tab td:nth-child(n+3){width:auto;white-space:normal}
  #cl-traj{overflow-x:auto}.cl-traj-svg{min-width:640px}
  .cl-tab .comp{display:none}   /* campanhas: a competição sai (o ano leva à edição) */
  .longo{display:none}.curto{display:inline}.cpp-tab .mv.novo,.cpp-tab .mv.vet{margin-left:3px;padding:1px 5px;font-size:10px}.cpp-tab td:nth-child(n+3){white-space:nowrap}
}
"""

# competição aberta: ?c= no endereço, senão a última vista, senão a primeira. Os dados dela vêm de
# dados/<competição>.js, posto na página enquanto ela carrega (uma <script src> funciona também aberta do disco,
# onde o navegador não deixa ler arquivos com fetch). VERSAO evita o navegador usar dados velhos guardados.
ESCOLHA = """
const COMP = (() => { const q = new URLSearchParams(location.search).get('c'); let s = null;
  try { s = localStorage.getItem('v2-comp'); } catch (e) {}
  const tem = x => COMPS.some(c => c.s === x);
  return tem(q) ? q : tem(s) ? s : COMPS[0].s; })();
try { localStorage.setItem('v2-comp', COMP); } catch (e) {}
document.write('<script src="dados/' + COMP + '.js?v=' + VERSAO + '"><\\/script>');
"""
# preenche os [data-t] e expõe os dados da competição aberta
SELECAO = """
const D = window.DADOS_COMP, EDP = D.EDP, PART = D.PART, VIT = D.VIT, CJV = D.CJV, CUR = D.CUR, EDS = D.EDS, ARTC = D.ARTC, CONF = D.CONF;
document.querySelectorAll('[data-t]').forEach(n => { n.innerHTML = D.TX[n.dataset.t] ?? ''; });
"""
JS = """
const ED = D.ED;
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const cor = n => CORES[n] || ['#1ecb74', '#0b2616'];
// texto legível sobre a cor do clube
const luz = h => { const n = parseInt(h.slice(1), 16); return ((n >> 16) * 299 + ((n >> 8) & 255) * 587 + (n & 255) * 114) / 1000; };
const MEDALHA = { ouro: 'campeão', prata: 'vice', bronze: '3º lugar' };
const medalha = (i, c) => !ED[i] ? '' : ED[i].campeao === c || ED[i].co === c ? 'ouro' : ED[i].vice === c ? 'prata' : ED[i].terceiro === c ? 'bronze' : '';
const claro = h => luz(h) > 150, escuro = h => luz(h) < 40;
// 'São Paulo' -> 'sao-paulo' (vai no endereço da aba Por clube)
// ⫽ no eixo onde a competição ficou 3 anos ou mais sem edição (a Série A pula de 1937 para 1959)
const quebras = (anos, X, y) => anos.slice(1).map((a, i) => a - anos[i] >= 3 ? '<text class="cr-eixo" x="' + ((X(i) + X(i + 1)) / 2) + '" y="' + y + '" text-anchor="middle">⫽</text>' : '').join('');
// no celular o gráfico rola de lado: mantém à vista a ponta das linhas (o ano que está passando)
const seguir = (svg, x) => { const r = svg.parentElement, vb = svg.viewBox && svg.viewBox.baseVal;
  if (!vb || !vb.width || r.scrollWidth <= r.clientWidth + 2) return;
  r.scrollLeft = x * svg.clientWidth / vb.width - r.clientWidth * 0.55; };
// ano para mostrar: a temporada quando ela cruza o ano ("1992/93"); nas contas (décadas, eixos) vale o número
const anoT = x => x.t || x.ano;
// sem coluna de pontos: mata-mata e edição de várias fases (a soma de todos os jogos não é a pontuação oficial; decisão de 20/11/2026)
const semPts = e => e.mata || e.disputa.length > 1;
const ptsE = (e, v, em, d) => e.pv * v + (e.pe ?? 1) * em + (e.pd ?? 0) * d;   // empate e derrota valem 1 e 0, salvo pe/pd (Marrocos 3-2-1, Taiti 4-2-1)
const slugClube = c => c.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');   // contorno do vice: cor quase preta some no fundo escuro, usa a segunda cor
function desenhar() {
  // t = títulos, v = vices, r = 3º lugares
  const por = new Map(), ver = c => { if (!por.has(c)) por.set(c, { t: [], v: [], r: [] }); return por.get(c); };
  for (const e of ED) { if (e.campeao) ver(e.campeao).t.push(e); if (e.co) ver(e.co).t.push(e); if (e.vice) ver(e.vice).v.push(e); if (e.terceiro) ver(e.terceiro).r.push(e); }
  // mais títulos; empate: mais vices; depois mais 3º; depois quem subiu ao pódio primeiro
  const primeiro = x => Math.min(...x.t.map(e => e.ano), ...x.v.map(e => e.ano), ...x.r.map(e => e.ano));
  const clubes = [...por].sort((a, b) => b[1].t.length - a[1].t.length || b[1].v.length - a[1].v.length || b[1].r.length - a[1].r.length
    || primeiro(a[1]) - primeiro(b[1]) || a[0].localeCompare(b[0], 'pt-BR'));
  let k = 0;
  const camps = e => e.campeao + (e.co ? ' e ' + e.co : '');   // título dividido (D-07)
  const QUEM = { t: (c, e) => c + ' campeão' + (e.co ? ' (dividido com ' + (c === e.co ? e.campeao : e.co) + ')' : '') + '; vice: ' + (e.vice || '—'),
                 v: (c, e) => c + ' vice; campeão: ' + camps(e),
                 r: (c, e) => c + ' 3º lugar; campeão: ' + camps(e) + ', vice: ' + (e.vice || '—') };
  const bloco = (c, e, tipo) => { const [c1, c2] = cor(c), borda = claro(c1) || !escuro(c1) ? c1 : c2;
    return '<span class="bloco' + (tipo === 'v' ? ' vice' : tipo === 'r' ? ' terc' : '') + (e.comp ? ' antigo' : '') + '" style="--c1:' + c1 + ';--c2:' + c2 + ';--borda:' + borda + ';--fg:' + (claro(c1) ? '#111' : '#fff') +
      ';--risca:' + (claro(c1) ? 'rgba(0,0,0,.22)' : 'rgba(255,255,255,.22)') + ';animation-delay:' + Math.min(k++ * 3, 600) + 'ms"' +
      ' data-dica="' + esc('<b>' + anoT(e) + (e.comp ? ' · ' + e.comp : '') + '</b><br>' + QUEM[tipo](c, e) + (e.nota ? '<br>' + e.nota : '')) + '">' + (e.t ? e.t.slice(2) : e.ano) + '</span>'; };   // "2016/17" vira "16/17"
  const plural = (n, um, varios) => n + '<small>' + (n === 1 ? um : varios) + '</small>';
  const faixa = (c, x, tipo, cls) => x[tipo].length ? '<div class="trilho' + cls + '">' + x[tipo].map(e => bloco(c, e, tipo)).join('') + '</div>' : '';
  document.getElementById('grafico').innerHTML = clubes.map(([c, x]) => { const [c1, c2] = cor(c);
    return '<div class="linha"><div class="clube">' + (ESCUDOS[c] ? '<img class="escudo" alt="" src="' + ESCUDOS[c] + '" style="--c1:' + c1 + '">'
        : '<span class="bola" style="background:linear-gradient(90deg,' + c1 + ' 0 55%,' + c2 + ' 55%)"></span>') + '<span>' + esc(c) + '</span></div>' +
      '<div class="trilhos"><div class="trilho">' + x.t.map(e => bloco(c, e, 't')).join('') + '</div>' + faixa(c, x, 'v', ' vices') + faixa(c, x, 'r', ' terc') + '</div>' +
      '<div class="totais"><div class="total">' + plural(x.t.length, 'título', 'títulos') + '</div><div class="total v">' + plural(x.v.length, 'vice', 'vices') + '</div>' +
      '<div class="total r">' + x.r.length + '<small>3º</small></div></div></div>'; }).join('');
}
const dica = document.getElementById('dica');
document.addEventListener('mousemove', ev => {
  const b = ev.target.closest('[data-dica]');
  if (!b) { dica.hidden = true; return; }
  dica.innerHTML = b.dataset.dica; dica.hidden = false;
  dica.style.left = Math.min(ev.clientX + 14, innerWidth - dica.offsetWidth - 8) + 'px';
  dica.style.top = (ev.clientY + 18 + dica.offsetHeight > innerHeight ? ev.clientY - dica.offsetHeight - 10 : ev.clientY + 18) + 'px';
});
document.addEventListener('click', ev => {
  const t = ev.target.closest('.tema');
  if (t) { const r = document.documentElement, novo = r.dataset.theme === 'dark' ? 'light' : 'dark'; r.dataset.theme = novo; t.textContent = novo === 'dark' ? '☀ Claro' : '☾ Escuro';
    try { localStorage.setItem('v2-tema', novo); } catch (e) {} document.dispatchEvent(new Event('tema-mudou')); }
});
// ---- corrida dos títulos (ou dos vices, ou dos terceiros): posição de cada clube no ranking, ano a ano (1º no topo) ----
(() => {
  const svg = document.getElementById('corrida'); if (!svg) return;
  const NS = 'http://www.w3.org/2000/svg', W = 1000, ML = 44, MR = 210, MT = 18, MB = 32, PASSO = 490 / 16;   // 17 linhas cabem em 540
  const anos = [...new Set(ED.map(e => e.ano))].sort((a, b) => a - b), N = anos.length;
  const X = i => ML + i * (W - ML - MR) / (N - 1), Y = r => MT + (r - 1) * PASSO;
  const suave = t => t * t * (3 - 2 * t);
  const NOME = { campeao: 'títulos', vice: 'vices', terceiro: 'terceiros lugares' };
  // clube de cor quase preta: no tema escuro a linha usa a segunda cor (e no claro, cor clara usa a segunda)
  const corLinha = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  const TRACOS = ['', '8 5', '2 5', '12 4 2 4', '4 3'];
  let clubes = [], val = {}, pos = {}, inicio = {}, el = {}, anoG = null, fixo = null, chaveAtual = 'campeao';
  function montar(chave) {
    chaveAtual = chave;
    const quem = e => chave === 'campeao' ? [e.campeao, e.co].filter(Boolean) : e[chave] ? [e[chave]] : [];   // título dividido conta para os dois
    clubes = [...new Set(ED.flatMap(quem))];
    const R = clubes.length, H = MT + MB + (R - 1) * PASSO;
    // val[c][i]: quantos até anos[i]; pos[c][i]: posição no ranking (só quem já tem algum).
    // Empate: fica na frente quem chegou primeiro àquele número.
    const cont = {}, quando = {}; val = {}; pos = {};
    for (const c of clubes) { val[c] = []; pos[c] = []; cont[c] = 0; }
    anos.forEach((a, i) => {
      for (const e of ED) if (e.ano === a) for (const c of quem(e)) { cont[c]++; quando[c] = i; }
      for (const c of clubes) val[c][i] = cont[c];
      clubes.filter(c => cont[c] > 0).sort((x, y) => cont[y] - cont[x] || quando[x] - quando[y] || x.localeCompare(y, 'pt-BR'))
        .forEach((c, k) => { pos[c][i] = k + 1; });
    });
    inicio = Object.fromEntries(clubes.map(c => [c, val[c].findIndex(v => v > 0)]));
    let eixos = '';
    for (let r = 1; r <= R; r++) eixos += '<line class="cr-grade" x1="' + ML + '" x2="' + (W - MR) + '" y1="' + Y(r) + '" y2="' + Y(r) + '"/><text class="cr-eixo" x="' + (ML - 10) + '" y="' + (Y(r) + 4) + '" text-anchor="end">' + r + 'º</text>';
    anos.forEach((a, i) => { if (i === 0 || (a % 10 === 0 && X(i) - X(0) > 44)) eixos += '<text class="cr-eixo" x="' + X(i) + '" y="' + (H - MB + 22) + '" text-anchor="middle">' + a + '</text>'; });
    eixos += quebras(anos, X, H - MB + 6);
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    svg.setAttribute('aria-label', 'Posição de cada clube no ranking de ' + NOME[chave] + ', ano a ano');
    svg.innerHTML = '<text id="cr-anogrande" x="' + ((ML + W - MR) / 2) + '" y="' + (H - MB - 24) + '" text-anchor="middle"></text>' + eixos + '<g id="cr-linhas"></g><g id="cr-rotulos"></g>';
    const gL = svg.querySelector('#cr-linhas'), gR = svg.querySelector('#cr-rotulos'); anoG = svg.querySelector('#cr-anogrande');
    el = {};
    for (const c of clubes) {
      const pth = document.createElementNS(NS, 'path'); pth.setAttribute('class', 'cr-linha'); pth.dataset.clube = c; gL.appendChild(pth);
      const g = document.createElementNS(NS, 'g'); g.setAttribute('class', 'cr-rot'); g.dataset.clube = c;
      g.innerHTML = '<circle class="cr-ponta" cx="0" cy="0" r="5"/>' + (ESCUDOS[c] ? '<image href="' + ESCUDOS[c] + '" x="10" y="-11" width="22" height="22"/>' : '') + '<text x="37" y="5"></text>';
      gR.appendChild(g); el[c] = { pth, g, txt: g.querySelector('text'), ponta: g.querySelector('circle') };
    }
    pintar();
    document.getElementById('cr-titulo').textContent = 'Corrida dos ' + NOME[chave];
  }
  function pintar() { const vistos = {};
    for (const c of clubes) { const s = corLinha(c), k = vistos[s] = (vistos[s] ?? -1) + 1;
      el[c].pth.setAttribute('stroke', s); el[c].pth.setAttribute('stroke-dasharray', TRACOS[k % TRACOS.length]); el[c].ponta.setAttribute('fill', s); } }
  document.addEventListener('tema-mudou', pintar);
  const btn = document.getElementById('cr-play'), barra = document.getElementById('cr-ano'), saida = document.getElementById('cr-saida');
  barra.max = N - 1;
  let p = N - 1, tocando = false, tAnt = 0;
  const VEL = 0.0014;   // edições por milissegundo: ~50 s de 1937 a hoje
  function quadro() {
    const i = Math.min(N - 1, Math.floor(p + 1e-9)), fr = p - i, xp = X(p);
    for (const c of clubes) {
      const e = el[c], f = inicio[c];
      if (f < 0 || f > i) { e.pth.setAttribute('d', ''); e.g.style.display = 'none'; continue; }
      // curva suave entre uma posição e a seguinte; a ponta anda até p
      let d = 'M' + X(f) + ' ' + Y(pos[c][f]);
      for (let k = f + 1; k <= i; k++) { const xm = (X(k - 1) + X(k)) / 2; d += 'C' + xm + ' ' + Y(pos[c][k - 1]) + ' ' + xm + ' ' + Y(pos[c][k]) + ' ' + X(k) + ' ' + Y(pos[c][k]); }
      let yp = Y(pos[c][i]);
      if (fr > 0 && i + 1 < N) {
        yp = Y(pos[c][i]) + (Y(pos[c][i + 1]) - Y(pos[c][i])) * suave(fr);
        const xm = (X(i) + xp) / 2; d += 'C' + xm + ' ' + Y(pos[c][i]) + ' ' + xm + ' ' + yp + ' ' + xp + ' ' + yp;
      }
      e.pth.setAttribute('d', d);
      e.g.style.display = ''; e.g.setAttribute('transform', 'translate(' + xp.toFixed(1) + ' ' + yp.toFixed(1) + ')');
      const v = val[c][fr > .5 && i + 1 < N ? i + 1 : i];
      e.txt.innerHTML = esc(c) + ' <tspan>' + v + '</tspan>';
    }
    anoG.textContent = anos[i]; saida.textContent = anos[i]; barra.value = p; seguir(svg, X(p));
    // quem foi campeão (ou vice, ou 3º) no ano em que a corrida está pulsa
    const pontuou = new Set(ED.filter(e => e.ano === anos[i] && e[chaveAtual]).map(e => e[chaveAtual]));
    for (const c of clubes) el[c].g.classList.toggle('pulsa', pontuou.has(c));
  }
  function tique(t) {
    if (!tocando) return;
    p = Math.min(N - 1, p + (tAnt ? t - tAnt : 16) * VEL); tAnt = t; quadro();
    if (p >= N - 1) parar(); else requestAnimationFrame(tique);
  }
  function tocar() { if (p >= N - 1) p = 0; tocando = true; tAnt = 0; btn.textContent = '❚❚ Pausar'; requestAnimationFrame(tique); }
  function parar() { tocando = false; btn.textContent = p >= N - 1 ? '↺ Ver de novo' : '▶ Continuar'; }
  btn.onclick = () => tocando ? parar() : tocar();
  barra.oninput = () => { if (tocando) parar(); p = +barra.value; quadro(); btn.textContent = p >= N - 1 ? '↺ Ver de novo' : '▶ Continuar'; };
  // destaque: passar o mouse (ou tocar) num clube
  const focar = c => { svg.classList.toggle('foco', !!c); for (const k of clubes) { el[k].pth.classList.toggle('ativo', k === c); el[k].g.classList.toggle('ativo', k === c); } };
  svg.addEventListener('mouseover', ev => { const t = ev.target.closest('[data-clube]'); if (t) focar(t.dataset.clube); });
  svg.addEventListener('mouseleave', () => focar(fixo));
  svg.addEventListener('click', ev => { const t = ev.target.closest('[data-clube]'); fixo = t && fixo !== t.dataset.clube ? t.dataset.clube : null; focar(fixo); });
  // Títulos | Vices | Terceiros
  const tb = document.querySelectorAll('#cr-tipo button');
  tb.forEach(b => b.addEventListener('click', () => {
    tb.forEach(x => x.classList.toggle('ativo', x === b));
    if (tocando) parar(); fixo = null; montar(b.dataset.tipo); focar(null); quadro();
    btn.textContent = p >= N - 1 ? '▶ Ver a corrida' : '▶ Continuar';
  }));
  montar('campeao'); quadro();
  btn.textContent = '▶ Ver a corrida';
})();
// ---- participações: uma faixa por clube, um quadradinho por edição (cheio = jogou; dourado = campeão) ----
(() => {
  const box = document.getElementById('participacoes'); if (!box) return;
  const N = EDP.length, TOP = 30;
  // mais participações; empate: quem estreou primeiro; depois o nome
  const lista = Object.entries(PART).sort((a, b) => b[1].length - a[1].length || a[1][0][0] - b[1][0][0] || a[0].localeCompare(b[0], 'pt-BR'));
  const corCel = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  // rótulos do eixo: a primeira edição e a primeira de cada década
  const eixo = EDP.map((e, i) => '<span>' + (i === 0 || (Math.floor(e.ano / 10) !== Math.floor(EDP[i - 1].ano / 10) && i > 2) ? e.ano : '') + '</span>').join('');
  let todos = false;
  function desenhar() {
    const linhas = (todos ? lista : lista.slice(0, TOP)).map(([c, ps]) => {
      const onde = new Map(ps.map(([i, pos]) => [i, pos])), cc = corCel(c), [c1, c2] = cor(c);
      const cel = Array.from({ length: N }, (_, i) => {
        if (!onde.has(i)) return '<i></i>';
        const e = EDP[i], m = medalha(i, c);
        return '<i class="on' + (m ? ' m-' + m : '') + '" data-dica="' + esc('<b>' + anoT(e) + (e.comp ? ' · ' + e.comp : '') + '</b><br>' + c + ': ' + onde.get(i) + 'º de ' + e.n + (m ? ' · ' + MEDALHA[m] : '')) + '"></i>';
      }).join('');
      return '<div class="pt-linha"><div class="clube">' + (ESCUDOS[c] ? '<img class="escudo" alt="" src="' + ESCUDOS[c] + '" style="--c1:' + c1 + '">'
        : '<span class="bola" style="background:linear-gradient(90deg,' + c1 + ' 0 55%,' + c2 + ' 55%)"></span>') + '<span>' + esc(c) + '</span></div>' +
        '<div class="pt-faixa" style="--n:' + N + ';--c:' + cc + '">' + cel + '</div><div class="total">' + ps.length + '</div></div>';
    }).join('');
    box.innerHTML = '<div class="pt-rolar"><div class="pt-tabela"><div class="pt-cab"><span></span><div class="pt-eixo" style="--n:' + N + '">' + eixo + '</div><span></span></div>' + linhas + '</div></div>' +
      '<button class="pt-mais" type="button">' + (todos ? 'Ver só os ' + TOP + ' que mais participaram' : 'Ver todos os ' + lista.length + ' clubes') + '</button>';
    const pr = box.querySelector('.pt-rolar'); pr.scrollLeft = pr.scrollWidth;   // no celular rola de lado: começa nas edições mais novas
  }
  box.addEventListener('click', ev => { if (ev.target.closest('.pt-mais')) { todos = !todos; desenhar(); } });
  document.addEventListener('tema-mudou', desenhar);
  desenhar();
})();
// ---- jogos e vitórias: barra do tamanho dos jogos, preenchida pelas vitórias ----
(() => {
  const box = document.getElementById('jogos-vitorias'); if (!box) return;
  const TOP = 30, MIN = 100;   // no %, só clubes com MIN jogos ou mais (com poucos jogos o % engana)
  const ORDEM = {
    vitorias: [...VIT].sort((a, b) => b[2] - a[2] || a[1] - b[1] || a[0].localeCompare(b[0], 'pt-BR')),
    jogos: [...VIT].sort((a, b) => b[1] - a[1] || b[2] - a[2] || a[0].localeCompare(b[0], 'pt-BR')),
    pct: VIT.filter(x => x[1] >= MIN).sort((a, b) => b[2] / b[1] - a[2] / a[1] || b[2] - a[2]),
  };
  const maxJ = Math.max(...VIT.map(x => x[1]));
  const corBarra = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  const fmtN = n => n.toLocaleString('pt-BR'), pct = (v, j) => (100 * v / j).toFixed(1).replace('.', ',') + '%';
  let modo = 'vitorias', todos = false;
  function desenhar() {
    const lista = ORDEM[modo];
    document.querySelectorAll('#jv-ordem button').forEach(b => b.classList.toggle('ativo', b.dataset.modo === modo));
    document.getElementById('jv-nota').textContent = modo === 'pct' ? ' · no %, só clubes com ' + MIN + ' jogos ou mais (' + lista.length + ')' : '';
    box.innerHTML = (todos ? lista : lista.slice(0, TOP)).map(([c, j, v, e, d, gp, gc], k) => { const [c1, c2] = cor(c), ed = (PART[c] || []).length;
      const dica = '<b>' + esc(c) + '</b><br>' + fmtN(j) + ' jogos em ' + ed + (ed === 1 ? ' edição' : ' edições') + '<br>' + fmtN(v) + ' vitórias (' + pct(v, j) + '), ' +
        fmtN(e) + ' empates (' + pct(e, j) + '), ' + fmtN(d) + ' derrotas (' + pct(d, j) + ')<br>gols: ' + fmtN(gp) + ' marcados, ' + fmtN(gc) + ' sofridos';
      return '<div class="jv-linha"><div class="clube">' + (ESCUDOS[c] ? '<img class="escudo" alt="" src="' + ESCUDOS[c] + '" style="--c1:' + c1 + '">'
        : '<span class="bola" style="background:linear-gradient(90deg,' + c1 + ' 0 55%,' + c2 + ' 55%)"></span>') + '<span>' + esc(c) + '</span></div>' +
        '<div class="jv-area" data-dica="' + esc(dica) + '"><div class="jv-jogos" style="width:' + (100 * j / maxJ).toFixed(2) + '%;--c:' + corBarra(c) + ';animation-delay:' + Math.min(k * 15, 450) + 'ms">' +
        '<i class="v" style="width:' + (100 * v / j).toFixed(2) + '%"></i><i class="e" style="width:' + (100 * e / j).toFixed(2) + '%"></i>' +
        '<i class="d" style="width:' + (100 * d / j).toFixed(2) + '%"></i></div></div>' +
        '<div class="jv-num"><b>' + fmtN(v) + '</b> <span>de ' + fmtN(j) + ' · ' + pct(v, j) + '</span><small>' + fmtN(e) + ' empates · ' + fmtN(d) + ' derrotas</small></div></div>'; }).join('') +
      (lista.length > TOP ? '<button class="pt-mais" type="button">' + (todos ? 'Ver só os ' + TOP + ' primeiros' : 'Ver todos os ' + lista.length + ' clubes') + '</button>' : '');
  }
  box.addEventListener('click', ev => { if (ev.target.closest('.pt-mais')) { todos = !todos; desenhar(); } });
  document.querySelectorAll('#jv-ordem button').forEach(b => b.addEventListener('click', () => { modo = b.dataset.modo; todos = false; desenhar(); if (window.jvCorrida && modo !== 'pct') window.jvCorrida(modo); }));
  // Barras | Corrida: na corrida o % não vale (sem sentido acumulado); a métrica é Vitórias ou Jogos
  document.querySelectorAll('#jv-vista button').forEach(b => b.addEventListener('click', () => {
    const corrida = b.dataset.vista === 'corrida';
    document.querySelectorAll('#jv-vista button').forEach(x => x.classList.toggle('ativo', x === b));
    document.getElementById('jv-barras').hidden = corrida; document.getElementById('jv-corrida').hidden = !corrida;
    document.querySelector('#jv-ordem [data-modo=pct]').hidden = corrida;
    if (corrida && modo === 'pct') { modo = 'vitorias'; desenhar(); }
    if (corrida && window.jvCorrida) window.jvCorrida(modo);
  }));
  document.addEventListener('tema-mudou', desenhar);
  desenhar();
})();
// ---- corridas de posições (jogos, vitórias, participações): ranking do acumulado, edição a edição; Top 20 ou Todos ----
// valores por edição → acumulado → posição (empate: quem chegou antes àquele número; depois o nome)
function ranking(inc, entrou = inc) {   // entrou: série que diz quando o clube aparece (acumulado > 0)
  const N = EDP.length, clubes = Object.keys(inc), acum = {}, pos = {}, desde = {}, base = {};
  for (const c of clubes) { let t = 0, u = 0; acum[c] = inc[c].map(x => t += x); base[c] = entrou[c].map(x => u += x); pos[c] = []; desde[c] = 0; }
  for (let i = 0; i < N; i++) {
    for (const c of clubes) if (i > 0 && acum[c][i] !== acum[c][i - 1]) desde[c] = i;
    clubes.filter(c => base[c][i] > 0).sort((a, b) => acum[b][i] - acum[a][i] || desde[a] - desde[b] || (a < b ? -1 : 1)).forEach((c, k) => pos[c][i] = k + 1);
    for (const c of clubes) if (pos[c][i] === undefined) pos[c][i] = 999;
  }
  return { clubes, acum, pos };
}
function corridaPosicoes(id, medalhas) {
  const svg = document.getElementById(id); if (!svg) return null;
  const NS = 'http://www.w3.org/2000/svg', W = 1000, ML = 44, MR = 230, MT = 18, MB = 32, TOP = 20, VEL = 0.0014;   // ~50 s de 1937 a hoje
  // eixo: anos das edições (padrão) ou o que vier em usar(..., eixo) — rodadas, por exemplo
  let anos = EDP.map(e => e.ano), N = anos.length, quebra = true, faixas = [], nomear = a => a;
  const X = i => ML + i * (W - ML - MR) / (N - 1);
  let marca = (a, i) => i === 0 || (a % 10 === 0 && X(i) - X(0) > 44);
  const suave = t => t * t * (3 - 2 * t);
  let fmtN = n => n.toLocaleString('pt-BR');
  const corLinha = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  const TRACOS = ['', '8 5', '2 5', '12 4 2 4', '4 3'];
  const btn = document.getElementById(id + '-play'), barra = document.getElementById(id + '-ano'), saida = document.getElementById(id + '-saida');
  barra.max = N - 1;
  let dados = null, todos = false, R = TOP, passo = 1, lista = [], el = {}, p = N - 1, tocando = false, tAnt = 0, fixo = null, anoG = null;
  const Y = r => MT + (r - 1) * passo;
  const yPos = (c, i) => { const r = dados.pos[c][i]; return Y(r <= R ? r : R + 1.6); };   // fora do top: some por baixo (cortado)
  function montar() {
    if (!dados) return;
    lista = dados.clubes.filter(c => todos ? dados.pos[c][N - 1] < 999 : dados.pos[c].some(r => r <= TOP));
    R = todos ? lista.length : TOP;
    passo = todos ? 26 : (600 - MT - MB) / (TOP - 1);
    const H = MT + MB + (R - 1) * passo, corte = todos ? H : Y(R) + passo * 0.6;
    let eixos = '';
    for (let r = 1; r <= R; r++) eixos += '<line class="cr-grade" x1="' + ML + '" x2="' + (W - MR) + '" y1="' + Y(r) + '" y2="' + Y(r) + '"/><text class="cr-eixo" x="' + (ML - 10) + '" y="' + (Y(r) + 4) + '" text-anchor="end">' + r + 'º</text>';
    anos.forEach((a, i) => { if (marca(a, i)) eixos += '<text class="cr-eixo" x="' + X(i) + '" y="' + (H - MB + 22) + '" text-anchor="middle">' + a + '</text>'; });
    if (quebra) eixos += quebras(anos, X, H - MB + 6);
    // faixas da tabela (título, Libertadores, Sul-Americana, rebaixamento) atrás das linhas
    eixos = faixas.filter(f => f[0] <= R).map(([r1, r2, z]) => '<rect class="cr-faixa ' + z + '" x="' + ML + '" width="' + (W - MR - ML) + '" y="' + (Y(r1) - passo / 2) +
      '" height="' + ((Math.min(r2, R) - r1 + 1) * passo) + '"/>').join('') + eixos;
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); svg.classList.toggle('alto', todos);
    svg.innerHTML = '<defs><clipPath id="' + id + '-corte"><rect x="0" y="0" width="' + W + '" height="' + corte + '"/></clipPath></defs>' +
      '<text class="cr-anogrande" x="' + ((ML + W - MR) / 2) + '" y="' + (todos ? MT + 150 : H - MB - 24) + '" text-anchor="middle"></text>' + eixos +
      '<g class="cr-linhas" clip-path="url(#' + id + '-corte)"></g><g class="cr-medalhas" clip-path="url(#' + id + '-corte)"></g><g class="cr-rotulos"></g>';
    const gL = svg.querySelector('.cr-linhas'), gM = svg.querySelector('.cr-medalhas'), gR = svg.querySelector('.cr-rotulos');
    anoG = svg.querySelector('.cr-anogrande'); el = {};
    const vistos = {};
    for (const c of lista) {
      const pth = document.createElementNS(NS, 'path'); pth.setAttribute('class', 'cr-linha'); pth.dataset.clube = c; gL.appendChild(pth);
      const g = document.createElementNS(NS, 'g'); g.setAttribute('class', 'cr-rot'); g.dataset.clube = c;
      g.innerHTML = '<circle class="cr-ponta" cx="0" cy="0" r="5"/>' + (ESCUDOS[c] ? '<image href="' + ESCUDOS[c] + '" x="10" y="-11" width="22" height="22"/>' : '') + '<text x="37" y="5"></text>';
      gR.appendChild(g);
      const st = corLinha(c), k = vistos[st] = (vistos[st] ?? -1) + 1;
      pth.setAttribute('stroke', st); pth.setAttribute('stroke-dasharray', TRACOS[k % TRACOS.length]); g.querySelector('circle').setAttribute('fill', st);
      const meds = [], gm = document.createElementNS(NS, 'g');
      if (medalhas) {   // pontinho no ano do pódio: ouro campeão, prata vice, bronze 3º
        gm.setAttribute('class', 'cr-med'); gm.dataset.clube = c; gM.appendChild(gm);
        for (let i = 0; i < N; i++) { const m = medalha(i, c); if (!m) continue;
          const ci = document.createElementNS(NS, 'circle'); ci.setAttribute('class', m); ci.setAttribute('r', '4.5');
          ci.setAttribute('cx', X(i)); ci.setAttribute('cy', yPos(c, i)); ci.dataset.dica = '<b>' + anos[i] + '</b><br>' + esc(c) + ': ' + MEDALHA[m];
          gm.appendChild(ci); meds.push([i, ci]); }
      }
      el[c] = { pth, g, gm, meds, txt: g.querySelector('text') };
    }
    if (fixo && !el[fixo]) fixo = null;
    focar(fixo);
  }
  function quadro() {
    if (!dados) return;
    const i = Math.min(N - 1, Math.floor(p + 1e-9)), fr = p - i, xp = X(p);
    for (const c of lista) {
      const e = el[c], val = dados.acum[c], f = dados.pos[c].findIndex(r => r < 999);
      for (const [k, ci] of e.meds) ci.style.display = k <= p + 1e-9 ? '' : 'none';
      if (f < 0 || f > i) { e.pth.setAttribute('d', ''); e.g.style.display = 'none'; continue; }
      let d = 'M' + X(f) + ' ' + yPos(c, f);
      for (let k = f + 1; k <= i; k++) { const xm = (X(k - 1) + X(k)) / 2; d += 'C' + xm + ' ' + yPos(c, k - 1) + ' ' + xm + ' ' + yPos(c, k) + ' ' + X(k) + ' ' + yPos(c, k); }
      let yp = yPos(c, i);
      if (fr > 0 && i + 1 < N) { yp = yPos(c, i) + (yPos(c, i + 1) - yPos(c, i)) * suave(fr); const xm = (X(i) + xp) / 2; d += 'C' + xm + ' ' + yPos(c, i) + ' ' + xm + ' ' + yp + ' ' + xp + ' ' + yp; }
      e.pth.setAttribute('d', d);
      const dentro = yp <= Y(R) + 1;
      e.g.style.display = dentro ? '' : 'none';
      if (dentro) { e.g.setAttribute('transform', 'translate(' + xp.toFixed(1) + ' ' + yp.toFixed(1) + ')');
        e.txt.innerHTML = esc(c) + ' <tspan>' + fmtN(val[fr > .5 && i + 1 < N ? i + 1 : i]) + '</tspan>'; }
    }
    anoG.textContent = anos[i]; saida.textContent = nomear(anos[i]); barra.value = p; seguir(svg, xp);
  }
  function tique(t) { if (!tocando) return; p = Math.min(N - 1, p + (tAnt ? t - tAnt : 16) * VEL); tAnt = t; quadro(); if (p >= N - 1) parar(); else requestAnimationFrame(tique); }
  function tocar() { if (p >= N - 1) p = 0; tocando = true; tAnt = 0; btn.textContent = '❚❚ Pausar'; requestAnimationFrame(tique); }
  function parar() { tocando = false; btn.textContent = p >= N - 1 ? '↺ Ver de novo' : '▶ Continuar'; }
  btn.onclick = () => tocando ? parar() : tocar();
  barra.oninput = () => { if (tocando) parar(); p = +barra.value; quadro(); btn.textContent = p >= N - 1 ? '↺ Ver de novo' : '▶ Continuar'; };
  function focar(c) { svg.classList.toggle('foco', !!c); for (const k in el) { const e = el[k]; e.pth.classList.toggle('ativo', k === c); e.g.classList.toggle('ativo', k === c); e.gm.classList.toggle('ativo', k === c); } }
  svg.addEventListener('mouseover', ev => { const t = ev.target.closest('[data-clube]'); if (t) focar(t.dataset.clube); });
  svg.addEventListener('mouseleave', () => focar(fixo));
  svg.addEventListener('click', ev => { const t = ev.target.closest('[data-clube]'); fixo = t && fixo !== t.dataset.clube ? t.dataset.clube : null; focar(fixo); });
  // Top 20 | Todos
  const qb = document.querySelectorAll('#' + id + '-quantos button');
  qb.forEach(b => b.addEventListener('click', () => { todos = b.dataset.q === 'todos'; qb.forEach(x => x.classList.toggle('ativo', x === b)); montar(); quadro(); }));
  document.addEventListener('tema-mudou', () => { montar(); quadro(); });
  btn.textContent = '▶ Ver a corrida';
  return { usar(d, fmt, eixo) {
    if (tocando) parar(); dados = d; if (fmt) fmtN = fmt; fixo = null;
    if (eixo) { anos = eixo.rot; N = anos.length; marca = eixo.marca; quebra = !!eixo.quebra; nomear = eixo.nomear || (a => a); faixas = eixo.faixas || [];
      barra.max = N - 1; p = N - 1; btn.textContent = '▶ Ver a corrida'; }
    montar(); quadro(); } };
}
// jogos e vitórias: a métrica vem dos botões Vitórias / Jogos
(() => {
  const jvc = corridaPosicoes('jvc', false); if (!jvc) return;
  const feito = {};
  window.jvCorrida = m => { const k = m === 'jogos' ? 'j' : 'v'; jvc.usar(feito[k] = feito[k] || ranking(CJV[k])); };
})();
// gols: a métrica vem dos botões Feitos / Tomados / Saldo
(() => {
  const glc = corridaPosicoes('glc', false); if (!glc) return;
  const feito = {}, num = n => n.toLocaleString('pt-BR'), saldo = n => (n > 0 ? '+' : n < 0 ? '−' : '') + num(Math.abs(n));
  const serie = {
    feitos: () => ranking(CJV.gp, CJV.j),
    tomados: () => ranking(CJV.gc, CJV.j),
    saldo: () => { const inc = {}; for (const c in CJV.gp) inc[c] = CJV.gp[c].map((g, i) => g - CJV.gc[c][i]); return ranking(inc, CJV.j); },
  };
  window.glCorrida = m => glc.usar(feito[m] = feito[m] || serie[m](), m === 'saldo' ? saldo : num);
})();
// pontuação histórica: pontos acumulados (3 por vitória, 1 por empate)
(() => {
  const pnc = corridaPosicoes('pnc', false); if (!pnc) return;
  let feito = null;
  window.pnCorrida = () => { if (!feito) { const inc = {}; for (const c in CJV.v) inc[c] = CJV.v[c].map((v, i) => 3 * v + CJV.e[c][i]); feito = ranking(inc, CJV.j); } pnc.usar(feito); };
})();
// participações: corrida das participações acumuladas, com as medalhas no caminho
(() => {
  const ptc = corridaPosicoes('ptc', true); if (!ptc) return;
  let pronto = false;
  const bs = document.querySelectorAll('#pt-vista button');
  bs.forEach(b => b.addEventListener('click', () => {
    const corrida = b.dataset.vista === 'corrida';
    bs.forEach(x => x.classList.toggle('ativo', x === b));
    document.getElementById('pt-quadro').hidden = corrida; document.getElementById('pt-corrida').hidden = !corrida;
    if (corrida && !pronto) { const inc = {};
      for (const [c, ps] of Object.entries(PART)) { const a = new Array(EDP.length).fill(0); ps.forEach(([i]) => a[i] = 1); inc[c] = a; }
      ptc.usar(ranking(inc)); pronto = true; }
  }));
})();
// ---- gols: barra com todos os gols dos jogos do clube, dividida em feitos e tomados ----
(() => {
  const box = document.getElementById('gols'); if (!box) return;
  const TOP = 30, MIN = 100;   // na média por jogo, só clubes com MIN jogos ou mais
  const nome = (a, b) => a[0].localeCompare(b[0], 'pt-BR');
  const ORDEM = {
    feitos: [...VIT].sort((a, b) => b[5] - a[5] || nome(a, b)),
    tomados: [...VIT].sort((a, b) => b[6] - a[6] || nome(a, b)),
    saldo: [...VIT].sort((a, b) => (b[5] - b[6]) - (a[5] - a[6]) || b[5] - a[5] || nome(a, b)),
    media: VIT.filter(x => x[1] >= MIN).sort((a, b) => b[5] / b[1] - a[5] / a[1] || b[5] - a[5]),
  };
  const maxG = Math.max(...VIT.map(x => x[5] + x[6]));
  const corBarra = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  const fmtN = n => n.toLocaleString('pt-BR'), med = (g, j) => (g / j).toFixed(2).replace('.', ',');
  const saldo = n => (n > 0 ? '+' : n < 0 ? '−' : '') + fmtN(Math.abs(n));
  let modo = 'feitos', todos = false;
  // número em destaque = o critério da ordenação escolhida; os outros vão na linha de baixo
  const numeros = (j, gp, gc) => ({
    feitos: '<b>' + fmtN(gp) + '</b> <span>feitos</span><small>' + fmtN(gc) + ' tomados · saldo ' + saldo(gp - gc) + ' · ' + med(gp, j) + ' por jogo</small>',
    tomados: '<b>' + fmtN(gc) + '</b> <span>tomados</span><small>' + fmtN(gp) + ' feitos · saldo ' + saldo(gp - gc) + ' · ' + med(gc, j) + ' tomados por jogo</small>',
    saldo: '<b>' + saldo(gp - gc) + '</b> <span>de saldo</span><small>' + fmtN(gp) + ' feitos · ' + fmtN(gc) + ' tomados</small>',
    media: '<b>' + med(gp, j) + '</b> <span>feitos por jogo</span><small>' + fmtN(gp) + ' feitos em ' + fmtN(j) + ' jogos</small>',
  })[modo];
  function desenhar() {
    const lista = ORDEM[modo];
    document.querySelectorAll('#gl-ordem button').forEach(b => b.classList.toggle('ativo', b.dataset.modo === modo));
    document.getElementById('gl-nota').textContent = modo === 'media' ? ' · na média, só clubes com ' + MIN + ' jogos ou mais (' + lista.length + ')' : '';
    box.innerHTML = (todos ? lista : lista.slice(0, TOP)).map(([c, j, v, e, d, gp, gc], k) => { const [c1, c2] = cor(c), t = gp + gc;
      const dica = '<b>' + esc(c) + '</b><br>' + fmtN(j) + ' jogos<br>' + fmtN(gp) + ' gols feitos (' + med(gp, j) + ' por jogo)<br>' +
        fmtN(gc) + ' gols tomados (' + med(gc, j) + ' por jogo)<br>saldo ' + saldo(gp - gc);
      return '<div class="jv-linha"><div class="clube">' + (ESCUDOS[c] ? '<img class="escudo" alt="" src="' + ESCUDOS[c] + '" style="--c1:' + c1 + '">'
        : '<span class="bola" style="background:linear-gradient(90deg,' + c1 + ' 0 55%,' + c2 + ' 55%)"></span>') + '<span>' + esc(c) + '</span></div>' +
        '<div class="jv-area" data-dica="' + esc(dica) + '"><div class="jv-jogos" style="width:' + (100 * t / maxG).toFixed(2) + '%;--c:' + corBarra(c) + ';animation-delay:' + Math.min(k * 15, 450) + 'ms">' +
        '<i class="v" style="width:' + (100 * gp / t).toFixed(2) + '%"></i><i class="d" style="width:' + (100 * gc / t).toFixed(2) + '%"></i></div></div>' +
        '<div class="jv-num">' + numeros(j, gp, gc) + '</div></div>'; }).join('') +
      (lista.length > TOP ? '<button class="pt-mais" type="button">' + (todos ? 'Ver só os ' + TOP + ' primeiros' : 'Ver todos os ' + lista.length + ' clubes') + '</button>' : '');
  }
  box.addEventListener('click', ev => { if (ev.target.closest('.pt-mais')) { todos = !todos; desenhar(); } });
  document.querySelectorAll('#gl-ordem button').forEach(b => b.addEventListener('click', () => { modo = b.dataset.modo; todos = false; desenhar(); if (window.glCorrida && modo !== 'media') window.glCorrida(modo); }));
  // Barras | Corrida: na corrida a média por jogo não vale; a métrica é Feitos, Tomados ou Saldo
  document.querySelectorAll('#gl-vista button').forEach(b => b.addEventListener('click', () => {
    const corrida = b.dataset.vista === 'corrida';
    document.querySelectorAll('#gl-vista button').forEach(x => x.classList.toggle('ativo', x === b));
    document.getElementById('gl-barras').hidden = corrida; document.getElementById('gl-corrida').hidden = !corrida;
    document.querySelector('#gl-ordem [data-modo=media]').hidden = corrida;
    if (corrida && modo === 'media') { modo = 'feitos'; desenhar(); }
    if (corrida && window.glCorrida) window.glCorrida(modo);
  }));
  document.addEventListener('tema-mudou', desenhar);
  desenhar();
})();
// ---- pontuação histórica: vitória 3, empate 1; barra do tamanho dos pontos possíveis (3 por jogo) ----
(() => {
  const box = document.getElementById('pontos'); if (!box) return;
  const TOP = 30, MIN = 100;   // no aproveitamento, só clubes com MIN jogos ou mais
  const pts = x => 3 * x[2] + x[3], nome = (a, b) => a[0].localeCompare(b[0], 'pt-BR');
  const ORDEM = {
    pontos: [...VIT].sort((a, b) => pts(b) - pts(a) || a[1] - b[1] || nome(a, b)),
    aprov: VIT.filter(x => x[1] >= MIN).sort((a, b) => pts(b) / b[1] - pts(a) / a[1] || pts(b) - pts(a)),
  };
  const maxP = Math.max(...VIT.map(x => 3 * x[1]));
  const corBarra = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  const fmtN = n => n.toLocaleString('pt-BR'), aprov = (p, j) => (100 * p / (3 * j)).toFixed(1).replace('.', ',') + '%';
  let modo = 'pontos', todos = false;
  const numeros = (j, p) => modo === 'pontos'
    ? '<b>' + fmtN(p) + '</b> <span>pontos</span><small>' + aprov(p, j) + ' de aproveitamento · ' + fmtN(j) + ' jogos</small>'
    : '<b>' + aprov(p, j) + '</b> <span>de aproveitamento</span><small>' + fmtN(p) + ' de ' + fmtN(3 * j) + ' pontos possíveis</small>';
  function desenhar() {
    const lista = ORDEM[modo];
    document.querySelectorAll('#pn-ordem button').forEach(b => b.classList.toggle('ativo', b.dataset.modo === modo));
    document.getElementById('pn-nota').textContent = modo === 'aprov' ? ' · no aproveitamento, só clubes com ' + MIN + ' jogos ou mais (' + lista.length + ')' : '';
    box.innerHTML = (todos ? lista : lista.slice(0, TOP)).map(([c, j, v, e, d], k) => { const [c1, c2] = cor(c), p = 3 * v + e, t = 3 * j;
      const dica = '<b>' + esc(c) + '</b><br>' + fmtN(p) + ' pontos em ' + fmtN(j) + ' jogos (' + aprov(p, j) + ')<br>' +
        fmtN(v) + ' vitórias × 3 = ' + fmtN(3 * v) + '<br>' + fmtN(e) + ' empates × 1 = ' + fmtN(e) + '<br>' + fmtN(t - p) + ' pontos perdidos';
      return '<div class="jv-linha"><div class="clube">' + (ESCUDOS[c] ? '<img class="escudo" alt="" src="' + ESCUDOS[c] + '" style="--c1:' + c1 + '">'
        : '<span class="bola" style="background:linear-gradient(90deg,' + c1 + ' 0 55%,' + c2 + ' 55%)"></span>') + '<span>' + esc(c) + '</span></div>' +
        '<div class="jv-area" data-dica="' + esc(dica) + '"><div class="jv-jogos" style="width:' + (100 * t / maxP).toFixed(2) + '%;--c:' + corBarra(c) + ';animation-delay:' + Math.min(k * 15, 450) + 'ms">' +
        '<i class="v" style="width:' + (100 * 3 * v / t).toFixed(2) + '%"></i><i class="e" style="width:' + (100 * e / t).toFixed(2) + '%"></i>' +
        '<i class="d" style="width:' + (100 * (t - p) / t).toFixed(2) + '%"></i></div></div>' +
        '<div class="jv-num">' + numeros(j, p) + '</div></div>'; }).join('') +
      (lista.length > TOP ? '<button class="pt-mais" type="button">' + (todos ? 'Ver só os ' + TOP + ' primeiros' : 'Ver todos os ' + lista.length + ' clubes') + '</button>' : '');
  }
  box.addEventListener('click', ev => { if (ev.target.closest('.pt-mais')) { todos = !todos; desenhar(); } });
  document.querySelectorAll('#pn-ordem button').forEach(b => b.addEventListener('click', () => { modo = b.dataset.modo; todos = false; desenhar(); }));
  // Barras | Corrida: na corrida o aproveitamento não vale; corre só o total de pontos
  document.querySelectorAll('#pn-vista button').forEach(b => b.addEventListener('click', () => {
    const corrida = b.dataset.vista === 'corrida';
    document.querySelectorAll('#pn-vista button').forEach(x => x.classList.toggle('ativo', x === b));
    document.getElementById('pn-barras').hidden = corrida; document.getElementById('pn-corrida').hidden = !corrida;
    document.getElementById('pn-ordem').hidden = corrida;
    if (corrida && window.pnCorrida) window.pnCorrida();
  }));
  document.addEventListener('tema-mudou', desenhar);
  desenhar();
})();
// ---- estatísticas e curiosidades: recordes em cartões, em quatro partes (Jogos | Clubes | Campeões | Edições) ----
(() => {
  const box = document.getElementById('curiosidades'); if (!box) return;
  const fmtN = n => n.toLocaleString('pt-BR'), pct = x => (100 * x).toFixed(1).replace('.', ',') + '%', dec = x => x.toFixed(2).replace('.', ',');
  const pl = (n, um, varios) => fmtN(n) + ' ' + (n === 1 ? um : varios), sinal = n => (n > 0 ? '+' : n < 0 ? '−' : '') + fmtN(Math.abs(n));
  const escudo = (c, p) => ESCUDOS[c] ? '<img class="cu-esc' + (p ? ' p' : '') + '" alt="" src="' + ESCUDOS[c] + '" data-dica="' + esc(esc(c)) + '">'
    : '<span class="cu-esc' + (p ? ' p' : '') + '" style="background:' + cor(c)[0] + '" data-dica="' + esc(esc(c)) + '"></span>';
  const cartao = (rot, corpo, det) => '<div class="cu-card"><span class="cu-rot">' + rot + '</span>' + corpo + '<small>' + det + '</small></div>';
  const jogo = j => '<div class="cu-jogo">' + escudo(j.m) + '<b>' + j.gm + ' × ' + j.gv + '</b>' + escudo(j.v) + '</div>';
  const um = (c, num, txt) => '<div class="cu-um">' + (c ? escudo(c) : '') + '<b>' + num + '</b><span>' + txt + '</span></div>';
  const varios = (cs, num, txt) => '<div class="cu-um">' + cs.map(c => escudo(c)).join('') + '<b>' + num + '</b><span>' + txt + '</span></div>';
  const nomeJogo = j => '<b>' + esc(j.m) + '</b> × <b>' + esc(j.v) + '</b> · ' + j.ano;
  const B = c => '<b>' + esc(c) + '</b>';
  const campanha = x => x.j + ' jogos: ' + pl(x.v, 'vitória', 'vitórias') + ', ' + pl(x.e, 'empate', 'empates') + ', ' + pl(x.d, 'derrota', 'derrotas');
  const edicao = x => anoT(x) + (x.comp ? ' · ' + x.comp : '');
  const cartoes = xs => '<div class="cu-cartoes">' + xs.filter(Boolean).join('') + '</div>';
  const bloco = (titulo, html, largo) => '<div class="cu-bloco' + (largo ? ' largo' : '') + '"><h3>' + titulo + '</h3>' + html + '</div>';
  // linhas com barra e escudos (títulos por estado, campeões por década)
  const linhas = (rows, dica) => { const mx = Math.max(...rows.map(r => r[1]));
    return rows.map(([rot, n, cs]) => '<div class="cu-uf"><b>' + rot + '</b><div class="meio"><div class="trilho-uf" style="width:' + (55 * n / mx) + '%"></div>' +
      '<div class="esc">' + cs.map(([c, k]) => '<span data-dica="' + esc(dica(c, k)) + '">' + escudo(c, true).replace(/ data-dica="[^"]*"/, '') + '</span>').join('') + '</div></div>' +
      '<span class="n">' + n + '</span></div>').join(''); };

  const JG = CUR.jogos, CL = CUR.clubes, CP = CUR.campeoes, ED_ = CUR.edicoes;
  function parteJogos() {
    const g = JG.goleada, fr = JG.freguesia, nf = fr.v + fr.e + fr.d;
    const cards = [
      cartao('Maior goleada', jogo(g), nomeJogo(g) + (g.tb.length ? '<br>também por ' + Math.abs(g.gm - g.gv) + ' gols: ' +
        g.tb.map(j => esc(j.m) + ' ' + j.gm + ' × ' + j.gv + ' ' + esc(j.v) + ' (' + j.ano + ')').join(', ') : '')),
      cartao('Maior goleada fora de casa', jogo(JG.fora), nomeJogo(JG.fora)),
      cartao('Jogo com mais gols', jogo(JG.mais_gols), nomeJogo(JG.mais_gols) + ' · <b>' + (JG.mais_gols.gm + JG.mais_gols.gv) + ' gols</b>'),
      cartao('Empate com mais gols', jogo(JG.empates[0]), JG.empates.map(nomeJogo).join('<br>')),
      cartao('Confronto mais repetido', '<div class="cu-um"><b>' + fmtN(JG.confrontos[0].va + JG.confrontos[0].e + JG.confrontos[0].vb) + '</b><span>jogos entre os mesmos dois clubes</span></div>' +
        JG.confrontos.map(x => '<div class="cu-par">' + escudo(x.a, true) + '<b>' + x.va + '</b> × <b>' + x.vb + '</b>' + escudo(x.b, true) + pl(x.e, 'empate', 'empates') + '</div>').join(''),
        JG.confrontos.map(x => B(x.a) + ' × ' + B(x.b)).join('<br>')),
      cartao('Maior freguesia', '<div class="cu-jogo">' + escudo(fr.a) + '<b>' + fr.v + ' × ' + fr.d + '</b>' + escudo(fr.b) + '</div>',
        B(fr.a) + ' venceu ' + fr.v + ' e perdeu ' + fr.d + ' dos ' + nf + ' jogos contra o ' + B(fr.b) + ' (' + pl(fr.e, 'empate', 'empates') + ') · entre confrontos com ' + fr.min + ' jogos ou mais'),
    ];
    const [m, e, v] = JG.mando;
    const mando = '<div class="cu-mando"><i class="m" style="width:' + 100 * m + '%">' + pct(m) + '</i><i class="e" style="width:' + 100 * e + '%">' + pct(e) + '</i><i class="v" style="width:' + 100 * v + '%">' + pct(v) + '</i></div>' +
      '<div class="cu-mando-leg"><span>vitória do mandante</span><span>empate</span><span>vitória do visitante</span></div>';
    // placares: linha = gols do mandante, coluna = gols do visitante
    const q = {}; let maxQ = 0; for (const [a, b, n] of JG.placar) { q[a + 'x' + b] = n; maxQ = Math.max(maxQ, n); }
    const top3 = JG.placar.slice().sort((x, y) => y[2] - x[2]).slice(0, 3).map(([a, b]) => a + 'x' + b);
    let placar = '<span></span>' + [0, 1, 2, 3, 4, 5].map(b => '<span>' + b + '</span>').join('');
    for (let a = 0; a <= 5; a++) { placar += '<span>' + a + '</span>';
      for (let b = 0; b <= 5; b++) { const n = q[a + 'x' + b] || 0;
        placar += '<i class="' + (top3.includes(a + 'x' + b) ? 'top' : '') + '" style="--a:' + Math.round(85 * n / maxQ) + '%" data-dica="' + esc('<b>' + a + ' × ' + b + '</b><br>' + fmtN(n) + ' jogos (' + pct(n / JG.n) + ')') + '">' +
          a + '×' + b + '<small>' + pct(n / JG.n) + '</small></i>'; } }
    return cartoes(cards) + '<div class="cu-grade">' + bloco('Mando de campo · ' + fmtN(JG.n) + ' jogos', mando) +
      bloco('Placares mais comuns · mandante × visitante', '<div class="cu-placar">' + placar + '</div>') + '</div>';
  }
  function parteClubes() {
    const x = CL, lt = x.lanterna, ltTit = lt.c.filter(c => ED.some(e => e.campeao === c || e.co === c));
    return cartoes([
      cartao('Mais temporadas seguidas', um(x.seguidas.c, x.seguidas.n, 'temporadas sem faltar'), B(x.seguidas.c) + ' · de ' + x.seguidas.de + ' a ' + x.seguidas.ate),
      cartao('Mais edições sem título', um(x.sem_titulo.c, x.sem_titulo.n, 'edições sem ser campeão'), B(x.sem_titulo.c)),
      cartao('Mais vitórias numa edição', um(x.vit.c, x.vit.v, 'vitórias em ' + x.vit.j + ' jogos'), B(x.vit.c) + ' · ' + x.vit.ano),
      cartao('Mais gols numa edição', um(x.gols.c, x.gols.gp, 'gols em ' + x.gols.j + ' jogos'), B(x.gols.c) + ' · ' + x.gols.ano),
      cartao('Melhor saldo numa edição', um(x.saldo.c, sinal(x.saldo.gp - x.saldo.gc), 'de saldo'), B(x.saldo.c) + ' · ' + x.saldo.ano + ' · ' + x.saldo.gp + ' feitos, ' + x.saldo.gc + ' sofridos'),
      cartao('Melhor defesa numa edição', um(x.defesa.c, x.defesa.gc, 'gols sofridos em ' + x.defesa.j + ' jogos'), B(x.defesa.c) + ' · ' + x.defesa.ano + ' · ' + dec(x.defesa.gc / x.defesa.j) + ' por jogo · entre campanhas de ' + x.defesa.min + ' jogos ou mais'),
      cartao('Mais derrotas numa edição', um(x.der.c, x.der.d, 'derrotas em ' + x.der.j + ' jogos'), B(x.der.c) + ' · ' + x.der.ano),
      cartao('Pior campanha', um(x.pior.c, pct(x.pior.ap), 'de aproveitamento'), B(x.pior.c) + ' · ' + x.pior.ano + ' · ' + campanha(x.pior)),
      cartao('Mais vezes em último', varios(lt.c, lt.n, 'vezes lanterna'),
        lt.c.map(c => B(c) + (ltTit.includes(c) ? ' · e também já foi campeão (' + ED.filter(e => e.campeao === c || e.co === c).map(e => e.ano).join(', ') + ')' : '')).join('<br>')),
      cartao('Maior tempo fora', um(x.volta.c, x.volta.n, 'anos sem jogar'), B(x.volta.c) + ' · jogou em ' + x.volta.de + ' e só voltou em ' + x.volta.ate),
      cartao('Uma vez e nunca mais', um(null, x.uma_vez, 'clubes jogaram uma só edição'), 'de ' + Object.keys(PART).length + ' clubes que já disputaram ' + CONF.o),
    ]);
  }
  function parteCampeoes() {
    const x = CP, inv = x.invictos;
    return cartoes([
      cartao('Mais títulos seguidos', um(x.seq.c, x.seq.n, 'títulos seguidos'), B(x.seq.c) + ' · de ' + x.seq.de + ' a ' + x.seq.ate),
      cartao('Maior jejum entre títulos', um(x.jejum.c, x.jejum.n, 'anos de espera'), B(x.jejum.c) + ' · campeão em ' + x.jejum.de + ' e de novo só em ' + x.jejum.ate),
      cartao(inv.length === 1 ? 'Campeão invicto' : 'Campeões invictos', varios(inv.map(i => i.c), inv.map(i => i.ano).join(', '), ''), inv.map(i => B(i.c) + ' · ' + campanha(i)).join('<br>')),
      cartao('Melhor campanha de campeão', um(x.melhor.c, pct(x.melhor.ap), 'de aproveitamento'), B(x.melhor.c) + ' · ' + x.melhor.ano + ' · ' + campanha(x.melhor)),
      cartao('Pior campanha de campeão', um(x.pior.c, pct(x.pior.ap), 'de aproveitamento'), B(x.pior.c) + ' · ' + x.pior.ano + ' · ' + campanha(x.pior)),
      x.pontos && cartao('Campeão com mais pontos', um(x.pontos.c, x.pontos.pts, 'pontos em ' + x.pontos.j + ' jogos'), B(x.pontos.c) + ' · ' + x.pontos.ano + ' · pontos corridos'),
      x.pontos20 && cartao('Mais pontos com 20 clubes', um(x.pontos20.c, x.pontos20.pts, 'pontos em ' + x.pontos20.j + ' jogos'), B(x.pontos20.c) + ' · ' + x.pontos20.ano + ' · desde ' + x.pc20_desde),
      x.vantagem && cartao('Maior vantagem sobre o vice', um(x.vantagem.c, x.vantagem.vant, 'pontos à frente'), B(x.vantagem.c) + ' · ' + x.vantagem.ano + ' · vice: ' + B(x.vantagem.vice)),
      x.apertados.length > 0 && cartao('Título mais apertado', varios(x.apertados.map(a => a.c), x.apertados[0].vant, x.apertados[0].vant === 0 ? 'empate em pontos' : x.apertados[0].vant === 1 ? 'ponto à frente' : 'pontos à frente'),
        x.apertados.map(a => B(a.c) + ' · ' + a.ano + ' · vice: ' + B(a.vice)).join('<br>') + '<br>pontos corridos, desde ' + x.pc_desde),
      cartao('Vices sem nenhum título', '<div class="cu-um"><b>' + x.vices_sem.length + '</b><span>clubes chegaram<br>perto e pararam</span></div>',
        '<div class="cu-escudos">' + x.vices_sem.map(([c]) => escudo(c, true)).join('') + '</div>' + x.vices_sem.map(([c, q]) => esc(c) + (q > 1 ? ' (' + q + ')' : '')).join(', ')),
    ]) + '<div class="cu-grade">' +
      (x.uf.length ? bloco('Títulos por estado', linhas(x.uf, (c, k) => '<b>' + esc(c) + '</b>: ' + pl(k, 'título', 'títulos'))) : '') +
      bloco('Campeões diferentes por década', linhas(x.decadas.map(([d, n, cs]) => [d + 's', n, cs]), c => '<b>' + esc(c) + '</b>')) + '</div>';
  }
  function parteEdicoes() {
    const x = ED_;
    const cards = [
      cartao('Edição com mais clubes', um(null, x.mais_clubes.n, 'clubes'), edicao(x.mais_clubes)),
      cartao('Edição com menos clubes', um(null, x.menos_clubes.n, 'clubes'), edicao(x.menos_clubes)),
      cartao('Edição com mais jogos', um(null, fmtN(x.mais_jogos.j), 'jogos'), edicao(x.mais_jogos)),
      cartao('Edição com mais gols', um(null, fmtN(x.mais_gols.g), 'gols'), edicao(x.mais_gols) + ' · ' + dec(x.mais_gols.g / x.mais_gols.j) + ' por jogo'),
      cartao('Edição com menos jogos', um(null, fmtN(x.menos_jogos.j), 'jogos'), edicao(x.menos_jogos)),
      cartao('Mais clubes estreando', um(null, x.estreantes.est, 'estreantes'), edicao(x.estreantes) + ' · de ' + x.estreantes.n + ' clubes'),
      x.duplos.length > 0 && cartao('Anos com dois campeões', '<div class="cu-um"><b>' + x.duplos.length + '</b><span>anos tiveram duas<br>edições ao mesmo tempo</span></div>',
        x.duplos.map(([a, cs]) => '<b>' + a + '</b>: ' + (new Set(cs).size === 1 ? esc(cs[0]) + ' ganhou as duas' : cs.map(c => esc(c)).join(' e '))).join('<br>')),
      x.formatos.length > 1 && cartao('Formatos da disputa', '<div class="cu-um"><b>' + x.formatos.length + '</b><span>nomes de torneio<br>na história</span></div>',
        x.formatos.map(([c, q]) => '<b>' + esc(c) + '</b>: ' + pl(q, 'edição', 'edições')).join('<br>')),
    ];
    // gols por jogo em cada edição (as duas pontas em dourado)
    // edição só com a tabela final (sem jogos) fica de fora do gráfico
    const E = x.por_ed.filter(e => e.j > 0).map(e => ({ ...e, m: e.g / e.j })), W = 1000, H = 230, ML = 34, MR = 10, MT = 26, MB = 26;
    const maxM = Math.ceil(Math.max(...E.map(e => e.m))), bw = (W - ML - MR) / E.length;
    const Yg = m => H - MB - m / maxM * (H - MT - MB);
    const iMax = E.reduce((a, e, i) => e.m > E[a].m ? i : a, 0), iMin = E.reduce((a, e, i) => e.m < E[a].m ? i : a, 0);
    const media = E.reduce((a, e) => a + e.g, 0) / E.reduce((a, e) => a + e.j, 0);
    let svg = '';
    for (let m = 0; m <= maxM; m++) svg += '<line class="cr-grade" x1="' + ML + '" x2="' + (W - MR) + '" y1="' + Yg(m) + '" y2="' + Yg(m) + '"/><text class="cr-eixo" x="' + (ML - 8) + '" y="' + (Yg(m) + 4) + '" text-anchor="end">' + m + '</text>';
    E.forEach((e, i) => {
      const cls = i === iMax ? ' max' : i === iMin ? ' min' : '';
      svg += '<rect class="cu-barra-g' + cls + '" x="' + (ML + i * bw + 1) + '" y="' + Yg(e.m) + '" width="' + (bw - 2) + '" height="' + (H - MB - Yg(e.m)) + '" rx="2" data-dica="' +
        esc('<b>' + edicao(e) + '</b><br>' + dec(e.m) + ' gols por jogo<br>' + fmtN(e.g) + ' gols em ' + fmtN(e.j) + ' jogos · ' + e.n + ' clubes') + '"/>';
      if (i === 0 || (e.ano % 10 === 0 && E[i - 1].ano % 10 !== 0 && i > 3)) svg += '<text class="cr-eixo" x="' + (ML + i * bw + bw / 2) + '" y="' + (H - 6) + '" text-anchor="middle">' + e.ano + '</text>';
      if (cls) svg += '<text class="cu-txt" x="' + (ML + i * bw + bw / 2) + '" y="' + (Yg(e.m) - 7) + '" text-anchor="' + (i < 3 ? 'start' : 'middle') + '">' + dec(e.m) + ' em ' + e.ano + '</text>';
    });
    svg += '<line class="cu-media" x1="' + ML + '" x2="' + (W - MR) + '" y1="' + Yg(media) + '" y2="' + Yg(media) + '"/><text class="cu-txt" x="' + (W - MR) + '" y="' + (Yg(media) - 6) + '" text-anchor="end">média ' + dec(media) + '</text>';
    return cartoes(cards) + '<div class="cu-grade">' + bloco('Gols por jogo em cada edição', '<svg id="cu-gols" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Gols por jogo em cada edição">' + svg + '</svg>', true) + '</div>';
  }
  const PARTES = { jogos: parteJogos, clubes: parteClubes, campeoes: parteCampeoes, edicoes: parteEdicoes };
  const bs = document.querySelectorAll('#cu-parte button');
  const abrir = k => { bs.forEach(b => b.classList.toggle('ativo', b.dataset.parte === k)); box.innerHTML = PARTES[k](); };
  bs.forEach(b => b.addEventListener('click', () => abrir(b.dataset.parte)));
  abrir('jogos');
})();
// ---- por campeonato: escolhe a edição (lista ou setas) e vê números, pódio e classificação final ----
(() => {
  const sel = document.getElementById('cp-sel'); if (!sel) return;
  const IDX = Object.fromEntries(EDS.map((e, i) => [e.id, i])), TOP = 20;
  const fmtN = n => n.toLocaleString('pt-BR');
  const sinal = n => (n > 0 ? '+' : n < 0 ? '−' : '') + fmtN(Math.abs(n));
  const escudo = (c, cls) => ESCUDOS[c] ? '<img class="cp-esc' + (cls ? ' ' + cls : '') + '" alt="" src="' + ESCUDOS[c] + '">'
    : '<span class="cp-esc' + (cls ? ' ' + cls : '') + '" style="background:linear-gradient(90deg,' + cor(c)[0] + ' 0 55%,' + cor(c)[1] + ' 55%)"></span>';
  const MEDIA = EDS.reduce((a, e) => a + e.g, 0) / EDS.reduce((a, e) => a + e.j, 0);
  // lista por década, da mais nova para a mais antiga
  const dec10 = {}; EDS.forEach(e => (dec10[Math.floor(e.ano / 10) * 10] = dec10[Math.floor(e.ano / 10) * 10] || []).push(e));
  sel.innerHTML = Object.keys(dec10).sort((a, b) => b - a).map(d => '<optgroup label="Anos ' + d + '">' +
    dec10[d].slice().reverse().map(e => '<option value="' + e.id + '">' + anoT(e) + ' · ' + esc(e.nome) + '</option>').join('') + '</optgroup>').join('');
  let atual = EDS[EDS.length - 1].id, todos = false;
  const dec = x => x.toFixed(2).replace('.', ',');
  const kpi = (v, rot, sub) => '<div class="kpi"><b>' + v + '</b><span>' + rot + '</span><small>' + sub + '</small></div>';
  function mostrar(id) {
    if (id !== atual) { todos = false; grupoJ = EDS[IDX[id]].grupos.length - 1; }
    atual = id; sel.value = id; if (sel.sincronizar) sel.sincronizar();
    const i = IDX[id], e = EDS[i], g = e.gol, t = e.tab, tp = t.filter(r => r[1] != null), pts = r => r[10] ? (r[9] ?? '—') : ptsE(e, r[3], r[4], r[5]) + (r[8] || 0);   // r[8]: punição/bônus; r[10]: linha parcial da fonte; tp: sem quem jogou e ficou fora da classificação
    document.getElementById('cp-ant').disabled = i === 0; document.getElementById('cp-prox').disabled = i === EDS.length - 1;
    document.getElementById('cp-titulo').textContent = anoT(e) + ' · ' + e.nome;
    document.getElementById('cp-cartoes').innerHTML = [
      kpi(t.length, 'Clubes', t.length > tp.length ? (t.length - tp.length) + ' sem posição na fonte' : 'na classificação final'),
      kpi(e.est, 'Estreantes', e.est === 1 ? 'clube pela 1ª vez' : 'clubes pela 1ª vez'),
      e.j ? kpi(fmtN(e.j), 'Jogos', e.inc ? 'registrados (a fonte não tem todos)' : 'partidas disputadas') : kpi('—', 'Jogos', 'só a tabela final desta edição'),
      kpi(e.j ? fmtN(e.g) : '—', 'Gols', e.inc ? 'nos jogos registrados' : 'marcados na edição'),
      kpi(e.j ? dec(e.g / e.j) : '—', 'Gols por jogo', 'média da história: ' + dec(MEDIA)),
      g ? kpi(g.gm + ' × ' + g.gv, 'Maior goleada', esc(g.m) + ' × ' + esc(g.v)) : kpi('—', 'Maior goleada', 'sem jogos nesta edição'),
      e.mata ? kpi(e.disputa.length, e.disputa.length === 1 ? 'Fase' : 'Fases', 'na edição') : kpi(e.pv, 'Pontos por vitória', 'empate vale ' + (e.pe ?? 1) + (e.pd ? ', derrota ' + e.pd : '')),
    ].join('');
    const nota = document.getElementById('cp-nota'); nota.textContent = e.nota; nota.hidden = !e.nota;
    // pódio: 2º, 1º, 3º
    const cl = (r, k) => r ? '<div class="pd pd' + k + '">' + escudo(r[0]) + '<b>' + esc(r[0]) + '</b><small>' + (r[10] ? (r[9] != null ? r[9] + ' pontos' : '') : r[3] + ' V · ' + r[4] + ' E · ' + r[5] + ' D') + '</small><div class="degrau">' + k + 'º</div></div>' : '';
    // título dividido (D-07): os dois campeões no degrau do meio; quem vem depois sobe uma posição
    const co = e.co ? tp.find(r => r[0] === e.co) : null, resto = tp.filter(r => r !== co), med = new Map(resto.slice(0, 3).map((r, k) => [r[0], k + 1]));
    if (co) med.set(co[0], 1);
    document.getElementById('cp-podio').innerHTML = co ? '<div class="podio dividido">' + cl(resto[1], 2) + cl(resto[0], 1) + cl(co, 1) + cl(resto[2], 3) + '</div>'
      : '<div class="podio">' + cl(tp[1], 2) + cl(tp[0], 1) + cl(tp[2], 3) + '</div>';
    // classificação final
    const linhas = (todos ? t : t.slice(0, TOP)).map(r => { const [c, pos] = r, [J, V, E, D, GP, GC] = r[10] ? Array(6).fill('—') : r.slice(2, 8), sg = r[10] ? NaN : GP - GC;
      return '<tr class="' + (co ? (med.has(c) ? 'p' + med.get(c) : '') : pos != null && pos <= 3 ? 'p' + pos : '') + '"><td class="pos">' + (pos == null ? '—' : pos + 'º') + '</td><td class="clube"><a class="cl-link" href="#clube/resumo/' + slugClube(c) + '">' + escudo(c) + esc(c) + '</a></td>' +
        (semPts(e) ? '' : '<td class="pts">' + pts(r) + '</td>') + '<td>' + J + '</td><td>' + V + '</td><td>' + E + '</td><td>' + D + '</td><td class="gpgc">' + GP + '</td><td class="gpgc">' + GC + '</td>' +
        '<td class="' + (sg < 0 ? 'neg' : '') + '">' + (isNaN(sg) ? '—' : sinal(sg)) + '</td></tr>'; }).join('');
    document.getElementById('cp-tabela').innerHTML = '<div class="cp-rolar"><table class="cp-tab"><thead><tr><th></th><th>Clube</th>' + (semPts(e) ? '' : '<th title="vitória = ' + e.pv + ' pontos">Pts</th>') +
      '<th>J</th><th>V</th><th>E</th><th>D</th><th class="gpgc">GP</th><th class="gpgc">GC</th><th>SG</th></tr></thead><tbody>' + linhas + '</tbody></table></div>' +
      (t.length > TOP ? '<button class="pt-mais" type="button">' + (todos ? 'Ver só os ' + TOP + ' primeiros' : 'Ver todos os ' + t.length + ' clubes') + '</button>' : '');
    resumo(e); participantes(e); jogos(e); duelo(e); corrida(e); artilharia(e);
  }
  // ---- Resumo: destaques e como foi a disputa
  const escP = (c, p) => ESCUDOS[c] ? '<img class="cu-esc' + (p ? ' p' : '') + '" alt="" src="' + ESCUDOS[c] + '">'
    : '<span class="cu-esc' + (p ? ' p' : '') + '" style="background:' + cor(c)[0] + '"></span>';
  const cartao = (rot, corpo, det) => '<div class="cu-card"><span class="cu-rot">' + rot + '</span>' + corpo + '<small>' + det + '</small></div>';
  const um = (c, num, txt) => '<div class="cu-um">' + (c ? escP(c) : '') + '<b>' + num + '</b><span>' + txt + '</span></div>';
  const pct = x => (100 * x).toFixed(1).replace('.', ',') + '%';
  const melhor = (t, f) => t.reduce((a, r) => f(r) > f(a) ? r : a);   // primeiro na classificação vence o empate
  const TIPO = { liga: 'pontos corridos', grupo: 'grupos', grupos: 'grupos', mata_mata: 'mata-mata' };
  const SERIE = { ida_volta: 'ida e volta', jogo_unico: 'jogo único', pontos_corridos: 'turno e returno', grupos: '' };
  // ---- Participantes: estreantes, veteranos, de onde cada clube chegou e para onde foi
  const NV = n => CONF.niveis[n] || ('divisão ' + n);
  function participantes(e) {
    const i = IDX[e.id], N = CONF.nivel, t = e.tab, mv = e.mv || t.map(() => [null, null]);
    const vezes = c => (PART[c] || []).filter(([k]) => k <= i).length;
    const linhas = t.map((r, k) => ({ c: r[0], pos: r[1], n: vezes(r[0]), veio: mv[k][0],
      foi: e.ac && mv[k][1] && mv[k][1] < N && !e.ac.includes(r[0]) ? N : mv[k][1] }));   // subir só com acesso oficial, quando a fonte diz
    const lista = (xs, txt) => xs.length ? '<div class="cu-escudos">' + xs.map(x => escP(x.c, true)).join('') + '</div>' + xs.map(x => esc(x.c) + (txt ? txt(x) : '')).join(', ') : '';
    const grupo = (rot, xs, num, det, txt) => xs.length ? cartao(rot, um(null, num ?? xs.length, det), lista(xs, txt)) : '';
    const est = linhas.filter(x => x.n === 1), maxN = Math.max(...linhas.map(x => x.n));
    const vet = linhas.filter(x => x.n === maxN);
    if (N === null) return participantesCopa(e, linhas, est, vet, maxN, lista, grupo);
    document.getElementById('cpp-cartoes').innerHTML = '<div class="cu-cartoes">' + [
      grupo('Estreantes', est, null, est.length === 1 ? 'clube pela 1ª vez' : 'clubes pela 1ª vez'),
      maxN > 1 ? grupo(vet.length === 1 ? 'Mais veterano' : 'Mais veteranos', vet, maxN + 'ª', 'participação') : '',
      grupo('Caíram da ' + NV(N - 1), linhas.filter(x => x.veio && x.veio < N), null, 'rebaixados no ano anterior'),
      grupo('Subiram da ' + NV(N + 1), linhas.filter(x => x.veio && x.veio > N), null, 'promovidos no ano anterior'),
      grupo('Subiram para a ' + NV(N - 1), linhas.filter(x => x.foi && x.foi < N), null, 'no ano seguinte', x => ' (' + x.pos + 'º)'),
      grupo('Caíram para a ' + NV(N + 1), linhas.filter(x => x.foi && x.foi > N), null, 'no ano seguinte', x => ' (' + x.pos + 'º)'),
    ].join('') + '</div>';
    // texto inteiro e, no celular, curto: '↓ caiu da Série A' vira '↓ Série A'; 'já estava' e 'ficou' viram '='
    const dois = (longo, curto) => '<span class="longo">' + longo + '</span><span class="curto">' + curto + '</span>';
    const seta = (v, de) => v === null ? '' : v === 0 ? '<span class="mv fora" title="não jogou nenhuma série do banco em ' + (e.ano + (de ? -1 : 1)) + '">—</span>'
      : v === N ? '<span class="mv">' + dois(de ? 'já estava' : 'ficou', '=') + '</span>'
      : (v < N) === de ? '<span class="mv cai">' + dois('↓ ' + (de ? 'caiu da ' : 'caiu para a ') + NV(v), '↓ ' + NV(v)) + '</span>'
      : '<span class="mv sobe">' + dois('↑ ' + (de ? 'subiu da ' : 'subiu para a ') + NV(v), '↑ ' + NV(v)) + '</span>';
    document.getElementById('cpp-tabela').innerHTML = '<div class="cp-rolar"><table class="cp-tab cpp-tab"><thead><tr><th></th><th>Clube</th><th><span class="longo">Participação</span><span class="curto">Nº</span></th><th>Chegou</th><th><span class="longo">No ano seguinte</span><span class="curto">Depois</span></th></tr></thead><tbody>' +
      linhas.map(x => '<tr class="' + (x.pos <= 3 ? 'p' + x.pos : '') + '"><td class="pos">' + x.pos + 'º</td><td class="clube"><a class="cl-link" href="#clube/resumo/' + slugClube(x.c) + '">' + escudo(x.c) + esc(x.c) + '</a></td>' +
        '<td><b class="' + (x.n === 1 ? 'n-novo' : x.n === maxN ? 'n-vet' : '') + '">' + x.n + 'ª</b><span class="longo">' + (x.n === 1 ? ' <span class="mv novo">estreia</span>' : x.n === maxN ? ' <span class="mv vet">mais veterano</span>' : '') + '</span></td>' +
        '<td>' + seta(x.veio, true) + '</td><td>' + seta(x.foi, false) + '</td></tr>').join('') + '</tbody></table></div>';
  }
  // copa: em vez de subir e cair, a divisão em que cada clube jogava naquele ano
  function participantesCopa(e, linhas, est, vet, maxN, lista, grupo) {
    const div = v => v === null ? '' : v === 0 ? '<span class="mv fora">fora das séries</span>' : '<span class="mv">' + NV(v) + '</span>';
    const niveis = [...new Set(linhas.map(x => x.veio).filter(v => v !== null))].sort((a, b) => (a || 99) - (b || 99));
    document.getElementById('cpp-cartoes').innerHTML = '<div class="cu-cartoes">' + [
      grupo('Estreantes', est, null, est.length === 1 ? 'clube pela 1ª vez' : 'clubes pela 1ª vez'),
      maxN > 1 ? grupo(vet.length === 1 ? 'Mais veterano' : 'Mais veteranos', vet, maxN + 'ª', 'participação') : '',
      ...niveis.map(v => grupo(v ? 'Da ' + NV(v) : 'Fora das séries', linhas.filter(x => x.veio === v), null, 'no ano de ' + e.ano)),
    ].join('') + '</div>';
    document.getElementById('cpp-tabela').innerHTML = '<div class="cp-rolar"><table class="cp-tab cpp-tab"><thead><tr><th></th><th>Clube</th><th><span class="longo">Participação</span><span class="curto">Nº</span></th><th>Série no ano</th></tr></thead><tbody>' +
      linhas.map(x => '<tr class="' + (x.pos <= 3 ? 'p' + x.pos : '') + '"><td class="pos">' + x.pos + 'º</td><td class="clube"><a class="cl-link" href="#clube/resumo/' + slugClube(x.c) + '">' + escudo(x.c) + esc(x.c) + '</a></td>' +
        '<td><b class="' + (x.n === 1 ? 'n-novo' : x.n === maxN ? 'n-vet' : '') + '">' + x.n + 'ª</b><span class="longo">' + (x.n === 1 ? ' <span class="mv novo">estreia</span>' : x.n === maxN ? ' <span class="mv vet">mais veterano</span>' : '') + '</span></td>' +
        '<td>' + div(x.veio) + '</td></tr>').join('') + '</tbody></table></div>';
  }
  function resumo(e) {
    const t = e.tab, J = e.jogos, maxJ = Math.max(...t.map(r => r[2]));
    const ataque = melhor(t, r => r[6]), defesa = melhor(t.filter(r => r[2] >= maxJ / 2), r => -r[7] / r[2]);
    const vit = melhor(t, r => r[3]), emp = melhor(t, r => r[4]), lant = t[t.length - 1];
    const mais = J.length ? J.reduce((a, x) => x[3] + x[4] > a[3] + a[4] ? x : a, J[0]) : null;   // edição sem jogos: tabela anual
    const m = J.filter(x => x[3] > x[4]).length / J.length, em = J.filter(x => x[3] === x[4]).length / J.length;
    const pts = r => ptsE(e, r[3], r[4], r[5]) + (r[8] || 0), art = (e.artof && e.artof[0]) || (e.cob >= 0.9 ? e.art[0] : null);   // oficial; senão, só se quase todos os gols têm autor
    // melhor mandante e melhor visitante: maior aproveitamento jogando em casa / fora
    // (só quem fez pelo menos metade dos jogos do que mais jogou ali; empate, mais pontos)
    const lado = qual => { const c = t.map(() => [0, 0, 0]);   // jogos, vitórias, empates
      for (const [, mi, vi, gm, gv] of J) { const k = qual === 'm' ? mi : vi, a = qual === 'm' ? gm : gv, b = qual === 'm' ? gv : gm;
        c[k][0]++; if (a > b) c[k][1]++; else if (a === b) c[k][2]++; }
      const mx = Math.max(...c.map(x => x[0])), pt = x => ptsE(e, x[1], x[2], x[0] - x[1] - x[2]);
      let k = -1; c.forEach((x, i) => { if (x[0] < mx / 2) return;
        if (k < 0 || pt(x) / x[0] > pt(c[k]) / c[k][0] || (pt(x) / x[0] === pt(c[k]) / c[k][0] && pt(x) > pt(c[k]))) k = i; });
      const x = c[k]; return { c: t[k][0], j: x[0], v: x[1], e: x[2], d: x[0] - x[1] - x[2], pts: pt(x), ap: pt(x) / (e.pv * x[0]) }; };
    const casa = J.length ? lado('m') : null, fora = J.length ? lado('v') : null;
    const ladoCard = (rot, x, onde) => cartao(rot, um(x.c, x.pts, 'pontos ' + onde + ' em ' + x.j + ' jogos'),
      '<b>' + esc(x.c) + '</b> · ' + x.v + ' V · ' + x.e + ' E · ' + x.d + ' D · ' + pct(x.ap) + ' de aproveitamento');
    const cards = [
      cartao('Melhor ataque', um(ataque[0], ataque[6], 'gols em ' + ataque[2] + ' jogos'), '<b>' + esc(ataque[0]) + '</b> · ' + ataque[1] + 'º colocado'),
      cartao('Melhor defesa', um(defesa[0], defesa[7], 'gols sofridos em ' + defesa[2] + ' jogos'), '<b>' + esc(defesa[0]) + '</b> · ' + dec(defesa[7] / defesa[2]) + ' por jogo'),
      cartao('Mais vitórias', um(vit[0], vit[3], 'vitórias em ' + vit[2] + ' jogos'), '<b>' + esc(vit[0]) + '</b> · ' + vit[1] + 'º colocado'),
      cartao('Mais empates', um(emp[0], emp[4], 'empates em ' + emp[2] + ' jogos'), '<b>' + esc(emp[0]) + '</b> · ' + emp[1] + 'º colocado'),
      mais && cartao('Jogo com mais gols', '<div class="cu-jogo">' + escP(t[mais[1]][0]) + '<b>' + mais[3] + ' × ' + mais[4] + '</b>' + escP(t[mais[2]][0]) + '</div>',
        '<b>' + esc(t[mais[1]][0]) + '</b> × <b>' + esc(t[mais[2]][0]) + '</b> · ' + esc(e.grupos[mais[0]])),
      J.length > 0 && cartao('Mando de campo', '<div class="cu-mando"><i class="m" style="width:' + 100 * m + '%">' + pct(m) + '</i><i class="e" style="width:' + 100 * em + '%"></i><i class="v" style="width:' + 100 * (1 - m - em) + '%"></i></div>',
        'vitória do mandante · ' + pct(em) + ' de empates · ' + pct(1 - m - em) + ' vitória do visitante'),
      !e.mata && casa && ladoCard('Melhor mandante', casa, 'em casa'),
      !e.mata && fora && ladoCard('Melhor visitante', fora, 'fora'),
    ].filter(Boolean);
    if (e.cor) cards.push(cartao('Vantagem do campeão', um(t[0][0], pts(t[0]) - pts(t[1]), pts(t[0]) - pts(t[1]) === 1 ? 'ponto à frente' : 'pontos à frente'),
      '<b>' + esc(t[0][0]) + '</b> ' + pts(t[0]) + ' × ' + pts(t[1]) + ' <b>' + esc(t[1][0]) + '</b>'));
    if (art) cards.push(cartao('Artilheiro', um(art[1], art[2], 'gols'), '<b>' + esc(art[0]) + '</b> · ' + esc(art[1])));
    if (!e.mata) cards.push(cartao('Lanterna', um(lant[0], lant[1] + 'º', 'e último lugar'), '<b>' + esc(lant[0]) + '</b> · ' + lant[3] + ' V · ' + lant[4] + ' E · ' + lant[5] + ' D'));
    document.getElementById('cp-destaques').innerHTML = '<div class="cu-cartoes">' + cards.join('') + '</div>';
    document.getElementById('cp-disputa').innerHTML = '<ol class="cp-fases">' + e.disputa.map(([n, tp, sr, ng, nj, nc]) =>
      '<li><b>' + esc(n) + '</b><span>' + [TIPO[tp] || '', SERIE[sr] || '', ng > 1 ? ng + ' grupos' : '', nc + ' clubes', nj + (nj === 1 ? ' jogo' : ' jogos')].filter(Boolean).join(' · ') + '</span></li>').join('') + '</ol>';
  }
  // ---- Jogos: por rodada ou por fase
  const jsel = document.getElementById('cpj-sel');
  let grupoJ = 0;
  function jogos(e) {
    jsel.innerHTML = e.grupos.map((g, k) => '<option value="' + k + '">' + esc(g) + '</option>').join('');
    jsel.value = grupoJ; document.getElementById('cpj-ant').disabled = grupoJ === 0; document.getElementById('cpj-prox').disabled = grupoJ === e.grupos.length - 1;
    const t = e.tab, lado = (c, cls) => '<span class="' + cls + '">' + (cls === 'm' ? esc(c) + escP(c, true) : escP(c, true) + esc(c)) + '</span>';
    let sub = null, html = '';
    const lista = e.jogos.map(([g, mi, vi, ...r]) => [g, t[mi][0], t[vi][0], ...r]).concat(e.xj || []);   // xj: desempates, fora da tabela
    for (const [g, cm, cv, gm, gv, sg, pen] of lista) { if (g !== grupoJ) continue;
      if (sg !== sub) { if (sub !== null) html += '</div>'; html += (sg ? '<h3 class="cp-subgrupo">' + (/^grupo\b/i.test(sg) ? '' : 'Grupo ') + esc(sg) + '</h3>' : '') + '<div class="cp-jogos">'; sub = sg; }
      const [pm, pv] = pen ? pen.split('-').map(Number) : [0, 0], ganha = gm !== gv ? gm > gv : pm > pv;   // empate decidido nos pênaltis
      html += '<div class="cp-jogo' + (gm === gv && !pen ? '' : ganha ? ' vm' : ' vv') + '">' + lado(cm, 'm') + '<b>' + gm + ' × ' + gv +
        (pen ? '<small class="pen">pên. ' + pm + ' × ' + pv + '</small>' : '') + '</b>' + lado(cv, 'v') + '</div>'; }
    document.getElementById('cpj-lista').innerHTML = (html || '<p class="cp-nota">Sem jogos registrados.</p>') + (sub !== null ? '</div>' : '');
  }
  jsel.addEventListener('change', () => { grupoJ = +jsel.value; jogos(EDS[IDX[atual]]); });
  document.getElementById('cpj-ant').addEventListener('click', () => { if (grupoJ > 0) { grupoJ--; jogos(EDS[IDX[atual]]); } });
  document.getElementById('cpj-prox').addEventListener('click', () => { const e = EDS[IDX[atual]]; if (grupoJ < e.grupos.length - 1) { grupoJ++; jogos(e); } });
  // ---- Duelo: dois clubes, pontos de cada um contra cada adversário (na ordem da classificação final)
  const dlA = document.getElementById('dl-a'), dlB = document.getElementById('dl-b');
  let duA = null, duB = null;
  function duelo(e) {
    const t = e.tab, nomes = t.map(r => r[0]);
    const opts = t.map((r, k) => '<option value="' + k + '">' + (r[1] == null ? '—' : r[1] + 'º') + ' · ' + esc(r[0]) + '</option>').join('');
    dlA.innerHTML = opts; dlB.innerHTML = opts;
    if (!nomes.includes(duA)) duA = nomes[0];
    if (!nomes.includes(duB) || duB === duA) duB = nomes.find(c => c !== duA);
    const ia = nomes.indexOf(duA), ib = nomes.indexOf(duB);
    dlA.value = ia; dlB.value = ib;
    const res = document.getElementById('dl-resumo'), graf = document.getElementById('dl-grafico');
    if (!e.jogos.length || nomes.length < 2) { res.innerHTML = '<p class="cp-nota">Esta edição não tem jogos registrados, só a tabela final.</p>'; graf.innerHTML = ''; return; }
    const contra = eu => { const pts = {}, js = {};   // adversário -> pontos e a lista dos jogos
      for (const [g, mi, vi, gm, gv, sg, pen] of e.jogos) {
        if (gm == null || (mi !== eu && vi !== eu)) continue;
        const casa = mi === eu, adv = casa ? vi : mi, meus = casa ? gm : gv, deles = casa ? gv : gm;
        pts[adv] = (pts[adv] || 0) + (meus > deles ? e.pv : meus === deles ? (e.pe ?? 1) : (e.pd ?? 0));
        (js[adv] = js[adv] || []).push(meus + ' × ' + deles + (casa ? ' em casa' : ' fora') + (pen ? ' (pênaltis)' : '') + ' · ' + e.grupos[g]);
      }
      return [pts, js]; };
    const [pa, ja] = contra(ia), [pb, jb] = contra(ib);
    const advs = t.map((_, k) => k).filter(k => k !== ia && k !== ib && (ja[k] || jb[k]));
    const max = Math.max(1, ...advs.map(k => Math.max(pa[k] || 0, pb[k] || 0)), pa[ib] || 0, pb[ia] || 0);
    let cA = corDe(duA), cB = corDe(duB); if (cA === cB) cB = '#8a8f8a';
    const barra = (lado, quem, adv, pts, js, c) => js
      ? '<div class="dl-barra ' + lado + '" data-dica="' + esc('<b>' + quem + ' × ' + adv + '</b><br>' + js.join('<br>') + '<br><b>' + pts + (pts === 1 ? ' ponto' : ' pontos') + '</b>') + '">' +
        '<i style="width:' + (100 * pts / max) + '%;background:' + c + '"></i><b>' + pts + '</b></div>'
      : '<div class="dl-barra ' + lado + ' vazio"><span>não jogaram</span></div>';
    const linha = (k, rotulo) => { const kb = rotulo ? ia : k;   // "Entre eles": o lado de B é contra A
      return '<div class="dl-linha' + (rotulo ? ' dl-entre' : '') + '">' + barra('a', duA, rotulo ? duB : t[k][0], pa[k] || 0, ja[k], cA) +
      '<div class="dl-adv">' + (rotulo ? '<b>' + rotulo + '</b>' : '<span class="n">' + (t[k][1] == null ? '—' : t[k][1] + 'º') + '</span>' + escP(t[k][0], true) + '<b>' + esc(t[k][0]) + '</b>') + '</div>' +
      barra('b', duB, rotulo ? duA : t[k][0], pb[kb] || 0, jb[kb], cB) + '</div>'; };
    const comuns = advs.filter(k => ja[k] && jb[k]);
    const tA = comuns.reduce((s, k) => s + (pa[k] || 0), 0), tB = comuns.reduce((s, k) => s + (pb[k] || 0), 0);
    const mA = comuns.filter(k => (pa[k] || 0) > (pb[k] || 0)).length, mB = comuns.filter(k => (pb[k] || 0) > (pa[k] || 0)).length;
    const q = n => n + (n === 1 ? ' adversário' : ' adversários');
    res.innerHTML = '<div class="dl-placar"><span class="dl-q">' + escP(duA, true) + '<b>' + esc(duA) + '</b></span><b class="dl-num">' + tA + ' × ' + tB + '</b>' +
      '<span class="dl-q">' + escP(duB, true) + '<b>' + esc(duB) + '</b></span></div>' +
      '<p class="cp-nota">Pontos contra os ' + q(comuns.length) + ' que os dois enfrentaram. ' + esc(duA) + ' fez mais pontos contra ' + q(mA) + ', ' +
      esc(duB) + ' contra ' + q(mB) + (comuns.length - mA - mB ? ', e empataram em ' + (comuns.length - mA - mB) : '') + '.</p>';
    graf.innerHTML = '<div class="dl-linha dl-cab"><div class="dl-q a">' + esc(duA) + escP(duA, true) + '</div><div class="dl-adv"></div><div class="dl-q b">' + escP(duB, true) + esc(duB) + '</div></div>' +
      ((ja[ib] || jb[ia]) ? linha(ib, 'Entre eles') : '') + advs.map(k => linha(k)).join('');
  }
  const trocarDuelo = () => duelo(EDS[IDX[atual]]);
  dlA.addEventListener('change', () => { const n = EDS[IDX[atual]].tab[+dlA.value][0]; if (n === duB) duB = duA; duA = n; trocarDuelo(); });
  dlB.addEventListener('change', () => { const n = EDS[IDX[atual]].tab[+dlB.value][0]; if (n === duA) duA = duB; duB = n; trocarDuelo(); });
  document.getElementById('dl-troca').addEventListener('click', () => { [duA, duB] = [duB, duA]; trocarDuelo(); });
  // ---- Corrida (desde 2003) e Artilharia
  const cpc = corridaPosicoes('cpc', false);
  function corrida(e) {
    const tem = !!e.cor;
    document.getElementById('cpc-bloco').hidden = !tem; document.getElementById('cpc-sem').hidden = tem;
    if (!tem) return;
    const cl = e.cor.cl.map(k => e.tab[k][0]), pos = {}, acum = {};
    cl.forEach((c, k) => { pos[c] = e.cor.pos[k]; acum[c] = e.cor.pts[k]; });
    cpc.usar({ clubes: cl, pos, acum }, null, { rot: e.grupos.map((_, k) => k + 1), marca: (a, i) => i === 0 || a % 5 === 0, quebra: false,
      nomear: a => 'Rodada ' + a, faixas: e.cor.faixas });
  }
  function artilharia(e) {
    // lista oficial quando o banco tem; senão, os gols com autor registrados jogo a jogo (avisa quando cobrem só parte)
    const of = e.artof && e.artof.length, lista = of ? e.artof.concat(e.art.length ? [['__', '', 0]] : [], e.art) : e.art, aviso = document.getElementById('cpa-sem');
    aviso.textContent = !lista.length ? D.TX['cpa-sem'] : !of && e.cob < 0.9 ? 'Parcial: só ' + Math.round(100 * e.cob) + '% dos gols desta edição têm autor registrado.' : '';
    aviso.hidden = !aviso.textContent;
    const mx = lista.length ? lista[0][2] : 1;
    let pos = 0;
    document.getElementById('cpa-lista').innerHTML = lista.map(([j, c, n]) => j === '__' ? (pos = 0, '<h3 class="cp-subgrupo">Gols registrados jogo a jogo' + (e.cob < 0.9 ? ' (' + Math.round(100 * e.cob) + '% dos gols)' : '') + '</h3>') : (k =>  '<div class="cp-art"><span class="n">' + (k + 1) + 'º</span>' +
      '<div class="quem"><b>' + esc(j) + '</b><span>' + escP(c, true) + esc(c) + '</span></div><div class="trilho"><i style="width:' + (100 * n / mx) + '%;--c:' + corDe(c) + '"></i></div><b class="gols">' + n + '</b></div>')(pos++)).join('');
  }
  const corDe = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  document.addEventListener('tema-mudou', () => { artilharia(EDS[IDX[atual]]); duelo(EDS[IDX[atual]]); });
  let subAtual = 'resumo', feito = false;
  const ir = id => { location.hash = 'campeonato/' + subAtual + '/' + id; };
  sel.addEventListener('change', () => ir(sel.value));
  document.getElementById('cp-ant').addEventListener('click', () => { const i = IDX[atual]; if (i > 0) ir(EDS[i - 1].id); });
  document.getElementById('cp-prox').addEventListener('click', () => { const i = IDX[atual]; if (i < EDS.length - 1) ir(EDS[i + 1].id); });
  document.getElementById('cp-tabela').addEventListener('click', ev => { if (ev.target.closest('.pt-mais')) { todos = !todos; mostrar(atual); } });
  // a aba avisa quando abre; a edição vem do endereço (#campeonato/2019) ou fica a última vista
  document.addEventListener('aba-aberta', ev => {
    if (ev.detail.k !== 'campeonato') return;
    subAtual = ev.detail.sub;
    const id = ev.detail.resto in IDX ? ev.detail.resto : atual;
    if (id !== atual || !feito) { feito = true; mostrar(id); }
    if (ev.detail.resto !== id) history.replaceState(null, '', '#campeonato/' + subAtual + '/' + id);
  });
})();
// ---- por clube: escolhe o clube e vê números, trajetória, campanhas, confrontos, jogos e artilharia ----
(() => {
  const sel = document.getElementById('cl-sel'); if (!sel) return;
  const CLUBES = Object.keys(PART).sort((a, b) => a.localeCompare(b, 'pt-BR')), POR = Object.fromEntries(CLUBES.map(c => [slugClube(c), c]));
  sel.innerHTML = CLUBES.map(c => '<option value="' + slugClube(c) + '">' + esc(c) + '</option>').join('');
  const VITc = Object.fromEntries(VIT.map(x => [x[0], x])), TOP = 30;
  const fmtN = n => n.toLocaleString('pt-BR'), pct = x => (100 * x).toFixed(1).replace('.', ',') + '%', dec = x => x.toFixed(2).replace('.', ',');
  const sinal = n => (n > 0 ? '+' : n < 0 ? '−' : '') + fmtN(Math.abs(n));
  const pl = (n, um, varios) => fmtN(n) + ' ' + (n === 1 ? um : varios);
  const escP = (c, p) => ESCUDOS[c] ? '<img class="cu-esc' + (p ? ' p' : '') + '" alt="" src="' + ESCUDOS[c] + '">'
    : '<span class="cu-esc' + (p ? ' p' : '') + '" style="background:' + cor(c)[0] + '"></span>';
  const cartao = (rot, corpo, det) => '<div class="cu-card"><span class="cu-rot">' + rot + '</span>' + corpo + '<small>' + det + '</small></div>';
  const um = (c, num, txt) => '<div class="cu-um">' + (c ? escP(c) : '') + '<b>' + num + '</b><span>' + txt + '</span></div>';
  const kpi = (v, rot, sub) => '<div class="kpi"><b>' + v + '</b><span>' + rot + '</span><small>' + sub + '</small></div>';
  const nomeEd = i => anoT(EDS[i]) + (EDP[i].comp ? ' · ' + EDP[i].comp : '');
  let atual = 'palmeiras', subAtual = 'resumo', feito = false, todosConf = false, edJ = null;
  // jogos do clube: [edição, grupo, adversário, gols pró, gols contra, em casa?]
  const cacheJ = {};
  const jogosDe = c => cacheJ[c] = cacheJ[c] || EDS.flatMap((e, i) => { const k = e.tab.findIndex(r => r[0] === c); if (k < 0) return [];
    return e.jogos.filter(x => x[1] === k || x[2] === k).map(([g, mi, vi, gm, gv, , pen]) => { const pp = pen ? pen.split('-') : null;
      return mi === k ? [i, g, e.tab[vi][0], gm, gv, true, pp && pp.join(' × ')] : [i, g, e.tab[mi][0], gv, gm, false, pp && pp.slice().reverse().join(' × ')]; }); });
  // campanhas: [edição, posição, J, V, E, D, GP, GC]
  const campanhas = c => PART[c].map(([i, pos]) => { const r = EDS[i].tab.find(x => x[0] === c); return [i, pos, r[2], r[3], r[4], r[5], r[6], r[7], r[8] || 0]; });
  const MED = { ouro: 'campeão', prata: 'vice', bronze: '3º lugar' };

  function cabecalho(c, cs) {
    const x = VITc[c], tit = ED.map((e, i) => [e, i]).filter(([e]) => e.campeao === c || e.co === c), vic = ED.filter(e => e.vice === c), ter = ED.filter(e => e.terceiro === c);
    document.getElementById('cl-escudo').innerHTML = escP(c);
    document.getElementById('cl-titulo').textContent = c;
    document.getElementById('cl-cartoes').innerHTML = [
      kpi(cs.length, 'Participações', 'estreia em ' + EDS[cs[0][0]].ano),
      kpi(tit.length, tit.length === 1 ? 'Título' : 'Títulos', tit.length ? 'último em ' + tit[tit.length - 1][0].ano : 'ainda sem título'),
      kpi(vic.length, vic.length === 1 ? 'Vice' : 'Vices', vic.length ? 'último em ' + vic[vic.length - 1].ano : '—'),
      kpi(ter.length, 'Terceiros', ter.length ? 'último em ' + ter[ter.length - 1].ano : '—'),
      kpi(fmtN(x[1]), 'Jogos', x[2] + ' V · ' + x[3] + ' E · ' + x[4] + ' D'),
      kpi(pct((3 * x[2] + x[3]) / (3 * x[1])), 'Aproveitamento', 'vitória 3, empate 1'),
      kpi(fmtN(x[5]), 'Gols', 'sofreu ' + fmtN(x[6]) + ' · saldo ' + sinal(x[5] - x[6])),
    ].join('');
  }
  // ---- Resumo: trajetória, pódios e destaques
  function resumo(c, cs, js) {
    const N = EDS.length, W = 1000, H = 250, ML = 40, MR = 16, MT = 16, MB = 28;
    // escala raiz quadrada: abre o topo da tabela (onde está a briga) e comprime o fundo
    const maxP = Math.max(20, ...cs.map(x => x[1])), X = i => ML + i * (W - ML - MR) / (N - 1),
      Y = q => MT + (Math.sqrt(q) - 1) / (Math.sqrt(maxP) - 1) * (H - MT - MB);
    let svg = '', ultY = -99;
    for (const q of [1, 3, 5, 10, 20, 40, 60, 90].filter(q => q <= maxP)) { if (Y(q) - ultY < 16) continue; ultY = Y(q); svg += '<line class="cr-grade" x1="' + ML + '" x2="' + (W - MR) + '" y1="' + Y(q) + '" y2="' + Y(q) + '"/><text class="cr-eixo" x="' + (ML - 8) + '" y="' + (Y(q) + 4) + '" text-anchor="end">' + q + 'º</text>'; }
    EDS.forEach((e, i) => { if (i === 0 || (e.ano % 10 === 0 && EDS[i - 1].ano % 10 !== 0 && i > 3)) svg += '<text class="cr-eixo" x="' + X(i) + '" y="' + (H - 6) + '" text-anchor="middle">' + e.ano + '</text>'; });
    const onde = Object.fromEntries(cs.map(x => [x[0], x]));
    let d = '';
    cs.forEach(([i, q], k) => { d += (k && cs[k - 1][0] === i - 1 ? 'L' : 'M') + X(i).toFixed(1) + ' ' + Y(q).toFixed(1); });
    svg += '<path class="cl-traj" d="' + d + '" stroke="' + corDe(c) + '"/>';
    for (const [i, q, J, V, E, D] of cs) { const m = medalha(i, c);
      svg += '<circle class="cl-ponto ' + (m || '') + '" cx="' + X(i) + '" cy="' + Y(q) + '" r="' + (m ? 6 : 4) + '" style="--c:' + corDe(c) + '" data-dica="' +
        esc('<b>' + nomeEd(i) + '</b><br>' + q + 'º de ' + EDS[i].tab.length + (m ? ' · ' + MED[m] : '') + '<br>' + V + ' V · ' + E + ' E · ' + D + ' D') + '"/>'; }
    const traj = document.getElementById('cl-traj');
    traj.innerHTML = '<svg viewBox="0 0 ' + W + ' ' + H + '" class="cl-traj-svg" role="img" aria-label="Posição final em cada edição">' + svg + '</svg>';
    traj.scrollLeft = traj.scrollWidth;   // no celular rola de lado: começa nas edições mais novas
    // pódios: um selo por ano
    const pods = cs.filter(([i]) => medalha(i, c)).map(([i]) => '<span class="cl-pod ' + medalha(i, c) + '" data-dica="' + esc('<b>' + nomeEd(i) + '</b><br>' + MED[medalha(i, c)]) + '">' + EDS[i].ano + '</span>');
    document.getElementById('cl-podios').innerHTML = pods.length ? '<div class="cl-pods">' + pods.join('') + '</div>' : '<p class="cp-nota">Nenhum pódio ainda: a melhor colocação foi ' +
      Math.min(...cs.map(x => x[1])) + 'º.</p>';
    // destaques
    const ap = x => (3 * x[3] + x[4]) / (3 * x[2]), com10 = cs.filter(x => x[2] >= 10);
    const bom = com10.length ? com10.reduce((a, x) => ap(x) > ap(a) ? x : a) : null, ruim = com10.length ? com10.reduce((a, x) => ap(x) < ap(a) ? x : a) : null;
    const gols = cs.reduce((a, x) => x[6] > a[6] ? x : a);
    const dif = j => j[3] - j[4], aplicada = js.reduce((a, j) => dif(j) > dif(a) || (dif(j) === dif(a) && j[3] > a[3]) ? j : a, js[0]);
    const sofrida = js.reduce((a, j) => dif(j) < dif(a) || (dif(j) === dif(a) && j[4] > a[4]) ? j : a, js[0]);
    // temporadas seguidas (duas edições no mesmo ano contam como um ano)
    const anosC = [...new Set(EDP.map(x => x.ano))], kAno = Object.fromEntries(anosC.map((a, k) => [a, k]));
    const ks = [...new Set(cs.map(([i]) => kAno[EDS[i].ano]))].sort((a, b) => a - b);
    let seq = [0, 0, 0], ini = ks[0];
    ks.forEach((k, j) => { if (j && ks[j - 1] !== k - 1) ini = k; if (k - ini + 1 > seq[0]) seq = [k - ini + 1, ini, k]; });
    const conf = confrontos(c, js), mais = conf[0], fregues = conf.slice().sort((a, b) => b.v - a.v || a.j - b.j)[0], carrasco = conf.slice().sort((a, b) => b.d - a.d || a.j - b.j)[0];
    const placar = j => '<div class="cu-jogo">' + escP(j[5] ? c : j[2]) + '<b>' + (j[5] ? j[3] + ' × ' + j[4] : j[4] + ' × ' + j[3]) + '</b>' + escP(j[5] ? j[2] : c) + '</div>';
    const art = (ARTC[c] || [])[0], primeira = cs[0], ultima = cs[cs.length - 1];
    const cards = [
      cartao('Estreia', um(c, anoT(EDS[primeira[0]]), nomeEd(primeira[0]).split(' · ')[1] || CONF.curto), primeira[1] + 'º colocado de ' + EDS[primeira[0]].tab.length),
      cartao('Última participação', um(c, anoT(EDS[ultima[0]]), EDP[ultima[0]].comp || CONF.curto), ultima[1] + 'º colocado de ' + EDS[ultima[0]].tab.length),
      cartao('Mais temporadas seguidas', um(c, seq[0], 'temporadas sem faltar'), 'de ' + anosC[seq[1]] + ' a ' + anosC[seq[2]]),
      bom && cartao('Melhor campanha', um(c, pct(ap(bom)), 'de aproveitamento'), nomeEd(bom[0]) + ' · ' + bom[1] + 'º · ' + bom[3] + ' V · ' + bom[4] + ' E · ' + bom[5] + ' D'),
      ruim && cartao('Pior campanha', um(c, pct(ap(ruim)), 'de aproveitamento'), nomeEd(ruim[0]) + ' · ' + ruim[1] + 'º · ' + ruim[3] + ' V · ' + ruim[4] + ' E · ' + ruim[5] + ' D'),
      cartao('Mais gols numa edição', um(c, gols[6], 'gols em ' + gols[2] + ' jogos'), nomeEd(gols[0])),
      js.length && cartao('Maior goleada aplicada', placar(aplicada), '<b>' + esc(c) + '</b> × <b>' + esc(aplicada[2]) + '</b> · ' + (aplicada[5] ? 'em casa' : 'fora') + ' · ' + EDS[aplicada[0]].ano),
      js.length && cartao('Maior goleada sofrida', placar(sofrida), '<b>' + esc(c) + '</b> × <b>' + esc(sofrida[2]) + '</b> · ' + (sofrida[5] ? 'em casa' : 'fora') + ' · ' + EDS[sofrida[0]].ano),
      mais && cartao('Adversário mais enfrentado', um(mais.c, mais.j, 'jogos'), '<b>' + esc(mais.c) + '</b> · ' + mais.v + ' V · ' + mais.e + ' E · ' + mais.d + ' D'),
      fregues && fregues.v && cartao('Maior freguês', um(fregues.c, fregues.v, 'vitórias contra'), '<b>' + esc(fregues.c) + '</b> · ' + fregues.v + ' V · ' + fregues.e + ' E · ' + fregues.d + ' D em ' + fregues.j + ' jogos'),
      carrasco && carrasco.d && cartao('Maior carrasco', um(carrasco.c, carrasco.d, 'derrotas para'), '<b>' + esc(carrasco.c) + '</b> · ' + carrasco.v + ' V · ' + carrasco.e + ' E · ' + carrasco.d + ' D em ' + carrasco.j + ' jogos'),
      art && (D.ARTCOB || {})[c] >= 0.8 && cartao('Maior artilheiro', um(c, art[1], 'gols'), '<b>' + esc(art[0]) + '</b> · ' + (art[2] === art[3] ? art[2] : art[2] + ' a ' + art[3])),
    ].filter(Boolean);
    document.getElementById('cl-destaques').innerHTML = '<div class="cu-cartoes">' + cards.join('') + '</div>';
  }
  // ---- Campanhas: uma linha por edição (a linha leva à edição)
  function tabela(c, cs) {
    const linhas = cs.slice().reverse().map(([i, q, J, V, E, D, GP, GC, AJ]) => { const e = EDS[i], m = medalha(i, c), sg = GP - GC;
      return '<tr class="cl-camp ' + (m ? 'p' + { ouro: 1, prata: 2, bronze: 3 }[m] : '') + '" data-ed="' + e.id + '" title="Ver a edição"><td class="pos">' + q + 'º</td><td class="clube">' + anoT(e) + '</td><td class="comp">' + esc(EDP[i].comp || CONF.curto) + '</td>' +
        '<td class="pts">' + (semPts(e) ? '–' : ptsE(e, V, E, D) + AJ) + '</td><td>' + J + '</td><td>' + V + '</td><td>' + E + '</td><td>' + D + '</td><td class="gpgc">' + GP + '</td><td class="gpgc">' + GC + '</td>' +
        '<td class="' + (sg < 0 ? 'neg' : '') + '">' + sinal(sg) + '</td><td>' + pct(ptsE(e, V, E, D) / (e.pv * J)) + '</td></tr>'; }).join('');
    document.getElementById('cl-campanhas').innerHTML = '<div class="cp-rolar"><table class="cp-tab cl-tab"><thead><tr><th>Pos</th><th>Ano</th><th class="comp">Competição</th><th>Pts</th><th>J</th><th>V</th><th>E</th><th>D</th>' +
      '<th class="gpgc">GP</th><th class="gpgc">GC</th><th>SG</th><th title="vitória 3, empate 1">Aprov.</th></tr></thead><tbody>' + linhas + '</tbody></table></div>';
  }
  document.getElementById('cl-campanhas').addEventListener('click', ev => { const tr = ev.target.closest('tr[data-ed]'); if (tr) location.hash = 'campeonato/classificacao/' + tr.dataset.ed; });
  // ---- Confrontos: retrospecto contra cada adversário
  function confrontos(c, js) {
    const m = {};
    for (const [, , adv, gp, gc] of js) { const x = m[adv] = m[adv] || { c: adv, j: 0, v: 0, e: 0, d: 0, gp: 0, gc: 0 };
      x.j++; x.gp += gp; x.gc += gc; if (gp > gc) x.v++; else if (gp === gc) x.e++; else x.d++; }
    return Object.values(m).sort((a, b) => b.j - a.j || b.v - a.v || a.c.localeCompare(b.c, 'pt-BR'));
  }
  function listaConf(c, js) {
    const conf = confrontos(c, js), mx = conf.length ? conf[0].j : 1;
    document.getElementById('cl-confrontos').innerHTML = '<div class="pt-legenda" style="margin:10px 0 6px"><span><span class="cl-leg v"></span>vitórias</span><span><span class="cl-leg e"></span>empates</span>' +
      '<span><span class="cl-leg d"></span>derrotas</span><span>' + pl(conf.length, 'adversário', 'adversários') + ' diferentes</span></div>' +
      (todosConf ? conf : conf.slice(0, TOP)).map(x => '<div class="cl-conf"><div class="quem">' + escP(x.c, true) + '<a class="cl-link" href="#clube/confrontos/' + slugClube(x.c) + '">' + esc(x.c) + '</a></div>' +
        '<div class="barra" style="width:' + (100 * x.j / mx) + '%" data-dica="' + esc('<b>' + esc(c) + ' × ' + esc(x.c) + '</b><br>' + x.j + ' jogos: ' + x.v + ' V, ' + x.e + ' E, ' + x.d + ' D<br>gols: ' + x.gp + ' × ' + x.gc) + '">' +
        '<i class="v" style="flex:' + x.v + '"></i><i class="e" style="flex:' + x.e + '"></i><i class="d" style="flex:' + x.d + '"></i></div>' +
        '<div class="num"><b>' + x.j + '</b> jogos<small>' + x.v + ' V · ' + x.e + ' E · ' + x.d + ' D · saldo ' + sinal(x.gp - x.gc) + '</small></div></div>').join('') +
      (conf.length > TOP ? '<button class="pt-mais" type="button">' + (todosConf ? 'Ver só os ' + TOP + ' mais enfrentados' : 'Ver todos os ' + conf.length + ' adversários') + '</button>' : '');
  }
  document.getElementById('cl-confrontos').addEventListener('click', ev => { if (ev.target.closest('.pt-mais')) { todosConf = !todosConf; listaConf(POR[atual], jogosDe(POR[atual])); } });
  // ---- Jogos: os jogos do clube numa edição
  const jsel = document.getElementById('clj-sel');
  function jogos(c, cs, js) {
    const eds = cs.map(x => x[0]).reverse();
    if (!eds.includes(edJ)) edJ = eds.find(i => EDS[i].j > 0) ?? eds[0];   // abre numa edição que tem jogos
    jsel.innerHTML = eds.map(i => '<option value="' + i + '">' + esc(nomeEd(i)) + '</option>').join(''); jsel.value = edJ;
    document.getElementById('clj-ant').disabled = edJ === eds[eds.length - 1]; document.getElementById('clj-prox').disabled = edJ === eds[0];
    const e = EDS[edJ], lado = (n, cls) => '<span class="' + cls + '">' + (cls === 'm' ? esc(n) + escP(n, true) : escP(n, true) + esc(n)) + '</span>';
    const meus = js.filter(j => j[0] === edJ);
    document.getElementById('clj-lista').innerHTML = '<div class="cp-jogos">' + meus.map(([, g, adv, gp, gc, casa, pen]) => { const r = gp > gc ? 'v' : gp === gc ? 'e' : 'd';
      return '<div class="cl-jogo"><span class="rot">' + esc(e.grupos[g]) + '</span><div class="cp-jogo ' + (casa ? (gp > gc ? 'vm' : gp < gc ? 'vv' : '') : (gp > gc ? 'vv' : gp < gc ? 'vm' : '')) + '">' +
        (casa ? lado(c, 'm') + '<b>' + gp + ' × ' + gc + (pen ? '<small class="pen">pên. ' + pen + '</small>' : '') + '</b>' + lado(adv, 'v')
              : lado(adv, 'm') + '<b>' + gc + ' × ' + gp + (pen ? '<small class="pen">pên. ' + pen.split(' × ').reverse().join(' × ') + '</small>' : '') + '</b>' + lado(c, 'v')) + '</div><i class="cl-res ' + r + '">' + r.toUpperCase() + '</i></div>'; }).join('') + '</div>';
  }
  const passoJ = d => { const c = POR[atual], eds = PART[c].map(x => x[0]), k = eds.indexOf(edJ) + d; if (k >= 0 && k < eds.length) { edJ = eds[k]; jogos(c, campanhas(c), jogosDe(c)); } };
  jsel.addEventListener('change', () => { edJ = +jsel.value; const c = POR[atual]; jogos(c, campanhas(c), jogosDe(c)); });
  document.getElementById('clj-ant').addEventListener('click', () => passoJ(-1));
  document.getElementById('clj-prox').addEventListener('click', () => passoJ(1));
  // ---- Artilharia (desde 2003)
  function artilharia(c) {
    const a = ARTC[c] || [], mx = a.length ? a[0][1] : 1;
    document.getElementById('cla-sem').hidden = a.length > 0;
    document.getElementById('cla-lista').innerHTML = a.map(([j, n, a1, a2], k) => '<div class="cp-art"><span class="n">' + (k + 1) + 'º</span>' +
      '<div class="quem"><b>' + esc(j) + '</b><span>' + (a1 === a2 ? a1 : a1 + ' a ' + a2) + '</span></div><div class="trilho"><i style="width:' + (100 * n / mx) + '%;--c:' + corDe(c) + '"></i></div><b class="gols">' + n + '</b></div>').join('');
  }
  const corDe = c => { const [c1, c2] = cor(c);
    return document.documentElement.dataset.theme === 'dark' ? (escuro(c1) ? c2 : c1) : (claro(c1) ? (claro(c2) ? '#8a8f8a' : c2) : c1); };
  function mostrar(sl) {
    if (sl !== atual) { todosConf = false; edJ = null; }
    atual = sl; sel.value = sl; if (sel.sincronizar) sel.sincronizar();
    const c = POR[sl], cs = campanhas(c), js = jogosDe(c), k = CLUBES.indexOf(c);
    document.getElementById('cl-ant').disabled = k === 0; document.getElementById('cl-prox').disabled = k === CLUBES.length - 1;
    cabecalho(c, cs); resumo(c, cs, js); tabela(c, cs); listaConf(c, js); jogos(c, cs, js); artilharia(c);
  }
  document.addEventListener('tema-mudou', () => { if (feito) mostrar(atual); });
  const ir = sl => { location.hash = 'clube/' + subAtual + '/' + sl; };
  sel.addEventListener('change', () => ir(sel.value));
  document.getElementById('cl-ant').addEventListener('click', () => { const k = CLUBES.indexOf(POR[atual]); if (k > 0) ir(slugClube(CLUBES[k - 1])); });
  document.getElementById('cl-prox').addEventListener('click', () => { const k = CLUBES.indexOf(POR[atual]); if (k < CLUBES.length - 1) ir(slugClube(CLUBES[k + 1])); });
  // a aba avisa quando abre; o clube vem do endereço (#clube/resumo/palmeiras) ou fica o último visto
  document.addEventListener('aba-aberta', ev => {
    if (ev.detail.k !== 'clube') return;
    subAtual = ev.detail.sub;
    // sem clube no endereço: o último visto; se ele não jogou esta competição, o de mais participações
    const sl = ev.detail.resto in POR ? ev.detail.resto : atual in POR ? atual
      : slugClube(Object.keys(PART).sort((x, y) => PART[y].length - PART[x].length)[0]);
    if (sl !== atual || !feito) { feito = true; mostrar(sl); }
    if (ev.detail.resto !== sl) history.replaceState(null, '', '#clube/' + subAtual + '/' + sl);
  });
})();
// ---- seletor próprio no lugar do <select> nativo (que abre branco, fora do visual): busca, grupos e ícone ----
// o <select> continua escondido como fonte do valor: quem usa lê sel.value e ouve 'change' como antes
function escolha(sel, opc = {}) {
  if (!sel) return;
  const box = document.createElement('div'); box.className = 'esc-box';
  box.innerHTML = '<button type="button" class="esc-btn" aria-haspopup="listbox"><span class="esc-txt"></span><i class="esc-seta">▾</i></button>';
  sel.after(box); box.prepend(sel); sel.classList.add('esc-oculto'); sel.tabIndex = -1;
  const painel = document.createElement('div'); painel.className = 'esc-painel'; painel.hidden = true;   // no body: o topo corta o que passa da borda
  painel.innerHTML = (opc.busca ? '<input class="esc-busca" type="search" placeholder="' + opc.busca + '" aria-label="' + opc.busca + '">' : '') + '<div class="esc-lista" role="listbox"></div>';
  document.body.appendChild(painel);
  const btn = box.querySelector('.esc-btn'), txt = box.querySelector('.esc-txt'), lista = painel.querySelector('.esc-lista'), busca = painel.querySelector('.esc-busca');
  const ic = o => opc.icone ? opc.icone(o) : '', norm = t => t.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const item = o => '<button type="button" class="esc-op" role="option" data-v="' + esc(o.value) + '" data-t="' + esc(norm(o.text)) + '">' + ic(o) + '<span>' + esc(o.text) + '</span></button>';
  function montar() {
    let h = '';
    for (const n of sel.children) h += n.tagName === 'OPTGROUP' ? '<div class="esc-grupo">' + esc(n.label) + '</div>' + [...n.children].map(item).join('') : item(n);
    lista.innerHTML = h; sync();
  }
  function sync() {
    const o = sel.options[sel.selectedIndex];
    txt.innerHTML = o ? ic(o) + '<span>' + esc(o.text) + '</span>' : '';
    lista.querySelectorAll('.esc-op').forEach(b => b.classList.toggle('ativo', b.dataset.v === sel.value));
  }
  function filtrar() {
    const q = busca ? norm(busca.value.trim()) : '';
    lista.querySelectorAll('.esc-op').forEach(b => { b.hidden = !!q && !b.dataset.t.includes(q); });
    lista.querySelectorAll('.esc-grupo').forEach(g => { let n = g.nextElementSibling, algum = false;
      while (n && !n.classList.contains('esc-grupo')) { if (!n.hidden) algum = true; n = n.nextElementSibling; } g.hidden = !algum; });
  }
  function abrir() {
    const r = btn.getBoundingClientRect(), larg = Math.max(r.width, 280);
    painel.hidden = false; box.classList.add('aberto');
    painel.style.left = Math.max(8, Math.min(r.left, innerWidth - larg - 8)) + 'px'; painel.style.top = (r.bottom + 6) + 'px';
    painel.style.width = larg + 'px'; painel.style.maxHeight = Math.max(220, innerHeight - r.bottom - 20) + 'px';
    if (busca) { busca.value = ''; busca.focus(); }
    filtrar();
    const a = lista.querySelector('.ativo'); if (a) lista.scrollTop = a.offsetTop - lista.clientHeight / 2;
  }
  function fechar() { if (painel.hidden) return; painel.hidden = true; box.classList.remove('aberto'); }
  btn.addEventListener('click', () => painel.hidden ? abrir() : fechar());
  lista.addEventListener('click', ev => { const b = ev.target.closest('.esc-op'); if (!b) return;
    fechar(); if (b.dataset.v !== sel.value) { sel.value = b.dataset.v; sel.dispatchEvent(new Event('change')); } sync(); });
  if (busca) { busca.addEventListener('input', filtrar);
    busca.addEventListener('keydown', ev => { if (ev.key === 'Enter') { const b = [...lista.querySelectorAll('.esc-op')].find(x => !x.hidden); if (b) b.click(); } }); }
  painel.addEventListener('keydown', ev => { if (ev.key === 'Escape') { fechar(); btn.focus(); } });
  document.addEventListener('click', ev => { if (!box.contains(ev.target) && !painel.contains(ev.target)) fechar(); });
  addEventListener('resize', fechar);
  addEventListener('scroll', ev => { if (!painel.contains(ev.target)) fechar(); }, true);
  new MutationObserver(montar).observe(sel, { childList: true, subtree: true });   // as opções mudam (rodadas, edições do clube)
  sel.addEventListener('change', sync); sel.sincronizar = sync;   // quem troca sel.value por código chama sel.sincronizar()
  montar();
}
escolha(document.getElementById('cp-sel'), { busca: 'Buscar ano ou competição' });
escolha(document.getElementById('cpj-sel'));
escolha(document.getElementById('cl-sel'), { busca: 'Buscar clube', icone: o => ESCUDOS[o.text] ? '<img class="esc-ico" alt="" src="' + ESCUDOS[o.text] + '">' : '' });
escolha(document.getElementById('clj-sel'), { busca: 'Buscar ano' });
// ---- competição: trocar recarrega a página com ?c= (mesma aba e sub-aba)
// painel de competições: países por continente à esquerda; as competições do país à direita (Ligas, Copas, Estaduais); busca
(() => {
  const btn = document.getElementById('comp-btn'), painel = document.getElementById('comp-painel');
  const busca = document.getElementById('comp-busca'), lPaises = document.getElementById('comp-paises'), lista = document.getElementById('comp-lista');
  const atual = COMPS.find(c => c.s === COMP);
  const band = c => c.band ? '<img class="cpn-band" alt="" src="' + c.band + '">' : '<span class="cpn-band vazio"></span>';
  btn.innerHTML = band(atual) + '<span class="cb-txt"><b>' + esc(atual.curto) + '</b><small>' + esc(atual.pn) + '</small></span><i class="esc-seta">▾</i>';
  const paises = [...new Map(COMPS.map(c => [c.pais, c])).values()];   // na ordem do seletor (Brasil primeiro)
  const conts = [...new Set(paises.map(c => c.cont))];
  let pais = atual.pais;
  const ir = s => { try { localStorage.setItem('v2-comp', s); } catch (e) {}
    location.href = location.pathname + '?c=' + s + '#' + location.hash.slice(1).split('/').slice(0, 2).join('/'); };
  const item = (c, comPais) => '<button type="button" class="cpn-comp' + (c.s === COMP ? ' ativo' : '') + '" data-s="' + c.s + '">' +
    (comPais ? band(c) : '') + '<span><b>' + esc(comPais ? c.curto + ' · ' + c.pn : c.curto) + '</b><small>' + esc(c.nome) + ' · ' + esc(c.per) + '</small></span></button>';
  const norm = t => t.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  function desenhar() {
    const q = norm(busca.value.trim());
    lPaises.innerHTML = conts.map(ct => '<div class="cpn-cont">' + esc(ct) + '</div>' + paises.filter(p => p.cont === ct).map(p =>
      '<button type="button" class="cpn-pais' + (p.pais === pais && !q ? ' ativo' : '') + '" data-p="' + p.pais + '">' + band(p) + '<span>' + esc(p.pn) +
      '</span><small>' + COMPS.filter(c => c.pais === p.pais).length + '</small></button>').join('')).join('');
    if (q) {   // busca: todas as competições cujo nome, rótulo ou país têm o texto
      const achadas = COMPS.filter(c => norm(c.nome + ' ' + c.curto + ' ' + c.pn).includes(q));
      lista.innerHTML = achadas.length ? achadas.map(c => item(c, true)).join('') : '<p class="cpn-nada">Nenhuma competição com esse nome.</p>';
      return;
    }
    const ORDEM = ['Ligas', 'Copas', 'Estaduais'], doPais = COMPS.filter(c => c.pais === pais);
    const grupos = [...new Set(doPais.map(c => c.grupo))].sort((a, b) => (ORDEM.indexOf(a) + 1 || 9) - (ORDEM.indexOf(b) + 1 || 9));
    lista.innerHTML = '<div class="cpn-titulo">' + band(doPais[0]) + esc(doPais[0].pn) + '</div>' +
      grupos.map(g => '<div class="cpn-grupo">' + esc(g) + '</div>' + doPais.filter(c => c.grupo === g).map(c => item(c, false)).join('')).join('');
  }
  const abrir = () => { pais = atual.pais; busca.value = ''; desenhar(); painel.hidden = false; document.body.classList.add('sem-rolar');
    if (matchMedia('(min-width:901px)').matches) busca.focus(); };
  const fechar = () => { painel.hidden = true; document.body.classList.remove('sem-rolar'); };
  btn.addEventListener('click', abrir);
  painel.addEventListener('click', ev => {
    if (ev.target === painel || ev.target.closest('.cpn-fechar')) return fechar();
    const p = ev.target.closest('.cpn-pais'); if (p) { pais = p.dataset.p; busca.value = ''; desenhar(); return; }
    const c = ev.target.closest('.cpn-comp'); if (c) { if (c.dataset.s === COMP) fechar(); else ir(c.dataset.s); }
  });
  busca.addEventListener('input', desenhar);
  document.addEventListener('keydown', ev => { if (ev.key === 'Escape' && !painel.hidden) fechar(); });
})();
// ---- abas (barra lateral) e sub-abas (História): guardadas no endereço (#historia/podio, #clube...) ----
(() => {
  const abas = [...document.querySelectorAll('.aba')], botoes = [...document.querySelectorAll('.nav')];
  const ultimaSub = {};   // cada aba lembra a última sub-aba aberta
  const abrir = (hash, rolar = true) => {
    let [k, sub, ...resto] = decodeURIComponent(hash || '').split('/'); resto = resto.join('/');   // "2025%20Apertura" -> "2025 Apertura"
    if (!abas.some(a => a.id === 'aba-' + k)) k = 'historia';
    const aba = document.getElementById('aba-' + k), subs = [...document.querySelectorAll('.sub[data-aba="' + k + '"]')];
    document.querySelectorAll('.subnav-lat').forEach(g => { g.hidden = g.dataset.de !== k; });
    if (subs.length) { if (!subs.some(b => b.dataset.sub === sub)) { if (sub && !resto) resto = sub; sub = ultimaSub[k] || subs[0].dataset.sub; } ultimaSub[k] = sub;
      subs.forEach(b => b.classList.toggle('ativo', b.dataset.sub === sub));
      aba.querySelectorAll('section[data-sub]').forEach(x => { x.hidden = x.dataset.sub !== sub; }); } else sub = sub || '';   // sem sub-abas: o resto do endereço é da aba (#campeonato/2019)
    abas.forEach(a => { a.hidden = a !== aba; }); botoes.forEach(b => b.classList.toggle('ativo', b.dataset.aba === k));
    const novo = k + (sub ? '/' + sub : '') + (resto ? '/' + resto : '');
    if (location.hash.slice(1) !== novo) history.replaceState(null, '', '#' + novo);
    if (rolar) window.scrollTo(0, 0);
    if (k === 'campeonato' && !EDS.some(x => x.cor)) document.querySelector('.sub[data-aba="campeonato"][data-sub="corrida"]').hidden = true;
    if (CONF.tipo === 'copa') document.querySelector('.sub[data-aba="historia"][data-sub="pontos"]').hidden = true;   // copa não tem pontos (CB-013)
    const ativa = subs.find(b => b.classList.contains('ativo'));   // no celular as sub-abas rolam de lado: a aberta fica à vista
    if (ativa) ativa.parentElement.scrollLeft = ativa.offsetLeft - ativa.parentElement.offsetLeft - 24;
    document.dispatchEvent(new CustomEvent('aba-aberta', { detail: { k, sub, resto } }));
  };
  botoes.forEach(b => b.addEventListener('click', () => abrir(b.dataset.aba)));
  document.querySelectorAll('.sub').forEach(b => b.addEventListener('click', () => abrir(b.dataset.aba + '/' + b.dataset.sub)));
  window.addEventListener('hashchange', () => abrir(location.hash.slice(1)));
  abrir(location.hash.slice(1) || 'historia');
})();
try { const t = localStorage.getItem('v2-tema'); if (t) { document.documentElement.dataset.theme = t; document.querySelector('.tema').textContent = t === 'dark' ? '☀ Claro' : '☾ Escuro'; document.dispatchEvent(new Event('tema-mudou')); } } catch (e) {}
desenhar();
"""


def main() -> None:
    competicoes_dos_pacotes()
    dados, todos_clubes = {}, set()
    for slug in COMPETICOES:
        con = abrir(slug)
        try:
            eds = campeoes(con)
            edp, part = participacoes(con)
            jogos, total_gols = gols(con)
            vit = campanhas(con)
            cjv = corridas_jv(con)
            cur = curiosidades(con, eds, edp, part, cjv)
            det = edicoes_detalhe(con, edp, part, cjv)
            artc = artilharia_clubes(con)
            todos_art = artilharia_clubes(con, todos=True)
        finally:
            con.close()
        tx, conf = textos(slug, eds, edp, part, jogos, total_gols, det, artc)
        # quanto dos gols de cada clube tem autor registrado (o cartão "Maior artilheiro" só aparece com 80% ou mais)
        artcob = {c: round(sum(n for _, n, *_ in todos_art.get(c, [])) / max(1, sum(cjv["gp"].get(c, []))), 2) for c in part}
        dados[slug] = {"ED": eds, "EDP": edp, "PART": part, "VIT": vit, "CJV": cjv, "CUR": cur, "EDS": det, "ARTC": artc, "TX": tx,
                       "CONF": conf, "ARTCOB": artcob}
        todos_clubes |= set(part)
        print(f"  {COMPETICOES[slug]['curto']}: {len(eds)} edições, {len(part)} clubes, {jogos} jogos")
    movimentos(dados)
    comps = catalogo(dados)
    for x in comps:   # cabeçalho da competição: bandeira, "Inglaterra · 1ª divisão · 1888/89 a 2024/25" e o nome
        tx = dados[x["s"]]["TX"]
        tx["bandeira"] = f'<img class="comp-band" alt="" src="{x["band"]}">' if x["band"] else ""
        tx["selo"] = " · ".join(filter(None, (x["pn"], x["curto"] if x["curto"] != x["nome"] else "", x["per"])))
        tx["h1"] = x["nome"]
    (PAINEL / "dados").mkdir(parents=True, exist_ok=True)
    for slug, d in dados.items():
        (PAINEL / "dados" / f"{slug}.js").write_text(
            "window.DADOS_COMP = " + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    import hashlib
    versao = hashlib.sha1(b"".join((PAINEL / "dados" / f"{s}.js").read_bytes() for s in dados)).hexdigest()[:10]
    pagina = (
        '<!doctype html><html lang="pt-BR" data-theme="dark"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1"><title>Clube Analítico</title>'
        '<link rel="icon" href="marca/icone.svg" type="image/svg+xml"><link rel="icon" href="marca/favicon-32.png" sizes="32x32">'
        '<link rel="apple-touch-icon" href="marca/apple-touch-icon.png"><meta name="theme-color" content="#06140c">'
        f"<style>{CSS}</style></head><body>"
        '<nav class="lateral" aria-label="Seções"><div class="marca"><img src="marca/escudo.svg" alt="" width="52" height="56"><span>Clube Analítico<small data-t="marca"></small></span></div>'
        '<div class="comp-escolha"><button type="button" id="comp-btn" class="comp-btn" aria-haspopup="dialog" aria-label="Trocar competição"></button></div>'
        '<button class="nav ativo" data-aba="historia" type="button"><span class="ico">🏆</span>História</button>'
        '<div class="subnav-lat" data-de="historia"><button class="sub ativo" data-aba="historia" data-sub="corrida" type="button">Corrida dos títulos</button>'
        '<button class="sub" data-aba="historia" data-sub="podio" type="button">Pódio</button>'
        '<button class="sub" data-aba="historia" data-sub="participacoes" type="button">Participações</button>'
        '<button class="sub" data-aba="historia" data-sub="jogos" type="button">Jogos e vitórias</button>'
        '<button class="sub" data-aba="historia" data-sub="gols" type="button">Gols</button>'
        '<button class="sub" data-aba="historia" data-sub="pontos" type="button">Pontuação histórica</button>'
        '<button class="sub" data-aba="historia" data-sub="curiosidades" type="button">Estatísticas e curiosidades</button></div>'
        '<button class="nav" data-aba="campeonato" type="button"><span class="ico">📅</span>Por campeonato</button>'
        '<div class="subnav-lat" data-de="campeonato" hidden><button class="sub" data-aba="campeonato" data-sub="resumo" type="button">Resumo</button>'
        '<button class="sub" data-aba="campeonato" data-sub="classificacao" type="button">Classificação</button>'
        '<button class="sub" data-aba="campeonato" data-sub="participantes" type="button">Participantes</button>'
        '<button class="sub" data-aba="campeonato" data-sub="corrida" type="button">Corrida</button>'
        '<button class="sub" data-aba="campeonato" data-sub="jogos" type="button">Jogos</button>'
        '<button class="sub" data-aba="campeonato" data-sub="duelo" type="button">Duelo</button>'
        '<button class="sub" data-aba="campeonato" data-sub="artilharia" type="button">Artilharia</button></div>'
        '<button class="nav" data-aba="clube" type="button"><span class="ico">🛡️</span>Por clube</button>'
        '<div class="subnav-lat" data-de="clube" hidden><button class="sub" data-aba="clube" data-sub="resumo" type="button">Resumo</button>'
        '<button class="sub" data-aba="clube" data-sub="campanhas" type="button">Campanhas</button>'
        '<button class="sub" data-aba="clube" data-sub="confrontos" type="button">Confrontos</button>'
        '<button class="sub" data-aba="clube" data-sub="jogos" type="button">Jogos</button>'
        '<button class="sub" data-aba="clube" data-sub="artilharia" type="button">Artilharia</button></div>'
        '<button class="tema" type="button">☀ Claro</button></nav>'
        '<div class="area"><div class="aba" id="aba-historia">'
        '<header class="topo"><div class="comp-cab"><span data-t="bandeira"></span><div class="comp-cab-txt">'
        '<span class="comp-sobre" data-t="selo"></span><h1 data-t="h1"></h1></div></div><div data-t="cartoes"></div>'
        '</header>'
        '<main><section class="painel" data-sub="corrida"><div class="cab-bloco"><h2 class="titulo-bloco" id="cr-titulo">Corrida dos títulos</h2>'
        '<div class="alterna" id="cr-tipo" role="group" aria-label="Corrida de"><button type="button" data-tipo="campeao" class="ativo">Títulos</button>'
        '<button type="button" data-tipo="vice">Vices</button><button type="button" data-tipo="terceiro">Terceiros</button></div></div>'
        '<div class="corrida-ctl" style="margin-top:14px"><button id="cr-play" type="button">▶ Ver a corrida</button>'
        '<input id="cr-ano" type="range" min="0" step="0.01" aria-label="Ano"><output id="cr-saida"></output></div>'
        '<div class="corrida-rolar"><svg id="corrida" role="img"></svg></div></section>'
        '<section class="painel" data-sub="podio" hidden><h2 class="titulo-bloco">Pódio por clube</h2>'
        '<div id="grafico"></div>'
        '</section>'
        '<section class="painel" data-sub="participacoes" hidden><div class="cab-bloco"><h2 class="titulo-bloco">Participações</h2>'
        '<div class="alterna" id="pt-vista" role="group" aria-label="Ver em"><button type="button" data-vista="quadro" class="ativo">Quadro</button>'
        '<button type="button" data-vista="corrida">Corrida</button></div></div>'
        '<div id="pt-quadro"><div class="pt-legenda" style="margin-top:8px"><span><i></i>jogou a edição</span><span><i class="vazio"></i>não jogou</span><span><b class="med ouro"></b>campeão</span><span><b class="med prata"></b>vice</span><span><b class="med bronze"></b>3º lugar</span>'
        '<span data-t="pt-info"></span></div>'
        '<div id="participacoes"></div></div>'
        '<div id="pt-corrida" class="jv-corrida" hidden><div class="pt-legenda" style="margin:8px 0 0"><span><b class="med ouro"></b>campeão</span><span><b class="med prata"></b>vice</span><span><b class="med bronze"></b>3º lugar</span></div>'
        + controles_corrida("ptc", "Corrida das participações") + '</div></section>'
        '<section class="painel" data-sub="jogos" hidden><div class="cab-bloco"><h2 class="titulo-bloco">Jogos e vitórias</h2><div class="botoes">'
        '<div class="alterna" id="jv-vista" role="group" aria-label="Ver em"><button type="button" data-vista="barras" class="ativo">Barras</button>'
        '<button type="button" data-vista="corrida">Corrida</button></div>'
        '<div class="alterna" id="jv-ordem" role="group" aria-label="Ordenar por"><button type="button" data-modo="vitorias" class="ativo">Vitórias</button>'
        '<button type="button" data-modo="jogos">Jogos</button><button type="button" data-modo="pct">%</button></div></div></div>'
        '<div id="jv-barras">'
        '<div class="pt-legenda" style="margin-top:8px"><span><span class="legenda-jv"><i></i>vitórias</span><span class="legenda-jv"><i class="meio"></i>empates</span>'
        '<span class="legenda-jv"><i class="claro"></i>derrotas</span>'
        '<span data-t="jv-info"></span><span id="jv-nota"></span> · passe o mouse para ver os detalhes</span></div>'
        '<div id="jogos-vitorias"></div></div>'
        '<div id="jv-corrida" class="jv-corrida" hidden>' + controles_corrida("jvc", "Corrida de jogos e vitórias") + '</div></section>'
        '<section class="painel" data-sub="gols" hidden><div class="cab-bloco"><h2 class="titulo-bloco">Gols</h2><div class="botoes">'
        '<div class="alterna" id="gl-vista" role="group" aria-label="Ver em"><button type="button" data-vista="barras" class="ativo">Barras</button>'
        '<button type="button" data-vista="corrida">Corrida</button></div>'
        '<div class="alterna" id="gl-ordem" role="group" aria-label="Ordenar por"><button type="button" data-modo="feitos" class="ativo">Feitos</button>'
        '<button type="button" data-modo="tomados">Tomados</button><button type="button" data-modo="saldo">Saldo</button><button type="button" data-modo="media">Por jogo</button></div></div></div>'
        '<div id="gl-barras"><div class="pt-legenda" style="margin-top:8px"><span><span class="legenda-jv"><i></i>gols feitos</span><span class="legenda-jv"><i class="claro"></i>gols tomados</span>'
        '<span data-t="gl-info"></span><span id="gl-nota"></span> · passe o mouse para ver os detalhes</span></div>'
        '<div id="gols"></div></div>'
        '<div id="gl-corrida" class="jv-corrida" hidden>' + controles_corrida("glc", "Corrida dos gols") + '</div></section>'
        '<section class="painel" data-sub="pontos" hidden><div class="cab-bloco"><h2 class="titulo-bloco">Pontuação histórica</h2><div class="botoes">'
        '<div class="alterna" id="pn-vista" role="group" aria-label="Ver em"><button type="button" data-vista="barras" class="ativo">Barras</button>'
        '<button type="button" data-vista="corrida">Corrida</button></div>'
        '<div class="alterna" id="pn-ordem" role="group" aria-label="Ordenar por"><button type="button" data-modo="pontos" class="ativo">Pontos</button>'
        '<button type="button" data-modo="aprov">Aproveitamento</button></div></div></div>'
        '<div id="pn-barras"><div class="pt-legenda" style="margin-top:8px"><span><span class="legenda-jv"><i></i>pontos das vitórias (3)</span>'
        '<span class="legenda-jv"><i class="meio"></i>pontos dos empates (1)</span><span class="legenda-jv"><i class="claro"></i>pontos perdidos</span>'
        'barra do tamanho dos pontos possíveis (3 por jogo)<span id="pn-nota"></span> · passe o mouse para ver os detalhes</span></div>'
        '<div id="pontos"></div></div>'
        '<div id="pn-corrida" class="jv-corrida" hidden>' + controles_corrida("pnc", "Corrida da pontuação histórica") + '</div></section>'
        '<section class="painel" data-sub="curiosidades" hidden><div class="cab-bloco"><h2 class="titulo-bloco">Estatísticas e curiosidades</h2>'
        '<div class="alterna" id="cu-parte" role="group" aria-label="Parte"><button type="button" data-parte="jogos" class="ativo">Jogos</button>'
        '<button type="button" data-parte="clubes">Clubes</button><button type="button" data-parte="campeoes">Campeões</button>'
        '<button type="button" data-parte="edicoes">Edições</button></div></div>'
        '<div id="curiosidades"></div></section></main></div>'
        + '<div class="aba" id="aba-campeonato" hidden><header class="topo"><span class="selo">Por campeonato</span>'
        '<div class="cp-escolha"><button type="button" class="cp-seta" id="cp-ant" aria-label="Edição anterior">◀</button>'
        '<select id="cp-sel" aria-label="Edição"></select><button type="button" class="cp-seta" id="cp-prox" aria-label="Próxima edição">▶</button></div>'
        '<h1 id="cp-titulo"></h1><div class="cartoes-topo" id="cp-cartoes"></div></header>'
        '<main><section class="painel" data-sub="resumo"><h2 class="titulo-bloco">Pódio</h2><p class="cp-nota" id="cp-nota" hidden></p><div id="cp-podio"></div></section>'
        '<section class="painel" data-sub="resumo"><h2 class="titulo-bloco">Destaques</h2><div id="cp-destaques"></div></section>'
        '<section class="painel" data-sub="resumo"><h2 class="titulo-bloco">Como foi a disputa</h2><div id="cp-disputa"></div></section>'
        '<section class="painel" data-sub="classificacao" hidden><h2 class="titulo-bloco">Classificação final</h2><div id="cp-tabela"></div></section>'
        '<section class="painel" data-sub="participantes" hidden><h2 class="titulo-bloco">Participantes</h2><div id="cpp-cartoes"></div><div id="cpp-tabela"></div></section>'
        '<section class="painel" data-sub="corrida" hidden><h2 class="titulo-bloco">Corrida rodada a rodada</h2>'
        '<p class="cp-nota" id="cpc-sem" data-t="cpc-sem" hidden></p>'
        '<div id="cpc-bloco" class="jv-corrida"><div class="pt-legenda cp-legenda-faixa" style="margin:10px 0 0" data-t="cpc-legenda"></div>' + controles_corrida("cpc", "Posição de cada clube rodada a rodada") + '</div></section>'
        '<section class="painel" data-sub="jogos" hidden><h2 class="titulo-bloco">Jogos</h2>'
        '<div class="cp-nav"><button type="button" class="cp-seta" id="cpj-ant" aria-label="Anterior">◀</button><select id="cpj-sel" aria-label="Rodada ou fase"></select>'
        '<button type="button" class="cp-seta" id="cpj-prox" aria-label="Próxima">▶</button></div><div id="cpj-lista"></div></section>'
        '<section class="painel" data-sub="duelo" hidden><h2 class="titulo-bloco">Duelo</h2>'
        '<p class="cp-nota">Escolha dois clubes: o gráfico mostra quantos pontos cada um fez contra cada adversário, na ordem da classificação final. Passe o mouse numa barra para ver os jogos.</p>'
        '<div class="cp-nav dl-escolha"><select id="dl-a" aria-label="Primeiro clube"></select>'
        '<button type="button" class="cp-seta" id="dl-troca" aria-label="Trocar os lados">⇄</button>'
        '<select id="dl-b" aria-label="Segundo clube"></select></div><div id="dl-resumo"></div><div id="dl-grafico"></div></section>'
        '<section class="painel" data-sub="artilharia" hidden><h2 class="titulo-bloco">Artilharia</h2>'
        '<p class="cp-nota" id="cpa-sem" data-t="cpa-sem" hidden></p><div id="cpa-lista" style="margin-top:12px"></div></section></main></div>'
        '<div class="aba" id="aba-clube" hidden><header class="topo"><span class="selo">Por clube</span>'
        '<div class="cp-escolha"><button type="button" class="cp-seta" id="cl-ant" aria-label="Clube anterior">◀</button>'
        '<select id="cl-sel" aria-label="Clube"></select><button type="button" class="cp-seta" id="cl-prox" aria-label="Próximo clube">▶</button></div>'
        '<div class="cl-nome"><span id="cl-escudo"></span><h1 id="cl-titulo"></h1></div><div class="cartoes-topo" id="cl-cartoes"></div></header>'
        '<main><section class="painel" data-sub="resumo"><h2 class="titulo-bloco">Trajetória</h2><div id="cl-traj"></div><div id="cl-podios"></div></section>'
        '<section class="painel" data-sub="resumo"><h2 class="titulo-bloco">Destaques</h2><div id="cl-destaques"></div></section>'
        '<section class="painel" data-sub="campanhas" hidden><h2 class="titulo-bloco">Campanhas</h2><div id="cl-campanhas"></div></section>'
        '<section class="painel" data-sub="confrontos" hidden><h2 class="titulo-bloco">Confrontos</h2><div id="cl-confrontos"></div></section>'
        '<section class="painel" data-sub="jogos" hidden><h2 class="titulo-bloco">Jogos</h2>'
        '<div class="cp-nav"><button type="button" class="cp-seta" id="clj-ant" aria-label="Edição anterior">◀</button><select id="clj-sel" aria-label="Edição"></select>'
        '<button type="button" class="cp-seta" id="clj-prox" aria-label="Próxima edição">▶</button></div><div id="clj-lista"></div></section>'
        '<section class="painel" data-sub="artilharia" hidden><h2 class="titulo-bloco">Artilharia</h2>'
        '<p class="cp-nota" id="cla-sem" data-t="cla-sem" hidden></p><div id="cla-lista" style="margin-top:12px"></div></section></main></div>'
        + '</div><div id="dica" hidden></div>'
        '<div id="comp-painel" class="comp-painel" hidden role="dialog" aria-label="Escolher competição"><div class="cpn-caixa">'
        '<div class="cpn-topo"><input id="comp-busca" type="search" placeholder="Buscar competição ou país" aria-label="Buscar competição ou país">'
        '<button type="button" class="cpn-fechar" aria-label="Fechar">✕</button></div>'
        '<div class="cpn-corpo"><nav class="cpn-paises" id="comp-paises" aria-label="Países"></nav><div class="cpn-lista" id="comp-lista"></div></div></div></div>'
        f"<script>const CORES = {json.dumps({**cores_auto(todos_clubes), **{k: list(v) for k, v in CORES.items()}}, ensure_ascii=False)};\n"
        f"const ESCUDOS = {json.dumps(escudos(todos_clubes))};\n"
        f"const COMPS = {json.dumps(comps, ensure_ascii=False)};\n"
        f"const VERSAO = '{versao}';\n{ESCOLHA}</script>"
        f"<script>{SELECAO}{JS}</script>"
        "</body></html>"
    )
    (PAINEL / "index.html").write_text(pagina, encoding="utf-8")
    ATALHO.write_text('<!doctype html><meta charset="utf-8"><title>Clube Analítico</title>'
                      '<meta http-equiv="refresh" content="0; url=painel/index.html">'
                      '<a href="painel/index.html">Abrir o painel</a>', encoding="utf-8")
    kb = lambda f: f.stat().st_size // 1024
    print(f"OK: painel/index.html ({kb(PAINEL / 'index.html')} KB) + dados de {len(dados)} competições "
          f"({', '.join(f'{s} {kb(PAINEL / "dados" / (s + ".js"))} KB' for s in dados)}), {len(todos_clubes)} clubes")


if __name__ == "__main__":
    main()
