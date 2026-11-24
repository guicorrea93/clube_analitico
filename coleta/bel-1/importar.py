"""Monta o pacote da 1ª divisão belga (bel-1), 1895/96 a 2025/26, e o relatório docs/coleta/bel-1.md.

Base dos jogos:
  até 1959/60   a matriz de resultados da Wikipédia (en) de cada temporada, sem data nem rodada (o ogol não tem os jogos
                dessas temporadas); de 1898/99 a 1903/04 (dois grupos e um torneio final) não há matriz: entram só as
                tabelas dos grupos e do torneio final da RSSSF e os jogos finais;
  1960/61+      o calendário do ogol, com data e rodada; o clube é casado pelo código do ogol (clubes_bel.OGOL). Jogo
                decidido fora de campo ("DA" no ogol, sem placar) fica com o placar oficial da matriz da Wikipédia ou do
                football-data, marcado `awd`.
  2009/10+      play-offs: a fase regular é o primeiro jogo de cada par mandante x visitante (o ogol numera as rodadas dos
                play-offs junto com as da fase regular); o resto são os play-offs, separados pelos clubes que se enfrentam
                e casados com as tabelas de play-off da Wikipédia (título, europeu, rebaixamento).
Conferência: tabela final da RSSSF (belghist.html, até 2007/08) e tabelas da Wikipédia (fase regular e play-offs), com o
ponto de partida dos play-offs (metade dos pontos da fase regular) que a Wikipédia traz.
Outras fontes: engsoccerdata e football-data (1995/96+, placar; hora e estatísticas do football-data); ESPN (2010/11+, hora,
estádio, público, gols e cartões, casada pelo código da ESPN, por votação); RSSSF (lista de campeões e de artilheiros).

Uso: python coleta/bel-1/importar.py
"""
from __future__ import annotations

import csv
import html
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
import clubes_bel as clubes  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, nome_oficial, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
import notas_wiki  # noqa: E402
from rsssf_bel import ler as ler_hist  # noqa: E402
from wiki_tabela import _fecha, limpar, resultados as wiki_resultados, tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")
BRUXELAS = ZoneInfo("Europe/Brussels")
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "bel-1.md"
FD = range(1995, 2026)
ESD = range(1995, 2025)
GRUPOS = {1898, 1899, 1901, 1902, 1903}   # dois grupos e final ou torneio final
OGOL_DESDE = 1960
PLAYOFFS_DESDE = 2009

# temporada interrompida: aceita menos jogos
INTERROMPIDAS = {2019: "interrompida em março de 2020 pela pandemia de covid-19, antes da última rodada da fase regular; o "
                       "Club Brugge foi declarado campeão e não houve play-offs"}
# clube que não está na temporada seguinte sem ter caído: (ano, clube) -> motivo
NAO_REBAIXADOS: dict[tuple, str] = {}
# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
EXPLICACOES: dict[int, list[str]] = {
    1948: ["na matriz de resultados da Wikipédia os nomes de KVM e RCM estão cruzados (KVM leva ao Racing Mechelen); pelos "
           "códigos (KVM = KV, RCM = Racing, como na tabela do artigo) os jogos fecham com as duas tabelas (MATRIZ_CODIGOS)"],
    1970: ["a Wikipédia dá ao Sint-Truiden 12 vitórias e 2 pontos a menos (com \"?\"); a RSSSF e os jogos dão 11 vitórias e "
           "29 pontos, sem punição: fica a RSSSF (IGNORAR_AJUSTE)"],
    1973: ["a tabela da Wikipédia traz 10-11-9 para o RFC Liège; a RSSSF e os jogos, 11-9-10 (mesmos pontos)"],
    1981: ["os números de Club Brugge e Cercle Brugge estão trocados na tabela da RSSSF (e na da Wikipédia, que a copia); o ogol "
           "e a matriz da Wikipédia, montados jogo a jogo, concordam entre si, e a ordem da tabela (Club 14º, Cercle 15º, "
           "empatados em pontos e vitórias) só fecha pelo saldo com os números dos jogos"],
    1984: ["a tabela da Wikipédia dá 32 jogos ao Beerschot VAC; a RSSSF e os jogos, 34"],
    1985: ["a tabela da RSSSF dá 35 jogos ao Kortrijk (erro de digitação: 8+9+17 = 34)"],
    1986: ["a tabela da RSSSF dá 33 jogos ao KSK Beveren (erro de digitação: 15+14+5 = 34)"],
    1995: ["o Eendracht Aalst perdeu por 0-5, só para ele, os jogos com o RFC Seraing (2-4 em campo) e o Sint-Truiden (0-0): os "
           "adversários ficaram com o resultado de campo (a RSSSF e a Wikipédia mostram assim); a classificação do Aalst fica com "
           "os números da tabela publicada (TABELA_OFICIAL)",
           "Gent (gols pró) e Cercle Brugge (gols contra): 1 gol a menos na RSSSF que na Wikipédia e nos jogos"],
    1999: ["a tabela da RSSSF de 1999/00 tem as linhas do 7º ao 14º deslocadas (os números de cada clube estão na linha de "
           "outro); a da Wikipédia fecha com os jogos e dá a ordem"],
    2005: ["a tabela da Wikipédia traz 10-8-16 e 38-56 para o Cercle Brugge; a RSSSF e os jogos, 10-7-17 e 38-61"],
    2008: ["Cercle Brugge x Genk (26/04/2009): o football-data e o engsoccerdata dão 1-3; o ogol, a matriz e as tabelas, 1-2: "
           "fica 1-2"],
    2012: ["play-off do título: a tabela da Wikipédia dá 22-20 gols ao Standard e 11-13 ao Genk; o ogol e a matriz da "
           "Wikipédia (jogo a jogo) dão 18-17 e 11-12",
           "play-off de rebaixamento: a tabela da Wikipédia dá 3-2 gols ao Cercle Brugge; o ogol e a matriz, 5-3 (1-0, 0-1, 2-1 e "
           "2-1)"],
    2019: ["a tabela da Wikipédia dá 36-53 gols ao Sint-Truiden; os jogos (com o 3-3 do jogo suspenso contra o Genk, que vale) "
           "dão 33-50, e a mesma tabela fecha para o Genk"],
}
# placar do ogol corrigido: (ano, mandante, visitante) -> (gols, gols, motivo)
CORRECOES = {
    (1994, "Eendracht Aalst", "KV Mechelen"): (1, 1, "o ogol dá 0-0; a matriz da Wikipédia e as tabelas da RSSSF e da "
                                                    "Wikipédia (gols de Aalst e Mechelen) dão 1-1"),
    (2008, "Lokeren", "Roeselare"): (2, 1, "o ogol dá 1-1; football-data, engsoccerdata, ESPN, matriz e tabela da Wikipédia "
                                           "dão 2-1"),
    (2024, "Antwerp", "Beerschot"): (5, 0, "o ogol dá 4-0; football-data, engsoccerdata, ESPN, matriz e tabela da Wikipédia "
                                           "dão 5-0"),
    (1995, "RFC Seraing (1904)", "RWD Molenbeek"): (0, 1, "\"DA\" no ogol, sem placar; football-data, engsoccerdata e as "
                                                          "tabelas da RSSSF e da Wikipédia dão 0-1 (a matriz da Wikipédia, 0-5)"),
}
# clube cuja classificação fica com os números da tabela publicada (punição em jogo que não muda o adversário)
TABELA_OFICIAL = {(1995, "Eendracht Aalst"): "perdeu por 0-5, só para ele, os jogos com RFC Seraing (2-4 em campo) e "
                                             "Sint-Truiden (0-0 em campo); números da tabela publicada"}
# código da matriz da Wikipédia com o nome errado no próprio artigo: ano -> {código: clube}
MATRIZ_CODIGOS = {1948: {"KVM": "KV Mechelen", "RCM": "Racing Mechelen"}}
# nome do artilheiro sem o acento na página da RSSSF
NOMES_ARTILHEIRO = {"Ren Thirifays": "René Thirifays"}
# ajuste de pontos da tabela da Wikipédia que não vale
IGNORAR_AJUSTE = {(1970, "Sint-Truiden")}
# clube que saiu no meio da temporada, com os jogos anulados: fica no fim da classificação, zerado (como nas tabelas da
# Wikipédia e da RSSSF); ano -> {clube: motivo}
EXCLUIDOS = {
    2002: {"KFC Lommel SK": "desistiu com 8 rodadas por jogar (falência; só 13 jogadores); os jogos dele foram anulados"},
    2009: {"Excelsior Mouscron": "saiu em dezembro de 2009 (falência); os jogos dele foram anulados"},
}
# desempate pelo título fora da tabela (fase "Desempate"): ano -> motivo
DESEMPATES = {2008: "Standard e Anderlecht terminaram empatados em pontos e vitórias; o título foi decidido em dois jogos "
                    "(Anderlecht 1-1 Standard e Standard 1-0 Anderlecht)"}

COMPETICAO = {
    "slug": "bel-1", "nome": "Campeonato Belga", "nome_curto": "Belga", "tipo": "liga", "nivel": 1,
    "pais": "BEL", "pais_nome": "Bélgica", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Belga", "menu_painel": "Bélgica · 1ª divisão",
    "do_painel": "do Campeonato Belga", "o_painel": "o Campeonato Belga",
    "observacao": "1ª divisão belga desde a criação (1895/96): Coupe de Championnat, Division d'Honneur, First Division, "
                  "First Division A e Pro League. Sem 1914/15-1918/19, 1939/40-1940/41 e 1944/45 (guerras). De 1898/99 a "
                  "1903/04, dois grupos e um torneio final. Desde 2009/10, fase regular e play-offs (o título é decidido "
                  "no play-off, que começa com a metade dos pontos da fase regular).",
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


def texto_rsssf(nome: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", (DADOS / "rsssf" / nome).read_bytes().decode("latin-1"))).replace("\r", "")


# ------------------------------------------------------------------ fontes
def texto_wiki(a: int) -> str:
    arqs = sorted((DADOS / "wikipedia").glob(f"{wiki_titulo(a)}*.wiki"))
    return "\n".join(x.read_text(encoding="utf-8") for x in arqs)


def tabelas_wiki(a: int) -> list[dict]:
    res = []
    for tb in wiki_tabelas(texto_wiki(a)):
        for x in tb["times"]:
            x["clube"] = clubes.esd(x["nome"], a)
        res.append(tb)
    return res


def sem_notas(texto: str) -> str:
    """Tira as notas de rodapé ({{efn|...}}, {{refn|...}}, {{#tag:ref|...}}): dentro de uma célula da matriz, o placar citado
    na nota ("Standard vencia por 3–1") viraria outro jogo."""
    while True:
        m = re.search(r"\{\{\s*(?:efn|refn|#tag:ref)", texto, re.I)
        if not m:
            return texto
        texto = texto[:m.start()] + texto[_fecha(texto, m.start()):]


def matriz_wiki(a: int, tbs: list[dict]) -> dict[tuple, list]:
    """Placares da matriz de resultados da Wikipédia: (mandante, visitante) -> [(g, g), ...]. Candidatos de cada código: o
    alvo do link em name_XXX ("[[K.R.C. Mechelen|Mechelen]]" é o Racing, embora mostre só "Mechelen"), o nome visível e o
    código na tabela do mesmo artigo; vale o primeiro que joga a temporada. Nenhum sozinho serve: o link às vezes aponta
    para o sucessor (Germinal Beerschot no lugar do Beerschot de 1899), e o código da tabela pode ser outro clube na matriz
    (em 1948/49, "KVM" é o Racing na matriz e o KV na tabela; em 2004/05, "BRU" é o FC Brussels na matriz e o Club Brugge
    na tabela). Os jogos dos play-offs ficam dentro da própria tabela ("Sports
    table" com match_XXX_YYY), lida aqui do mesmo jeito; a matriz da fase regular vem antes no artigo."""
    res: dict[tuple, list] = defaultdict(list)
    cod_tab = {x["codigo"]: x["clube"] for tb in tbs for x in tb["times"] if x["clube"]}
    texto = re.sub(r"(?i)#invoke:\s*sports table", "#invoke:sports results", sem_notas(texto_wiki(a)))
    alvos = []   # alvo do link de cada código, por matriz (só as que têm placar, como em wiki_resultados)
    for m in re.finditer(r"\{\{\s*#invoke:\s*sports results\s*\|", texto, flags=re.I):
        corpo = texto[m.start():_fecha(texto, m.start())]
        if re.search(r"\|\s*match_[^_=|\s]+_[^_=|\s]+\s*=[^|]*?\d+\s*[–-]\s*\d+", corpo):
            alvos.append(dict(re.findall(r"\|\s*name_([^=|\s]+)\s*=\s*\[\[([^\]|]+)", corpo)))
    grupos = wiki_resultados(texto)
    if len(alvos) != len(grupos):
        raise SystemExit(f"{temporada(a)}: {len(grupos)} matrizes na Wikipédia e {len(alvos)} lidas à parte")
    for g, alvo in zip(grupos, alvos):
        # candidatos de cada código, na ordem; vale o primeiro que está entre os clubes da temporada (tabelas do artigo) e
        # ainda não foi usado por outro código da mesma matriz
        temporada_set = set(cod_tab.values())
        cod, usados = {}, set()
        for k, v in g["nomes"].items():
            cands = [c for c in (clubes.esd(alvo.get(k, ""), a), clubes.esd(v, a), cod_tab.get(k), clubes.esd(k, a)) if c]
            boas = [c for c in cands if c in temporada_set and c not in usados] if temporada_set else cands
            cod[k] = MATRIZ_CODIGOS.get(a, {}).get(k) or (boas or cands or [None])[0]
            usados.add(cod[k])
        for (c1, c2), placares in g["jogos"].items():
            if cod.get(c1) is None or cod.get(c2) is None:
                raise SystemExit(f"{temporada(a)}: clube da matriz da Wikipédia sem cadastro: {g['nomes'].get(c1, c1)} x "
                                 f"{g['nomes'].get(c2, c2)}")
            res[(cod[c1], cod[c2])] += placares
    return res


def carregar_ogol(a: int) -> list[dict]:
    res = []
    arq = DADOS / "ogol" / f"bel1_{a}.json"
    for o in json.loads(arq.read_text(encoding="utf-8")):
        if o["resultado"] in ("ADI", "ANU"):
            continue
        m = clubes.ogol(o["mandante_id"], a) or clubes.esd(o["mandante"], a)
        v = clubes.ogol(o["visitante_id"], a) or clubes.esd(o["visitante"], a)
        if m is None or v is None:
            raise SystemExit(f"{temporada(a)}: clube do ogol sem cadastro: {o['mandante']} ({o['mandante_id']}) x "
                             f"{o['visitante']} ({o['visitante_id']})")
        r = re.match(r"^R(\d+)$", o["fase"] or "")
        res.append({"data": o["data"], "m": m, "v": v, "nm": o["mandante"], "nv": o["visitante"], "gm": o["gols_mandante"],
                    "gv": o["gols_visitante"], "rodada": int(r.group(1)) if r else None, "fonte": "ogol", "ogol": o,
                    "fase": "Liga", "grupo": None})
    return res


def carregar_fd() -> dict[int, list]:
    res = {}
    for a in FD:
        arq = DADOS / "football-data" / f"B1_{str(a)[-2:]}{str(a + 1)[-2:]}.csv"
        if arq.exists():
            res[a] = [(chave(x["HomeTeam"], a, "football-data"), chave(x["AwayTeam"], a, "football-data"), data_fd(x["Date"]), x)
                      for x in ler_csv(arq) if x.get("HomeTeam") and x.get("FTHG")]
    return res


def carregar_esd() -> dict[int, list]:
    res = defaultdict(list)
    for x in ler_csv(DADOS / "engsoccerdata" / "belgium_tier1.csv"):
        a = int(x["Season"])
        res[a].append((chave(x["home"], a, "engsoccerdata"), chave(x["visitor"], a, "engsoccerdata"), x["Date"], x))
    return res


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for arq in sorted((DADOS / "espn").glob("bel1_*.json")):
        a = int(arq.stem[5:9])
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(BRUXELAS).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
                              gv=int(j["gols_visitante"])))
        if jogos:
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
    votos: dict[str, Counter] = defaultdict(Counter)
    votos_ano: dict[tuple, Counter] = defaultdict(Counter)
    for a, jogos in outra.items():
        por_dia = defaultdict(list)
        for b in base.get(a, []):
            if b["data"] and b["gm"] is not None:
                por_dia[(b["data"], b["gm"], b["gv"])].append(b)
        for j in jogos:
            d = date.fromisoformat(j["data"])
            cand = [b for k in (-1, 0, 1) for b in por_dia.get(((d + timedelta(days=k)).isoformat(), j["gm"], j["gv"]), [])]
            if len(cand) == 1:
                for campo, lado in ((campo_m, "m"), (campo_v, "v")):
                    votos[j[campo]][cand[0][lado]] += 1
                    votos_ano[(j[campo], a)][cand[0][lado]] += 1
    return Mapa({k: c.most_common(1)[0][0] for k, c in votos.items()},
                {k: c.most_common(1)[0][0] for k, c in votos_ano.items()})


def casar(jogos: list[dict], usados: set, m: str, v: str, d: str, dias: int = 20) -> dict | None:
    cand = [j for j in jogos if (j["m"], j["v"]) == (m, v) and id(j) not in usados and j["data"]]
    if not cand:
        return None
    j = min(cand, key=lambda j: abs((date.fromisoformat(j["data"]) - date.fromisoformat(d)).days))
    if abs((date.fromisoformat(j["data"]) - date.fromisoformat(d)).days) > dias and len(cand) > 1:
        return None
    usados.add(id(j))
    return j


def campeoes_rsssf() -> dict[int, str | None]:
    """belgchamp.html: "1896 FC Liége" (pelo ano final); "1915-19 not held"."""
    res = {}
    for m in re.finditer(r"^(\d{4})\s+(\S.*?)\s*(?:\[\*\])?\s*$", texto_rsssf("belgchamp.html"), re.M):
        a = int(m.group(1)) - 1
        nome = {"FC Liége": "FC Liégeois", "FC Liège": "FC Liégeois", "Racing Brussel": "Racing Club de Bruxelles",
                "Union": "Union Saint-Gilloise", "Daring CB": "Daring Club de Bruxelles", "FC Mechelen": "KV Mechelen",
                "RWDM": "RWD Molenbeek", "Racing Genk": "Genk", "AA Gent": "Gent", "Beerschot": "Beerschot VAC",
                "SK Beveren": "KSK Beveren", "Lierse SK": "Lierse", "Standard": "Standard Liège"}.get(m.group(2), m.group(2))
        res[a] = clubes.esd(nome, a) or nome
    return res


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pv: int) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        if j["gm"] is None:
            continue
        for lado, c, gp, gc in (("m", j["m"], j["gm"], j["gv"]), ("v", j["v"], j["gv"], j["gm"])):
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
    """criterio: "vitorias" (pontos, vitórias, saldo, gols pró), "saldo" (pontos, saldo, gols pró), "media" (pontos, média
    de gols) ou "confronto" (pontos; entre os empatados, pontos e saldo nos jogos entre eles; depois saldo e gols pró)."""
    def pts(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, p = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        if criterio == "vitorias":
            return (-v, -(gp - gc), -gp)
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


def separar(jogos: list[dict], so: set | None = None) -> tuple[list[dict], list[dict]]:
    """Fase regular (o primeiro jogo de cada par mandante x visitante, pela data, entre os clubes de `so`) e o resto
    (play-offs)."""
    vistos, regular, resto = set(), [], []
    for j in sorted(jogos, key=lambda j: (j["data"] or "9999", j["rodada"] or 0)):
        if (j["m"], j["v"]) in vistos or (so and not {j["m"], j["v"]} <= so):
            resto.append(j)
        else:
            vistos.add((j["m"], j["v"]))
            regular.append(j)
    return regular, resto


def componentes(jogos: list[dict]) -> list[list[dict]]:
    """Grupos de jogos ligados pelos clubes que se enfrentam (cada play-off é um grupo fechado)."""
    pai: dict[str, str] = {}

    def raiz(c):
        while pai.setdefault(c, c) != c:
            c = pai[c]
        return c
    for j in jogos:
        pai[raiz(j["m"])] = raiz(j["v"])
    grupos = defaultdict(list)
    for j in jogos:
        grupos[raiz(j["m"])].append(j)
    return list(grupos.values())


# ------------------------------------------------------------------ temporadas de grupos (1898/99-1903/04)
def temporada_grupos(a: int, rs_hist: dict, camp: dict, tab, nomes, ocorr) -> tuple:
    """1898/99, 1899/00, 1901/02, 1902/03 e 1903/04: tabelas dos grupos (A e B) e do torneio final da RSSSF, sem os jogos (a
    Wikipédia não tem a matriz). Entram os jogos que a RSSSF lista nas notas: final entre os primeiros dos grupos ("Final
    Game") e desempates ("Play Off", "Playoff for Second Place")."""
    T = temporada(a)
    url = "https://www.rsssf.org/tablesb/belghist.html"
    grupos = rs_hist[a][:3]
    final_tour = [tb for tb in grupos if "Final Tour" in (tb["titulo"] or "")]
    extras, notas, secao = [], [], None
    for tb in grupos:
        for nota in tb["notas"]:
            m = re.match(r"^(\S.*?)\s+-\s+(\S.*?)\s+(\d+)-(\d+)(\s+aet)?\s*$", nota)
            if m:
                extras.append({"m": chave(m.group(1), a, "RSSSF"), "v": chave(m.group(2), a, "RSSSF"), "gm": int(m.group(3)),
                               "gv": int(m.group(4)), "aet": bool(m.group(5)),
                               "fase": "Final" if secao == "final" and not final_tour else "Desempate"})
            elif re.match(r"(?i)^(final game|play ?off)", nota):
                secao = "final" if nota.lower().startswith("final") else "desempate"
            elif re.match(r"(?i)^(remarks|first division|final tour)", nota):
                secao = None
            else:
                notas.append(nota)
    pv = 2
    soma: dict[str, list[int]] = defaultdict(lambda: [0] * 7)
    for tb in grupos:
        titulo = tb["titulo"] or ""
        g = re.search(r"Division ([AB])", titulo)
        fase, grupo = ("Torneio final", None) if "Final Tour" in titulo else ("Grupos", f"Grupo {g.group(1)}")
        for x in tb["linhas"]:
            c = chave(x["nome"], a, "RSSSF")
            nomes[c][f"rsssf:{x['nome']}"].add(a)
            for i, k in enumerate(("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "pontos")):
                soma[c][i] += x[k] or 0
            tab["tabelas_publicadas"].append({
                "temporada": T, "fase": fase, "grupo": grupo, "posicao": x["posicao"], "nome_fonte": x["nome"],
                "clube": clubes.exibicao(c), "jogos": x["jogos"], "vitorias": x["vitorias"], "empates": x["empates"],
                "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"],
                "fonte": url})
    for p in extras:   # os jogos finais e de desempate entram na soma
        for c, gp, gc in ((p["m"], p["gm"], p["gv"]), (p["v"], p["gv"], p["gm"])):
            x = soma[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            x[1 if gp > gc else 2 if gp == gc else 3] += 1
            x[6] += pv if gp > gc else 1 if gp == gc else 0
    campeao = camp.get(a)
    ordem = [chave(x["nome"], a, "RSSSF") for x in final_tour[0]["linhas"]] if final_tour else []
    finais = [p for p in extras if p["fase"] == "Final"]
    if finais:   # final entre os primeiros dos grupos: campeão e vice
        ordem = [campeao] + [c for c in (finais[0]["m"], finais[0]["v"]) if c != campeao]
    resto = defaultdict(list)   # os outros, pela posição no grupo (A antes de B)
    for tb in grupos:
        if "Final Tour" in (tb["titulo"] or ""):
            continue
        for i, x in enumerate(tb["linhas"]):
            resto[i].append(chave(x["nome"], a, "RSSSF"))
    for i in sorted(resto):
        ordem += [c for c in resto[i] if c not in ordem]
    if campeao in ordem and ordem[0] != campeao:
        ordem.remove(campeao)
        ordem.insert(0, campeao)
    for i, p in enumerate(extras, 1):
        obs = ("final entre os primeiros dos grupos" if p["fase"] == "Final" else
               "jogo-desempate (empate em pontos)") + (" (com prorrogação)" if p["aet"] else "")
        tab["partidas"].append({
            "id": f"{a}-{i:04d}", "temporada": T, "fase": p["fase"], "grupo": None, "rodada": None, "data": None, "hora": None,
            "mandante": clubes.exibicao(p["m"]), "visitante": clubes.exibicao(p["v"]), "gols_mandante": p["gm"],
            "gols_visitante": p["gv"], "penaltis_mandante": None, "penaltis_visitante": None, "resultado_especial": None,
            "estadio": None, "cidade": None, "publico": None, "fonte": "RSSSF", "fonte_id": None, "gols_texto": None,
            "observacao": obs, "arbitro": None})
    for pos, c in enumerate(ordem, 1):
        j_, v_, e_, d_, gp, gc, p = soma[c]
        tab["classificacao_final"].append({
            "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
            "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p, "ajuste_pontos": 0,
            "situacao": "campeao" if c == campeao else None,
            "fonte": "RSSSF (torneio final ou final; depois a posição no grupo)",
            "observacao": "soma dos grupos, do torneio final e dos jogos finais e de desempate; não há classificação "
                          "oficial além do campeão" + (" e da ordem do torneio final" if final_tour else " e do vice")})
    n = len(ordem)
    formato = ("dois grupos (A e B) e torneio final entre os melhores" if final_tour else
               "dois grupos (A e B) e final entre os primeiros")
    tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                           "pontos_vitoria": pv, "formato": formato, "campeao": clubes.exibicao(campeao),
                           "vice": clubes.exibicao(ordem[1]), "fontes": "RSSSF",
                           "observacao": "sem os jogos dos grupos (a matriz não existe); tabelas da RSSSF"})
    tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Grupos", "tipo": "grupos", "num_grupos": 2,
                         "formato_serie": "pontos_corridos", "criterio": "pontos"})
    tab["fases"].append({"temporada": T, "ordem": 2, "fase": "Torneio final" if final_tour else "Final",
                         "tipo": "grupos" if final_tour else "mata_mata", "num_grupos": 1 if final_tour else None,
                         "formato_serie": "pontos_corridos" if final_tour else "ida_volta", "criterio": "pontos"})
    if any(p["fase"] == "Desempate" for p in extras):
        tab["fases"].append({"temporada": T, "ordem": 3, "fase": "Desempate", "tipo": "mata_mata", "num_grupos": None,
                             "formato_serie": "jogo_unico", "criterio": "jogo-desempate"})
    gols = sum(p["gm"] + p["gv"] for p in extras)
    tab["conferencia"].append({"temporada": T, "jogos": len(extras), "jogos_esperados": None, "tabelas_conferidas": 0,
                               "tabelas_divergentes": 0, "gols": gols, "gols_com_autor": 0,
                               "observacao": f"campeão {clubes.exibicao(campeao)} (RSSSF); só tabelas e jogos finais e de desempate"})
    ocorr[a].append("temporada com dois grupos: sem a matriz de resultados, entram as tabelas da RSSSF (grupos e torneio "
                    "final) e os jogos finais e de desempate listados nas notas")
    for nota in notas:
        ocorr[a].append(f"nota da RSSSF: {nota}")
    return (T, "RSSSF", n, len(extras), gols, 0, 0, 0, clubes.exibicao(campeao), "")


# ------------------------------------------------------------------ principal
def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rs_hist = ler_hist(DADOS / "rsssf" / "belghist.html")
    fd = carregar_fd()
    esd = carregar_esd()
    espn = carregar_espn()
    camp = campeoes_rsssf()
    ogol = {a: carregar_ogol(a) for a in TEMPORADAS if a >= OGOL_DESDE}
    mapa_espn = votar(ogol, espn, "mandante_id", "visitante_id")
    prox_2026 = {j[k] for j in carregar_ogol(TEMPORADAS[-1] + 1) for k in ("m", "v")}

    nomes = defaultdict(lambda: defaultdict(set))
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel = []
    criterios = {}
    clubes_por_ano = {}

    for a in TEMPORADAS:
        ocorr[a].extend(EXPLICACOES.get(a, []))
        excl = EXCLUIDOS.get(a, {})
        if a in GRUPOS:
            linhas_rel.append(temporada_grupos(a, rs_hist, camp, tab, nomes, ocorr))
            continue
        T = temporada(a)
        pv = 3 if a >= 1995 else 2
        tbs = tabelas_wiki(a)
        mz = matriz_wiki(a, tbs)
        if a >= OGOL_DESDE:
            jogos = ogol[a]
            fonte_base = "ogol"
        else:
            fonte_base = "Wikipédia"
            jogos = [{"data": None, "m": m, "v": v, "nm": m, "nv": v, "gm": g1, "gv": g2, "rodada": None,
                      "fonte": "Wikipédia (matriz)", "fase": "Liga", "grupo": None}
                     for (m, v), pl in mz.items() for g1, g2 in pl]
        if not jogos:
            raise SystemExit(f"{T}: sem jogos")
        for j in jogos:
            nomes[j["m"]][f"{j['fonte'].split(' ')[0].lower()}:{j['nm']}"].add(a)
            nomes[j["v"]][f"{j['fonte'].split(' ')[0].lower()}:{j['nv']}"].add(a)
        # fase regular e play-offs (desempate de 2008/09); desde 2016/17 o play-off europeu tem clubes da 2ª divisão: a fase
        # regular fica entre os clubes da maior tabela da Wikipédia
        if a >= PLAYOFFS_DESDE or a in DESEMPATES:
            maior = max(tbs, key=lambda tb: len(tb["times"]), default=None)
            regular, resto = separar(jogos, {x["clube"] for x in maior["times"]} if maior and a >= PLAYOFFS_DESDE else None)
        else:
            regular, resto = jogos, []
        reg_ids = {id(j) for j in regular}
        for j in jogos:   # jogo decidido fora de campo, sem placar no ogol
            if j["gm"] is not None:
                continue
            o = j["ogol"]
            cand = mz.get((j["m"], j["v"]), [])
            fd_j = next((x for m, v, d, x in fd.get(a, []) if (m, v) == (j["m"], j["v"])), None)
            par_regular = any((r["m"], r["v"]) == (j["m"], j["v"]) for r in regular)
            if cand and (id(j) in reg_ids or len(cand) > 1 or not par_regular):
                j["gm"], j["gv"] = cand[0] if id(j) in reg_ids else cand[-1]
                origem = "matriz da Wikipédia"
            elif fd_j:
                j["gm"], j["gv"] = int(fd_j["FTHG"]), int(fd_j["FTAG"])
                origem = "football-data"
            else:
                raise SystemExit(f"{T}: jogo sem placar no ogol ({o['resultado']}) e sem outra fonte: {j['m']} x {j['v']} "
                                 f"({j['data']})")
            j["especial"] = "awd"
            j["obs"] = (f"resultado decidido fora de campo (no ogol: \"{o['resultado']}\", sem placar); placar oficial pela "
                        f"{origem}")
            ocorr[a].append(f"{j['m']} x {j['v']} ({j['data']}): {o['resultado']} no ogol; fica {j['gm']}-{j['gv']} pela {origem}")
        for (b_, m_, v_), (g1, g2, motivo) in CORRECOES.items():
            if b_ != a:
                continue
            j = next((j for j in jogos if (j["m"], j["v"]) == (m_, v_)), None)
            if j is None:
                raise SystemExit(f"{T}: jogo da correção não encontrado: {m_} x {v_}")
            j["gm"], j["gv"] = g1, g2
            j["obs"] = ("resultado decidido fora de campo; " if j.get("especial") else "") + f"placar corrigido: {motivo}"
            ocorr[a].append(f"{m_} x {v_} ({j['data']}): placar corrigido para {g1}-{g2} ({motivo})")
        clubes_ano = sorted({j["m"] for j in regular} | {j["v"] for j in regular})
        clubes_por_ano[a] = set(clubes_ano)
        n = len(clubes_ano)
        esperados = n * (n - 1)
        if len(regular) != esperados and a not in INTERROMPIDAS:
            ocorr[a].append(f"fase regular com {len(regular)} jogos de {esperados}")
        fase_reg = "Fase regular" if resto and a >= PLAYOFFS_DESDE else "Liga"
        for j in regular:
            j["fase"] = fase_reg

        # ---- conferência jogo a jogo com a matriz da Wikipédia (1960/61+)
        if a >= OGOL_DESDE and mz:
            por_par = defaultdict(list)
            for j in jogos:
                por_par[(j["m"], j["v"])].append(j)
            dif = []
            for par, pl in mz.items():
                if set(par) & set(excl):
                    continue
                nossos = sorted((j["gm"], j["gv"]) for j in por_par.get(par, []))
                if sorted(pl) != nossos and not (len(pl) < len(nossos) and set(pl) <= set(nossos)):
                    outras = [f"{f_} {', '.join(f'{x[cm]}-{x[cv]}' for m, v, d, x in dados.get(a, []) if (m, v) == par)}"
                              for f_, dados, cm, cv in (("engsoccerdata", esd, "hgoal", "vgoal"), ("football-data", fd, "FTHG", "FTAG"))
                              if any((m, v) == par for m, v, d, x in dados.get(a, []))]
                    dif.append(f"{par[0]} x {par[1]}: ogol {', '.join(f'{x}-{y}' for x, y in nossos) or '—'}; Wikipédia "
                               f"{', '.join(f'{x}-{y}' for x, y in sorted(pl))}" + "".join(f"; {o}" for o in outras))
            for d in dif[:15]:
                ocorr[a].append(f"placar diferente na matriz da Wikipédia — {d}")
            if len(dif) > 15:
                ocorr[a].append(f"... e mais {len(dif) - 15} pares com placar diferente na matriz da Wikipédia")

        # ---- engsoccerdata e football-data (casados pelo par e pela data mais próxima)
        for fonte, dados, cm, cv in (("engsoccerdata", esd, "hgoal", "vgoal"), ("football-data", fd, "FTHG", "FTAG")):
            if a not in dados:
                continue
            usados = set()
            for m, v, d, x in dados[a]:
                nomes[m][f"{fonte}:{x['home' if fonte == 'engsoccerdata' else 'HomeTeam']}"].add(a)
                b = casar(jogos, usados, m, v, d)
                if b is None:
                    ocorr[a].append(f"jogo do {fonte} sem par no ogol: {m} x {v} ({d})")
                    continue
                if fonte == "football-data":
                    b["fd"] = x
                if (int(x[cm]), int(x[cv])) != (b["gm"], b["gv"]) and not b.get("especial"):
                    ocorr[a].append(f"placar diferente no {fonte} — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, "
                                    f"{fonte} {x[cm]}-{x[cv]}")

        # ---- ESPN
        usados = set()
        es_ok = 0
        for e in espn.get(a, []):
            m, v = mapa_espn.get(e["mandante_id"], a), mapa_espn.get(e["visitante_id"], a)
            if m is None or v is None:
                continue
            b = casar(jogos, usados, m, v, e["data"], 3)
            if b is None:
                continue
            nomes[m][f"espn:{e['mandante']}"].add(a)
            b["espn"] = e
            es_ok += 1
            if (e["gm"], e["gv"]) != (b["gm"], b["gv"]) and not b.get("especial"):
                ocorr[a].append(f"placar diferente na ESPN — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, ESPN {e['gm']}-{e['gv']}")

        # ---- fase regular: tabelas publicadas e ordem
        ref = calcular(regular, pv)
        w_reg = max((tb for tb in tbs if not re.search(r"(?i)play|group|europ|relegation", tb["secao"])),
                    key=lambda tb: len({x["clube"] for x in tb["times"]} & set(clubes_ano)), default=None)
        if w_reg and len({x["clube"] for x in w_reg["times"]} & set(clubes_ano)) < n - 2:
            w_reg = None
        w_reg_orig = w_reg
        if w_reg and excl:
            w_reg = dict(w_reg, times=[x for x in w_reg["times"] if x["clube"] not in excl])
        for c, motivo in excl.items():
            anulados = sum(len(pl) for par, pl in mz.items() if c in par)
            ocorr[a].append(f"{c} {motivo} ({anulados} jogos na matriz da Wikipédia, fora do pacote); fica no fim, zerado")
        ajuste: dict[str, int] = {}
        if w_reg:
            for x in w_reg["times"]:
                if x["clube"] is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
                nomes[x["clube"]][f"wikipedia:{x['nome']}"].add(a)
                if x["ajuste"] and (a, x["clube"]) not in IGNORAR_AJUSTE:
                    ajuste[x["clube"]] = x["ajuste"]
        rs = None
        if a in rs_hist and rs_hist[a]:
            linhas = [x for x in rs_hist[a][0]["linhas"] if x["jogos"] is not None and clubes.esd(x["nome"], a) not in excl]
            for x in linhas:
                x["clube"] = clubes.esd(x["nome"], a)
                if x["clube"] is None:
                    raise SystemExit(f"{T}: nome da RSSSF sem cadastro: {x['nome']}")
                nomes[x["clube"]][f"rsssf:{x['nome']}"].add(a)
            if {x["clube"] for x in linhas} == set(clubes_ano):
                rs = linhas
            else:
                ocorr[a].append(f"tabela da RSSSF com outros clubes: {sorted({x['clube'] for x in linhas} ^ set(clubes_ano))}")
        if rs:
            for x in rs:   # punição que só a RSSSF traz
                c = ref.get(x["clube"])
                if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                        and x["pontos"] < c[6] and x["clube"] not in ajuste:
                    ajuste[x["clube"]] = x["pontos"] - c[6]
                    ocorr[a].append(f"punição tirada da tabela da RSSSF: {x['clube']} {x['pontos'] - c[6]:+d} pontos")
        conferidas = divergentes = 0
        confere = {}
        publicadas = []
        if rs:
            publicadas.append(("RSSSF", "https://www.rsssf.org/tablesb/belghist.html", rs, "Liga" if fase_reg == "Liga" else fase_reg))
        if w_reg:
            publicadas.append(("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                               [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                     pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in w_reg["times"]],
                               fase_reg))
        if not publicadas:
            ocorr[a].append("sem tabela publicada legível (RSSSF e Wikipédia)")
        for fonte, url, linhas, fase_t in publicadas:
            erro = []
            for x in linhas:
                c = ref.get(x["clube"])
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = (c[:6] + [c[6] + ajuste.get(x["clube"], 0)]) if c else None
                if pub != meu:
                    erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": fase_t, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"], "empates": x["empates"],
                    "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"],
                    "fonte": url})
            confere[fonte] = not erro
            if erro:
                divergentes += 1
                for e_ in erro[:8]:
                    ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {e_}")
            else:
                conferidas += 1
        # antes de 1960 os jogos vêm só da matriz da Wikipédia, montada depois; quando a soma deles não fecha com a tabela
        # publicada (a da RSSSF; sem ela, a da Wikipédia), a classificação final fica com os números publicados
        numeros_pub = {}
        if a < OGOL_DESDE and publicadas:
            fonte_pub, _, linhas_pub, _ = publicadas[0]
            numeros_pub = {x["clube"]: (fonte_pub, [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"],
                                                    x["gols_contra"], x["pontos"]]) for x in linhas_pub}
        if w_reg and (confere.get("Wikipédia") or not confere.get("RSSSF")):
            ordem = [x["clube"] for x in w_reg["times"]]
            fonte_ordem = "Wikipédia (ordem oficial)"
        elif rs:
            ordem = [x["clube"] for x in sorted(rs, key=lambda x: x["posicao"])]
            fonte_ordem = "RSSSF (ordem oficial)"
            if w_reg:
                ocorr[a].append("a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF")
        else:
            ordem = ordenar(ref, ajuste, "vitorias", regular, pv)
            fonte_ordem = "calculada"
        if set(ordem) != set(clubes_ano):
            ocorr[a].append(f"ordem oficial com outros clubes ({sorted(set(ordem) ^ set(clubes_ano))}): fica a calculada")
            ordem = ordenar(ref, ajuste, "vitorias", regular, pv)
            fonte_ordem = "calculada"
        tentativas = {cr: ordenar(ref, ajuste, cr, regular, pv) for cr in ("vitorias", "saldo", "confronto", "media")}
        ok = [cr for cr, o in tentativas.items() if o == ordem]
        criterio = ok[0] if ok else min(tentativas, key=lambda cr: sum(x != y for x, y in zip(tentativas[cr], ordem)))
        if not ok and a not in INTERROMPIDAS:
            dif = [c for c, d in zip(ordem, tentativas[criterio]) if c != d]
            ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo ({criterio}) difere em "
                            f"{len(dif)} posições (ex.: {dif[:2]})")
        criterios[a] = (criterio, bool(ok))

        # ---- play-offs
        fases_po = []   # (fase, grupo, jogos, tabela da Wikipédia)
        pontos_po: dict[str, int] = {}
        ajuste_po: dict[str, int] = {}
        if resto:
            # tabelas de play-off da Wikipédia (menores que a da fase regular): a que tem o 1º da fase regular é a do título, a
            # que tem o último é a de rebaixamento, as outras são do play-off europeu (grupos A e B quando são duas)
            tbs_po = [tb for tb in tbs if tb is not w_reg_orig and len(tb["times"]) < n]
            for tb in tbs_po:
                for x in tb["times"]:
                    if x["clube"] is None:
                        raise SystemExit(f"{T}: nome da Wikipédia (play-off) sem cadastro: {x['nome']}")
            europeus = [tb for tb in tbs_po if not {ordem[0], ordem[-1]} & {x["clube"] for x in tb["times"]}]
            tipo_tb = []
            for tb in tbs_po:
                conj = {x["clube"] for x in tb["times"]}
                if ordem[0] in conj:
                    fase, grupo = "Play-off do título", None
                elif ordem[-1] in conj:
                    fase, grupo = "Play-off de rebaixamento", None
                else:
                    g = re.search(r"(?:\b|group\s*)([AB])$", tb["secao"].strip(), re.I)
                    grupo = (f"Grupo {g.group(1).upper()}" if g else f"Grupo {'AB'[europeus.index(tb)]}") if len(europeus) > 1 else None
                    fase = "Play-off europeu"
                tipo_tb.append((fase, grupo, conj, tb))
            sobra = []
            por_tb = defaultdict(list)
            for j in resto:
                k = next((i for i, (_, _, conj, _) in enumerate(tipo_tb) if {j["m"], j["v"]} <= conj), None)
                if k is None:
                    sobra.append(j)
                else:
                    por_tb[k].append(j)
            for k, (fase, grupo, conj, tb) in enumerate(tipo_tb):
                if por_tb[k]:
                    fases_po.append((fase, grupo, por_tb[k], tb))
                else:
                    ocorr[a].append(f"tabela de play-off da Wikipédia sem jogos no ogol: {sorted(conj)}")
            queda_tb = set().union(*[conj for f, g, conj, tb in tipo_tb if f == "Play-off de rebaixamento"])
            for comp in componentes(sobra):   # jogos fora das tabelas: desempate, final do europeu, rebaixamento
                times = {j["m"] for j in comp} | {j["v"] for j in comp}
                pos_reg = [ordem.index(c) for c in times if c in ordem]
                if a in DESEMPATES and len(times) == 2:
                    fase, grupo = "Desempate", None
                elif times & queda_tb or (pos_reg and min(pos_reg) >= n - 3):
                    fase, grupo = "Play-off de rebaixamento", None
                else:
                    fase, grupo = "Play-off europeu", "Final" if len(times) == 2 else "Semifinal e final"
                fases_po.append((fase, grupo, comp, None))
            for fase, grupo, comp, tb in fases_po:
                for j in comp:
                    j["fase"], j["grupo"] = fase, grupo
            for fase, grupo, comp, tb in fases_po:
                if tb is not None:   # tabela do play-off: ponto de partida (metade da fase regular) + jogos
                    calc_po = calcular(comp, pv)
                    erro = []
                    for x in tb["times"]:
                        c = x["clube"]
                        nomes[c][f"wikipedia:{x['nome']}"].add(a)
                        cp = calc_po.get(c, [0] * 7)
                        pub = [sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")), x["vitorias"], x["empates"],
                               x["derrotas"], x["gols_pro"], x["gols_contra"], pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]]
                        meu = cp[:6] + [cp[6] + x["ajuste"]]
                        if pub != meu:
                            erro.append(f"{c} tabela {pub} jogos {meu}")
                        if fase != "Play-off europeu":   # o europeu começa do zero e não muda a classificação
                            pontos_po[c] = cp[6] + x["ajuste"]
                            ajuste_po[c] = (fase, x["ajuste"])
                        tab["tabelas_publicadas"].append({
                            "temporada": T, "fase": fase, "grupo": grupo, "posicao": x["posicao"], "nome_fonte": x["nome"],
                            "clube": clubes.exibicao(c), "jogos": pub[0], "vitorias": x["vitorias"], "empates": x["empates"],
                            "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": pub[6],
                            "fonte": f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}"})
                    if erro:
                        divergentes += 1
                        for e_ in erro[:6]:
                            ocorr[a].append(f"tabela do {fase}{' ' + grupo if grupo else ''} (Wikipédia) x jogos — {e_}")
                    else:
                        conferidas += 1

        # ---- classificação final
        po_titulo = next(((tb, comp) for f, g, comp, tb in fases_po if f == "Play-off do título" and tb), None)
        po_queda = next(((tb, comp) for f, g, comp, tb in fases_po if f == "Play-off de rebaixamento" and tb), None)
        if po_titulo:
            topo = [x["clube"] for x in po_titulo[0]["times"]]
            queda = [x["clube"] for x in po_queda[0]["times"]] if po_queda else []
            ordem_final = topo + [c for c in ordem if c not in topo and c not in queda] + queda
            fonte_final = "Wikipédia (play-off do título; depois a fase regular e o play-off de rebaixamento)"
        else:
            ordem_final, fonte_final = ordem, fonte_ordem
        if a in DESEMPATES:
            desemp = next((comp for f, g, comp, tb in fases_po if f == "Desempate"), [])
            if desemp:
                ocorr[a].append(f"desempate pelo título fora da tabela: {DESEMPATES[a]}")
                camp_d = camp.get(a)
                if camp_d in ordem_final and ordem_final[0] != camp_d:
                    ordem_final.remove(camp_d)
                    ordem_final.insert(0, camp_d)
                    fonte_final = fonte_ordem + "; campeão pelo desempate"
        total = calcular(jogos, pv)
        prox = next((b for b in TEMPORADAS if b > a), None)
        if prox is not None:
            prox_clubes = ({j[k] for j in ogol[prox] for k in ("m", "v")} if prox >= OGOL_DESDE else None)
            if prox_clubes is None:   # antes do ogol: os clubes da matriz (ou das tabelas) da temporada seguinte
                tbs_p = tabelas_wiki(prox)
                mz_p = matriz_wiki(prox, tbs_p) if prox not in GRUPOS else {}
                prox_clubes = {c for par in mz_p for c in par} or {x["clube"] for tb in tbs_p[:1] for x in tb["times"]}
                if prox in GRUPOS:
                    prox_clubes = {clubes.esd(x["nome"], prox) for tb in rs_hist.get(prox, [])[:3] for x in tb["linhas"]}
        else:
            prox_clubes = prox_2026
        rebaixados = {c for c in clubes_ano if c not in prox_clubes and (a, c) not in NAO_REBAIXADOS} | set(excl)
        ordem_final = ordem_final + list(excl)
        for (b_, c), motivo in NAO_REBAIXADOS.items():
            if b_ == a:
                ocorr[a].append(f"{c} não está na temporada seguinte, mas não caiu: {motivo}")
        campeao = ordem_final[0]
        if camp.get(a) and camp[a] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {camp[a]} (classificação: {campeao})")
        for pos, c in enumerate(ordem_final, 1):
            j_, v_, e_, d_, gp, gc, p = total[c]
            if c in excl:
                pts, obs = 0, excl[c]
            elif c in pontos_po:
                pts = pontos_po[c]
                f_, aj_ = ajuste_po[c]
                obs = (f"pontos do {f_.lower()}: {aj_} de partida (a metade dos pontos da fase regular) mais os do play-off"
                       if f_ == "Play-off do título" else f"pontos do {f_.lower()}: {aj_} de partida mais os do play-off")
            else:
                pts = ref[c][6] + ajuste.get(c, 0)
                obs = None
                fonte_pub, pub = numeros_pub.get(c, (None, None))
                if (a, c) in TABELA_OFICIAL and publicadas:
                    fonte_pub, _, linhas_pub, _ = publicadas[0]
                    x_ = next(x for x in linhas_pub if x["clube"] == c)
                    pub = [x_["jogos"], x_["vitorias"], x_["empates"], x_["derrotas"], x_["gols_pro"], x_["gols_contra"], x_["pontos"]]
                if pub and pub != [j_, v_, e_, d_, gp, gc, pts]:
                    obs = (f"números da tabela publicada ({fonte_pub}); a soma dos jogos da matriz da Wikipédia dá {j_} jogos, "
                           f"{v_}-{e_}-{d_}, {gp}-{gc} gols e {pts} pontos")
                    j_, v_, e_, d_, gp, gc, pts = pub
                    p = pv * v_ + e_
            nota = (w_reg and next((notas_wiki.traduzir(x["nota"] or x["hth"]) for x in w_reg["times"] if x["clube"] == c), None))
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": pts, "ajuste_pontos": pts - p,
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None, "fonte": fonte_final,
                "observacao": "; ".join(x for x in (obs, nota) if x) or None})

        # ---- partidas, gols, cartões, estatísticas
        jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
            hora = None
            if x and x.get("Time"):
                hora = datetime.fromisoformat(f"{data_fd(x['Date'])}T{x['Time']}").replace(tzinfo=LONDRES).astimezone(BRUXELAS).strftime("%H:%M")
            elif e:
                local = e["utc"].astimezone(BRUXELAS)
                if local.date().isoformat() == j["data"]:
                    hora = local.strftime("%H:%M")
            ids = ([f"ogol:{o['id']}"] if o else []) + ([f"espn:{e['id']}"] if e else [])
            fontes = [j["fonte"]] + (["football-data"] if x else []) + (["ESPN"] if e else [])
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
                "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": j.get("especial"), "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
                "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids),
                "gols_texto": None, "observacao": j.get("obs") or ("desempate pelo título, fora da tabela" if j["fase"] == "Desempate" else None),
                "arbitro": (x or {}).get("Referee") or None})
            gols_ano += j["gm"] + j["gv"]
            if e and e["lances"] and not j.get("especial"):
                # a ESPN de 2016/17 repete lances (mesmo minuto, lado e jogador): repetidos saem
                vistos_l = set()
                e["lances"] = [l for l in e["lances"] if not ((k_ := (l["tipo"], l["minuto"], l["lado"], tuple(l["jogadores"] or ()),
                                                                      l["gol"], l["amarelo"], l["vermelho"])) in vistos_l
                                                              or vistos_l.add(k_))]
                gl = [l for l in e["lances"] if l["gol"]]
                if len(gl) > j["gm"] + j["gv"]:   # repetidos com 1 minuto de diferença (87' e 88')
                    gl2 = []
                    for l in gl:
                        if not any((k["lado"], k["tipo"], k["jogadores"]) == (l["lado"], l["tipo"], l["jogadores"])
                                   and abs((minuto(k["minuto"])[0] or 0) - (minuto(l["minuto"])[0] or 0)) <= 1 for k in gl2):
                            gl2.append(l)
                    if len(gl2) == j["gm"] + j["gv"]:
                        gl = gl2
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

        # ---- classificação rodada a rodada (fase regular, quando todos os jogos têm rodada)
        if regular and all(j["rodada"] for j in regular):
            pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
            for r in sorted({j["rodada"] for j in regular}):
                ate = [j for j in regular if j["rodada"] <= r]
                parcial = calcular(ate, pv)
                for pos, c in enumerate(ordenar(parcial, ajuste, criterio, ate, pv), 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        # ---- edição, fases, conferência
        fontes_ed = [fonte_base] + (["engsoccerdata"] if a in esd else []) + (["football-data"] if a in fd else []) \
            + (["ESPN"] if a in espn else []) + (["RSSSF"] if rs else []) + (["Wikipédia"] if w_reg or mz else [])
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        formato = "pontos corridos (turno e returno)"
        if fases_po and a >= PLAYOFFS_DESDE:
            formato = "fase regular em turno e returno e play-offs (o do título começa com a metade dos pontos da fase regular)"
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pv, "formato": formato, "campeao": clubes.exibicao(campeao),
                               "vice": clubes.exibicao(ordem_final[1]), "fontes": " + ".join(dict.fromkeys(fontes_ed)),
                               "observacao": "; ".join(x for x in (f"temporada {INTERROMPIDAS[a]}" if a in INTERROMPIDAS else "",
                                                                    f"punições: {pun}" if pun else "",
                                                                    DESEMPATES.get(a, ""),
                                                                    "; ".join(f"{c} {m}" for c, m in excl.items())) if x) or None})
        crit_txt = {"vitorias": "pontos, vitórias, saldo de gols, gols pró", "saldo": "pontos, saldo de gols, gols pró",
                    "confronto": "pontos, confronto direto, saldo de gols, gols pró",
                    "media": "pontos, média de gols (goal average)"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": fase_reg, "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        vistas = []
        for fase, grupo, comp, tb in fases_po:
            if fase in vistas:
                continue
            vistas.append(fase)
            ng = len({g for f, g, c_, t_ in fases_po if f == fase and g})
            tab["fases"].append({"temporada": T, "ordem": len(vistas) + 1, "fase": fase,
                                 "tipo": "mata_mata" if fase == "Desempate" else "grupos", "num_grupos": ng or 1,
                                 "formato_serie": "ida_volta" if fase == "Desempate" else "pontos_corridos",
                                 "criterio": "jogos-desempate, fora da tabela" if fase == "Desempate" else
                                 "pontos, com a metade dos pontos da fase regular de partida" if fase != "Play-off europeu" else
                                 "pontos"})
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": esperados,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autor_ano,
                                   "observacao": f"campeão {clubes.exibicao(campeao)} (RSSSF, lista de campeões: "
                                                 f"{clubes.exibicao(camp[a]) if camp.get(a) in clubes.CLUBES else camp.get(a, '—')})"})
        linhas_rel.append((T, " + ".join(dict.fromkeys(fontes_ed)), n, len(jogos), gols_ano, autor_ano, conferidas, divergentes,
                           clubes.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos ({len(regular)} da fase regular), tabelas {conferidas} ok / {divergentes} div, "
              f"gols {gols_ano} ({autor_ano} c/ autor), critério {criterio}{'' if criterios[a][1] else ' (aprox.)'}, "
              f"campeão {clubes.exibicao(campeao)}", flush=True)

    # ---- clubes
    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = [{"codigo": "BEL", "nome": "Bélgica", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_espn, criterios)


def artilheiros(ocorr) -> list[dict]:
    """Artilheiro(s) de cada temporada pela lista da RSSSF (tablesb/belgtops.html, desde 1945/46: "1945-46  Bert De Cleyn
    40  FC Mechelen"; empate na linha seguinte, sem temporada)."""
    t = (DADOS / "rsssf" / "belgtops.html").read_bytes()
    try:
        txt = t.decode("utf-8")
    except UnicodeDecodeError:
        txt = t.decode("latin-1")
    txt = html.unescape(re.sub(r"<[^>]+>", "", txt)).replace("\r", "")
    res, ano = [], None
    for l in txt.split("\n"):
        m = re.match(r"^(\d{4})-\d{2}\s+(\S.*?)\s{2,}(\d+)\s+(\S.*?)\s*$", l)
        m2 = re.match(r"^\s{5,}(\S.*?)\s{2,}(\d+)\s*(\S.*?)?\s*$", l)
        if m:
            ano, nome, gols, clube_txt = int(m.group(1)), m.group(2), int(m.group(3)), m.group(4)
        elif m2 and ano is not None:
            nome, gols, clube_txt = m2.group(1), int(m2.group(2)), m2.group(3) or ""
        else:
            if l.strip() and not l.startswith(" "):
                ano = None
            continue
        if ano not in TEMPORADAS:
            continue
        c = clubes.esd(clube_txt, ano) if clube_txt else None
        res.append({"temporada": temporada(ano), "jogador": NOMES_ARTILHEIRO.get(nome.strip(), nome.strip()), "clube": clubes.exibicao(c) if c else None,
                    "gols": gols, "fonte": "RSSSF (tablesb/belgtops.html)"})
        if c is None:
            ocorr[ano].append(f"artilheiro com clube sem cadastro ou sem clube na lista: {nome} ({clube_txt})")
    return res


def relatorio(linhas, ocorr, tab, mapa_espn, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Belga (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/bel-1/importar.py`. Pacote em `data/coleta/bel-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1895/96 a 2025/26. Sem 1914/15-1918/19, 1939/40-1940/41 e 1944/45 (guerras).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (ESPN), {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- Wikipédia (en): matriz de resultados (base dos jogos até 1959/60, sem data), tabelas da fase regular e dos play-offs "
        "(com o ponto de partida dos play-offs) e conferência jogo a jogo depois;",
        "- ogol (zerozero): base dos jogos de 1960/61 em diante, com data e rodada; o clube pelo código do ogol (os nomes do "
        "calendário não são confiáveis); calendários em `data/cache/ogol-bel-1/` para os escudos;",
        "- RSSSF: tabelas finais de 1895/96 a 2007/08 (belghist.html; de 1898/99 a 1903/04, grupos e torneio final), lista de "
        "campeões e de artilheiros (desde 1945/46);",
        "- engsoccerdata e football-data: conferência de placar de 1995/96 em diante; hora e estatísticas do football-data;",
        "- ESPN (liga `bel.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.", "",
        "**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a "
        "oficial (Wikipédia; sem ela, RSSSF). Nos play-offs (2009/10+), a classificação final é a do play-off do título, "
        "depois os outros clubes pela fase regular e o play-off de rebaixamento; os pontos são os oficiais (a metade da fase "
        "regular, arredondada para cima, mais os do play-off) e a diferença para a soma de todos os jogos fica em "
        "`ajuste_pontos`. 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Rebaixado = clube que não está na 1ª "
        "divisão na temporada seguinte.", "",
        f"**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (vitórias em {cr['vitorias']}, "
        f"saldo em {cr['saldo']}, confronto direto em {cr['confronto']}, média de gols em {cr['media']}).", "",
        "| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for T, f, n, j, g, au, ok, dv, camp, pun in linhas:
        out.append(f"| {T} | {f} | {n} | {j} | {g} | {au} | {ok} / {dv} | {camp} | {pun or '—'} |")
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
        "- Cadastro em `coleta/comum-europa/clubes_bel.py`: o mesmo clube com nomes de época vira uma chave só (pela "
        "matrícula da federação, como na Wikipédia); clubes diferentes com nome parecido ficam separados (os três Beerschot, os "
        "dois Seraing, Mouscron, Lommel e RWDM; KSK Beveren e Waasland-Beveren; AS Oostende e KV Oostende).",
        f"- A ESPN é casada por votação jogo a jogo (mesma data e placar): {len(mapa_espn)} códigos.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Datas e rodadas antes de 1960/61:** a matriz da Wikipédia não traz; o ogol não tem esses jogos.",
        "- **Jogos dos grupos de 1898/99 a 1903/04:** só as tabelas e os jogos finais.",
        "- **Autores dos gols antes da ESPN:** nenhuma fonte em lote.",
        "- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
