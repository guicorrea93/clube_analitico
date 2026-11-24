"""Junta as fontes da 1ª divisão de Fiji e grava o pacote em data/coleta/fij-1/pacote/ e o relatório em docs/coleta/fij-1.md.

Fontes:
- RSSSF (ler.py): lista de campeões (fijichamp.html, "League Championship (for Districts)", 1977-2026) e as páginas por ano
  (jogos, datas, rodadas, autores dos gols; tabelas para a conferência e a classificação);
- Wikipédia em inglês (data/coleta/fij-1/wikipedia/liga.wiki): segunda fonte do campeão;
- ogol (data/coleta/fij-1/ogol/): os jogos de 2011 (a RSSSF só tem a tabela), a data dos jogos da RSSSF sem data e a grafia
  dos times para os escudos.

Uso: python coleta/fij-1/importar.py
"""
from __future__ import annotations

import copy
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
from clubes_fij import CLUBES, clube  # noqa: E402
from edicoes import EDICOES, GRUPOS, LIGA, PACOTE, PASTA_DADOS, REBAIX, RELATORIO, SLUG, TITULO, UNICA, Edicao  # noqa: E402

REGIONAL = LIGA   # (nomes do importador da Nova Caledônia: aqui a "fase regular")
ELIM, QUARTAS, SEMI, TERCEIRO, FINAL = "Rodada preliminar", "Quartas de final", "Semifinal", "Disputa do 3º lugar", "Final"
from explicacoes import EXPLICACOES  # noqa: E402
from ler import campeoes  # noqa: E402

FASES_LIGA = (UNICA, REGIONAL, REBAIX, GRUPOS, TITULO)
NIVEL = {ELIM: 1, QUARTAS: 2, SEMI: 3, TERCEIRO: 3, FINAL: 4}
CRITERIO = {
    LIGA: "todos contra todos", GRUPOS: "dois grupos (Pool 1 e Pool 2)",
    TITULO: "os primeiros da fase anterior (Super 6/Super Six); o 1º é o campeão",
    REBAIX: "os últimos da fase anterior (Pepsi 4/Bottom Four); o último cai ou vai à repescagem",
}


def tid(t: str) -> str:
    return t.replace("/", "-")


def wiki_campeoes() -> dict[str, str]:
    """Campeões pela Wikipédia em inglês (página "Fiji Premier League", tabela "Champions": time, títulos, anos)."""
    arq = PASTA_DADOS / "wikipedia" / "liga.wiki"
    if not arq.exists():
        return {}
    out, time = {}, None
    for l in arq.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\|\s*\[\[(?:[^|\]]*\|)?([^\]]*)\]\]\s*$", l)
        if m:
            time = m.group(1)
            continue
        if time and re.fullmatch(r"\|\s*\d{4}(\s*,\s*\d{4})*\s*", l):
            for a in re.findall(r"\d{4}", l):
                out[a] = clube(time, int(a))
            time = None
    return out


def ogol_jogos(e: Edicao) -> dict[tuple[str, str], list[dict]]:
    arq = PASTA_DADOS / "ogol" / f"{tid(e.temporada)}.json"
    out: dict[tuple[str, str], list[dict]] = defaultdict(list)
    if arq.exists():
        for x in json.loads(arq.read_text(encoding="utf-8")):
            a, b = clube(x["mandante"], e.ano_inicio), clube(x["visitante"], e.ano_inicio)
            if a and b:
                out[(a, b)].append(x)
    return out





def montar(e: Edicao, cps: dict, wcp: dict) -> dict:
    c, v, tr = cps[e.temporada]
    d = {"e": e, "jogos": [], "usadas": [], "tabelas": [], "difs": [], "fases": [], "campeao": clube(c, e.ano_inicio),
         "vice": clube(v, e.ano_inicio) if v else None, "terceiro": clube(tr, e.ano_inicio) if tr else None,
         "rsssf_campeao": c, "wiki_campeao": wcp.get(e.temporada)}
    jogos, usadas, difs, falta = conf.conferir(e)
    assert not falta, f"{e.temporada}: nomes sem clube {falta}"
    d.update(jogos=jogos, usadas=usadas, difs=difs, tabelas=conf.TODAS.get(e.temporada, []),
             fases=list(dict.fromkeys([f for _, _, _, f, _ in e.trechos] + [j.fase for j in jogos])))
    d["fases"] = [f for f in d["fases"] if any(j.fase == f for j in jogos) or any(t.fase == f for t in d["tabelas"])]
    og = ogol_jogos(e)
    for j in jogos:   # data do ogol para jogo sem data (mesmo mando e placar)
        cand = [x for x in og.get((j.mandante, j.visitante), []) if (x["gols_mandante"], x["gols_visitante"]) == (j.gm, j.gv)]
        if len(cand) == 1:
            j.ogol_id = cand[0]["id"]
            j.data = j.data or cand[0]["data"]
    fin = [j for j in jogos if j.fase == FINAL]
    if not d["vice"] and fin:
        d["vice"] = fin[-1].visitante if fin[-1].mandante == d["campeao"] else fin[-1].mandante
    if not d["vice"]:
        for f in (TITULO, UNICA):
            tabs = [t for t in _junta([x for x in d["tabelas"] if x.linhas]) if t.fase == f and len(t.linhas) > 1]
            if tabs:
                d["vice"] = next(r["clube"] for r in tabs[-1].linhas if r["clube"] != d["campeao"])
                break
    ter = [j for j in jogos if j.fase == TERCEIRO]
    if not d["terceiro"] and ter and ter[-1].gm is not None:
        j = ter[-1]
        d["terceiro"] = j.mandante if (j.gm, j.pen_m or 0) > (j.gv, j.pen_v or 0) else j.visitante
    return d


def _junta(tabs: list) -> list:
    """Tabela cortada em duas pela linha de rebaixamento: as partes seguidas da mesma fase viram uma."""
    out = []
    for t in tabs:
        if out and out[-1].fase == t.fase and out[-1].pagina == t.pagina and t.linhas and t.linhas[0]["pos"] and \
                out[-1].linhas[-1]["pos"] and t.linhas[0]["pos"] == out[-1].linhas[-1]["pos"] + 1:
            out[-1] = copy.copy(out[-1])   # cópia: a tabela original (tabelas_publicadas) fica como a página publica
            out[-1].linhas = out[-1].linhas + t.linhas
        else:
            out.append(t)
    return out


def classificacao(d: dict) -> list[dict]:
    """Campeão, vice e 3º; depois o playoff do título (ordem oficial), os eliminados do mata-mata (da fase mais alta para a
    mais baixa) e as tabelas da fase única, de grupos ou da Grande Terre (com o grupo do rebaixamento à frente da fase
    regular para quem jogou os dois). Edição só com o campeão: campeão (e vice e 3º, quando a lista dá)."""
    e = d["e"]
    linhas_c: list[dict] = []
    vistos: set[str] = set()

    def add(c, r=None, fonte="", obs=""):
        if not c or c in vistos:
            return
        vistos.add(c)
        linhas_c.append({"clube": c, "j": r["j"] if r else None, "v": r["v"] if r else None, "e": r["e"] if r else None,
                         "d": r["d"] if r else None, "gp": r["gp"] if r else None, "gc": r["gc"] if r else None,
                         "pts": r["pts"] if r else None, "obs": obs, "fonte": fonte or "lista de campeões da RSSSF"})

    tabs = _junta([t for t in d["tabelas"] if t.linhas])
    linha_de = {}
    for f in (GRUPOS, REGIONAL, REBAIX, UNICA, TITULO):   # a última tabela que traz o clube dá a campanha
        for t in [t for t in tabs if t.fase == f]:
            for r in t.linhas:
                linha_de[r["clube"]] = (r, f"RSSSF ({t.pagina}, linha {t.linha})", f"campanha na {f.lower()}" if f != UNICA else "")
    for c in (d["campeao"], d["vice"], d["terceiro"]):
        add(c, *linha_de.get(c, (None, "", "")))
    for t in [t for t in tabs if t.fase == TITULO][-1:]:
        for r in t.linhas:
            add(r["clube"], *linha_de[r["clube"]])
    mata = sorted({j.fase for j in d["jogos"] if j.fase in NIVEL}, key=lambda f: -NIVEL[f])
    for f in mata:
        for j in d["jogos"]:
            if j.fase == f:
                for c in (j.mandante, j.visitante):
                    add(c, *linha_de.get(c, (None, "RSSSF (mata-mata)", f"eliminado: {f.lower()}")))
    for f in (UNICA, REBAIX, REGIONAL, GRUPOS):
        ts = [t for t in tabs if t.fase == f]
        ts = ts if f == GRUPOS else ts[-1:]   # duas tabelas da mesma fase (2002: a montada e a final divulgada): vale a última
        restantes = [(k, r) for t in ts for k, r in enumerate(t.linhas, 1)]
        for k, r in sorted(restantes, key=lambda x: (x[0] if f == GRUPOS else 0)):
            add(r["clube"], *linha_de[r["clube"]])
    pts = e.pontos
    for k, r in enumerate(linhas_c, 1):
        r["pos"] = k
        r["obs"] = re.sub(r"\s+", " ", re.sub(r"\[[\d\s\-:]+\]", "", r["obs"] or "")).strip(" ;")
        r["ajuste"] = (r["pts"] - (pts[0] * r["v"] + pts[1] * r["e"] + pts[2] * r["d"])) if pts and None not in (
            r["pts"], r["v"], r["e"], r["d"]) else None
    return linhas_c


def situacao(r: dict, d: dict) -> str:
    if r["clube"] == d["campeao"]:
        return "campeao"
    if r["clube"] == d["vice"]:
        return "vice"
    if re.search(r"relegat|rebaixad", r.get("obs", ""), re.I):
        return "rebaixado"
    return ""


def placar_oficial(j) -> tuple:
    obs = []
    gm, gv, esp = j.gm, j.gv, ""
    if j.especial in ("wo_m", "wo_v"):
        venc = j.mandante if j.especial == "wo_m" else j.visitante
        obs.append(f"pontos para o {venc} (decisão fora de campo)" + (f"; placar em campo {j.gm}-{j.gv}" if j.gm is not None else ""))
        gm = gv = None
        esp = "awd" if j.gm is not None else "wo"
    elif j.especial == "derrota_ambos":
        obs.append(f"derrota para os dois clubes (decisão fora de campo); placar em campo {j.gm}-{j.gv}")
        gm = gv = None
        esp = "awd"
    elif j.especial == "anulado":
        obs.append(f"jogo anulado ({j.gm}-{j.gv}) e jogado de novo")
        gm = gv = None
        esp = "n/p"
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


def _csv(arquivo: str, cab: list[str], linhas_: list[list]) -> None:
    with open(PACOTE / arquivo, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cab)
        w.writerows(linhas_)


def esperados(d: dict) -> int:
    n, com = 0, set()
    for t in d["usadas"]:
        if (t.fase, t.grupo) in com:
            continue
        com.add((t.fase, t.grupo))
        if not (d["e"].acumula and t.fase == REBAIX):
            n += sum(r["j"] for r in t.linhas) // 2
        else:
            n += sum(1 for j in d["jogos"] if j.fase == REBAIX)
    n += sum(1 for j in d["jogos"] if (j.fase, j.grupo) not in com)
    n += sum(1 for j in d["jogos"] if j.especial in ("anulado", "abd") and (j.fase, j.grupo) in com)
    return n if d["usadas"] else len(d["jogos"])


def formato(d: dict) -> str:
    e = d["e"]
    if not d["jogos"] and not d["tabelas"]:
        return "só o campeão (sem jogos nem tabela)"
    if not d["jogos"]:
        return "só a tabela final (sem jogos)" + (f"; {e.pontos[0]} pontos por vitória" if e.pontos else "")
    if not e.trechos:
        return "só o campeão (sem jogos nem tabela)"
    desc = {UNICA: "pontos corridos", LIGA: "fase regular", TITULO: "grupo do título", REBAIX: "grupo do rebaixamento",
            GRUPOS: "fase de grupos"}
    partes = []
    for f in d["fases"]:
        n = len({r["clube"] for t in d["tabelas"] if t.fase == f for r in t.linhas})
        partes.append(desc[f] + (f" ({n} clubes)" if n and f in FASES_LIGA else ""))
    txt = " + ".join(partes)
    if e.pontos:
        txt += f"; {e.pontos[0]} pontos por vitória, {e.pontos[1]} por empate e {e.pontos[2]} por derrota"
    return f"jogos incompletos: {txt}" if e.incompleta else txt


def gravar(eds: list[dict]) -> None:
    PACOTE.mkdir(parents=True, exist_ok=True)
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    ed_l, fa_l, pa_l, go_l, cl_l, tp_l, co_l = [], [], [], [], [], [], []
    for d in eds:
        e = d["e"]
        jogos = d["jogos"]
        if d["campeao"]:
            nomes_fonte[d["campeao"]][f"rsssf:{d['rsssf_campeao']}"].append(e.ano_inicio)
        for j in jogos:
            nomes_fonte[j.mandante][f"rsssf:{j.nome_m}"].append(e.ano_inicio)
            nomes_fonte[j.visitante][f"rsssf:{j.nome_v}"].append(e.ano_inicio)
        for t in d["tabelas"]:
            for r in t.linhas:
                nomes_fonte[r["clube"]][f"rsssf:{r['nome']}"].append(e.ano_inicio)
        for (a, b), xs in ogol_jogos(e).items():
            for x in xs:
                nomes_fonte[a][f"ogol:{x['mandante']}"].append(e.ano_inicio)
                nomes_fonte[b][f"ogol:{x['visitante']}"].append(e.ano_inicio)
        n_gols = n_autor = 0
        for n, j in enumerate(jogos, 1):
            pid = f"{tid(e.temporada)}-{n:04d}"
            gm, gv, esp, obs = placar_oficial(j)
            if j.nota and not re.fullmatch(r"\s*(at |aet|\d)", j.nota) and not esp:
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
            fid = f"rsssf:{j.pagina}:{j.linha}" if j.origem != "lista" else "rsssf:newcalchamp" + (f"|ogol:{j.ogol_id}" if getattr(j, "ogol_id", None) else "")
            pa_l.append([pid, e.temporada, j.fase, j.grupo, j.rodada or "", j.data or "", "", j.mandante, j.visitante,
                         "" if gm is None else gm, "" if gv is None else gv, "" if j.pen_m is None else j.pen_m,
                         "" if j.pen_v is None else j.pen_v, esp, j.local or "", "", "", "RSSSF", fid,
                         j.gols_texto if j.gols_texto and not sep else "", "; ".join(obs)])
        d["n_gols"], d["n_autor"] = n_gols, n_autor
        for k, f in enumerate(d["fases"], 1):
            js = [j for j in jogos if j.fase == f]
            pares = Counter(frozenset((j.mandante, j.visitante)) for j in js)
            tipo = "liga" if f in FASES_LIGA else "mata_mata"
            serie = "pontos_corridos" if tipo == "liga" else ("ida_volta" if pares and max(pares.values()) > 1 else "jogo_unico")
            fa_l.append([e.temporada, k, f, tipo, "", serie, CRITERIO.get(f, "")])
        cls = classificacao(d)
        d["cls"] = cls
        for r in cls:
            cl_l.append([e.temporada, r["pos"], r["clube"], "" if r["j"] is None else r["j"], "" if r["v"] is None else r["v"],
                         "" if r["e"] is None else r["e"], "" if r["d"] is None else r["d"], "" if r["gp"] is None else r["gp"],
                         "" if r["gc"] is None else r["gc"], "" if r["pts"] is None else r["pts"], r["ajuste"] or "",
                         situacao(r, d), r["fonte"], r["obs"]])
        for t in d["tabelas"]:
            for k, r in enumerate(t.linhas, 1):
                tp_l.append([e.temporada, t.fase, t.grupo, r["pos"] or k, r["nome"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"],
                             r["gc"], r["pts"], f"RSSSF ({t.pagina}, linha {t.linha})"])
        clubes_ed = {j.mandante for j in jogos} | {j.visitante for j in jogos} | {r["clube"] for r in cls}
        obs = [x for x in (e.obs, e.incompleta) if x]
        ed_l.append([e.temporada, e.ano_inicio, e.ano_fim, e.nome_oficial, len(clubes_ed), e.pontos[0] if e.pontos else "",
                     *((e.pontos[1], e.pontos[2]) if e.pontos and e.pontos[1:] != (1, 0) else ("", "")), formato(d),
                     d["campeao"] or "", d["vice"] or "", "RSSSF" + (" + ogol" if any(getattr(j, "ogol_id", None) for j in jogos) else ""),
                     "; ".join(obs)])
        ndif = len({id(t) for t, *_ in d["difs"]})
        wc = d["wiki_campeao"]
        ob = [f"campeão {d['campeao']} (RSSSF: {d['rsssf_campeao']}; Wikipédia: {wc or 'sem a informação'})"]
        if wc and wc != d["campeao"]:
            ob.append(f"a Wikipédia dá {wc} (copia uma versão antiga da lista da RSSSF; vale a RSSSF, decisão do "
                      "Guilherme em 24/11/2026)")
        if ndif:
            ob.append(EXPLICACOES.get(e.temporada, "divergência sem explicação"))
        if e.incompleta:
            ob.append(e.incompleta)
        co_l.append([e.temporada, len(jogos), esperados(d), len(d["usadas"]), ndif, n_gols, n_autor, "; ".join(ob)])
    _csv("edicoes.csv", ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "pontos_empate",
                         "pontos_derrota", "formato", "campeao", "vice",
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
        cidade, provincia = CLUBES[c]
        nf = []
        for k, anos in sorted(nomes_fonte[c].items()):
            a = sorted(set(anos))
            nf.append(f"{k}:{a[0]}" + (f"-{a[-1]}" if a[-1] != a[0] else ""))
        clubes_l.append([c, provincia, cidade, "FIJ", "|".join(nf)])
    _csv("clubes.csv", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], clubes_l)
    comp = {"slug": SLUG, "nome": "Campeonato Fijiano", "nome_curto": "Fijiano", "tipo": "liga", "nivel": 1, "pais": "FIJ",
            "pais_nome": "Fiji", "regiao": None, "confederacao": "OFC", "rotulo_painel": "Fijiano",
            "menu_painel": "Fiji · 1ª divisão", "do_painel": "do Campeonato Fijiano", "o_painel": "o Campeonato Fijiano",
            "observacao": "1ª divisão de Fiji de 1977 a 2026: a liga das associações dos distritos (National Football League, "
                          "hoje Fiji Premier League), uma edição por ano, como na lista de campeões da RSSSF. Até 1997 quase só o "
                          "campeão ou a tabela final; jogos de 1998 em diante (parte deles até 2004; 2011 e 2012 só a tabela). "
                          "Seleções de base de Fiji jogaram a liga em vários anos (Fiji Olympians, Fiji U-20)."}
    (PACOTE / "competicao.json").write_text(json.dumps(comp, ensure_ascii=False, indent=1), encoding="utf-8")


def relatorio(eds: list[dict]) -> None:
    import explicacoes as ex
    tot_j = sum(len(d["jogos"]) for d in eds)
    out = [f"# Coleta: Campeonato Fijiano (`{SLUG}`)", "", "Gerado por `python coleta/fij-1/importar.py`. Pacote em `data/coleta/fij-1/pacote/`.",
           "", "## Resumo", "",
           f"- {len(eds)} edições (1977 a 2026), {sum(1 for d in eds if d['jogos'])} com jogos; {tot_j} jogos, "
           f"{sum(d['n_gols'] for d in eds)} gols, {sum(d['n_autor'] for d in eds)} com autor.",
           "- Escopo aprovado pelo Guilherme em 24/11/2026, depois de pesquisa a fundo (docstrings de `coleta/fij-1/edicoes.py` e "
           "`coleta/fij-1/clubes_fij.py`):",
           "  - a 1ª divisão é a liga dos distritos (desde 1977); ficam de fora o Inter-District Championship, o National Club "
           "Championship, a Club Franchise League (2004/05-2006), as copas, a 2ª divisão e as repescagens;",
           "  - 2003 = Ba (os Olympians, 1º na tabela, ganharam um jogo no tribunal; o Ba recorreu à justiça, a final de desempate "
           "nunca foi jogada e a federação deu o título ao Ba em 2006); 2010 = Ba (o título dado ao Lautoka no tribunal foi "
           "revogado);",
           "  - nomes: o distrito puro, salvo \"Ba FC\"; seleções de base: \"Fiji Olympians\", \"Fiji U-20\" (2010) e \"Fiji Youth "
           "Teams\" (2011).",
           "- Pontuação: 2 por vitória até 1986, 3 a partir de 1988.", "",
           "## Fontes", "",
           "- **RSSSF** (`data/coleta/fij-1/rsssf/`, `baixar_rsssf.py`): lista de campeões e páginas por ano (1977-1989, 1992-1994, "
           "1997-2026).",
           "- **Wikipédia em inglês** (`data/coleta/fij-1/wikipedia/`, `baixar_wikipedia.py`): segunda fonte do campeão (bate com a "
           "RSSSF em todos os anos).",
           "- **ogol** (`data/coleta/fij-1/ogol/`, cache em `data/cache/ogol-fij-1/`, `baixar_ogol.py`): os jogos de 2011 (fecham com a "
           "tabela da RSSSF) e a grafia dos times para os escudos.", "",
           "## Correções e decisões", ""]
    for k, (a, b, m) in ex.CONSERTA_TEXTO.items():
        out.append(f"- `{k[0]}`, linha {k[1]}: \"{a}\" -> \"{b}\": {m}.")
    for k, v in ex.CORRIGE.items():
        out.append(f"- `{' / '.join(str(x) for x in k)}`: " + (f"{v[1]}." if v else "descartado (adversário incerto na página)."))
    for k, v in ex.TABELAS_FORA.items():
        out.append(f"- tabela `{k[0]}`, linha {k[1]}, fora da conferência: {v}.")
    out.append("- 2000: os 8 jogos do sub-20 (\"Under 20\") foram anulados e ficam de fora, como na tabela da página.")
    out += ["", "## Divergências que ficam", ""]
    for t, v in ex.EXPLICACOES.items():
        out.append(f"- **{t}:** {v}.")
    out += ["", "## Edição a edição", "",
            "| Ano | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Observação |", "|---|---|---|---|---|---|---|---|---|"]
    for d in eds:
        e = d["e"]
        obs = [x for x in (e.obs, e.incompleta) if x]
        if d["wiki_campeao"] and d["wiki_campeao"] != d["campeao"]:
            obs.append(f"Wikipédia: {d['wiki_campeao']}")
        out.append(f"| {e.temporada} | {formato(d)} | {len(d['jogos'])} | {esperados(d) if d['jogos'] else 0} | {d['n_gols']} | "
                   f"{d['n_autor']} | {d['campeao']} | {d['vice'] or ''} | {'; '.join(obs)} |")
    out += ["", "## O que não deu para coletar", "",
            "- 1977-1982, 1987, 1989-1993, 1995 e 1996: só o campeão (e o vice em poucos anos); 1983-1988, 1994 e 1997 só a tabela.",
            "- 1998-2004 com parte dos jogos; 2012 só a tabela (o calendário do ogol não fecha com ela).",
            "- Hora, estádio, público, cartões e artilheiros.", ""]
    RELATORIO.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    cps, wcp = campeoes(), wiki_campeoes()
    eds = [montar(e, cps, wcp) for e in EDICOES]
    gravar(eds)
    relatorio(eds)
    for d in eds:
        aviso = f" ATENÇÃO Wikipédia: {d['wiki_campeao']}" if d["wiki_campeao"] and d["wiki_campeao"] != d["campeao"] else ""
        print(f"{d['e'].temporada}: {len(d['jogos'])} jogos ({esperados(d)} esperados), {d['n_autor']}/{d['n_gols']} com autor, "
              f"campeão {d['campeao']}, vice {d['vice']}, 1º {d['cls'][0]['clube'] if d['cls'] else '-'}{aviso}")


if __name__ == "__main__":
    main()
