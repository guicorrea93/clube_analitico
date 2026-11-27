"""Monta o pacote do campeonato cipriota (cyp-1), 1934/35 a 2025/26, e o relatório docs/coleta/cyp-1.md.

Bases de jogos:
- até 1995/96: a matriz de resultados da Wikipédia (en) de cada temporada, sem data nem rodada (algumas temporadas antigas
  têm a matriz incompleta);
- de 1996/97 em diante: o calendário do ogol (data, hora e rodada), o clube pelo código do ogol; a fase regular é o
  primeiro encontro de cada par; grupos (título, intermediário e rebaixamento) pelas tabelas da Wikipédia.
Tabelas publicadas: Wikipédia (ordem oficial, punições) e RSSSF (a página de cada temporada, casada pelos números).
Campeões: RSSSF (cypchamp.html); artilheiros: RSSSF (cyptops.html). Sem football-data e sem ESPN para Chipre (sem autores
dos gols e cartões).

Pontos: 2-1-0 até 1990/91, 3-1-0 depois.

Escopo (Guilherme, 27/11/2026): ver coleta/cyp-1/edicoes.py.

Uso: python coleta/cyp-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
sys.path.append(str(AQUI.parent / "gre-1"))   # fichas e seções da Wikipédia, no fim da busca
sys.path.append(str(AQUI.parent / "cze-1"))   # leitor das páginas de temporada da RSSSF (mesmo formato)
import clubes_cyp as clubes  # noqa: E402
import notas_wiki  # noqa: E402
import rsssf_cze as rsssf  # noqa: E402
import wiki_gre  # noqa: E402
from edicoes import DADOS, OGOL_DESDE, RAIZ, TEMPORADAS, ano_fim, ano_inicio, nome_oficial, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from wiki_tabela import _fecha, _num, limpar  # noqa: E402
from wiki_tabela import resultados as wiki_resultados  # noqa: E402
from wiki_tabela import tabelas as wiki_tabelas  # noqa: E402

PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "cyp-1.md"
OSLO = ZoneInfo("Asia/Nicosia")
LONDRES = ZoneInfo("Europe/London")
DOIS, TRES = (2, 1, 0), (3, 1, 0)
PENALTIS: set = set()

ORDEM_FASES = {"Liga": 0, "Fase regular": 0, "Grupo do título": 4, "Grupo intermediário": 5,
               "Grupo de rebaixamento": 6, "Desempate": 7, "Quartas de final": 7, "Semifinal": 8, "Final": 9, "Desempate da final": 10,
               "Play-off europeu": 11, "Play-off de rebaixamento": 12}
# jogo do ogol com data ou placar errados, pelo código: id -> (data, gols, gols, motivo)
CORRIGE_OGOL: dict[str, tuple] = {}
COMPLETA_FD: set = set()
DECIDIDOS: dict[tuple, tuple] = {}
NAO_REBAIXADOS: dict[tuple, str] = {}
EXPLICACOES: dict[str, list[str]] = {}
# derrota para os dois: temporada -> [(mandante, visitante, fase, motivo)]
DERROTA_DOIS = {"2008/09": [("APOEL", "Omonia", "Grupo do título",
                             "jogo da última rodada suspenso no intervalo pela violência das duas torcidas; a tabela da "
                             "Wikipédia dá uma derrota a cada um, sem gols")]}

COMPETICAO = {
    "slug": "cyp-1", "nome": "Campeonato Cipriota", "nome_curto": "Cipriota", "tipo": "liga", "nivel": 1,
    "pais": "CYP", "pais_nome": "Chipre", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Cipriota", "menu_painel": "Chipre · 1ª divisão",
    "do_painel": "do Campeonato Cipriota", "o_painel": "o Campeonato Cipriota",
    "observacao": "Os 86 títulos que a federação (CFA) reconhece, desde 1934/35 (A' Katigoria). Não inclui os campeonatos "
                  "não oficiais de 1931/32 a 1933/34 nem as temporadas sem campeão (1941/42 a 1943/44, 1958/59, 1963/64 e "
                  "2019/20). De 1967/68 a 1973/74, o campeão também jogou o Campeonato Grego (competição gre-1).",
}


def faixa(rotulos) -> str:
    a = sorted(rotulos, key=TEMPORADAS_ORDEM.get)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else a[0]


TEMPORADAS_ORDEM = {t: i for i, t in enumerate(TEMPORADAS + ["2026/27"])}  # noqa: E501


def pontos(t: str) -> tuple[int, int, int]:
    if 1960 <= ano_inicio(t) <= 1969:   # 3-2-1, como a Grécia (RSSSF); a Wikipédia calcula com 2-1-0
        return (3, 2, 1)
    return DOIS if ano_inicio(t) < 1991 else TRES


def minuto(s: str | None) -> tuple[int | None, int | None]:
    m = re.match(r"^(\d+)'?(?:\+(\d+)'?)?", s or "")
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else (None, None)


def _normal(s: str) -> str:
    s = s.replace("ø", "o").replace("Ø", "O").replace("æ", "ae").replace("å", "a").replace("Å", "A")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]", " ", unicodedata.normalize("NFKD", s).encode("ascii", "ignore")
                                       .decode().lower())).strip()


# ------------------------------------------------------------------ fontes
def texto_wiki(t: str) -> str:
    return "\n".join(x.read_text(encoding="utf-8") for x in sorted((DADOS / "wikipedia").glob(f"{wiki_titulo(t)}*.wiki")))


def url_wiki(t: str) -> str:
    return f"https://en.wikipedia.org/wiki/{wiki_titulo(t).replace(' ', '_')}"


def ler_wiki(t: str) -> dict:
    """Tabelas (clube pelo link) e matrizes (blocos) e o texto; {{nowrap|...}} desembrulhado (2016/17)."""
    txt = re.sub(r"\{\{\s*nowrap\s*\|(.*?)\}\}", r"\1", texto_wiki(t), flags=re.I)
    cod, vis = {}, {}
    for c, alvo, nome in re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", txt):
        cod.setdefault(c, alvo.strip())
        vis.setdefault((nome or alvo).strip(), alvo.strip())

    def ident(alvo: str | None, nome: str) -> str:
        c = clubes.link(alvo) if alvo else None
        c = c or clubes.link(vis.get((nome or "").strip())) or getattr(clubes, "VISIVEIS", {}).get((nome or "").strip())
        if c is None:
            raise SystemExit(f"{t}: clube da Wikipédia sem cadastro: {nome} ({alvo})")
        return c

    caminho = wiki_gre.secao_em(txt)
    tbs = []
    for tb in wiki_tabelas(txt):
        for x in tb["times"]:
            m = re.match(r"\s*\[\[([^\]|]+)", x["nome_wiki"])
            x["clube"] = ident(m.group(1) if m else cod.get(x["codigo"]), x["nome"])
            x["ativo"] = x["vitorias"] is not None
            pw, pl_ = _num(tb["params"].get(f"PKwin_{x['codigo']}")), _num(tb["params"].get(f"PKloss_{x['codigo']}"))
            x["bonus"] = pw or 0   # o ponto a mais do vencedor nos pênaltis
            x["pk"] = (pw, pl_) if pw is not None or pl_ is not None else None
            if x["pk"]:
                x["empates"] = (x["empates"] or 0) + (pw or 0) + (pl_ or 0)
        tb["ativos"] = [x for x in tb["times"] if x["ativo"]]
        tb["caminho"] = caminho(tb["inicio"])
        tbs.append(tb)
    tbl_cod = {x["codigo"]: x["clube"] for tb in tbs for x in tb["times"]}
    blocos = []
    tm = re.sub(r"(?i)#invoke:\s*sports table", "#invoke:sports results", txt)
    for mm in re.finditer(r"\{\{\s*#invoke:\s*sports results\s*\|", tm, flags=re.I):
        bloco = tm[mm.start():_fecha(tm, mm.start())]
        pens = {(a, b): (int(p), int(q)) for a, b, p, q in
                re.findall(r"\|\s*match_([^_|=\s]+)_([^_|=\s]+)\s*=[^\n]*?<sup>\s*\(?\s*(\d+)\s*[–-]\s*(\d+)", bloco)}
        limpo = re.sub(r"<sup>.*?</sup>", "", bloco, flags=re.S)
        limpo = re.sub(r"\{\{\s*(?:efn|refn|sfn|note|cref|ref label|abbr)[^{}]*\}\}", "", limpo, flags=re.I)
        rr = wiki_resultados(limpo)
        if not rr:
            continue
        g = rr[0]
        alvos = dict(re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)", bloco))
        notas = {(a, b): re.split(r"\|\s*[\w ]+=", v)[0].strip()
                 for a, b, v in re.findall(r"\|\s*match_([^_|=\s]+)_([^_|=\s]+)_note\s*=([^\n]*)", bloco)}
        jogos = []
        for (a, b), pl in g["jogos"].items():
            # o código da tabela vale para a matriz do mesmo artigo (1976: a matriz liga o Randers Freja ao Randers FC)
            ma = tbl_cod.get(a) or ident(alvos.get(a) or cod.get(a), g["nomes"].get(a, a))
            mb = tbl_cod.get(b) or ident(alvos.get(b) or cod.get(b), g["nomes"].get(b, b))
            for gm, gv in pl:
                n = notas.get((a, b), "")
                k = tuple(n.split("_"))
                if len(k) == 2 and k in notas:
                    n = notas[k]
                jogos.append({"m": ma, "v": mb, "nm": g["nomes"].get(a, a), "nv": g["nomes"].get(b, b), "gm": gm, "gv": gv,
                              "pen": pens.get((a, b)), "nota": limpar(n) or None})
        blocos.append({"clubes": {c for j in jogos for c in (j["m"], j["v"])}, "jogos": jogos,
                       "caminho": caminho(mm.start())})
    return {"tbs": tbs, "blocos": blocos, "texto": txt, "ident": ident, "caminho": caminho}


def carregar_ogol(t: str) -> list[dict]:
    res = []
    for o in json.loads((DADOS / "ogol" / f"cyp1_{t.replace('/', '-')}.json").read_text(encoding="utf-8")):
        if o["resultado"] in ("ADI", "ANU"):
            continue
        m = clubes.ogol(o["mandante_id"], t) or clubes.esd(o["mandante"])
        v = clubes.ogol(o["visitante_id"], t) or clubes.esd(o["visitante"])
        if m is None or v is None:
            raise SystemExit(f"{t}: clube do ogol sem cadastro: {o['mandante']} ({o['mandante_id']}) x "
                             f"{o['visitante']} ({o['visitante_id']})")
        corr = CORRIGE_OGOL.get(str(o["id"]))
        if corr:
            o = dict(o, data=corr[0], gols_mandante=corr[1], gols_visitante=corr[2])
        r = re.match(r"^R(\d+)$", o["fase"] or "")
        res.append({"data": o["data"], "hora": o.get("hora") or None, "m": m, "v": v, "nm": o["mandante"], "nv": o["visitante"],
                    "gm": o["gols_mandante"], "gv": o["gols_visitante"], "rodada": int(r.group(1)) if r else None,
                    "fonte": "ogol", "fonte_id": f"ogol:{o['id']}", "ogol": o, "fase": "Liga", "grupo": None,
                    "especial": None, "obs": (f"data e placar corrigidos: {corr[3]}" if corr else None), "pen": None})
    return res


def football_data() -> dict[str, list[dict]]:
    res = defaultdict(list)
    arq = DADOS / "football-data" / "sem.csv"
    if not arq.exists():
        return res
    with open(arq, encoding="utf-8-sig") as f:
        for x in csv.DictReader(f):
            if not x.get("HG"):
                continue
            d, mth, y = x["Date"].split("/")
            data = f"{y if len(y) == 4 else '20' + y}-{mth}-{d}"
            a_, b_ = x["Season"].split("/")
            res[f"{a_}/{b_[-2:]}"].append({"data": data, "hora": x.get("Time") or None, "m": clubes.esd(x["Home"]),
                                     "v": clubes.esd(x["Away"]), "nm": x["Home"], "nv": x["Away"],
                                     "gm": int(x["HG"]), "gv": int(x["AG"])})
    return res


def carregar_espn() -> dict[str, list[dict]]:
    res = {}
    for arq in sorted((DADOS / "espn").glob("cyp1_*.json")):
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(OSLO).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
                              gv=int(j["gols_visitante"])))
        if jogos:
            res[arq.stem[5:].replace("-", "/")] = jogos
    return res


def votar_espn(ogol: dict[str, list[dict]], espn: dict[str, list[dict]]) -> dict[str, str]:
    """Código do clube na ESPN -> chave, pelos jogos de mesma data (±1 dia) e mesmo placar no ogol."""
    votos: dict[str, Counter] = defaultdict(Counter)
    for t, jogos in espn.items():
        por_dia = defaultdict(list)
        for b in ogol.get(t, []):
            if b["data"] and b["gm"] is not None:
                por_dia[(b["data"], b["gm"], b["gv"])].append(b)
        for j in jogos:
            d = date.fromisoformat(j["data"])
            cand = [b for k in (-1, 0, 1) for b in por_dia.get(((d + timedelta(days=k)).isoformat(), j["gm"], j["gv"]), [])]
            if len(cand) == 1:
                votos[j["mandante_id"]][cand[0]["m"]] += 1
                votos[j["visitante_id"]][cand[0]["v"]] += 1
    return {k: c.most_common(1)[0][0] for k, c in votos.items()}


def campeoes_rsssf() -> dict[str, str]:
    t = rsssf.texto(DADOS / "rsssf" / "cypchamp.html")
    return {m.group(1): re.sub(r"\s*\(.*\)\s*$", "", m.group(2)).strip()
            for m in re.finditer(r"^(\d{4}(?:/\d{2})?)\s+([^\s\d\[].*?)\s*$", t, re.M)}


def pagina_rsssf(t: str) -> tuple[str, str] | None:
    from edicoes import rsssf_urls
    for url in rsssf_urls(t):
        arq = DADOS / "rsssf" / url.rsplit("/", 1)[1]
        if arq.exists():
            return rsssf.texto(arq), url
    return None


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pts) -> dict[str, list[int]]:
    """J V E D GP GC Pts Extra (o ponto a mais do vencedor nos pênaltis de 1987)."""
    t = defaultdict(lambda: [0] * 8)
    for j in jogos:
        if j.get("dois"):   # derrota para os dois: um jogo e uma derrota para cada, sem gols
            for c in (j["m"], j["v"]):
                t[c][0] += 1
                t[c][3] += 1
            continue
        if j["gm"] is None:
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            k = 1 if gp > gc else 2 if gp == gc else 3
            x[k] += 1
            x[6] += pts[k - 1]
        if j["gm"] == j["gv"] and j["fase"] == "Liga" and (j.get("pen") or j.get("pen_venc")):
            t[j.get("pen_venc") or (j["m"] if j["pen"][0] > j["pen"][1] else j["v"])][7] += 1
    return t


def ordenar(t, ajuste, criterio, jogos, pts) -> list[str]:
    def p(c):
        return t[c][6] + t[c][7] + ajuste.get(c, 0)

    def geral(c):
        _, v, e, d, gp, gc, *_ = t[c]
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
            g.sort(key=lambda c: (-(mini[c][6] + mini[c][7]), -(mini[c][4] - mini[c][5]), *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def pub_wiki(x: dict, pts) -> list[int]:
    v, e, d = x["vitorias"] or 0, x["empates"] or 0, x["derrotas"] or 0
    return [v + e + d, v, e, d, x["gols_pro"], x["gols_contra"],
            pts[0] * v + pts[1] * e + pts[2] * d + (x["ajuste"] or 0) + x.get("bonus", 0)]


def pub_rs(x: dict) -> list[int]:
    return [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]


# ------------------------------------------------------------------ eras
LINHA_TAB = re.compile(r"^\s*(\d+)\.\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)(?:\s+(-?\d+))?(?:\s.*)?$")


def tabela_rsssf(t: str) -> tuple[list[dict], str] | None:
    """A primeira tabela da página da temporada: o formato do tcheco ("1.Pafos FC 26 20 2 4 50-12 62") ou o antigo, em
    colunas ("1. APOEL Nicosia  14 12 0 2 52 15 [GD] 24")."""
    pg = pagina_rsssf(t)
    if not pg:
        return None
    tbs = rsssf.tabelas(pg[0])
    if tbs:
        return tbs[0], pg[1]
    texto = pg[0][pg[0].find("Final Table"):]
    cab = next((l for l in texto.split("\n") if "Played" in l), "")
    gd_antes = re.search(r"\bGD\b.*Points", cab) is not None
    linhas = []
    for l in texto.split("\n"):
        m = LINHA_TAB.match(l.replace("\t", " "))
        if m:
            pos, nome, j, v, e, d, gp, gc, a, b = m.groups()
            pts = int(b) if (b is not None and gd_antes) else int(a)
            linhas.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                           "derrotas": int(d), "gols_pro": int(gp), "gols_contra": int(gc), "pontos": pts})
        elif linhas and l.strip() and not l.startswith(("-", " ")) and not re.match(r"^\s*\d+\.", l):
            break
    return (linhas, pg[1]) if linhas else None


def liga_wiki(t: str, W: dict, pts, ocorr: list[str]) -> dict:
    tb = max(W["tbs"], key=lambda tb: len(tb["ativos"]))
    cs = {x["clube"] for x in tb["ativos"]}
    js = []
    for b in W["blocos"]:
        if not b["clubes"] <= cs:
            ocorr.append(f"matriz da Wikipédia com outros clubes, fora do pacote: {sorted(b['clubes'] - cs)}")
            continue
        for j in b["jogos"]:
            nota = j["nota"]
            js.append({"m": j["m"], "v": j["v"], "nm": j["nm"], "nv": j["nv"], "gm": j["gm"], "gv": j["gv"], "fase": "Liga",
                       "grupo": None, "rodada": None, "data": None, "hora": None, "fonte": "Wikipédia (matriz)",
                       "fonte_id": None, "especial": None, "pen": None,
                       "obs": (f"nota da matriz da Wikipédia: {nota}" if nota else None)})
    e = {"fase": "Liga", "grupo": None, "tb": tb, "rs": None, "jogos": js, "base": [], "sem_jogos": False}
    return {"etapas": [e], "jogos": js, "ordem": None, "formato": "pontos corridos (turno e returno); sem datas (só a matriz "
            "de resultados)", "fonte_ordem": "Wikipédia (ordem oficial)", "numeros": None, "ogol": False}


def separar(jogos: list[dict], so: set) -> tuple[list[dict], list[dict]]:
    """Fase regular (o primeiro jogo de cada par mandante x visitante, pela data, entre os clubes de `so`) e o resto."""
    vistos, regular, resto = set(), [], []
    for j in sorted(jogos, key=lambda j: (j["data"] or "9999", j["rodada"] or 0)):
        if (j["m"], j["v"]) in vistos or not {j["m"], j["v"]} <= so:
            resto.append(j)
        else:
            vistos.add((j["m"], j["v"]))
            regular.append(j)
    return regular, resto


def liga_ogol(t: str, W: dict, jogos: list[dict], ocorr: list[str]) -> dict:
    tbs = [tb for tb in W["tbs"] if tb["ativos"]]
    maior = max(tbs, key=lambda tb: len(tb["ativos"]))
    liga = {x["clube"] for x in maior["ativos"]}
    fora = [j for j in jogos if not {j["m"], j["v"]} <= liga]
    for j in fora:
        ocorr.append(f"jogo com clube de fora da liga, fora do pacote: {j['m']} x {j['v']} ({j['data']}, {j['ogol']['resultado']})")
    jogos = [j for j in jogos if j not in fora]
    grupos_tb = [tb for tb in tbs if tb is not maior]
    if not grupos_tb:
        e = {"fase": "Liga", "grupo": None, "tb": maior, "rs": None, "jogos": jogos, "base": [], "sem_jogos": False}
        return {"etapas": [e], "jogos": jogos, "ordem": None, "formato": "pontos corridos (turno e returno)",
                "fonte_ordem": "Wikipédia (ordem oficial)", "numeros": None, "ogol": True}
    regular, resto = separar(jogos, liga)
    for j in regular:
        j["fase"] = "Fase regular"
    etapas = [{"fase": "Fase regular", "grupo": None, "tb": maior, "rs": None, "jogos": regular, "base": [],
               "sem_jogos": False}]
    ordem_reg = [x["clube"] for x in maior["ativos"]]
    nomes = (["Grupo do título", "Grupo intermediário", "Grupo de rebaixamento"] if len(grupos_tb) == 3 else
             ["Grupo do título", "Grupo de rebaixamento"])
    grupos_tb.sort(key=lambda tb: min(ordem_reg.index(x["clube"]) for x in tb["ativos"]))
    sobra = list(resto)
    for tb, fase in zip(grupos_tb, nomes):
        cs = {x["clube"] for x in tb["ativos"]}
        cand = [j for j in sobra if {j["m"], j["v"]} <= cs]
        js, _ = separar(cand, cs)   # turno e returno no grupo: o que passa disso é desempate
        sobra = [j for j in sobra if j not in js]
        for j in js:
            j["fase"] = fase
        base = [j for j in regular if j["m"] in cs or j["v"] in cs]
        etapas.append({"fase": fase, "grupo": None, "tb": tb, "rs": None, "jogos": js, "base": base, "sem_jogos": False})
    for j in sobra:
        j["fase"] = "Desempate"
        j["obs"] = "jogo fora dos grupos (desempate)"
        ocorr.append(f"jogo fora da fase regular e dos grupos, como desempate: {j['m']} x {j['v']} ({j['data']})")
    ordem = [x["clube"] for nome in nomes for e in etapas if e["fase"] == nome for x in e["tb"]["ativos"]]
    ordem += [c for c in ordem_reg if c not in ordem]
    if len(grupos_tb) == 3:
        formato = ("fase regular em turno e returno; grupos de 4 (título, intermediário e rebaixamento) em turno e returno, "
                   "com os pontos acumulados")
    else:
        formato = ("fase regular em turno e returno; grupos do título e de rebaixamento em turno e returno, com os pontos "
                   "acumulados")
    return {"etapas": etapas, "jogos": jogos, "ordem": ordem, "formato": formato,
            "fonte_ordem": "Wikipédia (grupo do título, depois os outros grupos, depois a fase regular)", "numeros": None,
            "ogol": True}


# ------------------------------------------------------------------ artilheiros
def artilheiros(ocorr) -> list[dict]:
    """dentops.html, em colunas: "1991/92 Peter Moller   (Aalborg Boldklub)   17"; empate na linha seguinte."""
    res, t = [], None
    for l in rsssf.texto(DADOS / "rsssf" / "cyptops.html").split("\n"):
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+(\S.*?)\s+\(([^)]*)\)\s+(\d+)\s*$", l)
        if not m:
            if l.strip():
                t = None
            continue
        if m.group(1):
            t = m.group(1)
        if t not in TEMPORADAS:
            continue
        nome = " ".join(w.capitalize() if w.isupper() and len(w) > 1 else w for w in m.group(2).split())
        nome = nome.replace(chr(0x93), '"').replace(chr(0x94), '"').replace('-"', ' "')   # aspas do Windows-1252
        if ", " in nome:   # "Tsiges, Takis" -> "Takis Tsiges"
            sobrenome, prenome = nome.split(", ", 1)
            nome = f"{prenome} {sobrenome}"
        c = clubes.esd(m.group(3)) if "/" not in m.group(3) else None
        if c is None:
            ocorr[t].append(f"artilheiro sem um clube só na lista da RSSSF: {nome} ({m.group(3)})")
        res.append({"temporada": t, "jogador": nome, "clube": clubes.exibicao(c) if c else None, "gols": int(m.group(4)),
                    "fonte": "RSSSF (tablesc/cyptops.html)"})
    return res


# ------------------------------------------------------------------ principal
def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    camp_rs = campeoes_rsssf()
    fd = football_data()
    espn = carregar_espn()
    nomes = defaultdict(lambda: defaultdict(set))
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel, criterios = [], {}

    wikis = {t: ler_wiki(t) for t in TEMPORADAS}
    clubes_de = {t: {x["clube"] for tb in w["tbs"] for x in tb["times"]} for t, w in wikis.items()}
    ogol = {t: carregar_ogol(t) for t in TEMPORADAS + ["2026/27"] if t >= OGOL_DESDE}
    clubes_de["2026/27"] = {c for j in ogol["2026/27"] for c in (j["m"], j["v"])}

    mapa_espn = votar_espn(ogol, espn)

    for t in TEMPORADAS:
        ocorr[t].extend(EXPLICACOES.get(t, []))
        W = wikis[t]
        pts = pontos(t)
        if False:
            pass
        elif t in ogol:
            # jogos que o ogol não tem e o football-data tem (grupos de classificação de 2016/17): entram pelo football-data
            for x in fd.get(t, []) if t in COMPLETA_FD else []:
                if x["m"] is None or x["v"] is None:
                    continue
                d = date.fromisoformat(x["data"])
                if any((j["m"], j["v"]) == (x["m"], x["v"]) and j["data"] and
                       abs((date.fromisoformat(j["data"]) - d).days) <= 2 for j in ogol[t]):
                    continue
                ogol[t].append({"data": x["data"], "hora": None, "m": x["m"], "v": x["v"], "nm": x["nm"], "nv": x["nv"],
                                "gm": x["gm"], "gv": x["gv"], "rodada": None, "fonte": "football-data", "fonte_id": None,
                                "ogol": {"fase": "", "resultado": "", "id": None}, "fase": "Liga", "grupo": None,
                                "especial": None, "obs": "jogo que o ogol não tem: placar e data do football-data", "pen": None})
                ocorr[t].append(f"{x['m']} x {x['v']} ({x['data']}): o ogol não tem o jogo; entra {x['gm']}-{x['gv']} pelo "
                                f"football-data")
            for j in ogol[t]:
                for lado in ("m", "v"):
                    nomes[j[lado]][f"ogol:{j['n' + lado]}"].add(t)
            est = liga_ogol(t, W, ogol[t], ocorr[t])
        else:
            est = liga_wiki(t, W, pts, ocorr[t])
        etapas, jogos = est["etapas"], est["jogos"]
        era_ogol = est["ogol"]
        unica = len(etapas) == 1
        # tabela da RSSSF (a página da temporada) para conferir a da Wikipédia, casada pelos números
        trs = tabela_rsssf(t)
        e0_ = max(etapas, key=lambda e: len(e["tb"]["ativos"]))
        if trs and not e0_["rs"] and len(trs[0]) == len(e0_["tb"]["ativos"]):
            iguais = sum(pub_rs(x)[1:6] == pub_wiki(y, pts)[1:6] for x, y in zip(trs[0], e0_["tb"]["ativos"]))
            if iguais * 2 >= len(trs[0]):
                e0_["rs"] = [dict(x, clube=y["clube"]) for x, y in zip(trs[0], e0_["tb"]["ativos"])]
                e0_["fonte_rs"] = trs[1]
            else:
                ocorr[t].append(f"tabela da RSSSF sem casar pelos números com a da Wikipédia ({iguais} linhas iguais)")
        mz_w = defaultdict(list)
        pen_w = {}
        for b in W["blocos"]:
            for w in b["jogos"]:
                mz_w[(w["m"], w["v"])].append((w["gm"], w["gv"]))
                if w["pen"]:
                    pen_w[(w["m"], w["v"])] = w["pen"]

        if era_ogol:
            e0 = etapas[0]
            # ---- decididos fora de campo (sem placar no ogol): placar da matriz da Wikipédia
            for j in jogos:
                chave_d = (t, j["m"], j["v"], j["data"]) if (t, j["m"], j["v"], j["data"]) in DECIDIDOS else (t, j["m"], j["v"])
                if chave_d in DECIDIDOS and len(chave_d) == 4 and not j.get("especial"):
                    j["gm"], j["gv"], motivo = DECIDIDOS[chave_d]
                    j["especial"], j["obs"] = "awd", f"resultado decidido fora de campo: {motivo}"
                    ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): fica {j['gm']}-{j['gv']} ({motivo})")
                    continue
                if j["gm"] is not None:
                    continue
                if (t, j["m"], j["v"]) in DECIDIDOS:
                    j["gm"], j["gv"], motivo = DECIDIDOS[(t, j["m"], j["v"])]
                    j["especial"], j["obs"] = "awd", f"resultado decidido fora de campo: {motivo}"
                    continue
                cand = mz_w.get((j["m"], j["v"]), [])
                if not cand:
                    raise SystemExit(f"{t}: jogo sem placar no ogol ({j['ogol']['resultado']}) e sem a matriz da Wikipédia: "
                                     f"{j['m']} x {j['v']} ({j['data']})")
                j["gm"], j["gv"] = cand[0] if j["fase"] in ("Liga", "Fase regular") or len(cand) == 1 else cand[-1]
                j["especial"] = "awd"
                j["obs"] = (f"resultado decidido fora de campo (no ogol: \"{j['ogol']['resultado']}\", sem placar); placar "
                            f"oficial pela matriz da Wikipédia")
                ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): {j['ogol']['resultado']} no ogol; fica {j['gm']}-{j['gv']} "
                                f"pela matriz da Wikipédia")
            if t in PENALTIS:
                for j in jogos:
                    if j["gm"] == j["gv"] and (j["m"], j["v"]) in pen_w:
                        j["pen"] = pen_w[(j["m"], j["v"])]
                sem = [j for j in jogos if j["gm"] == j["gv"] and not j["pen"]]
                pk = {x["clube"]: x["pk"][0] or 0 for x in e0["tb"]["ativos"] if x["pk"]}
                feitas = Counter(j["m"] if j["pen"][0] > j["pen"][1] else j["v"] for j in jogos if j["pen"])
                for j in sem:   # o vencedor pela contagem de vitórias nos pênaltis da tabela
                    falta_m, falta_v = pk.get(j["m"], 0) - feitas[j["m"]], pk.get(j["v"], 0) - feitas[j["v"]]
                    if (falta_m, falta_v) in ((1, 0), (0, 1)) and sum(1 for k in sem if j["m"] in (k["m"], k["v"])) == 1:
                        j["pen_venc"] = j["m"] if falta_m else j["v"]
                        j["obs"] = (f"empate; {j['pen_venc']} venceu nos pênaltis (pela contagem da tabela da Wikipédia; o "
                                    f"placar dos pênaltis não está nas fontes)")
                        ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): empate sem os pênaltis na matriz da Wikipédia; "
                                        f"{j['pen_venc']} venceu, pela contagem da tabela")
                    else:
                        ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): empate sem os pênaltis na matriz da Wikipédia")
            for m, v, fase, motivo in DERROTA_DOIS.get(t, []):
                e_ = next(e for e in etapas if e["fase"] == fase)
                j = {"m": m, "v": v, "nm": m, "nv": v, "gm": None, "gv": None, "fase": fase, "grupo": None, "rodada": None,
                     "data": None, "hora": None, "fonte": "Wikipédia (tabela)", "fonte_id": None, "especial": "awd", "pen": None,
                     "obs": f"derrota para os dois: {motivo}", "dois": True}
                e_["jogos"].append(j)
                jogos.append(j)
                ocorr[t].append(f"{m} x {v}: derrota para os dois ({motivo})")
            mz_reg = defaultdict(list)
            for e in etapas:
                bloco = next((b for b in W["blocos"] if b["clubes"] == {x["clube"] for x in e["tb"]["ativos"]}), None)
                if bloco is None:
                    continue
                for w in bloco["jogos"]:
                    if e is e0:
                        mz_reg[(w["m"], w["v"])].append((w["gm"], w["gv"]))
                    if not (w["nota"] and re.search(r"(?i)awarded|walk ?over|forfeit", w["nota"])):
                        continue
                    cand = [j for j in e["jogos"] if (j["m"], j["v"]) == (w["m"], w["v"]) and not j["especial"]]
                    if len(cand) != 1:
                        continue
                    j = cand[0]
                    if (j["gm"], j["gv"]) != (w["gm"], w["gv"]):
                        ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): fica {w['gm']}-{w['gv']}, decidido fora de campo "
                                        f"(nota da matriz da Wikipédia); o ogol dá {j['gm']}-{j['gv']}")
                    j["gm"], j["gv"], j["especial"] = w["gm"], w["gv"], "awd"
                    j["obs"] = "resultado decidido fora de campo pela federação (nota da matriz da Wikipédia)"
            if not mz_reg:
                mz_reg = mz_w
            # ---- RSSSF: tabela e jogos da página da temporada (desde 1998)
            pg = pagina_rsssf(t)
            rs_jogos = []
            if pg:
                tbs_rs = rsssf.tabelas(pg[0])
                if False:
                    linhas = tbs_rs[0]
                    ok = [dict(x, clube=clubes.esd(x["nome"])) for x in linhas]
                    if {x["clube"] for x in ok} == {x["clube"] for x in e0["tb"]["ativos"]}:
                        e0["rs"] = ok
                    else:
                        ocorr[t].append(f"tabela da RSSSF com outros clubes: {sorted(str(x['clube']) for x in ok)}")
                for x in []:
                    m, v = clubes.esd(x["m"]), clubes.esd(x["v"])
                    if m and v and {m, v} <= {y["clube"] for y in e0["tb"]["ativos"]}:
                        rs_jogos.append(dict(x, cm=m, cv=v))
            if rs_jogos:
                pares = Counter((j["m"], j["v"], j["gm"], j["gv"]) for j in jogos)
                iguais = sum(1 for x in rs_jogos if pares[(x["cm"], x["cv"], x["gm"], x["gv"])])
                if iguais < 0.9 * len(rs_jogos):
                    ocorr[t].append(f"jogos da página da RSSSF fora da conferência: só {iguais} de {len(rs_jogos)} batem com o "
                                    f"ogol (a página mistura outras competições ou a leitura falhou)")
                    rs_jogos = []
            # ---- ogol x matriz da Wikipédia: placar diferente; fica a matriz quando fecha melhor com as tabelas ou, empatada,
            # quando o football-data ou a RSSSF concordam com ela
            fd_idx = defaultdict(list)
            for x in fd.get(t, []):
                fd_idx[(x["m"], x["v"])].append((x["gm"], x["gv"]))
            rs_idx = defaultdict(list)
            for x in rs_jogos:
                rs_idx[(x["cm"], x["cv"])].append((x["gm"], x["gv"]))
            pubs = [{x["clube"]: pub_wiki(x, pts)[:6] for x in e0["tb"]["ativos"]}]
            if e0["rs"]:
                pubs.append({x["clube"]: pub_rs(x)[:6] for x in e0["rs"]})

            def distancia(cs):
                c_ = calcular(e0["jogos"], pts)
                return sum(abs(c_[c][q] - p_[c][q]) for p_ in pubs for c in cs if c in p_ for q in range(6))
            difs = defaultdict(list)
            for j in jogos:
                pl = mz_reg.get((j["m"], j["v"]))
                if j["fase"] in ("Liga", "Fase regular") and j["fonte"] == "ogol" and not j["especial"] and pl and len(pl) == 1 \
                        and (j["gm"], j["gv"]) not in pl:
                    difs[frozenset((j["m"], j["v"]))].append(j)
            for par, js in difs.items():
                for grupo_js in ([js] if len(js) > 1 else []) + [[j] for j in js]:
                    if any(j.get("trocado") for j in grupo_js):
                        continue
                    antes = distancia(tuple(par))
                    velhos = [(j["gm"], j["gv"]) for j in grupo_js]
                    for j in grupo_js:
                        j["gm"], j["gv"] = mz_reg[(j["m"], j["v"])][0]
                    d = distancia(tuple(par))
                    vts = [[f for f, ok in (("football-data", (j["gm"], j["gv"]) in fd_idx.get((j["m"], j["v"]), [])),
                                            ("RSSSF", (j["gm"], j["gv"]) in rs_idx.get((j["m"], j["v"]), []))) if ok]
                           for j in grupo_js]
                    if d < antes or (d == antes and all(vts)):
                        for j, vp, vt in zip(grupo_js, velhos, vts):
                            j["trocado"] = True
                            txt = f" (igual ao {' e à '.join(vt)})" if vt else ""
                            j["obs"] = f"placar da matriz da Wikipédia{txt}; o ogol dá {vp[0]}-{vp[1]}"
                            ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): fica {j['gm']}-{j['gv']} pela matriz da "
                                            f"Wikipédia{txt}; o ogol dá {vp[0]}-{vp[1]}"
                                            + (", que fecha pior com as tabelas" if d < antes else ""))
                    else:
                        for j, vp in zip(grupo_js, velhos):
                            j["gm"], j["gv"] = vp
            for x in fd.get(t, []):
                cand = [j for j in jogos if (j["m"], j["v"]) == (x["m"], x["v"]) and j["data"] == x["data"]
                        and j["fonte"] == "ogol" and not j["especial"] and (j["gm"], j["gv"]) != (x["gm"], x["gv"])]
                if len(cand) != 1:
                    continue
                j = cand[0]
                vt = [f for f, ok in (("RSSSF", (x["gm"], x["gv"]) in rs_idx.get((j["m"], j["v"]), [])),
                                      ("matriz da Wikipédia", (x["gm"], x["gv"]) in mz_w.get((j["m"], j["v"]), []))) if ok]
                if vt:
                    velho = (j["gm"], j["gv"])
                    j["gm"], j["gv"] = x["gm"], x["gv"]
                    j["obs"] = f"placar do football-data (igual à {' e à '.join(vt)}); o ogol dá {velho[0]}-{velho[1]}"
                    ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): fica {x['gm']}-{x['gv']} pelo football-data (igual à "
                                    f"{' e à '.join(vt)}); o ogol dá {velho[0]}-{velho[1]}")
            for e in etapas[1:]:
                cs = {x["clube"] for x in e["tb"]["ativos"]}
                bloco = next((b for b in W["blocos"] if b["clubes"] == cs), None)
                if bloco is None:
                    continue
                tem_e = Counter((j["m"], j["v"]) for j in e["jogos"])
                for w in bloco["jogos"]:
                    if tem_e[(w["m"], w["v"])]:
                        tem_e[(w["m"], w["v"])] -= 1
                        continue
                    j = {"m": w["m"], "v": w["v"], "nm": w["nm"], "nv": w["nv"], "gm": w["gm"], "gv": w["gv"], "fase": e["fase"],
                         "grupo": e["grupo"], "rodada": None, "data": None, "hora": None, "fonte": "Wikipédia (matriz)",
                         "fonte_id": None, "especial": None, "pen": None,
                         "obs": "jogo que o ogol não tem: placar da matriz da Wikipédia, sem data"}
                    e["jogos"].append(j)
                    jogos.append(j)
                    ocorr[t].append(f"{w['m']} x {w['v']} ({e['fase'].lower()}): o ogol não tem o jogo; entra "
                                    f"{w['gm']}-{w['gv']} pela matriz da Wikipédia, sem data")
            # ---- jogos que faltam no ogol: da matriz da Wikipédia, sem data
            tem = Counter((j["m"], j["v"]) for j in jogos)
            tem_par = Counter(frozenset((j["m"], j["v"])) for j in jogos)
            for (m, v), pl in mz_w.items():
                if not unica or not {m, v} <= {x["clube"] for x in e0["tb"]["ativos"]}:
                    continue
                falta = min(len(pl) - tem[(m, v)], len(pl) + len(mz_w.get((v, m), [])) - tem_par[frozenset((m, v))])
                for gm, gv in (pl[len(pl) - falta:] if falta > 0 else []):
                    j = {"m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "fase": "Liga", "grupo": None, "rodada": None,
                         "data": None, "hora": None, "fonte": "Wikipédia (matriz)", "fonte_id": None, "especial": None,
                         "pen": pen_w.get((m, v)), "obs": "jogo que o ogol não tem: placar da matriz da Wikipédia, sem data"}
                    jogos.append(j)
                    ocorr[t].append(f"{m} x {v}: o ogol não tem o jogo; entra {gm}-{gv} pela matriz da Wikipédia, sem data")
            # ---- conferência: matriz da Wikipédia, football-data, RSSSF
            por_par = defaultdict(list)
            for j in jogos:
                por_par[(j["m"], j["v"])].append((j["gm"], j["gv"]))
            dif = [f"{m} x {v}: ogol {', '.join(f'{a}-{b}' for a, b in sorted(por_par[(m, v)]))}; Wikipédia "
                   f"{', '.join(f'{a}-{b}' for a, b in pl)}" for (m, v), pl in mz_w.items()
                   if por_par.get((m, v)) and (sorted(pl) != sorted(por_par[(m, v)]) if unica else
                                               any(x not in por_par[(m, v)] for x in pl))]
            ocorr[t] += [f"placar diferente na matriz da Wikipédia — {d}" for d in dif[:15]]
            if len(dif) > 15:
                ocorr[t].append(f"... e mais {len(dif) - 15} pares com placar diferente na matriz da Wikipédia")
            for fonte, lista in (("football-data", [(x["m"], x["v"], x["data"], x["gm"], x["gv"], x["nm"], x["nv"]) for x in fd.get(t, [])]),
                                 ("RSSSF", [(x["cm"], x["cv"], None, x["gm"], x["gv"], x["m"], x["v"]) for x in rs_jogos])):
                if not lista:
                    continue
                difs_f = []
                for m, v, data, gm, gv, nm, nv in lista:
                    if m is None or v is None:
                        ocorr[t].append(f"nome do {fonte} sem cadastro: {nm} x {nv}")
                        continue
                    if (gm, gv) not in por_par.get((m, v), []) and por_par.get((m, v)):
                        difs_f.append(f"{m} x {v}{(' (' + data + ')') if data else ''}: ogol "
                                      f"{', '.join(f'{a}-{b}' for a, b in por_par[(m, v)])}, {fonte} {gm}-{gv}")
                ocorr[t] += [f"{fonte} — {d}" for d in difs_f[:10]]
                if len(difs_f) > 10:
                    ocorr[t].append(f"... e mais {len(difs_f) - 10} diferenças com o {fonte}")
            # ---- ESPN (gols e cartões) e football-data (hora), casados pelo par e pela data
            usados = set()
            for x in espn.get(t, []):
                m, v = mapa_espn.get(x["mandante_id"]), mapa_espn.get(x["visitante_id"])
                cand = [j for j in jogos if (j["m"], j["v"]) == (m, v) and id(j) not in usados and j["data"]]
                if not cand:
                    continue
                j = min(cand, key=lambda j: abs((date.fromisoformat(j["data"]) - date.fromisoformat(x["data"])).days))
                if abs((date.fromisoformat(j["data"]) - date.fromisoformat(x["data"])).days) > 3:
                    continue
                usados.add(id(j))
                j["espn"] = x
                nomes[m][f"espn:{x['mandante']}"].add(t)
                if (x["gm"], x["gv"]) != (j["gm"], j["gv"]) and not j["especial"]:
                    ocorr[t].append(f"placar diferente na ESPN — {m} x {v} ({j['data']}): {j['gm']}-{j['gv']}, ESPN "
                                    f"{x['gm']}-{x['gv']}")
            for x in fd.get(t, []):
                cand = [j for j in jogos if (j["m"], j["v"]) == (x["m"], x["v"]) and j["data"] == x["data"]]
                if cand:
                    cand[0]["fd"] = x
                    nomes[x["m"]][f"football-data:{x['nm']}"].add(t)
            for x in rs_jogos:   # autores dos gols da RSSSF (quando a conta fecha), para os jogos sem a ESPN
                if not x.get("gols_txt"):
                    continue
                cand = [j for j in jogos if (j["m"], j["v"]) == (x["cm"], x["cv"]) and (j["gm"], j["gv"]) == (x["gm"], x["gv"])]
                if len(cand) == 1 and not cand[0].get("espn"):
                    au = rsssf.autores(x["gols_txt"], x["gm"], x["gv"])
                    if au:
                        cand[0]["autores_rs"] = au

        # ---- tabelas publicadas x jogos, fase a fase
        conferidas = divergentes = 0
        ajuste: dict[str, int] = {}
        publicados: dict[str, list[int]] = {}
        publicados_liga: dict[str, list[int]] = {}
        for e in etapas:
            tb = e["tb"]
            for x in tb["ativos"]:
                nomes[x["clube"]][f"wikipedia:{x['nome']}"].add(t)
                if x["ajuste"]:
                    ajuste[x["clube"]] = x["ajuste"]
            for x in e["rs"] or []:
                nomes[x["clube"]][f"rsssf:{x['nome']}"].add(t)
            rot = f" ({e['grupo']})" if e["grupo"] else ""
            if e["sem_jogos"] or est["numeros"] == "publicados":
                for x in tb["ativos"]:
                    publicados[x["clube"]] = pub_wiki(x, pts)[:6]
            if e["sem_jogos"]:
                for x in tb["ativos"]:
                    tab["tabelas_publicadas"].append({
                        "temporada": t, "fase": e["fase"], "grupo": e["grupo"], "posicao": x["posicao"], "nome_fonte": x["nome"],
                        "clube": clubes.exibicao(x["clube"]), **dict(zip(("jogos", "vitorias", "empates", "derrotas", "gols_pro",
                                                                         "gols_contra", "pontos"), pub_wiki(x, pts))),
                        "fonte": e.get("fonte_tb") or url_wiki(t)})
                continue
            so = calcular(e["jogos"], pts)
            if e["base"]:
                com = calcular(e["base"] + e["jogos"], pts)

                def dist(c_):
                    return sum(abs(c_[x["clube"]][q] - pub_wiki(x, pts)[q]) for x in tb["ativos"] for q in range(1, 6))
                e["acumula"] = dist(com) <= dist(so)
                calc = com if e["acumula"] else so
            else:
                calc = so
            aj_tb = {x["clube"]: x["ajuste"] or 0 for x in tb["ativos"]}
            erros = {}
            for fonte, url, linhas, f_pub in (("Wikipédia", url_wiki(t), tb["ativos"], lambda x: pub_wiki(x, pts)),
                                              ("RSSSF", e.get("fonte_rs") or (pagina_rsssf(t) or ("", ""))[1], e["rs"] or [],
                                               pub_rs)):
                if not linhas:
                    continue
                erro = []
                for x in linhas:
                    c = calc.get(x["clube"])
                    pub = f_pub(x)
                    meu = (c[:6] + [c[6] + c[7] + aj_tb.get(x["clube"], 0)]) if c else None
                    if pub != meu:
                        erro.append((x["clube"], pub, meu))
                    tab["tabelas_publicadas"].append({
                        "temporada": t, "fase": e["fase"], "grupo": e["grupo"], "posicao": x["posicao"], "nome_fonte": x["nome"],
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
                    fecha = outra and c not in {x[0] for x in erros[outra[0]]}
                    ocorr[t].append(f"tabela{rot} da {fonte} x jogos — {c} tabela {pub} jogos {meu}"
                                    + (f" (a tabela da {outra[0]} fecha com os jogos)" if fecha else ""))
            if not era_ogol and len(etapas) == 1:
                for x in tb["ativos"]:
                    y = next((y for y in e["rs"] or [] if y["clube"] == x["clube"]), None)
                    pub = pub_wiki(x, pts)[:6]
                    c_ = calc.get(x["clube"])
                    if (y is None or pub_rs(y)[:6] == pub) and (c_ is None or pub != c_[:6]):
                        publicados_liga[x["clube"]] = pub
                if publicados_liga:
                    ocorr[t].append(f"os jogos da matriz não fecham com as tabelas publicadas em {len(publicados_liga)} clubes: a "
                                    f"classificação final fica com os números publicados (observação na linha)")
            ordem_tb = [x["clube"] for x in tb["ativos"]]
            crits = ("media", "saldo", "confronto") if ano_inicio(t) < 1962 else ("saldo", "confronto", "media")
            so_tb = {c: calc[c] for c in ordem_tb}
            aj_tb = {x["clube"]: x["ajuste"] or 0 for x in tb["ativos"]}
            tent = {cr: ordenar(so_tb, aj_tb, cr, (e["base"] + e["jogos"]) if e.get("acumula") else e["jogos"], pts)
                    for cr in crits}
            ok = [cr for cr, o in tent.items() if o == ordem_tb]
            cr = ok[0] if ok else min(tent, key=lambda q: sum(a != b for a, b in zip(tent[q], ordem_tb)))
            if not ok:
                d_ = [c for c, d in zip(ordem_tb, tent[cr]) if c != d]
                ocorr[t].append(f"nenhum critério calculado reproduz a ordem oficial{rot}; o mais próximo ({cr}) difere em "
                                f"{len(d_)} posições (ex.: {d_[:2]})")
            criterios[(t, id(e))] = (cr, bool(ok))
            e["criterio"] = cr
            n_esp = len(tb["ativos"]) * (len(tb["ativos"]) - 1) * (3 if t == "1994/95" else 2) // 2
            if len(e["jogos"]) != n_esp:
                ocorr[t].append(f"{len(e['jogos'])} jogos{rot} para {len(tb['ativos'])} clubes (esperados {n_esp})")

        # ---- classificação final
        ordem = est["ordem"] or [x["clube"] for x in etapas[0]["tb"]["ativos"]]
        todos = [j for j in jogos if not j["fase"].startswith(("Desempate", "Play-off"))]
        if est["numeros"] == "publicados":   # tabelas sem os jogos: o grupo pela tabela, mais o mata-mata
            numeros = defaultdict(lambda: [0] * 8)
            ko = calcular(todos, pts)
            for c in set(publicados) | set(ko):
                q = publicados.get(c, [0] * 6)
                k_ = ko.get(c, [0] * 8)
                numeros[c] = [q[i] + k_[i] for i in range(6)] + [pts[0] * q[1] + pts[1] * q[2] + pts[2] * q[3] + k_[6], 0]
        else:
            numeros = calcular(todos, pts)
        # pontos oficiais dos grupos finais (acumulados ou com o ponto de partida): o ajuste é a diferença
        oficial = {x["clube"]: pub_wiki(x, pts)[6] for e in etapas if e["fase"].startswith("Grupo d") for x in e["tb"]["ativos"]}
        prox = TEMPORADAS[TEMPORADAS.index(t) + 1] if t != TEMPORADAS[-1] else "2026/27"
        if prox != "2026/27" and ano_inicio(prox) - ano_inicio(t) > 1:   # a temporada seguinte não teve campeão
            rebaixados = {x["clube"] for e in etapas for x in e["tb"]["ativos"]
                          if x["status"] in ("R", "REL") or x["resultado"] in ("R", "REL")}
        else:
            rebaixados = set()
            for c in ordem:
                if c not in clubes_de[prox]:
                    if (t, c) in NAO_REBAIXADOS:
                        ocorr[t].append(f"{c} não está na temporada seguinte, mas não caiu: {NAO_REBAIXADOS[(t, c)]}")
                    else:
                        rebaixados.add(c)
        campeao = ordem[0]
        nome_rs = camp_rs.get(t)
        if nome_rs and clubes.esd(nome_rs) != campeao:
            ocorr[t].append(f"campeão diferente na lista de campeões da RSSSF: {nome_rs} (classificação: {campeao})")
        notas_tb = {}
        for e in etapas:
            for x in e["tb"]["ativos"]:
                if x["nota"] or x["hth"]:
                    try:
                        notas_tb.setdefault(x["clube"], notas_wiki.traduzir(x["nota"] or x["hth"]))
                    except KeyError as k:
                        notas_tb.setdefault(x["clube"], None)
                        ocorr[t].append(f"nota da tabela sem tradução: {k}")
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p, b = numeros[c] if c in numeros else [0] * 8
            obs = []
            if c in publicados_liga:
                obs.append(f"números da tabela publicada; os jogos da matriz somam {j_} jogos, {v_}-{e_}-{d_} e {gp}-{gc} gols")
                j_, v_, e_, d_, gp, gc = publicados_liga[c]
                p, b = pts[0] * v_ + pts[1] * e_ + pts[2] * d_, 0
            if est["numeros"] == "publicados":
                obs.append("números do grupo pela tabela publicada (sem os jogos), mais os do mata-mata")
            if notas_tb.get(c):
                obs.append(notas_tb[c])
            aj = (oficial[c] - p) if c in oficial else ajuste.get(c, 0) + b
            tab["classificacao_final"].append({
                "temporada": t, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + aj, "ajuste_pontos": aj,
                "situacao": "campeao" if c == campeao else "rebaixado" if c in rebaixados else None,
                "fonte": est["fonte_ordem"], "observacao": "; ".join(obs) or None})

        # ---- partidas, gols e cartões
        if era_ogol:
            jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["m"]))
        else:
            jogos.sort(key=lambda j: (ORDEM_FASES.get(j["fase"], 50), j["grupo"] or "", j["m"], j["v"]))
        gols_ano = autor_ano = 0
        rot_id = t.replace("/", "-")
        for i, j in enumerate(jogos, 1):
            pid = f"{rot_id}-{i:04d}"
            e, x = j.get("espn"), j.get("fd")
            if j["fonte"] != "ogol":
                for lado in ("m", "v"):
                    nomes[j[lado]][f"wikipedia:{j['n' + lado]}"].add(t)
            hora = j["hora"]
            if not hora and x and x.get("hora"):
                hora = datetime.fromisoformat(f"{x['data']}T{x['hora']}").replace(tzinfo=LONDRES).astimezone(OSLO).strftime("%H:%M")
            elif not hora and e:
                local = e["utc"].astimezone(OSLO)
                if local.date().isoformat() == j["data"]:
                    hora = local.strftime("%H:%M")
            fontes = [j["fonte"]] + (["football-data"] if x else []) + (["ESPN"] if e else [])
            ids = ([j["fonte_id"]] if j["fonte_id"] else []) + ([f"espn:{e['id']}"] if e else [])
            obs = j["obs"]
            if j.get("pen"):
                obs = "; ".join(x_ for x_ in (obs, f"empate; {j['pen'][0]}-{j['pen'][1]} nos pênaltis (o vencedor ganhou 2 "
                                                   f"pontos e o perdedor 1)") if x_)
            tab["partidas"].append({
                "id": pid, "temporada": t, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
                "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"],
                "penaltis_mandante": j["pen"][0] if j.get("pen") else None,
                "penaltis_visitante": j["pen"][1] if j.get("pen") else None,
                "resultado_especial": j["especial"], "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
                "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids) or None,
                "gols_texto": None, "observacao": obs, "arbitro": None, "_derrota_dois": bool(j.get("dois"))})
            gols_ano += (j["gm"] or 0) + (j["gv"] or 0)
            lado_de = {"home": j["m"], "away": j["v"]}
            if e and e["lances"] and not j["especial"]:
                vistos = set()
                lances = [l for l in e["lances"] if not ((k_ := (l["tipo"], l["minuto"], l["lado"], tuple(l["jogadores"] or ()),
                                                                 l["gol"], l["amarelo"], l["vermelho"])) in vistos or vistos.add(k_))]
                gl = [l for l in lances if l["gol"]]
                if all(l["lado"] in lado_de for l in gl) and \
                        (sum(l["lado"] == "home" for l in gl), sum(l["lado"] == "away" for l in gl)) == (j["gm"], j["gv"]):
                    for l in gl:
                        mi, ac = minuto(l["minuto"])
                        tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(lado_de[l["lado"]]),
                                            "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                            "tipo": "contra" if l["contra"] else "penalti" if l["penalti"] else "normal",
                                            "fonte": "ESPN"})
                    autor_ano += len(gl)
                for l in lances:
                    if (l["amarelo"] or l["vermelho"]) and l["lado"] in lado_de:
                        mi, ac = minuto(l["minuto"])
                        tab["cartoes"].append({"partida_id": pid, "clube": clubes.exibicao(lado_de[l["lado"]]),
                                               "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                               "cor": "vermelho" if l["vermelho"] else "amarelo", "fonte": "ESPN"})
            elif j.get("autores_rs"):
                for c, lista in zip((j["m"], j["v"]), j["autores_rs"]):
                    for nome, mi, ac, tipo in lista:
                        tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(c), "jogador": nome, "minuto": mi,
                                            "acrescimo": ac, "tipo": tipo, "fonte": "RSSSF"})
                autor_ano += j["gm"] + j["gv"]

        # ---- classificação rodada a rodada (era do ogol)
        reg = [j for j in jogos if j["fase"] in ("Liga", "Fase regular")]
        if era_ogol and reg and all(j["rodada"] for j in reg):
            jogos_r, jogos = jogos, reg
            e0 = etapas[0]
            pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
            for r in sorted({j["rodada"] for j in jogos}):
                ate = [j for j in jogos if j["rodada"] <= r]
                parcial = calcular(ate, pts)
                for pos, c in enumerate(ordenar(parcial, ajuste, e0["criterio"], ate, pts), 1):
                    jj, v_, e_, d_, gp, gc, p, b = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": t, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos,
                        "pontos": p + b + ajuste.get(c, 0), "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_,
                        "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})
            jogos = jogos_r

        # ---- edição, fases, conferência
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items() if not oficial or ano_inicio(t) >= 1995)
        obs_ed = [x for x in (
            f"punições: {pun}" if pun else "",
            "empate decidido nos pênaltis: 2 pontos ao vencedor e 1 ao perdedor (o ponto a mais em ajuste_pontos)"
            if t in PENALTIS else "",
            "o campeão também jogou o Campeonato Grego (competição gre-1)" if 1967 <= ano_inicio(t) <= 1973 else "",
        ) if x]
        tab["edicoes"].append({
            "temporada": t, "ano_inicio": ano_inicio(t), "ano_fim": ano_fim(t), "nome_oficial": nome_oficial(t),
            "num_clubes": len(ordem), "pontos_vitoria": pts[0],
            "pontos_empate": pts[1] if pts == (3, 2, 1) else None, "pontos_derrota": pts[2] if pts == (3, 2, 1) else None,
            "formato": est["formato"], "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(ordem[1]),
            "co_campeao": None,
            "fontes": ("Wikipédia" + (" + RSSSF" if any(e["rs"] for e in etapas) else "")
                       if not era_ogol else
                       "ogol + Wikipédia" + (" + RSSSF" if pagina_rsssf(t) else "") + (" + football-data" if t in fd else "")
                       + (" + ESPN" if t in espn else "")),
            "observacao": "; ".join(obs_ed) or None, "oficial": None})
        crit_txt = {"saldo": "pontos, saldo de gols", "media": "pontos, média de gols (goal average)",
                    "confronto": "pontos, confronto direto, saldo de gols"}
        fases_ed = {}
        for e in etapas:
            if e["fase"] not in fases_ed:
                n_g = sum(1 for x in etapas if x["fase"] == e["fase"])
                liga_ = e["fase"] in ("Liga", "Fase regular")
                fases_ed[e["fase"]] = {"temporada": t, "fase": e["fase"], "tipo": "liga" if liga_ else "grupos",
                                       "num_grupos": None if liga_ else n_g, "formato_serie": "pontos_corridos",
                                       "criterio": crit_txt[e.get("criterio", "saldo")] +
                                       ("; pontos acumulados com a fase regular" if e.get("acumula") else "")}
        for f in dict.fromkeys(j["fase"] for j in jogos):
            if f in fases_ed:
                continue
            ida_volta = f.startswith("Play-off")
            fases_ed[f] = {"temporada": t, "fase": f, "tipo": "mata_mata", "num_grupos": None,
                           "formato_serie": "ida_volta" if ida_volta else "jogo_unico",
                           "criterio": "soma dos placares; empate, jogo extra ou sorteio" if ida_volta else
                           "jogo único; empate, jogo extra"}
        for k, f in enumerate(sorted(fases_ed, key=lambda f: ORDEM_FASES.get(f, 50)), 1):
            tab["fases"].append({"ordem": k, **fases_ed[f]})
        tab["conferencia"].append({"temporada": t, "jogos": len(jogos), "jogos_esperados": None, "tabelas_conferidas": conferidas,
                                   "tabelas_divergentes": divergentes, "gols": gols_ano, "gols_com_autor": autor_ano,
                                   "observacao": f"campeão {clubes.exibicao(campeao)}; lista da RSSSF: {nome_rs or '—'}"})
        linhas_rel.append((t, len(ordem), len(jogos), gols_ano, autor_ano, conferidas, divergentes, clubes.exibicao(campeao),
                           pun))
        print(f"{t}: {len(jogos)} jogos, {len(ordem)} clubes, tabelas {conferidas} ok / {divergentes} div, autores {autor_ano}, "
              f"campeão {clubes.exibicao(campeao)}", flush=True)

    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c in nomes:
            tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais,
                                  "nomes_fonte": "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))})
    tab["paises"] = [{"codigo": "CYP", "nome": "Chipre", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, criterios, mapa_espn)


def relatorio(linhas, ocorr, tab, criterios, mapa_espn) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"] or 0) + int(x["gols_visitante"] or 0) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Cipriota (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/cyp-1/importar.py`. Pacote em `data/coleta/cyp-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1934/35 a 2025/26: os 86 títulos que a federação reconhece.", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['clubes'])} clubes. Sem autores dos gols e cartões (sem ESPN e sem "
        "football-data para Chipre).", "",
        "**Fontes:**",
        "- Wikipédia (en): tabelas e matriz de resultados (base dos jogos até 1995/96, conferência depois);",
        "- ogol (zerozero): base dos jogos desde 1996/97, com data, hora e rodada; calendários em `data/cache/ogol-cyp-1/`;",
        "- RSSSF: página de cada temporada (tabela; jogos por rodada desde 2009/10), lista de campeões e de artilheiros.", "",
        "**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a "
        "oficial (Wikipédia; com grupos, o grupo do título, depois os outros). Pontos 2-1-0 até 1990/91 e 3-1-0 depois. "
        "Rebaixado = clube que não está na 1ª divisão na temporada seguinte (antes de uma temporada sem campeão, a marca "
        "da tabela).", "",
        f"**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em {cr['media']} tabelas, saldo em "
        f"{cr['saldo']}, confronto direto em {cr['confronto']}).", "",
        "| Temporada | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for t, n, j, g, au, ok, dv, camp, pun in linhas:
        out.append(f"| {t} | {n} | {j} | {g} | {au} | {ok} / {dv} | {camp} | {pun or '—'} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for t, *_ in linhas:
        out += [f"### {t}", ""] + [f"- {o}" for o in ocorr.get(t, []) or ["sem ocorrências"]] + [""]
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_cyp.py`, pela linhagem do clube (o alvo do link da Wikipédia, seguindo os "
        "redirecionamentos). O AEK Larnaca fica separado do EPA e do Pezoporikos; o AEP Paphos, do Evagoras e do APOP Paphos; "
        "o Lefkoşa Türk é o Çetinkaya; o \"Trast\" de 1934/35 é o Enosis Neon Trust. APOEL, AEL Limassol, EPA Larnaca e "
        "Olympiakos Nicosia têm o mesmo nome do gre-1 (os campeões cipriotas no Campeonato Grego).",
        "- Os nomes de cada fonte, com as temporadas, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Datas e rodadas até 1995/96** (só as matrizes).",
        "- **Autores dos gols e cartões:** nenhuma fonte em lote cobre Chipre.",
        "- **Jogos que faltam nas matrizes antigas** (temporadas dos anos 1930 e 1940).",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
