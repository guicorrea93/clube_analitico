PRAGMA foreign_keys = ON;

CREATE TABLE fonte (
    fonte_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    url TEXT,
    tipo TEXT,
    observacao TEXT
);

CREATE TABLE competicao (
    competicao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    organizacao TEXT,
    tipo TEXT,
    observacao TEXT
);

CREATE TABLE selecao (
    selecao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    nome_normalizado TEXT NOT NULL UNIQUE,
    codigo_bandeira TEXT,
    confederacao TEXT,
    observacao TEXT
);

CREATE TABLE alias_selecao (
    alias TEXT PRIMARY KEY,
    alias_normalizado TEXT NOT NULL,
    selecao_id INTEGER NOT NULL REFERENCES selecao(selecao_id),
    fonte_id INTEGER REFERENCES fonte(fonte_id),
    observacao TEXT
);

CREATE TABLE identidade_pessoa (
    identidade_pessoa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chave_identidade TEXT NOT NULL UNIQUE,
    nome_canonico TEXT NOT NULL,
    nome_normalizado TEXT NOT NULL,
    wikidata_id TEXT,
    observacao TEXT
);

CREATE TABLE pessoa (
    pessoa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    identidade_pessoa_id INTEGER REFERENCES identidade_pessoa(identidade_pessoa_id),
    nome TEXT NOT NULL,
    nome_normalizado TEXT NOT NULL,
    selecao_principal_id INTEGER REFERENCES selecao(selecao_id),
    wikidata_id TEXT,
    observacao TEXT,
    UNIQUE (nome_normalizado, selecao_principal_id)
);

CREATE TABLE alias_pessoa (
    alias_pessoa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    alias TEXT NOT NULL,
    alias_normalizado TEXT NOT NULL,
    pessoa_id INTEGER NOT NULL REFERENCES pessoa(pessoa_id),
    selecao_contexto_id INTEGER REFERENCES selecao(selecao_id),
    papel TEXT,
    fonte_id INTEGER REFERENCES fonte(fonte_id),
    confianca TEXT NOT NULL DEFAULT 'media',
    observacao TEXT,
    UNIQUE (alias_normalizado, pessoa_id, selecao_contexto_id, papel)
);

CREATE TABLE estadio (
    estadio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT,
    pais TEXT,
    nome_normalizado TEXT NOT NULL,
    UNIQUE (nome_normalizado, cidade, pais)
);

CREATE TABLE edicao (
    edicao_id INTEGER PRIMARY KEY,
    competicao_id INTEGER NOT NULL REFERENCES competicao(competicao_id),
    ano INTEGER NOT NULL UNIQUE,
    sede TEXT,
    campeao_id INTEGER REFERENCES selecao(selecao_id),
    vice_id INTEGER REFERENCES selecao(selecao_id),
    terceiro_id INTEGER REFERENCES selecao(selecao_id),
    quarto_id INTEGER REFERENCES selecao(selecao_id),
    jogos INTEGER,
    gols INTEGER,
    publico_total INTEGER,
    status TEXT NOT NULL DEFAULT 'realizada',
    fonte_id INTEGER REFERENCES fonte(fonte_id),
    url TEXT
);

CREATE TABLE participacao_edicao (
    participacao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    selecao_id INTEGER NOT NULL REFERENCES selecao(selecao_id),
    posicao_final INTEGER,
    grupo TEXT,
    pontos INTEGER,
    jogos INTEGER,
    vitorias INTEGER,
    empates INTEGER,
    derrotas INTEGER,
    gols_pro INTEGER,
    gols_contra INTEGER,
    saldo_gols INTEGER,
    classificado TEXT,
    UNIQUE (edicao_id, selecao_id)
);

CREATE TABLE fase (
    fase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    nome TEXT NOT NULL,
    ordem INTEGER,
    tipo TEXT,
    observacao TEXT,
    UNIQUE (edicao_id, nome)
);

CREATE TABLE grupo (
    grupo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    fase_id INTEGER REFERENCES fase(fase_id),
    nome TEXT NOT NULL,
    UNIQUE (edicao_id, nome)
);

CREATE TABLE partida (
    partida_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    fase_id INTEGER REFERENCES fase(fase_id),
    grupo_id INTEGER REFERENCES grupo(grupo_id),
    data_texto TEXT,
    horario_texto TEXT,
    estadio_id INTEGER REFERENCES estadio(estadio_id),
    selecao_1_id INTEGER NOT NULL REFERENCES selecao(selecao_id),
    selecao_2_id INTEGER NOT NULL REFERENCES selecao(selecao_id),
    gols_selecao_1 INTEGER,
    gols_selecao_2 INTEGER,
    placar_texto TEXT,
    teve_prorrogacao INTEGER NOT NULL DEFAULT 0,
    teve_penaltis INTEGER NOT NULL DEFAULT 0,
    penaltis_selecao_1 INTEGER,
    penaltis_selecao_2 INTEGER,
    vencedor_id INTEGER REFERENCES selecao(selecao_id),
    publico INTEGER,
    arbitro_id INTEGER REFERENCES pessoa(pessoa_id),
    fonte_id INTEGER REFERENCES fonte(fonte_id),
    observacao TEXT,
    UNIQUE (edicao_id, fase_id, grupo_id, data_texto, selecao_1_id, selecao_2_id, placar_texto)
);
CREATE INDEX idx_partida_edicao ON partida(edicao_id);
CREATE INDEX idx_partida_selecao_1 ON partida(selecao_1_id);
CREATE INDEX idx_partida_selecao_2 ON partida(selecao_2_id);

CREATE TABLE gol (
    gol_id INTEGER PRIMARY KEY AUTOINCREMENT,
    partida_id INTEGER NOT NULL REFERENCES partida(partida_id),
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    selecao_id INTEGER NOT NULL REFERENCES selecao(selecao_id),
    selecao_autor_id INTEGER REFERENCES selecao(selecao_id),
    pessoa_id INTEGER REFERENCES pessoa(pessoa_id),
    minuto INTEGER,
    acrescimo INTEGER,
    minuto_texto TEXT,
    tipo TEXT NOT NULL DEFAULT 'normal',
    texto_original TEXT,
    fonte_id INTEGER REFERENCES fonte(fonte_id)
);
CREATE INDEX idx_gol_partida ON gol(partida_id);
CREATE INDEX idx_gol_pessoa ON gol(pessoa_id);
CREATE INDEX idx_gol_selecao ON gol(selecao_id);
CREATE INDEX idx_gol_selecao_autor ON gol(selecao_autor_id);
CREATE INDEX idx_pessoa_identidade ON pessoa(identidade_pessoa_id);

CREATE TABLE escalacao (
    escalacao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    partida_id INTEGER NOT NULL REFERENCES partida(partida_id),
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    selecao_id INTEGER NOT NULL REFERENCES selecao(selecao_id),
    pessoa_id INTEGER NOT NULL REFERENCES pessoa(pessoa_id),
    numero TEXT,
    posicao TEXT,
    situacao TEXT NOT NULL,
    ordem INTEGER,
    fonte_id INTEGER REFERENCES fonte(fonte_id),
    UNIQUE (partida_id, selecao_id, pessoa_id, situacao, ordem)
);
CREATE INDEX idx_escalacao_partida ON escalacao(partida_id);
CREATE INDEX idx_escalacao_pessoa ON escalacao(pessoa_id);

CREATE TABLE comando_tecnico (
    comando_tecnico_id INTEGER PRIMARY KEY AUTOINCREMENT,
    partida_id INTEGER NOT NULL REFERENCES partida(partida_id),
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    selecao_id INTEGER NOT NULL REFERENCES selecao(selecao_id),
    pessoa_id INTEGER NOT NULL REFERENCES pessoa(pessoa_id),
    fonte_id INTEGER REFERENCES fonte(fonte_id),
    UNIQUE (partida_id, selecao_id, pessoa_id)
);

CREATE TABLE premiacao (
    premiacao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_id INTEGER NOT NULL REFERENCES edicao(edicao_id),
    premio TEXT NOT NULL,
    pessoa_id INTEGER REFERENCES pessoa(pessoa_id),
    selecao_id INTEGER REFERENCES selecao(selecao_id),
    valor_texto TEXT,
    fonte_id INTEGER REFERENCES fonte(fonte_id)
);

CREATE TABLE auditoria_identidade (
    auditoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_entidade TEXT NOT NULL,
    chave TEXT NOT NULL,
    descricao TEXT NOT NULL,
    severidade TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pendente',
    fonte_primaria_id INTEGER REFERENCES fonte(fonte_id),
    fonte_cruzamento_id INTEGER REFERENCES fonte(fonte_id),
    observacao TEXT
);

CREATE VIEW vw_gols_por_jogador AS
SELECT
    p.pessoa_id,
    p.nome AS jogador,
    s.nome AS selecao,
    e.ano,
    COUNT(*) AS gols
FROM gol g
JOIN pessoa p ON p.pessoa_id = g.pessoa_id
JOIN selecao s ON s.selecao_id = COALESCE(g.selecao_autor_id, g.selecao_id)
JOIN edicao e ON e.edicao_id = g.edicao_id
WHERE g.tipo <> 'gol_contra'
GROUP BY p.pessoa_id, p.nome, s.nome, e.ano;

CREATE VIEW vw_gols_por_jogador_global AS
SELECT
    ip.identidade_pessoa_id,
    ip.nome_canonico AS jogador,
    s.nome AS selecao,
    e.ano,
    COUNT(*) AS gols
FROM gol g
JOIN pessoa p ON p.pessoa_id = g.pessoa_id
JOIN identidade_pessoa ip ON ip.identidade_pessoa_id = p.identidade_pessoa_id
JOIN selecao s ON s.selecao_id = COALESCE(g.selecao_autor_id, g.selecao_id)
JOIN edicao e ON e.edicao_id = g.edicao_id
WHERE g.tipo <> 'gol_contra'
GROUP BY ip.identidade_pessoa_id, ip.nome_canonico, s.nome, e.ano;

CREATE VIEW vw_partidas_resumo AS
SELECT
    e.ano,
    f.nome AS fase,
    gr.nome AS grupo,
    p.data_texto,
    s1.nome AS selecao_1,
    p.placar_texto,
    s2.nome AS selecao_2,
    est.nome AS estadio,
    p.publico
FROM partida p
JOIN edicao e ON e.edicao_id = p.edicao_id
LEFT JOIN fase f ON f.fase_id = p.fase_id
LEFT JOIN grupo gr ON gr.grupo_id = p.grupo_id
JOIN selecao s1 ON s1.selecao_id = p.selecao_1_id
JOIN selecao s2 ON s2.selecao_id = p.selecao_2_id
LEFT JOIN estadio est ON est.estadio_id = p.estadio_id;
