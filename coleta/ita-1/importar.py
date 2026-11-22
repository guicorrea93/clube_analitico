"""Monta o pacote da 1ª divisão italiana (ita-1), 1929/30 a 2025/26, e o relatório docs/coleta/ita-1.md.

Base dos jogos: engsoccerdata. Cada jogo é casado pelo par mandante x visitante, que é único na fase (turno e
returno), com:
  ogol           rodada oficial e conferência de placar (clubes casados pelo código do ogol, por votação); completa as
                 temporadas em que a base vem com jogos faltando ou fora da temporada (ver `reparar`);
  football-data  1993/94+: conferência de placar; hora (2019/20+), árbitro e estatísticas por time;
  ESPN           2001/02+: hora, estádio, público, gols e cartões com minuto (clubes casados pelo código da ESPN);
  RSSSF          tabela final, quando a página traz uma tabela legível (os formatos mudam muito de uma temporada para
                 outra);
  Wikipédia      tabela final de cada temporada (ordem oficial, punições), campeões e Capocannoniere.

1945/46 (Divisione Nazionale): grupo Norte (14 clubes), grupo Centro-Sul (11) e grupo final (os 4 primeiros de cada).

Regras: o placar é o da base; jogo que falta na base entra pelo ogol, com o motivo. Os gols da ESPN só entram quando
a soma bate com o placar.

Uso: python coleta/ita-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_ita as clubes  # noqa: E402
from edicoes import DADOS, DIVISIONE, RAIZ, TEMPORADAS, nome_oficial, rsssf_url, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from wiki_tabela import limpar, tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")
ROMA = ZoneInfo("Europe/Rome")
PACOTE = DADOS / "pacote"
SO_FD = (2025,)   # temporadas que o engsoccerdata não tem: base pelo football-data
RELATORIO = RAIZ / "docs" / "coleta" / "ita-1.md"

# placar corrigido na base: (ano, mandante, visitante) -> (gols, gols, motivo). Chaves de clubes_ita.
OGOL_WIKI = "o ogol e a tabela da Wikipédia fecham com este placar"
CORRECOES: dict[tuple, tuple] = {
    (1933, "AC Milan", "Casale"): (6, 2, OGOL_WIKI),
    (1933, "AS Livorno", "US Palermo"): (3, 2, OGOL_WIKI),
    (1933, "Torino FC", "AS Roma"): (3, 6, OGOL_WIKI + "; os pontos da RSSSF também (Roma 40, Torino 29)"),
    (1933, "Juventus", "Bologna FC"): (4, 1, OGOL_WIKI),
    (1934, "US Alessandria 1912", "AS Roma"): (1, 6, OGOL_WIKI + "; os pontos da RSSSF também (Roma 35, Alessandria 29)"),
    (1958, "Calcio Padova", "Lazio Roma"): (3, 1, OGOL_WIKI),
}

# resultado dado no tribunal (W.O. técnico): (ano, mandante, visitante) -> (gols, gols, motivo). Fica `awd`.
TRIBUNAL: dict[tuple, tuple] = {
    (2005, "A.C.R. Messina", "Empoli FC"): (0, 3, "abandonado aos 89 minutos com 1-2; vitória de 3-0 dada ao Empoli "
                                                  "(RSSSF; ogol e Wikipédia contam 0-3). O engsoccerdata, o football-data e a "
                                                  "ESPN trazem o 1-2 de campo"),
    (2020, "Hellas Verona", "AS Roma"): (3, 0, "0-0 em campo; a Roma escalou um jogador irregular e perdeu por 3-0 (ogol: "
                                               "\"DA\"; as tabelas da RSSSF e da Wikipédia contam 3-0). O engsoccerdata traz 0-0"),
}

# mando trocado na base: (ano, data, mandante da base, visitante da base) -> motivo. O jogo vira visitante x mandante,
# com o placar invertido (o ogol traz o mesmo erro; a base ficava com o par repetido na temporada)
INVERTIDOS = {
    (1965, "1965-11-21", "Torino FC", "Juventus"): "a RSSSF traz Juventus 2-0 Torino na 10ª rodada; no returno, Torino 0-0 "
                                                   "Juventus",
    (1965, "1966-01-23", "Bologna FC", "Cagliari Calcio"): "a RSSSF traz Cagliari 1-3 Bologna na 18ª rodada, jogado em Bolonha; "
                                                           "no turno, Bologna 1-0 Cagliari",
}

# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
WIKI_GOLS = "a tabela da Wikipédia erra gols (ou vitórias e empates) de alguns clubes; a base e o ogol concordam jogo a jogo e os " \
            "pontos da RSSSF fecham com os jogos"
EXPLICACOES: dict[int, list[str]] = {
    1929: [WIKI_GOLS],
    1930: [WIKI_GOLS + ", menos o Brescia: a RSSSF dá 32 pontos, mas a base, o ogol e a Wikipédia dão 13 vitórias e 8 "
           "empates (34 pontos)"],
    1945: ["Andrea Doria x Sampierdarenese (21/10/1945): o ogol traz 0-1 e a base 0-0. Os grupos de 1945/46 não têm tabela "
           "publicada legível para desempatar: fica a base"],
    1947: ["a base traz só 380 dos 420 jogos (21 clubes): os que faltam entram pelo ogol, e as tabelas da RSSSF e da Wikipédia "
           "fecham com o conjunto"],
    1948: [WIKI_GOLS + " (Bologna: a Wikipédia dá 11 vitórias e 18 empates; os jogos e a RSSSF, 12 e 17)"],
    1952: [WIKI_GOLS, "a base traz Novara 3-2 Pro Patria duas vezes; o ogol mostra que o jogo de 03/05/1953 foi Pro Patria 2-3 "
           "Novara (o returno)"],
    1959: ["Genoa: 18 pontos a menos (suborno), e mandado para a Serie B; a Wikipédia desconta, a classificação da RSSSF não"],
    1962: [WIKI_GOLS],
    1963: [WIKI_GOLS, "os dois jogos de 07/06/1964 que só o ogol traz são desempates (spareggi): Bologna 2-0 Inter, pelo "
           "título, e Sampdoria 2-0 Modena, pelo rebaixamento. Ficam de fora"],
    1993: ["a tabela da Wikipédia dá à Cremonese 8 vitórias e 16 empates; os jogos e a RSSSF dão 9 e 14 (os mesmos 32 pontos)"],
    2004: ["os dois jogos de junho de 2005 que só o ogol traz (Parma x Bologna) são o desempate (spareggio) de rebaixamento: "
           "ficam de fora"],
    2005: ["Calciopoli: a ordem oficial (Wikipédia) põe a Juventus em último e desconta pontos de Fiorentina, Lazio e Milan; "
           "a Inter recebeu o título"],
}

COMPETICAO = {
    "slug": "ita-1", "nome": "Campeonato Italiano", "nome_curto": "Italiano", "tipo": "liga", "nivel": 1,
    "pais": "ITA", "pais_nome": "Itália", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Italiano", "menu_painel": "Itália · 1ª divisão",
    "do_painel": "do Campeonato Italiano", "o_painel": "o Campeonato Italiano",
    "observacao": "Serie A desde a criação do grupo único (1929/30). Sem 1943/44 e 1944/45 (Segunda Guerra). 1945/46 foi a "
                  "Divisione Nazionale: grupos Norte e Centro-Sul e grupo final. Não inclui os desempates (spareggi) de "
                  "título e de rebaixamento nem os campeonatos de antes de 1929/30 (grupos regionais e finais).",
}


def ler_csv(arq: Path) -> list[dict]:
    with arq.open(encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def data_fd(s: str) -> str:
    d, m, y = s.split("/")
    y = int(y) + (2000 if len(y) == 2 and int(y) < 50 else 1900 if len(y) == 2 else 0)
    return f"{y:04d}-{int(m):02d}-{int(d):02d}"


def minuto(s: str | None) -> tuple[int | None, int | None]:
    m = re.match(r"^(\d+)'?(?:\+(\d+)'?)?", s or "")
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else (None, None)


def faixa(anos) -> str:
    a = sorted(anos)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else f"{a[0]}"


def chave(nome: str, a: int, fonte: str) -> str:
    c = clubes.esd(nome, a)
    if c is None:
        raise SystemExit(f"{temporada(a)}: nome do {fonte} sem cadastro: {nome}")
    return c


# ------------------------------------------------------------------ fontes
def carregar_base() -> dict[int, list[dict]]:
    base = defaultdict(list)
    for x in ler_csv(DADOS / "engsoccerdata" / "italy_tier1.csv"):
        a = int(x["Season"])
        base[a].append({"data": x["Date"], "m": chave(x["home"], a, "engsoccerdata"), "v": chave(x["visitor"], a, "engsoccerdata"),
                        "nm": x["home"], "gm": int(x["hgoal"]), "gv": int(x["vgoal"]), "fase": "Liga", "grupo": None,
                        "fonte": "engsoccerdata"})
    for a in SO_FD:   # temporadas que o engsoccerdata não tem: base pelo football-data
        for x in ler_csv(DADOS / "football-data" / f"I1_{str(a)[-2:]}{str(a + 1)[-2:]}.csv"):
            if not x.get("HomeTeam"):
                continue
            base[a].append({"data": data_fd(x["Date"]), "m": chave(x["HomeTeam"], a, "football-data"),
                            "v": chave(x["AwayTeam"], a, "football-data"), "nm": x["HomeTeam"], "gm": int(x["FTHG"]),
                            "gv": int(x["FTAG"]), "fase": "Liga", "grupo": None, "fonte": "football-data"})
    for (a, d, m, v), motivo in INVERTIDOS.items():
        j = next(j for j in base[a] if (j["data"], j["m"], j["v"]) == (d, m, v))
        j.update(m=v, v=m, gm=j["gv"], gv=j["gm"], invertido=motivo)
    return base


def carregar_fd() -> dict[int, dict]:
    res = {}
    for a in range(1993, 2026):
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        jogos = {}
        for x in ler_csv(DADOS / "football-data" / f"I1_{cod}.csv"):
            if not x.get("HomeTeam"):
                continue
            jogos[(chave(x["HomeTeam"], a, "football-data"), chave(x["AwayTeam"], a, "football-data"))] = x
        res[a] = jogos
    return res


class Mapa(dict):
    """Código do clube na outra fonte -> chave. `get(cod, ano)` usa o voto da temporada quando há."""
    def __init__(self, geral: dict, por_ano: dict):
        super().__init__(geral)
        self.por_ano = por_ano

    def get(self, cod, ano=None):
        return self.por_ano.get((cod, ano)) or super().get(cod)


def votar(base: dict[int, list[dict]], outra: dict[int, list[dict]], campo_m: str, campo_v: str) -> Mapa:
    """Código do clube na outra fonte -> chave, por votação: jogo de mesma data (±1 dia) e mesmo placar, quando só um
    jogo da base serve."""
    votos: dict[str, Counter] = defaultdict(Counter)
    votos_ano: dict[tuple, Counter] = defaultdict(Counter)
    for a, jogos in outra.items():
        por_dia = defaultdict(list)
        for b in base.get(a, []):
            por_dia[(b["data"], b["gm"], b["gv"])].append(b)
        for j in jogos:
            if j.get("gm") is None:
                continue
            d = date.fromisoformat(j["data"])
            cand = [b for k in (-1, 0, 1) for b in por_dia.get(((d + timedelta(days=k)).isoformat(), j["gm"], j["gv"]), [])]
            if len(cand) == 1:
                for campo, lado in ((campo_m, "m"), (campo_v, "v")):
                    votos[j[campo]][cand[0][lado]] += 1
                    votos_ano[(j[campo], a)][cand[0][lado]] += 1
    return Mapa({k: c.most_common(1)[0][0] for k, c in votos.items()},
                {k: c.most_common(1)[0][0] for k, c in votos_ano.items()})


def carregar_ogol() -> dict[int, list[dict]]:
    res = {}
    for a in TEMPORADAS:
        arq = DADOS / "ogol" / f"ita1_{a}.json"
        if arq.exists():
            res[a] = [dict(j, gm=j["gols_mandante"], gv=j["gols_visitante"]) for j in json.loads(arq.read_text(encoding="utf-8"))]
    return res


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for a in range(2001, 2026):
        arq = DADOS / "espn" / f"ita1_{a}.json"
        if not arq.exists():
            continue
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(ROMA).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
                              gv=int(j["gols_visitante"])))
        res[a] = jogos
    return res


def carregar_wiki() -> dict[int, list[dict]]:
    res = {}
    for a in TEMPORADAS:
        arq = DADOS / "wikipedia" / f"{wiki_titulo(a)}.wiki"
        if not arq.exists():
            continue
        txt = arq.read_text(encoding="utf-8")
        modelo = arq.with_name(f"{wiki_titulo(a)} (tabela).wiki")   # tabela num modelo à parte (temporadas recentes)
        if modelo.exists():
            txt += "\n" + modelo.read_text(encoding="utf-8")
        tabs = wiki_tabelas(txt)
        if tabs:
            res[a] = tabs
    return res


def links(cel: str) -> list[str]:
    """Nomes dos links de uma célula ("[[Inter Milan|Ambrosiana]]" -> "Ambrosiana"), na ordem."""
    return [(y or x).strip() for x, y in re.findall(r"\[\[([^|\]]+)(?:\|([^\]]*))?\]\]", cel)]


def clube_link(cel: str, a: int) -> str | None:
    """Clube de uma célula da Wikipédia: pelos links ou, sem link, pelo texto ("Ambrosiana-Inter (3)")."""
    texto = re.sub(r"<sup>.*?</sup>|<ref.*?(?:/>|</ref>)|\{\{[^{}]*\}\}", "", cel)
    texto = re.sub(r"^\s*(?:bgcolor|style)=[^|]*\|", "", texto)
    for nome in links(cel) + [re.sub(r"\s*\(\d+\)\s*$", "", limpar(texto)).strip()]:
        c = clubes.esd(nome, a)
        if c:
            return c
    return None


SERIE = r"(?:Serie A(?:-B)?|Italian Football Championship|Divisione Nazionale)"


def campeoes_wiki() -> dict[int, str | None]:
    """Campeão de cada temporada pela "List of Italian football champions" (linha: temporada || campeão || ...).
    None = título não atribuído (2004/05, tirado da Juventus no Calciopoli)."""
    arq = DADOS / "wikipedia" / "List of Italian football champions.wiki"
    res: dict[int, str | None] = {}
    if not arq.exists():
        return res
    for linha in arq.read_text(encoding="utf-8").split("\n|-"):
        m = re.match(rf"\s*\|\s*\[\[(\d{{4}})[–-]\d{{2,4}} {SERIE}[^\]]*\]\]\s*\|\|(.*?)\|\|", linha)
        if not m:
            continue
        a, cel = int(m.group(1)), m.group(2)
        if "<del>" in cel or "stripped" in cel:
            res[a] = None
        elif clube_link(cel, a):
            res[a] = clube_link(cel, a)
    return res


# ------------------------------------------------------------------ RSSSF: tabela final, quando legível
LINHA_A = re.compile(r"^\s*(\d+)\s*\.?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(-?\d+)\b(.*)$")   # J V E D GP-GC Pts
LINHA_B = re.compile(r"^\s*(\d+)\s*\.?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\b(.*)$")         # Pts J V E D GP GC


def tabela_rsssf(a: int, clubes_ano: set, pv: int) -> list[dict] | None:
    """Primeiro bloco de linhas de tabela cujos clubes são os da temporada, em um dos dois formatos comuns da RSSSF.
    A linha só vale se J = V + E + D."""
    arq = DADOS / "rsssf" / rsssf_url(a).rsplit("/", 1)[1]
    if not arq.exists():
        return None
    t = __import__("html").unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")
    linhas = t.split("\n")
    for regex, ordem in ((LINHA_A, "jvedgp"), (LINHA_B, "pjvedgg")):
        bloco: list[dict] = []
        for l in linhas + [""]:
            m = regex.match(l)
            x = None
            if m:
                g = [int(v) for v in m.groups()[2:9]]
                if ordem == "jvedgp":
                    j, v, e, d, gp, gc, p = g
                else:
                    p, j, v, e, d, gp, gc = g
                if j == v + e + d and j > 0:
                    x = {"posicao": int(m.group(1)), "nome": re.sub(r"\s*\(\d\)\s*$", "", m.group(2)).strip(), "jogos": j,
                         "vitorias": v, "empates": e, "derrotas": d, "gols_pro": gp, "gols_contra": gc, "pontos": p}
            if x:
                bloco.append(x)
                continue
            if bloco and re.match(r"^\s*(-{5,}\s*)?$", l) and len(bloco) < len(clubes_ano):
                continue   # linha de separação dentro da tabela
            if bloco:
                for b in bloco:
                    b["clube"] = clubes.esd(b["nome"], a) or clubes.esd(re.sub(r"\s*\(.*?\)", "", b["nome"]), a)
                if len(bloco) == len(clubes_ano) and {b["clube"] for b in bloco} == clubes_ano:
                    return bloco
                bloco = []
    return None


def pontos_rsssf(a: int, clubes_ano: set) -> dict[str, int] | None:
    """Páginas antigas: sem tabela final, mas com a "Classifica" depois de cada rodada ("Juventus 54; Fiorentina 45;
    Bologna e Padova 35; ..."). Devolve os pontos da última, se ela tem todos os clubes da temporada."""
    arq = DADOS / "rsssf" / rsssf_url(a).rsplit("/", 1)[1]
    if not arq.exists():
        return None
    t = __import__("html").unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")
    fim = t.find("CLASSIFICA MARCATORI")
    blocos = re.findall(r"Classifica\s*-\s*(.*?)(?:\n\s*\n|\n\S)", t[:fim if fim > 0 else len(t)], re.S)
    if not blocos:
        return None
    res = {}
    for parte in re.sub(r"\s+", " ", blocos[-1]).split(";"):
        m = re.match(r"^\s*(.*?)\s+(-?\d+)\s*\.?\s*$", parte)
        if not m:
            return None
        for nome in re.split(r",\s*|\s+(?:e|and)\s+", m.group(1)):
            c = clubes.esd(nome.strip(), a)
            if c is None:
                return None
            res[c] = int(m.group(2))
    return res if set(res) == clubes_ano else None


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pv: int) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            if gp > gc:
                x[1] += 1; x[6] += pv
            elif gp == gc:
                x[2] += 1; x[6] += 1
            else:
                x[3] += 1
    return t


def ordenar(t: dict[str, list[int]], ajuste: dict[str, int], criterio: str, jogos: list[dict] | None = None, pv: int = 2) -> list[str]:
    """criterio: "media" (pontos, média de gols), "saldo" (pontos, saldo, gols pró) ou "confronto" (pontos; entre os
    empatados, pontos e saldo nos jogos entre eles; depois saldo e gols pró)."""
    def pts(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, p = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        return (-(gp - gc), -gp)
    if criterio != "confronto":
        return sorted(t, key=lambda c: (-pts(c), *geral(c)))
    grupos = defaultdict(list)
    for c in t:
        grupos[pts(c)].append(c)
    res = []
    for p in sorted(grupos, reverse=True):
        g = grupos[p]
        if len(g) > 1 and jogos is not None:
            mini = calcular([j for j in jogos if j["m"] in g and j["v"] in g], pv)
            g.sort(key=lambda c: (-mini[c][6], -(mini[c][4] - mini[c][5]), *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def reparar(a: int, base: dict[int, list[dict]], ogol: list[dict], mapa_ogol: Mapa, ocorr, inicio_prox: str) -> list[dict]:
    """Temporada em que a base não fecha (pares repetidos ou faltando): o calendário do ogol diz quais jogos são da
    temporada. Para cada jogo do ogol, fica o jogo da base com o mesmo par e o mesmo placar: desta temporada ou, se a
    base o pôs na seguinte com data de antes do início dela (`inicio_prox`), da seguinte. Sem jogo na base, entra o do
    ogol."""
    pool = base.get(a, []) + [j for j in base.get(a + 1, []) if j["data"] < inicio_prox]
    usados, res, do_ogol, data_trocada = set(), [], [], []
    for o in ogol:
        m, v = mapa_ogol.get(o["mandante_id"], a), mapa_ogol.get(o["visitante_id"], a)
        cand = [j for j in pool if id(j) not in usados and (j["m"], j["v"]) == (m, v)
                and (o["gm"] is None or (j["gm"], j["gv"]) == (o["gm"], o["gv"]))]   # "DA" no ogol: sem placar
        if cand:
            j = min(cand, key=lambda j: abs((date.fromisoformat(j["data"]) - date.fromisoformat(o["data"])).days))
            usados.add(id(j))
            if abs((date.fromisoformat(j["data"]) - date.fromisoformat(o["data"])).days) > 20:
                data_trocada.append(f"{j['m']} x {j['v']} ({j['data']} -> {o['data']})")
                j = dict(j, data=o["data"])
            res.append(j)
        elif o["gm"] is None:
            ocorr[a].append(f"jogo do ogol sem placar (DA) e sem par na base: {o['mandante']} x {o['visitante']} ({o['data']})")
        else:
            res.append({"data": o["data"], "m": m, "v": v, "nm": o["mandante"], "gm": o["gm"], "gv": o["gv"], "fase": "Liga",
                        "grupo": None, "fonte": "ogol"})
            do_ogol.append(f"{m} {o['gm']}-{o['gv']} {v} ({o['data']})")
    sobra = [j for j in base.get(a, []) if id(j) not in usados]
    ocorr[a].append(f"a base não fecha nesta temporada ({len(base.get(a, []))} jogos): montada pelo calendário do ogol "
                    f"({len(ogol)} jogos), com {len(res) - len(do_ogol)} jogos da base")
    if do_ogol:
        ocorr[a].append(f"{len(do_ogol)} jogos só no ogol, que entram com o placar do ogol: {'; '.join(do_ogol[:6])}"
                        + (" ..." if len(do_ogol) > 6 else ""))
    if data_trocada:
        ocorr[a].append(f"{len(data_trocada)} jogos com data errada na base, trocada pela do ogol: {'; '.join(data_trocada[:4])}"
                        + (" ..." if len(data_trocada) > 4 else ""))
    if sobra:
        ocorr[a].append(f"{len(sobra)} jogos da base fora do calendário do ogol, descartados: "
                        f"{'; '.join(f'{j['m']} {j['gm']}-{j['gv']} {j['v']} ({j['data']})' for j in sobra[:6])}")
    # o que foi usado da temporada seguinte sai de lá
    if a + 1 in base:
        base[a + 1] = [j for j in base[a + 1] if id(j) not in usados]
    return res


def divisione(jogos: list[dict]) -> None:
    """1945/46: marca a fase e o grupo de cada jogo. Grupo final: os 8 clubes que jogam contra clubes do outro grupo;
    os jogos entre eles a partir do primeiro desses cruzamentos são da fase final."""
    adj = defaultdict(set)
    for j in jogos:
        adj[j["m"]].add(j["v"]); adj[j["v"]].add(j["m"])
    norte = {"AC Milan", "Inter", "Juventus", "Torino FC"}   # semente: grandes do Norte
    for _ in range(3):
        norte |= {c for c in adj if len(adj[c] & norte) >= 4 and c not in {"SSC Napoli", "AS Bari", "AS Roma", "AS Livorno"}}
    finalistas = {"AC Milan", "Inter", "Juventus", "Torino FC", "SSC Napoli", "AS Bari", "AS Roma", "AS Livorno"}
    corte = min(j["data"] for j in jogos if (j["m"] in norte) != (j["v"] in norte))
    for j in jogos:
        if j["m"] in finalistas and j["v"] in finalistas and j["data"] >= corte:
            j["fase"], j["grupo"] = "Fase final", "Final"
        else:
            j["fase"], j["grupo"] = "Grupos", ("Norte" if j["m"] in norte else "Centro-Sul")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    base = carregar_base()
    fd = carregar_fd()
    ogol = carregar_ogol()
    espn = carregar_espn()
    wiki = carregar_wiki()
    camp_wiki = campeoes_wiki()
    mapa_ogol = votar(base, ogol, "mandante_id", "visitante_id")
    mapa_espn = votar(base, espn, "mandante_id", "visitante_id")

    nomes = defaultdict(lambda: defaultdict(set))   # chave -> "fonte:nome" -> anos
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel = []
    criterios = {}

    for a in TEMPORADAS:
        T = temporada(a)
        ocorr[a].extend(EXPLICACOES.get(a, []))
        jogos = base[a]
        if a == DIVISIONE:
            divisione(jogos)
        pares = Counter((j["fase"], j["m"], j["v"]) for j in jogos)
        clubes_ano = sorted({j["m"] for j in jogos} | {j["v"] for j in jogos})
        n = len(clubes_ano)
        if a != DIVISIONE and (any(k > 1 for k in pares.values()) or len(jogos) != n * (n - 1)):
            inicio_prox = min((o["data"] for o in ogol.get(a + 1, [])), default="9999")
            jogos = base[a] = reparar(a, base, ogol.get(a, []), mapa_ogol, ocorr, inicio_prox)
            clubes_ano = sorted({j["m"] for j in jogos} | {j["v"] for j in jogos})
            n = len(clubes_ano)
        pares = Counter((j["fase"], j["m"], j["v"]) for j in jogos)
        assert all(k == 1 for k in pares.values()), (a, [p for p, k in pares.items() if k > 1])
        if a != DIVISIONE:
            assert len(jogos) == n * (n - 1), (a, len(jogos), n)
        por_par = {(j["fase"], j["m"], j["v"]): j for j in jogos}
        for j in jogos:
            nomes[j["m"] if not j.get("invertido") else j["v"]][f"{j['fonte']}:{j['nm']}"].add(a)
            if j.get("invertido"):
                ocorr[a].append(f"mando corrigido: {j['m']} {j['gm']}-{j['gv']} {j['v']} ({j['data']}); a base e o ogol trazem o "
                                f"mando trocado — {j['invertido']}")
            if (a, j["m"], j["v"]) in CORRECOES:
                gm, gv, motivo = CORRECOES[(a, j["m"], j["v"])]
                ocorr[a].append(f"placar corrigido: {j['m']} x {j['v']} de {j['gm']}-{j['gv']} para {gm}-{gv} — {motivo}")
                j["gm"], j["gv"] = gm, gv
            if (a, j["m"], j["v"]) in TRIBUNAL:
                gm, gv, motivo = TRIBUNAL[(a, j["m"], j["v"])]
                ocorr[a].append(f"resultado do tribunal: {j['m']} x {j['v']} fica {gm}-{gv} (base {j['gm']}-{j['gv']}) — {motivo}")
                j.update(gm=gm, gv=gv, especial="awd", campo=f"{j['gm']}-{j['gv']}")
        pv = 2 if a <= 1993 else 3

        # ---- ogol: rodada e conferência
        og_ok = 0
        for o in ogol.get(a, []):
            m, v = mapa_ogol.get(o["mandante_id"], a), mapa_ogol.get(o["visitante_id"], a)
            if m and v:
                nomes[m][f"ogol:{o['mandante']}"].add(a)
                nomes[v][f"ogol:{o['visitante']}"].add(a)
            # o mesmo par pode ter mais de um candidato (1945/46: grupo e fase final; mando corrigido em INVERTIDOS, em
            # que o ogol traz o par trocado): fica o de data mais próxima
            cands = [j for (f, jm, jv), j in por_par.items() if "ogol" not in j and
                     ((jm, jv) == (m, v) or ((jm, jv) == (v, m) and j.get("invertido")))]
            cands.sort(key=lambda j: abs((date.fromisoformat(j["data"]) - date.fromisoformat(o["data"])).days))
            b = cands[0] if cands else None
            if b is None:
                ocorr[a].append(f"jogo do ogol sem par na base: {o['mandante']} {o['resultado']} {o['visitante']} ({o['data']}, "
                                f"{o['fase']})")
                continue
            b["ogol"] = o
            og_ok += 1
            placar_o = (o["gm"], o["gv"]) if (b["m"], b["v"]) == (m, v) else (o["gv"], o["gm"])   # mando trocado (INVERTIDOS)
            if o["gm"] is not None and placar_o != (b["gm"], b["gv"]):
                ocorr[a].append(f"placar diferente no ogol — {b['m']} x {b['v']} ({b['data']}): base {b['gm']}-{b['gv']}, "
                                f"ogol {o['gm']}-{o['gv']}")
        for j in jogos:
            j["rodada"] = (j.get("ogol") or {}).get("rodada")
        sem_rodada = [j for j in jogos if not j["rodada"]]
        if sem_rodada:
            ocorr[a].append(f"{len(sem_rodada)} jogos sem rodada do ogol (ex.: {sem_rodada[0]['m']} x {sem_rodada[0]['v']})")
        datas_dif = [j for j in jogos if j.get("ogol") and j["ogol"]["data"] != j["data"]]
        if datas_dif:
            x = datas_dif[0]
            ocorr[a].append(f"data diferente no ogol em {len(datas_dif)} jogos (ex.: {x['m']} x {x['v']}: base {x['data']}, "
                            f"ogol {x['ogol']['data']}); fica a da base")

        # ---- football-data
        if a in fd:
            for (m, v), x in fd[a].items():
                nomes[m][f"football-data:{x['HomeTeam']}"].add(a)
                b = por_par.get(("Liga", m, v))
                if b is None:
                    ocorr[a].append(f"jogo do football-data sem par na base: {m} x {v}")
                    continue
                b["fd"] = x
                if (int(x["FTHG"]), int(x["FTAG"])) != (b["gm"], b["gv"]):
                    ocorr[a].append(f"placar diferente no football-data — {m} x {v}: base {b['gm']}-{b['gv']}, "
                                    f"football-data {x['FTHG']}-{x['FTAG']}")
            if len(fd[a]) != len(jogos):
                ocorr[a].append(f"football-data com {len(fd[a])} jogos (base {len(jogos)})")

        # ---- ESPN (entre eventos do mesmo par fica o de placar igual ao da base e com os gols fechando)
        es_ok = 0
        cand = defaultdict(list)
        for e in espn.get(a, []):
            m, v = mapa_espn.get(e["mandante_id"], a), mapa_espn.get(e["visitante_id"], a)
            if ("Liga", m, v) not in por_par:
                ocorr[a].append(f"jogo da ESPN sem par na base: {e['mandante']} {e['gm']}-{e['gv']} {e['visitante']} ({e['data']})")
                continue
            cand[(m, v)].append(e)
        descartados = 0
        for (m, v), es in cand.items():
            b = por_par[("Liga", m, v)]
            iguais = [e for e in es if (e["gm"], e["gv"]) == (b["gm"], b["gv"])]

            def fecha(e):
                g = [l for l in e["lances"] if l["gol"]]
                return all(l["lado"] in ("home", "away") for l in g) and \
                    (sum(l["lado"] == "home" for l in g), sum(l["lado"] == "away" for l in g)) == (b["gm"], b["gv"])
            e = sorted(iguais or es, key=lambda e: (not fecha(e), int(e["id"])))[0]
            descartados += len(es) - 1
            nomes[m][f"espn:{e['mandante']}"].add(a)
            b["espn"] = e
            es_ok += 1
            if not iguais:
                ocorr[a].append(f"placar diferente na ESPN — {m} x {v} ({b['data']}): base {b['gm']}-{b['gv']}, ESPN {e['gm']}-{e['gv']}")
        if descartados:
            ocorr[a].append(f"{descartados} eventos repetidos da ESPN descartados (fica o evento com o placar da base)")
        if a in espn and es_ok != len(jogos):
            falta = [j for j in jogos if "espn" not in j]
            ocorr[a].append(f"ESPN com {es_ok} de {len(jogos)} jogos (ex. sem ESPN: {falta[0]['m']} x {falta[0]['v']}, {falta[0]['data']})")

        # ---- tabelas publicadas e conferência
        if a == DIVISIONE:
            ref = calcular([j for j in jogos if j["fase"] == "Fase final"], pv)
            tab_jogos = [j for j in jogos if j["fase"] == "Fase final"]
        else:
            ref = calcular(jogos, pv)
            tab_jogos = jogos
        clubes_tab = sorted(ref)
        ajuste: dict[str, int] = {}

        def sobrepoe(tb):
            return len({clubes.esd(x["nome"], a) for x in tb["times"]} & set(clubes_tab))
        w = max(wiki.get(a, []), key=lambda tb: (sobrepoe(tb) - abs(len(tb["times"]) - len(clubes_tab)),), default=None)
        if w and sobrepoe(w) < len(clubes_tab) // 2:
            w = None
        if w:
            for x in w["times"]:
                c = clubes.esd(x["nome"], a)
                if c is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
                x["clube"] = c
                if x["ajuste"]:
                    ajuste[c] = x["ajuste"]
            if w["pontos_vitoria"] != pv:
                ocorr[a].append(f"Wikipédia com {w['pontos_vitoria']} pontos por vitória (aqui {pv})")
        rs = tabela_rsssf(a, set(clubes_tab), pv)
        if rs:
            for x in rs:   # punição que só a RSSSF traz
                c = ref.get(x["clube"])
                if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                        and x["pontos"] != c[6] and x["clube"] not in ajuste:
                    ajuste[x["clube"]] = x["pontos"] - c[6]
                    ocorr[a].append(f"punição tirada da tabela da RSSSF: {clubes.exibicao(x['clube'])} {x['pontos'] - c[6]:+d} pontos")
        conferidas, divergentes, confere = 0, 0, {}
        publicadas = []
        if rs:
            publicadas.append(("RSSSF", rsssf_url(a), rs))
        if w:
            publicadas.append(("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                               [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                     pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in w["times"]]))
        pts_rs = pontos_rsssf(a, set(clubes_tab)) if not rs and a != DIVISIONE else None
        if pts_rs:   # só os pontos (última "Classifica" da RSSSF)
            dif = [f"{c} RSSSF {p} jogos {ref[c][6] + ajuste.get(c, 0)}" for c, p in sorted(pts_rs.items())
                   if p != ref[c][6] + ajuste.get(c, 0)]
            if len(dif) > len(pts_rs) // 3:   # a última "Classifica" da página não é a da rodada final
                ocorr[a].append(f"a última classificação da página da RSSSF não é a final ({len(dif)} clubes com outros pontos): "
                                f"não serve para conferir")
                pts_rs, dif = None, []
        if pts_rs:
            confere["RSSSF (pontos)"] = not dif
            if dif:
                divergentes += 1
                ocorr[a].append(f"pontos da última classificação da RSSSF x jogos — {'; '.join(dif)}")
            else:
                conferidas += 1
        if not publicadas and not pts_rs:
            ocorr[a].append("sem tabela publicada legível (RSSSF e Wikipédia)")
        for fonte, url, linhas in publicadas:
            erro = []
            if sorted(x["clube"] for x in linhas) != clubes_tab:
                erro.append(f"clubes diferentes: {sorted(set(x['clube'] for x in linhas) ^ set(clubes_tab))}")
            for x in linhas:
                c = ref.get(x["clube"])
                if c is None:
                    continue
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = c[:6] + [c[6] + ajuste.get(x["clube"], 0)]
                if pub != meu:
                    erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": "Fase final" if a == DIVISIONE else "Liga", "grupo": None, "posicao": x["posicao"],
                    "nome_fonte": x["nome"], "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"],
                    "empates": x["empates"], "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"],
                    "pontos": x["pontos"], "fonte": url})
            confere[fonte] = not erro
            if erro:
                divergentes += 1
                for e in erro:
                    ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {e}")
            else:
                conferidas += 1

        # ordem oficial: Wikipédia; se ela não fecha e a RSSSF fecha, a da RSSSF; sem nenhuma, calculada
        if w and (confere.get("Wikipédia") or not confere.get("RSSSF")):
            ordem = [x["clube"] for x in w["times"]]
            fonte_ordem = "Wikipédia (ordem oficial)"
        elif rs:
            ordem = [x["clube"] for x in rs]
            fonte_ordem = "RSSSF (ordem oficial)"
            if w:
                ocorr[a].append("a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF")
        else:
            ordem = ordenar(ref, ajuste, "saldo", tab_jogos, pv)
            fonte_ordem = "calculada"
        if rs and w and fonte_ordem.startswith("Wikipédia") and [x["clube"] for x in rs] != ordem:
            dif = [(r["clube"], c) for r, c in zip(rs, ordem) if r["clube"] != c]
            ocorr[a].append(f"ordem diferente entre RSSSF e Wikipédia em {len(dif)} posições (ex.: RSSSF {dif[0][0]}, Wikipédia "
                            f"{dif[0][1]}); fica a da Wikipédia")
        tentativas = {cr: ordenar(ref, ajuste, cr, tab_jogos, pv) for cr in ("confronto", "saldo", "media")}
        ok = [cr for cr, o in tentativas.items() if o == ordem]
        criterio = ok[0] if ok else min(tentativas, key=lambda cr: sum(x != y for x, y in zip(tentativas[cr], ordem)))
        if not ok:
            dif = [c for c, d in zip(ordem, tentativas[criterio]) if c != d]
            ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo ({criterio}) difere em "
                            f"{len(dif)} posições (ex.: {dif[:2]}). Na Itália, empate em pontos no título ou no rebaixamento "
                            f"era decidido em jogo-desempate (spareggio) ou deixado como posição dividida")
        criterios[a] = (criterio, bool(ok))

        # 1945/46: a classificação final é a do grupo final; os outros clubes seguem pela campanha nos grupos
        if a == DIVISIONE:
            grupos_calc = calcular([j for j in jogos if j["fase"] == "Grupos"], pv)
            resto = ordenar({c: grupos_calc[c] for c in grupos_calc if c not in ordem}, {}, "saldo")
            ordem_final = ordem + resto
            calc_final = calcular(jogos, pv)
        else:
            ordem_final, calc_final = ordem, ref

        # rebaixados: quem não está na 1ª divisão no ano seguinte (última temporada: marca da Wikipédia)
        prox = next((b for b in TEMPORADAS if b > a), None)
        if prox is not None:
            prox_clubes = {j["m"] for j in base[prox]} | {j["v"] for j in base[prox]}
            rebaixados = {c for c in clubes_ano if c not in prox_clubes}
        else:
            textos = {k[5:]: limpar(v) for k, v in w["params"].items() if k.startswith("text_")}
            rebaixados = {x["clube"] for x in w["times"] if "relegat" in textos.get(x["resultado"], "").lower()}
        campeao, vice = ordem_final[0], ordem_final[1]
        sem_titulo = a in camp_wiki and camp_wiki[a] is None
        if sem_titulo:
            ocorr[a].append(f"título não atribuído (lista de campeões da Wikipédia); {clubes.exibicao(campeao)} terminou em 1º")
        elif camp_wiki.get(a) and camp_wiki[a] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da Wikipédia: {camp_wiki[a]} (tabela: {campeao})")
        for pos, c in enumerate(ordem_final, 1):
            j_, v_, e_, d_, gp, gc, p = calc_final[c]
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + ajuste.get(c, 0), "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if pos == 1 and not sem_titulo else "rebaixado" if c in rebaixados else None,
                "fonte": fonte_ordem if c in ordem else "calculada (campanha nos grupos)",
                "observacao": ((w and next((x["hth"] or x["nota"] for x in w["times"] if x["clube"] == c), None)) or None)
                if c in ordem else "não foi ao grupo final"})

        # ---- partidas, gols, cartões, estatísticas
        jogos.sort(key=lambda j: (j["data"], j["rodada"] or 0, j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
            hora = None
            if x and x.get("Time"):   # o football-data dá a hora do Reino Unido
                d = datetime.fromisoformat(f"{data_fd(x['Date'])}T{x['Time']}").replace(tzinfo=LONDRES).astimezone(ROMA)
                hora = d.strftime("%H:%M")
            elif e:
                local = e["utc"].astimezone(ROMA)
                if local.date().isoformat() == j["data"]:
                    hora = local.strftime("%H:%M")
            ids = [f"ogol:{o['id']}"] if o else []
            if e:
                ids.append(f"espn:{e['id']}")
            fontes = [j["fonte"]] + (["ogol"] if o and j["fonte"] != "ogol" else []) + (["football-data"] if x else []) \
                + (["ESPN"] if e else [])
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
                "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": "awd" if j.get("especial") or (o and o["resultado"] == "DA") else None,
                "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
                "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids),
                "gols_texto": None,
                "observacao": f"resultado dado no tribunal; em campo, {j['campo']}" if j.get("campo") else
                "resultado decidido pela federação (no ogol: \"DA\", decisão administrativa)"
                if o and o["resultado"] == "DA" else
                "mando corrigido (a base e o ogol trazem o mando trocado)" if j.get("invertido") else None,
                "arbitro": (x or {}).get("Referee") or None})
            gols_ano += j["gm"] + j["gv"]
            if e and e["lances"]:
                gl = [l for l in e["lances"] if l["gol"]]
                lado = {"home": j["m"], "away": j["v"]}
                if all(l["lado"] in lado for l in gl) and \
                        (sum(l["lado"] == "home" for l in gl), sum(l["lado"] == "away" for l in gl)) == (j["gm"], j["gv"]):
                    for l in gl:
                        mi, ac = minuto(l["minuto"])
                        tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(lado[l["lado"]]),
                                            "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                            "tipo": "contra" if l["contra"] else "penalti" if l["penalti"] else
                                            "falta" if "free-kick" in (l["tipo"] or "").lower() else "normal", "fonte": "ESPN"})
                    autor_ano += len(gl)
                elif gl:
                    ocorr[a].append(f"gols da ESPN não batem com o placar — {j['m']} {j['gm']}-{j['gv']} {j['v']}: "
                                    f"ESPN {sum(l['lado'] == 'home' for l in gl)}-{sum(l['lado'] == 'away' for l in gl)}"
                                    f"{' e gol sem clube' if not all(l['lado'] in lado for l in gl) else ''} (descartados)")
                for l in e["lances"]:
                    if (l["amarelo"] or l["vermelho"]) and l["lado"] in lado:
                        mi, ac = minuto(l["minuto"])
                        tab["cartoes"].append({"partida_id": pid, "clube": clubes.exibicao(lado[l["lado"]]),
                                               "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                               "cor": "vermelho" if l["vermelho"] else "amarelo", "fonte": "ESPN"})
            if x and x.get("HS"):
                def num(k):
                    v_ = x.get(k)
                    return int(float(v_)) if v_ not in (None, "") else None
                for c, s in ((j["m"], "H"), (j["v"], "A")):
                    tab["estatisticas"].append({"partida_id": pid, "clube": clubes.exibicao(c), "chutes": num(f"{s}S"),
                                                "chutes_alvo": num(f"{s}ST"), "faltas": num(f"{s}F"), "escanteios": num(f"{s}C"),
                                                "amarelos": num(f"{s}Y"), "vermelhos": num(f"{s}R"), "fonte": "football-data.co.uk"})

        # ---- classificação rodada a rodada (não em 1945/46, que teve grupos)
        if not sem_rodada and a != DIVISIONE:
            pos_reb = {p for p, c in enumerate(ordem_final, 1) if c in rebaixados}   # faixa: as posições finais de quem caiu
            for r in sorted({j["rodada"] for j in jogos}):
                ate = [j for j in jogos if j["rodada"] <= r]
                parcial = calcular(ate, pv)
                for pos, c in enumerate(ordenar(parcial, ajuste, criterio, ate, pv), 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        fontes_ed = ["engsoccerdata", "ogol"] + (["football-data"] if a in fd else []) + (["ESPN"] if a in espn else []) \
            + (["RSSSF"] if rs else []) + (["Wikipédia"] if w else [])
        pun = "; ".join(f"{clubes.exibicao(c)} {v:+d} pontos" for c, v in ajuste.items())
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pv,
                               "formato": "pontos corridos (turno e returno)" if a != DIVISIONE else
                               "grupos Norte (14) e Centro-Sul (11), em turno e returno; grupo final com os 4 primeiros de cada",
                               "campeao": None if sem_titulo else clubes.exibicao(campeao), "vice": clubes.exibicao(vice),
                               "fontes": " + ".join(fontes_ed),
                               "observacao": "; ".join(x for x in (f"punições: {pun}" if pun else "",
                                                                    "título não atribuído" if sem_titulo else "") if x) or None})
        crit_txt = {"confronto": "pontos, confronto direto, saldo de gols, gols pró", "saldo": "pontos, saldo de gols, gols pró",
                    "media": "pontos, média de gols (goal average)"}[criterio]
        if a == DIVISIONE:
            tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Grupos", "tipo": "grupos", "num_grupos": 2,
                                 "formato_serie": "pontos_corridos", "criterio": "pontos"})
            tab["fases"].append({"temporada": T, "ordem": 2, "fase": "Fase final", "tipo": "grupos", "num_grupos": 1,
                                 "formato_serie": "pontos_corridos", "criterio": "pontos"})
        else:
            tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Liga", "tipo": "liga", "num_grupos": None,
                                 "formato_serie": "pontos_corridos", "criterio": crit_txt})
        obs = [f"campeão {'não atribuído' if sem_titulo else clubes.exibicao(campeao)} (Wikipédia, lista de campeões: "
               f"{('não atribuído' if camp_wiki[a] is None else clubes.exibicao(camp_wiki[a])) if a in camp_wiki else '—'})"]
        if divergentes:
            obs.append("divergências explicadas no relatório")
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": n * (n - 1) if a != DIVISIONE else 348,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autor_ano, "observacao": "; ".join(obs)})
        linhas_rel.append((T, " + ".join(fontes_ed), n, len(jogos), og_ok, gols_ano, autor_ano, conferidas, divergentes,
                           "—" if sem_titulo else clubes.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos, ogol {og_ok}, tabelas {conferidas} ok / {divergentes} div, gols {gols_ano} "
              f"({autor_ano} c/ autor), critério {criterio}{'' if criterios[a][1] else ' (aprox.)'}, campeão "
              f"{'—' if sem_titulo else clubes.exibicao(campeao)}", flush=True)

    # ---- clubes
    for c, (exib, cidade, pais) in sorted(clubes.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": exib, "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = []
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_ogol, mapa_espn, criterios)


def artilheiros(ocorr) -> list[dict]:
    """Capocannoniere (Wikipédia, "Capocannoniere"): artilheiro de cada temporada; empate em várias linhas."""
    arq = DADOS / "wikipedia" / "Capocannoniere.wiki"
    if not arq.exists():
        return []
    txt = arq.read_text(encoding="utf-8")
    txt = txt[txt.index('{| class="wikitable sortable"'):]
    txt = txt[:txt.index("\n|}")]
    res = []
    # linha: "![[1931–32 Serie A|1931–32]]" e as células jogador(es) | nacionalidade | clube(s) | gols; empate separado
    # por <hr/> dentro da célula
    for bloco in txt.split("\n|-")[1:]:
        cab = re.search(rf"^!.*?\[\[(\d{{4}})[–-]\d{{2,4}} {SERIE}", bloco.strip(), re.M)
        if not cab or int(cab.group(1)) not in TEMPORADAS:
            continue
        ano = int(cab.group(1))
        cel = [c.strip() for c in re.findall(r"^\|(?!-)(.*)$", bloco, re.M)]
        if len(cel) < 4:
            ocorr[ano].append("artilheiro: linha da lista Capocannoniere sem as quatro colunas")
            continue
        jogadores = [(links(p) or [limpar(p)])[0] for p in re.split(r"<hr\s*/?>", cel[0])]
        clubes_cel = re.split(r"<hr\s*/?>", cel[2])
        gols = int(re.search(r"\d+", re.sub(r"<ref.*", "", cel[3])).group())   # "{{center|25}}"
        for i, jog in enumerate(jogadores):
            c = clube_link(clubes_cel[min(i, len(clubes_cel) - 1)], ano)
            res.append({"temporada": temporada(ano), "jogador": jog, "clube": clubes.exibicao(c) if c else None, "gols": gols,
                        "fonte": "Wikipédia (Capocannoniere)"})
            if c is None:
                ocorr[ano].append(f"artilheiro com clube sem cadastro: {jog} ({clubes_cel[min(i, len(clubes_cel) - 1)]})")
    return res


def relatorio(linhas, ocorr, tab, mapa_ogol, mapa_espn, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Italiano (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/ita-1/importar.py`. Pacote em `data/coleta/ita-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1929/30 a 2025/26 (Serie A; 1945/46 foi a Divisione Nazionale). Sem 1943/44 e 1944/45 "
        "(Segunda Guerra).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (ESPN), {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1929/30-2024/25;",
        "- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;",
        "- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários "
        "guardados em `data/cache/ogol-ita-1/` para os escudos;",
        "- ESPN (liga `ita.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;",
        "- RSSSF (Maurizio Mariani e outros): tabela final, nas temporadas em que a página traz uma tabela legível;",
        "- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e Capocannoniere.", "",
        "**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols "
        "pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando "
        "a soma bate com o placar. Hora local (Roma). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. "
        "2 pontos por vitória até 1993/94, 3 a partir de 1994/95. Placar diferente no ogol, no football-data ou na ESPN numa "
        "temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra "
        "fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em "
        "`importar.py`, com o motivo).", "",
        f"**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em "
        f"{cr['confronto']}, saldo de gols em {cr['saldo']}, média de gols em {cr['media']}); é ele que ordena a classificação "
        "rodada a rodada. Até 2004/05, empate em pontos no título ou no rebaixamento era decidido em jogo-desempate (spareggio), "
        "que não está no pacote.", "",
        "| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for T, f, n, j, og, g, au, ok, dv, camp, pun in linhas:
        out.append(f"| {T} | {f} | {n} | {j} ({og}) | {g} | {au} | {ok} / {dv} | {camp} | {pun or '—'} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for T, *_ in linhas:
        a = int(T[:4])
        out.append(f"### {T}")
        out.append("")
        for o in ocorr.get(a, []) or ["sem ocorrências"]:
            out.append(f"- {o}")
        out.append("")
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_ita.py` (serve para todas as divisões italianas): nome de exibição como o "
        "clube é conhecido no Brasil, cidade e país. As grafias de época do engsoccerdata viram um clube só (Genova 1893 e Genoa; "
        "AC Liguria e Sampierdarenese; Lanerossi Vicenza e Vicenza; US e AS Livorno; Parma AC e Parma FC; US Anconitana e Ancona).",
        "- A Sampdoria (fusão de 1946) fica separada da Sampierdarenese e da Andrea Doria. \"Inter\" fica \"Inter de Milão\".",
        "- \"Palermo\" já é um clube argentino no banco: o italiano fica \"Palermo FC\".",
        f"- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): {len(mapa_ogol)} códigos do "
        f"ogol e {len(mapa_espn)} da ESPN.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.",
        "",
        "## O que não deu para coletar", "",
        "- **Autores dos gols e cartões antes de 2001/02:** não entraram. A RSSSF traz os autores rodada a rodada em muitas "
        "temporadas antigas (formato italiano, \"MARCATORI\"); dá para ler num próximo passo, se aprovado.",
        "- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.",
        "- **Spareggi (jogos-desempate de título e rebaixamento):** ficam de fora.",
        "- **Campeonatos de 1897/98 a 1928/29** (grupos regionais e finais): ficam para depois; o ogol tem os calendários.",
        "- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
