"""Monta o pacote do campeonato polonês (pol-1), 1921 a 2025/26, e o relatório docs/coleta/pol-1.md.

Três eras, três bases de jogos:
- torneios entre os campeões regionais (1921-1926, 1946 e 1947): a matriz da RSSSF (polhist.html), com o clube de cada
  linha casado pelos números com a tabela da Wikipédia (que traz o link do clube); as finais, o desempate de 1925 e o
  mata-mata de 1946 pelas fichas da Wikipédia; o grupo final de 1926 não tem os jogos em nenhuma fonte (fica a tabela);
- liga de 1927 a 1962: a matriz de resultados da Wikipédia (en), sem data nem rodada, conferida jogo a jogo com a matriz
  da RSSSF; o clube pelo alvo do link (clubes_pol.LINKS). Final de 1952 e play-offs de classificação de 1962 pela RSSSF;
- de 1962/63 em diante: o calendário do ogol (data, hora e rodada), o clube pelo código do ogol; conferido com a matriz da
  Wikipédia, a tabela e a matriz da RSSSF (até 2000/01) e o football-data (desde 2012/13).
Tabelas publicadas: Wikipédia (ordem oficial, punições, bônus) e RSSSF (polhist.html, até 2000/01). Campeões: RSSSF
(polchamp.html); artilheiros: RSSSF (poltops.html, com a grafia de polhist.html quando ela traz o nome).

Pontos: 2-1-0 até 1994/95, 3-1-0 depois. De 1986/87 a 1989/90, +1 ponto pela vitória por 3 gols ou mais e -1 pela derrota
por 3 ou mais (em `ajuste_pontos`). De 2013/14 a 2019/20, os pontos da fase regular divididos por dois antes dos grupos
(também em `ajuste_pontos`, pela tabela da Wikipédia).

Escopo (Guilherme, 25/11/2026): ver coleta/pol-1/edicoes.py.

Uso: python coleta/pol-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
sys.path.append(str(AQUI.parent / "gre-1"))   # leitor das fichas da Wikipédia, no fim da busca
import clubes_pol as clubes  # noqa: E402
import notas_wiki  # noqa: E402
import rsssf_pol as rsssf  # noqa: E402
import wiki_gre  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, TORNEIOS, ano_fim, ano_inicio, nome_oficial, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from wiki_tabela import _fecha, _num, limpar  # noqa: E402
from wiki_tabela import resultados as wiki_resultados  # noqa: E402
from wiki_tabela import tabelas as wiki_tabelas  # noqa: E402

PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "pol-1.md"
URL_HIST = "https://www.rsssf.org/tablesp/polhist.html"
DOIS, TRES = (2, 1, 0), (3, 1, 0)

# torneios: (índice da seção da RSSSF, fase, grupo) e as fichas da Wikipédia (título da seção -> fase, grupo)
ESPEC_TORNEIO = {
    "1921": {"grupos": [(0, "Grupo final", None)]},
    "1922": {"grupos": [(0, "Grupos", "Grupo Sul"), (1, "Grupos", "Grupo Norte")], "final_rsssf": 2,
             "matriz_de": {0: 1, 1: 0}},   # a RSSSF trocou as matrizes dos dois grupos
    "1923": {"grupos": [(0, "Grupos", "Grupo Oeste"), (1, "Grupos", "Grupo Leste")],
             "fichas": {"Final matches": ("Final", None)}},
    "1925": {"grupos": [(0, "Grupos", "Grupo Norte"), (1, "Grupos", "Grupo Leste"), (2, "Grupos", "Grupo Sul"),
                        (3, "Grupo final", None)],
             "fichas": {"Southern Group": ("Desempate", "Grupo Sul")}},
    "1926": {"grupos": [(0, "Grupos", "Grupo Oeste"), (1, "Grupos", "Grupo Sul"), (2, "Grupos", "Grupo Norte"),
                        (3, "Grupo final", None)]},
    "1946": {"grupos": [(3, "Grupo final", None)],
             "fichas": {"Qualifying round": ("Preliminar", None), "First round": ("Oitavas de final", None),
                        "Second round": ("Quartas de final", None)}},
    "1947": {"grupos": [(0, "Grupos", "Grupo 1"), (1, "Grupos", "Grupo 2"), (2, "Grupos", "Grupo 3"),
                        (3, "Grupo final", None)]},
}
FORMATO_TORNEIO = {
    "1921": "torneio em turno e returno entre 5 campeões regionais",
    "1922": "dois grupos de 4 campeões regionais (turno e returno) e final de ida e volta entre os primeiros",
    "1923": "dois grupos de 4 campeões regionais (turno e returno) e final de ida e volta entre os primeiros, com jogo extra",
    "1925": "três grupos de 3 campeões regionais (turno e returno) e grupo final entre os primeiros",
    "1926": "três grupos de 3 campeões regionais (turno e returno) e grupo final entre os primeiros",
    "1946": "mata-mata em jogo único entre 18 campeões regionais (preliminar, oitavas e quartas de final) e grupo final "
            "de 4 (turno e returno)",
    "1947": "três grupos de campeões regionais (turno e returno) e grupo final entre os primeiros",
}
# ordem das fases na edição
ORDEM_FASES = {"Liga": 0, "Fase regular": 0, "Grupos": 1, "Preliminar": 1, "Oitavas de final": 2, "Quartas de final": 3,
               "Desempate": 4, "Grupo do título": 5, "Grupo de rebaixamento": 6, "Play-off de classificação": 7,
               "Grupo final": 8, "Final": 8, "Desempate da final": 9}
# temporadas da liga com mais de uma tabela: (fase, grupo) de cada matriz, na ordem do artigo
ESPEC_LIGA = {"1933": [("Grupos", "Grupo Leste"), ("Grupos", "Grupo Oeste"), ("Grupo do título", None),
                       ("Grupo de rebaixamento", None)],
              "1952": [("Grupos", "Grupo 1"), ("Grupos", "Grupo 2")],
              "1962": [("Grupos", "Grupo A"), ("Grupos", "Grupo B")]}
# jogos que nenhuma matriz tem: temporada -> [(fase, grupo, data, mandante, visitante, gols, gols, observação)]
EXTRAS = {"1952": [("Final", None, "1952-11-13", "Ruch Chorzów", "Polonia Bytom", 7, 0,
                    "final entre os primeiros dos grupos, 1º jogo; a RSSSF anota que um primeiro jogo (2-2) foi "
                    "interrompido aos 80 minutos pelas condições do campo"),
                   ("Final", None, "1952-11-16", "Polonia Bytom", "Ruch Chorzów", 0, 0,
                    "final entre os primeiros dos grupos, 2º jogo")]}
# jogo extra entre empatados em pontos: temporada -> [(data, mandante, visitante, gols, gols, observação)]
DESEMPATES = {"1948": [("1948-12-05", "Cracovia", "Wisła Cracóvia", 3, 1,
                        "jogo extra pelo título: Cracovia e Wisła terminaram empatadas em pontos (38) (RSSSF e Wikipédia)")]}
# jogos anulados (ficam fora do pacote): (temporada, mandante, visitante) -> motivo
ANULADOS = {
    ("1992/93", "ŁKS Łódź", "Olimpia Poznań"): "7-1 no campo, anulado pela federação por suspeita de manipulação",
    ("1992/93", "Wisła Cracóvia", "Legia Varsóvia"): "0-6 no campo, anulado pela federação por suspeita de manipulação",
}
# jogo decidido fora de campo ("DA" no ogol, sem placar) com o placar dado aqui: (temporada, mandante, visitante) -> ...
DECIDIDOS: dict[tuple, tuple] = {}
# título fora da ordem da liga: temporada -> (clube, motivo)
CAMPEAO_FORA = {"1951": ("Ruch Chorzów", "o título polonês foi para o vencedor da Copa da Polônia de 1950/51 (decisão da "
                                         "federação antes da temporada): o Ruch, 6º na liga; a Wisła venceu a liga")}
EXPLICACOES = {
    "1922": ["a Wikipédia polonesa dá Warta 23:6, Pogoń 37:6 e Ruch 6:38 (gols), como os jogos; a Wikipédia em inglês e a "
             "RSSSF dão 33:6, 37:8 e 8:38 (https://pl.wikipedia.org/wiki/Mistrzostwa_Polski_w_piłce_nożnej_(1922))"],
}
# clube que não está na temporada seguinte sem ter caído: (temporada, clube) -> motivo
NAO_REBAIXADOS = {
    ("1994/95", "Olimpia Poznań"): "fundiu-se com o Lechia Gdańsk (Olimpia/Lechia Gdańsk, que ficou com a vaga em 1995/96)",
    ("1994/95", "Sokół Pniewy"): "mudou-se para Tychy (Sokół Tychy, hoje GKS Tychy, que ficou com a vaga em 1995/96)",
    ("2005/06", "Amica Wronki"): "fundiu-se com o Lech Poznań depois da temporada (nota da tabela da Wikipédia)",
    ("2007/08", "Dyskobolia"): "fundiu-se com a Polonia Varsóvia, que ficou com a vaga em 2008/09",
}
# derrota para os dois (jogo não disputado, W.O. contra os dois): temporada -> [(mandante, visitante, motivo)]
DERROTA_DOIS = {"1934": [("Garbarnia Cracóvia", "ŁKS Łódź", "jogo não disputado; W.O. contra os dois (RSSSF)")]}

COMPETICAO = {
    "slug": "pol-1", "nome": "Campeonato Polonês", "nome_curto": "Polonês", "tipo": "liga", "nivel": 1,
    "pais": "POL", "pais_nome": "Polônia", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Polonês", "menu_painel": "Polônia · 1ª divisão",
    "do_painel": "do Campeonato Polonês", "o_painel": "o Campeonato Polonês",
    "observacao": "Os 98 títulos poloneses que a federação (PZPN) reconhece: torneios entre os campeões regionais (1921-1926, "
                  "1946 e 1947) e a liga (Liga, I liga e Ekstraklasa) de 1927 a 1938 e desde 1948; 1962 só com a "
                  "primavera, na passagem para o calendário de outono a primavera. Não inclui 1920 (abandonado), 1924 (não "
                  "disputado), 1939 (interrompido pela guerra) nem as ligas municipais da guerra.",
}


def faixa(rotulos) -> str:
    a = sorted(rotulos, key=TEMPORADAS_ORDEM.get)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else a[0]


TEMPORADAS_ORDEM = {t: i for i, t in enumerate(TEMPORADAS + ["2026/27"])}


def pontos(t: str) -> tuple[int, int, int]:
    return DOIS if ano_inicio(t) < 1995 else TRES


def caixa_alta(s: str) -> bool:
    letras = [c for c in s if c.isalpha()]
    return bool(letras) and all(c.isupper() for c in letras)


# ------------------------------------------------------------------ fontes
def texto_wiki(t: str) -> str:
    return "\n".join(x.read_text(encoding="utf-8") for x in sorted((DADOS / "wikipedia").glob(f"{wiki_titulo(t)}*.wiki")))


def url_wiki(t: str) -> str:
    return f"https://en.wikipedia.org/wiki/{wiki_titulo(t).replace(' ', '_')}"


# notas das células da matriz da Wikipédia (1927-1962), traduzidas
NOTAS_CELULA = {
    "Match awarded.": "resultado decidido fora de campo",
    "The match between Pogoń Lwów and Wisła Kraków was stopped after 85 minutes and was scored 3–0.":
        "jogo interrompido aos 85 minutos; resultado dado como 3-0",
    "Strzelec Siedlce withdrew in August 1934. The remaining ten games were rated 0:3 for the opponents.":
        "o Strzelec Siedlce desistiu em agosto de 1934; os dez jogos restantes foram dados como 0-3 para os adversários",
    "The match between Legia Warsaw and Pogoń Lwów was stopped at the score of 0–1 because a eliminated player refused to "
    "leave the field. It was scored 0–3.": "jogo interrompido com 0-1 porque um jogador expulso se recusou a sair de campo; "
                                           "resultado dado como 0-3",
    "The match between Śląsk Świętochłowice and Polonia Warsaw (originally finished 2–0) was rated with 3–0 win for home "
    "team.": "2-0 no campo; resultado dado como 3-0 para o mandante",
    "The match Garbarnia Kraków and Śląsk Świętochłowice was rated with 3–0 win for home team.":
        "resultado dado como 3-0 para o mandante",
    "The match between ŁKS Łódź and Polonia Bytom was stopped after 58 minutes due to riots and the score was 0–3.":
        "jogo interrompido aos 58 minutos por tumulto; resultado dado como 0-3",
}
AWD = re.compile(r"(?i)walk ?-?over|\bw\.?\s?o\b|awarded|rated|verified|forfeit")


def ler_wiki(t: str) -> dict:
    """Tabelas (clube pelo link, bônus das colunas OT somado), matrizes (blocos, com as notas das células) e fichas."""
    txt = texto_wiki(t)
    cod, vis = {}, {}
    for c, alvo, nome in re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", txt):
        cod.setdefault(c, alvo.strip())
        vis.setdefault((nome or alvo).strip(), alvo.strip())

    def ident(alvo: str | None, nome: str) -> str:
        nome = (nome or "").replace("↑", "").strip()
        c = clubes.link(alvo) if alvo else None
        c = c or clubes.link(vis.get(nome)) or clubes.VISIVEIS.get(nome)
        if c is None:
            raise SystemExit(f"{t}: clube da Wikipédia sem cadastro: {nome} ({alvo})")
        return c

    tbs = []
    for tb in wiki_tabelas(txt):
        p = tb["params"]
        for x in tb["times"]:
            m = re.match(r"\s*\[\[([^\]|]+)", x["nome_wiki"])
            x["nome"] = x["nome"].replace("↑", "").strip()
            x["clube"] = ident(m.group(1) if m else cod.get(x["codigo"]), x["nome"])
            ow, ol = _num(p.get(f"OTwin_{x['codigo']}")), _num(p.get(f"OTloss_{x['codigo']}"))
            x["bonus"] = 0
            if ow is not None or ol is not None:
                x["vitorias"] = (x["vitorias"] or 0) + (ow or 0)
                x["derrotas"] = (x["derrotas"] or 0) + (ol or 0)
                x["bonus"] = (ow or 0) - (ol or 0)
            x["ativo"] = x["vitorias"] is not None
        tb["bonus"] = any(k.startswith("OTwin_") for k in p)
        tb["ativos"] = [x for x in tb["times"] if x["ativo"]]
        tbs.append(tb)
    blocos = []
    tm = re.sub(r"(?i)#invoke:\s*sports table", "#invoke:sports results", txt)
    for mm in re.finditer(r"\{\{\s*#invoke:\s*sports results\s*\|", tm, flags=re.I):
        bloco = tm[mm.start():_fecha(tm, mm.start())]
        limpo = re.sub(r"\{\{\s*(?:efn|refn|sfn|note|cref|ref label|abbr)[^{}]*\}\}", "", bloco, flags=re.I)
        rr = wiki_resultados(limpo)
        if not rr:
            continue
        g = rr[0]
        alvos = dict(re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)", bloco))
        notas = {}
        for a, b, v in re.findall(r"\|\s*match_([^_|=\s]+)_([^_|=\s]+)_note\s*=([^\n]*)", bloco):
            notas[(a, b)] = re.split(r"\|\s*[\w ]+=", v)[0].strip()

        def nota(a, b):
            n = notas.get((a, b), "")
            k = tuple(n.split("_"))
            if len(k) == 2 and k in notas:
                n = notas[k]
            return limpar(n) or None
        jogos = []
        for (a, b), pl in g["jogos"].items():
            ma = ident(alvos.get(a) or cod.get(a), g["nomes"].get(a, a))
            mb = ident(alvos.get(b) or cod.get(b), g["nomes"].get(b, b))
            for gm, gv in pl:
                jogos.append({"m": ma, "v": mb, "nm": g["nomes"].get(a, a), "nv": g["nomes"].get(b, b), "gm": gm, "gv": gv,
                              "nota": nota(a, b)})
        blocos.append({"clubes": {c for j in jogos for c in (j["m"], j["v"])}, "jogos": jogos})
    fichas = [f for f in wiki_gre.ler(txt)["jogos"] if f["fonte"] != "matriz"]
    for f in fichas:
        f["m"], f["v"] = ident(f["tm"], f["nm"]), ident(f["tv"], f["nv"])
    return {"tbs": tbs, "blocos": blocos, "fichas": fichas, "ident": ident}


def carregar_ogol(t: str) -> list[dict]:
    res = []
    for o in json.loads((DADOS / "ogol" / f"pol1_{t.replace('/', '-')}.json").read_text(encoding="utf-8")):
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
                    "etapa": o["fase"] or ""})
    return res


def football_data() -> dict[str, list[dict]]:
    res = defaultdict(list)
    with open(DADOS / "football-data" / "POL.csv", encoding="utf-8-sig") as f:
        for x in csv.DictReader(f):
            if not x.get("HG"):
                continue
            a, b = x["Season"].split("/")
            d, mth, y = x["Date"].split("/")
            res[f"{a}/{b[-2:]}"].append({"data": f"{y if len(y) == 4 else '20' + y}-{mth}-{d}", "m": clubes.esd(x["Home"]),
                                         "v": clubes.esd(x["Away"]), "nm": x["Home"], "nv": x["Away"],
                                         "gm": int(x["HG"]), "gv": int(x["AG"])})
    return res


def campeoes_rsssf() -> dict[str, str]:
    t = rsssf.texto(DADOS / "rsssf" / "polchamp.html")
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^(\d{4}(?:/\d{2})?)\s+([^\s\d\[].*?)\s*(?:\[\d+\])?\s*$", t, re.M)}


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pts, bonus: bool = False) -> dict[str, list[int]]:
    """J V E D GP GC Pts Bônus (os pontos sem o bônus)."""
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
            if bonus and abs(gp - gc) >= 3:
                x[7] += 1 if gp > gc else -1
    return t


def ordenar(t, ajuste, criterio, jogos, pts, bonus=False) -> list[str]:
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
            mini = calcular([j for j in jogos if j["m"] in g and j["v"] in g], pts, bonus)
            g.sort(key=lambda c: (-(mini[c][6] + mini[c][7]), -(mini[c][4] - mini[c][5]), *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def pub_wiki(x: dict, pts) -> list[int]:
    v, e, d = x["vitorias"] or 0, x["empates"] or 0, x["derrotas"] or 0
    return [v + e + d, v, e, d, x["gols_pro"], x["gols_contra"], pts[0] * v + pts[1] * e + (x["ajuste"] or 0) + x["bonus"]]


def pub_rs(x: dict) -> list[int]:
    return [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]


def casar_rs(rs: list[dict], tb: dict, pts) -> list[dict] | None:
    """Linhas da RSSSF com o clube da linha da Wikipédia: pelos números iguais (V, E, D, GP, GC) quando só uma linha os
    tem, depois pelo nome, depois pela posição; None se o número de linhas não bate."""
    ativos = tb["ativos"]
    if len(rs) != len(ativos):
        return None
    par: dict[int, dict] = {}
    livres = list(ativos)
    for i, x in enumerate(rs):
        cand = [y for y in livres if pub_wiki(y, pts)[1:6] == pub_rs(x)[1:6]]
        if len(cand) == 1 and sum(pub_rs(z)[1:6] == pub_rs(x)[1:6] for z in rs) == 1:
            par[i] = cand[0]
            livres.remove(cand[0])
    for i, x in enumerate(rs):
        if i in par:
            continue
        y = next((y for y in livres if y["clube"] == clubes.esd(x["nome"])), None)
        if y is None and ativos[i] in livres:
            y = ativos[i]
        if y is None and len(livres) == 1:
            y = livres[0]
        if y is None:
            return None
        par[i] = y
        livres.remove(y)
    return [dict(x, clube=par[i]["clube"]) for i, x in enumerate(rs)]


def melhor_rs(secs: list[dict], tb: dict, pts, usadas: set) -> list[dict] | None:
    melhor, nota = None, -1
    for k, s in enumerate(secs):
        if k in usadas or len(s["tabela"]) != len(tb["ativos"]):
            continue
        r = casar_rs(s["tabela"], tb, pts)
        if r is None:
            continue
        n = sum(pub_rs(x)[1:6] == pub_wiki(y, pts)[1:6] for x, y in zip(s["tabela"], tb["ativos"]))
        if n > nota:
            melhor, nota = (k, r), n
    if melhor is None:
        return None
    usadas.add(melhor[0])
    return melhor[1]


def jogos_rs(linhas: list[dict], wo: int, fase: str, grupo: str | None) -> list[dict]:
    res = []
    for g in rsssf.jogos_da_matriz(linhas):
        gm, gv = (wo, 0) if g["wo"] and g["gm"] > g["gv"] else (0, wo) if g["wo"] else (g["gm"], g["gv"])
        res.append({"m": linhas[g["i"]]["clube"], "v": linhas[g["k"]]["clube"], "nm": linhas[g["i"]]["nome"],
                    "nv": linhas[g["k"]]["nome"], "gm": gm, "gv": gv, "fase": fase, "grupo": grupo, "rodada": None,
                    "data": None, "hora": None, "fonte": "RSSSF (matriz)", "fonte_id": None,
                    "especial": "awd" if g["wo"] else None,
                    "obs": f"W.O. ({gm}-{gv}, placar da tabela da RSSSF)" if g["wo"] else None})
    return res


def da_ficha(f: dict, fase: str, grupo: str | None, obs: str | None = None) -> dict:
    return {"m": f["m"], "v": f["v"], "nm": f["nm"], "nv": f["nv"], "gm": f["gm"], "gv": f["gv"], "fase": fase, "grupo": grupo,
            "rodada": None, "data": f["data"], "hora": None, "fonte": "Wikipédia (ficha)", "fonte_id": None, "especial": None,
            "obs": obs}


def da_matriz(j: dict, fase: str, grupo: str | None) -> dict:
    x = {"m": j["m"], "v": j["v"], "nm": j["nm"], "nv": j["nv"], "gm": j["gm"], "gv": j["gv"], "fase": fase, "grupo": grupo,
         "rodada": None, "data": None, "hora": None, "fonte": "Wikipédia (matriz)", "fonte_id": None, "especial": None,
         "obs": None}
    if j["nota"]:
        if j["nota"] not in NOTAS_CELULA:
            raise SystemExit(f"nota da matriz da Wikipédia sem tradução: {j['nota']!r}")
        x["especial"] = "awd"   # todas as notas das matrizes são de resultado dado fora de campo
        x["obs"] = NOTAS_CELULA[j["nota"]] + " (nota da matriz da Wikipédia)"
    return x


# ------------------------------------------------------------------ eras
def torneio(t: str, W: dict, secs: list[dict], pts, ocorr: list[str]) -> dict:
    esp = ESPEC_TORNEIO[t]
    etapas, jogos, livres = [], [], list(W["tbs"])
    for idx, fase, grupo in esp["grupos"]:
        s = secs[idx]
        cand = [tb for tb in livres if len(tb["ativos"]) == len(s["tabela"]) and casar_rs(s["tabela"], tb, pts)]
        tb = max(cand, key=lambda tb: sum(pub_rs(x)[1:6] == pub_wiki(y, pts)[1:6] for x, y in zip(s["tabela"], tb["ativos"])),
                 default=None)
        if tb is None:
            raise SystemExit(f"{t}: tabela da RSSSF ({s['titulo']}) sem a da Wikipédia")
        livres.remove(tb)
        linhas = casar_rs(s["tabela"], tb, pts)
        if idx in esp.get("matriz_de", {}):
            outra = secs[esp["matriz_de"][idx]]["tabela"]
            linhas = [dict(x, celulas=y["celulas"]) for x, y in zip(linhas, outra)]
            ocorr.append(f"{grupo}: a matriz da RSSSF está trocada com a do outro grupo (a nota dela sobre Ruch x Cracovia, 2-8 e "
                         f"0-7, está na matriz do outro grupo); os jogos vêm da matriz certa, linha a linha pela posição; com "
                         f"isso, os números fecham com as tabelas da Wikipédia polonesa")
        js = []
        if any(x["celulas"] for x in linhas):
            def dist(js_):
                c = calcular(js_, pts)
                return sum(abs(c[x["clube"]][q] - pub_rs(x)[q]) for x in linhas for q in (4, 5))
            js = min((jogos_rs(linhas, wo, fase, grupo) for wo in (3, 5)), key=dist)
        etapas.append({"fase": fase, "grupo": grupo, "tb": tb, "rs": linhas, "jogos": js, "base": [], "sem_jogos": not js})
        jogos += js
    for f in W["fichas"]:
        sec = f["secao"][-1] if f["secao"] else ""
        if sec not in esp.get("fichas", {}):
            continue
        fase, grupo = esp["fichas"][sec]
        obs = None
        if fase == "Desempate":
            obs = f"jogo extra{(' ' + f['extra']) if f['extra'] else ''} (campo neutro): empate em pontos no {grupo}"
            obs = obs.replace("in Lwów", "em Lwów")
        j = da_ficha(f, fase, grupo, obs)
        jogos.append(j)
    if t == "1923":   # a final terminou com uma vitória para cada lado: o 3º jogo decidiu
        finais = [j for j in jogos if j["fase"] == "Final"]
        finais[2]["fase"] = "Desempate da final"
        finais[2]["obs"] = "3º jogo da final: Pogoń e Wisła venceram um jogo cada"
    if "final_rsssf" in esp:
        for k, x in enumerate(secs[esp["final_rsssf"]]["jogos"], 1):
            m, v = clubes.esd(x["m"]), clubes.esd(x["v"])
            jogos.append({"m": m, "v": v, "nm": x["m"], "nv": x["v"], "gm": x["gm"], "gv": x["gv"], "fase": "Final", "grupo": None,
                          "rodada": None, "data": None, "hora": None, "fonte": "RSSSF", "fonte_id": None, "especial": None,
                          "obs": f"final entre os primeiros dos grupos, {k}º jogo"})
    # ordem final: o grupo final (ou a final), depois os outros pela posição no grupo
    ordem = []
    fin = next((e for e in etapas if e["fase"] == "Grupo final"), None)
    if fin:
        ordem = [x["clube"] for x in fin["tb"]["ativos"]]
    finais = [j for j in jogos if j["fase"] in ("Final", "Desempate da final")]
    if finais:
        des = [j for j in finais if j["fase"] == "Desempate da final"]
        tot = calcular(finais, pts)
        if des:
            d = des[0]
            venc = d["m"] if d["gm"] > d["gv"] else d["v"]
        else:
            venc = max(tot, key=lambda c: (tot[c][6], tot[c][4] - tot[c][5]))
        ordem = [venc, next(c for c in tot if c != venc)]
    ko = {"Preliminar": 3, "Oitavas de final": 2, "Quartas de final": 1}
    grupos = [e for e in etapas if e["fase"] == "Grupos"]
    resto = []
    for e in grupos:
        calc = calcular(e["jogos"], pts)
        for x in e["tb"]["ativos"]:
            if x["clube"] not in ordem:
                p = calc[x["clube"]] if e["jogos"] else pub_wiki(x, pts) + [0]
                resto.append((x["posicao"], -(p[6] + p[7] if len(p) > 7 else p[6]), -(p[4] - p[5]), -p[4], x["clube"]))
    ordem += [c for *_, c in sorted(resto)]
    perdedores = []
    for j in jogos:
        if j["fase"] in ko:
            perd = j["v"] if j["gm"] > j["gv"] else j["m"]
            perdedores.append((-ko[j["fase"]], len(perdedores), perd))
    ordem += [c for *_, c in sorted(perdedores, key=lambda x: (-x[0], x[1])) if c not in ordem]
    return {"etapas": etapas, "jogos": jogos, "ordem": ordem, "formato": FORMATO_TORNEIO[t],
            "fonte_ordem": "Wikipédia e RSSSF (grupo final ou final, depois a posição no grupo" +
                           ("; no mata-mata, a fase em que caiu)" if t == "1946" else ")"),
            "numeros": "todos"}


def liga_antiga(t: str, W: dict, secs: list[dict], pts, ocorr: list[str]) -> dict:
    nomes = ESPEC_LIGA.get(t, [("Liga", None)])
    etapas, livres, usadas = [], [tb for tb in W["tbs"] if tb["ativos"]], set()
    for b in W["blocos"]:
        tb = next((tb for tb in livres if {x["clube"] for x in tb["ativos"]} == b["clubes"]), None)
        if tb is None:
            ocorr.append(f"matriz da Wikipédia sem tabela de mesmos clubes, fora do pacote: {sorted(b['clubes'])}")
            continue
        livres.remove(tb)
        fase, grupo = nomes[len(etapas)]
        js = [da_matriz(j, fase, grupo) for j in b["jogos"]]
        rs = melhor_rs(secs, tb, pts, usadas)
        etapas.append({"fase": fase, "grupo": grupo, "tb": tb, "rs": rs, "jogos": js, "base": [], "sem_jogos": False})
    for tb in livres:
        ocorr.append(f"tabela da Wikipédia sem matriz (play-off contra clubes da 2ª divisão), fora do pacote: "
                     f"{[x['clube'] for x in tb['ativos']]}")
    if t == "1933":   # grupos finais: a conferência vê se os pontos da 1ª fase contam (não contam)
        primeira = etapas[0]["jogos"] + etapas[1]["jogos"]
        for e in etapas[2:]:
            cs = {x["clube"] for x in e["tb"]["ativos"]}
            e["base"] = [j for j in primeira if j["m"] in cs or j["v"] in cs]
    # matriz da RSSSF: conferência jogo a jogo; o placar dela fica quando só ele fecha com as tabelas
    for e in etapas:
        if not e["rs"] or not all(len(x["celulas"]) == len(e["rs"]) for x in e["rs"]):
            if e["rs"]:
                ocorr.append(f"sem a matriz da RSSSF{(' do ' + e['grupo']) if e['grupo'] else ''} para conferir os jogos")
            continue
        mz = {}
        for g in rsssf.jogos_da_matriz(e["rs"]):
            mz[(e["rs"][g["i"]]["clube"], e["rs"][g["k"]]["clube"])] = (g["gm"], g["gv"], g["wo"])
        pubs = [{x["clube"]: pub_wiki(x, pts)[:6] for x in e["tb"]["ativos"]}, {x["clube"]: pub_rs(x)[:6] for x in e["rs"]}]

        def distancia(cs):
            c_ = calcular(e["jogos"], pts)
            return sum(abs(c_[c][q] - p_[c][q]) for p_ in pubs for c in cs for q in range(6))
        for j in e["jogos"]:
            r = mz.get((j["m"], j["v"]))
            if r is None or (r[0], r[1]) == (j["gm"], j["gv"]) or r[2] or j["especial"]:
                continue
            antes = distancia((j["m"], j["v"]))
            velho = (j["gm"], j["gv"])
            j["gm"], j["gv"] = r[0], r[1]
            if distancia((j["m"], j["v"])) < antes:
                j["obs"] = (f"placar da matriz da RSSSF; a da Wikipédia dá {velho[0]}-{velho[1]}, que fecha pior com as "
                            f"tabelas")
                ocorr.append(f"{j['m']} x {j['v']}: fica {r[0]}-{r[1]} (RSSSF); a matriz da Wikipédia dá {velho[0]}-{velho[1]}, "
                             f"que fecha pior com as tabelas")
            else:
                j["gm"], j["gv"] = velho
                ocorr.append(f"{j['m']} x {j['v']}: a matriz da RSSSF dá {r[0]}-{r[1]}; fica {velho[0]}-{velho[1]} (Wikipédia), "
                             f"que fecha melhor ou igual com as tabelas")
    for m, v, motivo in DERROTA_DOIS.get(t, []):
        etapas[0]["jogos"].append({"m": m, "v": v, "nm": m, "nv": v, "gm": None, "gv": None, "fase": etapas[0]["fase"],
                                   "grupo": None, "rodada": None, "data": None, "hora": None, "fonte": "RSSSF", "fonte_id": None,
                                   "especial": "awd", "obs": f"derrota para os dois: {motivo}", "dois": True})
        ocorr.append(f"{m} x {v}: derrota para os dois ({motivo})")
    jogos = [j for e in etapas for j in e["jogos"]]
    extra = []
    for fase, grupo, data, m, v, gm, gv, obs in EXTRAS.get(t, []):
        extra.append({"m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "fase": fase, "grupo": grupo, "rodada": None,
                      "data": data, "hora": None, "fonte": "RSSSF e Wikipédia", "fonte_id": None, "especial": None, "obs": obs})
    for data, m, v, gm, gv, obs in DESEMPATES.get(t, []):
        extra.append({"m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "fase": "Desempate", "grupo": None, "rodada": None,
                      "data": data, "hora": None, "fonte": "RSSSF e Wikipédia", "fonte_id": None, "especial": None, "obs": obs})
    ordem, fonte_ordem, formato = None, "Wikipédia (ordem oficial)", "pontos corridos (turno e returno)"
    if t == "1962":   # play-offs de classificação: 1º contra 1º, 2º contra 2º...; o vencedor em caixa alta na RSSSF
        pares = {}
        for s in secs:
            if "playoff" not in s["titulo"].lower():
                continue
            for x in s["jogos"]:
                m, v = clubes.esd(x["m"]), clubes.esd(x["v"])
                par = pares.setdefault(frozenset((m, v)), {"jogos": [], "venc": None})
                par["jogos"].append((x, m, v))
                for nome, c in ((x["m"], m), (x["v"], v)):
                    if caixa_alta(nome):
                        par["venc"] = c
        ordem = []
        for k, par in enumerate(pares.values()):
            lugar = 2 * k + 1
            for n, (x, m, v) in enumerate(par["jogos"], 1):
                extra.append({"m": m, "v": v, "nm": x["m"].title(), "nv": x["v"].title(), "gm": x["gm"], "gv": x["gv"],
                              "fase": "Play-off de classificação", "grupo": f"{lugar}º lugar", "rodada": None, "data": None,
                              "hora": None, "fonte": "RSSSF", "fonte_id": None, "especial": None,
                              "obs": f"disputa do {lugar}º lugar, {n}º jogo"})
            venc = par["venc"]
            ordem += [venc, next(c for c in {m for _, m, v in par["jogos"]} | {v for _, m, v in par["jogos"]} if c != venc)]
        fonte_ordem = "RSSSF (play-offs de classificação)"
        formato = "dois grupos de 7 (turno e returno) e play-offs de classificação de ida e volta entre os de mesma posição"
    elif t == "1952":
        tot = calcular(extra, pts)
        venc = max(tot, key=lambda c: (tot[c][6], tot[c][4] - tot[c][5]))
        ordem = [venc, next(c for c in tot if c != venc)]
        resto = []
        for e in etapas:
            calc = calcular(e["jogos"], pts)
            for x in e["tb"]["ativos"]:
                if x["clube"] not in ordem:
                    p = calc[x["clube"]]
                    resto.append((x["posicao"], -p[6], -(p[4] - p[5]), -p[4], x["clube"]))
        ordem += [c for *_, c in sorted(resto)]
        fonte_ordem = "RSSSF e Wikipédia (final entre os primeiros dos grupos; depois a posição no grupo)"
        formato = "dois grupos de 6 (turno e returno) e final de ida e volta entre os primeiros"
    elif t == "1933":
        ordem = [x["clube"] for e in etapas[2:] for x in e["tb"]["ativos"]]
        fonte_ordem = "Wikipédia (grupo do título, depois grupo de rebaixamento)"
        formato = ("dois grupos regionais de 6 (turno e returno), depois grupo do título e grupo de rebaixamento de 6 (turno "
                   "e returno)")
    return {"etapas": etapas, "jogos": jogos + extra, "ordem": ordem, "formato": formato + "; sem datas (só a matriz de "
            "resultados)", "fonte_ordem": fonte_ordem, "numeros": "todos" if t in ("1952", "1962") else None}


def liga_ogol(t: str, W: dict, jogos: list[dict], pts, ocorr: list[str]) -> dict:
    tbs = [tb for tb in W["tbs"] if tb["ativos"]]
    liga = {x["clube"] for tb in tbs for x in tb["ativos"]}
    fora = [j for j in jogos if not {j["m"], j["v"]} <= liga]
    for j in fora:
        ocorr.append(f"jogo com clube de fora da liga, fora do pacote: {j['m']} x {j['v']} ({j['data']}, {j['ogol']['resultado']})")
    jogos = [j for j in jogos if j not in fora]
    for j in list(jogos):
        if (t, j["m"], j["v"]) in ANULADOS:
            ocorr.append(f"{j['m']} x {j['v']} ({j['data']}, {j['gm']}-{j['gv']} no ogol): fora do pacote — "
                         f"{ANULADOS[(t, j['m'], j['v'])]}")
            jogos.remove(j)
    if len(tbs) == 1:
        e = {"fase": "Liga", "grupo": None, "tb": tbs[0], "rs": None, "jogos": jogos, "base": [], "sem_jogos": False}
        return {"etapas": [e], "jogos": jogos, "ordem": None, "formato": "pontos corridos (turno e returno)",
                "fonte_ordem": "Wikipédia (ordem oficial)", "numeros": None}
    regular = [j for j in jogos if j["rodada"]]
    resto = [j for j in jogos if not j["rodada"]]
    etapas = []
    if t == "2001/02":
        fases1 = [("Grupos", "Grupo A"), ("Grupos", "Grupo B")]
        tb1, tb2 = tbs[:2], tbs[2:]
    else:
        maior = max(tbs, key=lambda tb: len(tb["ativos"]))
        tb1, tb2 = [maior], [tb for tb in tbs if tb is not maior]
        fases1 = [("Fase regular", None)]
    for (fase, grupo), tb in zip(fases1, tb1):
        cs = {x["clube"] for x in tb["ativos"]}
        js = [j for j in regular if {j["m"], j["v"]} <= cs]
        for j in js:
            j["fase"], j["grupo"] = fase, grupo
        etapas.append({"fase": fase, "grupo": grupo, "tb": tb, "rs": None, "jogos": js, "base": [], "sem_jogos": False})
    primeiro = tb1[0]["ativos"][0]["clube"] if len(tb1) == 1 else None
    for tb in tb2:
        cs = {x["clube"] for x in tb["ativos"]}
        tit = (primeiro in cs) if primeiro else (tb is tb2[0])
        fase = "Grupo do título" if tit else "Grupo de rebaixamento"
        js = [j for j in resto if {j["m"], j["v"]} <= cs]
        for j in js:
            j["fase"] = fase
        base = [j for j in regular if j["m"] in cs or j["v"] in cs]
        etapas.append({"fase": fase, "grupo": None, "tb": tb, "rs": None, "jogos": js, "base": base, "sem_jogos": False})
    sobra = [j for j in jogos if not any(j in e["jogos"] for e in etapas)]
    for j in sobra:
        ocorr.append(f"jogo sem fase, fora do pacote: {j['m']} x {j['v']} ({j['data']})")
    jogos = [j for e in etapas for j in e["jogos"]]
    ordem = [x["clube"] for e in etapas if e["fase"] == "Grupo do título" for x in e["tb"]["ativos"]] + \
            [x["clube"] for e in etapas if e["fase"] == "Grupo de rebaixamento" for x in e["tb"]["ativos"]]
    if t == "2001/02":
        formato = "dois grupos de 8 (turno e returno), depois grupo do título e grupo de rebaixamento de 8 (turno e returno)"
    else:
        formato = ("fase regular em turno e returno e grupos do título e de rebaixamento em turno único, com os pontos da "
                   "fase regular divididos por dois")
    return {"etapas": etapas, "jogos": jogos, "ordem": ordem, "formato": formato,
            "fonte_ordem": "Wikipédia (grupo do título, depois grupo de rebaixamento)", "numeros": None}


# ------------------------------------------------------------------ artilheiros
def _dobra(s: str) -> str:
    return unicodedata.normalize("NFKD", s.replace("ł", "l").replace("Ł", "L")).encode("ascii", "ignore").decode().lower()


def _nome(s: str) -> str:
    return " ".join("-".join(p.capitalize() if p.isupper() and len(p) > 1 else p for p in w.split("-")) for w in s.split())


def artilheiros(hist: dict[str, str], ocorr) -> list[dict]:
    """poltops.html: "1922 - Waclaw KUCHAR (Pogon Lwow) - 21", empates em linhas de continuação; o ano depois de 1962 é o
    do fim da temporada. A grafia com acentos vem do bloco da temporada em polhist.html, quando ele traz o nome."""
    linhas, atual = [], None
    for l in rsssf.texto(DADOS / "rsssf" / "poltops.html").split("\n"):
        l = l.replace("\x96", "-")   # travessão do Windows-1252 no meio do texto
        m = re.match(r"^(\d{4})\s*-?\s+(\S.*)$", l)
        if m:
            atual = [int(m.group(1)), m.group(2)]
            linhas.append(atual)
        elif atual and re.match(r"^\s{4,}\S", l):
            atual[1] += " " + l.strip()
        else:
            atual = None
    res = []
    for ano, txt in linhas:
        t = str(ano) if ano <= 1962 else f"{ano - 1}/{str(ano)[-2:]}"
        if t not in TEMPORADAS:
            continue
        g = re.search(r"[-\s](\d+)\s*(?:\+\s*\d+ annulled)?\s*(\[[^\]]*\])?\s*$", txt)
        if not g:
            continue
        corpo = txt[:g.start()]
        bloco = hist.get(t, "")
        grafias = {_dobra(f"{a} {b}"): f"{a} {b}" for a, b in
                   re.findall(r"([A-ZÀ-ÝĄĆĘŁŃÓŚŹŻ][a-zà-ÿąćęłńóśźż]+)\s+([A-ZÀ-ÝĄĆĘŁŃÓŚŹŻ][A-Za-zÀ-ÿĄĆĘŁŃÓŚŹŻąćęłńóśźż-]+)", bloco)}
        for nome, clube_txt in re.findall(r"([^,()]+?)\s*\(([^)]*)\)", corpo):
            nome = nome.strip().lstrip(",- ").strip()
            nome = _nome(grafias.get(_dobra(nome), nome))
            nome = {"Carlitos Daniel Lopez": "Carlitos"}.get(nome, nome)
            c = clubes.esd(clube_txt)
            if c is None:
                ocorr[t].append(f"artilheiro com clube sem cadastro na lista da RSSSF: {nome} ({clube_txt})")
            res.append({"temporada": t, "jogador": nome, "clube": clubes.exibicao(c) if c else None, "gols": int(g.group(1)),
                        "fonte": "RSSSF (tablesp/poltops.html" + ("; só a fase final)" if t in ("1946", "1947") else ")")})
    return res


# ------------------------------------------------------------------ principal
def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    hist = rsssf.blocos(rsssf.texto(DADOS / "rsssf" / "polhist.html"))
    camp_rs = campeoes_rsssf()
    fd = football_data()
    nomes = defaultdict(lambda: defaultdict(set))
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel, criterios = [], {}

    wikis = {t: ler_wiki(t) for t in TEMPORADAS}
    clubes_de = {t: {x["clube"] for tb in w["tbs"] for x in tb["times"]} for t, w in wikis.items()}
    clubes_de["2026/27"] = {c for j in carregar_ogol("2026/27") for c in (j["m"], j["v"])}

    for t in TEMPORADAS:
        ocorr[t].extend(EXPLICACOES.get(t, []))
        W = wikis[t]
        pts = pontos(t)
        secs = rsssf.secoes(hist[t]) if t in hist else []
        if t in TORNEIOS:
            est = torneio(t, W, secs, pts, ocorr[t])
        elif ano_inicio(t) < 1962 or t == "1962":
            est = liga_antiga(t, W, secs, pts, ocorr[t])
        else:
            og = carregar_ogol(t)
            for j in og:
                for lado in ("m", "v"):
                    nomes[j[lado]][f"ogol:{j['n' + lado]}"].add(t)
            est = liga_ogol(t, W, og, pts, ocorr[t])
            usadas = set()
            for e in est["etapas"]:
                if ano_inicio(t) <= 2000:
                    e["rs"] = melhor_rs(secs, e["tb"], pts, usadas)
        bonus = any(e["tb"]["bonus"] for e in est["etapas"] if e["tb"])
        etapas, jogos = est["etapas"], est["jogos"]

        # ---- decididos fora de campo, sem placar no ogol: placar da matriz da Wikipédia
        mz_w = defaultdict(list)
        for b in W["blocos"]:
            for w in b["jogos"]:
                mz_w[(w["m"], w["v"])].append((w["gm"], w["gv"]))
        for j in jogos:
            j.setdefault("especial", None)
            j.setdefault("obs", None)
            if j["gm"] is not None or j.get("dois"):
                continue
            if (t, j["m"], j["v"]) in DECIDIDOS:
                j["gm"], j["gv"], motivo = DECIDIDOS[(t, j["m"], j["v"])]
                j["especial"], j["obs"] = "awd", f"resultado decidido fora de campo: {motivo}"
                ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): sem placar no ogol; fica {j['gm']}-{j['gv']} ({motivo})")
                continue
            cand = mz_w.get((j["m"], j["v"]), [])
            if not cand:
                raise SystemExit(f"{t}: jogo sem placar no ogol ({j['ogol']['resultado']}) e sem a matriz da Wikipédia: "
                                 f"{j['m']} x {j['v']} ({j['data']})")
            j["gm"], j["gv"] = cand[0] if j["fase"] in ("Liga", "Fase regular", "Grupos") else cand[-1]
            j["especial"] = "awd"
            j["obs"] = (f"resultado decidido fora de campo (no ogol: \"{j['ogol']['resultado']}\", sem placar); placar oficial "
                        f"pela matriz da Wikipédia")
            ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): {j['ogol']['resultado']} no ogol; fica {j['gm']}-{j['gv']} pela "
                            f"matriz da Wikipédia")

        # ---- ogol x matriz da Wikipédia: mando trocado e placar diferente. Fica a matriz quando ela fecha melhor com as
        # tabelas publicadas ou, empatado, quando o football-data ou a matriz da RSSSF concordam com ela
        if ano_inicio(t) >= 1962 and t != "1962":
            fd_idx = defaultdict(list)
            for x in fd.get(t, []):
                fd_idx[(x["m"], x["v"])].append((x["gm"], x["gv"]))
            for e in etapas:
                if e["base"] or not e["tb"]:
                    continue
                pubs = [{x["clube"]: pub_wiki(x, pts)[:6] for x in e["tb"]["ativos"]}]
                rs_mz = {}
                if e["rs"]:
                    pubs.append({x["clube"]: pub_rs(x)[:6] for x in e["rs"]})
                    if all(len(x["celulas"]) == len(e["rs"]) for x in e["rs"]):
                        for g in rsssf.jogos_da_matriz(e["rs"]):
                            rs_mz[(e["rs"][g["i"]]["clube"], e["rs"][g["k"]]["clube"])] = (g["gm"], g["gv"])

                def distancia(cs):
                    c_ = calcular(e["jogos"], pts, bonus)
                    return sum(abs(c_[c][q] - p_[c][q]) for p_ in pubs for c in cs if c in p_ for q in range(6))

                def votos(m, v, pl):
                    return [f for f, ok in (("football-data", pl in fd_idx.get((m, v), [])), ("RSSSF", rs_mz.get((m, v)) == pl))
                            if ok]
                por_dir = defaultdict(list)
                for j in e["jogos"]:
                    if j["fonte"] == "ogol":
                        por_dir[(j["m"], j["v"])].append(j)
                for (m, v), js in list(por_dir.items()):   # mando trocado: o par duas vezes no mesmo sentido
                    if len(js) <= len(mz_w.get((m, v), [])) or len(por_dir.get((v, m), [])) >= len(mz_w.get((v, m), [])):
                        continue
                    for pl in mz_w[(v, m)][len(por_dir.get((v, m), [])):]:
                        antes = distancia((m, v))
                        melhor = None
                        for j in js:
                            velho_j = (j["m"], j["v"], j["gm"], j["gv"])
                            j["m"], j["v"], j["gm"], j["gv"] = v, m, pl[0], pl[1]
                            d = distancia((m, v))
                            if (d < antes or (d == antes and votos(v, m, pl))) and (melhor is None or d < melhor[0]):
                                melhor = (d, j, velho_j)
                            j["m"], j["v"], j["gm"], j["gv"] = velho_j
                        if melhor is None:
                            ocorr[t].append(f"{m} x {v}: o ogol tem o par duas vezes com o mesmo mandante; a matriz da Wikipédia "
                                            f"dá {v} {pl[0]}-{pl[1]} {m} no returno; fica o ogol (a troca não fecha melhor)")
                            continue
                        _, j, velho_j = melhor
                        j["m"], j["v"], j["gm"], j["gv"] = v, m, pl[0], pl[1]
                        j["obs"] = (f"mando e placar da matriz da Wikipédia ({v} {pl[0]}-{pl[1]} {m}); o ogol dá {m} "
                                    f"{velho_j[2]}-{velho_j[3]} {v}, o par duas vezes com o mesmo mandante")
                        ocorr[t].append(f"{v} x {m} ({j['data']}): fica {pl[0]}-{pl[1]} pela matriz da Wikipédia; o ogol dá "
                                        f"{m} {velho_j[2]}-{velho_j[3]} {v} (o par duas vezes com o mesmo mandante)")
                        js.remove(j)
                # placar diferente: primeiro o par inteiro (ida e volta com os placares trocados), depois jogo a jogo
                difs = defaultdict(list)
                for j in e["jogos"]:
                    pl = mz_w.get((j["m"], j["v"]))
                    if j["fonte"] == "ogol" and not j["especial"] and pl and len(pl) == 1 and (j["gm"], j["gv"]) not in pl:
                        difs[frozenset((j["m"], j["v"]))].append(j)
                for par, js in difs.items():
                    for grupo_js in ([js] if len(js) > 1 else []) + [[j] for j in js]:
                        if any(j.get("trocado") for j in grupo_js):
                            continue
                        cs = tuple(par)
                        antes = distancia(cs)
                        velhos = [(j["gm"], j["gv"]) for j in grupo_js]
                        for j in grupo_js:
                            j["gm"], j["gv"] = mz_w[(j["m"], j["v"])][0]
                        d = distancia(cs)
                        vts = [votos(j["m"], j["v"], (j["gm"], j["gv"])) for j in grupo_js]
                        if d < antes or (d == antes and all(vts)):
                            for j, vp, vt in zip(grupo_js, velhos, vts):
                                j["trocado"] = True
                                txt = f" (igual ao {' e à '.join(vt)})" if vt else ""
                                j["obs"] = f"placar da matriz da Wikipédia{txt}; o ogol dá {vp[0]}-{vp[1]}"
                                ocorr[t].append(f"{j['m']} x {j['v']} ({j['data']}): fica {j['gm']}-{j['gv']} pela matriz da "
                                                f"Wikipédia{txt}; o ogol dá {vp[0]}-{vp[1]}" +
                                                (", que fecha pior com as tabelas" if d < antes else ""))
                        else:
                            for j, vp in zip(grupo_js, velhos):
                                j["gm"], j["gv"] = vp

        # ---- jogos que faltam no ogol (só na liga de uma tabela): da matriz da Wikipédia, sem data
        if ano_inicio(t) >= 1962 and t != "1962" and len(etapas) == 1:
            tem = Counter((j["m"], j["v"]) for j in jogos)
            tem_par = Counter(frozenset((j["m"], j["v"])) for j in jogos)
            for (m, v), pl in mz_w.items():
                falta = min(len(pl) - tem[(m, v)],   # o ogol às vezes troca o mando: conta o par nos dois sentidos
                            len(pl) + len(mz_w.get((v, m), [])) - tem_par[frozenset((m, v))])
                for gm, gv in pl[len(pl) - max(falta, 0):] if falta > 0 else []:
                    j = {"m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "fase": etapas[0]["fase"], "grupo": None,
                         "rodada": None, "data": None, "hora": None, "fonte": "Wikipédia (matriz)", "fonte_id": None,
                         "especial": None, "obs": "jogo que o ogol não tem: placar da matriz da Wikipédia, sem data"}
                    jogos.append(j)
                    if etapas[0]["jogos"] is not jogos:
                        etapas[0]["jogos"].append(j)
                    ocorr[t].append(f"{m} x {v}: o ogol não tem o jogo; entra {gm}-{gv} pela matriz da Wikipédia, sem data")

        # ---- conferência com a matriz da Wikipédia (ogol) e com o football-data
        if ano_inicio(t) >= 1962 and t != "1962":
            por_par = defaultdict(list)
            for j in jogos:
                por_par[(j["m"], j["v"])].append((j["gm"], j["gv"]))
            dif = [f"{m} x {v}: ogol {', '.join(f'{a}-{b}' for a, b in sorted(por_par[(m, v)]))}; Wikipédia "
                   f"{', '.join(f'{a}-{b}' for a, b in pl)}" for (m, v), pl in mz_w.items()
                   if por_par.get((m, v)) and sorted(pl) != sorted(por_par[(m, v)])]
            ocorr[t] += [f"placar diferente na matriz da Wikipédia — {d}" for d in dif[:15]]
            if len(dif) > 15:
                ocorr[t].append(f"... e mais {len(dif) - 15} pares com placar diferente na matriz da Wikipédia")
            if not mz_w:
                ocorr[t].append("sem matriz na Wikipédia para conferir os jogos")
            fdj = fd.get(t, [])
            if fdj:
                idx = defaultdict(list)
                for j in jogos:
                    idx[(j["m"], j["v"])].append(j)
                dif_fd = []
                for x in fdj:
                    if x["m"] is None or x["v"] is None:
                        ocorr[t].append(f"nome do football-data sem cadastro: {x['nm']} x {x['nv']}")
                        continue
                    c_ = idx.get((x["m"], x["v"]), [])
                    j = min(c_, key=lambda j: abs((int((j["data"] or "0000-00-00").replace("-", "")) -
                                                    int(x["data"].replace("-", "")))), default=None)
                    if j is None:
                        dif_fd.append(f"{x['m']} x {x['v']} ({x['data']}): no football-data, não no ogol")
                    elif (j["gm"], j["gv"]) != (x["gm"], x["gv"]) and not j["especial"]:
                        dif_fd.append(f"{x['m']} x {x['v']} ({j['data']}): ogol {j['gm']}-{j['gv']}, football-data {x['gm']}-{x['gv']}")
                ocorr[t] += [f"football-data — {d}" for d in dif_fd[:10]]
                if len(dif_fd) > 10:
                    ocorr[t].append(f"... e mais {len(dif_fd) - 10} diferenças com o football-data")

        # ---- tabelas publicadas x jogos, fase a fase
        conferidas = divergentes = 0
        ajuste: dict[str, int] = {}
        publicados: dict[str, list[int]] = {}
        acumula = {}
        for e in etapas:
            tb = e["tb"]
            for x in tb["ativos"]:
                nomes[x["clube"]][f"wikipedia:{x['nome']}"].add(t)
                if x["ajuste"]:
                    ajuste[x["clube"]] = x["ajuste"]
            for x in e["rs"] or []:
                nomes[x["clube"]][f"rsssf:{x['nome']}"].add(t)
            if e["sem_jogos"]:   # grupo final de 1926: só a tabela
                for x in tb["ativos"]:
                    publicados[x["clube"]] = pub_wiki(x, pts)[:6]
                    tab["tabelas_publicadas"].append({
                        "temporada": t, "fase": e["fase"], "grupo": e["grupo"], "posicao": x["posicao"], "nome_fonte": x["nome"],
                        "clube": clubes.exibicao(x["clube"]), **dict(zip(("jogos", "vitorias", "empates", "derrotas", "gols_pro",
                                                                         "gols_contra", "pontos"), pub_wiki(x, pts))),
                        "fonte": url_wiki(t)})
                ocorr[t].append(f"{e['fase']}: sem os jogos em nenhuma fonte (RSSSF, Wikipédia em inglês e em polonês); fica a "
                                f"tabela publicada")
                continue
            so = calcular(e["jogos"], pts, bonus)
            com = calcular(e["base"] + e["jogos"], pts, bonus) if e["base"] else so

            def dist(c_):
                return sum(abs(c_[x["clube"]][q] - pub_wiki(x, pts)[q]) for x in tb["ativos"] for q in range(1, 6))
            acumula[id(e)] = bool(e["base"]) and dist(com) <= dist(so)
            calc = com if acumula[id(e)] else so
            erros = {}
            for fonte, url, linhas, f_pub in (("Wikipédia", url_wiki(t), tb["ativos"], lambda x: pub_wiki(x, pts)),
                                              ("RSSSF", URL_HIST, e["rs"] or [], pub_rs)):
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
            rot = f" ({e['grupo'] or e['fase']})" if len(etapas) > 1 else ""
            for fonte, erro in erros.items():
                outra = [f_ for f_ in erros if f_ != fonte]
                for c, pub, meu in erro[:8]:
                    fecha = outra and c not in {x[0] for x in erros[outra[0]]}
                    ocorr[t].append(f"tabela{rot} da {fonte} x jogos — {c} tabela {pub} jogos {meu}"
                                    + (f" (a tabela da {outra[0]} fecha com os jogos)" if fecha else ""))
            # matriz que não fecha com as duas tabelas, que concordam entre si: a classificação fica com os publicados
            if len(etapas) == 1 and ano_inicio(t) < 1962:
                for x in tb["ativos"]:
                    y = next((y for y in e["rs"] or [] if y["clube"] == x["clube"]), None)
                    pub = pub_wiki(x, pts)[:6]
                    if (y is None or pub_rs(y)[:6] == pub) and pub != calc[x["clube"]][:6]:
                        publicados[x["clube"]] = pub
                if publicados:
                    ocorr[t].append(f"os jogos da matriz não fecham com as tabelas publicadas, que concordam entre si, em "
                                    f"{len(publicados)} clubes: a classificação final fica com os números publicados "
                                    f"(observação na linha)")
            ordem_tb = [x["clube"] for x in tb["ativos"]]
            js_ord = (e["base"] + e["jogos"]) if acumula[id(e)] else e["jogos"]
            crits = ("media", "saldo") if ano_inicio(t) < 1962 else ("saldo", "media") if ano_inicio(t) < 1990 else \
                ("confronto", "saldo")
            tent = {cr: ordenar(calc, ajuste, cr, js_ord, pts, bonus) for cr in crits}
            ok = [cr for cr, o in tent.items() if o == ordem_tb]
            cr = ok[0] if ok else min(tent, key=lambda q: sum(a != b for a, b in zip(tent[q], ordem_tb)))
            if not ok:
                d_ = [c for c, d in zip(ordem_tb, tent[cr]) if c != d]
                ocorr[t].append(f"nenhum critério calculado reproduz a ordem oficial{rot}; o mais próximo ({cr}) difere em "
                                f"{len(d_)} posições (ex.: {d_[:2]})")
            criterios[(t, id(e))] = (cr, bool(ok))
            e["criterio"] = cr
            n_esp = len(tb["ativos"]) * (len(tb["ativos"]) - 1) * (1 if e["fase"] != "Grupo do título" or t == "2001/02" or
                                                                   ano_inicio(t) < 2000 else 0)
            if n_esp and len(e["jogos"]) != n_esp and e["fase"] in ("Liga", "Grupos", "Fase regular", "Grupo final"):
                ocorr[t].append(f"{len(e['jogos'])} jogos{rot} para {len(tb['ativos'])} clubes (esperados {n_esp})")

        # ---- classificação final (o vencedor de um desempate fica à frente do perdedor)
        ordem = est["ordem"] or [x["clube"] for x in etapas[0]["tb"]["ativos"]]
        for j in jogos:
            if j["fase"] == "Desempate" and t not in TORNEIOS:
                venc, perd = (j["m"], j["v"]) if j["gm"] > j["gv"] else (j["v"], j["m"])
                a_, b_ = ordem.index(venc), ordem.index(perd)
                if a_ > b_:
                    ordem[a_], ordem[b_] = perd, venc
        todos = [j for j in jogos if not j["fase"].startswith("Desempate")]
        if est["numeros"] == "todos" or len(etapas) == 1 or all(acumula.get(id(e), True) for e in etapas if e["base"]):
            numeros = calcular(todos, pts, bonus)
            so_grupo = {}
        else:   # grupos finais sem os pontos da 1ª fase: os números do grupo
            numeros = calcular(todos, pts, bonus)
            so_grupo = {}
            for e in etapas:
                if e["fase"] in ("Grupo do título", "Grupo de rebaixamento"):
                    c_ = calcular(e["jogos"], pts, bonus)
                    for x in e["tb"]["ativos"]:
                        numeros[x["clube"]] = c_[x["clube"]]
                        so_grupo[x["clube"]] = e["fase"].lower()
        ajuste_final = dict(ajuste)
        for e in etapas:
            if e["fase"] in ("Grupo do título", "Grupo de rebaixamento"):
                for x in e["tb"]["ativos"]:
                    ajuste_final[x["clube"]] = x["ajuste"] or 0
        prox = TEMPORADAS[TEMPORADAS.index(t) + 1] if t != TEMPORADAS[-1] else "2026/27"
        if t in TORNEIOS:
            rebaixados = set()
        elif t == "1938" or prox in TORNEIOS:   # a guerra: quem caiu pela tabela
            rebaixados = {x["clube"] for e in etapas for x in e["tb"]["ativos"] if "R" in (x["status"], x["resultado"])}
        else:
            rebaixados = set()
            for c in ordem:
                if c not in clubes_de[prox]:
                    if (t, c) in NAO_REBAIXADOS:
                        ocorr[t].append(f"{c} não está na temporada seguinte, mas não caiu: {NAO_REBAIXADOS[(t, c)]}")
                    else:
                        rebaixados.add(c)
            marca = {x["clube"] for e in etapas for x in e["tb"]["ativos"] if x["status"] == "R" or x["resultado"] == "R"}
            if marca and marca != rebaixados and len(etapas) == 1:
                ocorr[t].append(f"rebaixados pela temporada seguinte {sorted(rebaixados)}; marcados na tabela da Wikipédia "
                                f"{sorted(marca)}")
        campeao = ordem[0]
        obs_camp = None
        if t in CAMPEAO_FORA:
            campeao, obs_camp = CAMPEAO_FORA[t]
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
            if c in publicados and c in numeros and len(etapas) == 1:
                obs.append(f"números das tabelas publicadas (Wikipédia e RSSSF, iguais); os jogos da matriz somam {j_} jogos, "
                           f"{v_}-{e_}-{d_} e {gp}-{gc} gols")
                j_, v_, e_, d_, gp, gc = publicados[c]
                p = pts[0] * v_ + pts[1] * e_
                b = next((x["bonus"] for x in etapas[0]["tb"]["ativos"] if x["clube"] == c), 0)
            elif c in publicados:   # 1926: o grupo final só pela tabela
                q = publicados[c]
                j_, v_, e_, d_, gp, gc = j_ + q[0], v_ + q[1], e_ + q[2], d_ + q[3], gp + q[4], gc + q[5]
                p += pts[0] * q[1] + pts[1] * q[2]
                obs.append("inclui os números do grupo final, só da tabela publicada (sem os jogos)")
            if c in so_grupo:
                obs.append(f"números só do {so_grupo[c]} (os pontos da 1ª fase não contam)")
            if c == campeao and obs_camp:
                obs.append(obs_camp)
            if notas_tb.get(c):
                obs.append(notas_tb[c])
            aj = ajuste_final.get(c, 0) + b
            tab["classificacao_final"].append({
                "temporada": t, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + aj, "ajuste_pontos": aj,
                "situacao": "campeao" if c == campeao else "rebaixado" if c in rebaixados else None,
                "fonte": est["fonte_ordem"], "observacao": "; ".join(obs) or None})

        # ---- partidas
        if ano_inicio(t) < 1962 or t == "1962":
            ordem_fase = {f: k for k, f in enumerate(dict.fromkeys(j["fase"] for j in jogos))}
            jogos.sort(key=lambda j: (ordem_fase[j["fase"]], j["grupo"] or "", j["data"] or "", j["m"], j["v"]))
        else:
            jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["m"]))
        gols_ano = 0
        rot_id = t.replace("/", "-")
        for i, j in enumerate(jogos, 1):
            for lado in ("m", "v"):
                if j["fonte"] != "ogol":
                    nomes[j[lado]][f"{'rsssf' if 'RSSSF' in j['fonte'] else 'wikipedia'}:{j['n' + lado]}"].add(t)
            tab["partidas"].append({
                "id": f"{rot_id}-{i:04d}", "temporada": t, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"],
                "data": j["data"], "hora": j["hora"], "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": j["especial"], "estadio": None, "cidade": None, "publico": None, "fonte": j["fonte"],
                "fonte_id": j["fonte_id"], "gols_texto": None, "observacao": j["obs"], "arbitro": None,
                "_derrota_dois": bool(j.get("dois"))})
            gols_ano += (j["gm"] or 0) + (j["gv"] or 0)

        # ---- classificação rodada a rodada (liga ou fase regular do ogol)
        reg = [j for j in jogos if j["fase"] in ("Liga", "Fase regular") and j["rodada"]]
        if reg and len(reg) == len([j for j in jogos if j["fase"] in ("Liga", "Fase regular")]):
            e0 = next(e for e in etapas if e["fase"] in ("Liga", "Fase regular"))
            aj0 = {x["clube"]: x["ajuste"] for x in e0["tb"]["ativos"] if x["ajuste"]} if len(etapas) > 1 else ajuste
            pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
            for r in sorted({j["rodada"] for j in reg}):
                ate = [j for j in reg if j["rodada"] <= r]
                parcial = calcular(ate, pts, bonus)
                for pos, c in enumerate(ordenar(parcial, aj0, e0["criterio"], ate, pts, bonus), 1):
                    jj, v_, e_, d_, gp, gc, p, b = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": t, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + b + aj0.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        # ---- edição, fases, conferência
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items()
                        if not any(e["fase"] in ("Grupo do título", "Grupo de rebaixamento") for e in etapas) or
                        ano_inicio(t) < 2013)
        obs_ed = [x for x in (
            obs_camp,
            "os pontos de bônus estão em ajuste_pontos" if bonus else "",
            f"punições: {pun}" if pun else "",
            "pontos da fase regular divididos por dois antes dos grupos (em ajuste_pontos)" if 2013 <= ano_inicio(t) <= 2019 else "",
            "; ".join(f"{(c_)} saiu do campeonato e teve os jogos anulados (linha vazia na tabela da Wikipédia)"
                      for e in etapas for c_ in [x["clube"] for x in e["tb"]["times"] if not x["ativo"]]),
            "dois jogos da última rodada anulados pela federação (ŁKS 7-1 Olimpia Poznań e Wisła 0-6 Legia, suspeita de "
            "manipulação): Legia e ŁKS, 1º e 2º no campo, perderam a vantagem e o título foi do Lech" if t == "1992/93" else "",
        ) if x]
        tab["edicoes"].append({
            "temporada": t, "ano_inicio": ano_inicio(t), "ano_fim": ano_fim(t), "nome_oficial": nome_oficial(t),
            "num_clubes": len({c for j in jogos for c in (j["m"], j["v"])} | set(publicados)), "pontos_vitoria": pts[0],
            "pontos_empate": None, "pontos_derrota": None,
            "formato": est["formato"] + ("; +1 ponto pela vitória por 3 gols ou mais e -1 pela derrota por 3 ou mais"
                                         if bonus else ""),
            "campeao": clubes.exibicao(campeao), "vice": None if t in CAMPEAO_FORA else clubes.exibicao(ordem[1]),
            "co_campeao": None,
            "fontes": ("RSSSF + Wikipédia" if t in TORNEIOS else "Wikipédia + RSSSF" if ano_inicio(t) < 1962 or t == "1962"
                       else "ogol + Wikipédia" + (" + RSSSF" if ano_inicio(t) <= 2000 else "") +
                       (" + football-data" if t in fd else "")),
            "observacao": "; ".join(obs_ed) or None, "oficial": None})
        crit_txt = {"saldo": "pontos, saldo de gols", "media": "pontos, média de gols (goal average)",
                    "confronto": "pontos, confronto direto, saldo de gols"}
        fases_ed = {}
        for e in etapas:
            if e["fase"] in fases_ed:
                continue
            n_g = sum(1 for x in etapas if x["fase"] == e["fase"])
            fases_ed[e["fase"]] = {"temporada": t, "fase": e["fase"],
                                   "tipo": "liga" if e["fase"] in ("Liga", "Fase regular") else "grupos",
                                   "num_grupos": None if e["fase"] in ("Liga", "Fase regular") else n_g,
                                   "formato_serie": "pontos_corridos",
                                   "criterio": crit_txt[e.get("criterio", "saldo")] + (
                                       "; pontos da fase regular divididos por dois" if e["base"] and
                                       2013 <= ano_inicio(t) <= 2019 else
                                       "; pontos acumulados com a 1ª fase" if acumula.get(id(e)) else "")}
        for f in dict.fromkeys(j["fase"] for j in jogos):
            if f in fases_ed:
                continue
            ida_volta = f in ("Final", "Play-off de classificação")
            fases_ed[f] = {"temporada": t, "fase": f, "tipo": "mata_mata", "num_grupos": None,
                           "formato_serie": "ida_volta" if ida_volta else "jogo_unico",
                           "criterio": "pontos nos dois jogos; empate, jogo extra" if t == "1923" and f == "Final" else
                           "pontos nos dois jogos, depois saldo" if ida_volta else "jogo único"}
        for k, f in enumerate(sorted(fases_ed, key=lambda f: ORDEM_FASES.get(f, 50)), 1):
            tab["fases"].append({"ordem": k, **fases_ed[f]})
        tab["conferencia"].append({"temporada": t, "jogos": len(jogos), "jogos_esperados": None, "tabelas_conferidas": conferidas,
                                   "tabelas_divergentes": divergentes, "gols": gols_ano, "gols_com_autor": 0,
                                   "observacao": f"campeão {clubes.exibicao(campeao)}; lista da RSSSF: {nome_rs or '—'}"})
        linhas_rel.append((t, len(ordem), len(jogos), gols_ano, conferidas, divergentes, clubes.exibicao(campeao), pun))
        print(f"{t}: {len(jogos)} jogos, {len(ordem)} clubes, tabelas {conferidas} ok / {divergentes} div, "
              f"campeão {clubes.exibicao(campeao)}", flush=True)

    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c in nomes:
            tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais,
                                  "nomes_fonte": "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))})
    tab["paises"] = [{"codigo": "POL", "nome": "Polônia", "confederacao": "UEFA"},
                     {"codigo": "UKR", "nome": "Ucrânia", "confederacao": "UEFA"},
                     {"codigo": "LTU", "nome": "Lituânia", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(hist, ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, criterios)


def relatorio(linhas, ocorr, tab, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"] or 0) + int(x["gols_visitante"] or 0) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Polonês (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/pol-1/importar.py`. Pacote em `data/coleta/pol-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1921 a 2025/26: os 98 títulos que a federação reconhece (torneios entre os campeões "
        "regionais em 1921-1926, 1946 e 1947; liga de 1927 a 1938 e desde 1948; 1962 só com a primavera).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['clubes'])} clubes. Sem autores dos gols, cartões e público.", "",
        "**Fontes:**",
        "- RSSSF (polhist.html): matriz dos torneios (base dos jogos de 1921-1926, 1946 e 1947), tabela e matriz de cada "
        "temporada até 2000/01 (conferência), final de 1922 e play-offs de 1962; lista de campeões e de artilheiros;",
        "- Wikipédia (en): tabela de cada fase (ordem oficial, punições, bônus), matriz de resultados (base dos jogos de 1927 "
        "a 1962, conferência depois), fichas das finais de 1923, do desempate de 1925 e do mata-mata de 1946;",
        "- ogol (zerozero): base dos jogos desde 1962/63, com data, hora e rodada; calendários em `data/cache/ogol-pol-1/`;",
        "- football-data: conferência dos placares desde 2012/13.", "",
        "**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a "
        "oficial (Wikipédia; nos torneios, o grupo final ou a final e depois a posição no grupo; em 1962, os play-offs de "
        "classificação). Pontos 2-1-0 até 1994/95 e 3-1-0 depois; bônus de 1986/87 a 1989/90 e pontos da fase regular "
        "divididos por dois de 2013/14 a 2019/20, em `ajuste_pontos`. Rebaixado = clube que não está na 1ª divisão na "
        "temporada seguinte (em 1938, a marca da tabela).", "",
        f"**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em {cr['media']} fases, saldo em "
        f"{cr['saldo']}, confronto direto em {cr['confronto']}).", "",
        "| Temporada | Clubes | Jogos | Gols | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|",
    ]
    for t, n, j, g, ok, dv, camp, pun in linhas:
        out.append(f"| {t} | {n} | {j} | {g} | {ok} / {dv} | {camp} | {pun or '—'} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for t, *_ in linhas:
        out += [f"### {t}", ""] + [f"- {o}" for o in ocorr.get(t, []) or ["sem ocorrências"]] + [""]
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_pol.py`, pela linhagem do clube (o alvo do link da Wikipédia, seguindo os "
        "redirecionamentos). Mesmo clube: Wisła Cracóvia = Gwardia Kraków; Lech = KKS Poznań e Kolejarz; Ruch = Unia "
        "Chorzów; Legia = CWKS; Wisła Płock = Petrochemia e Orlen; GKS Tychy = Sokół; ROW Rybnik = Energetyk; Stomil = OKS "
        "Olsztyn; Termalica = LKS Nieciecza; Rymer Niedobczyce = Rymer Rybnik. Pelo link, a Wikipédia dá o PKS Szczecin de "
        "1946-47 como o Pogoń Szczecin, o Motor Białystok de 1947 como o Jagiellonia, o Grochów de 1947 como o Gwardia "
        "Varsóvia e o RKU Sosnowiec como o Zagłębie Sosnowiec.",
        "- Clubes de Lwów e Wilno com o país de hoje: Ucrânia (Lviv) e Lituânia (Vilnius). O Strzelec Wilno de 1922 (a "
        "RSSSF o chama de Śmigły, clube fundado em 1933 da fusão do Strzelec com outros).",
        "- Os nomes de cada fonte, com as temporadas, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Datas e rodadas de 1921 a 1962** (só a matriz de resultados, exceto as fichas da Wikipédia e a final de 1952).",
        "- **Os jogos do grupo final de 1926:** nenhuma fonte traz (a Wikipédia polonesa só cita a vitória decisiva do "
        "Pogoń sobre a Polonia, 2-0, sem o mando); fica a tabela publicada.",
        "- **Autores dos gols, cartões, público, estádio e árbitro:** nenhuma fonte em lote cobre a Polônia (sem ESPN; o "
        "football-data não traz cartões da Polônia); só a ficha de cada jogo no ogol.",
        "- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
