"""Junta as fontes da 1ª divisão do Taiti e grava o pacote em data/coleta/tah-1/pacote/ e o relatório em docs/coleta/tah-1.md.

Fontes:
- RSSSF (ler.py): lista de campeões (tahitichamp.html: campeão de 1948 a 2025/26 e o vice em 8 anos) e as páginas por
  temporada (jogos, fases, datas, rodadas, autores dos gols; tabelas para a conferência e a classificação);
- Wikipédia em inglês (data/coleta/tah-1/wikipedia/liga.wiki): segunda fonte do campeão;
- ogol (data/coleta/tah-1/ogol/): data dos jogos da RSSSF sem data e a grafia dos clubes para os escudos.

Uso: python coleta/tah-1/importar.py
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
import rsssf_oce  # noqa: E402
from clubes_tah import CLUBES, clube  # noqa: E402
from edicoes import EDICOES, FINAL, LIGA, PACOTE, PASTA_DADOS, REBAIX, RELATORIO, SEMI, SLUG, TITULO, UNICA, Edicao  # noqa: E402
from explicacoes import EXPLICACOES  # noqa: E402
from ler import campeoes, linhas  # noqa: E402

FASES_LIGA = (UNICA, LIGA, TITULO, REBAIX)
CRITERIO = {
    TITULO: "os primeiros da fase regular (e, em parte dos anos, o campeão de Mooréa); o 1º é o campeão. Bônus de 2 pontos ao "
            "vencedor da fase regular",
    REBAIX: "os últimos da fase regular; os de baixo caem",
    SEMI: "os 4 primeiros da fase regular", FINAL: "decide o título",
}
VICE_PIRAE = {1990, 1992, 1995, 1996, 1997, 1998, 1999, 2000}   # "[*] in each of the (8) years ... AS Pirae were runners-up"


# classificação lida à mão (a tabela da página não tem os gols e o leitor comum não a lê)
MANUAL = {"2004/05": ("RSSSF (tahiti05, linhas 70 e 109: tabelas só com pontos)", [
    ("AS Tefana", 6, 3, 3, 0, 18, "campanha no playoff do título"),
    ("AS Pirae", 6, 2, 2, 2, 16, "campanha no playoff do título; 2 pontos de bônus como 1º da fase regular"),
    ("AS Manu-Ura", 5, 2, 3, 0, 14, "campanha no playoff do título (um jogo a menos na página)"),
    ("Central Sport", 5, 0, 0, 5, 5, "campanha no playoff do título (um jogo a menos na página)"),
    ("AS Tamarii Faa'a", 5, 4, 1, 0, 18, "campanha no grupo do rebaixamento"),
    ("AS Dragon", 5, 3, 0, 2, 14, "campanha no grupo do rebaixamento"),
    ("AS Vénus", 5, 2, 1, 2, 13, "campanha no grupo do rebaixamento; 1 ponto de bônus; rebaixado (o 1º rebaixamento da história)"),
    ("AS Vairao", 5, 0, 0, 5, 5, "campanha no grupo do rebaixamento; rebaixado")])}


def tid(t: str) -> str:
    return t.replace("/", "-")


def wiki_campeoes() -> dict[int, str]:
    txt = (PASTA_DADOS / "wikipedia" / "liga.wiki").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^\*\[?\[?(?:[^|\]]*\|)?(\d{4})(?:–(\d{2}))?\]?\]?:\s*(.*)$", txt, re.M):
        ano = int(m.group(1)) + (1 if m.group(2) else 0)
        nome = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", m.group(3))
        nome = re.sub(r"\s*\(.*$|<ref.*$", "", nome).strip()
        if nome:
            out[ano] = clube(nome, ano)
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


def ranking_1968() -> list[str]:
    """1968: a página traz só a ordem final ("1.Fei-Pi   (best attack with 39 goals)")."""
    out = []
    for l in linhas("tahiti68")[30:40]:
        m = re.match(r"^\s*\d\.(\S[^(]*?)\s*(\(|$)", l)
        if m:
            out.append(clube(m.group(1), 1968))
    return out


def montar(e: Edicao, cps: dict, wcp: dict) -> dict:
    ano_lista = e.ano_fim
    campeao = clube(cps[ano_lista], e.ano_inicio)
    vice = "AS Pirae" if ano_lista in VICE_PIRAE else ranking_1968()[1] if e.temporada == "1968" else None
    d = {"e": e, "jogos": [], "usadas": [], "tabelas": [], "difs": [], "fases": [], "campeao": campeao, "vice": vice,
         "rsssf_campeao": cps[ano_lista], "wiki_campeao": wcp.get(ano_lista)}
    if not e.trechos:
        return d
    jogos, usadas, difs, falta = conf.conferir(e)
    assert not falta, f"{e.temporada}: nomes sem clube {falta}"
    d.update(jogos=jogos, usadas=usadas, difs=difs, tabelas=conf.TODAS[e.temporada],
             fases=list(dict.fromkeys(f for _, _, _, f, _ in e.trechos if any(j.fase == f for j in jogos) or
                                      any(t.fase == f for t in conf.TODAS[e.temporada]))))
    og = ogol_jogos(e)
    for j in jogos:   # data do ogol para jogo sem data (mesmo mando e placar)
        c = [x for x in og.get((j.mandante, j.visitante), []) if (x["gols_mandante"], x["gols_visitante"]) == (j.gm, j.gv)]
        if len(c) == 1:
            j.ogol_id = c[0]["id"]
            j.data = j.data or c[0]["data"]
    if not vice and e.temporada in MANUAL:
        vice = d["vice"] = MANUAL[e.temporada][1][1][0]
    if not vice:   # vice: o 2º do playoff do título, ou o perdedor da final, ou o 2º da tabela da fase única
        fin = [j for j in jogos if j.fase == FINAL]
        if fin:
            vice = fin[-1].visitante if fin[-1].mandante == campeao else fin[-1].mandante
        else:
            for f in (TITULO, UNICA, LIGA):
                t = [t for t in d["tabelas"] if t.fase == f and t.linhas]
                if t and len(t[-1].linhas) > 1:
                    cand = [r["clube"] for r in t[-1].linhas if r["clube"] != campeao]
                    vice = cand[0] if not ("parte dos jogos" in e.incompleta and f == UNICA and len(t[-1].linhas) < 6) else None
                    break
        d["vice"] = vice
    return d


def _junta(tabs: list) -> list:
    """Tabela cortada em duas pela linha de rebaixamento: as partes seguidas da mesma fase viram uma."""
    out = []
    for t in tabs:
        if out and out[-1].fase == t.fase and out[-1].pagina == t.pagina and t.linhas and t.linhas[0]["pos"] and \
                out[-1].linhas[-1]["pos"] and t.linhas[0]["pos"] == out[-1].linhas[-1]["pos"] + 1:
            out[-1].linhas = out[-1].linhas + t.linhas
        else:
            out.append(t)
    return out


def classificacao(d: dict) -> list[dict]:
    """Playoff do título (ordem oficial), depois o grupo do rebaixamento, depois os demais pela fase regular. Campeão em 1º e
    vice em 2º. Edição só com o campeão: campeão (e vice)."""
    e = d["e"]
    linhas_c: list[dict] = []
    tabs = _junta([t for t in d["tabelas"] if t.linhas])
    vistos = set()
    for f in (TITULO, REBAIX, UNICA, LIGA):
        for t in [t for t in tabs if t.fase == f][-1:]:
            for r in t.linhas:
                if r["clube"] in vistos:
                    continue
                vistos.add(r["clube"])
                linhas_c.append({"clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                                 "pts": r["pts"], "obs": (f"campanha na {f.lower()}" if f != UNICA else "") +
                                 (f"; {r['obs']}" if r["obs"] else ""), "fonte": f"RSSSF ({t.pagina}, linha {t.linha})"})
    if e.temporada in MANUAL:   # tabela só com jogos, vitórias, empates, derrotas e pontos (sem os gols)
        linhas_c = [{"clube": c, "j": j_, "v": v, "e": e_, "d": d_, "gp": None, "gc": None, "pts": p, "obs": o,
                     "fonte": MANUAL[e.temporada][0]} for c, j_, v, e_, d_, p, o in MANUAL[e.temporada][1]]
    if e.temporada == "1968":
        linhas_c = [{"clube": c, "j": None, "v": None, "e": None, "d": None, "gp": None, "gc": None, "pts": None, "obs": "",
                     "fonte": "RSSSF (tahiti68: classificação sem números)"} for c in ranking_1968()]
    for alvo in (d["campeao"], d["vice"]):
        if alvo and not any(r["clube"] == alvo for r in linhas_c):
            linhas_c.append({"clube": alvo, "j": None, "v": None, "e": None, "d": None, "gp": None, "gc": None, "pts": None, "obs": "",
                             "fonte": "lista de campeões da RSSSF"})
    for alvo, k in ((d["campeao"], 0), (d["vice"], 1)):
        if alvo and linhas_c[k]["clube"] != alvo:
            r = next(r for r in linhas_c if r["clube"] == alvo)
            linhas_c.remove(r)
            linhas_c.insert(k, r)
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
        if t.fase in com:
            continue
        com.add(t.fase)
        n += sum(r["j"] for r in t.linhas) // 2
        if d["e"].acumula and t.fase != d["e"].trechos[0][3]:
            n -= sum(r["j"] for r in t.linhas) // 2   # (tabela acumulada: conta só pela fase regular)
    n += sum(1 for j in d["jogos"] if j.fase not in com)
    n += sum(1 for j in d["jogos"] if j.especial in ("anulado", "abd") and j.fase in com)
    return n if d["usadas"] else len(d["jogos"])


def formato(d: dict) -> str:
    e = d["e"]
    if not e.trechos:
        return "só o campeão (sem jogos nem tabela)"
    desc = {UNICA: "pontos corridos", LIGA: "fase regular", TITULO: "playoff do título", REBAIX: "grupo do rebaixamento",
            SEMI: "semifinais", FINAL: "final"}
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
    cps = campeoes()
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
            fid = f"rsssf:{j.pagina}:{j.linha}" + (f"|ogol:{j.ogol_id}" if getattr(j, "ogol_id", None) else "")
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
            ob.append(f"ATENÇÃO: a Wikipédia dá {wc} (copia uma versão antiga da lista da RSSSF; vale a RSSSF, decisão do "
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
        cidade, ilha = CLUBES[c]
        nf = []
        for k, anos in sorted(nomes_fonte[c].items()):
            a = sorted(set(anos))
            nf.append(f"{k}:{a[0]}" + (f"-{a[-1]}" if a[-1] != a[0] else ""))
        clubes_l.append([c, ilha, cidade, "TAH", "|".join(nf)])
    _csv("clubes.csv", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], clubes_l)
    comp = {"slug": SLUG, "nome": "Campeonato Taitiano", "nome_curto": "Taitiano", "tipo": "liga", "nivel": 1, "pais": "TAH",
            "pais_nome": "Taiti", "regiao": None, "confederacao": "OFC", "rotulo_painel": "Taitiano", "menu_painel": "Taiti · 1ª divisão",
            "do_painel": "do Campeonato Taitiano", "o_painel": "o Campeonato Taitiano",
            "observacao": "1ª divisão do Taiti (Polinésia Francesa) de 1948 a 2025/26, uma edição por título, como na lista de "
                          "campeões da RSSSF: Division d'Honneur, Division Fédérale (2003/04) e Ligue 1 (2008/09). A maioria das "
                          "edições até 1998 tem só o campeão; jogos em 1968 (parte), 1969-1971 e de 1998/99 em diante (parte até "
                          "2004/05; 2011/12 só com as tabelas). Pontuação de 4 pontos por vitória, 2 por empate e 1 por derrota na "
                          "maior parte dos anos recentes; a classificação traz os pontos oficiais."}
    (PACOTE / "competicao.json").write_text(json.dumps(comp, ensure_ascii=False, indent=1), encoding="utf-8")


def relatorio(eds: list[dict]) -> None:
    import explicacoes as ex
    tot_j = sum(len(d["jogos"]) for d in eds)
    out = [f"# Coleta: Campeonato Taitiano (`{SLUG}`)", "", "Gerado por `python coleta/tah-1/importar.py`. Pacote em `data/coleta/tah-1/pacote/`.",
           "", "## Resumo", "",
           f"- {len(eds)} edições (1948 a 2025/26), {sum(1 for d in eds if d['jogos'])} com jogos; {tot_j} jogos, "
           f"{sum(d['n_gols'] for d in eds)} gols, {sum(d['n_autor'] for d in eds)} com autor.",
           "- Escopo aprovado pelo Guilherme em 24/11/2026 (docstring de `coleta/tah-1/edicoes.py`): desde 1948, até 2025/26, "
           "\"2025/26\" nas temporadas que cruzam o ano, nomes com \"AS\", em 1956, 1957 e 1961 vale a RSSSF.",
           "- Pontuação: 4-2-1 (vitória, empate, derrota) na maior parte dos anos recentes, 3-2-1 em 1969-1971 e 2007/08, 3-1-0 de "
           "1998/99 a 2002/03. A classificação traz os pontos oficiais; `ajuste_pontos` = bônus e punições.",
           "- Classificação final: playoff do título, grupo do rebaixamento e o resto pela fase regular; campeão e vice no topo.", "",
           "## Fontes", "",
           "- **RSSSF** (`data/coleta/tah-1/rsssf/`, `baixar_rsssf.py`): lista de campeões e páginas por temporada (1968-1971, 1985, "
           "1998/99 em diante).",
           "- **Wikipédia em inglês** (`data/coleta/tah-1/wikipedia/`, `baixar_wikipedia.py`): segunda fonte do campeão (lista da "
           "página \"Tahiti Ligue 1\", que copia uma versão antiga da RSSSF).",
           "- **ogol** (`data/coleta/tah-1/ogol/`, cache em `data/cache/ogol-tah-1/`, `baixar_ogol.py`): jogos de 2012/13 e 2013/14 "
           "(playoff), 2021/22 e 2023/24; nas outras edições só o campeão.", "",
           "## Correções e decisões", ""]
    for k, (a, b, m) in ex.CONSERTA_TEXTO.items():
        out.append(f"- `{k[0]}`, linha {k[1]}: \"{a}\" -> \"{b}\": {m}.")
    for k, v in ex.CORRIGE.items():
        if v is not None:
            out.append(f"- `{' / '.join(str(x) for x in k)}`: {v[1]}.")
    out += ["- Jogos anulados e repetidos: a página lista os dois; o anulado entra como não disputado (`n/p`), com o placar na "
            "observação.", "", "## Edição a edição", "",
            "| Temporada | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Observação |", "|---|---|---|---|---|---|---|---|---|"]
    for d in eds:
        e = d["e"]
        obs = [x for x in (e.obs, e.incompleta) if x]
        if d["wiki_campeao"] and d["wiki_campeao"] != d["campeao"]:
            obs.append(f"Wikipédia: {d['wiki_campeao']}")
        out.append(f"| {e.temporada} | {formato(d)} | {len(d['jogos'])} | {esperados(d) if d['jogos'] else 0} | {d['n_gols']} | "
                   f"{d['n_autor']} | {d['campeao']} | {d['vice'] or ''} | {'; '.join(obs)} |")
    out += ["", "## O que não deu para coletar", "",
            "- Jogos e tabelas de 1948-1967, 1972-1998 (só o campeão; o vice em 8 anos): nenhuma fonte aberta.",
            "- Jogos de 1998/99 a 2004/05 só em parte (muitos só com \"venceu\"/\"perdeu\"), de 2010/11 (playoff) e de 2011/12.",
            "- Hora, estádio, público, cartões e artilheiros.", ""]
    RELATORIO.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    cps, wcp = campeoes(), wiki_campeoes()
    eds = [montar(e, cps, wcp) for e in EDICOES]
    gravar(eds)
    relatorio(eds)
    for d in eds:
        if not d["jogos"] and not d["wiki_campeao"] == d["campeao"]:
            print(f"{d['e'].temporada}: campeão {d['campeao']} (Wikipédia: {d['wiki_campeao']})")
        elif d["jogos"]:
            print(f"{d['e'].temporada}: {len(d['jogos'])} jogos ({esperados(d)} esperados), {d['n_autor']}/{d['n_gols']} com autor, "
                  f"campeão {d['campeao']}, vice {d['vice']}, 1º da classificação {d['cls'][0]['clube']}")


if __name__ == "__main__":
    main()
