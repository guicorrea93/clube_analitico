-- Banco genérico de futebol (db/futebol.db): qualquer competição, de qualquer país, em qualquer época.
--
-- país -> competição (liga, copa, estadual, continental; com o nível da divisão) -> edição (uma temporada)
-- -> fase (turno único, grupos, mata-mata) -> partida -> gols, cartões, estatísticas.
-- Clubes têm país e estado/província; os nomes que cada fonte usa ficam em clube_nome (com o período).
-- Toda linha que vem de fonte externa guarda a fonte, para conferir e refazer.

PRAGMA foreign_keys = ON;

CREATE TABLE pais (
    pais_id        INTEGER PRIMARY KEY,
    nome           TEXT NOT NULL UNIQUE,      -- "Brasil"
    codigo         TEXT UNIQUE,               -- ISO 3166 alfa-3: "BRA"
    confederacao   TEXT                       -- CONMEBOL, UEFA, CAF, AFC, CONCACAF, OFC
);

CREATE TABLE clube (
    clube_id       INTEGER PRIMARY KEY,
    nome           TEXT NOT NULL,             -- nome de exibição: "Athletico-PR", "Brasil de Pelotas"
    pais_id        INTEGER REFERENCES pais(pais_id),
    regiao         TEXT,                      -- estado/província: "PR" (vazio quando não se sabe)
    cidade         TEXT,
    nome_completo  TEXT,
    escudo         TEXT,                      -- arquivo em data/escudos/
    observacao     TEXT,
    UNIQUE (nome, pais_id)
);

-- nomes de um clube como cada fonte escreve (e, quando o clube mudou de nome, o período)
CREATE TABLE clube_nome (
    clube_id       INTEGER NOT NULL REFERENCES clube(clube_id),
    nome           TEXT NOT NULL,             -- como está na fonte: "Etti Jundiaí", "América Mineiro"
    nome_chave     TEXT NOT NULL,             -- sem acento e minúsculo, para casar
    fonte          TEXT NOT NULL,             -- "rsssf", "espn", "ogol", "wikipedia", "cbf", "historico"...
    ano_inicio     INTEGER,
    ano_fim        INTEGER,
    PRIMARY KEY (nome_chave, fonte, clube_id)
);

CREATE TABLE competicao (
    competicao_id  INTEGER PRIMARY KEY,
    slug           TEXT NOT NULL UNIQUE,      -- "bra-serie-a", "bra-serie-b", "bra-sp-paulista", "eng-premier-league"
    nome           TEXT NOT NULL,             -- "Campeonato Brasileiro Série A"
    nome_curto     TEXT,                      -- "Série A"
    tipo           TEXT NOT NULL,             -- liga | copa | estadual | continental | mundial | amistoso
    nivel          INTEGER,                   -- divisão (1 = principal); vazio em copa
    pais_id        INTEGER REFERENCES pais(pais_id),   -- vazio nas continentais e mundiais
    regiao         TEXT,                      -- estado, nos estaduais
    confederacao   TEXT,
    observacao     TEXT
);

CREATE TABLE edicao (
    edicao_id      INTEGER PRIMARY KEY,
    competicao_id  INTEGER NOT NULL REFERENCES competicao(competicao_id),
    temporada      TEXT NOT NULL,             -- "2019" ou "2019/20"
    ano_inicio     INTEGER NOT NULL,
    ano_fim        INTEGER,
    nome_oficial   TEXT,                      -- quando a edição teve outro nome: "Taça Brasil", "Copa João Havelange"
    chave          TEXT,                      -- identificador da edição na fonte de origem ("1967_robertao")
    num_clubes     INTEGER,
    pontos_vitoria INTEGER,
    pontos_empate  INTEGER,                   -- vazio = 1 (Marrocos e Taiti davam 2 pelo empate)
    pontos_derrota INTEGER,                   -- vazio = 0 (Marrocos e Taiti davam 1 pela derrota)
    oficial        INTEGER,                   -- 0 = edição não oficial (D-10, TL-005): jogos e participações, sem título; vazio = oficial
    formato        TEXT,                      -- descrição curta: "pontos corridos, turno e returno"
    campeao_id     INTEGER REFERENCES clube(clube_id),
    vice_id        INTEGER REFERENCES clube(clube_id),
    co_campeao_id  INTEGER REFERENCES clube(clube_id),   -- título dividido: o 1º dos outros campeões (todos em edicao_co_campeao; D-07)
    fontes         TEXT,
    observacao     TEXT,
    UNIQUE (competicao_id, temporada, chave)
);

CREATE TABLE fase (
    fase_id        INTEGER PRIMARY KEY,
    edicao_id      INTEGER NOT NULL REFERENCES edicao(edicao_id),
    ordem          INTEGER NOT NULL,
    nome           TEXT NOT NULL,             -- "Fase única", "Primeira fase", "Semifinal"
    tipo           TEXT,                      -- liga | grupos | mata_mata
    num_grupos     INTEGER,
    formato_serie  TEXT,                      -- jogo_unico | ida_volta | melhor_de_tres...
    criterio       TEXT,
    observacao     TEXT,
    UNIQUE (edicao_id, nome)
);

CREATE TABLE partida (
    partida_id          INTEGER PRIMARY KEY,
    edicao_id           INTEGER NOT NULL REFERENCES edicao(edicao_id),
    fase_id             INTEGER NOT NULL REFERENCES fase(fase_id),
    grupo               TEXT,
    rodada              INTEGER,
    data                TEXT,                 -- AAAA-MM-DD (hora local)
    hora                TEXT,
    mandante_id         INTEGER NOT NULL REFERENCES clube(clube_id),
    visitante_id        INTEGER NOT NULL REFERENCES clube(clube_id),
    gols_mandante       INTEGER,              -- placar oficial (com prorrogação, quando houve)
    gols_visitante      INTEGER,
    penaltis_mandante   INTEGER,
    penaltis_visitante  INTEGER,
    resultado_especial  TEXT,                 -- awd (tribunal) | wo | abd (abandonado) | n/p (não jogado)
    estadio             TEXT,
    cidade              TEXT,
    publico             INTEGER,
    arrecadacao         REAL,
    arbitro             TEXT,
    tecnico_mandante    TEXT,
    tecnico_visitante   TEXT,
    formacao_mandante   TEXT,
    formacao_visitante  TEXT,
    gols_texto          TEXT,                 -- autores como a fonte escreve (quando não deu para separar)
    fonte               TEXT,
    fonte_id            TEXT,                 -- id do jogo na fonte (ESPN, ogol...)
    observacao          TEXT
);

CREATE TABLE gol (
    gol_id        INTEGER PRIMARY KEY,
    partida_id    INTEGER NOT NULL REFERENCES partida(partida_id),
    clube_id      INTEGER NOT NULL REFERENCES clube(clube_id),   -- quem ganhou o gol (no contra, o adversário do autor)
    jogador       TEXT,
    minuto        INTEGER,
    acrescimo     INTEGER,
    tipo          TEXT,                       -- normal | penalti | contra | falta
    fonte         TEXT
);

CREATE TABLE cartao (
    cartao_id     INTEGER PRIMARY KEY,
    partida_id    INTEGER NOT NULL REFERENCES partida(partida_id),
    clube_id      INTEGER NOT NULL REFERENCES clube(clube_id),
    jogador       TEXT,
    minuto        INTEGER,
    acrescimo     INTEGER,
    cor           TEXT,                       -- amarelo | vermelho
    fonte         TEXT
);

CREATE TABLE estatistica_partida (           -- números de cada clube no jogo
    partida_id     INTEGER NOT NULL REFERENCES partida(partida_id),
    clube_id       INTEGER NOT NULL REFERENCES clube(clube_id),
    chutes INTEGER, chutes_alvo INTEGER, posse REAL, passes INTEGER, precisao_passes REAL,
    faltas INTEGER, amarelos INTEGER, vermelhos INTEGER, impedimentos INTEGER, escanteios INTEGER,
    fonte          TEXT,
    PRIMARY KEY (partida_id, clube_id)
);

CREATE TABLE classificacao_final (
    edicao_id      INTEGER NOT NULL REFERENCES edicao(edicao_id),
    clube_id       INTEGER NOT NULL REFERENCES clube(clube_id),
    posicao        INTEGER NOT NULL,
    jogos INTEGER, vitorias INTEGER, empates INTEGER, derrotas INTEGER, gols_pro INTEGER, gols_contra INTEGER,
    pontos         INTEGER,
    ajuste_pontos  INTEGER,                   -- punição (negativo) ou bônus
    situacao       TEXT,                      -- campeao | acesso | rebaixado | ...
    fonte          TEXT,
    observacao     TEXT,
    PRIMARY KEY (edicao_id, clube_id)
);

CREATE TABLE classificacao_rodada (           -- tabela depois de cada rodada (pontos corridos)
    edicao_id      INTEGER NOT NULL REFERENCES edicao(edicao_id),
    rodada         INTEGER NOT NULL,
    clube_id       INTEGER NOT NULL REFERENCES clube(clube_id),
    posicao        INTEGER,
    pontos INTEGER, jogos INTEGER, vitorias INTEGER, empates INTEGER, derrotas INTEGER, gols_pro INTEGER, gols_contra INTEGER,
    zona           TEXT,
    PRIMARY KEY (edicao_id, rodada, clube_id)
);

CREATE TABLE tabela_publicada (               -- tabela de fase/grupo como a fonte publica (conferência)
    edicao_id      INTEGER NOT NULL REFERENCES edicao(edicao_id),
    fase           TEXT, grupo TEXT, posicao INTEGER,
    clube_id       INTEGER REFERENCES clube(clube_id),
    nome_fonte     TEXT,
    jogos INTEGER, vitorias INTEGER, empates INTEGER, derrotas INTEGER, gols_pro INTEGER, gols_contra INTEGER, pontos INTEGER,
    fonte          TEXT
);

CREATE TABLE artilheiro (
    edicao_id      INTEGER NOT NULL REFERENCES edicao(edicao_id),
    jogador        TEXT NOT NULL,
    clube_id       INTEGER REFERENCES clube(clube_id),
    gols           INTEGER,
    fonte          TEXT
);

CREATE INDEX idx_partida_edicao ON partida(edicao_id, fase_id);
CREATE INDEX idx_partida_clubes ON partida(mandante_id, visitante_id);
CREATE INDEX idx_gol_partida ON gol(partida_id);
CREATE INDEX idx_cartao_partida ON cartao(partida_id);
CREATE INDEX idx_edicao_comp ON edicao(competicao_id, ano_inicio);
CREATE INDEX idx_clube_nome_chave ON clube_nome(nome_chave);

-- título dividido entre mais de dois clubes (Cearense 1992: quatro campeões): um registro por co-campeão (D-07)
CREATE TABLE IF NOT EXISTS edicao_co_campeao (
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    clube_id  INTEGER NOT NULL REFERENCES clube(clube_id),
    PRIMARY KEY (edicao_id, clube_id)
);
