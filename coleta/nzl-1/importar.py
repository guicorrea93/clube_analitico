"""Junta as fontes da 1ª divisão neozelandesa e grava o pacote em data/coleta/nzl-1/pacote/ e o relatório em docs/coleta/nzl-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler.py): base de jogos, fases, grupos, rodadas, datas e autores dos gols (uma página por temporada, nzYY / nzAAAA);
  as tabelas das páginas são a conferência e a classificação. A lista de campeões (nzchamp.html) traz campeão e vice;
- Wikipédia em inglês (wikipedia_nz.py): matriz de resultados das ligas regionais de 2022-2025 (a RSSSF só tem as tabelas),
  tabela de 1992 (a da RSSSF não fecha) e segunda fonte do campeão;
- ogol (baixar_ogol.py): fase de liga de 2010/11 e 2011/12 (a RSSSF só tem as tabelas), ligas regionais Central e Southern de
  2025, e a data dos jogos da RSSSF que vêm sem ela (2008/09 em diante).

Uso: python coleta/nzl-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
sys.path.insert(0, str(AQUI))
import autores  # noqa: E402
import conferir as conf  # noqa: E402
import wikipedia_nz  # noqa: E402
from clubes_nzl import CLUBES, clube  # noqa: E402
from edicoes import (EDICOES, ELIM, FINAL, LIGA, NACIONAL, PACOTE, PASTA_DADOS, PRELIM, REGIONAL, RELATORIO, SEMI, SLUG,  # noqa: E402
                     UNICA, Edicao)
from explicacoes import EXPLICACOES, WIKI_FORA  # noqa: E402
from ler import campeoes  # noqa: E402

FASES_LIGA = (UNICA, LIGA, NACIONAL)
GRUPOS = {"Norte": "Northern League", "Centro": "Central League", "Sul": "Southern League",
          "Ilha Norte": "North Island Soccer League", "Ilha Sul": "South Island Soccer League"}
CRITERIO = {
    SEMI: "semifinais entre os 4 primeiros da fase anterior (de 1996 a 2003 e em 2004/05: semifinal maior, 1º x 2º, cujo "
          "vencedor vai à final, e menor, 3º x 4º)",
    PRELIM: "o perdedor da semifinal maior contra o vencedor da menor; quem vence vai à final",
    ELIM: "3º x 6º e 4º x 5º da fase de liga",
    FINAL: "Grand Final: decide o título",
}


def tid(t: str) -> str:
    return t.replace("/", "-")


def wiki_campeao(e: Edicao) -> str | None:
    """Campeão pela Wikipédia: "champions"/"winners" do infobox ou o clube com status C na tabela."""
    arq = wikipedia_nz.PASTA / f"{tid(e.temporada)}.wiki"
    if not arq.exists():
        return None
    txt = arq.read_text(encoding="utf-8")
    m = re.search(r"\|\s*(?:champions|winners)\s*=\s*(\[\[[^\]]*\]\]|[^\n|]+)", txt, re.I)
    if m and m.group(1).strip():
        return clube(wikipedia_nz._nome(m.group(1)), e.ano_inicio)
    m = re.search(r"\|\s*status_(\w+)\s*=\s*C\b", txt)
    if m:
        n = re.search(r"\|\s*name_" + m.group(1) + r"\s*=\s*(\[\[[^\]]*\]\]|[^\n|]+)", txt)
        if n:
            return clube(wikipedia_nz._nome(n.group(1)), e.ano_inicio)
    return None


def ogol_datas(e: Edicao) -> dict[tuple[str, str], list[dict]]:
    arq = PASTA_DADOS / "ogol" / f"{tid(e.temporada)}.json"
    out: dict[tuple[str, str], list[dict]] = defaultdict(list)
    if arq.exists():
        for x in json.loads(arq.read_text(encoding="utf-8")):
            a, b = clube(x["mandante"], e.ano_inicio), clube(x["visitante"], e.ano_inicio)
            if a and b:
                out[(a, b)].append(x)
    return out


def montar(e: Edicao, cps: dict) -> dict:
    jogos, usadas, difs, falta = conf.conferir(e)
    assert not falta, f"{e.temporada}: nomes sem clube {falta}"
    tabelas = conf.TODAS[e.temporada]
    ordem_f = list(dict.fromkeys(f for _, _, _, f, _ in e.trechos))
    # ordem dos jogos: fase, depois a ordem na fonte (página e linha; ogol e Wikipédia no fim de cada fase)
    peso = {"rodadas": 0, "matriz": 0, "ogol": 1, "wikipedia": 1}
    jogos.sort(key=lambda j: (ordem_f.index(j.fase), list(GRUPOS).index(j.grupo) if j.grupo else -1, peso[j.origem],
                              j.data or "" if j.origem == "ogol" else "", j.linha))
    # data do ogol para os jogos da RSSSF sem data (mesmo mando; o mais perto na ordem)
    og = ogol_datas(e)
    for j in jogos:
        if j.data or j.origem != "rodadas":
            continue
        cands = og.get((j.mandante, j.visitante), [])
        if len(cands) == 1 and (cands[0]["gols_mandante"], cands[0]["gols_visitante"]) == (j.gm, j.gv):
            j.data, j.ogol_id = cands[0]["data"], cands[0]["id"]
        elif j.rodada and (c := [x for x in cands if x["rodada"] == j.rodada and (x["gols_mandante"], x["gols_visitante"]) == (j.gm, j.gv)]):
            j.data, j.ogol_id = c[0]["data"], c[0]["id"]
    # a lista de campeões da RSSSF dá 1996/97 e 1997/98 pelo ano em que terminam ("1997", "1998")
    rs = cps.get(e.temporada) or cps.get(str(e.ano_fim) if e.temporada in ("1996/97", "1997/98") else "")
    campeao = clube(rs[0], e.ano_inicio) if rs else None
    vice = clube(rs[1], e.ano_inicio) if rs else None
    return {"e": e, "jogos": jogos, "usadas": usadas, "tabelas": tabelas, "difs": difs, "fases": ordem_f, "campeao": campeao,
            "vice": vice, "rsssf_campeao": rs[0] if rs else "", "wiki_campeao": wiki_campeao(e)}


def classificacao(d: dict) -> list[dict]:
    """Classificação final. A tabela da fase de liga (ou nacional) na ordem oficial; depois os clubes que caíram na fase
    regional, pela posição no grupo e pontos por jogo. Campeão (da final ou da liga) em 1º e vice em 2º."""
    e = d["e"]
    pv = e.pontos_vitoria
    tabs = [t for t in d["tabelas"] if t.usada or t.sem_jogos]
    liga = [t for t in tabs if t.fase in FASES_LIGA]
    linhas = []
    if e.temporada == "1992":   # a tabela da RSSSF não fecha (581 gols pró x 580 contra); a da Wikipédia fecha com os jogos
        wt = wikipedia_nz.tabelas("1992")[0]
        for r in wt["linhas"]:
            linhas.append({"clube": clube(r["nome"], 1992), "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"],
                           "gc": r["gc"], "pts": pv * r["v"] + r["e"], "obs": "", "fonte": "Wikipédia (1992 New Zealand National Soccer League)"})
    elif liga:
        t = liga[-1]
        for r in t.linhas:
            linhas.append({"clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                           "pts": r["pts"], "obs": r["obs"], "fonte": f"RSSSF ({t.pagina}, linha {t.linha})"})
    ja = {r["clube"] for r in linhas}
    regionais = []
    for t in tabs:
        if t.fase != REGIONAL:
            continue
        for k, r in enumerate(t.linhas, 1):
            if r["clube"] not in ja:
                regionais.append((r["pos"] or k, -(r["pts"] / r["j"]) if r["j"] else 0, {
                    "clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"], "pts": r["pts"],
                    "obs": f"campanha na fase regional ({GRUPOS[t.grupo]}, {r['pos'] or k}º)" + (f"; {r['obs']}" if r["obs"] else ""),
                    "fonte": f"RSSSF ({t.pagina}, linha {t.linha})"}))
    linhas += [x[2] for x in sorted(regionais, key=lambda x: x[:2])]
    for alvo, k in ((d["campeao"], 0), (d["vice"], 1)):
        if alvo and any(r["clube"] == alvo for r in linhas) and linhas[k]["clube"] != alvo:
            r = next(r for r in linhas if r["clube"] == alvo)
            linhas.remove(r)
            linhas.insert(k, r)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
        r["obs"] = re.sub(r"\s+", " ", re.sub(r"\[[\d\s\-:]+\]", "", r["obs"] or "")).strip(" ;")   # colunas extras da tabela
        r["ajuste"] = r["pts"] - (pv * r["v"] + r["e"]) if None not in (r["pts"], r["v"], r["e"]) else None
    return linhas


def situacao(r: dict, d: dict) -> str:
    if r["clube"] == d["campeao"]:
        return "campeao"
    if r["clube"] == d["vice"]:
        return "vice"
    if re.search(r"relegat", r.get("obs", ""), re.I):
        return "rebaixado"
    return ""


def placar_oficial(j) -> tuple:
    """(gols mandante, gols visitante, resultado_especial, observação) como vão para o pacote."""
    obs = []
    gm, gv, esp = j.gm, j.gv, ""
    if j.especial in ("wo_m", "wo_v"):
        venc = j.mandante if j.especial == "wo_m" else j.visitante
        obs.append(f"pontos para o {venc} (decisão fora de campo)" + (f"; placar em campo {j.gm}-{j.gv}" if j.gm is not None else ""))
        gm = gv = None
        esp = "awd" if j.gm is not None else "wo"
    elif j.gm_of is not None and (j.gm_of, j.gv_of) != (j.gm, j.gv):
        obs.append(f"placar em campo {j.gm}-{j.gv}")
        gm, gv, esp = j.gm_of, j.gv_of, "awd"
    elif j.especial == "abd":
        obs.append(f"abandonado{f' com {j.gm}-{j.gv}' if j.gm is not None else ''}; não vale na tabela")
        gm = gv = None
        esp = "abd"
    elif j.especial == "awd":
        esp = "awd"
    return gm, gv, esp, obs


def _csv(arquivo: str, cab: list[str], linhas: list[list]) -> None:
    with open(PACOTE / arquivo, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cab)
        w.writerows(linhas)


def esperados(d: dict) -> int:
    """Jogos esperados: metade da soma dos jogos de cada tabela conferida (ou da fase sem jogos), mais os do mata-mata."""
    n = 0
    com_tabela = set()
    for t in d["tabelas"]:
        if t.usada or t.sem_jogos or (t.fase, t.grupo) in {(u.fase, u.grupo) for u in d["usadas"]}:
            if (t.fase, t.grupo) in com_tabela:
                continue
            com_tabela.add((t.fase, t.grupo))
            n += sum(r["j"] for r in t.linhas) // 2
    n += sum(1 for j in d["jogos"] if (j.fase, j.grupo) not in com_tabela)
    n += sum(1 for j in d["jogos"] if j.especial == "abd" and (j.fase, j.grupo) in com_tabela)   # abandonado e jogado de novo
    return n


def formato(d: dict) -> str:
    e = d["e"]
    desc = {UNICA: "pontos corridos", LIGA: "fase de liga", NACIONAL: "fase nacional", REGIONAL: "ligas regionais",
            ELIM: "rodada eliminatória", SEMI: "semifinais", PRELIM: "final preliminar", FINAL: "final"}
    partes = []
    for f in d["fases"]:
        n = len({r["clube"] for t in d["tabelas"] if t.fase == f and (t.usada or t.sem_jogos) for r in t.linhas})
        x = desc[f]
        if f == REGIONAL:
            x += f" ({len({t.grupo for t in d['tabelas'] if t.fase == f})} grupos, {n} clubes)"
        elif f in (UNICA, LIGA, NACIONAL) and n:
            x += f" ({n} clubes)"
        partes.append(x)
    txt = " + ".join(partes)
    if d["e"].incompleta:
        txt = f"jogos incompletos: {txt}"
    return txt


def gravar(eds: list[dict]) -> None:
    PACOTE.mkdir(parents=True, exist_ok=True)
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    ed_l, fa_l, pa_l, go_l, cl_l, tp_l, co_l = [], [], [], [], [], [], []
    for d in eds:
        e = d["e"]
        jogos = d["jogos"]
        pref = {"rodadas": "rsssf", "matriz": "rsssf", "ogol": "ogol", "wikipedia": "wikipedia"}
        for j in jogos:
            nomes_fonte[j.mandante][f"{pref[j.origem]}:{j.nome_m}"].append(e.ano_inicio)
            nomes_fonte[j.visitante][f"{pref[j.origem]}:{j.nome_v}"].append(e.ano_inicio)
        for t in d["tabelas"]:
            if t.usada or t.sem_jogos:
                for r in t.linhas:
                    nomes_fonte[r["clube"]][f"rsssf:{r['nome']}"].append(e.ano_inicio)
        for (a, b), xs in ogol_datas(e).items():   # grafia do ogol de todos os calendários guardados (escudos)
            for x in xs:
                nomes_fonte[a][f"ogol:{x['mandante']}"].append(e.ano_inicio)
                nomes_fonte[b][f"ogol:{x['visitante']}"].append(e.ano_inicio)
        # partidas e gols
        n_gols = n_autor = 0
        for n, j in enumerate(jogos, 1):
            pid = f"{tid(e.temporada)}-{n:04d}"
            gm, gv, esp, obs = placar_oficial(j)
            if j.nota and not re.fullmatch(r"\s*(at |aet|\d)", j.nota):
                obs.append(j.nota)
            if j.correcao:
                obs.append(f"corrigido: {j.correcao}")
            sep = autores.gols(j.gols_texto, j.gm, j.gv, j.pagina) if j.gols_texto and not esp else None
            if gm is not None:
                n_gols += gm + gv
            if sep:
                for lado, clube_gol in ((sep[0], j.mandante), (sep[1], j.visitante)):
                    for jog, mi, ac, tipo in lado:
                        go_l.append([pid, clube_gol, jog, mi if mi is not None else "", ac or "", tipo, "RSSSF"])
                n_autor += gm + gv
            fonte = {"rodadas": "RSSSF", "matriz": "RSSSF", "ogol": "ogol", "wikipedia": "Wikipédia"}[j.origem]
            fid = (f"rsssf:{j.pagina}:{j.linha}" if j.origem in ("rodadas", "matriz") else
                   f"ogol:{j.linha}" if j.origem == "ogol" else f"wikipedia:{tid(e.temporada)}:{GRUPOS.get(j.grupo, '')}")
            if getattr(j, "ogol_id", None):
                fid += f"|ogol:{j.ogol_id}"
            pa_l.append([pid, e.temporada, j.fase, GRUPOS.get(j.grupo, j.grupo), j.rodada or "", j.data or "", "", j.mandante, j.visitante,
                         "" if gm is None else gm, "" if gv is None else gv, "" if j.pen_m is None else j.pen_m,
                         "" if j.pen_v is None else j.pen_v, esp, j.local or "", "", "", fonte, fid,
                         j.gols_texto if j.gols_texto and not sep else "", "; ".join(obs)])
        d["n_gols"], d["n_autor"] = n_gols, n_autor
        # fases
        for k, f in enumerate(d["fases"], 1):
            js = [j for j in jogos if j.fase == f]
            pares = Counter(frozenset((j.mandante, j.visitante)) for j in js)
            tipo = "grupos" if f == REGIONAL else "liga" if f in FASES_LIGA else "mata_mata"
            serie = "pontos_corridos" if tipo != "mata_mata" else ("ida_volta" if pares and max(pares.values()) > 1 else "jogo_unico")
            ng = len({t.grupo for t in d["tabelas"] if t.fase == f}) if f == REGIONAL else ""
            fa_l.append([e.temporada, k, f, tipo, ng, serie, CRITERIO.get(f, "")])
        # classificação
        cls = classificacao(d)
        d["cls"] = cls
        for r in cls:
            cl_l.append([e.temporada, r["pos"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"], r["pts"],
                         r["ajuste"] if r["ajuste"] else "", situacao(r, d), r["fonte"], r["obs"]])
        # tabelas publicadas
        for t in d["tabelas"]:
            if not (t.usada or t.sem_jogos):
                continue
            for k, r in enumerate(t.linhas, 1):
                tp_l.append([e.temporada, t.fase, GRUPOS.get(t.grupo, t.grupo), r["pos"] or k, r["nome"], r["clube"], r["j"], r["v"], r["e"],
                             r["d"], r["gp"], r["gc"], r["pts"], f"RSSSF ({t.pagina}, linha {t.linha})"])
        # edição
        clubes_ed = {j.mandante for j in jogos} | {j.visitante for j in jogos} | {r["clube"] for r in cls}
        lider = next((t.linhas[0]["clube"] for t in d["tabelas"] if t.fase in (LIGA, NACIONAL) and (t.usada or t.sem_jogos)), None)
        obs = [x for x in (e.obs, e.incompleta) if x]
        if lider and lider != d["campeao"] and FINAL in d["fases"]:
            obs.append(f"1º da {'fase nacional' if NACIONAL in d['fases'] else 'fase de liga'}: {lider}")
        fontes = ["RSSSF"] + (["Wikipédia"] if any(j.origem == "wikipedia" for j in jogos) or e.temporada == "1992" else []) + \
            (["ogol"] if any(j.origem == "ogol" or getattr(j, "ogol_id", None) for j in jogos) else [])
        ed_l.append([e.temporada, e.ano_inicio, e.ano_fim, e.nome_oficial, len(clubes_ed), e.pontos_vitoria, formato(d),
                     d["campeao"] or "", d["vice"] or "", " + ".join(fontes), "; ".join(obs)])
        # conferência
        ndif = len({id(t) for t, *_ in d["difs"]})
        wc = d["wiki_campeao"]
        ob = [f"campeão {d['campeao']} (RSSSF: {d['rsssf_campeao']}; Wikipédia: {wc or 'sem a informação'})"]
        if wc and wc != d["campeao"]:
            ob.append("ATENÇÃO: campeão diferente na Wikipédia")
        if ndif:
            ob.append(EXPLICACOES.get(e.temporada, "divergência sem explicação"))
        if e.incompleta:
            ob.append(e.incompleta)
        co_l.append([e.temporada, len(jogos), esperados(d), len(d["usadas"]), ndif, n_gols, n_autor, "; ".join(ob)])

    _csv("edicoes.csv", ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "formato", "campeao", "vice",
                         "fontes", "observacao"], ed_l)
    _csv("fases.csv", ["temporada", "ordem", "fase", "tipo", "num_grupos", "formato_serie", "criterio"], fa_l)
    _csv("partidas.csv", ["id", "temporada", "fase", "grupo", "rodada", "data", "hora", "mandante", "visitante", "gols_mandante",
                          "gols_visitante", "penaltis_mandante", "penaltis_visitante", "resultado_especial", "estadio", "cidade", "publico",
                          "fonte", "fonte_id", "gols_texto", "observacao"], pa_l)
    _csv("gols.csv", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "tipo", "fonte"], go_l)
    _csv("cartoes.csv", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "cor", "fonte"], [])
    _csv("classificacao_final.csv", ["temporada", "posicao", "clube", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra",
                                     "pontos", "ajuste_pontos", "situacao", "fonte", "observacao"], cl_l)
    _csv("tabelas_publicadas.csv", ["temporada", "fase", "grupo", "posicao", "nome_fonte", "clube", "jogos", "vitorias", "empates",
                                    "derrotas", "gols_pro", "gols_contra", "pontos", "fonte"], tp_l)
    _csv("artilheiros.csv", ["temporada", "jogador", "clube", "gols", "fonte"], [])
    _csv("conferencia.csv", ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols", "gols_com_autor",
                             "observacao"], co_l)
    usados = set(nomes_fonte) | {r[2] for r in cl_l}
    clubes_l = []
    for c in sorted(usados):
        cidade, regiao = CLUBES[c]
        nf = []
        for k, anos in sorted(nomes_fonte[c].items()):
            a = sorted(set(anos))
            nf.append(f"{k}:{a[0]}" + (f"-{a[-1]}" if a[-1] != a[0] else ""))
        clubes_l.append([c, regiao, cidade, "NZL", "|".join(nf)])
    _csv("clubes.csv", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], clubes_l)
    comp = {"slug": SLUG, "nome": "Campeonato Neozelandês", "nome_curto": "Neozelandês", "tipo": "liga", "nivel": 1, "pais": "NZL",
            "pais_nome": "Nova Zelândia", "regiao": None, "confederacao": "OFC", "rotulo_painel": "Neozelandês",
            "menu_painel": "Nova Zelândia · 1ª divisão", "do_painel": "do Campeonato Neozelandês", "o_painel": "o Campeonato Neozelandês",
            "observacao": "1ª divisão da Nova Zelândia de 1970 a 2025, uma edição por título, como na lista de campeões nacionais da "
                          "RSSSF: National Soccer League (1970-1992, pontos corridos), Superclub (1993-1995: ligas regionais, fase "
                          "nacional e mata-mata), Summer Soccer League (1996-1997/98), North e South Island League com final (1999), "
                          "National League (2000-2003), NZFC/Premiership (2004/05 a 2020/21, liga e mata-mata) e National League "
                          "(2022-2025: ligas regionais, fase nacional e final). Desde 1993 o campeão é o da final; 2004 e 2021 não "
                          "tiveram campeão. Sem jogos só a fase nacional de 1994."}
    (PACOTE / "competicao.json").write_text(json.dumps(comp, ensure_ascii=False, indent=1), encoding="utf-8")


def relatorio(eds: list[dict]) -> None:
    tot_j = sum(len(d["jogos"]) for d in eds)
    tot_g = sum(d["n_gols"] for d in eds)
    tot_a = sum(d["n_autor"] for d in eds)
    out = [f"# Coleta: Campeonato Neozelandês (`{SLUG}`)", "",
           "Gerado por `python coleta/nzl-1/importar.py`. Pacote em `data/coleta/nzl-1/pacote/`.", "",
           "## Resumo", "",
           f"- {len(eds)} edições (1970-2025), {tot_j} jogos, {tot_g} gols, {tot_a} com autor.",
           "- Escopo aprovado pelo Guilherme em 23/11/2026: começa em 1970 (1ª liga nacional); desde 1993 o campeão é o da final, "
           "com o 1º da fase de liga na observação; 2004 (finais canceladas) e 2021 (só a South Central Series) ficam de fora; as "
           "ligas regionais que classificam para a fase nacional (1993-1995, 1999, 2022-2025) entram como 1ª fase; o time reserva "
           "do Wellington Phoenix (e o do Auckland FC em 2025) leva \"Reserves\" no nome.",
           "- Classificação final: a tabela da fase de liga (ou nacional) na ordem oficial, com campeão e vice no topo; os clubes "
           "que caíram na fase regional vêm depois, pela posição no grupo, com a campanha da fase regional.",
           "",
           "## Fontes", "",
           "- **RSSSF** (`data/coleta/nzl-1/rsssf/`, baixadas por `baixar_rsssf.py`): lista de campeões (`nzchamp.html`) e uma página "
           "por temporada. 1970-1992: tabela e matriz de resultados (sem data); 1993-1995: ligas regionais (matriz) e fase nacional "
           "(rodadas, com autores; 1994 só a tabela); 1996-2007/08: rodadas com data e autores; 2008/09 em diante: rodadas com data, "
           "sem autores; 2010/11 e 2011/12: só as tabelas e o mata-mata.",
           "- **Wikipédia em inglês** (`data/coleta/nzl-1/wikipedia/`, `baixar_wikipedia.py`): matriz de resultados das ligas "
           "regionais de 2022-2025, tabela de 1992 e segunda fonte do campeão (infobox ou status \"C\" na tabela).",
           "- **ogol** (`data/coleta/nzl-1/ogol/` e cache em `data/cache/ogol-nzl-1/`, `baixar_ogol.py`): calendários de 2008/09 a "
           "2025 (as edições anteriores do ogol só têm o campeão). Entram a fase de liga de 2010/11 e 2011/12, as ligas Central e "
           "Southern de 2025 e a data de jogos da RSSSF sem data.",
           "- A ESPN não cobre a Nova Zelândia.", "",
           "## Correções e decisões", ""]
    import explicacoes as ex
    for k, (a, b, m) in ex.CONSERTA_TEXTO.items():
        out.append(f"- `{k[0]}`, linha {k[1]}: \"{a}\" -> \"{b}\": {m}.")
    for k, v in ex.CORRIGE.items():
        if v is not None:
            out.append(f"- `{' / '.join(str(x) for x in k)}`: {v[1]}.")
    for k, v in ex.WIKI_FORA.items():
        out.append(f"- {k[0]} ({GRUPOS[k[1]]}): {v}.")
    out += ["", "## Divergências que ficam (erro da própria fonte)", ""]
    for t, v in ex.EXPLICACOES.items():
        out.append(f"- **{t}:** {v}")
    out += ["", "## Edição a edição", "",
            "| Temporada | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Fontes | Observação |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for d in eds:
        e = d["e"]
        obs = []
        if d["difs"]:
            obs.append(f"{len(d['difs'])} divergência(s) com a tabela")
        if d["wiki_campeao"] and d["wiki_campeao"] != d["campeao"]:
            obs.append(f"Wikipédia: {d['wiki_campeao']}")
        if e.incompleta:
            obs.append(e.incompleta)
        fontes = "RSSSF" + (" + Wikipédia" if any(j.origem == "wikipedia" for j in d["jogos"]) else "") + \
                 (" + ogol" if any(j.origem == "ogol" for j in d["jogos"]) else "")
        out.append(f"| {e.temporada} | {formato(d)} | {len(d['jogos'])} | {esperados(d)} | {d['n_gols']} | {d['n_autor']} | "
                   f"{d['campeao']} | {d['vice']} | {fontes} | {'; '.join(obs)} |")
    out += ["", "## O que não deu para coletar", "",
            "- Fase nacional de 1994 (28 jogos): a RSSSF e a Wikipédia só têm a tabela.",
            "- Autores dos gols de 1970-1992, de 1994, de 1997/98 e de 2008/09 em diante (a RSSSF não traz; o ogol tem só na página "
            "de cada jogo).",
            "- Data dos jogos de 1970-1995 (matrizes) e das ligas regionais de 2022-2024 (matriz da Wikipédia).",
            "- Hora, estádio, público e cartões: nenhuma fonte aberta para a liga inteira.",
            "- Artilheiros: a RSSSF lista só em algumas temporadas; fica para depois.", ""]
    RELATORIO.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    cps = campeoes()
    eds = [montar(e, cps) for e in EDICOES]
    gravar(eds)
    relatorio(eds)
    for d in eds:
        aviso = " ATENÇÃO campeão Wikipédia " + d["wiki_campeao"] if d["wiki_campeao"] and d["wiki_campeao"] != d["campeao"] else ""
        print(f"{d['e'].temporada}: {len(d['jogos'])} jogos ({esperados(d)} esperados), {d['n_autor']}/{d['n_gols']} gols com autor, "
              f"campeão {d['campeao']}, vice {d['vice']}{aviso}")


if __name__ == "__main__":
    main()
