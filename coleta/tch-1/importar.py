"""Monta o pacote do campeonato da Tchecoslováquia (tch-1), 1925 a 1992/93, e o relatório docs/coleta/tch-1.md.

Base dos jogos: a matriz de resultados da Wikipédia (en) de cada temporada, sem data nem rodada (o ogol, a ESPN e o
football-data não têm esta liga). O clube sai do alvo do link da Wikipédia (clubes_tch.LINKS), que segue a linhagem
através das trocas de nome. 1945/46: dois grupos (A e B) e a final de ida e volta entre os primeiros (RSSSF).
Conferência: a tabela da Wikipédia (ordem oficial, punições) e a da RSSSF (tablest/tsjslhist.html), casada pela posição
com a da Wikipédia. Campeões: RSSSF (tsjslchamp.html).

Escopo (Guilherme, 25/11/2026): 1925 a 1992/93 com a liga do Protetorado (1938/39-1943/44); o outono de 1948 como edição
não oficial. Ver coleta/tch-1/edicoes.py.

Uso: python coleta/tch-1/importar.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
sys.path.append(str(AQUI.parent / "gre-1"))   # leitor da Wikipédia do grego, no fim da busca
sys.path.append(str(AQUI.parent / "cze-1"))   # texto da RSSSF do tcheco
import clubes_tch as clubes  # noqa: E402
import notas_wiki  # noqa: E402
import wiki_gre  # noqa: E402
from edicoes import (DADOS, NAO_OFICIAL, PROTETORADO, RAIZ, TEMPORADAS, nome_oficial, temporada,  # noqa: E402
                     wiki_titulo)
from pacote import gravar  # noqa: E402
from rsssf_cze import texto as texto_rsssf  # noqa: E402
from wiki_tabela import tabelas as wiki_tabelas  # noqa: E402

PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "tch-1.md"
URL_HIST = "https://www.rsssf.org/tablest/tsjslhist.html"

# jogos que a matriz da Wikipédia não tem: ano -> [(fase, mandante, visitante, gols, gols, observação)]
EXTRAS = {1945: [("Final", "Sparta Praga", "Slavia Praga", 4, 2, "final entre os primeiros dos grupos, 1º jogo (RSSSF)"),
                 ("Final", "Slavia Praga", "Sparta Praga", 0, 5, "final entre os primeiros dos grupos, 2º jogo (RSSSF)")]}
# campeões da RSSSF (tsjslchamp.html e, no Protetorado, tsjechamp.html), pelo nome da lista -> chave
CAMPEOES_RSSSF = {
    "SK Slavia Praha": "Slavia Praga", "AC Sparta Praha": "Sparta Praga", "SK Viktoria Žižkov": "Viktoria Žižkov",
    "NV Bratislava": "Slovan Bratislava", "ČKD Sokolovo Praha": "Sparta Praga", "ÚDA Praha": "Dukla Praga",
    "Spartak Praha Sokolovo": "Sparta Praga", "Slovan Bratislava": "Slovan Bratislava", "Dukla Praha": "Dukla Praga",
    "Červená hviezda Bratislava": "Inter Bratislava", "Spartak Hradec Králové": "Hradec Králové",
    "Sparta ČKD Praha": "Sparta Praga", "Sparta Praha": "Sparta Praga", "Spartak Trnava": "Spartak Trnava",
    "Baník Ostrava": "Baník Ostrava", "Zbrojovka Brno": "Zbrojovka Brno", "Bohemians Praha": "Bohemians 1905",
    "TJ Vítkovice": "Vítkovice",
}
EXPLICACOES: dict[int, list[str]] = {}

COMPETICAO = {
    "slug": "tch-1", "nome": "Campeonato Tchecoslovaco", "nome_curto": "Tchecoslovaco", "tipo": "liga", "nivel": 1,
    "pais": "TCH", "pais_nome": "Tchecoslováquia", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Tchecoslovaco", "menu_painel": "Tchecoslováquia · 1ª divisão",
    "do_painel": "do Campeonato Tchecoslovaco", "o_painel": "o Campeonato Tchecoslovaco",
    "observacao": "Campeonato da Tchecoslováquia, de 1925 (primeiro título oficial) a 1992/93, com a liga do Protetorado da "
                  "Boêmia e Morávia (Národní liga, 1938/39-1943/44). O outono de 1948 é edição não oficial. Não inclui o "
                  "campeonato da Boêmia Central antes de 1925, o campeonato amador, 1944/45 (abandonado) nem a liga "
                  "eslovaca da guerra. Depois de 1993: Campeonato Tcheco e Campeonato Eslovaco.",
}


def faixa(anos) -> str:
    a = sorted(anos)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else f"{a[0]}"


def texto_wiki(a: int) -> str:
    return "\n".join(x.read_text(encoding="utf-8") for x in sorted((DADOS / "wikipedia").glob(f"{wiki_titulo(a)}*.wiki")))


def links_do_texto(t: str) -> tuple[dict, dict]:
    """código -> alvo e nome visível -> alvo, pelos name_XXX = [[alvo|visível]] do artigo."""
    cod, vis = {}, {}
    for c, alvo, nome in re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", t):
        cod.setdefault(c, alvo.strip())
        vis.setdefault((nome or alvo).strip(), alvo.strip())
    return cod, vis


def tabelas_rsssf() -> dict[str, list[dict]]:
    """tsjslhist.html: um bloco por temporada ("1925 (spring) (Asociacni Liga)", "1938/39 BOHEMIA", "1948 - fall", "1945/46
    ... Group A") com linhas "pos. nome J V E D GP-GC Pts". Rótulo -> [tabelas]."""
    res = defaultdict(list)
    rotulo, atual = None, None
    for l in texto_rsssf(DADOS / "rsssf" / "tsjslhist.html").split("\n"):
        m = re.match(r"^(\d{4}(?:/\d{2})?)\b", l)
        if m:
            rotulo, atual = m.group(1), None
            continue
        if re.match(r"(?i)^\s*group\s+[ab]\s*$", l):
            atual = None
            continue
        mm = re.match(r"^\s*(\d+)\.\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(-?\d+)\s*(.*)$", l)
        if mm and rotulo:
            if atual is None:
                atual = []
                res[rotulo].append(atual)
            pos, nome, j, v, e, d, gp, gc, p, resto = mm.groups()
            atual.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                          "derrotas": int(d), "gols_pro": int(gp), "gols_contra": int(gc), "pontos": int(p)})
        elif atual is not None and l.strip() and not l.startswith(" "):
            atual = None
    return res


def campeoes_rsssf() -> dict[str, str]:
    res = {}
    for arq in ("tsjslchamp.html",):
        for m in re.finditer(r"^(\d{4}(?:/\d{2})?)\s+(\S.*?)\s*(?:\[.*)?$", texto_rsssf(DADOS / "rsssf" / arq), re.M):
            res.setdefault(m.group(1), m.group(2).strip())
    return res


def calcular(jogos: list[dict], pts) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0] * 7)
    for j in jogos:
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            k = 1 if gp > gc else 2 if gp == gc else 3
            x[k] += 1
            x[6] += pts[k - 1]
    return t


def ordenar(t, ajuste, criterio, jogos, pts) -> list[str]:
    def p(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, _ = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        return (-(gp - gc), -gp)
    if criterio != "confronto":
        return sorted(sorted(t), key=lambda c: (-p(c), *geral(c)))
    grupos = defaultdict(list)
    for c in sorted(t):
        grupos[p(c)].append(c)
    res = []
    for pt in sorted(grupos, reverse=True):
        g = grupos[pt]
        if len(g) > 1:
            mini = calcular([j for j in jogos if j["m"] in g and j["v"] in g], pts)
            g.sort(key=lambda c: (-mini[c][6], -(mini[c][4] - mini[c][5]), *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def pontos(tb_rs: list[dict] | None) -> tuple[int, int, int]:
    if not tb_rs:
        return (2, 1, 0)
    return max([(2, 1, 0), (3, 1, 0)], key=lambda q: sum(x["pontos"] == q[0] * x["vitorias"] + q[1] * x["empates"] for x in tb_rs))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rs_tabs = tabelas_rsssf()
    camp_rs = campeoes_rsssf()
    nomes = defaultdict(lambda: defaultdict(set))
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel, criterios = [], {}
    clubes_de: dict[int, set] = {}
    dados_ano = {}

    for a in TEMPORADAS:   # 1º passo: jogos e clubes de cada temporada (a seguinte diz quem caiu)
        T = temporada(a)
        txt = texto_wiki(a)
        cod_link, vis_link = links_do_texto(txt)
        wk = wiki_gre.ler(txt)
        jogos = []
        for w in wk["jogos"]:
            if w["fonte"] != "matriz":
                continue
            m = clubes.link(w["tm"] or vis_link.get(w["nm"]))
            v = clubes.link(w["tv"] or vis_link.get(w["nv"]))
            if m is None or v is None:
                raise SystemExit(f"{T}: clube da matriz da Wikipédia sem cadastro: {w['tm'] or w['nm']} x {w['tv'] or w['nv']}")
            secao = " ".join(w["secao"])
            grupo = re.search(r"Group ([AB])", secao)
            jogos.append({"m": m, "v": v, "nm": w["nm"], "nv": w["nv"], "gm": w["gm"], "gv": w["gv"],
                          "fase": "Grupos" if grupo else "Liga", "grupo": f"Grupo {grupo.group(1)}" if grupo else None,
                          "fonte": "Wikipédia (matriz)"})
        tbs = []
        for tb in wiki_tabelas(txt):
            for x in tb["times"]:
                x["clube"] = clubes.link(cod_link.get(x.get("codigo")) or vis_link.get(x["nome"]))
                if x["clube"] is None:
                    raise SystemExit(f"{T}: clube da tabela da Wikipédia sem cadastro: {x['nome']} ({cod_link.get(x.get('codigo'))})")
            tbs.append(tb)
        dados_ano[a] = (jogos, tbs)
        clubes_de[a] = {c for j in jogos for c in (j["m"], j["v"])}

    for a in TEMPORADAS:
        ocorr[a].extend(EXPLICACOES.get(a, []))
        T = temporada(a)
        jogos, tbs = dados_ano[a]
        for j in jogos:
            for lado in ("m", "v"):
                nomes[j[lado]][f"wikipedia:{j['n' + lado]}"].add(a)
        clubes_ano = sorted(clubes_de[a])
        n = len(clubes_ano)
        grupos = a == 1945
        rs_lista = rs_tabs.get(T, [])
        pts = pontos(rs_lista[0] if rs_lista else None)
        extras = [{"m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "fase": f, "grupo": None, "fonte": "RSSSF", "obs": o}
                  for f, m, v, gm, gv, o in EXTRAS.get(a, [])]

        # ---- tabelas: as da Wikipédia (uma por grupo em 1945/46) e as da RSSSF, casadas pela posição
        conferidas = divergentes = 0
        ajuste: dict[str, int] = {}
        conjuntos = [(tb, [j for j in jogos if {j["m"], j["v"]} <= {x["clube"] for x in tb["times"]}]) for tb in tbs
                     if len(tb["times"]) >= 3]
        if not grupos:   # a maior tabela é a da liga (1938/39 traz também a eslovaca)
            conjuntos = [max(conjuntos, key=lambda c: len(c[0]["times"]))]
        ordem_geral = []
        for k, (tb, js) in enumerate(conjuntos):
            calc = calcular(js, pts)
            fase = "Grupos" if grupos else "Liga"
            grupo = f"Grupo {'AB'[k]}" if grupos else None
            for x in tb["times"]:
                nomes[x["clube"]][f"wikipedia:{x['nome']}"].add(a)
                if x["ajuste"]:
                    ajuste[x["clube"]] = x["ajuste"]
            rs = rs_lista[k] if k < len(rs_lista) else None
            if rs and len(rs) == len(tb["times"]):
                for x, y in zip(rs, tb["times"]):   # o mesmo clube na mesma posição
                    x["clube"] = y["clube"]
                    nomes[y["clube"]][f"rsssf:{x['nome']}"].add(a)
            elif rs_lista:
                ocorr[a].append(f"tabela da RSSSF com {len(rs) if rs else 0} clubes e a da Wikipédia com {len(tb['times'])}: "
                                f"sem conferência pela RSSSF")
                rs = None
            pub_w = [dict(x, jogos=sum(x[c] or 0 for c in ("vitorias", "empates", "derrotas")),
                          pontos=pts[0] * (x["vitorias"] or 0) + pts[1] * (x["empates"] or 0) + (x["ajuste"] or 0))
                     for x in tb["times"]]
            # placar escrito ao contrário na matriz: inverte só quando, com isso, os dois clubes fecham exatamente com as
            # tabelas publicadas (a da Wikipédia e a da RSSSF); não há outra fonte jogo a jogo
            pubs = [{x["clube"]: [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]]
                     for x in linhas_} for linhas_ in (pub_w, rs or []) if linhas_]

            def distancia(cs_):
                t_ = calcular(js, pts)
                return sum(abs(t_[c][q] - p_[c][q]) for p_ in pubs for c in cs_ if c in p_ for q in range(6))
            for j in js:
                if j["gm"] == j["gv"]:
                    continue
                antes = distancia((j["m"], j["v"]))
                if not antes:
                    continue
                j["gm"], j["gv"] = j["gv"], j["gm"]
                if distancia((j["m"], j["v"])) == 0:   # só quando os dois clubes passam a fechar com as tabelas
                    j["obs"] = (f"placar invertido: a matriz da Wikipédia dá {j['gv']}-{j['gm']}, que não fecha com as "
                                f"tabelas da Wikipédia e da RSSSF")
                    ocorr[a].append(f"{j['m']} x {j['v']}: fica {j['gm']}-{j['gv']}; a matriz da Wikipédia dá {j['gv']}-{j['gm']} "
                                    f"(invertido), que não fecha com as tabelas")
                else:
                    j["gm"], j["gv"] = j["gv"], j["gm"]
            calc = calcular(js, pts)
            erros = {}
            for fonte, url, linhas in (("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}", pub_w),
                                       ("RSSSF", URL_HIST, rs or [])):
                if not linhas:
                    continue
                erro = []
                for x in linhas:
                    c = calc.get(x["clube"])
                    pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                    meu = (c[:6] + [c[6] + ajuste.get(x["clube"], 0)]) if c else None
                    if pub != meu:
                        erro.append((x["clube"], pub, meu))
                    tab["tabelas_publicadas"].append({
                        "temporada": T, "fase": fase, "grupo": grupo, "posicao": x["posicao"], "nome_fonte": x["nome"],
                        "clube": clubes.exibicao(x["clube"]), "jogos": pub[0], "vitorias": pub[1], "empates": pub[2],
                        "derrotas": pub[3], "gols_pro": pub[4], "gols_contra": pub[5], "pontos": pub[6], "fonte": url})
                erros[fonte] = erro
                if erro:
                    divergentes += 1
                else:
                    conferidas += 1
            for fonte, erro in erros.items():
                outra = [f_ for f_ in erros if f_ != fonte]
                for c, pub, meu in erro[:8]:
                    fecha = outra and c not in {e[0] for e in erros[outra[0]]}
                    ocorr[a].append(f"tabela {('do ' + grupo + ' ') if grupo else ''}da {fonte} x jogos — {c} tabela {pub} jogos "
                                    f"{meu}" + (f" (a tabela da {outra[0]} fecha com os jogos)" if fecha else ""))
            ordem = [x["clube"] for x in tb["times"]]
            tent = {cr: ordenar(calc, ajuste, cr, js, pts) for cr in ("confronto", "saldo", "media")}
            ok = [cr for cr, o in tent.items() if o == ordem]
            cr = ok[0] if ok else min(tent, key=lambda q: sum(x != y for x, y in zip(tent[q], ordem)))
            if not ok:
                d_ = [c for c, d in zip(ordem, tent[cr]) if c != d]
                ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial{(' do ' + grupo) if grupo else ''}; o mais "
                                f"próximo ({cr}) difere em {len(d_)} posições (ex.: {d_[:2]})")
            criterios[(a, k)] = (cr, bool(ok))
            # números publicados em que as duas tabelas concordam e os jogos da matriz não fecham: vão para a classificação
            publicados = {}
            for x in pub_w:
                y = next((y for y in rs or [] if y["clube"] == x["clube"]), None)
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]]
                if (y is None or [y["jogos"], y["vitorias"], y["empates"], y["derrotas"], y["gols_pro"], y["gols_contra"]] == pub)                         and pub != calc[x["clube"]][:6]:
                    publicados[x["clube"]] = pub
            ordem_geral.append((ordem, calc, grupo, publicados))
            if publicados and not grupos:
                ocorr[a].append(f"a matriz da Wikipédia (a única fonte jogo a jogo) não fecha com as tabelas da RSSSF e da "
                                f"Wikipédia, que concordam entre si, em {len(publicados)} clubes: a classificação final fica com "
                                f"os números publicados (observação na linha); limite de fonte")
            if len(js) != len(tb["times"]) * (len(tb["times"]) - 1) and a not in (1924, 1926, 1948, 1953, 1957):
                ocorr[a].append(f"{len(js)} jogos na matriz{(' do ' + grupo) if grupo else ''} para {len(tb['times'])} clubes")

        # ---- classificação final
        if grupos:   # os finalistas, depois os outros pela posição no grupo (A antes de B)
            final = [x["m"] for x in extras] + [x["v"] for x in extras]
            tot = calcular([j for j in extras], pts)
            vencedor = max(set(final), key=lambda c: (tot[c][4] - tot[c][5]))
            ordem_final = [vencedor, next(c for c in set(final) if c != vencedor)]
            for i in range(10):
                for ordem, *_ in ordem_geral:
                    if i < len(ordem) and ordem[i] not in ordem_final:
                        ordem_final.append(ordem[i])
            numeros = calcular(jogos, pts)
            fonte_cl = "RSSSF (final entre os primeiros dos grupos; depois a posição no grupo)"
        else:
            ordem_final, numeros, _, publicados = ordem_geral[0]
            fonte_cl = "Wikipédia (ordem oficial)"
        prox = next((b for b in TEMPORADAS if b > a), None)
        rebaixados = set() if prox is None else {c for c in clubes_ano if c not in clubes_de[prox]}
        campeao = ordem_final[0]
        nome_rs = camp_rs.get(T)
        if a in PROTETORADO:
            pass   # a lista tchecoslovaca da RSSSF manda o Protetorado para a lista tcheca
        elif nome_rs and CAMPEOES_RSSSF.get(nome_rs) != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {nome_rs} (classificação: {campeao})")
        for pos, c in enumerate(ordem_final, 1):
            j_, v_, e_, d_, gp, gc, p = numeros[c]
            obs_num = None
            if not grupos and c in publicados:   # a matriz não fecha com as tabelas: ficam os números publicados
                obs_num = (f"números das tabelas publicadas (Wikipédia e RSSSF, iguais); os jogos da matriz somam {j_} jogos, "
                           f"{v_}-{e_}-{d_} e {gp}-{gc} gols")
                j_, v_, e_, d_, gp, gc = publicados[c]
                p = pts[0] * v_ + pts[1] * e_
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + ajuste.get(c, 0), "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None, "fonte": fonte_cl,
                "observacao": "; ".join(x for x in (obs_num, next((notas_wiki.traduzir(x["nota"] or x["hth"]) for tb in tbs
                                                                   for x in tb["times"] if x["clube"] == c and
                                                                   (x["nota"] or x["hth"])), None)) if x) or None})

        # ---- partidas
        todos = sorted(jogos, key=lambda j: (j["grupo"] or "", j["m"], j["v"])) + extras
        for i, j in enumerate(todos, 1):
            tab["partidas"].append({
                "id": f"{a}-{i:04d}", "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": None, "data": None,
                "hora": None, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": None, "estadio": None, "cidade": None, "publico": None, "fonte": j["fonte"],
                "fonte_id": None, "gols_texto": None, "observacao": j.get("obs"), "arbitro": None})
        gols_ano = sum(j["gm"] + j["gv"] for j in todos)

        # ---- edição, fases, conferência
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        turnos = {1924: "turno único", 1926: "turno único", 1948: "turno único", 1953: "turno único",
                  1957: "três turnos"}.get(a, "turno e returno")
        formato = ("dois grupos de 10 (turno e returno) e final de ida e volta entre os primeiros" if grupos
                   else f"pontos corridos ({turnos}); sem datas (só a matriz de resultados)")
        tab["edicoes"].append({
            "temporada": T, "ano_inicio": a if T[:4] == str(a) else a + 1, "ano_fim": (a + 1) if "/" in T else int(T[:4]),
            "nome_oficial": nome_oficial(a), "num_clubes": n, "pontos_vitoria": pts[0], "formato": formato,
            "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(ordem_final[1]),
            "fontes": "Wikipédia" + (" + RSSSF" if rs_lista else ""),
            "observacao": "; ".join(x for x in (NAO_OFICIAL.get(a, ""),
                                                "liga do Protetorado da Boêmia e Morávia (Národní liga), durante a ocupação"
                                                if a in PROTETORADO else "",
                                                "temporada interrompida em 1938/39 e continuada como liga do Protetorado"
                                                if a == 1938 else "",
                                                f"punições: {pun}" if pun else "",
                                                "última temporada antes da separação: sem rebaixados (1993/94: Campeonato "
                                                "Tcheco e Campeonato Eslovaco)" if prox is None else "") if x) or None,
            "oficial": "não" if a in NAO_OFICIAL else None})
        cr, _ = criterios[(a, 0)]
        crit_txt = {"saldo": "pontos, saldo de gols", "confronto": "pontos, confronto direto, saldo de gols",
                    "media": "pontos, média de gols (goal average)"}[cr]
        if grupos:
            tab["fases"] += [{"temporada": T, "ordem": 1, "fase": "Grupos", "tipo": "grupos", "num_grupos": 2,
                              "formato_serie": "pontos_corridos", "criterio": crit_txt},
                             {"temporada": T, "ordem": 2, "fase": "Final", "tipo": "mata_mata", "num_grupos": None,
                              "formato_serie": "ida_volta", "criterio": "soma dos placares"}]
        else:
            tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Liga", "tipo": "liga", "num_grupos": None,
                                 "formato_serie": "pontos_corridos", "criterio": crit_txt})
        tab["conferencia"].append({"temporada": T, "jogos": len(todos), "jogos_esperados": None, "tabelas_conferidas": conferidas,
                                   "tabelas_divergentes": divergentes, "gols": gols_ano, "gols_com_autor": 0,
                                   "observacao": f"campeão {clubes.exibicao(campeao)}; lista da RSSSF: {nome_rs or '—'}"})
        linhas_rel.append((T, n, len(todos), gols_ano, conferidas, divergentes, clubes.exibicao(campeao), pun))
        print(f"{T}: {len(todos)} jogos, {n} clubes, tabelas {conferidas} ok / {divergentes} div, campeão {clubes.exibicao(campeao)}",
              flush=True)

    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c in nomes:
            tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais,
                                  "nomes_fonte": "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))})
    tab["paises"] = [{"codigo": "TCH", "nome": "Tchecoslováquia", "confederacao": "UEFA"},
                     {"codigo": "CZE", "nome": "Tchéquia", "confederacao": "UEFA"},
                     {"codigo": "SVK", "nome": "Eslováquia", "confederacao": "UEFA"},
                     {"codigo": "UKR", "nome": "Ucrânia", "confederacao": "UEFA"}]
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, criterios)


def relatorio(linhas, ocorr, tab, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Tchecoslovaco (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/tch-1/importar.py`. Pacote em `data/coleta/tch-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1925 a 1992/93, com a liga do Protetorado (1938/39-1943/44). O outono de 1948 é "
        "edição não oficial.", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['clubes'])} clubes. Sem datas, rodadas, autores dos gols e cartões "
        "(só a matriz de resultados).", "",
        "**Fontes:**",
        "- Wikipédia (en): matriz de resultados de cada temporada (base dos jogos), tabela final (ordem oficial, punições);",
        "- RSSSF: tabelas finais (tsjslhist.html, casadas pela posição com as da Wikipédia), lista de campeões, final de "
        "1945/46.", "",
        f"**Desempate:** o critério calculado que reproduz a ordem oficial (confronto direto em {cr['confronto']}, saldo em "
        f"{cr['saldo']}, média de gols em {cr['media']}).", "",
        "| Temporada | Clubes | Jogos | Gols | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|",
    ]
    for T, n, j, g, ok, dv, camp, pun in linhas:
        out.append(f"| {T} | {n} | {j} | {g} | {ok} / {dv} | {camp} | {pun or '—'} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for T, *_ in linhas:
        a = next(b for b in TEMPORADAS if temporada(b) == T)
        out += [f"### {T}", ""] + [f"- {o}" for o in ocorr.get(a, []) or ["sem ocorrências"]] + [""]
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_tch.py`, pelo alvo do link da Wikipédia (a linhagem através das trocas de "
        "nome da era comunista). Os clubes que também jogaram a liga tcheca têm a mesma chave do `cze-1`; os eslovacos têm o "
        "país de hoje (SVK).",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Datas, rodadas, autores dos gols, cartões, público:** a matriz da Wikipédia não traz; o ogol, a ESPN e o "
        "football-data não têm esta liga.",
        "- **Campeonato da Boêmia Central antes de 1925, campeonato amador, 1944/45 e liga eslovaca da guerra:** fora do "
        "escopo.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
