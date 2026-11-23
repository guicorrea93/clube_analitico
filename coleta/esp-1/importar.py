"""Monta o pacote da 1ª divisão espanhola (esp-1), 1928/29 a 2025/26, e o relatório docs/coleta/esp-1.md.

Base dos jogos: engsoccerdata. Cada jogo é casado pelo par mandante x visitante, que é único na fase (turno e
returno), com:
  ogol           rodada oficial e conferência de placar (clubes casados pelo código do ogol, por votação);
  football-data  1993/94+: conferência de placar; hora (2019/20+), árbitro e estatísticas por time (2003/04+);
  ESPN           2001/02+: hora, estádio, público, gols e cartões com minuto (clubes casados pelo código da ESPN);
  RSSSF          tabela final de todas as temporadas, matriz de resultados até 1999/2000 (conferência jogo a jogo)
                 e artilheiros até 1999/2000;
  Wikipédia      tabela final de cada temporada (ordem oficial, punições), campeões, artilheiros pela contagem oficial
                 da liga e Troféu Pichichi (do jornal Marca, só para conferir).

1986/87 teve duas fases: 34 rodadas e depois três grupos de seis (títulos, 7º-12º e rebaixamento), com os pontos
da 1ª fase somados.

Regras: o placar é o da base; jogo que falta na base entra por ACRESCIMOS, com o motivo. Os gols da ESPN só entram
quando a soma bate com o placar.

Uso: python coleta/esp-1/importar.py
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
import clubes_esp as clubes  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, nome_oficial, rsssf_url, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
import notas_wiki  # noqa: E402
from rsssf_esp import LINHA, ler as ler_rsssf, texto as texto_rsssf  # noqa: E402
from wiki_tabela import limpar, tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")
MADRI = ZoneInfo("Europe/Madrid")
CANARIAS = ZoneInfo("Atlantic/Canary")
PACOTE = DADOS / "pacote"
SO_FD = (2025,)   # temporadas que o engsoccerdata não tem: base pelo football-data
RELATORIO = RAIZ / "docs" / "coleta" / "esp-1.md"
FASE2 = 1986   # 1986/87: segunda fase em grupos

# jogo que falta na base: (ano, mandante, visitante) -> (data, gols, gols, motivo). Nomes do engsoccerdata.
ACRESCIMOS = {
    (1979, "CD Malaga", "UD Salamanca"): (
        "1980-04-27", 0, 3,
        "falta no engsoccerdata; a matriz da RSSSF traz o jogo: terminou 0-3 em 27/04/1980, foi anulado por "
        "irregularidade (o Salamanca perdeu 2 pontos) e o resultado original foi confirmado em 25/05/1982"),
}

# placar corrigido na base: (ano, mandante, visitante) -> (gols, gols, motivo). Nomes do engsoccerdata.
CORRECOES = {
    (2004, "CA Osasuna", "Albacete"): (3, 2, "o engsoccerdata traz 4-2; ogol, football-data, ESPN e as tabelas da RSSSF e da "
                                             "Wikipédia trazem 3-2"),
}

# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
# nomes da ESPN com o sobrenome na frente ou partidos em dois (2001/02 a 2008/09; revisão ES-006)
NOMES_ESPN = {
    "Kahveci Nihat": "Nihat Kahveci", "Fernando Sanchez Morientes": "Fernando Morientes", "Ismael Aranda Urzaiz": "Ismael Urzaiz",
    "Mendez Ruben Navarro": "Rubén Navarro", "Mocelin Magno": "Magno Mocelin", "Alsocer Raul Molina": "Raúl Molina",
    "Bortolini Pimentel Savio": "Sávio", "Fernandez Manuel Gutierrez Victor": "Víctor Fernández", "Víctor -": "Víctor Fernández",
    "Ballesta Salva": "Salva Ballesta", "Salvador Ballesta Vialcho": "Salva Ballesta",
}


def nome_espn(nome: str | None) -> str | None:
    return NOMES_ESPN.get(nome, nome)


# fora da temporada seguinte sem ter caído: (ano, clube) -> motivo (revisão ES-001)
NAO_REBAIXADOS = {
    (1935, "Real Oviedo"): "3º colocado em 1935/36, teve dispensa de 1939/40 por ter o estádio destruído na guerra e voltou em "
                           "1940/41 (Wikipédia es, 1935-36 e 1939-40)",
}

# caiu em campo, mas está na temporada seguinte: (ano, clube) -> motivo (revisão ES-001; o Guilherme decidiu ficar com o
# que a história aponta)
REBAIXADOS_EXTRA = {
    (1935, "Atletico Madrid"): "11º em 1935/36, caiu com o Osasuna; voltou à 1ª divisão em 1939/40 ao vencer a repescagem pela vaga "
                               "do Oviedo (Athletic de Madrid 3-1 Osasuna, Valência, 26/11/1939; Wikipédia es)",
}

LIGUILLA = ("1986/87: com a ampliação para 20 clubes, os três últimos do grupo de rebaixamento jogaram uma liguilla em turno "
            "único, que mandou um só para a 2ª divisão: Racing 1-1 Cádiz (24/06/1987; Racing 4-3 nos pênaltis), Cádiz 1-1 Osasuna "
            "(28/06; Cádiz 4-3 nos pênaltis) e Osasuna 2-0 Racing (30/06). Osasuna 3 pontos, Cádiz 2, Racing 1: caiu o Racing "
            "(cadizcf.com, racinguismo.com, RSSSF)")
# data corrigida: (ano, mandante, visitante) -> (data, motivo) (revisão QE-003)
DATAS: dict[tuple, tuple] = {
    (2003, "FC Barcelona", "Sevilla FC"): ("2003-09-03", "o \"jogo da meia-noite\": começou à 00:05 de 03/09/2003 (football-data, "
                                                         "ESPN, transfermarkt e BDFutbol); o engsoccerdata e o ogol trazem 02/09"),
}
# jogo suspenso e completado em outro dia: (ano, mandante, visitante) -> observação (revisão QE-004). Fica a data de conclusão
SUSPENSOS: dict[tuple, str] = {
    (2004, "Real Madrid", "Real Sociedad"): "começou em 12/12/2004 e foi suspenso aos 88 minutos, com 1-1 (ameaça de bomba); "
                                            "completado em 05/01/2005",
    (2023, "Granada CF", "Athletic Bilbao"): "começou em 10/12/2023 e foi suspenso no 1º tempo (morte de um torcedor na "
                                             "arquibancada); completado em 11/12/2023",
}
# temporada em que a ordem oficial é a da RSSSF, e não a da Wikipédia: ano -> motivo (revisão QE-002, decisão D-19 b)
ORDEM_RSSSF: dict[int, str] = {
    1960: ("Athletic Bilbao, Betis e Real Sociedad empatados com 30 pontos: no confronto direto entre os três, Athletic e "
           "Betis fazem 5 pontos e a Real Sociedad 2; entre os dois, Athletic 0-0 Betis e Betis 1-3 Athletic, e o Athletic "
           "fica em 6º. É a ordem da RSSSF e do BDFutbol, e a regra das outras temporadas; a Wikipédia põe o Betis à frente "
           "pelo saldo do triangular"),
}
WIKI_TROCADA = ("a tabela da Wikipédia põe os números de um clube na linha de outro (clubes com os mesmos pontos); a da "
                "RSSSF fecha com os jogos e dá a ordem")
EXPLICACOES: dict[int, list[str]] = {
    1928: ["a tabela da Wikipédia traz gols errados para Athletic Bilbao (47-34) e Arenas (33-43); a da RSSSF fecha com os jogos "
           "(43-33 e 32-39) e dá a ordem"],
    1929: ["a matriz da RSSSF traz 2-1 nos dois jogos de Espanyol x Europa; a base e o ogol trazem 1-2 nos dois (as tabelas "
           "não distinguem, porque cada clube fica com uma vitória e uma derrota). Fica a base"],
    1930: ["a tabela da Wikipédia traz 32 gols contra para o Real Madrid; a da RSSSF e os jogos dão 27"],
    1940: ["Valencia x Hércules: a RSSSF (matriz e tabela) traz 6-1; a base, o ogol e a tabela da Wikipédia trazem 6-0. "
           "Fica a base"],
    1961: [WIKI_TROCADA + " (Osasuna e Mallorca)"],
    1967: [WIKI_TROCADA + " (Elche e CD Málaga)"],
    1971: [WIKI_TROCADA + " (Sabadell e Córdoba)"],
    1973: [WIKI_TROCADA + " (Oviedo e Racing Santander); a Wikipédia também erra vitórias e empates de Atlético de Madrid, "
           "Zaragoza e Real Sociedad"],
    1979: ["CD Málaga x AD Almería (30/03/1980): o Málaga não compareceu; vitória de 1-0 dada ao Almería (W.O.) e 3 pontos "
           "a menos para o Málaga (RSSSF e Wikipédia). Nas tabelas, o W.O. conta a vitória mas não os gols"],
    1980: [WIKI_TROCADA + " (Atlético de Madrid e Valencia)"],
    1986: ["Real Valladolid x Las Palmas (17/12/1986): o ogol traz 0-0; a base, a matriz e a tabela da RSSSF e a da Wikipédia "
           "fecham com 2-1: erro do ogol",
           LIGUILLA + ". Esses jogos não contam como Primera División (Wikipédia es), e a classificação oficial continua a do "
           "grupo de rebaixamento: 16º Osasuna, 17º Racing (rebaixado) e 18º Cádiz (Wikipédia es e RSSSF)"],
    1993: ["Real Madrid x Real Sociedad: o football-data traz 0-1; a base, a matriz da RSSSF e as tabelas fecham com 0-2: "
           "erro do football-data"],
    1999: ["Valencia x Mallorca (20/06/2000): o ogol traz 2-0; a base, o football-data, a matriz da RSSSF e as tabelas "
           "fecham com 3-0: erro do ogol"],
    2000: ["a tabela da Wikipédia dá ao Espanyol 15 vitórias, 7 empates e 52 pontos; os jogos e a RSSSF dão 14, 8 e 50"],
    2002: ["Villarreal x Celta (18/05/2003): a ESPN traz 6-0; base, ogol, football-data e as tabelas fecham com 5-0 "
           "(gols da ESPN descartados)"],
    2006: ["a tabela da Wikipédia traz gols errados para Atlético de Madrid, Levante, Real Sociedad e Gimnàstic; a da RSSSF "
           "fecha com os jogos e dá a ordem"],
    2011: ["a ESPN traz 0-0, sem gols, em dez jogos do Granada (agosto a janeiro); os placares da base são confirmados pelo "
           "ogol, pelo football-data e pelas tabelas. Esses jogos ficam sem autores de gols"],
    2014: ["Almería: 3 pontos a menos (punição da FIFA por dívida de transferência); a Wikipédia desconta, a tabela da RSSSF não",
           "o Elche (13º) foi rebaixado por dívidas com o fisco e o Eibar (18º) ficou na 1ª divisão: o Elche sai como "
           "rebaixado e o Eibar não"],
}

COMPETICAO = {
    "slug": "esp-1", "nome": "Campeonato Espanhol", "nome_curto": "Espanhol", "tipo": "liga", "nivel": 1,
    "pais": "ESP", "pais_nome": "Espanha", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Espanhol", "menu_painel": "Espanha · 1ª divisão",
    "do_painel": "do Campeonato Espanhol", "o_painel": "o Campeonato Espanhol",
    "observacao": "1ª divisão espanhola (Primera División, \"La Liga\") desde a criação, em 1929. Sem 1936/37-1938/39 "
                  "(Guerra Civil). Em 1986/87, depois das 34 rodadas, três grupos de seis (título, 7º-12º e rebaixamento), "
                  "com os pontos somados. Não inclui as promoções (jogos de acesso e rebaixamento contra clubes da 2ª divisão).",
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


def fuso(mandante: str) -> ZoneInfo:
    return CANARIAS if mandante in ("UD Las Palmas", "CD Tenerife") else MADRI


def nome_rs(x: dict, a: int) -> str | None:
    """Nome da tabela da RSSSF -> chave (o campeão vem em maiúsculas; a cidade às vezes vem entre parênteses)."""
    n = x["nome"].title() if x.get("maiusculas") else x["nome"]
    return clubes.esd(n, a) or clubes.esd(re.sub(r"\s*\(.*?\)\s*", " ", n).strip(), a)


# ------------------------------------------------------------------ fontes
def carregar_base() -> dict[int, list[dict]]:
    base = defaultdict(list)
    for x in ler_csv(DADOS / "engsoccerdata" / "spain_tier1.csv"):
        a = int(x["Season"])
        fase2 = x["round"] == "phase2"
        base[a].append({"data": x["Date"], "m": x["home"], "v": x["visitor"], "gm": int(x["hgoal"]), "gv": int(x["vgoal"]),
                        "fase": "Fase final" if fase2 else "Liga", "grupo": x["group"] if fase2 else None,
                        "nota": None if x["notes"] in ("NA", "") else x["notes"], "fonte": "engsoccerdata"})
    for a in SO_FD:   # temporadas que o engsoccerdata não tem: base pelo football-data
        for x in ler_csv(DADOS / "football-data" / f"SP1_{str(a)[-2:]}{str(a + 1)[-2:]}.csv"):
            if not x.get("HomeTeam"):
                continue
            m, v = clubes.esd(x["HomeTeam"], a), clubes.esd(x["AwayTeam"], a)
            assert m and v, (a, x["HomeTeam"], x["AwayTeam"])
            base[a].append({"data": data_fd(x["Date"]), "m": m, "v": v, "nm": x["HomeTeam"], "gm": int(x["FTHG"]), "gv": int(x["FTAG"]),
                            "fase": "Liga", "grupo": None, "nota": None, "fonte": "football-data"})
    for (a, m, v), (d, gm, gv, motivo) in ACRESCIMOS.items():
        base[a].append({"data": d, "m": m, "v": v, "gm": gm, "gv": gv, "fase": "Liga", "grupo": None, "nota": None,
                        "fonte": "RSSSF", "acrescimo": motivo})
    return base


def carregar_fd() -> dict[int, dict]:
    res = {}
    for a in range(1993, 2026):
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        jogos = {}
        for x in ler_csv(DADOS / "football-data" / f"SP1_{cod}.csv"):
            if not x.get("HomeTeam"):
                continue
            m, v = clubes.esd(x["HomeTeam"], a), clubes.esd(x["AwayTeam"], a)
            assert m and v, (a, x["HomeTeam"], x["AwayTeam"])
            jogos[(m, v)] = x
        res[a] = jogos
    return res


class Mapa(dict):
    """Código do clube na outra fonte -> nome do engsoccerdata. `get(cod, ano)` usa o voto da temporada quando há
    (o ogol junta num código só clubes que o engsoccerdata separa, como CD Málaga e Málaga CF)."""
    def __init__(self, geral: dict, por_ano: dict):
        super().__init__(geral)
        self.por_ano = por_ano

    def get(self, cod, ano=None):
        return self.por_ano.get((cod, ano)) or super().get(cod)


def votar(base: dict[int, list[dict]], outra: dict[int, list[dict]], campo_m: str, campo_v: str) -> Mapa:
    """Código do clube na outra fonte -> nome do engsoccerdata, por votação: jogo de mesma data (±1 dia) e mesmo placar,
    quando só um jogo da base serve."""
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
                votos[j[campo_m]][cand[0]["m"]] += 1
                votos[j[campo_v]][cand[0]["v"]] += 1
                votos_ano[(j[campo_m], a)][cand[0]["m"]] += 1
                votos_ano[(j[campo_v], a)][cand[0]["v"]] += 1
    return Mapa({k: c.most_common(1)[0][0] for k, c in votos.items()},
                {k: c.most_common(1)[0][0] for k, c in votos_ano.items()})


def carregar_ogol() -> dict[int, list[dict]]:
    res = {}
    for a in TEMPORADAS:
        arq = DADOS / "ogol" / f"esp1_{a}.json"
        if arq.exists():
            res[a] = [dict(j, gm=j["gols_mandante"], gv=j["gols_visitante"]) for j in json.loads(arq.read_text(encoding="utf-8"))]
    return res


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for a in range(2001, 2026):
        arq = DADOS / "espn" / f"esp1_{a}.json"
        if not arq.exists():
            continue
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            local = utc.astimezone(MADRI)
            jogos.append(dict(j, data=local.date().isoformat(), utc=utc, gm=int(j["gols_mandante"]), gv=int(j["gols_visitante"])))
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
    """Nomes dos links de uma célula ("[[Real Madrid CF|Madrid FC]]" -> "Madrid FC"), na ordem."""
    return [(y or x).strip() for x, y in re.findall(r"\[\[([^|\]]+)(?:\|([^\]]*))?\]\]", cel)]


def clube_link(cel: str, a: int) -> str | None:
    for nome in links(cel):
        c = clubes.esd(nome, a) or clubes.esd(re.sub(r"\s*(?:CF|FC|C\.F\.)$", "", nome).strip(), a)
        if c:
            return c
    return None


def campeoes_wiki() -> dict[int, str]:
    """Campeão de cada temporada pela "List of Spanish football champions" (linha: temporada, campeão, pontos, ...)."""
    arq = DADOS / "wikipedia" / "List of Spanish football champions.wiki"
    res = {}
    if not arq.exists():
        return res
    for linha in arq.read_text(encoding="utf-8").split("\n|-"):
        m = re.search(r"\[\[(\d{4})(?:[–-](\d{2,4}))? La Liga[^\]]*\]\]", linha)
        if not m:
            continue
        a = int(m.group(1)) - (1 if not m.group(2) else 0)
        cel = [c for c in re.split(r"\n\|", linha) if c.strip()]
        if len(cel) > 1:
            c = clube_link(cel[1], a)
            if c:
                res[a] = c
    return res


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pv: int) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        wo = j.get("especial") == "wo"   # W.O.: conta a vitória, mas não os gols (como nas tabelas oficiais)
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1
            if not wo:
                x[4] += gp; x[5] += gc
            if gp > gc:
                x[1] += 1; x[6] += pv
            elif gp == gc:
                x[2] += 1; x[6] += 1
            else:
                x[3] += 1
    return t


def ordenar(t: dict[str, list[int]], ajuste: dict[str, int], criterio: str, jogos: list[dict] | None = None, pv: int = 2,
            so_completo: bool = False) -> list[str]:
    """criterio: "media" (pontos, média de gols), "saldo" (pontos, saldo, gols pró), "confronto" (pontos; entre os
    empatados, pontos e saldo nos jogos entre eles; depois saldo e gols pró) ou "confronto_esp", a regra espanhola
    (revisão QE-001): pontos entre os empatados, de novo entre os que seguem empatados (recursivo), depois saldo entre
    eles, saldo geral e gols pró. so_completo (classificação de rodada): o confronto só vale depois de jogados todos os
    jogos entre os empatados; antes, saldo e gols pró."""
    def pts(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, p = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        return (-(gp - gc), -gp)
    if criterio == "confronto_esp":
        def rank(g: list[str]) -> list[str]:
            if len(g) == 1 or jogos is None:
                return sorted(g, key=geral)
            jg = [j for j in jogos if j["m"] in g and j["v"] in g]
            if so_completo and len(jg) < len(g) * (len(g) - 1):
                return sorted(g, key=geral)
            mini = calcular(jg, pv)
            sub = defaultdict(list)
            for c in g:
                sub[mini[c][6]].append(c)
            res_ = []
            for p_ in sorted(sub, reverse=True):
                s = sub[p_]
                res_ += rank(s) if len(s) < len(g) else sorted(s, key=lambda c: (-(mini[c][4] - mini[c][5]), *geral(c)))
            return res_
        por_pts = defaultdict(list)
        for c in t:
            por_pts[pts(c)].append(c)
        return [c for p_ in sorted(por_pts, reverse=True) for c in rank(por_pts[p_])]
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


def tabela_rsssf_fase_final(a: int) -> list[dict]:
    """1986/87: as três "Final Table Places ..." da RSSSF (44 jogos por clube)."""
    t = texto_rsssf(DADOS / "rsssf" / rsssf_url(a).rsplit("/", 1)[1])
    i = [m.start() for m in re.finditer(rf"Spain {a}/{str(a + 1)[-2:]}\s*\n", t)][-1]
    t = t[i:t.find(f"Spain {a + 1}/", i)]
    res = []
    for bloco in re.split(r"Final Table Places [\d-]+:", t)[1:]:   # seis clubes em cada uma
        for m in [m for m in map(LINHA.match, bloco.split("\n")) if m][:6]:
            res.append({"posicao": int(m.group(1)), "nome": m.group(2).strip(), "maiusculas": m.group(2).strip().isupper(),
                        "jogos": int(m.group(3)), "vitorias": int(m.group(4)), "empates": int(m.group(5)),
                        "derrotas": int(m.group(6)), "gols_pro": int(m.group(7)), "gols_contra": int(m.group(8)),
                        "pontos": int(m.group(9))})
    return res


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
    rs_cache: dict[str, dict] = {}

    nomes = defaultdict(lambda: defaultdict(set))   # clube esd -> "fonte:nome" -> anos
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel = []
    criterios = {}

    for a in TEMPORADAS:
        T = temporada(a)
        jogos = base[a]
        ocorr[a].extend(EXPLICACOES.get(a, []))
        pares = Counter((j["fase"], j["m"], j["v"]) for j in jogos)
        assert all(n == 1 for n in pares.values()), (a, [p for p, n in pares.items() if n > 1])
        por_par = {(j["fase"], j["m"], j["v"]): j for j in jogos}
        liga = [j for j in jogos if j["fase"] == "Liga"]
        for j in jogos:
            nomes[j["m"]][f"{j['fonte']}:{j.get('nm', j['m'])}"].add(a)
            if (a, j["m"], j["v"]) in DATAS and j["fase"] == "Liga":
                d_, motivo = DATAS[(a, j["m"], j["v"])]
                ocorr[a].append(f"data corrigida: {j['m']} x {j['v']} de {j['data']} para {d_} — {motivo}")
                j["data"], j["data_corrigida"] = d_, motivo
            if (a, j["m"], j["v"]) in SUSPENSOS and j["fase"] == "Liga":
                j["suspenso"] = SUSPENSOS[(a, j["m"], j["v"])]
                ocorr[a].append(f"{j['m']} x {j['v']}: {j['suspenso']}")
            if (a, j["m"], j["v"]) in CORRECOES and j["fase"] == "Liga":
                gm, gv, motivo = CORRECOES[(a, j["m"], j["v"])]
                ocorr[a].append(f"placar corrigido: {j['m']} x {j['v']} de {j['gm']}-{j['gv']} para {gm}-{gv} — {motivo}")
                j["gm"], j["gv"] = gm, gv
            if j.get("acrescimo"):
                ocorr[a].append(f"jogo acrescentado: {j['m']} {j['gm']}-{j['gv']} {j['v']} ({j['data']}) — {j['acrescimo']}")
            if j["nota"]:
                if re.match(r"^1-0 win awarded to", j["nota"]):
                    j["especial"] = "wo"
                else:
                    ocorr[a].append(f"nota do engsoccerdata sem tratamento: {j['m']} x {j['v']}: {j['nota']}")
        clubes_ano = sorted({j["m"] for j in jogos} | {j["v"] for j in jogos})
        n = len(clubes_ano)
        assert len(liga) == n * (n - 1), (a, len(liga), n)
        pv = 2 if a <= 1994 else 3

        # ---- ogol: rodada e conferência
        og_ok = 0
        for o in ogol.get(a, []):
            m, v = mapa_ogol.get(o["mandante_id"], a), mapa_ogol.get(o["visitante_id"], a)
            if m and v:
                nomes[m][f"ogol:{o['mandante']}"].add(a)
                nomes[v][f"ogol:{o['visitante']}"].add(a)
            fase = "Liga" if o["rodada"] or a != FASE2 else "Fase final"
            b = por_par.get((fase, m, v))
            if b is None:
                inv = por_par.get((fase, v, m))
                ocorr[a].append(f"jogo do ogol sem par na base: {o['mandante']} {o['resultado']} {o['visitante']} ({o['data']}, "
                                f"{o['fase']})" + (" — mando invertido" if inv else ""))
                continue
            if "ogol" in b:
                ocorr[a].append(f"jogo repetido no ogol: {o['mandante']} x {o['visitante']}")
                continue
            b["ogol"] = o
            og_ok += 1
            if o["gm"] is not None and (o["gm"], o["gv"]) != (b["gm"], b["gv"]):
                ocorr[a].append(f"placar diferente no ogol — {b['m']} x {b['v']} ({b['data']}): base {b['gm']}-{b['gv']}, "
                                f"ogol {o['gm']}-{o['gv']}")
        for j in jogos:
            j["rodada"] = (j.get("ogol") or {}).get("rodada")
        if a == FASE2:   # 2ª fase: 10 rodadas por grupo, numeradas 35 a 44. Pela ordem das datas, cada jogo vai para a
            # primeira rodada incompleta em que os dois clubes ainda não jogaram (assim o jogo adiado volta à rodada dele)
            for g in "ABC":
                js = sorted((j for j in jogos if j["grupo"] == g), key=lambda j: (j["data"], j["m"]))
                ocup = defaultdict(set)
                for j in js:
                    r = next(r for r in range(35, 45) if len(ocup[r]) < 6 and not {j["m"], j["v"]} & ocup[r])
                    ocup[r] |= {j["m"], j["v"]}
                    j["rodada"] = r
                for r in range(35, 45):
                    cl = [c for j in js if j["rodada"] == r for c in (j["m"], j["v"])]
                    if len(set(cl)) != 6:
                        ocorr[a].append(f"2ª fase, grupo {g}: rodada {r} pela data não fecha (clubes repetidos)")
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
            if len(fd[a]) != len(liga):
                ocorr[a].append(f"football-data com {len(fd[a])} jogos (base {len(liga)})")

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
        if a in espn and es_ok != len(liga):
            falta = [j for j in liga if "espn" not in j]
            ocorr[a].append(f"ESPN com {es_ok} de {len(liga)} jogos (ex. sem ESPN: {falta[0]['m']} x {falta[0]['v']}, {falta[0]['data']})")

        # ---- RSSSF: matriz e tabela
        arq_rs = DADOS / "rsssf" / rsssf_url(a).rsplit("/", 1)[1]
        if arq_rs.name not in rs_cache:
            rs_cache[arq_rs.name] = ler_rsssf(arq_rs)
        rs = rs_cache[arq_rs.name].get(a)
        if rs is not None and "spanhist" not in arq_rs.name:   # nos arquivos por temporada a matriz achada é de outra divisão
            rs["matriz"], rs["matriz_notas"], rs["avisos"] = {}, {}, []
        if rs is None:
            raise SystemExit(f"{T}: sem a tabela da RSSSF")
        for x in rs["tabela"]:
            x["clube"] = nome_rs(x, a)
            if x["clube"] is None:
                raise SystemExit(f"{T}: nome da RSSSF sem cadastro: {x['nome']}")
        for av in rs["avisos"]:
            ocorr[a].append(f"RSSSF: {av}")
        for (nm, nv), (g1, g2) in rs["matriz"].items():
            m, v = nome_rs({"nome": nm, "maiusculas": nm.isupper()}, a), nome_rs({"nome": nv, "maiusculas": nv.isupper()}, a)
            b = por_par.get(("Liga", m, v))
            if b is None:
                ocorr[a].append(f"matriz da RSSSF com jogo sem par na base: {nm} x {nv}")
            elif (g1, g2) != (b["gm"], b["gv"]):
                ocorr[a].append(f"placar diferente na matriz da RSSSF — {m} x {v}: base {b['gm']}-{b['gv']}, RSSSF {g1}-{g2}")
        if rs["matriz"] and len(rs["matriz"]) + len(rs["matriz_notas"]) != len(liga):
            ocorr[a].append(f"matriz da RSSSF com {len(rs['matriz']) + len(rs['matriz_notas'])} jogos (base {len(liga)})")
        for nota in rs["notas"]:
            ocorr[a].append(f"nota da RSSSF: {nota}")

        # ---- tabelas publicadas e conferência
        calc_liga = calcular(liga, pv)
        calc = calcular(jogos, pv)
        ajuste: dict[str, int] = {}
        def sobrepoe(tb):
            return len({clubes.esd(x["nome"], a) for x in tb["times"]} & set(clubes_ano))
        w = max(wiki.get(a, []), key=lambda tb: (sobrepoe(tb), len(tb["times"])), default=None)
        if w and sobrepoe(w) < n // 2:
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
        # punição que só a RSSSF traz (pontos da tabela da RSSSF menos os calculados)
        for x in rs["tabela"]:
            c = calc_liga.get(x["clube"])
            if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                    and x["pontos"] != c[6] and x["clube"] not in ajuste:
                ajuste[x["clube"]] = x["pontos"] - c[6]
                ocorr[a].append(f"punição tirada da tabela da RSSSF: {clubes.exibicao(x['clube'])} {x['pontos'] - c[6]:+d} pontos")
        conferidas, divergentes = 0, 0
        confere = {}
        publicadas = [("RSSSF", rsssf_url(a) + (f"#{str(a)[-2:]}{str(a + 1)[-2:]}" if "spanhist" in rsssf_url(a) else ""),
                       rs["tabela"], calc_liga, "Liga" if a != FASE2 else "1ª fase")]
        if a == FASE2:
            publicadas.append(("RSSSF (final)", rsssf_url(a), [dict(x, clube=nome_rs(x, a)) for x in tabela_rsssf_fase_final(a)], calc,
                               "Final"))
        if w:
            publicadas.append(("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                               [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                     pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in w["times"]],
                               calc_liga if len(w["times"]) == n and a == FASE2 else calc, "Liga" if a != FASE2 else "1ª fase"))
        for fonte, url, linhas, ref, fase_pub in publicadas:
            erro = []
            if sorted(x["clube"] for x in linhas) != clubes_ano:
                erro.append(f"clubes diferentes: {sorted(set(x['clube'] for x in linhas) ^ set(clubes_ano))}")
            for x in linhas:
                c = ref.get(x["clube"])
                if c is None:
                    continue
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = c[:6] + [c[6] + ajuste.get(x["clube"], 0)]
                if pub != meu:
                    erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": "Liga" if fase_pub in ("Liga", "1ª fase") else "Fase final", "grupo": None,
                    "posicao": x["posicao"], "nome_fonte": x["nome"], "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"],
                    "vitorias": x["vitorias"], "empates": x["empates"], "derrotas": x["derrotas"], "gols_pro": x["gols_pro"],
                    "gols_contra": x["gols_contra"], "pontos": x["pontos"], "fonte": url})
            confere[fonte] = not erro
            if erro:
                divergentes += 1
                for e in erro:
                    ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {e}")
            else:
                conferidas += 1

        # ordem oficial: Wikipédia; sem ela, RSSSF. 1986/87: a das três tabelas finais da RSSSF (por grupo)
        if a == FASE2:
            ordem = [x["clube"] for x in publicadas[1][2]]
            fonte_ordem = "RSSSF (ordem oficial, por grupo da 2ª fase)"
        elif a in ORDEM_RSSSF and rs:
            ordem = [x["clube"] for x in rs["tabela"]]
            fonte_ordem = "RSSSF (ordem oficial)"
            ocorr[a].append(f"fica a ordem da RSSSF: {ORDEM_RSSSF[a]}")
        elif w and (confere.get("Wikipédia") or not confere.get("RSSSF")):
            ordem = [x["clube"] for x in w["times"]]
            fonte_ordem = "Wikipédia (ordem oficial)"
        elif w:
            ordem = [x["clube"] for x in rs["tabela"]]
            fonte_ordem = "RSSSF (ordem oficial)"
            ocorr[a].append("a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF")
        else:
            ordem = [x["clube"] for x in rs["tabela"]]
            fonte_ordem = "RSSSF (ordem oficial)"
            ocorr[a].append("sem tabela da Wikipédia: ordem da RSSSF")
        if a != FASE2 and w and fonte_ordem.startswith("Wikipédia") and [x["clube"] for x in rs["tabela"]] != ordem:
            dif = [(r["clube"], c) for r, c in zip(rs["tabela"], ordem) if r["clube"] != c]
            ocorr[a].append(f"ordem diferente entre RSSSF e Wikipédia em {len(dif)} posições (ex.: RSSSF {dif[0][0]}, Wikipédia "
                            f"{dif[0][1]}); fica a da Wikipédia")
        elif a != FASE2 and w and [x["clube"] for x in w["times"]] != ordem:
            dif = [(r["clube"], c) for r, c in zip(w["times"], ordem) if r["clube"] != c]
            ocorr[a].append(f"ordem diferente entre Wikipédia e RSSSF em {len(dif)} posições (ex.: Wikipédia {dif[0][0]}, RSSSF "
                            f"{dif[0][1]}); fica a da RSSSF")
        # critério de desempate: a regra espanhola em todas as temporadas (confronto direto recursivo; revisão QE-001),
        # conferida com a ordem oficial
        if a != FASE2:
            criterio = "confronto_esp"
            ok = ordenar(calc, ajuste, criterio, liga, pv) == ordem
            if not ok:
                dif = [c for c, d in zip(ordem, ordenar(calc, ajuste, criterio, liga, pv)) if c != d]
                ocorr[a].append(f"a regra de desempate (confronto direto recursivo) não reproduz a ordem oficial em "
                                f"{len(dif)} posições (ex.: {dif[:2]})")
        else:
            criterio = "confronto"
        criterios[a] = (criterio, bool(a == FASE2 or ok))

        # rebaixados: quem não está na 1ª divisão no ano seguinte (última temporada: marca da Wikipédia)
        prox = next((b for b in TEMPORADAS if b > a), None)
        if prox is not None:
            prox_clubes = {j["m"] for j in base[prox]}
            rebaixados = {c for c in clubes_ano if c not in prox_clubes}
        else:
            textos = {k[5:]: limpar(v) for k, v in w["params"].items() if k.startswith("text_")}
            rebaixados = {x["clube"] for x in w["times"] if "relegat" in textos.get(x["resultado"], "").lower()}
        obs_final = {}
        for (ano, c), motivo in NAO_REBAIXADOS.items():
            if ano == a and c in rebaixados:
                rebaixados.discard(c)
                obs_final[c] = motivo
                ocorr[a].append(f"{clubes.exibicao(c)} não está na temporada seguinte, mas não caiu: {motivo}")
        for (ano, c), motivo in REBAIXADOS_EXTRA.items():
            if ano == a:
                rebaixados.add(c)
                obs_final[c] = motivo
                ocorr[a].append(f"{clubes.exibicao(c)} está na temporada seguinte, mas caiu em campo: {motivo}")
        campeao, vice = ordem[0], ordem[1]
        if camp_wiki.get(a) and camp_wiki[a] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da Wikipédia: {camp_wiki[a]} (tabela: {campeao})")
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p = calc[c]
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + ajuste.get(c, 0), "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None, "fonte": fonte_ordem,
                "observacao": obs_final.get(c) or (w and next((notas_wiki.traduzir(x["hth"] or x["nota"]) for x in w["times"] if x["clube"] == c), None))
                or None})

        # ---- partidas, gols, cartões, estatísticas
        jogos.sort(key=lambda j: (j["data"], j["rodada"] or 0, j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
            hora = None
            tz = fuso(j["m"])
            if x and x.get("Time"):   # o football-data dá a hora do Reino Unido
                d = datetime.fromisoformat(f"{data_fd(x['Date'])}T{x['Time']}").replace(tzinfo=LONDRES).astimezone(tz)
                hora = d.strftime("%H:%M")
            elif e:
                local = e["utc"].astimezone(tz)
                if local.date().isoformat() == j["data"]:
                    hora = local.strftime("%H:%M")
            ids = [f"ogol:{o['id']}"] if o else []
            if e:
                ids.append(f"espn:{e['id']}")
            fontes = [j["fonte"]] + (["ogol"] if o else []) + (["football-data"] if x else []) + (["ESPN"] if e else [])
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"],
                "grupo": {"A": "Título", "B": "7º ao 12º", "C": "Rebaixamento"}.get(j["grupo"]) if j["grupo"] else None,
                "rodada": j["rodada"], "data": j["data"],
                "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": j.get("especial"), "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
                "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids),
                "gols_texto": None,
                "observacao": ("W.O.: vitória de 1-0 dada ao visitante" if j.get("especial") == "wo" else
                               "anulado e depois confirmado pela federação" if j.get("acrescimo") else
                               j.get("suspenso") or (f"data corrigida: {j['data_corrigida']}" if j.get("data_corrigida") else None)),
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
                                            "jogador": nome_espn((l["jogadores"] or [None])[0]), "minuto": mi, "acrescimo": ac,
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
                                               "jogador": nome_espn((l["jogadores"] or [None])[0]), "minuto": mi, "acrescimo": ac,
                                               "cor": "vermelho" if l["vermelho"] else "amarelo", "fonte": "ESPN"})
            if x and x.get("HS"):
                def num(k):
                    v_ = x.get(k)
                    return int(float(v_)) if v_ not in (None, "") else None
                for c, s in ((j["m"], "H"), (j["v"], "A")):
                    tab["estatisticas"].append({"partida_id": pid, "clube": clubes.exibicao(c), "chutes": num(f"{s}S"),
                                                "chutes_alvo": num(f"{s}ST"), "faltas": num(f"{s}F"), "escanteios": num(f"{s}C"),
                                                "amarelos": num(f"{s}Y"), "vermelhos": num(f"{s}R"), "fonte": "football-data.co.uk"})

        # ---- classificação rodada a rodada
        if not sem_rodada:
            pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}   # faixa: as posições finais de quem caiu
            for r in sorted({j["rodada"] for j in jogos}):
                ate = [j for j in jogos if j["rodada"] <= r]
                parcial = calcular(ate, pv)
                if r > 34 and a == FASE2:   # 2ª fase de 1986/87: ordem dentro de cada grupo
                    grupo_de = {c: j["grupo"] for j in jogos if j["grupo"] for c in (j["m"], j["v"])}
                    ordem_r = []
                    for g in "ABC":
                        sub = {c: parcial[c] for c in parcial if grupo_de[c] == g}
                        ordem_r += ordenar(sub, ajuste, "confronto", ate, pv)
                else:
                    ordem_r = ordenar(parcial, ajuste, criterio, ate, pv, so_completo=True)
                for pos, c in enumerate(ordem_r, 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        fontes_ed = ["engsoccerdata", "ogol"] + (["football-data"] if a in fd else []) \
            + (["ESPN"] if a in espn else []) + ["RSSSF"] + (["Wikipédia"] if w else [])
        pun = "; ".join(f"{clubes.exibicao(c)} {v:+d} pontos" for c, v in ajuste.items())
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pv,
                               "formato": "pontos corridos (turno e returno)" if a != FASE2 else
                               "pontos corridos (34 rodadas) e fase final em três grupos de seis, com os pontos somados",
                               "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(vice),
                               "fontes": " + ".join(fontes_ed),
                               "observacao": "; ".join(x for x in (f"punições: {pun}" if pun else "",
                                                                    LIGUILLA[9:] if a == FASE2 else "") if x) or None})
        crit_txt = {"confronto_esp": "pontos, confronto direto (pontos e saldo entre os empatados, de novo entre os que "
                                     "seguem empatados), saldo de gols, gols pró; na classificação de rodada, o confronto só "
                                     "depois de jogados todos os jogos entre eles",
                    "confronto": "pontos, confronto direto, saldo de gols, gols pró", "saldo": "pontos, saldo de gols, gols pró",
                    "media": "pontos, média de gols (goal average)"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Liga", "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        if a == FASE2:
            tab["fases"].append({"temporada": T, "ordem": 2, "fase": "Fase final", "tipo": "grupos", "num_grupos": 3,
                                 "formato_serie": "pontos_corridos", "criterio": "pontos somados aos da 1ª fase; " + crit_txt})
        obs = [f"campeão {clubes.exibicao(campeao)} (Wikipédia, lista de campeões: "
               f"{clubes.exibicao(camp_wiki[a]) if a in camp_wiki else '—'})"]
        if divergentes:
            obs.append("divergências explicadas no relatório")
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": n * (n - 1) + (90 if a == FASE2 else 0),
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autor_ano, "observacao": "; ".join(obs)})
        linhas_rel.append((T, " + ".join(fontes_ed), n, len(jogos), og_ok, gols_ano, autor_ano, conferidas, divergentes,
                           clubes.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos, ogol {og_ok}, tabelas {conferidas} ok / {divergentes} div, gols {gols_ano} "
              f"({autor_ano} c/ autor), critério {criterio}{'' if criterios[a][1] else ' (aprox.)'}, campeão {clubes.exibicao(campeao)}",
              flush=True)

    # ---- clubes
    for c, (exib, cidade, pais) in sorted(clubes.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": exib, "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = []
    tab["artilheiros"] = artilheiros(rs_cache, ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_ogol, mapa_espn, criterios)


def artilheiros(rs_cache: dict, ocorr) -> list[dict]:
    """Artilheiro(s) de cada temporada pela contagem oficial da liga (súmulas dos delegados da LFP; Wikipédia, "List of
    La Liga top scorers", seção "Top scorers by season"). O Troféu Pichichi é do jornal Marca, que tem regras próprias, e
    a liga não o reconhece: quando ele difere, fica anotado na `fonte`. Conferido também com o 1º da RSSSF (até 1999/2000).
    Empate: várias linhas na mesma temporada."""
    txt = (DADOS / "wikipedia" / "List of La Liga top scorers.wiki").read_text(encoding="utf-8")
    txt = txt[txt.index("==Top scorers by season=="):]
    txt = txt[txt.index('{| class="wikitable sortable"'):]
    txt = txt[:txt.index("\n|}")]
    res, ano = [], None
    for bloco in txt.split("\n|-")[1:]:
        cel = [c.strip() for c in re.findall(r"^\|(?!-)(.*)$", bloco, re.M)]
        cab = re.search(r"\[\[(\d{4})(?:[–-]\d{2,4})? La Liga", cel[0]) if cel else None
        if cab:   # "[[1929 La Liga|1929]]" é 1928/29
            ano = int(cab.group(1)) - (1 if cab.group(1) == "1929" and "1929–" not in cel[0] else 0)
            cel = cel[1:]
        if ano not in TEMPORADAS or len(cel) < 3:
            continue
        # atributos de célula ("bgcolor=#FFD700|", "bgcolor=mistyrose| '''50'''") saem
        cel = [re.sub(r"^\s*(?:(?:bgcolor|style|align|rowspan|valign)\s*=[^|]*\|)+", "", c).strip(" '") for c in cel]
        sn = re.search(r"\{\{sortname\|([^|}]*)\|([^|}]*)", cel[0])
        jogador = f"{sn.group(1)} {sn.group(2)}".strip() if sn else (links(cel[0]) or [limpar(cel[0])])[0]
        c = clube_link(cel[1], ano)
        gols = int(re.match(r"\d+", cel[2]).group())
        res.append({"temporada": temporada(ano), "jogador": jogador, "clube": clubes.exibicao(c) if c else None, "gols": gols,
                    "fonte": "LaLiga, contagem oficial das súmulas (Wikipédia, List of La Liga top scorers)"})
        if c is None:
            ocorr[ano].append(f"artilheiro com clube sem cadastro: {jogador} ({cel[1]})")
    pich = defaultdict(list)
    for x in pichichi(ocorr):
        pich[int(x["temporada"][:4])].append(x)
    por_ano = defaultdict(list)
    for x in res:
        por_ano[int(x["temporada"][:4])].append(x)
    for a in TEMPORADAS:
        if a not in por_ano:
            ocorr[a].append("artilheiro: a lista oficial da Wikipédia não traz esta temporada")
            continue
        p = pich.get(a, [])
        if p and (len(p) != len(por_ano[a]) or p[0]["gols"] != por_ano[a][0]["gols"]):
            txt_p = f"{', '.join(x['jogador'] for x in p)} com {p[0]['gols']} gols"
            ocorr[a].append(f"artilheiro: contagem oficial da liga {', '.join(x['jogador'] for x in por_ano[a])} com "
                            f"{por_ano[a][0]['gols']} gols; o Pichichi (Marca) deu {txt_p}. Fica a contagem oficial")
            for x in por_ano[a]:
                x["fonte"] += f"; Pichichi (Marca): {txt_p}"
    conferir_artilheiros_rsssf(res, pich, rs_cache, ocorr)
    return res


def pichichi(ocorr) -> list[dict]:
    """Troféu Pichichi (Wikipédia, "Pichichi Trophy": o artilheiro pela contagem do jornal Marca). Empate: várias linhas na
    mesma temporada."""
    txt = (DADOS / "wikipedia" / "Pichichi Trophy.wiki").read_text(encoding="utf-8")
    txt = txt[txt.index('{| class="wikitable sortable"'):]
    txt = txt[:txt.index("\n|}")]
    res, ano = [], None
    for bloco in txt.split("\n|-")[1:]:
        cab = re.search(r"^!.*?\[\[(\d{4})(?:[–-]\d{2,4})? La Liga", bloco.strip(), re.M)
        if cab:
            ano = int(cab.group(1)) - (1 if cab.group(1) == "1929" and "1929–" not in bloco else 0)
        cel = [c.strip() for c in re.findall(r"^\|(?!-)(.*)$", bloco, re.M)]
        if ano not in TEMPORADAS or len(cel) < 4:
            continue
        sn = re.search(r"\{\{sortname\|([^|}]*)\|([^|}]*)", cel[0])
        jogador = f"{sn.group(1)} {sn.group(2)}".strip() if sn else (links(cel[0]) or [limpar(cel[0])])[0]
        c = clube_link(cel[1], ano)
        gols = int(re.match(r"\d+", limpar(re.sub(r"\{\{refn.*", "", cel[3])).strip()).group())
        res.append({"temporada": temporada(ano), "jogador": jogador, "clube": clubes.exibicao(c) if c else None, "gols": gols,
                    "fonte": "Wikipédia (Pichichi Trophy)"})
        if c is None:
            ocorr[ano].append(f"artilheiro (Pichichi) com clube sem cadastro: {jogador} ({cel[1]})")
    return res


def conferir_artilheiros_rsssf(res: list[dict], pich: dict, rs_cache: dict, ocorr) -> None:
    """1º da lista de artilheiros da RSSSF (até 1999/2000): anotado quando difere da contagem oficial e do Pichichi."""
    por_ano = defaultdict(list)
    for x in res:
        por_ano[int(x["temporada"][:4])].append(x)
    for a in TEMPORADAS:
        if a > 1999 or a not in por_ano:
            continue
        rs = rs_cache.get(rsssf_url(a).rsplit("/", 1)[1], {}).get(a)
        top = (rs or {}).get("artilheiros") or []
        if not top:
            ocorr[a].append("artilheiro: sem a lista da RSSSF para conferir")
            continue
        g = top[0]["gols"]
        lideres = [t for t in top if t["gols"] == g]
        if (g, len(lideres)) not in {(por_ano[a][0]["gols"], len(por_ano[a])),
                                     (pich[a][0]["gols"], len(pich[a])) if pich.get(a) else None}:
            ocorr[a].append(f"artilheiro: a RSSSF dá {', '.join(t['jogador'] for t in lideres)} com {g} gols")


def relatorio(linhas, ocorr, tab, mapa_ogol, mapa_espn, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Espanhol (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/esp-1/importar.py`. Pacote em `data/coleta/esp-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1928/29 a 2025/26 (Primera División). Sem liga em 1936/37-1938/39 (Guerra Civil).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (ESPN), {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1928/29-2024/25;",
        "- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+) e estatísticas por time (chutes, faltas, "
        "escanteios, cartões; 2005/06+). Não traz árbitro na liga espanhola;",
        "- ogol: rodada oficial de cada jogo e conferência de placar; calendários guardados em `data/cache/ogol-esp-1/` para os escudos;",
        "- ESPN (liga `esp.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;",
        "- RSSSF (José Vicente Tejedor Carnicero e outros): tabela final de todas as temporadas e matriz de resultados até "
        "1999/2000 (conferência jogo a jogo); artilheiros até 1999/2000;",
        "- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões, artilheiros pela contagem "
        "oficial da liga (súmulas da LFP; \"List of La Liga top scorers\") e Troféu Pichichi (do jornal Marca, que a liga não "
        "reconhece; anotado quando difere).", "",
        "**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols "
        "pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando "
        "a soma bate com o placar. Hora local (Madri; Canárias nos jogos em casa do Las Palmas e do Tenerife). Rebaixado = clube "
        "que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96.", "",
        f"**Desempate:** a regra espanhola em todas as temporadas (revisão QE-001): pontos, confronto direto (pontos e saldo "
        f"entre os empatados, de novo entre os que seguem empatados), saldo de gols e gols pró. Ela reproduz a ordem oficial "
        f"em {sum(1 for _, ok in criterios.values() if ok)} de {len(criterios)} temporadas. Na classificação rodada a rodada, "
        f"o confronto só vale depois de jogados todos os jogos entre os empatados.", "",
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
        "- Cadastro em `coleta/comum-europa/clubes_esp.py` (serve para todas as divisões espanholas): nome de exibição como o "
        "clube é conhecido no Brasil, cidade e país. \"Athletic Club\" já é o clube de São João del-Rei (MG): o de Bilbao fica "
        "\"Athletic Bilbao\".",
        "- Clubes que o engsoccerdata separa ficam separados: CD Málaga (até 1992) e Málaga (de 1994); AD Almería (1971-1982) e "
        "Almería (UD, de 1989); Burgos (CF, 1946-1983) e Real Burgos (1983-1995).",
        f"- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): {len(mapa_ogol)} códigos do "
        f"ogol e {len(mapa_espn)} da ESPN.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv` (ex.: `ogol:Atlético Aviación`).",
        "",
        "## O que não deu para coletar", "",
        "- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz. A RSSSF tem os autores de 2000/01 em diante "
        "(a ESPN já cobre) e o ogol tem a ficha de muitos jogos; fica como próximo passo, se aprovado.",
        "- **Público e estádio antes de 2001/02:** idem.",
        "- **Promoções (jogos de acesso e rebaixamento contra clubes da 2ª divisão):** ficam de fora (entram quando a 2ª divisão "
        "for coletada).",
        "- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
