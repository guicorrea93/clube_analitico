"""Grava o pacote do Campeonato Paulista (data/coleta/bra-sp-1/pacote/) e o relatório (docs/coleta/bra-sp-1.md),
no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py.
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
from collections import Counter, defaultdict

import clubes_sp1
import fpf_sp1
from edicoes import NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RAIZ, RELATORIO, SLUG
from importar import CAMPEOES_DIVIDIDOS, FONTE_RSSSF, OBS_EDICAO, ORDEM, nome, pontos_vitoria
from rsssf_sp1 import rsssf


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
    ex = clubes_sp1.exibicao()
    serie_b = serie_b_por_ano()
    # ------------------------------------------------------------------ competicao.json
    PACOTE.mkdir(parents=True, exist_ok=True)
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": SLUG, "nome": "Campeonato Paulista", "nome_curto": "Paulista", "tipo": "estadual", "nivel": 1, "pais": "BRA",
        "regiao": "SP", "confederacao": "CONMEBOL",
        "observacao": "1ª divisão paulista, de 1902 a 2026. Nos anos de ligas rivais (1913-1916, 1926-1929, 1935-1936) cada torneio "
                      "reconhecido pela federação é uma edição (\"1913 LPF\", \"1913 APEA\").",
        "rotulo_painel": "Paulista", "menu_painel": "Paulista", "do_painel": "do Paulistão", "o_painel": "o Paulistão"},
        ensure_ascii=False, indent=1), encoding="utf-8")
    # ------------------------------------------------------------------ partidas, gols, fases, edições
    linhas_p, linhas_g, linhas_f, linhas_e, linhas_cf, linhas_tp, linhas_conf, linhas_art = [], [], [], [], [], [], [], []
    linhas_rod: list[list] = []
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    usados: set[str] = set()
    artilheiros_rsssf = artilheiros()
    a2 = participantes_a2()
    a1: dict[int, set[str]] = defaultdict(set)
    for ano, e in edicoes.items():
        a1[int(str(ano)[:4])] |= {nome(x) for p in e["partidas"] for x in (p.mandante, p.visitante) if p.fase != "Repescagem"}
    for ano, e in edicoes.items():
        ps = e["partidas"]
        e["rebaixados"] = rebaixados(ano, e, a1, a2, log)
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
            obs = observacao(p, log)   # antes da linha: tira o público e o estádio da nota (2018)
            linhas_p.append([pid, str(ano), p.fase, p.grupo, p.rodada, p.data, p.hora, nome(p.mandante), nome(p.visitante), p.gm, p.gv,
                             p.pen_m, p.pen_v, normalizar_especial(p.especial), p.estadio, p.cidade, p.publico, fonte_curta(p.fonte),
                             p.fonte_id, p.gols_texto.strip() if p.gols_texto and not p.gols else "", obs])
            for g in p.gols:
                linhas_g.append([pid, nome(p.mandante if g["lado"] == "mandante" else p.visitante), g["jogador"], g["minuto"],
                                 g["acrescimo"], g["tipo"], g["fonte"]])
        # classificação final
        final = e["final"]
        campeao = e["campeao"]
        caidos = e["rebaixados"]
        ib = infobox(ano)
        subiram: set = set()   # 1ª divisão: acesso é de quem vem da A2 (fica para o pacote bra-sp-2)
        for f in final:
            c = f["clube"]
            sit = "campeao" if c == campeao else "acesso" if nome(c) in subiram else "rebaixado" if c in caidos else ""
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
        lista = artilheiros_rsssf.get(str(ano))
        if int(str(ano)[:4]) >= ARTILHARIA_FPF_DESDE and artilheiros_fpf(ano):
            for jog, clube_txt, n in artilheiros_fpf(ano):
                linhas_art.append([str(ano), NOME_ARTILHEIRO_FPF.get(jog, jog), clube_fpf(clube_txt, ps), n,
                                   "FPF (artilharia oficial)"])
        elif str(ano) in ARTILHEIRO_CORRIGIDO:
            lista, fonte = ARTILHEIRO_CORRIGIDO[str(ano)]
            for jog, clube_txt, n in lista:
                linhas_art.append([str(ano), jog, clube_txt, n, fonte])
        elif lista:
            for jog, clube_txt, n in lista:
                linhas_art.append([str(ano), jog, casar_clube_texto(clube_txt, ps, e["mapa"]), n, "RSSSF (sptops.htm)"])
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
        if str(ano) in CAMPEOES_DIVIDIDOS:   # título dividido: o vice é o da decisão D-07, não o outro campeão
            vice = CAMPEOES_DIVIDIDOS[str(ano)][1]
        fontes = " + ".join(x for x, ok in (("RSSSF Brasil", bool(e["rs"])), ("ogol", bool(e["og"])),
                                               ("ESPN", any("espn:" in p.fonte_id for p in ps)), ("Wikipédia", bool(e["ajustes"])),
                                               ("FPF", bool(fpf_sp1.jogos(ano)))) if ok)
        obs = list(OBS_EDICAO.get(str(ano), []))
        # título dividido (D-07): o outro campeão na coluna co_campeao (formato do agente 1, 23/11)
        co_campeao = " / ".join(n for n in CAMPEOES_DIVIDIDOS.get(str(ano), ([], ''))[0] if n != (nome(campeao) if campeao else ""))
        linhas_e.append([str(ano), int(str(ano)[:4]), int(str(ano)[:4]), NOME_OFICIAL.get(ano, NOME_PADRAO), num_clubes, pontos_vitoria(ano),
                         formato(desenho), nome(campeao) if campeao else "", vice, co_campeao, fontes, "; ".join(obs)])
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
                         "co_campeao", "fontes", "observacao"], linhas_e)
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
    caidos = len(e["rebaixados"] & set(clubes)) if set(clubes) >= todos else 0
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


MESES_EN = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
# notas da RSSSF em inglês -> português (achado SP-022); regex do pedaço inteiro, sem diferença de maiúsculas
TRADUCOES: list[tuple[str, object]] = [
    (r"awarded (\d+-\d+), or[i]?ginally (\d+-\d+), Port\..*used an ineligible player",
     r"resultado \1 dado no tribunal (o jogo terminou \2; a Portuguesa escalou jogador irregular)"),
    (r"awarded (\d+-\d+) to (.+)", r"resultado \1 dado ao \2"),
    (r"victory awarded to (.+)", r"vitória dada ao \1"),
    (r"points awarded to (.+?), or[i]?ginally (\d+-\d+)", r"pontos dados ao \1 (o jogo terminou \2)"),
    (r"Due to irregularities in the sale of entrance tickets, the team of AA Palmeiras was eliminated from the championship\.?",
     "a AA das Palmeiras foi eliminada do campeonato por irregularidades na venda de ingressos"),
    (r"After this match, Internacional were eliminated from the championship, due to aggressiveness of a part of its "
     r"players towards the referee\.?", "depois deste jogo o Internacional foi eliminado do campeonato pela agressão de "
                                         "jogadores ao árbitro"),
    (r"After this match, AA Palmeiras withdrew from the championship, due to disagreement with certain irregularities "
     r"during this match\.?", "depois deste jogo a AA das Palmeiras desistiu do campeonato, em desacordo com irregularidades "
                              "na partida"),
    (r"(.+?) used ineligible player (.+)", r"o \1 escalou jogador irregular (\2)"),
    (r"match suspended and awarded (\d+-\d+)", r"jogo suspenso; resultado \1 dado no tribunal"),
    (r"(\d+-\d+)\?", r"placar em dúvida na página (\1?)"),
    (r"(\d{1,2}/\w{3})\?", r"data em dúvida na página (\1?)"),
    (r"(?:match )?postponed from (\d)º Turno", r"jogo adiado do \1º turno"),
    (r"postponed to (\w{3}) (\d{1,2})", lambda m: f"adiado para {int(m[2]):02d}/{MESES_EN[m[1].lower()]:02d}"),
    (r"(?:extra-time:|aet) (\d+-\d+)", r"prorrogação \1"),
    (r"(?:abandoned|abd) at (\d+-\d+) in (\d+)'", r"abandonado aos \2 min com \1"),
    (r"result stands", "resultado mantido"),
    (r"abandoned at halftime due to heavy rain", "abandonado no intervalo por causa de chuva forte"),
    (r"replay", "jogo refeito"),
    (r"(.+?) qualified on better season record", r"\1 classificado pela melhor campanha"),
    (r"1st leg in (.+)", r"jogo de ida em \1"),
    (r"both legs in (.+)", r"os dois jogos em \1"),
    (r"played at Estadio (.+?), in (.+)", r"jogo no estádio \1, em \2"),
    (r"(?:match )?played in (.+)", r"jogo em \1"),
    (r"Concluded on (\w{3})\w* (\d{1,2}), (\d{4})", lambda m: f"concluído em {int(m[2]):02d}/{MESES_EN[m[1].lower()]:02d}/{m[3]}"),
]


def _pedacos(t: str) -> list[str]:
    """Separa a nota no ";" (e nos colchetes da RSSSF) só fora de parênteses."""
    t = re.sub(r"\]\s*\[|\]", ";", t)
    saida, nivel, atual = [], 0, ""
    for ch in t:
        nivel += (ch == "(") - (ch == ")")
        if ch == ";" and nivel <= 0:
            saida.append(atual); atual = ""
        else:
            atual += ch
    return [x.strip(" [") for x in saida + [atual]]


def observacao(p, log: list[str]) -> str:
    """Observação do jogo em português (achado SP-022). Antes: o público e o estádio que a página de 2018 escreve na nota
    ("Att.: 20,960] - Pacaembu, São Paulo") vão para os campos próprios; pênaltis saem (estão nos campos próprios)."""
    t = p.obs or ""
    m = re.search(r"Att\.:\s*([\d,.]+)\]?(?:\s*-\s*([^,;\]]+?),\s*([^;\]]+?))?\s*(?=;|$)", t)
    if m:
        if p.publico is None:
            p.publico = int(re.sub(r"\D", "", m[1]))
        if m[2] and not p.estadio:
            p.estadio, p.cidade = m[2].strip(), m[3].strip()
        t = t[:m.start()] + t[m.end():]
    nossa = "pontos dados ao" in t   # nota de PONTOS_FORA_DE_CAMPO (importar.py): a da RSSSF sobre os pontos sai
    partes = []
    for x in _pedacos(t):
        if x.startswith("(") and x.endswith(")") and x.count("(") == 1:
            x = x[1:-1].strip()
        if not x or x == "*" or re.fullmatch(r"\d+", x) or re.fullmatch(r"pen\w*\.?:?\s*\d+-\d+", x, re.I):
            continue
        if nossa and re.match(r"points awarded to", x, re.I):
            continue
        for padrao, troca in TRADUCOES:
            if re.fullmatch(padrao, x, re.I):
                x = re.sub(padrao, troca, x, flags=re.I)
                break
        if re.search(r"\b(the|was|were|after|match|awarded|played|postponed|due)\b", x, re.I):
            log.append(f"{p.ano}: observação ainda em inglês: {x}")
        if x not in partes:
            partes.append(x)
    return "; ".join(partes)


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


# rebaixados sem a A2 do ano seguinte para conferir: temporada -> (clubes, fonte)
REBAIXADOS_MANUAL: dict[str, tuple[list[str], str]] = {
    "2026": (["Ponte Preta", "Velo Clube"], "infobox da Wikipédia pt (data/coleta/bra-sp-1/wikipedia/pt_2026.txt); a A2 de 2027 "
                                            "ainda não existe"),
}
# clube que foi para a A2 no ano seguinte sem cair em campo: (temporada, clube) -> motivo
NAO_REBAIXADO: dict[tuple[str, str], str] = {
    ("2019", "Red Bull Bragantino II"): "o Red Bull Brasil cedeu a vaga na 1ª divisão ao Bragantino (fusão) e foi para a A2; "
                                        "os rebaixados de 2019 são São Bento e São Caetano (Wikipédia pt; SP-015)",
}


# rebaixado que não aparece na A2 do ano seguinte: (temporada, clube) -> fonte
REBAIXADO_EXTRA: dict[tuple[str, str], str] = {
    ("1959", "Comercial Paulistano"): "Wikipédia pt (infobox: XV de Jaú, Nacional e Comercial); não jogou a A2 de 1960",
}


def participantes_a2() -> dict[int, set[str]]:
    """Ano -> clubes (nome de exibição) da A2, pelo pacote bra-sp-2 (que usa o mesmo cadastro de nomes)."""
    saida: dict[int, set[str]] = defaultdict(set)
    f = RAIZ / "data" / "coleta" / "bra-sp-2" / "pacote" / "classificacao_final.csv"
    for r in csv.DictReader(open(f, encoding="utf-8")):
        saida[int(r["temporada"][:4])].add(r["clube"])
    return saida


def rebaixados(ano, e: dict, a1: dict[int, set[str]], a2: dict[int, set[str]], log: list[str]) -> set[str]:
    """Rebaixados da temporada (achado SP-015): as marcas "Relegated" das tabelas da RSSSF, menos quem jogou a 1ª divisão
    no ano seguinte (1994, 1998, 1999, 2002), mais quem jogou a A2 no ano seguinte e não a 1ª (2014-2025, anos antigos sem
    marca, 1995 XV de Piracicaba, 2006 Portuguesa Santista; conferido com a Wikipédia pt), menos NAO_REBAIXADO, mais
    REBAIXADO_EXTRA; REBAIXADOS_MANUAL quando não há A2 seguinte. Clube que só jogou a repescagem ou o torneio do
    rebaixamento contra a A2 é da A2 e não cai (1979 Santo André, 1980 Catanduvense, 2002 Francana)."""
    t, y = str(ano), int(str(ano)[:4])
    ids = {x for p in e["partidas"] for x in (p.mandante, p.visitante)}
    da_a2 = {c for c in ids if all(p.fase in ("Repescagem", "Torneio de rebaixamento")
                                   for p in e["partidas"] if c in (p.mandante, p.visitante))}
    if t in REBAIXADOS_MANUAL:
        nomes, fonte = REBAIXADOS_MANUAL[t]
        saida = {c for c in ids if nome(c) in nomes}
        if len(saida) != len(nomes):
            raise ValueError(f"{t}: rebaixado manual fora da edição: {nomes}")
        return saida
    seguinte = a1.get(y + 1, set())
    marcas = rebaixados_rsssf(e)
    for c in sorted(marcas, key=nome):
        if nome(c) in seguinte:
            log.append(f"{t}: {nome(c)} tem a marca de rebaixado na RSSSF, mas jogou a 1ª divisão em {y + 1}: não caiu (SP-015)")
    saida = {c for c in marcas if nome(c) not in seguinte}
    if y + 1 in a2:
        saida |= {c for c in ids if nome(c) in a2[y + 1] and nome(c) not in seguinte and (t, nome(c)) not in NAO_REBAIXADO}
    saida |= {c for c in ids if (t, nome(c)) in REBAIXADO_EXTRA}
    return saida - da_a2


def rebaixados_rsssf(e: dict) -> set[str]:
    saida = set()
    for tb, linhas, nome_id in e["tabs"]:
        for r in tb.linhas:
            if re.search(r"relegat|rebaixad", r.get("obs", ""), re.I):
                if r["nome"] in nome_id:
                    saida.add(nome_id[r["nome"]])
    return saida


# liga da coluna da sptops.htm -> liga da temporada nos anos de duas ligas
LIGA_SPTOPS = {"LPFB": "LPF", "APEA": "APEA", "LAFB": "LAF", "LFESP": "LPF", "FPF": ""}
# de 2022 em diante a lista é a da FPF (a sptops.htm parou em 2021; decisão D-17 a)
ARTILHARIA_FPF_DESDE = 2022


def artilheiros() -> dict[str, list[tuple[str, str, int]]]:
    """sptops.htm, em colunas ("1902    Charles Miller    São Paulo AC    10    LPFB"): temporada -> [(jogador, clube
    como está na página, gols)]. Empate: um nome por linha, e os gols (e às vezes a liga) só na última linha do grupo.
    A coluna da liga diz a temporada nos anos de duas ligas (achado QS-010)."""
    from edicoes import LIGAS
    t = rsssf.texto(0, "sptops.htm")
    saida: dict[str, list] = {}
    ano, pendentes = None, []
    for l in t.splitlines():
        m = re.match(r"^(?:(\d{4})|\s{4,})\s+(\S.*?)\s*$", l)
        if not m:
            continue
        if m.group(1):
            ano, pendentes = int(m.group(1)), []
        if ano is None:
            continue
        cols = re.split(r"\s{2,}", m.group(2))
        liga = cols.pop() if cols[-1] in LIGA_SPTOPS else None
        gols = int(cols.pop()) if cols[-1].isdigit() else None
        if len(cols) != 2:
            continue
        pendentes.append(tuple(cols))
        if gols is None:
            continue
        sigla = LIGA_SPTOPS[liga or "FPF"]
        temporada = f"{ano} {sigla}" if ano in LIGAS and sigla in LIGAS[ano] else str(ano)
        saida.setdefault(temporada, []).extend((j, c, gols) for j, c in pendentes)
        pendentes = []
    return saida


# apelido da FPF -> nome pelo qual o jogador é conhecido
NOME_ARTILHEIRO_FPF = {"Roger": "Róger Guedes", "Lopez": "Flaco López"}
# artilheiro em que a FPF e o Futebol Nacional batem entre si contra a sptops.htm: temporada -> (lista, fonte)
ARTILHEIRO_CORRIGIDO: dict[str, tuple[list[tuple[str, str, int]], str]] = {
    "2021": ([("Bruno Mezenga", "Ferroviária-SP", 9)], "FPF e Futebol Nacional: 9 gols (a sptops.htm dá 10; achado SP-024)"),
}


def clube_fpf(txt: str, ps: list) -> str:
    """Clube da edição com o nome popular de hoje da FPF ("Grêmio Novorizontino") -> nome de exibição."""
    for c in {x for p in ps for x in (p.mandante, p.visitante)}:
        if fpf_sp1.chave(nome(c)) == fpf_sp1.chave(txt):
            return nome(c)
    return casar_clube_texto(txt, ps)


def artilheiros_fpf(ano) -> list[tuple[str, str, int]]:
    """Artilharia oficial da FPF (data/coleta/bra-sp-1/fpf/artilharia_{ano}.json, de baixar_fpf.py): os de mais gols."""
    f = PASTA_DADOS / "fpf" / f"artilharia_{ano}.json"
    lista = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    if not lista:
        return []
    topo = max(x["Gols"] for x in lista)
    return [(x["AtletaApelido"].strip(), x["ClubeNomePopular"], x["Gols"]) for x in lista if x["Gols"] == topo]


def casar_clube_texto(txt: str, ps: list, mapa: dict | None = None) -> str:
    """Clube da edição escrito como a fonte escreve ("Santo Amaro/PE", "Etti Jundiaí/SP") -> nome de exibição.
    Compara com o nome de exibição, os nomes do ogol (calendário e ficha) e os nomes da RSSSF ligados ao clube."""
    from importar import _sim
    ids = {x for p in ps for x in (p.mandante, p.visitante)}
    fs = clubes_sp1.fichas()
    outros: dict[str, set] = {i: set() for i in ids}
    for n, i in (mapa or {}).items():
        if i in outros:
            outros[i].add(n[0] if isinstance(n, tuple) else n)
    base, uf = clubes_sp1.separar_uf(txt.replace("/", "-"))
    def nota(i):
        nomes = {nome(i), *fs.get(i, {}).get("nomes_ogol", []), fs.get(i, {}).get("nome_completo") or "", *outros[i]}
        s = max(_sim(base, x) for x in nomes if x)
        return s + (0.2 if uf and clubes_sp1.exibicao().get(i, {}).get("uf") == uf else 0)
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
    linhas = ["# Campeonato Paulista (1ª divisão) — coleta de dados", "", *INTRO, "",
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
