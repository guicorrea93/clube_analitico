"""Monta o pacote do campeonato norueguês (nor-1), 1937/38 a 2025, e o relatório docs/coleta/nor-1.md.

Três eras, três bases de jogos:
- Norgesserien (1937/38, 1938/39, 1947/48): 11 grupos regionais e mata-mata. Os grupos ficam com a tabela da Wikipédia
  (en), que traz o link de cada clube; só um grupo por temporada tem os jogos (a matriz da Wikipédia em norueguês, Distrito
  V, grupo B). O mata-mata vem das tabelas da Wikipédia (ida, volta e jogos extras);
- Hovedserien (1948/49 a 1960/61): a matriz de resultados da Wikipédia de cada grupo, sem data nem rodada, e a final
  entre os primeiros;
- de 1961/62 em diante: o calendário do ogol (data, hora e rodada), o clube pelo código do ogol; conferido com a matriz da
  Wikipédia, a página da temporada da RSSSF (desde 1998) e o football-data (desde 2012). Gols e cartões da ESPN, casada
  pela data e pelo placar; autores dos gols da RSSSF onde a ESPN não tem (1999 a 2005, quando a conta fecha).
Tabelas publicadas: Wikipédia (ordem oficial, punições) e RSSSF. Campeões: RSSSF (noochamp.html); artilheiros: RSSSF
(nootops.html).

Pontos: 2-1-0 até 1986, 3-1-0 depois. Em 1987, o empate ia para os pênaltis: 2 pontos ao vencedor e 1 ao perdedor (o
ponto a mais em `ajuste_pontos`).

Escopo (Guilherme, 25/11/2026): ver coleta/nor-1/edicoes.py.

Uso: python coleta/nor-1/importar.py
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
import clubes_nor as clubes  # noqa: E402
import notas_wiki  # noqa: E402
import rsssf_cze as rsssf  # noqa: E402
import wiki_gre  # noqa: E402
from edicoes import DADOS, NORGESSERIEN, RAIZ, TEMPORADAS, ano_fim, ano_inicio, nome_oficial, wiki_no_titulo, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from wiki_tabela import _fecha, _num, limpar  # noqa: E402
from wiki_tabela import resultados as wiki_resultados  # noqa: E402
from wiki_tabela import tabelas as wiki_tabelas  # noqa: E402

PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "nor-1.md"
OSLO = ZoneInfo("Europe/Oslo")
LONDRES = ZoneInfo("Europe/London")
DOIS, TRES = (2, 1, 0), (3, 1, 0)
PENALTIS = {"1987"}   # empate decidido nos pênaltis: 2 pontos ao vencedor, 1 ao perdedor

FASES_KO = {"Preliminary round": "Preliminar", "Quarter-finals": "Quartas de final", "Semi-finals": "Semifinal",
            "Final": "Final"}
DESEMPATE_DE = {"Preliminar": "Desempate da preliminar", "Quartas de final": "Desempate das quartas de final",
                "Semifinal": "Desempate da semifinal", "Final": "Desempate da final"}
ORDEM_FASES = {"Liga": 0, "Grupos": 1, "Preliminar": 2, "Desempate da preliminar": 3, "Quartas de final": 4,
               "Desempate das quartas de final": 5, "Semifinal": 6, "Desempate da semifinal": 7, "Final": 8,
               "Desempate da final": 9}
# jogo decidido fora de campo ("DA" no ogol, sem placar) com o placar dado aqui: (temporada, mandante, visitante) -> ...
DECIDIDOS: dict[tuple, tuple] = {}
# clube que não está na temporada seguinte sem ter caído: (temporada, clube) -> motivo
NAO_REBAIXADOS: dict[tuple, str] = {}
EXPLICACOES: dict[str, list[str]] = {}

COMPETICAO = {
    "slug": "nor-1", "nome": "Campeonato Norueguês", "nome_curto": "Norueguês", "tipo": "liga", "nivel": 1,
    "pais": "NOR", "pais_nome": "Noruega", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Norueguês", "menu_painel": "Noruega · 1ª divisão",
    "do_painel": "do Campeonato Norueguês", "o_painel": "o Campeonato Norueguês",
    "observacao": "Os 79 títulos de liga que a federação (NFF) reconhece, desde 1937/38: Norgesserien (1937/38, 1938/39 e "
                  "1947/48, grupos regionais e mata-mata), Hovedserien (1948/49 a 1961/62), 1. divisjon (1963-1990), "
                  "Tippeligaen (1991-2016) e Eliteserien (desde 2017). Não inclui a Prøveligaen de 1914-16 (liga de teste), "
                  "1939/40 (interrompida pela guerra) nem a copa, que até 1937 dava o título de campeão norueguês.",
}


def faixa(rotulos) -> str:
    a = sorted(rotulos, key=TEMPORADAS_ORDEM.get)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else a[0]


TEMPORADAS_ORDEM = {t: i for i, t in enumerate(TEMPORADAS + ["2026"])}


def pontos(t: str) -> tuple[int, int, int]:
    return DOIS if ano_inicio(t) < 1987 else TRES


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
    """Tabelas (clube pelo link), matrizes (blocos; pênaltis de 1987 à parte) e o texto."""
    txt = texto_wiki(t)
    cod, vis = {}, {}
    for c, alvo, nome in re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", txt):
        cod.setdefault(c, alvo.strip())
        vis.setdefault((nome or alvo).strip(), alvo.strip())

    def ident(alvo: str | None, nome: str) -> str:
        c = clubes.link(alvo) if alvo else None
        c = c or clubes.link(vis.get((nome or "").strip())) or clubes.VISIVEIS.get((nome or "").strip())
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
            ma = ident(alvos.get(a) or cod.get(a), g["nomes"].get(a, a))
            mb = ident(alvos.get(b) or cod.get(b), g["nomes"].get(b, b))
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
    for o in json.loads((DADOS / "ogol" / f"nor1_{t.replace('/', '-')}.json").read_text(encoding="utf-8")):
        if o["resultado"] in ("ADI", "ANU"):
            continue
        m = clubes.ogol(o["mandante_id"], t) or clubes.esd(o["mandante"])
        v = clubes.ogol(o["visitante_id"], t) or clubes.esd(o["visitante"])
        if m is None or v is None:
            raise SystemExit(f"{t}: clube do ogol sem cadastro: {o['mandante']} ({o['mandante_id']}) x "
                             f"{o['visitante']} ({o['visitante_id']})")
        r = re.match(r"^R(\d+)$", o["fase"] or "")
        res.append({"data": o["data"], "hora": o.get("hora") or None, "m": m, "v": v, "nm": o["mandante"], "nv": o["visitante"],
                    "gm": o["gols_mandante"], "gv": o["gols_visitante"], "rodada": int(r.group(1)) if r else None,
                    "fonte": "ogol", "fonte_id": f"ogol:{o['id']}", "ogol": o, "fase": "Liga", "grupo": None,
                    "especial": None, "obs": None, "pen": None})
    return res


def football_data() -> dict[str, list[dict]]:
    res = defaultdict(list)
    with open(DADOS / "football-data" / "NOR.csv", encoding="utf-8-sig") as f:
        for x in csv.DictReader(f):
            if not x.get("HG"):
                continue
            d, mth, y = x["Date"].split("/")
            data = f"{y if len(y) == 4 else '20' + y}-{mth}-{d}"
            res[x["Season"]].append({"data": data, "hora": x.get("Time") or None, "m": clubes.esd(x["Home"]),
                                     "v": clubes.esd(x["Away"]), "nm": x["Home"], "nv": x["Away"],
                                     "gm": int(x["HG"]), "gv": int(x["AG"])})
    return res


def carregar_espn() -> dict[str, list[dict]]:
    res = {}
    for arq in sorted((DADOS / "espn").glob("nor1_*.json")):
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(OSLO).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
                              gv=int(j["gols_visitante"])))
        if jogos:
            res[arq.stem[5:]] = jogos
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
    t = rsssf.texto(DADOS / "rsssf" / "noochamp.html")
    return {m.group(1): re.sub(r"\s*\(.*\)\s*$", "", m.group(2)).strip()
            for m in re.finditer(r"^(\d{4}(?:/\d{2})?)\s+([^\s\d\[].*?)\s*$", t, re.M)}


def pagina_rsssf(t: str) -> tuple[str, str] | None:
    a = ano_inicio(t)
    for n in (f"noo{str(a)[-2:]}.html", f"noo{a}.html"):
        arq = DADOS / "rsssf" / n
        if arq.exists() and "/" not in t:
            return rsssf.texto(arq), f"https://www.rsssf.org/tablesn/{n}"
    return None


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pts) -> dict[str, list[int]]:
    """J V E D GP GC Pts Extra (o ponto a mais do vencedor nos pênaltis de 1987)."""
    t = defaultdict(lambda: [0] * 8)
    for j in jogos:
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
            pts[0] * v + pts[1] * e + (x["ajuste"] or 0) + x.get("bonus", 0)]


def pub_rs(x: dict) -> list[int]:
    return [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]


# ------------------------------------------------------------------ eras
def _celulas(linha: str) -> list[str]:
    return [c.strip() for c in re.split(r"\|\||(?<=^)\|", linha.strip().lstrip("|!"))]


def _clube_celula(W, cel: str) -> str | None:
    m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", cel)
    return W["ident"](m.group(1), m.group(2) or m.group(1)) if m else None


def _placar(cel: str):
    c = limpar(cel)
    m = re.match(r"^(\d+)\s*[–-]\s*(\d+)", c)
    return (int(m.group(1)), int(m.group(2)), bool(re.search(r"(?i)a\.?e\.?t|overtime", cel))) if m else None


def mata_mata(t: str, W: dict, ocorr: list[str]) -> list[dict]:
    """Mata-mata da Norgesserien: tabelas "Team 1 || Agg. || Team 2 || 1st leg || 2nd leg [|| Replay]" (ida e volta, os
    placares com o time 1 primeiro) ou "Team 1 || Score || Team 2 [|| Replay || 2nd replay]" (jogo único)."""
    txt = W["texto"]
    ini = txt.find("==Championship play-offs==")
    fim = txt.find("==Relegation play-offs==", ini)
    parte = txt[ini:fim if fim > 0 else txt.find("==References==", ini)]
    jogos = []
    for sec, corpo in re.findall(r"===\s*([^=]+?)\s*===\n(.*?)(?=\n===|\Z)", parte, flags=re.S):
        fase = FASES_KO.get(sec.strip())
        if fase is None:
            continue
        cab = None
        for linha in corpo.split("\n"):
            if linha.startswith("!"):
                cab = [limpar(re.sub(r"\{\{\s*Abbr\s*\|([^|}]*)\|[^}]*\}\}", r"\1", c)).lower() for c in _celulas(linha)]
                continue
            if not linha.startswith("||") or cab is None:
                continue
            cels = _celulas(linha)
            col = dict(zip(cab, cels))
            t1, t2 = _clube_celula(W, col.get("team 1", "")), _clube_celula(W, col.get("team 2", ""))
            if t1 is None or t2 is None:
                ocorr.append(f"linha do mata-mata sem clube: {linha[:80]}")
                continue
            venc = t1 if "'''" in col.get("team 1", "") else t2 if "'''" in col.get("team 2", "") else None
            jogos_par = []
            if "agg." in cab:
                for k, (m, v, inverte) in (("1st leg", (t1, t2, False)), ("2nd leg", (t2, t1, True))):
                    p = _placar(col.get(k, ""))
                    if p:
                        gm, gv = (p[1], p[0]) if inverte else (p[0], p[1])
                        jogos_par.append((fase, m, v, gm, gv, p[2], f"{'ida' if k == '1st leg' else 'volta'}"))
            else:
                p = _placar(col.get("score", ""))
                if p:
                    jogos_par.append((fase, t1, t2, p[0], p[1], p[2], "jogo único"))
            for k in ("replay", "2nd replay"):
                p = _placar(col.get(k, ""))
                if p:
                    jogos_par.append((DESEMPATE_DE[fase], t1, t2, p[0], p[1], p[2], "jogo extra; mando não informado"))
                elif col.get(k) and limpar(col[k]) not in ("", "N/A", "—"):
                    ocorr.append(f"{fase}: {t1} x {t2} — {limpar(col[k])}")
            for f, m, v, gm, gv, aet, txt_obs in jogos_par:
                jogos.append({"m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "fase": f, "grupo": None, "rodada": None,
                              "data": None, "hora": None, "fonte": "Wikipédia (mata-mata)", "fonte_id": None,
                              "especial": None, "pen": None, "venc": venc,
                              "obs": txt_obs + ("; com prorrogação" if aet else "")})
            if venc is None:
                ocorr.append(f"{fase}: {t1} x {t2} sem vencedor marcado na Wikipédia")
    return jogos


def matriz_no(t: str, tb: dict) -> list[dict]:
    """Matriz da Wikipédia em norueguês ({{Fb r header}} / {{Fb r team}} / {{Fb r |gf= |ga= }}) do grupo da tabela `tb`.
    Os nomes curtos ("Djerv 1919", "Stavanger") casam com os clubes da tabela pelo nome."""
    arq = DADOS / "wikipedia-no" / f"{wiki_no_titulo(t)}.wiki"
    txt = arq.read_text(encoding="utf-8")
    m = re.search(r"\{\{Fb r header\s*\|nt=\d+\s*\|([^}]*)\}\}", txt)
    if not m:
        return []
    nomes = [x.strip() for x in m.group(1).split("|") if x.strip()]
    ativos = tb["ativos"]

    def casa(curto):
        n = _normal(curto)
        cand = [x["clube"] for x in ativos if n in _normal(x["nome"]) or n in _normal(x["clube"]) or _normal(x["nome"]) in n]
        return cand[0] if len(cand) == 1 else None
    mapa = {n: casa(n) for n in nomes}
    if None in mapa.values() or len(set(mapa.values())) != len(nomes):
        raise SystemExit(f"{t}: matriz norueguesa sem casar com a tabela: {mapa}")
    jogos = []
    for bloco in re.split(r"\{\{Fb r team\s*\|t=", txt[m.end():])[1:]:
        dono = bloco.split("}}", 1)[0].strip()
        cels = re.findall(r"\{\{Fb r\s*\|([^}]*)\}\}", bloco.split("{{Fb r footer", 1)[0])
        for adv, cel in zip(nomes, cels):
            g = re.search(r"gf=\s*(\d+)\s*\|\s*ga=\s*(\d+)", cel)
            if g and adv != dono:
                jogos.append({"m": mapa[dono], "v": mapa[adv], "nm": dono, "nv": adv, "gm": int(g.group(1)), "gv": int(g.group(2)),
                              "fase": "Grupos", "grupo": None, "rodada": None, "data": None, "hora": None,
                              "fonte": "Wikipédia em norueguês (matriz)", "fonte_id": None, "especial": None, "pen": None,
                              "obs": None})
    return jogos


def _grupo_pt(caminho: list[str]) -> str:
    s = (caminho or [""])[-1]
    s = s.replace("District", "Distrito").replace(", Group ", ", grupo ")
    return s


def norgesserien(t: str, W: dict, pts, ocorr: list[str]) -> dict:
    etapas = []
    for tb in W["tbs"]:
        if any("elegation" in s for s in tb["caminho"]):
            continue
        grupo = _grupo_pt(tb["caminho"])
        js = matriz_no(t, tb) if grupo == "Distrito V, grupo B" else []
        for j in js:
            j["grupo"] = grupo
        etapas.append({"fase": "Grupos", "grupo": grupo, "tb": tb, "rs": None, "jogos": js, "base": [], "sem_jogos": not js})
    ko = mata_mata(t, W, ocorr)
    # ordem: campeão e vice, depois quem caiu em cada fase (semifinal, quartas, preliminar), depois os outros pela posição
    venc_final = next(j["venc"] for j in ko if j["fase"] == "Final")
    final = [j for j in ko if j["fase"] in ("Final", "Desempate da final")][0]
    ordem = [venc_final, final["v"] if final["m"] == venc_final else final["m"]]
    for fase in ("Semifinal", "Quartas de final", "Preliminar"):
        for j in ko:
            if j["fase"] == fase:
                for c in (j["m"], j["v"]):
                    if c != j["venc"] and c not in ordem:
                        ordem.append(c)
    resto = []
    for e in etapas:
        for x in e["tb"]["ativos"]:
            if x["clube"] not in ordem:
                p = pub_wiki(x, pts)
                resto.append((x["posicao"], -p[6], -(p[4] - p[5]), -p[4], x["clube"]))
    ordem += [c for *_, c in sorted(resto)]
    return {"etapas": etapas, "jogos": [j for e in etapas for j in e["jogos"]] + ko, "ordem": ordem,
            "formato": "11 grupos regionais (turno e returno) e mata-mata entre os primeiros (preliminar, quartas de final "
                       "em ida e volta, semifinal e final em jogo único); dos grupos, só um tem os jogos (Distrito V, grupo B)",
            "fonte_ordem": "Wikipédia (o mata-mata, depois a posição no grupo)", "numeros": "publicados"}


def hovedserien(t: str, W: dict, pts, ocorr: list[str]) -> dict:
    etapas = []
    livres = [tb for tb in W["tbs"] if tb["ativos"]]
    for k, b in enumerate(W["blocos"]):
        tb = next((tb for tb in livres if {x["clube"] for x in tb["ativos"]} == b["clubes"]), None)
        if tb is None:
            ocorr.append(f"matriz da Wikipédia sem tabela de mesmos clubes, fora do pacote: {sorted(b['clubes'])}")
            continue
        livres.remove(tb)
        grupo = f"Grupo {'AB'[len(etapas)]}"
        js = [{"m": j["m"], "v": j["v"], "nm": j["nm"], "nv": j["nv"], "gm": j["gm"], "gv": j["gv"], "fase": "Grupos",
               "grupo": grupo, "rodada": None, "data": None, "hora": None, "fonte": "Wikipédia (matriz)", "fonte_id": None,
               "especial": None, "pen": None, "obs": (f"nota da matriz da Wikipédia: {j['nota']}" if j["nota"] else None)}
              for j in b["jogos"]]
        etapas.append({"fase": "Grupos", "grupo": grupo, "tb": tb, "rs": None, "jogos": js, "base": [], "sem_jogos": False})
    # final: "*[[A]] 1–3 [[B]]" (um ou dois jogos) ou "*[[A]] - [[B]]: 2-2 (AET), 4-1 (Replay)"
    txt = W["texto"]
    i = max(txt.find("==Championship final"), txt.find("==Final"))
    final = []
    for linha in txt[i:txt.find("\n==", i + 5)].split("\n") if i >= 0 else []:
        m = re.match(r"^\*\s*\[\[([^\]|]+)(?:\|[^\]]*)?\]\]\s*(\d+)\s*[–-]\s*(\d+)\s*\[\[([^\]|]+)", linha)
        if m:
            a, b = W["ident"](m.group(1), m.group(1)), W["ident"](m.group(4), m.group(4))
            final.append(("Final", a, b, int(m.group(2)), int(m.group(3)), None))
            continue
        m = re.match(r"^\*\s*\[\[([^\]|]+)[^\]]*\]\]\s*-\s*\[\[([^\]|]+)[^\]]*\]\]:\s*(\d+)-(\d+)[^,]*,\s*(\d+)-(\d+)", linha)
        if m:
            a, b = W["ident"](m.group(1), m.group(1)), W["ident"](m.group(2), m.group(2))
            final.append(("Final", a, b, int(m.group(3)), int(m.group(4)), "com prorrogação"))
            final.append(("Desempate da final", a, b, int(m.group(5)), int(m.group(6)), "jogo extra; mando não informado"))
    extra = [{"m": a, "v": b, "nm": a, "nv": b, "gm": gm, "gv": gv, "fase": f, "grupo": None, "rodada": None, "data": None,
              "hora": None, "fonte": "Wikipédia", "fonte_id": None, "especial": None, "pen": None,
              "obs": obs or f"final entre os primeiros dos grupos, {k}º jogo"}
             for k, (f, a, b, gm, gv, obs) in enumerate(final, 1)]
    if not extra:
        raise SystemExit(f"{t}: final da Hovedserien não encontrada na Wikipédia")
    des = [j for j in extra if j["fase"] == "Desempate da final"]
    if des:
        d = des[0]
        venc = d["m"] if d["gm"] > d["gv"] else d["v"]
    else:
        tot = calcular(extra, pts)
        venc = max(tot, key=lambda c: (tot[c][6], tot[c][4] - tot[c][5]))
    ordem = [venc, next(c for c in {j["m"] for j in extra} | {j["v"] for j in extra} if c != venc)]
    resto = []
    for e in etapas:
        calc = calcular(e["jogos"], pts)
        for x in e["tb"]["ativos"]:
            if x["clube"] not in ordem:
                p = calc[x["clube"]]
                resto.append((x["posicao"], -p[6], -(p[4] - p[5]), -p[4], x["clube"]))
    ordem += [c for *_, c in sorted(resto)]
    return {"etapas": etapas, "jogos": [j for e in etapas for j in e["jogos"]] + extra, "ordem": ordem,
            "formato": "dois grupos de 8 (turno e returno) e final entre os primeiros; sem datas (só a matriz de resultados)",
            "fonte_ordem": "Wikipédia (final entre os primeiros dos grupos; depois a posição no grupo)", "numeros": "todos"}


def liga_ogol(t: str, W: dict, jogos: list[dict], ocorr: list[str]) -> dict:
    maior = max((tb for tb in W["tbs"] if tb["ativos"]), key=lambda tb: len(tb["ativos"]))
    liga = {x["clube"] for x in maior["ativos"]}
    for tb in W["tbs"]:
        if tb is not maior:
            ocorr.append(f"tabela da Wikipédia do play-off de rebaixamento (com clubes da 2ª divisão), fora do pacote: "
                         f"{[x['clube'] for x in tb['ativos']]}")
    fora = [j for j in jogos if not {j["m"], j["v"]} <= liga]
    for j in fora:
        ocorr.append(f"jogo com clube de fora da liga, fora do pacote: {j['m']} x {j['v']} ({j['data']}, {j['ogol']['resultado']})")
    jogos = [j for j in jogos if j not in fora]
    e = {"fase": "Liga", "grupo": None, "tb": maior, "rs": None, "jogos": jogos, "base": [], "sem_jogos": False}
    return {"etapas": [e], "jogos": jogos, "ordem": None, "formato": "pontos corridos (turno e returno)",
            "fonte_ordem": "Wikipédia (ordem oficial)", "numeros": None}


# ------------------------------------------------------------------ artilheiros
def _dobra(s: str) -> str:
    return _normal(s)


def artilheiros(ocorr) -> list[dict]:
    """nootops.html, em colunas: "1951/52  Jan TANGEN    Strømmen    15"; empate na linha seguinte, sem a temporada."""
    res, t = [], None
    for l in rsssf.texto(DADOS / "rsssf" / "nootops.html").split("\n"):
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+(\S.*?)\s{2,}(\S.*?)\s+(\d+)\s*$", l)
        if not m:
            if l.strip():
                t = None
            continue
        if m.group(1):
            t = m.group(1)
        if t not in TEMPORADAS:
            continue
        nome = " ".join(w.capitalize() if w.isupper() and len(w) > 1 else w for w in m.group(2).split())
        c = clubes.esd(m.group(3))
        # o nome curto vale o clube antigo antes da refundação (Sandefjord 1998, Sarpsborg 08 2008, Kristiansund BK 2003)
        c = {("Sandefjord", True): "Sandefjord BK", ("Sarpsborg 08", True): "Sarpsborg FK",
             ("Kristiansund BK", True): "Kristiansund FK"}.get((c, ano_inicio(t) < {"Sandefjord": 1998, "Sarpsborg 08": 2008,
                                                                                    "Kristiansund BK": 2003}.get(c, 0)), c)
        if c is None:
            ocorr[t].append(f"artilheiro com clube sem cadastro na lista da RSSSF: {nome} ({m.group(3)})")
        res.append({"temporada": t, "jogador": nome, "clube": clubes.exibicao(c) if c else None, "gols": int(m.group(4)),
                    "fonte": "RSSSF (tablesn/nootops.html)"})
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
    ogol = {t: carregar_ogol(t) for t in TEMPORADAS + ["2026"] if t >= "1961/62" or "/" not in t}
    clubes_de["2026"] = {c for j in ogol["2026"] for c in (j["m"], j["v"])}
    mapa_espn = votar_espn(ogol, espn)

    for t in TEMPORADAS:
        ocorr[t].extend(EXPLICACOES.get(t, []))
        W = wikis[t]
        pts = pontos(t)
        if t in NORGESSERIEN:
            est = norgesserien(t, W, pts, ocorr[t])
        elif t < "1961/62" and "/" in t:
            est = hovedserien(t, W, pts, ocorr[t])
        else:
            for j in ogol[t]:
                for lado in ("m", "v"):
                    nomes[j[lado]][f"ogol:{j['n' + lado]}"].add(t)
            est = liga_ogol(t, W, ogol[t], ocorr[t])
        etapas, jogos = est["etapas"], est["jogos"]
        era_ogol = est["numeros"] is None

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
                j["gm"], j["gv"] = cand[0]
                j["especial"] = "awd"
                j["obs"] = (f"resultado decidido fora de campo (no ogol: \"{j['ogol']['resultado']}\", sem placar); placar "
                            f"oficial pela matriz da Wikipédia")
                ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): {j['ogol']['resultado']} no ogol; fica {j['gm']}-{j['gv']} "
                                f"pela matriz da Wikipédia")
            # ---- pênaltis de 1987 (só na matriz da Wikipédia)
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
            # ---- RSSSF: tabela e jogos da página da temporada (desde 1998)
            pg = pagina_rsssf(t)
            rs_jogos = []
            if pg:
                tbs_rs = rsssf.tabelas(pg[0])
                if tbs_rs:
                    linhas = tbs_rs[0]
                    ok = [dict(x, clube=clubes.esd(x["nome"])) for x in linhas]
                    if {x["clube"] for x in ok} == {x["clube"] for x in e0["tb"]["ativos"]}:
                        e0["rs"] = ok
                    else:
                        ocorr[t].append(f"tabela da RSSSF com outros clubes: {sorted(str(x['clube']) for x in ok)}")
                for x in rsssf.jogos(pg[0], ano_inicio(t)):
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
                c_ = calcular(jogos, pts)
                return sum(abs(c_[c][q] - p_[c][q]) for p_ in pubs for c in cs if c in p_ for q in range(6))
            difs = defaultdict(list)
            for j in jogos:
                pl = mz_w.get((j["m"], j["v"]))
                if j["fonte"] == "ogol" and not j["especial"] and pl and len(pl) == 1 and (j["gm"], j["gv"]) not in pl:
                    difs[frozenset((j["m"], j["v"]))].append(j)
            for par, js in difs.items():
                for grupo_js in ([js] if len(js) > 1 else []) + [[j] for j in js]:
                    if any(j.get("trocado") for j in grupo_js):
                        continue
                    antes = distancia(tuple(par))
                    velhos = [(j["gm"], j["gv"]) for j in grupo_js]
                    for j in grupo_js:
                        j["gm"], j["gv"] = mz_w[(j["m"], j["v"])][0]
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
            # ---- jogos que faltam no ogol: da matriz da Wikipédia, sem data
            tem = Counter((j["m"], j["v"]) for j in jogos)
            tem_par = Counter(frozenset((j["m"], j["v"])) for j in jogos)
            for (m, v), pl in mz_w.items():
                if not {m, v} <= {x["clube"] for x in e0["tb"]["ativos"]}:
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
                   if por_par.get((m, v)) and sorted(pl) != sorted(por_par[(m, v)])]
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
                        "fonte": url_wiki(t)})
                continue
            calc = calcular(e["jogos"], pts)
            erros = {}
            for fonte, url, linhas, f_pub in (("Wikipédia", url_wiki(t), tb["ativos"], lambda x: pub_wiki(x, pts)),
                                              ("RSSSF", (pagina_rsssf(t) or ("", ""))[1], e["rs"] or [], pub_rs)):
                if not linhas:
                    continue
                erro = []
                for x in linhas:
                    c = calc.get(x["clube"])
                    pub = f_pub(x)
                    meu = (c[:6] + [c[6] + c[7] + ajuste.get(x["clube"], 0)]) if c else None
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
            ordem_tb = [x["clube"] for x in tb["ativos"]]
            crits = ("media", "saldo", "confronto") if ano_inicio(t) < 1962 else ("saldo", "confronto", "media")
            so_tb = {c: calc[c] for c in ordem_tb}
            aj_tb = {x["clube"]: x["ajuste"] or 0 for x in tb["ativos"]}
            tent = {cr: ordenar(so_tb, aj_tb, cr, e["jogos"], pts) for cr in crits}
            ok = [cr for cr, o in tent.items() if o == ordem_tb]
            cr = ok[0] if ok else min(tent, key=lambda q: sum(a != b for a, b in zip(tent[q], ordem_tb)))
            if not ok:
                d_ = [c for c, d in zip(ordem_tb, tent[cr]) if c != d]
                ocorr[t].append(f"nenhum critério calculado reproduz a ordem oficial{rot}; o mais próximo ({cr}) difere em "
                                f"{len(d_)} posições (ex.: {d_[:2]})")
            criterios[(t, id(e))] = (cr, bool(ok))
            e["criterio"] = cr
            n_esp = len(tb["ativos"]) * (len(tb["ativos"]) - 1)
            if len(e["jogos"]) != n_esp:
                ocorr[t].append(f"{len(e['jogos'])} jogos{rot} para {len(tb['ativos'])} clubes (esperados {n_esp})")

        # ---- classificação final
        ordem = est["ordem"] or [x["clube"] for x in etapas[0]["tb"]["ativos"]]
        todos = [j for j in jogos if not j["fase"].startswith("Desempate")]
        if est["numeros"] == "publicados":   # Norgesserien: o grupo pela tabela, mais o mata-mata
            numeros = defaultdict(lambda: [0] * 8)
            ko = calcular([j for j in todos if j["fase"] != "Grupos"], pts)
            for c in set(publicados) | set(ko):
                q = publicados.get(c, [0] * 6)
                k_ = ko.get(c, [0] * 8)
                numeros[c] = [q[i] + k_[i] for i in range(6)] + [pts[0] * q[1] + pts[1] * q[2] + k_[6], 0]
        else:
            numeros = calcular(todos, pts)
        prox = TEMPORADAS[TEMPORADAS.index(t) + 1] if t != TEMPORADAS[-1] else "2026"
        if t in NORGESSERIEN:   # liga reorganizada a cada vez: quem caiu pela marca da tabela
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
            if est["numeros"] == "publicados":
                obs.append("números do grupo pela tabela publicada (sem os jogos), mais os do mata-mata")
            if notas_tb.get(c):
                obs.append(notas_tb[c])
            aj = ajuste.get(c, 0) + b
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
                "gols_texto": None, "observacao": obs, "arbitro": None})
            gols_ano += j["gm"] + j["gv"]
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
        if era_ogol and jogos and all(j["rodada"] for j in jogos):
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

        # ---- edição, fases, conferência
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        obs_ed = [x for x in (
            f"punições: {pun}" if pun else "",
            "empate decidido nos pênaltis: 2 pontos ao vencedor e 1 ao perdedor (o ponto a mais em ajuste_pontos)"
            if t in PENALTIS else "",
            "liga de um ano e meio, na passagem para o calendário de ano civil" if t == "1961/62" else "",
        ) if x]
        tab["edicoes"].append({
            "temporada": t, "ano_inicio": ano_inicio(t), "ano_fim": ano_fim(t), "nome_oficial": nome_oficial(t),
            "num_clubes": len(ordem), "pontos_vitoria": pts[0], "pontos_empate": None, "pontos_derrota": None,
            "formato": est["formato"], "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(ordem[1]),
            "co_campeao": None,
            "fontes": ("Wikipédia" + (" + Wikipédia em norueguês" if t in NORGESSERIEN else "") if not era_ogol else
                       "ogol + Wikipédia" + (" + RSSSF" if pagina_rsssf(t) else "") + (" + football-data" if t in fd else "")
                       + (" + ESPN" if t in espn else "")),
            "observacao": "; ".join(obs_ed) or None, "oficial": None})
        crit_txt = {"saldo": "pontos, saldo de gols", "media": "pontos, média de gols (goal average)",
                    "confronto": "pontos, confronto direto, saldo de gols"}
        fases_ed = {}
        for e in etapas:
            if e["fase"] not in fases_ed:
                n_g = sum(1 for x in etapas if x["fase"] == e["fase"])
                fases_ed[e["fase"]] = {"temporada": t, "fase": e["fase"], "tipo": "liga" if e["fase"] == "Liga" else "grupos",
                                       "num_grupos": None if e["fase"] == "Liga" else n_g, "formato_serie": "pontos_corridos",
                                       "criterio": crit_txt[e.get("criterio", "saldo")] +
                                       ("; empate decidido nos pênaltis" if t in PENALTIS else "")}
        for f in dict.fromkeys(j["fase"] for j in jogos):
            if f in fases_ed:
                continue
            ida_volta = f in ("Preliminar", "Quartas de final") or (f == "Final" and sum(j["fase"] == "Final" for j in jogos) == 2)
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
    tab["paises"] = [{"codigo": "NOR", "nome": "Noruega", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, criterios, mapa_espn)


def relatorio(linhas, ocorr, tab, criterios, mapa_espn) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"] or 0) + int(x["gols_visitante"] or 0) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Norueguês (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/nor-1/importar.py`. Pacote em `data/coleta/nor-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1937/38 a 2025: os 79 títulos de liga que a federação reconhece (Norgesserien, "
        "Hovedserien, 1. divisjon, Tippeligaen e Eliteserien).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor, {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- Wikipédia (en): tabela de cada fase (ordem oficial, punições), matriz de resultados (base dos jogos de 1948/49 a "
        "1960/61, conferência depois), mata-mata da Norgesserien e finais da Hovedserien;",
        "- Wikipédia (no): a matriz do único grupo da Norgesserien que tem os jogos (Distrito V, grupo B);",
        "- ogol (zerozero): base dos jogos desde 1961/62, com data, hora e rodada; calendários em `data/cache/ogol-nor-1/`;",
        "- RSSSF: página de cada temporada desde 1998 (tabela, placares e autores dos gols de 1999 a 2005), lista de "
        "campeões e de artilheiros;",
        "- football-data: placar e hora desde 2012;",
        f"- ESPN (liga `nor.1`): estádio, público, gols e cartões nas temporadas que ela cobre ({len(mapa_espn)} clubes casados "
        "por votação, pela data e pelo placar).", "",
        "**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a "
        "oficial (Wikipédia; na Norgesserien, o mata-mata e depois a posição no grupo; na Hovedserien, a final e depois a "
        "posição no grupo). Pontos 2-1-0 até 1986 e 3-1-0 depois; em 1987, o empate ia para os pênaltis (2 pontos ao "
        "vencedor, 1 ao perdedor). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (na Norgesserien, a "
        "marca da tabela).", "",
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
        "- Cadastro em `coleta/comum-europa/clubes_nor.py`, pela linhagem do clube (o alvo do link da Wikipédia, seguindo os "
        "redirecionamentos). O clube e o departamento de futebol com artigos separados contam como um (Vålerengens IF e "
        "Vålerenga Fotball, como a RSSSF; Mjøndalen, Sogndal, Ranheim, Strømsgodset, Kongsvinger, Lyn). Clubes refundados "
        "com artigo próprio ficam separados: Sarpsborg FK x Sarpsborg 08, Kristiansund FK x Kristiansund BK, Sandefjord BK "
        "x Sandefjord Fotball (o ogol usa um código só para os dois).",
        "- Os nomes de cada fonte, com as temporadas, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Jogos dos grupos da Norgesserien** (1937/38, 1938/39, 1947/48), fora o Distrito V, grupo B: nenhuma fonte em lote "
        "traz; ficam as tabelas publicadas.",
        "- **Datas e rodadas de 1937/38 a 1960/61** (só as matrizes e as tabelas do mata-mata).",
        "- **Autores dos gols e cartões** antes da ESPN, fora as páginas da RSSSF de 1999 a 2005.",
        "- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
