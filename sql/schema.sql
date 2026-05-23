-- =====================================================================
-- Clube Analítico — Schema (SQLite, star schema)
-- =====================================================================
-- Filosofia:
--   * dim_*  : entidades (clube, arena, técnico, jogador, posição, temporada, competição)
--             ID surrogate INTEGER + chave natural UNIQUE
--   * fato_* : eventos/medidas (partida, gol, cartão, stats, classificação por rodada)
--             FKs para dims, índices nas colunas de filtro
-- =====================================================================

PRAGMA foreign_keys = ON;

-- ---------- DIMS ----------------------------------------------------

CREATE TABLE dim_competicao (
    competicao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome          TEXT NOT NULL UNIQUE,
    pais          TEXT NOT NULL,
    confederacao  TEXT,
    divisao       INTEGER NOT NULL,
    formato       TEXT
);

CREATE TABLE dim_temporada (
    temporada_id   INTEGER PRIMARY KEY,             -- ano (2016, 2017, ...)
    competicao_id  INTEGER NOT NULL REFERENCES dim_competicao(competicao_id),
    data_inicio    TEXT,                            -- ISO YYYY-MM-DD
    data_fim       TEXT,
    num_clubes     INTEGER,
    num_rodadas    INTEGER,
    num_jogos      INTEGER
);

CREATE TABLE dim_clube (
    clube_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome       TEXT NOT NULL UNIQUE,
    uf         TEXT
);

CREATE TABLE dim_arena (
    arena_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome       TEXT NOT NULL UNIQUE
);

CREATE TABLE dim_tecnico (
    tecnico_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome       TEXT NOT NULL UNIQUE
);

CREATE TABLE dim_posicao (
    posicao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome       TEXT NOT NULL UNIQUE                  -- Goleiro, Zagueiro, Meia, ...
);

CREATE TABLE dim_jogador (
    jogador_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome       TEXT NOT NULL UNIQUE,
    posicao_id INTEGER REFERENCES dim_posicao(posicao_id)  -- inferida do CSV de cartões
);

-- ---------- FATOS ---------------------------------------------------

CREATE TABLE fato_partida (
    partida_id        INTEGER PRIMARY KEY,             -- usa o ID da fonte
    temporada_id      INTEGER NOT NULL REFERENCES dim_temporada(temporada_id),
    competicao_id     INTEGER NOT NULL REFERENCES dim_competicao(competicao_id),
    rodada            INTEGER NOT NULL,
    data              TEXT NOT NULL,                   -- ISO YYYY-MM-DD
    hora              TEXT,
    mandante_id       INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    visitante_id      INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    arena_id          INTEGER REFERENCES dim_arena(arena_id),
    gols_mandante     INTEGER NOT NULL,
    gols_visitante    INTEGER NOT NULL,
    vencedor_id       INTEGER REFERENCES dim_clube(clube_id),  -- NULL = empate
    tecnico_mand_id   INTEGER REFERENCES dim_tecnico(tecnico_id),
    tecnico_vis_id    INTEGER REFERENCES dim_tecnico(tecnico_id),
    formacao_mandante TEXT,
    formacao_visitante TEXT,
    uf_mandante       TEXT,
    uf_visitante      TEXT,
    arrecadacao       REAL                              -- renda da partida em R$ (CSV "arrecadacao")
);
CREATE INDEX idx_partida_temp_rod  ON fato_partida(temporada_id, rodada);
CREATE INDEX idx_partida_mand      ON fato_partida(mandante_id);
CREATE INDEX idx_partida_vis       ON fato_partida(visitante_id);
CREATE INDEX idx_partida_data      ON fato_partida(data);

CREATE TABLE fato_gol (
    gol_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    partida_id  INTEGER NOT NULL REFERENCES fato_partida(partida_id),
    temporada_id INTEGER NOT NULL REFERENCES dim_temporada(temporada_id),
    rodada      INTEGER NOT NULL,
    clube_id    INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    jogador_id  INTEGER NOT NULL REFERENCES dim_jogador(jogador_id),
    minuto      INTEGER,
    tipo        TEXT                                  -- Normal, Penalti, Falta, Gol Contra, ...
);
CREATE INDEX idx_gol_partida    ON fato_gol(partida_id);
CREATE INDEX idx_gol_temporada  ON fato_gol(temporada_id);
CREATE INDEX idx_gol_jogador    ON fato_gol(jogador_id);
CREATE INDEX idx_gol_clube      ON fato_gol(clube_id);

CREATE TABLE fato_cartao (
    cartao_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    partida_id   INTEGER NOT NULL REFERENCES fato_partida(partida_id),
    temporada_id INTEGER NOT NULL REFERENCES dim_temporada(temporada_id),
    rodada       INTEGER NOT NULL,
    clube_id     INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    jogador_id   INTEGER NOT NULL REFERENCES dim_jogador(jogador_id),
    posicao_id   INTEGER REFERENCES dim_posicao(posicao_id),
    tipo         TEXT NOT NULL,                       -- Amarelo / Vermelho
    minuto       INTEGER,
    num_camisa   TEXT
);
CREATE INDEX idx_cartao_partida    ON fato_cartao(partida_id);
CREATE INDEX idx_cartao_temporada  ON fato_cartao(temporada_id);
CREATE INDEX idx_cartao_jogador    ON fato_cartao(jogador_id);

CREATE TABLE fato_stats_time (
    partida_id      INTEGER NOT NULL REFERENCES fato_partida(partida_id),
    clube_id        INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    temporada_id    INTEGER NOT NULL REFERENCES dim_temporada(temporada_id),
    rodada          INTEGER NOT NULL,
    chutes          REAL,
    chutes_alvo     REAL,
    posse           REAL,
    passes          REAL,
    prec_passes     REAL,
    faltas          REAL,
    amarelos        REAL,
    vermelhos       REAL,
    impedimentos    REAL,
    escanteios      REAL,
    PRIMARY KEY (partida_id, clube_id)
);
CREATE INDEX idx_stats_temp_rod ON fato_stats_time(temporada_id, rodada);

-- A tabela mais importante: classificação após cada rodada.
-- Preenchida durante o ingest via cálculo cumulativo.
CREATE TABLE fato_classificacao_rodada (
    temporada_id INTEGER NOT NULL REFERENCES dim_temporada(temporada_id),
    rodada       INTEGER NOT NULL,
    clube_id     INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    posicao      INTEGER NOT NULL,
    pontos       INTEGER NOT NULL,
    jogos        INTEGER NOT NULL,
    vitorias     INTEGER NOT NULL,
    empates      INTEGER NOT NULL,
    derrotas     INTEGER NOT NULL,
    gols_pro     INTEGER NOT NULL,
    gols_contra  INTEGER NOT NULL,
    saldo_gols   INTEGER NOT NULL,
    aproveitamento REAL NOT NULL,
    -- Detalhe por mando (para análises mando × visitante por rodada)
    pontos_mand   INTEGER NOT NULL,
    pontos_vis    INTEGER NOT NULL,
    jogos_mand    INTEGER NOT NULL,
    jogos_vis     INTEGER NOT NULL,
    zona          TEXT,                              -- titulo / libertadores / sula / meio / rebaixamento
    PRIMARY KEY (temporada_id, rodada, clube_id)
);
CREATE INDEX idx_class_temp ON fato_classificacao_rodada(temporada_id, posicao);
CREATE INDEX idx_class_clube ON fato_classificacao_rodada(clube_id);

-- Classificacao final historica nacional.
-- Cobre edicoes anteriores a 2003 e tambem as temporadas do banco atual.
-- Em anos com mais de uma edicao reconhecida (ex.: 1967/1968), edicao_id
-- diferencia Taca Brasil e Roberto Gomes Pedrosa.
CREATE TABLE dim_edicao_nacional (
    edicao_nacional_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_id          TEXT NOT NULL UNIQUE,
    temporada_id       INTEGER NOT NULL,
    competicao_nome    TEXT NOT NULL,
    tipo               TEXT,
    fonte_principal    TEXT,
    observacao         TEXT,
    num_clubes         INTEGER
);

CREATE TABLE dim_clube_alias (
    alias               TEXT PRIMARY KEY,
    alias_normalizado   TEXT NOT NULL,
    clube_id            INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    nome_canonico       TEXT NOT NULL,
    fonte               TEXT
);

CREATE TABLE stg_classificacao_final_codex (
    temporada_id     INTEGER NOT NULL,
    edicao_id        TEXT NOT NULL,
    competicao_nome  TEXT NOT NULL,
    posicao          INTEGER NOT NULL,
    clube_origem     TEXT NOT NULL,
    clube_canonico   TEXT NOT NULL,
    clube_id         INTEGER NOT NULL,
    fonte            TEXT,
    observacao       TEXT
);

CREATE TABLE fato_classificacao_final_nacional (
    edicao_nacional_id INTEGER NOT NULL REFERENCES dim_edicao_nacional(edicao_nacional_id),
    temporada_id       INTEGER NOT NULL,
    clube_id           INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    posicao            INTEGER NOT NULL,
    fonte              TEXT,
    observacao         TEXT,
    PRIMARY KEY (edicao_nacional_id, clube_id),
    UNIQUE (edicao_nacional_id, posicao)
);
CREATE INDEX idx_class_final_temp
    ON fato_classificacao_final_nacional(temporada_id, posicao);
CREATE INDEX idx_class_final_clube
    ON fato_classificacao_final_nacional(clube_id);

-- ---------- VIEWS DE CONVENIÊNCIA -----------------------------------

CREATE TABLE fato_participante_nacional_historico (
    edicao_nacional_id INTEGER NOT NULL REFERENCES dim_edicao_nacional(edicao_nacional_id),
    temporada_id       INTEGER NOT NULL,
    clube_id           INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    fonte              TEXT,
    observacao         TEXT,
    PRIMARY KEY (edicao_nacional_id, clube_id)
);
CREATE INDEX idx_participante_hist_temp
    ON fato_participante_nacional_historico(temporada_id);

CREATE TABLE dim_fase_nacional_historica (
    fase_nacional_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_nacional_id INTEGER NOT NULL REFERENCES dim_edicao_nacional(edicao_nacional_id),
    temporada_id       INTEGER NOT NULL,
    fase_ordem         INTEGER NOT NULL,
    fase_nome          TEXT NOT NULL,
    fase_tipo          TEXT,
    observacao         TEXT,
    UNIQUE (edicao_nacional_id, fase_nome)
);
CREATE INDEX idx_fase_hist_temp
    ON dim_fase_nacional_historica(temporada_id, fase_ordem);

CREATE TABLE fato_partida_nacional_historica (
    partida_hist_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_nacional_id INTEGER NOT NULL REFERENCES dim_edicao_nacional(edicao_nacional_id),
    temporada_id       INTEGER NOT NULL,
    fase_nacional_id   INTEGER NOT NULL REFERENCES dim_fase_nacional_historica(fase_nacional_id),
    rodada             INTEGER,
    jogo               INTEGER,
    data               TEXT,
    mandante_id        INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    visitante_id       INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    gols_mandante      INTEGER NOT NULL,
    gols_visitante     INTEGER NOT NULL,
    fonte              TEXT,
    observacao         TEXT
);
CREATE INDEX idx_partida_hist_temp
    ON fato_partida_nacional_historica(temporada_id, fase_nacional_id);
CREATE INDEX idx_partida_hist_clubes
    ON fato_partida_nacional_historica(mandante_id, visitante_id);

CREATE VIEW vw_tabela_final AS
SELECT
    cr.temporada_id,
    cr.posicao,
    c.nome AS clube,
    cr.pontos,
    cr.jogos,
    cr.vitorias,
    cr.empates,
    cr.derrotas,
    cr.gols_pro,
    cr.gols_contra,
    cr.saldo_gols,
    cr.aproveitamento,
    cr.zona
FROM fato_classificacao_rodada cr
JOIN dim_clube c ON c.clube_id = cr.clube_id
WHERE (cr.temporada_id, cr.rodada) IN (
    SELECT temporada_id, MAX(rodada)
    FROM fato_classificacao_rodada
    GROUP BY temporada_id
);

CREATE VIEW vw_classificacao_final_historica AS
SELECT
    e.temporada_id,
    e.edicao_id,
    e.competicao_nome,
    e.tipo,
    f.posicao,
    c.clube_id,
    c.nome AS clube,
    c.uf,
    f.fonte,
    f.observacao
FROM fato_classificacao_final_nacional f
JOIN dim_edicao_nacional e
  ON e.edicao_nacional_id = f.edicao_nacional_id
JOIN dim_clube c
  ON c.clube_id = f.clube_id;

CREATE VIEW vw_partida_full AS
SELECT
    p.partida_id,
    p.temporada_id,
    p.rodada,
    p.data,
    cm.nome AS mandante,
    cv.nome AS visitante,
    p.gols_mandante,
    p.gols_visitante,
    cw.nome AS vencedor,
    a.nome  AS arena,
    tm.nome AS tecnico_mandante,
    tv.nome AS tecnico_visitante,
    p.formacao_mandante,
    p.formacao_visitante,
    p.uf_mandante,
    p.uf_visitante,
    p.arrecadacao
FROM fato_partida p
JOIN dim_clube cm ON cm.clube_id = p.mandante_id
JOIN dim_clube cv ON cv.clube_id = p.visitante_id
LEFT JOIN dim_clube cw   ON cw.clube_id = p.vencedor_id
LEFT JOIN dim_arena a    ON a.arena_id  = p.arena_id
LEFT JOIN dim_tecnico tm ON tm.tecnico_id = p.tecnico_mand_id
LEFT JOIN dim_tecnico tv ON tv.tecnico_id = p.tecnico_vis_id;

CREATE VIEW vw_artilheiros_temporada AS
SELECT
    g.temporada_id,
    j.nome    AS jogador,
    c.nome    AS clube,
    COUNT(*)  AS gols,
    SUM(CASE WHEN g.tipo LIKE '%enal%' THEN 1 ELSE 0 END) AS penaltis,
    SUM(CASE WHEN g.tipo LIKE '%alta%' THEN 1 ELSE 0 END) AS faltas
FROM fato_gol g
JOIN dim_jogador j ON j.jogador_id = g.jogador_id
JOIN dim_clube   c ON c.clube_id   = g.clube_id
WHERE g.tipo != 'Gol Contra' OR g.tipo IS NULL
GROUP BY g.temporada_id, j.jogador_id, c.clube_id;

-- ---------- COPA DO BRASIL (estrutura independente da Serie A) -------

CREATE TABLE IF NOT EXISTS copa_brasil_edicao (
    ano         INTEGER PRIMARY KEY,
    nome        TEXT NOT NULL,
    formato     TEXT,
    fonte_url   TEXT NOT NULL,
    observacao  TEXT
);

CREATE TABLE IF NOT EXISTS copa_brasil_final (
    ano              INTEGER PRIMARY KEY REFERENCES copa_brasil_edicao(ano),
    campeao_id       INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    vice_id          INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    gols_campeao     INTEGER NOT NULL,
    gols_vice        INTEGER NOT NULL,
    criterio_decisao TEXT,
    resumo_decisao   TEXT,
    fonte_url        TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS copa_brasil_final_partida (
    ano             INTEGER NOT NULL REFERENCES copa_brasil_edicao(ano),
    jogo            INTEGER NOT NULL,
    mandante_id     INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    visitante_id    INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    gols_mandante   INTEGER NOT NULL,
    gols_visitante  INTEGER NOT NULL,
    estadio         TEXT,
    local           TEXT,
    fonte_url       TEXT NOT NULL,
    PRIMARY KEY (ano, jogo)
);

CREATE VIEW IF NOT EXISTS vw_copa_brasil_finais AS
SELECT
    f.ano,
    c.nome AS campeao,
    c.uf AS uf_campeao,
    v.nome AS vice,
    v.uf AS uf_vice,
    f.gols_campeao,
    f.gols_vice,
    f.criterio_decisao,
    f.resumo_decisao,
    f.fonte_url
FROM copa_brasil_final f
JOIN dim_clube c ON c.clube_id = f.campeao_id
JOIN dim_clube v ON v.clube_id = f.vice_id;

CREATE VIEW IF NOT EXISTS vw_copa_brasil_partidas_finais AS
SELECT
    p.ano,
    p.jogo,
    m.nome AS mandante,
    m.uf AS uf_mandante,
    p.gols_mandante,
    p.gols_visitante,
    vi.nome AS visitante,
    vi.uf AS uf_visitante,
    p.estadio,
    p.local,
    p.fonte_url
FROM copa_brasil_final_partida p
JOIN dim_clube m ON m.clube_id = p.mandante_id
JOIN dim_clube vi ON vi.clube_id = p.visitante_id;

CREATE VIEW IF NOT EXISTS vw_copa_brasil_desempenho_clube AS
WITH clubes AS (
    SELECT campeao_id AS clube_id, 1 AS titulos, 0 AS vices, ano FROM copa_brasil_final
    UNION ALL
    SELECT vice_id AS clube_id, 0 AS titulos, 1 AS vices, ano FROM copa_brasil_final
)
SELECT
    c.clube_id,
    c.nome AS clube,
    c.uf,
    SUM(titulos) AS titulos,
    SUM(vices) AS vices,
    COUNT(*) AS finais,
    MIN(ano) AS primeira_final,
    MAX(ano) AS ultima_final
FROM clubes x
JOIN dim_clube c ON c.clube_id = x.clube_id
GROUP BY c.clube_id, c.nome, c.uf;

CREATE VIEW IF NOT EXISTS vw_copa_brasil_titulos_por_uf AS
SELECT c.uf, COUNT(*) AS titulos
FROM copa_brasil_final f
JOIN dim_clube c ON c.clube_id = f.campeao_id
GROUP BY c.uf;

CREATE TABLE IF NOT EXISTS copa_brasil_edicao_info (
    ano              INTEGER PRIMARY KEY REFERENCES copa_brasil_edicao(ano),
    datas            TEXT,
    num_times        INTEGER,
    jogos            INTEGER,
    gols             INTEGER,
    artilheiro       TEXT,
    campeao_info     TEXT,
    vice_info        TEXT,
    melhor_jogador   TEXT,
    melhor_goleiro   TEXT,
    fonte_url        TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS copa_brasil_participante (
    ano                    INTEGER NOT NULL REFERENCES copa_brasil_edicao(ano),
    clube_id               INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    associacao             TEXT,
    criterio_classificacao TEXT,
    entra_terceira_fase    INTEGER NOT NULL DEFAULT 0,
    fonte_url              TEXT NOT NULL,
    PRIMARY KEY (ano, clube_id)
);

CREATE VIEW IF NOT EXISTS vw_copa_brasil_edicoes_completas AS
SELECT
    e.ano,
    e.nome,
    i.datas,
    i.num_times,
    i.jogos,
    i.gols,
    i.artilheiro,
    f.campeao,
    f.vice,
    f.gols_campeao,
    f.gols_vice,
    f.criterio_decisao,
    (SELECT COUNT(*) FROM copa_brasil_participante p WHERE p.ano = e.ano) AS participantes_mapeados,
    e.fonte_url
FROM copa_brasil_edicao e
LEFT JOIN copa_brasil_edicao_info i ON i.ano = e.ano
LEFT JOIN vw_copa_brasil_finais f ON f.ano = e.ano;

CREATE VIEW IF NOT EXISTS vw_copa_brasil_participantes AS
SELECT
    p.ano,
    c.nome AS clube,
    c.uf,
    p.associacao,
    p.criterio_classificacao,
    p.entra_terceira_fase,
    p.fonte_url
FROM copa_brasil_participante p
JOIN dim_clube c ON c.clube_id = p.clube_id;
