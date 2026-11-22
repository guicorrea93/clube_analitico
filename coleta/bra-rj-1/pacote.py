"""Grava o pacote do Campeonato Carioca (data/coleta/bra-rj-1/pacote/) e o relatório (docs/coleta/bra-rj-1.md),
no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py.
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
from collections import Counter, defaultdict

import clubes_rj1
from edicoes import NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RAIZ, RELATORIO, SLUG
from importar import ORDEM, fonte_rsssf, nome, pontos_vitoria
from rsssf_rj1 import rsssf


def _csv(arquivo: str, cabecalho: list[str], linhas: list[list]) -> None:
    PACOTE.mkdir(parents=True, exist_ok=True)
    with open(PACOTE / arquivo, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        for l in linhas:
            w.writerow(["" if x is None else x for x in l])


def serie_b_por_ano() -> dict[int, set[str]]:
    """Clubes (nome de exibição do futebol.db) que jogaram a Série B em cada ano: marca o acesso da Copa do Brasil."""
    con = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    saida: dict[int, set[str]] = defaultdict(set)
    for ano, n in con.execute("""SELECT e.ano_inicio, c.nome FROM classificacao_final f JOIN edicao e USING (edicao_id)
                                 JOIN competicao k USING (competicao_id) JOIN clube c USING (clube_id) WHERE k.slug = 'bra-serie-b'"""):
        saida[int(ano)].add(n)
    con.close()
    return saida


def infobox(ano: int) -> dict:
    """Campos do infobox da Wikipédia em português: promovidos, rebaixados e artilheiros [(jogador, clube, gols)]."""
    f = PASTA_DADOS / "wikipedia" / f"pt_{ano}.txt"
    t = f.read_text(encoding="utf-8") if f.exists() else ""
    def campo(nome_campo):
        m = re.search(rf"^\s*\|{nome_campo}\s*=(.*?)(?=^\s*\|\w+\s*=)", t, re.M | re.S)
        return m.group(1) if m else ""
    times = lambda s: [x.strip() for x in re.findall(r"\{\{\s*[Ff]utebol\s+([^}|]+)\}\}", s)]
    art = []
    bloco = campo("artilheiro")
    gols = re.search(r"(\d+)\s*gols", bloco)
    for jog, clube in re.findall(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]\s*\(\{\{\s*[Ff]utebol\s+([^}|]+)\}\}\)", bloco):
        if gols:
            art.append((jog.strip(), clube.strip(), int(gols.group(1))))
    return {"promovidos": times(campo("promovidos")), "rebaixados": times(campo("rebaixados")), "artilheiros": art}


def tipo_fase(ps: list) -> tuple[str, int | None, str]:
    """(tipo, nº de grupos, formato da série) de uma fase, pelo desenho dos jogos."""
    pares = Counter(frozenset((p.mandante, p.visitante)) for p in ps)
    clubes = Counter(x for par in pares for x in par)
    if pares and all(n == 1 for n in clubes.values()):   # cada clube enfrenta um adversário só: mata-mata
        n = Counter(pares.values()).most_common(1)[0][0]
        return "mata_mata", None, {1: "jogo_unico", 2: "ida_volta", 3: "melhor_de_3"}.get(n, "ida_volta")
    grupos = {p.grupo for p in ps if p.grupo}
    return ("grupos" if len(grupos) >= 2 else "liga"), (len(grupos) or None), "pontos_corridos"


def gravar(edicoes: dict, log: list[str], rs_c: dict, wk_c: dict) -> None:
    ex = clubes_rj1.exibicao()
    serie_b = serie_b_por_ano()
    # ------------------------------------------------------------------ competicao.json
    PACOTE.mkdir(parents=True, exist_ok=True)
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": SLUG, "nome": "Campeonato Carioca", "nome_curto": "Carioca", "tipo": "estadual", "nivel": 1, "pais": "BRA",
        "regiao": "RJ", "confederacao": "CONMEBOL",
        "observacao": "1ª divisão do Rio de Janeiro, de 1906 a 2026: até 1959 o campeonato do Distrito Federal (a cidade do Rio), "
                      "de 1960 a 1974 o do estado da Guanabara e, depois da fusão de 1975, o do estado do Rio de Janeiro. Nos anos "
                      "de ligas rivais (1912, 1924, 1933-1936) cada torneio reconhecido é uma edição (\"1933 AMEA\", \"1933 LCF\"); "
                      "1979 teve o campeonato normal e o Especial.",
        "rotulo_painel": "Carioca", "menu_painel": "Carioca", "do_painel": "do Carioca", "o_painel": "o Carioca"},
        ensure_ascii=False, indent=1), encoding="utf-8")
    # ------------------------------------------------------------------ partidas, gols, fases, edições
    linhas_p, linhas_g, linhas_f, linhas_e, linhas_cf, linhas_tp, linhas_conf, linhas_art = [], [], [], [], [], [], [], []
    linhas_rod: list[list] = []
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    usados: set[str] = set()
    artilheiros_rsssf = artilheiros()
    for ano, e in edicoes.items():
        ps = e["partidas"]
        for n, cid in e["mapa"].items():
            nomes_fonte[cid][f"rsssf:{n[0] if isinstance(n, tuple) else n}"].append(ano)
        for o in e["og"]:
            for lado in ("mandante", "visitante"):
                if o.get(f"{lado}_id"):
                    nomes_fonte[o[f"{lado}_id"]][f"ogol:{o[lado]}"].append(ano)
        # fases na ordem da competição
        por_fase = defaultdict(list)
        for p in ps:
            por_fase[p.fase].append(p)
        fases = sorted(por_fase, key=lambda f: (ORDEM.get(f, 0) if f != "Fase única" else 1, min(p.data or "9999" for p in por_fase[f])))
        desenho = []
        for i, f in enumerate(fases, 1):
            tipo, ng, serie = tipo_fase(por_fase[f])
            if tipo == "mata_mata":
                for p in por_fase[f]:
                    p.grupo = ""
            linhas_f.append([str(ano), i, f, tipo, ng, serie, ""])
            if tipo == "liga" and serie == "pontos_corridos":
                todos = {x for q in ps for x in (q.mandante, q.visitante)}
                linhas_rod += classificacao_rodada(str(ano), f, por_fase[f], e, ultima=(i == len(fases)), todos=todos)
            desenho.append({"grupos": f"{ng} grupos", "liga": "pontos corridos", "mata_mata": "mata-mata"}[tipo])
        ordem_jogo = sorted(ps, key=lambda p: (fases.index(p.fase), p.grupo, p.data or "9999", p.hora or "", p.linha))
        for k, p in enumerate(ordem_jogo, 1):
            pid = f"{ano}-{k:04d}"
            usados |= {p.mandante, p.visitante}
            linhas_p.append([pid, str(ano), p.fase, p.grupo, p.rodada, p.data, p.hora, nome(p.mandante), nome(p.visitante), p.gm, p.gv,
                             p.pen_m, p.pen_v, normalizar_especial(p.especial), p.estadio, p.cidade, p.publico, fonte_curta(p.fonte),
                             p.fonte_id, p.gols_texto.strip() if p.gols_texto and not p.gols else "", p.obs.strip("; ")])
            for g in p.gols:
                linhas_g.append([pid, nome(p.mandante if g["lado"] == "mandante" else p.visitante), g["jogador"], g["minuto"],
                                 g["acrescimo"], g["tipo"], g["fonte"]])
        # classificação final
        final = e["final"]
        campeao = e["campeao"]
        rebaixados = rebaixados_rsssf(e)   # marcas "Relegated" das tabelas da RSSSF
        ib = infobox(ano)
        subiram: set = set()   # 1ª divisão: acesso é de quem vem da A2 (fica para o pacote bra-sp-2)
        for f in final:
            c = f["clube"]
            sit = "campeao" if c == campeao else "acesso" if nome(c) in subiram else "rebaixado" if c in rebaixados else ""
            if f["pos"] == 2 and sit == "" and len(final) > 1 and campeao:
                sit = "vice"
            linhas_cf.append([str(ano), f["pos"], nome(c), f["j"], f["v"], f["e"], f["d"], f["gp"], f["gc"], f["pts"], f["ajuste"] or 0, sit,
                              f["fonte"], "punição de pontos (Wikipédia)" if f["ajuste"] else ""])
        # tabelas publicadas
        for tb, linhas, nome_id in e["tabs"]:
            for r in tb.linhas:
                c = nome_id.get(r["nome"], "")
                linhas_tp.append([str(ano), tb.fase, tb.grupo, r["pos"], r["nome"], nome(c) if c else "", r["j"], r["v"], r["e"], r["d"],
                                  r["gp"], r["gc"], r["pts"], fonte_rsssf(ano)])
        # artilheiros
        lista = artilheiros_rsssf.get(ano)
        if lista:
            for jog, clube_txt, n in lista:
                linhas_art.append([str(ano), jog, casar_clube_texto(clube_txt, ps, e["mapa"]), n, "RSSSF (rjtops.htm)"])
        elif ib["artilheiros"]:
            for jog, clube_txt, n in ib["artilheiros"]:
                linhas_art.append([str(ano), jog, casar_clube_texto(clube_txt, ps, e["mapa"]), n, "Wikipédia (infobox da edição)"])
        else:
            cont = Counter((g["jogador"], p.mandante if g["lado"] == "mandante" else p.visitante) for p in ps for g in p.gols if g["tipo"] != "contra")
            total = sum((p.gm or 0) + (p.gv or 0) for p in ps)
            if cont and sum(len(p.gols) for p in ps) >= 0.95 * total:
                topo = max(cont.values())
                for (jog, c), n in cont.items():
                    if n == topo:
                        linhas_art.append([str(ano), jog, nome(c), n, "contagem dos gols com autor"])
        # edição
        num_clubes = len({x for p in ps for x in (p.mandante, p.visitante)})
        vice = next((nome(f["clube"]) for f in final if f["pos"] == 2), "") if campeao else ""
        fontes = " + ".join(x for x, ok in (("RSSSF Brasil", bool(e["rs"])), ("ogol", bool(e["og"])),
                                               ("ESPN", any("espn:" in p.fonte_id for p in ps)), ("Wikipédia", bool(e["ajustes"]))) if ok)
        obs = []
        linhas_e.append([str(ano), int(str(ano)[:4]), int(str(ano)[:4]), NOME_OFICIAL.get(ano, NOME_PADRAO), num_clubes, pontos_vitoria(ano),
                         formato(desenho), nome(campeao) if campeao else "", vice, fontes, "; ".join(obs)])
        ng = sum((p.gm or 0) + (p.gv or 0) for p in ps)
        conf = e["conf"]
        linhas_conf.append([str(ano), len(ps), len(e["og"]) or "", conf["ok"], conf["dif"], ng, sum(len(p.gols) for p in ps),
                            obs_conferencia(ano, e, rs_c, wk_c)])
    # ------------------------------------------------------------------ clubes
    # uma linha por nome de exibição (o "Novorizontino" do banco junta dois códigos do ogol; veja docs/coleta/pedidos.md)
    por_nome: dict[str, list[str]] = defaultdict(list)
    for cid in usados:
        por_nome[nome(cid)].append(cid)
    linhas_c = []
    for n in sorted(por_nome):
        cids = sorted(por_nome[n], key=lambda c: min(a for anos in nomes_fonte[c].values() for a in anos))
        c = ex.get(cids[-1], {})
        juntos: dict[str, list[int]] = defaultdict(list)
        for cid in cids:
            for nf, anos in nomes_fonte[cid].items():
                juntos[nf] += anos
        partes = []
        for nf, anos in sorted(juntos.items()):
            a = sorted(set(anos))
            partes.append(f"{nf}:{a[0]}" + (f"-{a[-1]}" if a[-1] != a[0] else ""))
        linhas_c.append([n, c.get("uf"), c.get("cidade"), "BRA", "|".join(partes)])
    _csv("clubes.csv", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], linhas_c)
    _csv("edicoes.csv", ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "formato", "campeao", "vice",
                         "fontes", "observacao"], linhas_e)
    _csv("fases.csv", ["temporada", "ordem", "fase", "tipo", "num_grupos", "formato_serie", "criterio"], linhas_f)
    _csv("partidas.csv", ["id", "temporada", "fase", "grupo", "rodada", "data", "hora", "mandante", "visitante", "gols_mandante",
                          "gols_visitante", "penaltis_mandante", "penaltis_visitante", "resultado_especial", "estadio", "cidade", "publico",
                          "fonte", "fonte_id", "gols_texto", "observacao"], linhas_p)
    _csv("gols.csv", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "tipo", "fonte"], linhas_g)
    _csv("cartoes.csv", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "cor", "fonte"], [])
    _csv("classificacao_final.csv", ["temporada", "posicao", "clube", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra",
                                     "pontos", "ajuste_pontos", "situacao", "fonte", "observacao"], linhas_cf)
    _csv("tabelas_publicadas.csv", ["temporada", "fase", "grupo", "posicao", "nome_fonte", "clube", "jogos", "vitorias", "empates", "derrotas",
                                    "gols_pro", "gols_contra", "pontos", "fonte"], linhas_tp)
    _csv("artilheiros.csv", ["temporada", "jogador", "clube", "gols", "fonte"], linhas_art)
    _csv("classificacao_rodada.csv", ["temporada", "fase", "rodada", "clube", "posicao", "pontos", "jogos", "vitorias", "empates", "derrotas",
                                      "gols_pro", "gols_contra", "zona"], linhas_rod)
    _csv("conferencia.csv", ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols", "gols_com_autor",
                             "observacao"], linhas_conf)
    import registro   # cadastro comum de clubes (o mesmo nome em todos os pacotes)
    registro.acrescentar({cid: ex[cid] for cid in usados if cid in ex}, SLUG)
    relatorio(edicoes, log, rs_c, wk_c)


def classificacao_rodada(temporada: str, fase: str, ps: list, e: dict, ultima: bool, todos: set) -> list[list]:
    """Pontos corridos: a classificação de uma fase depois de cada rodada (pontos, vitórias, saldo, gols pró), com a fase
    numa coluna própria (pedido do agente 1: em 1979, 1996 e 1997 há mais de uma fase de pontos corridos). Só sai quando
    todos os jogos da fase têm a rodada e nenhum clube joga duas vezes na mesma rodada (rodada do ogol fora de ordem nos
    anos antigos). Zona: "titulo" para o 1º só na última fase; "rebaixamento" para as últimas posições, tantas quantos
    foram os rebaixados, só na fase que reúne todos os clubes da edição; "meio" para o resto."""
    if not ps or any(not p.rodada or p.gm is None for p in ps):
        return []
    por_rodada = Counter((p.rodada, x) for p in ps for x in (p.mandante, p.visitante))
    if any(n > 1 for n in por_rodada.values()):
        return []
    pv = pontos_vitoria(temporada)
    clubes = sorted({x for p in ps for x in (p.mandante, p.visitante)})
    caidos = len(rebaixados_rsssf(e) & set(clubes)) if set(clubes) >= todos else 0
    saida = []
    for r in range(1, max(p.rodada for p in ps) + 1):
        camp = {c: [0] * 6 for c in clubes}
        for p in ps:
            if p.rodada <= r:
                for eu, a, b in ((p.mandante, p.gm, p.gv), (p.visitante, p.gv, p.gm)):
                    x = camp[eu]
                    x[0] += 1; x[4] += a; x[5] += b
                    x[1 if a > b else 2 if a == b else 3] += 1
        pts = {c: pv * x[1] + x[2] for c, x in camp.items()}
        ordem = sorted(clubes, key=lambda c: (-pts[c], -camp[c][1], -(camp[c][4] - camp[c][5]), -camp[c][4], nome(c)))
        for pos, c in enumerate(ordem, 1):
            zona = "titulo" if pos == 1 and ultima else "rebaixamento" if caidos and pos > len(ordem) - caidos else "meio"
            saida.append([temporada, fase, r, nome(c), pos, pts[c], *camp[c], zona])
    return saida


def normalizar_especial(e: str) -> str:
    e = (e or "").lower()
    return "awd" if e in ("awd", "dns") or e.startswith("w") or "wo" in e else "n/p" if e in ("n/p", "canc") else "abd" if e == "abd" else ""


def fonte_curta(f: str) -> str:
    return "RSSSF Brasil" if "rsssf" in (f or "") else f


def formato(desenho: list[str]) -> str:
    saida = []
    for d in desenho:
        if not saida or saida[-1] != d:
            saida.append(d)
    if all(d == "mata-mata" for d in saida):
        return "mata-mata"
    return " + ".join(saida)


def rebaixados_rsssf(e: dict) -> set[str]:
    saida = set()
    for tb, linhas, nome_id in e["tabs"]:
        for r in tb.linhas:
            if re.search(r"relegat|rebaixad", r.get("obs", ""), re.I):
                if r["nome"] in nome_id:
                    saida.add(nome_id[r["nome"]])
    return saida


def artilheiros() -> dict[str, list[tuple[str, str, int]]]:
    """rjtops.htm: temporada -> [(jogador, clube como está na página, gols)]. Linhas "1912 - Harry Robinson (Paysandu)  26
    [LMSA]"; a outra liga do ano vem na linha de baixo, recuada ("       Mimi Sodré (Botafogo)  12  [AFRJ]"); empate na
    mesma linha ("Arlindo (Botafogo), Claudionor "Bolão" (Bangu)  18"); "1979 - Extra - Zico (Flamengo)  34" é o
    Campeonato Especial de 1979. A chave é a temporada do pacote ("1912 LMSA", "1979 Especial")."""
    from rsssf_rj1 import SIGLAS_LIGAS
    t = rsssf.texto(0, "rjtops.htm")
    saida: dict[str, list] = {}
    ano = None
    for l in t.splitlines():
        m = re.match(r"^(\d{4})\s*-\s*(.*)$", l)
        if m:
            ano, resto = m.group(1), m.group(2)
        elif ano and re.match(r"^\s{4,}\S", l):
            resto = l.strip()
        else:
            continue
        liga = re.search(rf"\[({SIGLAS_LIGAS})\]", resto)
        extra = re.match(r"(?i)extra\s*-\s*", resto)
        resto = re.sub(r"(?i)^extra\s*-\s*", "", resto)
        mg = re.search(r"\s(\d+)\s*(?:\[[^\]]*\])?\s*$", resto)
        if not mg:
            continue
        jogadores = re.findall(r"\s*([^,(]+?)\s*\(([^)]+)\)", resto[:mg.start()])
        if not jogadores:
            continue
        chave = f"{ano} {liga.group(1)}" if liga else f"{ano} Especial" if extra else ano
        saida.setdefault(chave, []).extend((j.strip(), c.strip(), int(mg.group(1))) for j, c in jogadores)
    return saida


def casar_clube_texto(txt: str, ps: list, mapa: dict | None = None) -> str:
    """Clube da edição escrito como a fonte escreve ("Santo Amaro/PE", "Etti Jundiaí/SP") -> nome de exibição.
    Compara com o nome de exibição, os nomes do ogol (calendário e ficha) e os nomes da RSSSF ligados ao clube."""
    from importar import _sim
    ids = {x for p in ps for x in (p.mandante, p.visitante)}
    fs = clubes_rj1.fichas()
    outros: dict[str, set] = {i: set() for i in ids}
    for n, i in (mapa or {}).items():
        if i in outros:
            outros[i].add(n[0] if isinstance(n, tuple) else n)
    base, uf = clubes_rj1.separar_uf(txt.replace("/", "-"))
    def nota(i):
        nomes = {nome(i), *fs.get(i, {}).get("nomes_ogol", []), fs.get(i, {}).get("nome_completo") or "", *outros[i]}
        s = max(_sim(base, x) for x in nomes if x)
        return s + (0.2 if uf and clubes_rj1.exibicao().get(i, {}).get("uf") == uf else 0)
    cands = sorted(((nota(i), i) for i in ids), reverse=True)
    return nome(cands[0][1]) if cands and cands[0][0] >= 0.8 else txt


def obs_conferencia(ano: int, e: dict, rs_c: dict, wk_c: dict) -> str:
    partes = []
    c = nome(e["campeao"]) if e["campeao"] else "?"
    partes.append(f"campeão {c} (RSSSF: {rs_c.get(ano, '-')}; Wikipédia: {wk_c.get(ano, '-')})")
    if e["conf"]["dif"]:
        partes.append("divergências explicadas no relatório")
    return "; ".join(partes)


def relatorio(edicoes: dict, log: list[str], rs_c: dict, wk_c: dict) -> None:
    from explicacoes import EXPLICACOES, FIM, INTRO
    linhas = ["# Campeonato Carioca (1ª divisão) — coleta de dados", "", *INTRO, "",
              "| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |",
              "|---|---|---|---|---|---|---|---|---|"]
    for ano, e in edicoes.items():
        ps = e["partidas"]
        ng = sum((p.gm or 0) + (p.gv or 0) for p in ps)
        f = e["final"]
        fontes = "RSSSF" if e["rs"] else ""
        fontes += (" + ogol" if e["og"] else "") + (" + ESPN" if any("espn:" in p.fonte_id for p in ps) else "")
        linhas.append(f"| {ano} | {fontes.strip(' +')} | {len(f)} | {len(ps)} ({len(e['og'])}) | {ng} | {sum(len(p.gols) for p in ps)} | "
                      f"{e['conf']['ok']} / {e['conf']['dif']} | {nome(e['campeao']) if e['campeao'] else '?'} | {f[0]['fonte'] if f else '-'} |")
    linhas += ["", "## Conferência e correções, ano a ano", ""]
    por_ano = defaultdict(list)
    for l in log:
        m = re.match(r"^(\d{4}(?: [A-Z]+)?): ", l)
        por_ano[m.group(1) if m else l[:4]].append(l[len(m.group(0)) if m else 6:])
    for ano, e in edicoes.items():
        linhas.append(f"### {ano}")
        linhas.append("")
        for x in EXPLICACOES.get(str(ano), []):
            linhas.append(f"- {x}")
        for l in e["conf"]["linhas"]:
            linhas.append(f"- tabela publicada x jogos — {l}")
        for l in por_ano.get(ano, []):
            linhas.append(f"- {l}")
        if not (EXPLICACOES.get(str(ano)) or e["conf"]["linhas"] or por_ano.get(ano)):
            linhas.append("- sem ocorrências")
        linhas.append("")
    linhas += FIM
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(linhas) + "\n", encoding="utf-8")
