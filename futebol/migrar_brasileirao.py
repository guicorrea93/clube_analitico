"""Monta db/futebol.db (modelo genérico, futebol/esquema.sql) a partir de db/brasileirao.db.

Leva para o modelo único:
- Série A: edições antigas (1937-2002: dim_edicao_nacional, fases e partidas históricas) e modernas
  (2003+: fato_partida com estádio, técnicos, formações, arrecadação; gols, cartões, estatísticas e
  tabela por rodada);
- Série B (tabelas *_serie_b, montadas por serie_b/importar.py).

Cada clube aparece uma vez (pelo nome de exibição do dashboard, gerar_dashboard_v2.nome), com o estado,
e guarda os nomes que tinha no banco antigo em clube_nome. O banco antigo não muda. No fim confere que
nada se perdeu: jogos, gols e campeão de cada edição, contra o banco antigo.

No fim separa os clubes de SEPARAR e carrega os pacotes do agente de coleta (futebol/carregar_pacotes.py:
Série C em diante).

Uso: python futebol/migrar_brasileirao.py
"""
from __future__ import annotations

import sqlite3
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ORIGEM = RAIZ / "db" / "brasileirao.db"
DESTINO = RAIZ / "db" / "futebol.db"
ESQUEMA = Path(__file__).resolve().parent / "esquema.sql"
sys.path.insert(0, str(RAIZ))
from gerar_dashboard_v2 import nome as exibir  # noqa: E402

UFS = set("AC AL AM AP BA CE DF ES GO MA MG MS MT PA PB PE PI PR RJ RN RO RR RS SC SE SP TO".split())
# estado de clubes antigos da Série A que o banco antigo não tinha (os da Série B vêm de serie_b/clubes.py)
UF_MANUAL = {"Aliança": "RJ", "CEUB": "DF", "Corumbaense": "MS", "Francana": "SP", "GE Maringá": "PR", "Hercílio Luz": "SC",
             "J.Malucelli": "PR", "Liga da Marinha": "RJ", "Manufatora": "RJ", "Metropol": "SC", "Olaria": "RJ", "Perdigão": "SC",
             "Potiguar": "RN", "Siderúrgica": "MG", "XV de Jaú": "SP", "Água Verde": "PR"}
# mesmo clube com dois nomes de exibição no banco antigo -> nome que fica (o outro vai para clube_nome)
MESCLAR = {"Comercial-SP": "Comercial-RP",   # Comercial de Ribeirão Preto (Série B o chama de Comercial-SP)
           "Grêmio Prudente": "Barueri"}      # Grêmio Barueri, que jogou como Grêmio Prudente em 2010-2011
# um nome de exibição que junta dois clubes no banco antigo: (nome, nome do clube antigo, estado, último ano do antigo)
SEPARAR = [("Novorizontino", "GE Novorizontino", "SP", 1999)]   # GE Novorizontino (1973-1999) x Grêmio Novorizontino (2010+)
TIPO_GOL = {"gol contra": "contra", "penalti": "penalti", "penalty": "penalti", "falta": "falta", "normal": "normal"}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return " ".join("".join(c if c.isalnum() else " " for c in s).split())


def uf_do_nome(nome: str) -> str | None:
    fim = nome.replace("/", "-").rsplit("-", 1)
    return fim[1] if len(fim) == 2 and fim[1] in UFS else None


def migrar() -> None:
    if DESTINO.exists():
        DESTINO.unlink()
    a = sqlite3.connect(ORIGEM)
    b = sqlite3.connect(DESTINO)
    b.executescript(ESQUEMA.read_text(encoding="utf-8"))
    b.execute("INSERT INTO pais (pais_id, nome, codigo, confederacao) VALUES (1, 'Brasil', 'BRA', 'CONMEBOL')")
    serie_a = b.execute("""INSERT INTO competicao (slug, nome, nome_curto, tipo, nivel, pais_id, confederacao, observacao)
        VALUES ('bra-serie-a', 'Campeonato Brasileiro Série A', 'Série A', 'liga', 1, 1, 'CONMEBOL',
                'Inclui as edições reconhecidas pela CBF: Torneio dos Campeões (1937), Taça Brasil (1959-1968) e Robertão (1967-1970)')""").lastrowid
    serie_b = b.execute("""INSERT INTO competicao (slug, nome, nome_curto, tipo, nivel, pais_id, confederacao, observacao)
        VALUES ('bra-serie-b', 'Campeonato Brasileiro Série B', 'Série B', 'liga', 2, 1, 'CONMEBOL',
                'Inclui a Taça de Prata (1980-1984) e a segunda divisão de 1971-1972')""").lastrowid

    # ---- clubes: os usados em algum fato, um por nome de exibição
    usados: set[int] = set()
    for t, cols in [("fato_partida", ("mandante_id", "visitante_id")), ("fato_partida_nacional_historica", ("mandante_id", "visitante_id")),
                    ("fato_classificacao_final_nacional", ("clube_id",)), ("fato_gol", ("clube_id",)), ("fato_cartao", ("clube_id",)),
                    ("fato_classificacao_rodada", ("clube_id",)), ("fato_stats_time", ("clube_id",)), ("fato_partida_serie_b", ("mandante_id", "visitante_id")),
                    ("fato_classificacao_final_serie_b", ("clube_id",)), ("fato_artilheiro_serie_b", ("clube_id",))]:
        for c in cols:
            usados |= {r[0] for r in a.execute(f"SELECT DISTINCT {c} FROM {t}") if r[0] is not None}
    por_nome: dict[str, list] = defaultdict(list)
    for cid, nm, uf in a.execute("SELECT clube_id, nome, uf FROM dim_clube"):
        if cid in usados:
            disp = exibir(nm)
            uf_ok = (uf or "").strip() if (uf or "").strip() in UFS else None   # "RP" (Ribeirão Preto) não é estado
            por_nome[MESCLAR.get(disp, disp)].append((cid, nm, uf_ok or uf_do_nome(disp) or ("SP" if disp.endswith("-RP") else None)))
    novo_id: dict[int, int] = {}
    conflitos = []
    for disp, linhas in sorted(por_nome.items()):
        ufs = {u for _, _, u in linhas if u}
        if len(ufs) > 1:
            conflitos.append((disp, linhas))
        cid_novo = b.execute("INSERT INTO clube (nome, pais_id, regiao) VALUES (?, 1, ?)", (disp, next(iter(sorted(ufs)), None))).lastrowid
        for cid, nm, _ in linhas:
            novo_id[cid] = cid_novo
            b.execute("INSERT OR IGNORE INTO clube_nome VALUES (?,?,?,?,?,?)", (cid_novo, nm, chave(nm), "brasileirao.db", None, None))
    # estado que faltava: identificação da Série B, depois a lista manual
    sys.path.insert(0, str(RAIZ / "serie_b"))
    import clubes as clubes_b, importar as importar_b
    uf_b = {c["clube"]: c["uf"] for c in clubes_b.canonicos(clubes_b.resolver_todos()).values() if c["uf"]}
    uf_b.update(importar_b.EXTRAS)
    for cid, nm in b.execute("SELECT clube_id, nome FROM clube WHERE regiao IS NULL").fetchall():
        uf = uf_b.get(nm) or UF_MANUAL.get(nm)
        if uf:
            b.execute("UPDATE clube SET regiao = ? WHERE clube_id = ?", (uf, cid))
    # nomes que cada fonte usa (aprendidos na Série B), com os anos em que apareceram
    import nomes as nomes_b
    id_por_nome = {nm: cid for cid, nm in b.execute("SELECT clube_id, nome FROM clube")}
    vistos: dict[tuple, list] = {}
    def guardar(nome_fonte: str, fonte: str, clube_nome: str | None, ano: int) -> None:
        cid = id_por_nome.get(MESCLAR.get(clube_nome, clube_nome)) if clube_nome else None
        if cid:
            k = (cid, nome_fonte, fonte)
            vistos[k] = [min(vistos.get(k, [ano])[0], ano), max(vistos.get(k, [ano, ano])[1], ano)]
    for (ano, bruto), c in clubes_b.canonicos(clubes_b.resolver_todos()).items():
        guardar(bruto, "rsssf", c["clube"], ano)
    for ano, ns in nomes_b.externos().items():
        for n in ns:
            guardar(n, "espn/ogol/wikipedia", nomes_b.casar(n, ano), ano)
    for (cid, nome_fonte, fonte), (a1, a2) in vistos.items():
        b.execute("INSERT OR IGNORE INTO clube_nome VALUES (?,?,?,?,?,?)", (cid, nome_fonte, chave(nome_fonte), fonte, a1, a2))
    for nome_alias, cid in a.execute("SELECT alias, clube_id FROM dim_clube_alias"):
        if cid in novo_id:
            b.execute("INSERT OR IGNORE INTO clube_nome VALUES (?,?,?,?,?,?)", (novo_id[cid], nome_alias, chave(nome_alias), "classificacao_codex", None, None))

    # ---- Série A antiga e moderna
    edicao_de: dict[int, int] = {}       # edicao_nacional_id -> edicao_id
    ed_moderna: dict[int, int] = {}      # temporada (2003+) -> edicao_id
    for eid, chave_ed, ano, comp, tipo, fonte, obs, n, pv in a.execute(
            """SELECT edicao_nacional_id, edicao_id, temporada_id, competicao_nome, tipo, fonte_principal, observacao, num_clubes, pontos_vitoria
               FROM dim_edicao_nacional ORDER BY temporada_id, edicao_id"""):
        formato = "mata-mata" if tipo in ("taca_brasil", "torneio_dos_campeoes") else None
        novo = b.execute("""INSERT INTO edicao (competicao_id, temporada, ano_inicio, ano_fim, nome_oficial, chave, num_clubes, pontos_vitoria, formato, fontes, observacao)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                         (serie_a, str(ano), ano, ano, None if comp == "Campeonato Brasileiro" else comp, chave_ed, n, pv, formato, fonte, obs)).lastrowid
        edicao_de[eid] = novo
        if ano >= 2003:
            ed_moderna[ano] = novo
    fase_de: dict[int, int] = {}
    for fid, eid, ordem, nome_f, tipo_f, obs, ng, serie, crit in a.execute(
            "SELECT fase_nacional_id, edicao_nacional_id, fase_ordem, fase_nome, fase_tipo, observacao, num_grupos, formato_serie, criterio FROM dim_fase_nacional_historica"):
        tipo_n = {"liga": "liga", "grupo": "grupos", "mata_mata": "mata_mata"}.get(tipo_f, tipo_f)
        fase_de[fid] = b.execute("INSERT INTO fase (edicao_id, ordem, nome, tipo, num_grupos, formato_serie, criterio, observacao) VALUES (?,?,?,?,?,?,?,?)",
                                 (edicao_de[eid], ordem, nome_f, tipo_n, ng, serie, crit, obs)).lastrowid
    for (pid, eid, fid, rodada, jogo, data, m, v, gm, gv, fonte, obs, grupo) in a.execute(
            """SELECT partida_hist_id, edicao_nacional_id, fase_nacional_id, rodada, jogo, data, mandante_id, visitante_id,
                      gols_mandante, gols_visitante, fonte, observacao, grupo FROM fato_partida_nacional_historica"""):
        b.execute("""INSERT INTO partida (edicao_id, fase_id, grupo, rodada, data, mandante_id, visitante_id, gols_mandante, gols_visitante, fonte, fonte_id, observacao)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                  (edicao_de[eid], fase_de[fid], grupo, rodada, data, novo_id[m], novo_id[v], gm, gv, fonte, f"jogo {jogo}" if jogo else None, obs))
    fase_unica = {}
    for ano, ed in ed_moderna.items():
        fase_unica[ano] = b.execute("INSERT INTO fase (edicao_id, ordem, nome, tipo, formato_serie) VALUES (?,?,?,?,?)",
                                    (ed, 1, "Fase única", "liga", "pontos_corridos")).lastrowid
        b.execute("UPDATE edicao SET formato = 'pontos corridos, turno e returno' WHERE edicao_id = ?", (ed,))
    arena = dict(a.execute("SELECT arena_id, nome FROM dim_arena"))
    tecnico = dict(a.execute("SELECT tecnico_id, nome FROM dim_tecnico"))
    partida_de: dict[int, int] = {}
    for (pid, ano, rodada, data, hora, m, v, ar, gm, gv, tm, tv, fm, fv, arrec) in a.execute(
            """SELECT partida_id, temporada_id, rodada, data, hora, mandante_id, visitante_id, arena_id, gols_mandante, gols_visitante,
                      tecnico_mand_id, tecnico_vis_id, formacao_mandante, formacao_visitante, arrecadacao FROM fato_partida"""):
        partida_de[pid] = b.execute(
            """INSERT INTO partida (edicao_id, fase_id, rodada, data, hora, mandante_id, visitante_id, gols_mandante, gols_visitante, estadio,
                                    arrecadacao, tecnico_mandante, tecnico_visitante, formacao_mandante, formacao_visitante, fonte, fonte_id)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (ed_moderna[ano], fase_unica[ano], rodada, data, hora, novo_id[m], novo_id[v], gm, gv, arena.get(ar), arrec,
             tecnico.get(tm), tecnico.get(tv), fm, fv, "brasileirao.db (Série A 2003+)", str(pid))).lastrowid
    jogador = dict(a.execute("SELECT jogador_id, nome FROM dim_jogador"))
    for pid, c, jid, mi, tipo in a.execute("SELECT partida_id, clube_id, jogador_id, minuto, tipo FROM fato_gol"):
        b.execute("INSERT INTO gol (partida_id, clube_id, jogador, minuto, tipo, fonte) VALUES (?,?,?,?,?,?)",
                  (partida_de[pid], novo_id[c], jogador.get(jid), mi, TIPO_GOL.get((tipo or "normal").lower(), "normal"), "brasileirao.db"))
    for pid, c, jid, tipo, mi in a.execute("SELECT partida_id, clube_id, jogador_id, tipo, minuto FROM fato_cartao"):
        cor = "vermelho" if tipo and "verm" in tipo.lower() else "amarelo"
        b.execute("INSERT INTO cartao (partida_id, clube_id, jogador, minuto, cor, fonte) VALUES (?,?,?,?,?,?)",
                  (partida_de[pid], novo_id[c], jogador.get(jid), mi, cor, "brasileirao.db"))
    for row in a.execute("""SELECT partida_id, clube_id, chutes, chutes_alvo, posse, passes, prec_passes, faltas, amarelos, vermelhos,
                                   impedimentos, escanteios FROM fato_stats_time"""):
        if row[0] in partida_de:
            b.execute("INSERT OR IGNORE INTO estatistica_partida VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (partida_de[row[0]], novo_id[row[1]], *row[2:], "brasileirao.db"))
    for ano, rodada, c, pos, pts, j, v, e, d, gp, gc, zona in a.execute(
            "SELECT temporada_id, rodada, clube_id, posicao, pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, zona FROM fato_classificacao_rodada"):
        b.execute("INSERT INTO classificacao_rodada VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (ed_moderna[ano], rodada, novo_id[c], pos, pts, j, v, e, d, gp, gc, zona))
    # classificação final: posição do banco antigo; números somados dos jogos; pontos da última rodada (com punições) quando há
    for eid, c, pos, fonte, obs in a.execute("SELECT edicao_nacional_id, clube_id, posicao, fonte, observacao FROM fato_classificacao_final_nacional"):
        b.execute("INSERT INTO classificacao_final (edicao_id, clube_id, posicao, fonte, observacao) VALUES (?,?,?,?,?)",
                  (edicao_de[eid], novo_id[c], pos, fonte, obs))

    # ---- Série B
    ed_b = {}
    for ano, n, pv, campeao, vice, fontes, obs in a.execute(
            "SELECT edicao_serie_b_id, num_clubes, pontos_vitoria, campeao_id, vice_id, fontes, observacao FROM dim_edicao_serie_b"):
        ed_b[ano] = b.execute("""INSERT INTO edicao (competicao_id, temporada, ano_inicio, ano_fim, nome_oficial, chave, num_clubes, pontos_vitoria,
                                                     campeao_id, vice_id, fontes, observacao) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                              (serie_b, str(ano), ano, ano, "Taça de Prata" if 1980 <= ano <= 1984 else None, str(ano), n, pv,
                               novo_id.get(campeao), novo_id.get(vice), fontes, obs)).lastrowid
    fase_b = {}
    for fid, ano, ordem, nome_f, ng in a.execute("SELECT fase_serie_b_id, edicao_serie_b_id, fase_ordem, fase_nome, num_grupos FROM dim_fase_serie_b"):
        tipo_f = "liga" if nome_f == "Fase única" else "grupos" if ng else "mata_mata" if any(
            k in nome_f.lower() for k in ("final", "semi", "quartas", "oitavas", "mata")) else None
        fase_b[fid] = b.execute("INSERT INTO fase (edicao_id, ordem, nome, tipo, num_grupos) VALUES (?,?,?,?,?)", (ed_b[ano], ordem, nome_f, tipo_f, ng)).lastrowid
    partida_b = {}
    for row in a.execute("""SELECT partida_serie_b_id, edicao_serie_b_id, fase_serie_b_id, grupo, rodada, data, hora, mandante_id, visitante_id,
                                   gols_mandante, gols_visitante, resultado_especial, estadio, cidade, publico, espn_id, gols_texto, fonte, observacao
                            FROM fato_partida_serie_b"""):
        (pid, ano, fid, grupo, rodada, data, hora, m, v, gm, gv, esp, est, cid, pub, espn, gtxt, fonte, obs) = row
        partida_b[pid] = b.execute(
            """INSERT INTO partida (edicao_id, fase_id, grupo, rodada, data, hora, mandante_id, visitante_id, gols_mandante, gols_visitante,
                                    resultado_especial, estadio, cidade, publico, gols_texto, fonte, fonte_id, observacao)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (ed_b[ano], fase_b[fid], grupo, rodada, data, hora, novo_id[m], novo_id[v], gm, gv, esp, est, cid, pub, gtxt, fonte,
             f"espn {espn}" if espn else None, obs)).lastrowid
    for pid, c, jog, mi, ac, tipo, fonte in a.execute("SELECT partida_serie_b_id, clube_id, jogador, minuto, acrescimo, tipo, fonte FROM fato_gol_serie_b"):
        b.execute("INSERT INTO gol (partida_id, clube_id, jogador, minuto, acrescimo, tipo, fonte) VALUES (?,?,?,?,?,?,?)",
                  (partida_b[pid], novo_id[c], jog, mi, ac, tipo, fonte))
    for pid, c, jog, mi, ac, cor, fonte in a.execute("SELECT partida_serie_b_id, clube_id, jogador, minuto, acrescimo, cor, fonte FROM fato_cartao_serie_b"):
        b.execute("INSERT INTO cartao (partida_id, clube_id, jogador, minuto, acrescimo, cor, fonte) VALUES (?,?,?,?,?,?,?)",
                  (partida_b[pid], novo_id[c], jog, mi, ac, cor, fonte))
    for ano, c, pos, j, v, e, d, gp, gc, pts, aj, fonte in a.execute(
            "SELECT edicao_serie_b_id, clube_id, posicao, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos, ajuste_pontos, fonte FROM fato_classificacao_final_serie_b"):
        b.execute("INSERT INTO classificacao_final (edicao_id, clube_id, posicao, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos, ajuste_pontos, fonte) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                  (ed_b[ano], novo_id[c], pos, j, v, e, d, gp, gc, pts, aj, fonte))
    # zona da posição na Série B de pontos corridos (2006+, 20 clubes): campeão, acesso (2º ao 4º) e rebaixamento (4 últimos)
    zona_b = lambda pos: "titulo" if pos == 1 else "acesso" if pos <= 4 else "rebaixamento" if pos >= 17 else "meio"
    for ano, rodada, c, pos, pts, j, v, e, d, gp, gc in a.execute("SELECT * FROM fato_classificacao_rodada_serie_b"):
        b.execute("INSERT INTO classificacao_rodada VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (ed_b[ano], rodada, novo_id[c], pos, pts, j, v, e, d, gp, gc, zona_b(pos)))
    for ano, fase_n, grupo, pos, c, nf, j, v, e, d, gp, gc, pts in a.execute("SELECT * FROM fato_tabela_fase_serie_b"):
        b.execute("INSERT INTO tabela_publicada VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (ed_b[ano], fase_n, grupo, pos, novo_id.get(c), nf, j, v, e, d, gp, gc, pts, "rsssf"))
    for ano, jog, c, cf, n, fonte in a.execute("SELECT * FROM fato_artilheiro_serie_b"):
        b.execute("INSERT INTO artilheiro VALUES (?,?,?,?,?)", (ed_b[ano], jog, novo_id.get(c), n, fonte))

    corrigir_serie_a(b, serie_a)
    # ---- números da classificação final da Série A (somados dos jogos; pontos da última rodada quando há)
    for (ed,) in b.execute("SELECT edicao_id FROM edicao WHERE competicao_id = ?", (serie_a,)).fetchall():
        pv = b.execute("SELECT pontos_vitoria FROM edicao WHERE edicao_id = ?", (ed,)).fetchone()[0] or 2
        camp = defaultdict(lambda: [0] * 6)
        for m, v, gm, gv in b.execute("SELECT mandante_id, visitante_id, gols_mandante, gols_visitante FROM partida WHERE edicao_id = ?", (ed,)):
            for eu, x, y in ((m, gm, gv), (v, gv, gm)):
                c = camp[eu]; c[0] += 1; c[4] += x; c[5] += y; c[1 if x > y else 2 if x == y else 3] += 1
        ultima = dict(b.execute("""SELECT clube_id, pontos FROM classificacao_rodada WHERE edicao_id = ? AND rodada =
                                   (SELECT max(rodada) FROM classificacao_rodada WHERE edicao_id = ?)""", (ed, ed)).fetchall())
        for c, (j, v, e, d, gp, gc) in camp.items():
            pts_calc = pv * v + e
            pts = ultima.get(c, pts_calc)
            b.execute("""UPDATE classificacao_final SET jogos=?, vitorias=?, empates=?, derrotas=?, gols_pro=?, gols_contra=?, pontos=?, ajuste_pontos=?
                         WHERE edicao_id=? AND clube_id=?""", (j, v, e, d, gp, gc, pts, pts - pts_calc, ed, c))
        top = b.execute("SELECT clube_id FROM classificacao_final WHERE edicao_id = ? ORDER BY posicao LIMIT 2", (ed,)).fetchall()
        b.execute("UPDATE edicao SET campeao_id = ?, vice_id = ? WHERE edicao_id = ?", (top[0][0] if top else None, top[1][0] if len(top) > 1 else None, ed))
    oficial_serie_a(b, serie_a)
    separar(b)
    b.commit()
    conferir(a, b, conflitos)
    import carregar_pacotes
    for slug in carregar_pacotes.pacotes():
        carregar_pacotes.carregar(b, slug)


def corrigir_serie_a(b: sqlite3.Connection, serie_a: int) -> None:
    """Erros do banco antigo achados pela revisão (docs/revisao/bra-serie-a.md), com a fonte de cada um."""
    def jogo(chave_ed: str, mandante: str, visitante: str, extra: str = "", *args) -> int:
        (pid,) = b.execute(f"""SELECT p.partida_id FROM partida p JOIN edicao e USING (edicao_id) JOIN clube m ON m.clube_id = p.mandante_id
                               JOIN clube v ON v.clube_id = p.visitante_id JOIN fase f USING (fase_id)
                               WHERE e.competicao_id = ? AND e.chave = ? AND m.nome = ? AND v.nome = ? {extra}""",
                           (serie_a, chave_ed, mandante, visitante, *args)).fetchone()
        return pid
    cid = lambda nome: b.execute("SELECT clube_id FROM clube WHERE nome = ?", (nome,)).fetchone()[0]
    # SA-010: rodada 12 de 2009 foi Flamengo 2-2 Botafogo (mando do Flamengo); o returno, Botafogo 0-1 Flamengo
    b.execute("UPDATE partida SET mandante_id = visitante_id, visitante_id = mandante_id WHERE partida_id = ?",
              (jogo("2009", "Botafogo", "Flamengo", "AND p.rodada = 12"),))
    # SA-011: final da CBF de 1987, ida Guarani 1-1 Sport em 30/01/1988 e volta Sport 1-0 Guarani em 07/02/1988 (Wikipédia en e pt)
    b.execute("UPDATE partida SET gols_mandante = 1, gols_visitante = 1, data = '1988-01-30', observacao = ? WHERE partida_id = ?",
              ("Final da CBF, ida: 1-1 (Catatau; Betão, de pênalti). Wikipédia en e pt.", jogo("1987", "Guarani", "Sport")))
    b.execute("UPDATE partida SET data = '1988-02-07' WHERE partida_id = ?", (jogo("1987", "Sport", "Guarani"),))
    # SA-012: quartas de 2001, Fluminense 2-1 Ponte Preta na prorrogação (o placar guarda a prorrogação)
    b.execute("UPDATE partida SET gols_mandante = 2, gols_visitante = 1 WHERE partida_id = ?",
              (jogo("2001", "Fluminense", "Ponte Preta", "AND f.nome = 'Quartas de final'"),))
    # SA-013: Taça Brasil 1959, desempate da Zona Norte, Ceará 2-1 ABC no Presidente Vargas (Wikipédia pt)
    ed, fase, grupo = b.execute("SELECT edicao_id, fase_id, grupo FROM partida WHERE partida_id = ?", (jogo("1959", "ABC", "Ceará"),)).fetchone()
    pid = b.execute("""INSERT INTO partida (edicao_id, fase_id, grupo, mandante_id, visitante_id, gols_mandante, gols_visitante, estadio, fonte, observacao)
                       VALUES (?,?,?,?,?,2,1,'Presidente Vargas','Wikipédia pt','Jogo de desempate da Zona Norte.')""",
                    (ed, fase, grupo, cid("Ceará"), cid("ABC"))).lastrowid
    for clube, jog in (("Ceará", "Claudinho"), ("Ceará", "Doca"), ("ABC", "Tiquinho")):
        b.execute("INSERT INTO gol (partida_id, clube_id, jogador, tipo, fonte) VALUES (?,?,?,'normal','Wikipédia pt')", (pid, cid(clube), jog))
    # SA-007: Robertão 1968, quadrangular final com os três em 2 pontos: vice Internacional (saldo +1), 3º Vasco, 4º Palmeiras
    (ed,) = b.execute("SELECT edicao_id FROM edicao WHERE competicao_id = ? AND chave = '1968_robertao'", (serie_a,)).fetchone()
    for pos, clube in ((2, "Internacional"), (3, "Vasco"), (4, "Palmeiras")):
        b.execute("UPDATE classificacao_final SET posicao = ? WHERE edicao_id = ? AND clube_id = ?", (pos, ed, cid(clube)))
    # SA-027: 2000 foi a Copa João Havelange; SA-028: acento no nome da fase de 1987
    b.execute("UPDATE edicao SET nome_oficial = 'Copa João Havelange' WHERE competicao_id = ? AND ano_inicio = 2000", (serie_a,))
    b.execute("UPDATE fase SET nome = replace(nome, 'Copa Uniao', 'Copa União') WHERE nome LIKE '%Copa Uniao%'")


def oficial_serie_a(b: sqlite3.Connection, serie_a: int) -> None:
    """Série A de pontos corridos: ordem final e punições do STJD da tabela oficial (futebol/oficial_serie_a.py).
    Os pontos ficam = vitória x pontos + empates + ajuste; vitórias, empates e gols continuam os dos jogos."""
    import oficial_serie_a as of
    for ed, ano, pv in b.execute("SELECT edicao_id, ano_inicio, pontos_vitoria FROM edicao WHERE competicao_id = ? AND ano_inicio >= 2003",
                                 (serie_a,)).fetchall():
        do_ano = {cid: (nm, ) for cid, nm in b.execute("SELECT c.clube_id, c.nome FROM classificacao_final f JOIN clube c USING (clube_id) WHERE f.edicao_id = ?", (ed,))}
        chaves: dict[str, set] = defaultdict(set)
        for cid, (nm,) in do_ano.items():
            chaves[chave(nm)].add(cid)
            for (n,) in b.execute("SELECT nome_chave FROM clube_nome WHERE clube_id = ?", (cid,)):
                chaves[n].add(cid)
        achar = lambda nome: next(iter(chaves[chave(nome)])) if len(chaves.get(chave(nome), ())) == 1 else None
        tab = of.oficial(ano, achar)
        if not tab or set(tab) != set(do_ano):
            print(f"  Série A {ano}: tabela oficial não casou com os clubes do banco; fica a classificação antiga")
            continue
        for cid, (pos, aj) in tab.items():
            b.execute("""UPDATE classificacao_final SET posicao = ?, ajuste_pontos = ?, pontos = ? * vitorias + empates + ?,
                         fonte = 'Wikipédia en (tabela oficial, com punições)' WHERE edicao_id = ? AND clube_id = ?""", (pos, aj, pv or 3, aj, ed, cid))
        dif = [(do_ano[cid][0], r["v"], r["e"], r["d"]) for r in of.tabela(ano) for cid in [achar(r["nome"])]
               if b.execute("SELECT vitorias, empates, derrotas FROM classificacao_final WHERE edicao_id = ? AND clube_id = ?", (ed, cid)).fetchone() != (r["v"], r["e"], r["d"])]
        if dif:
            print(f"  Série A {ano}: V/E/D da tabela oficial diferente dos jogos do banco:", dif[:6])
        top = b.execute("SELECT clube_id FROM classificacao_final WHERE edicao_id = ? ORDER BY posicao LIMIT 2", (ed,)).fetchall()
        b.execute("UPDATE edicao SET campeao_id = ?, vice_id = ? WHERE edicao_id = ?", (top[0][0], top[1][0], ed))


def separar(b: sqlite3.Connection) -> None:
    """Passa para um clube novo (o antigo) tudo o que o nome de SEPARAR tem até o último ano dele."""
    for nome, antigo, uf, ate in SEPARAR:
        (cid,) = b.execute("SELECT clube_id FROM clube WHERE nome = ?", (nome,)).fetchone()
        novo = b.execute("INSERT INTO clube (nome, pais_id, regiao) VALUES (?, 1, ?)", (antigo, uf)).lastrowid
        eds = f"SELECT edicao_id FROM edicao WHERE ano_inicio <= {int(ate)}"
        pts = f"SELECT partida_id FROM partida WHERE edicao_id IN ({eds})"
        for t, col, onde in [("partida", "mandante_id", eds), ("partida", "visitante_id", eds), ("gol", "clube_id", pts), ("cartao", "clube_id", pts),
                             ("estatistica_partida", "clube_id", pts), ("classificacao_final", "clube_id", eds), ("classificacao_rodada", "clube_id", eds),
                             ("tabela_publicada", "clube_id", eds), ("artilheiro", "clube_id", eds), ("edicao", "campeao_id", eds), ("edicao", "vice_id", eds)]:
            chave_t = "partida_id" if onde is pts else "edicao_id"
            b.execute(f"UPDATE {t} SET {col} = ? WHERE {col} = ? AND {chave_t} IN ({onde})", (novo, cid))
        b.execute("UPDATE clube_nome SET clube_id = ? WHERE clube_id = ? AND ano_fim <= ?", (novo, cid, ate))
        # nome que cobre os dois períodos (ex.: rsssf "Novorizontino" 1989-2024): parte do antigo até `ate`, o resto fica (CL-030)
        for nm, k, fonte, a1, a2 in b.execute("SELECT nome, nome_chave, fonte, ano_inicio, ano_fim FROM clube_nome WHERE clube_id = ? AND ano_inicio <= ? AND ano_fim > ?",
                                              (cid, ate, ate)).fetchall():
            b.execute("INSERT OR IGNORE INTO clube_nome VALUES (?,?,?,?,?,?)", (novo, nm, k, fonte, a1, ate))
            depois = b.execute("SELECT min(e.ano_inicio) FROM classificacao_final f JOIN edicao e USING (edicao_id) WHERE f.clube_id = ? AND e.ano_inicio > ?",
                               (cid, ate)).fetchone()[0]
            b.execute("UPDATE clube_nome SET ano_inicio = ? WHERE clube_id = ? AND nome_chave = ? AND fonte = ?", (depois or ate + 1, cid, k, fonte))


def conferir(a: sqlite3.Connection, b: sqlite3.Connection, conflitos: list) -> None:
    """Contagens do banco novo contra o antigo (por competição) e campeões."""
    sys.stdout.reconfigure(encoding="utf-8")
    origem = {
        "Série A": (a.execute("SELECT (SELECT count(*) FROM fato_partida) + (SELECT count(*) FROM fato_partida_nacional_historica)").fetchone()[0],
                    a.execute("""SELECT (SELECT sum(gols_mandante + gols_visitante) FROM fato_partida) +
                                        (SELECT sum(gols_mandante + gols_visitante) FROM fato_partida_nacional_historica)""").fetchone()[0],
                    a.execute("SELECT count(*) FROM fato_gol").fetchone()[0], a.execute("SELECT count(*) FROM fato_classificacao_final_nacional").fetchone()[0]),
        "Série B": (a.execute("SELECT count(*) FROM fato_partida_serie_b").fetchone()[0],
                    a.execute("SELECT sum(coalesce(gols_mandante,0) + coalesce(gols_visitante,0)) FROM fato_partida_serie_b").fetchone()[0],
                    a.execute("SELECT count(*) FROM fato_gol_serie_b").fetchone()[0], a.execute("SELECT count(*) FROM fato_classificacao_final_serie_b").fetchone()[0]),
    }
    # corrigir_serie_a: +1 jogo (desempate de 1959), +6 gols (3 do desempate, 2 da final de 1987, 1 da prorrogação de 2001), +3 autores
    j, g, au, f = origem["Série A"]
    origem["Série A"] = (j + 1, g + 6, au + 3, f)
    for nome_c, (jogos, gols, autores, final) in origem.items():
        n = b.execute("""SELECT count(*), sum(coalesce(gols_mandante,0) + coalesce(gols_visitante,0)) FROM partida p JOIN edicao e USING (edicao_id)
                         JOIN competicao c USING (competicao_id) WHERE c.nome_curto = ?""", (nome_c,)).fetchone()
        g = b.execute("""SELECT count(*) FROM gol JOIN partida USING (partida_id) JOIN edicao USING (edicao_id) JOIN competicao c USING (competicao_id)
                         WHERE c.nome_curto = ?""", (nome_c,)).fetchone()[0]
        f = b.execute("""SELECT count(*) FROM classificacao_final JOIN edicao USING (edicao_id) JOIN competicao c USING (competicao_id)
                         WHERE c.nome_curto = ?""", (nome_c,)).fetchone()[0]
        ok = (n[0], n[1], g, f) == (jogos, gols, autores, final)
        print(f"{nome_c}: jogos {n[0]}/{jogos}, gols {n[1]}/{gols}, gols com autor {g}/{autores}, classificação {f}/{final} -> {'OK' if ok else 'DIFERENTE'}")
    print("clubes:", b.execute("SELECT count(*) FROM clube").fetchone()[0], "| nomes guardados:", b.execute("SELECT count(*) FROM clube_nome").fetchone()[0])
    sem_estado = [r[0] for r in b.execute("SELECT nome FROM clube WHERE regiao IS NULL")]
    print("clubes sem estado:", len(sem_estado), sem_estado[:30])
    if conflitos:
        print("nomes de exibição com mais de um estado no banco antigo (conferir):")
        for disp, linhas in conflitos:
            print("  ", disp, linhas)
    print("campeões:", b.execute("""SELECT c2.nome_curto, e.temporada, cl.nome FROM edicao e JOIN competicao c2 USING (competicao_id)
                                     JOIN clube cl ON cl.clube_id = e.campeao_id WHERE e.temporada IN ('1937', '1971', '2025') ORDER BY 1, 2""").fetchall())


if __name__ == "__main__":
    migrar()
