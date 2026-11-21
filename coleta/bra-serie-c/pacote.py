"""Grava o pacote da Série C (data/coleta/bra-serie-c/pacote/) e o relatório (docs/coleta/bra-serie-c.md),
no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py.
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
from collections import Counter, defaultdict

from observacao import obs_pt
import clubes_c
from edicoes import NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RAIZ, RELATORIO, SLUG
from importar import FONTE_RSSSF, ORDEM, nome, pontos_vitoria
from rsssf_c import rsssf


def _csv(arquivo: str, cabecalho: list[str], linhas: list[list]) -> None:
    PACOTE.mkdir(parents=True, exist_ok=True)
    with open(PACOTE / arquivo, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        for l in linhas:
            w.writerow(["" if x is None else x for x in l])


def serie_b_por_ano(slug: str = "bra-serie-b") -> dict[int, set[str]]:
    """Clubes (nome de exibição do futebol.db) que jogaram a competição em cada ano: a Série B do ano seguinte marca o
    acesso da Série C; a Série D do ano seguinte, o rebaixamento."""
    con = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    saida: dict[int, set[str]] = defaultdict(set)
    for ano, n in con.execute("""SELECT e.ano_inicio, c.nome FROM classificacao_final f JOIN edicao e USING (edicao_id)
                                 JOIN competicao k USING (competicao_id) JOIN clube c USING (clube_id) WHERE k.slug = ?""", (slug,)):
        saida[int(ano)].add(n)
    con.close()
    return saida


# anos em que a Série B seguinte não foi por acesso (convite ou estaduais): só sobe quem está aqui (revisão SC-005)
ACESSO_SO_ESTES: dict[int, set[str]] = {1981: {"Olaria"}, 1988: set(), 1990: set(), 1992: set()}
# acesso que nem o infobox nem a Série B seguinte mostram (a Série B de 2000 foi o Módulo Amarelo da Copa João Havelange)
ACESSO_MANUAL: dict[int, set[str]] = {1999: {"Fluminense", "São Raimundo"}}
# rebaixados que não jogaram a Série D seguinte (licenciados ou desistentes), pela Wikipédia (revisão SC-004)
REBAIXADO_MANUAL: dict[int, set[str]] = {2016: {"Guaratinguetá"}, 2019: {"Luverdense"}}


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
    ex = clubes_c.exibicao()
    serie_b = serie_b_por_ano()
    serie_d = serie_b_por_ano("bra-serie-d")
    # ------------------------------------------------------------------ competicao.json
    PACOTE.mkdir(parents=True, exist_ok=True)
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": SLUG, "nome": "Campeonato Brasileiro Série C", "nome_curto": "Série C", "tipo": "liga", "nivel": 3, "pais": "BRA",
        "regiao": None, "confederacao": "CONMEBOL",
        "observacao": "Inclui a Taça de Bronze (1981). Não inclui 1987 (módulos Azul e Branco) nem 2000 (Módulo Verde e Branco "
                      "da Copa João Havelange), que RSSSF e Wikipédia não contam como Série C oficial.",
        "rotulo_painel": "Série C", "menu_painel": "Brasileirão Série C"}, ensure_ascii=False, indent=1), encoding="utf-8")
    # ------------------------------------------------------------------ partidas, gols, fases, edições
    linhas_p, linhas_g, linhas_f, linhas_e, linhas_cf, linhas_tp, linhas_conf, linhas_art = [], [], [], [], [], [], [], []
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    usados: set[str] = set()
    artilheiros_rsssf = artilheiros()
    for ano, e in edicoes.items():
        ps = e["partidas"]
        for n, cid in e["mapa"].items():
            nomes_fonte[cid][f"rsssf:{n[0] if isinstance(n, tuple) else n}"].append(ano)
        for o in e["og"]:
            for lado in ("mandante", "visitante"):
                # código trocado à mão (CORRIGE_OGOL): o nome do ogol é do outro clube e não entra (revisão CL-031)
                if o.get(f"{lado}_id") and not o.get(f"{lado}_corrigido"):
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
            desenho.append({"grupos": f"{ng} grupos", "liga": "pontos corridos", "mata_mata": "mata-mata"}[tipo])
        ordem_jogo = sorted(ps, key=lambda p: (fases.index(p.fase), p.grupo, p.data or "9999", p.hora or "", p.linha))
        for k, p in enumerate(ordem_jogo, 1):
            pid = f"{ano}-{k:04d}"
            usados |= {p.mandante, p.visitante}
            linhas_p.append([pid, str(ano), p.fase, p.grupo, p.rodada, p.data, p.hora, nome(p.mandante), nome(p.visitante), p.gm, p.gv,
                             p.pen_m, p.pen_v, normalizar_especial(p.especial), p.estadio, p.cidade, p.publico, fonte_curta(p.fonte),
                             p.fonte_id, p.gols_texto.strip() if p.gols_texto and not p.gols else "", obs_pt(p.obs)])
            for g in p.gols:
                linhas_g.append([pid, nome(p.mandante if g["lado"] == "mandante" else p.visitante), grafia(g["jogador"]), g["minuto"],
                                 g["acrescimo"], g["tipo"], g["fonte"]])
        # classificação final
        final = e["final"]
        campeao = e["campeao"]
        rebaixados = rebaixados_rsssf(e)
        ib = infobox(ano)
        subiram = {casar_clube_texto(x, ps, e["mapa"]) for x in ib["promovidos"]} | serie_b.get(ano + 1, set())
        if ano in ACESSO_SO_ESTES:
            subiram = ACESSO_SO_ESTES[ano]
        subiram |= ACESSO_MANUAL.get(ano, set())
        rebaixados |= {c for c in {x for p in ps for x in (p.mandante, p.visitante)}
                       if nome(c) in {casar_clube_texto(x, ps, e["mapa"]) for x in ib["rebaixados"]}}
        # quem jogou a Série D do ano seguinte caiu (revisão SC-004; a Série D existe desde 2009: em 2008 a Série C foi
        # reduzida a 20 clubes, e os outros foram para a nova Série D ou para os estaduais)
        if ano >= 2009:
            rebaixados |= {c for c in {x for p in ps for x in (p.mandante, p.visitante)} if nome(c) in serie_d.get(ano + 1, set())}
        rebaixados |= {c for c in {x for p in ps for x in (p.mandante, p.visitante)} if nome(c) in REBAIXADO_MANUAL.get(ano, set())}
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
                                  r["gp"], r["gc"], r["pts"], FONTE_RSSSF.format(ano=ano)])
        # artilheiros
        lista = artilheiros_rsssf.get(ano)
        if lista:
            for jog, clube_txt, n in lista:
                linhas_art.append([str(ano), grafia(jog), casar_clube_texto(clube_txt, ps, e["mapa"]), n, "RSSSF (br3tops.htm)"])
        elif ano in ARTILHEIRO_MANUAL:
            for jog, clube, n, fonte in ARTILHEIRO_MANUAL[ano]:
                linhas_art.append([str(ano), jog, clube, n, fonte])
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
        fontes = " + ".join(x for x, ok in (("RSSSF Brasil", bool(e["rs"]) and ano != 2019), ("ogol", bool(e["og"])),
                                               ("ESPN", any("espn:" in p.fonte_id for p in ps)), ("Wikipédia", bool(e["ajustes"]))) if ok)
        obs = []
        if ano == 2019:
            obs.append("jogos pelo ogol (a página da RSSSF parou na 1ª rodada)")
        linhas_e.append([str(ano), ano, ano if ano != 2020 else 2021, NOME_OFICIAL.get(ano, NOME_PADRAO), num_clubes, pontos_vitoria(ano),
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
    _csv("conferencia.csv", ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols", "gols_com_autor",
                             "observacao"], linhas_conf)
    import registro   # cadastro comum de clubes (o mesmo nome em todos os pacotes)
    registro.acrescentar({cid: ex[cid] for cid in usados if cid in ex}, SLUG)
    relatorio(edicoes, log, rs_c, wk_c)


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


# artilheiro que a RSSSF (br3tops.htm) e o infobox não trazem (revisão SC-022)
ARTILHEIRO_MANUAL: dict[int, list[tuple[str, str, int, str]]] = {
    1998: [("Kléber Pereira", "Moto Club", 25, "Wikipédia (artigo da edição)")]}
# grafia certa de nomes de jogador que a RSSSF escreve errado (revisão SC-023)
GRAFIA = {"Jonas Carioca": "Jones Carioca", "Assinzinho": "Assisinho", "Leandrao": "Leandrão", "Julio César": "Júlio César"}


def grafia(jogador: str) -> str:
    return GRAFIA.get(jogador, jogador)


def artilheiros() -> dict[int, list[tuple[str, str, int]]]:
    """br3tops.htm: ano -> [(jogador, clube como está na página, gols)]. Empate: nomes em linhas seguidas, gols na última."""
    t = rsssf.texto(0, "br3tops.htm")
    saida: dict[int, list] = {}
    ano, grupo = None, []
    for l in t.splitlines():
        m = re.match(r"^(\d{4})\s+(.*)$", l)
        if m:
            ano, grupo, resto = int(m.group(1)), [], m.group(2)
        elif ano and re.match(r"^\s{3,}\S", l):
            resto = l.strip()
        else:
            continue
        x = re.match(r"^(.+?)\s+\((.+?)\)\s*(\d+)?", resto.strip())
        if not x:
            continue
        grupo.append((x.group(1).strip(), x.group(2).strip()))
        if x.group(3):
            saida[ano] = [(j, c, int(x.group(3))) for j, c in grupo]
    return saida


def casar_clube_texto(txt: str, ps: list, mapa: dict | None = None) -> str:
    """Clube da edição escrito como a fonte escreve ("Santo Amaro/PE", "Etti Jundiaí/SP") -> nome de exibição.
    Compara com o nome de exibição, os nomes do ogol (calendário e ficha) e os nomes da RSSSF ligados ao clube."""
    from importar import _sim
    ids = {x for p in ps for x in (p.mandante, p.visitante)}
    fs = clubes_c.fichas()
    outros: dict[str, set] = {i: set() for i in ids}
    for n, i in (mapa or {}).items():
        if i in outros:
            outros[i].add(n[0] if isinstance(n, tuple) else n)
    base, uf = clubes_c.separar_uf(txt.replace("/", "-"))
    def nota(i):
        nomes = {nome(i), *fs.get(i, {}).get("nomes_ogol", []), fs.get(i, {}).get("nome_completo") or "", *outros[i]}
        s = max(_sim(base, x) for x in nomes if x)
        return s + (0.2 if uf and clubes_c.exibicao().get(i, {}).get("uf") == uf else 0)
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
    linhas = ["# Série C — coleta de dados", "", *INTRO, "",
              "| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |",
              "|---|---|---|---|---|---|---|---|---|"]
    for ano, e in edicoes.items():
        ps = e["partidas"]
        ng = sum((p.gm or 0) + (p.gv or 0) for p in ps)
        f = e["final"]
        fontes = "RSSSF" if e["rs"] and ano != 2019 else ""
        fontes += (" + ogol" if e["og"] else "") + (" + ESPN" if any("espn:" in p.fonte_id for p in ps) else "")
        linhas.append(f"| {ano} | {fontes.strip(' +')} | {len(f)} | {len(ps)} ({len(e['og'])}) | {ng} | {sum(len(p.gols) for p in ps)} | "
                      f"{e['conf']['ok']} / {e['conf']['dif']} | {nome(e['campeao']) if e['campeao'] else '?'} | {f[0]['fonte'] if f else '-'} |")
    linhas += ["", "## Conferência e correções, ano a ano", ""]
    por_ano = defaultdict(list)
    for l in log:
        por_ano[int(l[:4])].append(l[6:])
    for ano, e in edicoes.items():
        linhas.append(f"### {ano}")
        linhas.append("")
        for x in EXPLICACOES.get(ano, []):
            linhas.append(f"- {x}")
        for l in e["conf"]["linhas"]:
            linhas.append(f"- tabela publicada x jogos — {l}")
        for l in por_ano.get(ano, []):
            linhas.append(f"- {l}")
        if not (EXPLICACOES.get(ano) or e["conf"]["linhas"] or por_ano.get(ano)):
            linhas.append("- sem ocorrências")
        linhas.append("")
    linhas += FIM
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(linhas) + "\n", encoding="utf-8")
