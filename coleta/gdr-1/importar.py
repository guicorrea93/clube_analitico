"""Monta o pacote do campeonato da Alemanha Oriental (gdr-1), 1948 a 1990/91, e o relatório docs/coleta/gdr-1.md.

Decisão do Guilherme (D-05b, 22/11/2026): competição à parte (a federação alemã não conta esses títulos como alemães).

Base dos jogos:
  1948 e 1949        campeonato da zona soviética (Ostzonenmeisterschaft), mata-mata entre os campeões estaduais: as
                     fichas de jogo da Wikipédia (en), com data, local e público;
  1949/50-1990/91    DDR-Oberliga (a última como NOFV-Oberliga): a página da RSSSF de cada temporada (rodada, data e
                     placar de cada jogo; jogo dado fora de campo com "X:0", vitória para o lado do X e gols 0:0).
Conferência: tabela final da RSSSF e tabela e matriz de resultados da Wikipédia. Campeões e artilheiros: RSSSF
(ddrchamp.html, ddrtops.html). 2 pontos por vitória em todas as temporadas.

Uso: python coleta/gdr-1/importar.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_gdr as clubes  # noqa: E402
from edicoes import ANO_CIVIL, DADOS, RAIZ, TEMPORADAS, rsssf_pagina, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from rsssf_gdr import ler as ler_rsssf, texto as texto_rsssf  # noqa: E402
from wiki_tabela import _fecha, _partes, limpar, resultados as wiki_resultados, tabelas as wiki_tabelas  # noqa: E402

PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "gdr-1.md"
URL_RSSSF = "https://www.rsssf.org/tablesd/"
MATA_MATA = {1947, 1948}
SEM_TITULO = {1955: "rodada de transição (Übergangsrunde) no segundo semestre de 1955, para passar ao ano civil; o "
                    "primeiro colocado (Wismut Karl-Marx-Stadt) não é contado como campeão"}
MESES = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september",
                                     "october", "november", "december"], 1)}
MESES.update({m[:3]: i for m, i in list(MESES.items())})   # "Jun", "Sept"
MESES["sept"] = 9
FASES_EN = [(r"(?i)qualif", "Eliminatória"), (r"(?i)quarter", "Quartas de final"), (r"(?i)semi", "Semifinal"),
            (r"(?i)^final", "Final")]
# explicação das divergências que sobram (vai para o relatório)
EXPLICACOES: dict[int, list[str]] = {
    1951: ["a tabela final da RSSSF de 1951/52 não traz o 3º, o 4º e o 5º colocados: a ordem e a conferência ficam com a "
           "tabela da Wikipédia"],
}

COMPETICAO = {
    "slug": "gdr-1", "nome": "Campeonato da Alemanha Oriental", "nome_curto": "Alemanha Oriental", "tipo": "liga",
    "nivel": 1, "pais": "GDR", "pais_nome": "Alemanha Oriental", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Alemanha Oriental", "menu_painel": "Alemanha Oriental · DDR-Oberliga",
    "do_painel": "do Campeonato da Alemanha Oriental", "o_painel": "o Campeonato da Alemanha Oriental",
    "observacao": "Campeonato da zona soviética (1948 e 1949, mata-mata) e DDR-Oberliga (1949/50 a 1990/91; a última "
                  "temporada, já depois da reunificação, como NOFV-Oberliga). Ano civil de 1956 a 1960, depois da rodada de "
                  "transição de 1955. A federação alemã (DFB) não conta esses títulos como alemães: competição à parte.",
}


def chave(nome: str, a: int, fonte: str) -> str:
    c = clubes.esd(nome, a)
    if c is None:
        raise SystemExit(f"{temporada(a)}: nome da {fonte} sem cadastro: {nome}")
    return c


def faixa(anos) -> str:
    a = sorted(anos)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else f"{a[0]}"


def calcular(jogos: list[dict]) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0] * 7)
    for j in jogos:
        if j.get("vencedor"):   # dado fora de campo: vitória e 2 pontos para um lado, gols 0:0
            ganha, perde = (j["m"], j["v"]) if j["vencedor"] == "m" else (j["v"], j["m"])
            for c in (ganha, perde):
                t[c][0] += 1
            t[ganha][1] += 1; t[ganha][6] += 2
            t[perde][3] += 1
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            if gp > gc:
                x[1] += 1; x[6] += 2
            elif gp == gc:
                x[2] += 1; x[6] += 1
            else:
                x[3] += 1
    return t


def ordenar(t, criterio: str, jogos=None) -> list[str]:
    def geral(c):
        j, v, e, d, gp, gc, p = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        return (-(gp - gc), -gp)
    if criterio != "confronto":
        return sorted(t, key=lambda c: (-t[c][6], *geral(c)))
    grupos = defaultdict(list)
    for c in t:
        grupos[t[c][6]].append(c)
    res = []
    for p in sorted(grupos, reverse=True):
        g = grupos[p]
        if len(g) > 1 and jogos:
            mini = calcular([j for j in jogos if j["m"] in g and j["v"] in g])
            g.sort(key=lambda c: (-mini[c][6], -(mini[c][4] - mini[c][5]), *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def campeoes() -> dict[int, str]:
    """ddrchamp.html: "1949/50   ZSG Horch Zwickau"; "1948      SG Planitz" (chave 1947)."""
    res = {}
    for m in re.finditer(r"^(\d{4})(?:/(\d{2}))?\s+(\S.*?)\s*(?:\[.*\])?\s*$", texto_rsssf(DADOS / "rsssf" / "ddrchamp.html"), re.M):
        a = int(m.group(1))
        if not m.group(2):
            a = a - 1 if a <= 1949 else a
        res[a] = clubes.esd(m.group(3).replace("Carl-Zeiss", "Carl Zeiss").replace("1.FC", "1. FC"), a) or m.group(3)
    return res


def texto_wiki(a: int) -> str:
    arq = DADOS / "wikipedia" / f"{wiki_titulo(a)}.wiki"
    return arq.read_text(encoding="utf-8") if arq.exists() else ""


def caixas(texto: str) -> list[dict]:
    """Fichas {{football box}} com a seção (fase) de cada uma."""
    marcas = [(m.start(), limpar(m.group(1))) for m in re.finditer(r"^=+\s*(.*?)\s*=+\s*$", texto, re.M)]
    res = []
    for m in re.finditer(r"(?i)\{\{\s*football box", texto):
        corpo = texto[m.start() + 2:_fecha(texto, m.start()) - 2]
        p = {}
        for x in _partes(corpo)[1:]:
            k, _, v = x.partition("=")
            p[k.strip().lower()] = v.strip()
        sc = re.search(r"(\d+)\s*(?:&ndash;|–|-)\s*(\d+)", p.get("score", ""))
        if not sc:
            continue
        d = re.search(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", limpar(p.get("date", "")))
        secao = next((t for pos, t in reversed(marcas) if pos < m.start()), "")
        fase = next((b for a_, b in FASES_EN if re.search(a_, secao)), secao)
        alvo = lambda s: (re.search(r"\[\[([^\]|]+)", s) or [None, None])[1]   # noqa: E731
        pub = re.sub(r"\D", "", limpar(p.get("attendance", "")))
        est = limpar(p.get("stadium", ""))
        res.append({"fase": fase, "data": f"{d.group(3)}-{MESES[d.group(2).lower()]:02d}-{int(d.group(1)):02d}" if d else None,
                    "nm": limpar(p.get("team1", "")), "nv": limpar(p.get("team2", "")), "tm": alvo(p.get("team1", "")),
                    "tv": alvo(p.get("team2", "")), "gm": int(sc.group(1)), "gv": int(sc.group(2)),
                    "estadio": est.split(",")[0].strip() or None, "cidade": est.rsplit(",", 1)[1].strip() if "," in est else None,
                    "publico": int(pub) if pub else None, "extra": limpar(p.get("score", ""))[sc.end():].strip()})
    return res


def mata_mata(a: int, camp: dict, tab, nomes, ocorr) -> tuple:
    T = temporada(a)
    jogos = []
    for x in caixas(texto_wiki(a)):
        m = (clubes.esd(x["tm"], a) if x["tm"] else None) or chave(x["nm"], a, "Wikipédia")
        v = (clubes.esd(x["tv"], a) if x["tv"] else None) or chave(x["nv"], a, "Wikipédia")
        nomes[m][f"wikipedia:{x['nm']}"].add(a)
        nomes[v][f"wikipedia:{x['nv']}"].add(a)
        jogos.append({**x, "m": m, "v": v})
    ordem_f = {f: i for i, f in enumerate(["Eliminatória", "Quartas de final", "Semifinal", "Final"])}
    alcance = defaultdict(int)
    for j in jogos:
        for c in (j["m"], j["v"]):
            alcance[c] = max(alcance[c], ordem_f.get(j["fase"], 0))
    final = next((j for j in jogos if j["fase"] == "Final"), None)
    campeao = camp.get(a)
    vice = next((c for c in (final["m"], final["v"]) if c != campeao), None) if final else None
    total = calcular(jogos)
    ordem = sorted(total, key=lambda c: (c != campeao, c != vice, -alcance[c], -total[c][6], -(total[c][4] - total[c][5])))
    for pos, c in enumerate(ordem, 1):
        j_, v_, e_, d_, gp, gc, p = total[c]
        tab["classificacao_final"].append({
            "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
            "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p, "ajuste_pontos": 0,
            "situacao": "campeao" if c == campeao else None, "fonte": "Wikipédia (en); ordem pela fase alcançada",
            "observacao": "mata-mata: sem classificação oficial além do campeão e do vice"})
    jogos.sort(key=lambda j: (j["data"] or "9999", ordem_f.get(j["fase"], 0)))
    for i, j in enumerate(jogos, 1):
        tab["partidas"].append({
            "id": f"{a}-{i:04d}", "temporada": T, "fase": j["fase"], "grupo": None, "rodada": None, "data": j["data"],
            "hora": None, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]), "gols_mandante": j["gm"],
            "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None, "resultado_especial": None,
            "estadio": j["estadio"], "cidade": j["cidade"], "publico": j["publico"], "fonte": "Wikipédia (en)",
            "fonte_id": None, "gols_texto": None, "observacao": j["extra"] or None, "arbitro": None})
    fases = sorted({j["fase"] for j in jogos}, key=lambda f: ordem_f.get(f, 0))
    for i, f in enumerate(fases, 1):
        tab["fases"].append({"temporada": T, "ordem": i, "fase": f, "tipo": "mata_mata", "num_grupos": None,
                             "formato_serie": "jogo_unico", "criterio": "resultado"})
    gols = sum(j["gm"] + j["gv"] for j in jogos)
    tab["edicoes"].append({"temporada": T, "ano_inicio": a + 1, "ano_fim": a + 1, "nome_oficial": "Ostzonenmeisterschaft",
                           "num_clubes": len(ordem), "pontos_vitoria": 2,
                           "formato": "mata-mata entre os campeões estaduais da zona soviética",
                           "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(vice) if vice else None,
                           "fontes": "Wikipédia (en)", "observacao": None})
    tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": None, "tabelas_conferidas": 0,
                               "tabelas_divergentes": 0, "gols": gols, "gols_com_autor": 0,
                               "observacao": f"campeão {clubes.exibicao(campeao)} (RSSSF)"})
    ocorr[a].append("mata-mata entre os campeões estaduais: os jogos são as fichas da Wikipédia (en)")
    return (T, "Wikipédia (en)", len(ordem), len(jogos), gols, 0, 0, clubes.exibicao(campeao), "")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    camp = campeoes()
    rs = {a: ler_rsssf(DADOS / "rsssf" / rsssf_pagina(a)) for a in TEMPORADAS if a not in MATA_MATA}
    nomes = defaultdict(lambda: defaultdict(set))
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel, criterios = [], {}
    for a in TEMPORADAS:
        ocorr[a].extend(EXPLICACOES.get(a, []))
        if a in MATA_MATA:
            linhas_rel.append(mata_mata(a, camp, tab, nomes, ocorr))
            continue
        T = temporada(a)
        r = rs[a]
        url_rs = URL_RSSSF + rsssf_pagina(a)
        url_w = "https://en.wikipedia.org/wiki/" + wiki_titulo(a).replace(" ", "_")
        jogos = []
        for x in r["jogos"]:
            m, v = chave(x["nm"], a, "RSSSF"), chave(x["nv"], a, "RSSSF")
            nomes[m][f"rsssf:{x['nm']}"].add(a)
            nomes[v][f"rsssf:{x['nv']}"].add(a)
            jogos.append({**x, "m": m, "v": v})
        clubes_ano = sorted({j["m"] for j in jogos} | {j["v"] for j in jogos})
        n = len(clubes_ano)
        esperados = n * (n - 1) * (3 // 2 if a != 1961 else 1) if a != 1955 else n * (n - 1) // 2
        if a == 1961:
            esperados = n * (n - 1) * 3 // 2
        if len(jogos) != esperados:
            ocorr[a].append(f"{len(jogos)} jogos de {esperados}")
        calc = calcular(jogos)
        # ---- conferência com as tabelas publicadas
        publicadas = []
        tb_rs = [dict(x, clube=chave(x["nome"], a, "RSSSF")) for x in r["tabela"]]
        if tb_rs:
            publicadas.append(("RSSSF", url_rs, tb_rs))
        tw = wiki_tabelas(texto_wiki(a))
        tb_w = max(tw, key=lambda tb: len(tb["times"]), default=None)
        if tb_w:
            linhas_w = []
            for x in tb_w["times"]:
                c = chave(x["nome"], a, "Wikipédia")
                linhas_w.append(dict(x, clube=c, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                     pontos=2 * (x["vitorias"] or 0) + (x["empates"] or 0) + (x["ajuste"] or 0)))
            publicadas.append(("Wikipédia", url_w, linhas_w))
        conferidas = divergentes = 0
        confere = {}
        for fonte, u, linhas in publicadas:
            erro = []
            for x in linhas:
                nomes[x["clube"]][f"{fonte.lower().replace('é', 'e')}:{x['nome']}"].add(a)
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = calc.get(x["clube"])
                if meu is None or pub != meu:
                    erro.append(f"{clubes.exibicao(x['clube'])} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": "Liga", "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": pub[0], "vitorias": pub[1], "empates": pub[2],
                    "derrotas": pub[3], "gols_pro": pub[4], "gols_contra": pub[5], "pontos": pub[6], "fonte": u})
            if len(linhas) != n:
                erro.append(f"a tabela tem {len(linhas)} clubes; os jogos, {n}")
            confere[fonte] = not erro
            if erro:
                divergentes += 1
                for e_ in erro[:6]:
                    ocorr[a].append(f"tabela publicada ({fonte}) x jogos — {e_}")
            else:
                conferidas += 1
        # ---- matriz da Wikipédia, jogo a jogo
        dif = []
        por_par = defaultdict(list)
        for j in jogos:
            por_par[(j["m"], j["v"])].append((j["gm"], j["gv"]))
        for g in wiki_resultados(texto_wiki(a)):
            cod = {k: clubes.esd(v, a) or clubes.esd(k, a) for k, v in g["nomes"].items()}
            for (c1, c2), pl in g["jogos"].items():
                par = (cod.get(c1), cod.get(c2))
                if None in par:
                    continue
                if sorted(pl) != sorted(por_par.get(par, [])) and not set(pl) <= set(por_par.get(par, [])):
                    dif.append(f"{clubes.exibicao(par[0])} x {clubes.exibicao(par[1])}: RSSSF "
                               f"{', '.join(f'{x}-{y}' for x, y in por_par.get(par, [])) or '—'}; Wikipédia "
                               f"{', '.join(f'{x}-{y}' for x, y in pl)}")
        for d in dif[:10]:
            ocorr[a].append(f"placar diferente na matriz da Wikipédia — {d}")
        if len(dif) > 10:
            ocorr[a].append(f"... e mais {len(dif) - 10} pares com placar diferente na matriz da Wikipédia")
        # ---- ordem oficial e critério
        base = tb_rs if tb_rs and len(tb_rs) == n else (linhas_w if tb_w else None)
        if base:
            ordem = [x["clube"] for x in sorted(base, key=lambda x: (x["posicao"] or 99))] if base is tb_rs else [x["clube"] for x in base]
            if set(ordem) != set(clubes_ano):
                ocorr[a].append("a tabela oficial tem outros clubes: fica a ordem calculada")
                ordem = ordenar(calc, "saldo")
        else:
            ordem = ordenar(calc, "saldo")
        tent = {cr: ordenar(calc, cr, jogos) for cr in ("saldo", "media", "confronto")}
        ok = [cr for cr, o in tent.items() if o == ordem]
        criterio = ok[0] if ok else min(tent, key=lambda cr: sum(x != y for x, y in zip(tent[cr], ordem)))
        criterios[a] = (criterio, bool(ok))
        if not ok:
            ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo é {criterio}")
        # ---- rebaixados, campeão, classificação
        prox = next((b for b in TEMPORADAS if b > a), None)
        prox_cl = {chave(x["nm"], prox, "RSSSF") for x in rs[prox]["jogos"]} | {chave(x["nv"], prox, "RSSSF") for x in rs[prox]["jogos"]} \
            if prox in rs else set()
        relegados_rs = {x["clube"] for x in tb_rs if re.search(r"(?i)relegated", x["resto"])}
        rebaixados = (relegados_rs or {c for c in clubes_ano if prox_cl and c not in prox_cl}) if a != 1990 else set()
        campeao = None if a in SEM_TITULO else camp.get(a)
        if a in SEM_TITULO:
            ocorr[a].append(SEM_TITULO[a])
        elif campeao != ordem[0]:
            ocorr[a].append(f"campeão da lista da RSSSF ({clubes.exibicao(campeao)}) diferente do 1º da tabela ({clubes.exibicao(ordem[0])})")
        pts_of = {x["clube"]: x["pontos"] for x in (base or [])}
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p = calc[c]
            pts = pts_of.get(c, p)
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": pts, "ajuste_pontos": pts - p,
                "situacao": "campeao" if c == campeao else "rebaixado" if c in rebaixados else None,
                "fonte": "RSSSF (ordem oficial)" if base is tb_rs else "Wikipédia (ordem oficial)",
                "observacao": ("1º da rodada de transição, sem título" if (a in SEM_TITULO and pos == 1) else None)})
        # ---- partidas e Corrida
        jogos.sort(key=lambda j: (j["rodada"], j["data"] or "9999", j["m"]))
        for i, j in enumerate(jogos, 1):
            tab["partidas"].append({
                "id": f"{a}-{i:04d}", "temporada": T, "fase": "Liga", "grupo": None, "rodada": j["rodada"], "data": j["data"],
                "hora": None, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": "awd" if j["vencedor"] else None, "estadio": None, "cidade": None, "publico": None,
                "fonte": "RSSSF", "fonte_id": None, "gols_texto": None,
                "observacao": (f"resultado dado fora de campo: vitória do "
                               f"{clubes.exibicao(j['m'] if j['vencedor'] == 'm' else j['v'])} (gols 0:0)"
                               + (f"; {j['nota']}" if j["nota"] else "")) if j["vencedor"] else (j["nota"] or None),
                "arbitro": None})
        pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
        for rd in sorted({j["rodada"] for j in jogos}):
            ate = [j for j in jogos if j["rodada"] <= rd]
            parcial = calcular(ate)
            for pos, c in enumerate(ordenar(parcial, criterio, ate), 1):
                jj, v_, e_, d_, gp, gc, p = parcial[c]
                tab["classificacao_rodada"].append({
                    "temporada": T, "rodada": rd, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p, "jogos": jj,
                    "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                    "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})
        # ---- edição, fase, conferência
        gols = sum(j["gm"] + j["gv"] for j in jogos)
        formato = ("turno único (rodada de transição)" if a == 1955 else "três turnos (39 rodadas)" if a == 1961 else
                   "pontos corridos (turno e returno)")
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a if a in ANO_CIVIL else a + 1,
                               "nome_oficial": "NOFV-Oberliga" if a == 1990 else "DDR-Oberliga", "num_clubes": n,
                               "pontos_vitoria": 2, "formato": formato, "campeao": clubes.exibicao(campeao) if campeao else None,
                               "vice": clubes.exibicao(ordem[1]) if campeao else None, "fontes": "RSSSF + Wikipédia (en)",
                               "observacao": SEM_TITULO.get(a)})
        crit_txt = {"saldo": "pontos, saldo de gols, gols pró", "media": "pontos, média de gols",
                    "confronto": "pontos, confronto direto, saldo de gols"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Liga", "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": esperados,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols,
                                   "gols_com_autor": 0, "observacao": f"campeão {clubes.exibicao(campeao) if campeao else '—'} (RSSSF)"})
        linhas_rel.append((T, "RSSSF + Wikipédia (en)", n, len(jogos), gols, conferidas, divergentes,
                           clubes.exibicao(campeao) if campeao else "— (sem título)", ""))
        print(f"{T}: {len(jogos)} jogos, tabelas {conferidas} ok / {divergentes} div, critério {criterio}"
              f"{'' if ok else ' (aprox.)'}, campeão {clubes.exibicao(campeao) if campeao else '—'}", flush=True)
    # ---- clubes, artilheiros, pacote
    for c in sorted(nomes):
        cidade, pais = clubes.cidade_pais(c)
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = [{"codigo": "GDR", "nome": "Alemanha Oriental", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, criterios)


def artilheiros(ocorr) -> list[dict]:
    """ddrtops.html: "1949/50  Heinz Satrapa   ZSG Horch Zwickau   23"; "   1955  ..."; empate na linha seguinte."""
    t = texto_rsssf(DADOS / "rsssf" / "ddrtops.html")
    fim = re.search(r"^\s*All-Time Topscorers\s*$", t, re.M)   # a seção (o topo da página também cita "All-Time")
    t = t[:fim.start()] if fim else t
    res, ano = [], None
    for l in t.split("\n"):
        m = re.match(r"^\s*(\d{4})(?:/(\d{2}))?\s+(\S.*?)\s{2,}(\S.*?)\s{2,}(\d+)", l)
        m2 = re.match(r"^\s{6,}(\S.*?)\s{2,}(\S.*?)\s{2,}(\d+)", l)
        if m:
            a = int(m.group(1))
            ano = a if (m.group(2) or a in ANO_CIVIL) else None
            nome, clube, gols = m.group(3), m.group(4), int(m.group(5))
        elif m2 and ano is not None:
            nome, clube, gols = m2.group(1), m2.group(2), int(m2.group(3))
        else:
            continue
        if ano not in TEMPORADAS:
            continue
        c = clubes.esd(clube, ano)
        if c is None:
            ocorr[ano].append(f"artilheiro com clube sem cadastro: {nome} ({clube})")
        res.append({"temporada": temporada(ano), "jogador": nome.strip(), "clube": clubes.exibicao(c) if c else None,
                    "gols": gols, "fonte": "RSSSF (tablesd/ddrtops.html)"})
    return res


def relatorio(linhas, ocorr, tab, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato da Alemanha Oriental — coleta de dados", "",
        "Gerado por `python coleta/gdr-1/importar.py`. Pacote em `data/coleta/gdr-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}: o campeonato da zona soviética (1948 e 1949, mata-mata) e a DDR-Oberliga de 1949/50 a "
        "1990/91 (ano civil de 1956 a 1960; a rodada de transição de 1955 sem título; a última, como NOFV-Oberliga).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- RSSSF (Andreas Werner e outros): página de cada temporada, com rodada, data e placar de cada jogo e a tabela final; "
        "lista de campeões e de artilheiros;",
        "- Wikipédia (en): tabela e matriz de resultados de cada temporada (conferência) e as fichas dos jogos de 1948 e 1949.", "",
        "**Regras:** 2 pontos por vitória. Jogo dado fora de campo: vitória e 2 pontos para um lado, gols 0:0 (como a RSSSF), "
        "marcado `awd`. Cada tabela publicada é comparada com a calculada dos jogos; a ordem da classificação final é a da "
        "tabela da RSSSF (sem ela, a da Wikipédia).", "",
        f"**Desempate:** o critério calculado que reproduz a ordem oficial (saldo de gols em {cr['saldo']}, média de gols em "
        f"{cr['media']}, confronto direto em {cr['confronto']}).", "",
        "| Temporada | Fontes | Clubes | Jogos | Gols | Tabelas ok / div. | Campeão |",
        "|---|---|---|---|---|---|---|",
    ]
    for T, f, n, j, g, ok, dv, camp, _ in linhas:
        out.append(f"| {T} | {f} | {n} | {j} | {g} | {ok} / {dv} | {camp} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for T, *_ in linhas:
        a = next(b for b in TEMPORADAS if temporada(b) == T)
        out.append(f"### {T}")
        out.append("")
        for o in ocorr.get(a, []) or ["sem ocorrências"]:
            out.append(f"- {o}")
        out.append("")
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_gdr.py`, pela linhagem do clube através das mudanças de nome e de cidade "
        "da RDA (Empor Lauter -> Hansa Rostock; SC Dynamo Berlin -> BFC Dynamo; KVP Leipzig -> Vorwärts Berlin -> Vorwärts "
        "Frankfurt/Oder; SC Lokomotive Leipzig -> 1. FC Lok -> VfB Leipzig). Os clubes que também jogaram a Bundesliga usam o "
        "nome do `ger-1` (Hansa Rostock, Union Berlin, Dynamo Dresden, Energie Cottbus, Carl Zeiss Jena, VfB Leipzig).", "",
        "## O que não deu para coletar", "",
        "- Autores dos gols, público e estádio dos jogos da Oberliga (a RSSSF traz só o placar).",
        "- A primeira fase (campeonatos estaduais) de 1948 e 1949.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
