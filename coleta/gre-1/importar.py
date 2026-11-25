"""Monta o pacote da 1ª divisão grega (gre-1), 1927/28 a 2025/26, e o relatório docs/coleta/gre-1.md.

Base dos jogos:
  até 1958/59   a fase nacional do campeonato (campeões regionais), pela RSSSF (coleta/gre-1/antigo.py);
  1959/60-1992/93  a matriz de resultados da RSSSF (grkhist.html até 1967/68; depois a página de cada temporada), sem
                data nem rodada (nenhuma fonte tem). Célula com nota ("(1)", "(*)") resolvida em NOTAS_MATRIZ; "*" ou "x"
                no placar é W.O. Conferência jogo a jogo com a matriz da Wikipédia. Os jogos-desempate (título, 3º lugar)
                vêm das fichas da Wikipédia, com data, local e autores dos gols (fase "Desempate", fora da tabela);
  1993/94+      o calendário do ogol, com data e rodada (sem rodada de 1994/95 a 1996/97); o clube pelo código do ogol.
                Jogo decidido fora de campo ("DA" no ogol, sem placar) fica com o placar oficial da matriz da Wikipédia
                ou do football-data, marcado `awd`.
  play-offs     2007/08-2016/17: play-off europeu (2º a 5º, com pontos de bônus), que não muda a classificação;
                2019/20+: play-off do título e play-out de rebaixamento (desde 2024/25 também um play-off europeu, do 5º ao
                8º, que começa com metade dos pontos), com os pontos da fase regular acumulados: a classificação final é
                a ordem dos grupos, com os números de todos os jogos do clube.
Conferência: tabelas da RSSSF e da Wikipédia (fase regular e play-offs). Pontos: 3-2-1 (vitória, empate, derrota) até
1972/73; 2-1-0 de 1973/74 a 1991/92; 3-1-0 desde 1992/93.
Outras fontes: engsoccerdata e football-data (1994/95+, placar; hora, árbitro e estatísticas do football-data); ESPN
(hora, estádio, público, gols e cartões, casada pelo código da ESPN, por votação); RSSSF (campeões e artilheiros).

Uso: python coleta/gre-1/importar.py
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
import clubes_gre as clubes  # noqa: E402
import antigo  # noqa: E402
import notas_wiki  # noqa: E402
import rsssf_gre as rsssf  # noqa: E402
import wiki_gre  # noqa: E402
from edicoes import DADOS, LIGA, OGOL_DESDE, RAIZ, TEMPORADAS, nome_oficial, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from wiki_tabela import tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")
ATENAS = ZoneInfo("Europe/Athens")
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "gre-1.md"
FD = range(1994, 2026)
EUROPEU = range(2007, 2017)       # play-off europeu (2º a 5º), fora da classificação
GRUPOS_DESDE = 2019               # play-off do título e play-out de rebaixamento, com os pontos acumulados

# placar das células da matriz da RSSSF que remetem a uma nota: (ano, nota) -> (gols, gols, especial, observação)
NOTAS_MATRIZ: dict[tuple, tuple] = {
    (1969, "1"): (2, 0, "awd", "0-0 em campo; vitória dada ao Aris porque o Panachaiki tentou combinar o resultado (RSSSF)"),
    (1970, "1"): (0, 2, "awd", "vitória dada ao Fostiras fora de campo (RSSSF)"),
    (1971, "1"): (0, 2, "awd", "interrompido aos 85 minutos (0-1); dado 0-2, e o Olympiakos Nicosia perdeu também o ponto da "
                               "derrota (RSSSF: \"0-2 on goals and 0-3 on points\")"),
    (1976, "1"): (2, 0, "awd", "o Atromitos não compareceu em Serres (RSSSF)"),
    (1979, "1"): (2, 0, "awd", "0-0 em campo; vitória dada ao Apollon (RSSSF)"),
    (1982, "*"): (0, 2, "awd", "interrompido: o Rodos ficou com 6 jogadores (1-2 no intervalo); vitória dada ao AEK (RSSSF)"),
    (1984, "1"): (0, 1, None, "jogado em Trikala (RSSSF)"),
    (1984, "2"): (2, 2, None, "jogado em Katerini (RSSSF)"),
    (1984, "3"): (2, 3, None, "jogado em Tavros (RSSSF)"),
    (1985, "1"): (0, 2, "awd", "1-0 em campo; o Panachaiki escalou um jogador suspenso: vitória dada ao Iraklis e 1 ponto a "
                               "menos para o Panachaiki (RSSSF)"),
    (1986, "1"): (2, 0, "awd", "greve das 3 últimas rodadas: o visitante não compareceu (RSSSF)"),
    (1986, "2"): (0, 2, "awd", "greve das 3 últimas rodadas: o mandante não compareceu (RSSSF)"),
    (1986, "*"): (0, 0, "awd", "greve das 3 últimas rodadas: nenhum dos dois compareceu; derrota para os dois (RSSSF)"),
    (1987, "1"): (0, 2, "awd", "4-2 em campo; o Panachaiki escalou um jogador suspenso: vitória dada ao Panserraikos (RSSSF)"),
    (1990, "1"): (3, 0, None, "interrompido aos 77 minutos porque o PAOK deixou o campo; ficou o 3-0 (RSSSF)"),
    (1990, "2"): (0, 2, "awd", "2-2 em campo; invasão de campo: vitória dada ao Athinaikos (RSSSF)"),
    (1990, "3"): (1, 0, None, "1-2 no primeiro jogo, interrompido pela fumaça; repetido em Rodes (RSSSF)"),
}
# derrota para os dois (greve de 1986/87): (ano, nota) -> True
DERROTA_DOIS = {(1986, "*")}
# jogo do ogol sem placar ("ANU") que valeu derrota para os dois: (ano, mandante, visitante) -> motivo
DERROTA_DOIS_OGOL = {
    (2014, "Niki Volos", "OFI Creta"): "não disputado: os dois clubes tinham sido excluídos da liga (a matriz da Wikipédia "
                                       "marca \"–\"); as tabelas da RSSSF e da Wikipédia contam 34 jogos para os dois, o que só "
                                       "fecha com derrota para os dois",
}
# clube que não está na temporada seguinte sem ter caído: (ano, clube) -> motivo (os cipriotas entram sozinhos)
NAO_REBAIXADOS: dict[tuple, str] = {}
# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
EXPLICACOES: dict[int, list[str]] = {
    2004: ["o clube da liga era o Chalkidona (Wikipédia, engsoccerdata); ele se fundiu com o Atromitos em 2005 e o ogol põe "
           "a temporada no código do Atromitos"],
}
# placar corrigido: (ano, mandante, visitante) -> (gols, gols, motivo[, "awd"])
CORRECOES: dict[tuple, tuple] = {
    (1997, "Ionikos", "Olympiacos"): (0, 1, "o ogol dá 0-0; a matriz da Wikipédia, o engsoccerdata, o football-data e as "
                                            "tabelas da RSSSF e da Wikipédia dão 0-1"),
    (1998, "Aris Salônica", "Ionikos"): (1, 1, "o ogol dá 0-0; a matriz da Wikipédia, o engsoccerdata, o football-data e as "
                                               "tabelas da RSSSF e da Wikipédia dão 1-1"),
    (2014, "Asteras Tripolis", "Ergotelis"): (2, 1, "o ogol dá 3-0; o football-data, o engsoccerdata, a ESPN e as tabelas da "
                                                    "RSSSF e da Wikipédia dão 2-1"),
    (2023, "Kifisia", "Volos NFC"): (3, 0, "0-0 em campo; em 04/03/2024 a vitória foi dada ao Kifisia por 3-0, depois da "
                                          "agressão racista do presidente do Volos a Andrews Tetteh (nota da matriz da "
                                          "Wikipédia); as tabelas da RSSSF e da Wikipédia contam o 3-0", "awd"),
}
# jogo do ogol com o mando trocado: (ano, data, mandante do ogol, visitante do ogol) -> (mandante, visitante, gols, gols, motivo)
INVERTIDOS: dict[tuple, tuple] = {
    (2001, "2001-10-14", "Ethnikos Asteras", "Panachaiki"): (
        "Panachaiki", "Ethnikos Asteras", 0, 0, "o ogol traz Ethnikos Asteras 1-1 Panachaiki nesta data e de novo em "
                                                "17/02/2002; o engsoccerdata, a matriz da Wikipédia e as tabelas da RSSSF e da "
                                                "Wikipédia dão Panachaiki 0-0 Ethnikos Asteras na 3ª rodada"),
}

COMPETICAO = {
    "slug": "gre-1", "nome": "Campeonato Grego", "nome_curto": "Grego", "tipo": "liga", "nivel": 1,
    "pais": "GRE", "pais_nome": "Grécia", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Grego", "menu_painel": "Grécia · 1ª divisão",
    "do_painel": "do Campeonato Grego", "o_painel": "o Campeonato Grego",
    "observacao": "Campeonato grego reconhecido pela federação, desde 1927/28: até 1958/59, fase nacional entre os campeões "
                  "das ligas regionais (Panhellenic Championship; no pacote, só a fase nacional); desde 1959/60, liga "
                  "nacional (Alpha Ethniki; Super League desde 2006/07), com play-offs desde 2019/20. Os campeões do Chipre "
                  "jogaram a liga de 1967/68 a 1973/74. Sem 1928/29, 1934/35, 1940/41-1944/45, 1949/50 e 1951/52. Não "
                  "inclui o campeonato SEGAS (1906-1912) nem os jogos de acesso contra clubes da 2ª divisão.",
}


def pontos(a: int) -> tuple[int, int, int]:
    """Pontos por vitória, empate e derrota."""
    return (3, 2, 1) if a <= 1972 else (2, 1, 0) if a <= 1991 else (3, 1, 0)


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
HIST = rsssf.blocos(DADOS / "rsssf" / "grkhist.html")


def pagina_rsssf(a: int) -> tuple[str, str] | None:
    """Texto e URL da página da temporada na RSSSF (desde 1968/69)."""
    for nome in (f"grk{str(a + 1)[-2:]}.html", f"grk{a + 1}.html"):
        arq = DADOS / "rsssf" / nome
        if arq.exists():
            return rsssf.texto(arq), f"https://www.rsssf.org/tablesg/{nome}"
    return None


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


def wiki(a: int) -> dict:
    """Jogos da Wikipédia (fichas, OneLegResult e matriz), com o clube pelo alvo do link ou pelo nome visível."""
    r = wiki_gre.ler(texto_wiki(a))
    for j in r["jogos"]:
        j["m"] = clubes.esd(j["tm"] or "", a) or clubes.esd(j["nm"], a)
        j["v"] = clubes.esd(j["tv"] or "", a) or clubes.esd(j["nv"], a)
    return r


def matriz_rsssf(a: int, ocorr) -> tuple[list[dict], str]:
    """Jogos da matriz da RSSSF: página da temporada desde 1968/69; antes, o bloco de grkhist.html."""
    pg = pagina_rsssf(a)
    t, url = pg if pg else (HIST[temporada(a)], "https://www.rsssf.org/tablesg/grkhist.html")
    m = rsssf.matriz(t)
    cl = [chave(n, a, "RSSSF") for n in m["clubes"]]
    jogos = []
    for x in m["jogos"]:
        j = {"data": None, "m": cl[x["i"]], "v": cl[x["j"]], "nm": m["clubes"][x["i"]], "nv": m["clubes"][x["j"]],
             "rodada": None, "fonte": "RSSSF (matriz)", "fase": "Liga", "grupo": None}
        if x["nota"] is not None:
            if (a, x["nota"]) not in NOTAS_MATRIZ:
                raise SystemExit(f"{temporada(a)}: nota ({x['nota']}) da matriz da RSSSF sem placar em NOTAS_MATRIZ: "
                                 f"{j['m']} x {j['v']} — {m['notas'].get(x['nota'], '')[:150]}")
            j["gm"], j["gv"], esp, j["obs"] = NOTAS_MATRIZ[(a, x["nota"])]
            if esp:
                j["especial"] = esp
            if (a, x["nota"]) in DERROTA_DOIS:
                j["dois"] = True
        else:
            j["gm"], j["gv"] = x["gm"], x["gv"]
            if x["wo"]:
                j["especial"] = "awd"
                j["obs"] = "vitória dada fora de campo (W.O.; na matriz da RSSSF, placar com \"*\" ou \"x\")"
        jogos.append(j)
    # correções e jogos repetidos anotados no bloco de grkhist ("Panathinaikos-AEK originally 3-2, 2-0 forfait")
    for l in HIST.get(temporada(a), "").split("\n"):
        mm = re.match(r"^\s*(\S.*?)\s*-\s*(\S.*?)\s+originally\s+(\d+)[-:](\d+)\s*,\s*(\d+)[-:](\d+)\s*(.*)$", l)
        if not mm:
            continue
        mand, vis = chave(mm.group(1), a, "RSSSF"), chave(mm.group(2), a, "RSSSF")
        j = next((j for j in jogos if (j["m"], j["v"]) == (mand, vis)), None)
        if j is None:
            ocorr[a].append(f"nota da RSSSF sem jogo na matriz: {l.strip()}")
            continue
        if (j["gm"], j["gv"]) != (int(mm.group(5)), int(mm.group(6))):
            ocorr[a].append(f"nota da RSSSF com placar diferente da matriz: {l.strip()} (matriz {j['gm']}-{j['gv']})")
        if "forfait" in mm.group(7).lower():
            j["especial"] = "awd"
            j["obs"] = f"{mm.group(3)}-{mm.group(4)} em campo; vitória dada fora de campo (RSSSF)"
        else:
            j["obs"] = f"jogo repetido; o primeiro terminou {mm.group(3)}-{mm.group(4)} (RSSSF)"
    return jogos, url


def tabela_rsssf(a: int, clubes_ano: set | None = None) -> tuple[list[dict], str] | None:
    """Tabela final da RSSSF: grkhist.html até 1998/99; depois, a tabela da página da temporada que tem os clubes da liga
    (a página traz também os play-offs e as outras divisões)."""
    if a <= 1998:
        t, url = HIST.get(temporada(a), ""), "https://www.rsssf.org/tablesg/grkhist.html"
    else:
        pg = pagina_rsssf(a)
        if not pg:
            return None
        t, url = pg
    blocos_, atual = [], []
    for x in rsssf.tabela(t):
        if atual and x["posicao"] < atual[-1]["posicao"]:
            blocos_.append(atual)   # começou outra tabela
            atual = []
        atual.append(x)
    if atual:
        blocos_.append(atual)
    if not blocos_:
        return None
    if clubes_ano:
        melhor = max(blocos_, key=lambda b: (len({clubes.esd(x["nome"], a) for x in b} & clubes_ano), len(b)))
    else:
        melhor = blocos_[0]
    return melhor, url


def carregar_ogol(a: int) -> list[dict]:
    res = []
    for o in json.loads((DADOS / "ogol" / f"gre1_{a}.json").read_text(encoding="utf-8")):
        if o["resultado"] == "ADI":
            continue
        if o["resultado"] == "ANU":   # 2014/15: jogos anulados no ogol que valeram (W.O.): ficam sem placar, como "DA"
            o = dict(o, gols_mandante=None, gols_visitante=None)
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
        arq = DADOS / "football-data" / f"G1_{str(a)[-2:]}{str(a + 1)[-2:]}.csv"
        if arq.exists():
            res[a] = [(chave(x["HomeTeam"], a, "football-data"), chave(x["AwayTeam"], a, "football-data"), data_fd(x["Date"]), x)
                      for x in ler_csv(arq) if x.get("HomeTeam") and x.get("FTHG")]
    return res


def carregar_esd() -> dict[int, list]:
    res = defaultdict(list)
    for x in ler_csv(DADOS / "engsoccerdata" / "greece_tier1.csv"):
        a = int(x["Season"])
        res[a].append((chave(x["home"], a, "engsoccerdata"), chave(x["visitor"], a, "engsoccerdata"), x["Date"], x))
    return res


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for arq in sorted((DADOS / "espn").glob("gre1_*.json")):
        a = int(arq.stem[5:9])
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(ATENAS).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
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
    """grkchamp.html: "1959/60  Panathinaïkos" (pelo ano inicial); "1928/29    not held"."""
    res = {}
    for m in re.finditer(r"^(\d{4})/\d{2}\s+(\S.*?)\s*$", rsssf.texto(DADOS / "rsssf" / "grkchamp.html"), re.M):
        a = int(m.group(1))
        if "not held" in m.group(2) or a < 1927:
            continue
        res[a] = clubes.esd(m.group(2).replace("ï", "i").replace("�", "i"), a) or m.group(2)
    return res


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pts: tuple[int, int, int]) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        if j["gm"] is None:
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            if j.get("dois"):   # derrota para os dois
                x[3] += 1; x[6] += pts[2]
            elif gp > gc:
                x[1] += 1; x[6] += pts[0]
            elif gp == gc:
                x[2] += 1; x[6] += pts[1]
            else:
                x[3] += 1; x[6] += pts[2]
    return t


def ordenar(t: dict[str, list[int]], ajuste: dict[str, int], criterio: str, jogos: list[dict] | None, pts) -> list[str]:
    """criterio: "vitorias" (pontos, vitórias, saldo, gols pró), "saldo" (pontos, saldo, gols pró), "media" (pontos, média
    de gols) ou "confronto" (pontos; entre os empatados, pontos e saldo nos jogos entre eles; depois saldo e gols pró)."""
    def p(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, _ = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        if criterio == "vitorias":
            return (-v, -(gp - gc), -gp)
        return (-(gp - gc), -gp)
    if criterio != "confronto":
        return sorted(sorted(t), key=lambda c: (-p(c), *geral(c)))
    grupos = defaultdict(list)
    for c in sorted(t):
        grupos[p(c)].append(c)
    res = []
    for pt in sorted(grupos, reverse=True):
        g = grupos[pt]
        if len(g) > 1 and jogos is not None:
            mini = calcular([j for j in jogos if j["m"] in g and j["v"] in g], pts)
            g.sort(key=lambda c: (-mini[c][6], -(mini[c][4] - mini[c][5]), *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def separar(jogos: list[dict], so: set | None = None) -> tuple[list[dict], list[dict]]:
    """Fase regular (o primeiro jogo de cada par mandante x visitante, pela data, entre os clubes de `so`) e o resto."""
    vistos, regular, resto = set(), [], []
    for j in sorted(jogos, key=lambda j: (j["data"] or "9999", j["rodada"] or 0)):
        if (j["m"], j["v"]) in vistos or (so and not {j["m"], j["v"]} <= so):
            resto.append(j)
        else:
            vistos.add((j["m"], j["v"]))
            regular.append(j)
    return regular, resto


def numeros(x: dict, pts) -> list[int]:
    """Números de uma linha de tabela da Wikipédia: J V E D GP GC Pts (com o ajuste)."""
    v, e, d = x["vitorias"] or 0, x["empates"] or 0, x["derrotas"] or 0
    return [v + e + d, v, e, d, x["gols_pro"], x["gols_contra"], pts[0] * v + pts[1] * e + pts[2] * d + (x["ajuste"] or 0)]


# ------------------------------------------------------------------ principal
def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
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
    clubes_por_ano: dict[int, set] = {}
    base_ano: dict[int, list[dict]] = {}

    # jogos de cada temporada antes de montar (a temporada seguinte diz quem caiu)
    for a in LIGA:
        if a >= OGOL_DESDE:
            base_ano[a] = ogol[a]
        else:
            base_ano[a], _ = matriz_rsssf(a, defaultdict(list))

    for a in LIGA:
        ocorr[a].extend(EXPLICACOES.get(a, []))
        T = temporada(a)
        pts = pontos(a)
        tbs = tabelas_wiki(a)
        wk = wiki(a)
        mz_w = defaultdict(list)   # matriz da Wikipédia: (m, v) -> [(g, g)]
        for j in wk["jogos"]:
            if j["fonte"] == "matriz":
                if j["m"] is None or j["v"] is None:
                    raise SystemExit(f"{T}: clube da matriz da Wikipédia sem cadastro: {j['nm']} x {j['nv']}")
                mz_w[(j["m"], j["v"])].append((j["gm"], j["gv"]))
        if a >= OGOL_DESDE:
            jogos, fonte_base, url_base = ogol[a], "ogol", None
        else:
            jogos, url_base = matriz_rsssf(a, ocorr)
            fonte_base = "RSSSF"
        if not jogos:
            raise SystemExit(f"{T}: sem jogos")
        for j in jogos:
            for lado in ("m", "v"):
                nomes[j[lado]][f"{j['fonte'].split(' ')[0].lower()}:{j['n' + lado]}"].add(a)

        # ---- fase regular e o resto (play-offs)
        maior = max(tbs, key=lambda tb: len(tb["times"]), default=None)
        if maior:
            for x in maior["times"]:
                if x["clube"] is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
        liga = {x["clube"] for x in maior["times"]} if maior else None
        if a >= OGOL_DESDE and (a in EUROPEU or a >= GRUPOS_DESDE):
            regular, resto = separar(jogos, liga)
        else:
            regular, resto = jogos, []
        fora = [j for j in jogos if liga and not {j["m"], j["v"]} <= liga]
        for j in fora:   # jogos contra clubes de fora da liga (acesso): ficam de fora
            ocorr[a].append(f"jogo com clube de fora da liga, fora do pacote: {j['m']} x {j['v']} ({j['data']}, {j['gm']}-{j['gv']})")
        jogos = [j for j in jogos if j not in fora]
        resto = [j for j in resto if j not in fora]
        reg_ids = {id(j) for j in regular}
        for j in jogos:   # jogo decidido fora de campo, sem placar no ogol
            if j["gm"] is not None:
                continue
            o = j["ogol"]
            if (a, j["m"], j["v"]) in DERROTA_DOIS_OGOL:
                j["gm"], j["gv"], j["especial"], j["dois"] = 0, 0, "awd", True
                j["obs"] = f"derrota para os dois: {DERROTA_DOIS_OGOL[(a, j['m'], j['v'])]}"
                ocorr[a].append(f"{j['m']} x {j['v']} ({j['data']}): {o['resultado']} no ogol; derrota para os dois")
                continue
            cand = mz_w.get((j["m"], j["v"]), [])
            fd_j = next((x for m, v, d, x in fd.get(a, []) if (m, v) == (j["m"], j["v"])), None)
            if cand and (id(j) in reg_ids or len(cand) > 1):
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
        for (b_, d_, m_, v_), (m2, v2, g1, g2, motivo) in INVERTIDOS.items():
            if b_ != a:
                continue
            j = next((j for j in jogos if (j["data"], j["m"], j["v"]) == (d_, m_, v_)), None)
            if j is None:
                raise SystemExit(f"{T}: jogo do mando trocado não encontrado: {m_} x {v_} ({d_})")
            j["m"], j["v"], j["gm"], j["gv"] = m2, v2, g1, g2
            j["obs"] = f"mando e placar corrigidos: {motivo}"
            ocorr[a].append(f"{m2} x {v2} ({d_}): mando e placar corrigidos ({motivo})")
        for (b_, m_, v_), (g1, g2, motivo, *esp) in CORRECOES.items():
            if b_ != a:
                continue
            j = next((j for j in jogos if (j["m"], j["v"]) == (m_, v_) and id(j) in reg_ids), None)
            if j is None:
                raise SystemExit(f"{T}: jogo da correção não encontrado: {m_} x {v_}")
            j["gm"], j["gv"] = g1, g2
            if esp:
                j["especial"] = esp[0]
            j["obs"] = ("resultado decidido fora de campo; " if j.get("especial") and not esp else "") + f"placar corrigido: {motivo}"
            ocorr[a].append(f"{m_} x {v_} ({j['data']}): placar corrigido para {g1}-{g2} ({motivo})")
        clubes_ano = sorted({j["m"] for j in regular} | {j["v"] for j in regular})
        clubes_por_ano[a] = set(clubes_ano)
        n = len(clubes_ano)
        esperados = n * (n - 1)
        if len(regular) != esperados:
            ocorr[a].append(f"fase regular com {len(regular)} jogos de {esperados}")
        if liga and liga != set(clubes_ano):
            ocorr[a].append(f"tabela da Wikipédia com outros clubes: {sorted(liga ^ set(clubes_ano))}")
        fase_reg = "Fase regular" if resto else "Liga"
        for j in regular:
            j["fase"] = fase_reg

        # ---- jogos-desempate (antes do ogol): fichas da Wikipédia em seções de play-off, entre clubes da liga
        desempates = []
        if a < OGOL_DESDE:
            for w in wk["jogos"]:
                if w["fonte"] == "matriz" or not re.search(r"(?i)play", " ".join(w["secao"])):
                    continue
                if not {w["m"], w["v"]} <= set(clubes_ano):
                    ocorr[a].append(f"jogo de play-off com clube de fora da liga (acesso), fora do pacote: {w['nm']} x "
                                    f"{w['nv']} {w['gm']}-{w['gv']} ({w['secao'][-1]})")
                    continue
                titulo = "título" if re.search(r"(?i)champion", w["secao"][-1]) else \
                    "3º lugar" if re.search(r"(?i)third", w["secao"][-1]) else "classificação"
                esp = "awd" if re.search(r"(?i)award", w["extra"] or "") else None
                desempates.append({"data": w["data"], "m": w["m"], "v": w["v"], "nm": w["nm"], "nv": w["nv"], "gm": w["gm"],
                                   "gv": w["gv"], "rodada": None, "fonte": "Wikipédia (ficha)", "fase": "Desempate",
                                   "grupo": None, "cidade": w["local"], "estadio": w["estadio"], "arbitro": w["arbitro"],
                                   "especial": esp, "gols_wiki": (w["gols_m"], w["gols_v"]),
                                   "obs": f"jogo-desempate pelo {titulo}, fora da tabela" + (" (vitória dada fora de campo)" if esp else "")})
        # desempates que só estão nas notas da tabela da Wikipédia ("7th place play-off: PAOK–Aris 0–0", "Relegation play-out:
        # Panionios–Makedonikos 3–2"), sem data
        ja = {(j["m"], j["v"], j["gm"], j["gv"]) for j in desempates}   # só contra os outros desempates (a fase regular
        # pode ter o mesmo par com o mesmo placar)
        for x in (maior or {}).get("times", []):
            nt = x["nota"] or x["hth"] or ""
            mt = re.match(r"(?i)^([^:]*play[-–]?(?:off|out)[^:]*):\s*(.*)$", nt)
            if not mt:
                continue
            tipo = (notas_wiki.traduzir(f"{mt.group(1)}: A–B 0–0") or "desempate").split(":")[0]
            for seg in re.split(r"\s*,\s*", re.sub(r"\(see below\)", "", mt.group(2))):
                mm = re.match(r"^\s*(\S.*?)\s*[–-]\s*(\S.*?)\s+(\d+)\s*[–-]\s*(\d+)\s*\.?\s*$", seg)
                if not mm:
                    continue
                m_, v_ = clubes.esd(mm.group(1), a), clubes.esd(mm.group(2), a)
                gm_, gv_ = int(mm.group(3)), int(mm.group(4))
                if not {m_, v_} <= set(clubes_ano):
                    ocorr[a].append(f"jogo de play-off da nota da Wikipédia com clube de fora da liga: {seg.strip()}")
                    continue
                if (m_, v_, gm_, gv_) in ja:
                    continue
                ja.add((m_, v_, gm_, gv_))
                desempates.append({"data": None, "m": m_, "v": v_, "nm": mm.group(1), "nv": mm.group(2), "gm": gm_, "gv": gv_,
                                   "rodada": None, "fonte": "Wikipédia (nota da tabela)", "fase": "Desempate", "grupo": None,
                                   "obs": f"{tipo}, fora da tabela (placar da nota da tabela da Wikipédia; sem data)"})
        if desempates:
            jogos = jogos + [j for j in desempates if j not in jogos]

        # ---- antes do ogol: placar em que a matriz da RSSSF e a da Wikipédia discordam. Fica o que deixa os dois clubes mais
        # perto das tabelas publicadas (RSSSF e Wikipédia), somando as diferenças de J V E D GP GC nas duas
        if a < OGOL_DESDE and mz_w:
            pubs = []
            tr_ = tabela_rsssf(a, set(clubes_ano))
            if tr_:
                pubs.append({chave(x["nome"], a, "RSSSF (tabela)"): [x["jogos"], x["vitorias"], x["empates"], x["derrotas"],
                                                                     x["gols_pro"], x["gols_contra"]] for x in tr_[0]})
            if maior:
                pubs.append({x["clube"]: numeros(x, pts)[:6] for x in maior["times"]})

            def distancia(lista, cs):
                t_ = calcular(lista, pts)
                return sum(abs(t_[c][k] - p_[c][k]) for p_ in pubs for c in cs if c in p_ for k in range(6))
            por_par = defaultdict(list)
            for j in regular:
                por_par[(j["m"], j["v"])].append(j)
            for par, pl in mz_w.items():
                js_ = por_par.get(par, [])
                if len(pl) != 1 or len(js_) != 1 or (js_[0]["gm"], js_[0]["gv"]) == pl[0] or js_[0].get("especial") or not pubs:
                    continue
                j = js_[0]
                antes = distancia(regular, par)
                velho = (j["gm"], j["gv"])
                j["gm"], j["gv"] = pl[0]
                if distancia(regular, par) < antes:
                    j["fonte"] = "RSSSF (matriz) + Wikipédia (placar)"
                    j["obs"] = (f"placar da matriz da Wikipédia; a da RSSSF dá {velho[0]}-{velho[1]}, que não fecha com as "
                                f"tabelas publicadas")
                    ocorr[a].append(f"{par[0]} x {par[1]}: fica {pl[0][0]}-{pl[0][1]} (matriz da Wikipédia), que fecha com as "
                                    f"tabelas; a matriz da RSSSF dá {velho[0]}-{velho[1]}")
                else:
                    j["gm"], j["gv"] = velho
            # placares trocados entre duas células da mesma linha ou coluna: só fecham trocando os dois juntos
            restam = [(par, pl[0], por_par[par][0]) for par, pl in mz_w.items()
                      if len(pl) == 1 and len(por_par.get(par, [])) == 1 and (por_par[par][0]["gm"], por_par[par][0]["gv"]) != pl[0]
                      and not por_par[par][0].get("especial")]
            usados_p = set()
            for i1 in range(len(restam)):
                for i2 in range(i1 + 1, len(restam)):
                    if i1 in usados_p or i2 in usados_p:
                        continue
                    (p1, s1, j1), (p2, s2, j2) = restam[i1], restam[i2]
                    cs = set(p1) | set(p2)
                    antes = distancia(regular, cs)
                    v1, v2 = (j1["gm"], j1["gv"]), (j2["gm"], j2["gv"])
                    (j1["gm"], j1["gv"]), (j2["gm"], j2["gv"]) = s1, s2
                    if distancia(regular, cs) < antes:
                        usados_p |= {i1, i2}
                        for (par, s, j), v in (((p1, s1, j1), v1), ((p2, s2, j2), v2)):
                            j["fonte"] = "RSSSF (matriz) + Wikipédia (placar)"
                            j["obs"] = (f"placar da matriz da Wikipédia; a da RSSSF dá {v[0]}-{v[1]} (placares trocados entre "
                                        f"duas células), que não fecha com as tabelas publicadas")
                            ocorr[a].append(f"{par[0]} x {par[1]}: fica {s[0]}-{s[1]} (matriz da Wikipédia), que fecha com as "
                                            f"tabelas; a matriz da RSSSF dá {v[0]}-{v[1]} (trocado com outro jogo)")
                    else:
                        (j1["gm"], j1["gv"]), (j2["gm"], j2["gv"]) = v1, v2

        # ---- conferência jogo a jogo com a matriz da Wikipédia
        if mz_w:
            por_par = defaultdict(list)
            for j in regular:
                por_par[(j["m"], j["v"])].append(j)
            dif = []
            for par, pl in mz_w.items():
                nossos = sorted((j["gm"], j["gv"]) for j in por_par.get(par, []))
                if sorted(pl) != nossos and not (len(pl) < len(nossos) and set(pl) <= set(nossos)):
                    outras = sorted((int(x[cm]), int(x[cv])) for dados, cm, cv in ((fd, "FTHG", "FTAG"), (esd, "hgoal", "vgoal"))
                                    for m, v, d, x in dados.get(a, []) if (m, v) == par and str(x[cm]).isdigit())
                    apoio = " (football-data e engsoccerdata = ogol)" if outras and set(outras) <= set(nossos) else ""
                    dif.append(f"{par[0]} x {par[1]}: {fonte_base} {', '.join(f'{x}-{y}' for x, y in nossos) or '—'}; "
                               f"Wikipédia {', '.join(f'{x}-{y}' for x, y in sorted(pl))}{apoio}")
            for d in dif[:15]:
                ocorr[a].append(f"placar diferente na matriz da Wikipédia — {d}")
            if len(dif) > 15:
                ocorr[a].append(f"... e mais {len(dif) - 15} pares com placar diferente na matriz da Wikipédia")
        elif a < OGOL_DESDE:
            ocorr[a].append("sem matriz na Wikipédia para conferir os jogos")

        # ---- engsoccerdata e football-data (casados pelo par e pela data mais próxima)
        for fonte, dados, cm, cv in (("engsoccerdata", esd, "hgoal", "vgoal"), ("football-data", fd, "FTHG", "FTAG")):
            if a not in dados or a < OGOL_DESDE:
                continue
            usados = set()
            for m, v, d, x in dados[a]:
                if not (str(x[cm]).isdigit() and str(x[cv]).isdigit()):   # "NA" no engsoccerdata
                    continue
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
        for e in espn.get(a, []):
            m, v = mapa_espn.get(e["mandante_id"], a), mapa_espn.get(e["visitante_id"], a)
            if m is None or v is None:
                continue
            b = casar(jogos, usados, m, v, e["data"], 3)
            if b is None:
                continue
            nomes[m][f"espn:{e['mandante']}"].add(a)
            b["espn"] = e
            if (e["gm"], e["gv"]) != (b["gm"], b["gv"]) and not b.get("especial"):
                ocorr[a].append(f"placar diferente na ESPN — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, ESPN {e['gm']}-{e['gv']}")

        # ---- fase regular: tabelas publicadas, ajuste de pontos e ordem
        ref = calcular(regular, pts)
        w_reg = maior if maior and len({x["clube"] for x in maior["times"]} & set(clubes_ano)) >= n - 2 else None
        ajuste: dict[str, int] = {}
        if w_reg:
            for x in w_reg["times"]:
                nomes[x["clube"]][f"wikipedia:{x['nome']}"].add(a)
                if x["ajuste"]:
                    ajuste[x["clube"]] = x["ajuste"]
        rs = None
        tr = tabela_rsssf(a, set(clubes_ano))
        if tr:
            linhas, url_rs = tr
            for x in linhas:
                x["clube"] = chave(x["nome"], a, "RSSSF (tabela)")
                nomes[x["clube"]][f"rsssf:{re.sub(r'[(]-?[0-9]+[)]|[*]+', '', x['nome']).strip()}"].add(a)
            if {x["clube"] for x in linhas} == set(clubes_ano):
                rs = linhas
            else:
                ocorr[a].append(f"tabela da RSSSF com outros clubes: {sorted({x['clube'] for x in linhas} ^ set(clubes_ano))}")
        wiki_ok = {x["clube"] for x in (w_reg or {}).get("times", []) if numeros(x, pts) == (ref[x["clube"]][:6] + [
            ref[x["clube"]][6] + (x["ajuste"] or 0)] if x["clube"] in ref else None)}
        if rs:
            for x in rs:   # punição que só a RSSSF traz (se a tabela da Wikipédia fecha sem ela, é erro da RSSSF)
                c = ref.get(x["clube"])
                if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                        and x["pontos"] != c[6] and x["clube"] not in ajuste and x["clube"] in wiki_ok:
                    ocorr[a].append(f"a tabela da RSSSF dá {x['pontos']} pontos ao {x['clube']}; os jogos dão {c[6]}, como a "
                                    f"tabela da Wikipédia: erro da RSSSF")
                    continue
                if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                        and x["pontos"] != c[6] and x["clube"] not in ajuste:
                    ajuste[x["clube"]] = x["pontos"] - c[6]
                    ocorr[a].append(f"punição tirada da tabela da RSSSF: {x['clube']} {x['pontos'] - c[6]:+d} pontos")
        conferidas = divergentes = 0
        confere = {}
        publicadas = []
        if rs:
            publicadas.append(("RSSSF", url_rs, rs))
        if w_reg:
            publicadas.append(("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                               [dict(x, posicao=x["posicao"], **dict(zip(("jogos", "vitorias", "empates", "derrotas", "gols_pro",
                                                                         "gols_contra", "pontos"), numeros(x, pts))))
                                for x in w_reg["times"]]))
        if not publicadas:
            ocorr[a].append("sem tabela publicada legível (RSSSF e Wikipédia)")
        for fonte, url, linhas in publicadas:
            erro = []
            for x in linhas:
                c = ref.get(x["clube"])
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = (c[:6] + [c[6] + ajuste.get(x["clube"], 0)]) if c else None
                if pub != meu:
                    erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": fase_reg, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"], "empates": x["empates"],
                    "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"],
                    "fonte": url})
            confere[fonte] = not erro
            if erro:
                divergentes += 1
            else:
                conferidas += 1
        for fonte, url, linhas in publicadas:   # cada divergência diz se a outra tabela fecha com os jogos naquele clube
            outra = next((ls for f_, u_, ls in publicadas if f_ != fonte), None)
            n_err = 0
            for x in linhas:
                c = ref.get(x["clube"])
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = (c[:6] + [c[6] + ajuste.get(x["clube"], 0)]) if c else None
                if pub == meu:
                    continue
                n_err += 1
                if n_err > 8:
                    continue
                y = next((y for y in outra or [] if y["clube"] == x["clube"]), None)
                outra_ok = y is not None and [y["jogos"], y["vitorias"], y["empates"], y["derrotas"], y["gols_pro"],
                                              y["gols_contra"], y["pontos"]] == meu
                nome_outra = "Wikipédia" if fonte == "RSSSF" else "RSSSF"
                ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {x['clube']} tabela {pub} jogos {meu}"
                                + (f" (a tabela da {nome_outra} fecha com os jogos)" if outra_ok else ""))
        if w_reg and (confere.get("Wikipédia") or not confere.get("RSSSF")):
            ordem = [x["clube"] for x in w_reg["times"]]
            fonte_ordem = "Wikipédia (ordem oficial)"
        elif rs:
            ordem = [x["clube"] for x in sorted(rs, key=lambda x: x["posicao"])]
            fonte_ordem = "RSSSF (ordem oficial)"
            if w_reg:
                ocorr[a].append("a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF")
        else:
            ordem = ordenar(ref, ajuste, "confronto", regular, pts)
            fonte_ordem = "calculada"
        if set(ordem) != set(clubes_ano):
            ocorr[a].append(f"ordem oficial com outros clubes ({sorted(set(ordem) ^ set(clubes_ano))}): fica a calculada")
            ordem = ordenar(ref, ajuste, "confronto", regular, pts)
            fonte_ordem = "calculada"
        tentativas = {cr: ordenar(ref, ajuste, cr, regular, pts) for cr in ("confronto", "saldo", "vitorias", "media")}
        ok = [cr for cr, o in tentativas.items() if o == ordem]
        criterio = ok[0] if ok else min(tentativas, key=lambda cr: sum(x != y for x, y in zip(tentativas[cr], ordem)))
        if not ok:
            dif = [c for c, d in zip(ordem, tentativas[criterio]) if c != d]
            desemp = {c for j in desempates for c in (j["m"], j["v"])}
            if not set(dif) <= desemp:
                ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo ({criterio}) difere em "
                                f"{len(dif)} posições (ex.: {dif[:2]})")
        criterios[a] = (criterio, bool(ok))

        # ---- play-offs
        fases_po = []   # (fase, grupo, jogos, tabela da Wikipédia)
        if resto:
            tbs_po = [tb for tb in tbs if tb is not maior and len(tb["times"]) < n]
            for tb in tbs_po:
                for x in tb["times"]:
                    if x["clube"] is None:
                        raise SystemExit(f"{T}: nome da Wikipédia (play-off) sem cadastro: {x['nome']}")
            tipos = []
            for tb in tbs_po:
                conj = {x["clube"] for x in tb["times"]}
                if a in EUROPEU:
                    fase = "Play-off europeu"
                elif ordem[0] in conj:
                    fase = "Play-off do título"
                elif ordem[-1] in conj:
                    fase = "Play-out de rebaixamento"
                else:
                    fase = "Play-off europeu"
                tipos.append((fase, conj, tb))
            por_tb = defaultdict(list)
            sobra = []
            for j in resto:
                k = next((i for i, (_, conj, _) in enumerate(tipos) if {j["m"], j["v"]} <= conj), None)
                (sobra if k is None else por_tb[k]).append(j)
            for k, (fase, conj, tb) in enumerate(tipos):
                if por_tb[k]:
                    fases_po.append((fase, None, por_tb[k], tb))
                else:
                    ocorr[a].append(f"tabela de play-off da Wikipédia sem jogos no ogol: {sorted(conj)}")
            if sobra:   # jogo fora das tabelas (desempate do play-off europeu)
                fases_po.append(("Play-off europeu" if a in EUROPEU else "Desempate", "Final" if a in EUROPEU else None, sobra, None))
                for j in sobra:
                    ocorr[a].append(f"jogo fora das tabelas de play-off: {j['m']} x {j['v']} ({j['data']}, {j['gm']}-{j['gv']})")
            for fase, grupo, comp, tb in fases_po:
                for j in comp:
                    j["fase"], j["grupo"] = fase, grupo
                if tb is None:
                    continue
                # 2007/08-2016/17: a tabela do play-off europeu traz só os jogos dele (com o bônus em pontos); desde 2019/20,
                # os números acumulados da fase regular e do play-off
                calc_po = calcular(comp if a in EUROPEU else regular + comp, pts)
                erro = []
                for x in tb["times"]:
                    c = x["clube"]
                    nomes[c][f"wikipedia:{x['nome']}"].add(a)
                    cp = calc_po.get(c, [0] * 7)
                    pub = numeros(x, pts)
                    meu = cp[:6] + [cp[6] + (x["ajuste"] or 0) + (0 if a in EUROPEU else ajuste.get(c, 0))]
                    if pub[:6] != meu[:6] or (a not in EUROPEU and pub[6] + ajuste.get(c, 0) != meu[6]):
                        erro.append(f"{c} tabela {pub} jogos {meu}")
                    tab["tabelas_publicadas"].append({
                        "temporada": T, "fase": fase, "grupo": grupo, "posicao": x["posicao"], "nome_fonte": x["nome"],
                        "clube": clubes.exibicao(c), "jogos": pub[0], "vitorias": x["vitorias"], "empates": x["empates"],
                        "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": pub[6],
                        "fonte": f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}"})
                if erro:
                    divergentes += 1
                    for e_ in erro[:6]:
                        ocorr[a].append(f"tabela do {fase} (Wikipédia) x jogos — {e_}")
                else:
                    conferidas += 1

        # ---- classificação final
        grupos_cl = [(f, comp, tb) for f, g, comp, tb in fases_po if tb is not None and f != "Play-off europeu"] \
            if a >= GRUPOS_DESDE else []
        if a >= GRUPOS_DESDE and len(grupos_cl) >= 2:
            ordem_tit = {"Play-off do título": 0, "Play-off europeu": 1, "Play-out de rebaixamento": 2}
            grupos_cl = sorted([(f, comp, tb) for f, g, comp, tb in fases_po if tb is not None], key=lambda x: ordem_tit[x[0]])
            ordem_final = [x["clube"] for f, comp, tb in grupos_cl for x in tb["times"]]
            fonte_final = "Wikipédia (ordem dos grupos do play-off)"
            ajuste_final = {x["clube"]: (x["ajuste"] or 0) + ajuste.get(x["clube"], 0) for f, comp, tb in grupos_cl for x in tb["times"]}
            numeros_cl = calcular([j for j in jogos if j["fase"] != "Desempate"], pts)
            fase_de = {x["clube"]: f for f, comp, tb in grupos_cl for x in tb["times"]}
        else:
            ordem_final, fonte_final = ordem, fonte_ordem
            ajuste_final = ajuste
            numeros_cl = ref
            fase_de = {}
        if set(ordem_final) != set(clubes_ano):
            raise SystemExit(f"{T}: classificação final com outros clubes: {sorted(set(ordem_final) ^ set(clubes_ano))}")
        prox = next((b for b in LIGA if b > a), None)
        prox_clubes = ({c for j in base_ano[prox] for c in (j["m"], j["v"])} if prox is not None else prox_2026)
        rebaixados = set()
        for c in clubes_ano:
            if c in prox_clubes:
                continue
            if clubes.CLUBES[c][1] == "CYP":
                ocorr[a].append(f"{c} não está na temporada seguinte, mas não caiu: campeão do Chipre convidado, voltou à liga "
                                f"cipriota")
            elif (a, c) in NAO_REBAIXADOS:
                ocorr[a].append(f"{c} não está na temporada seguinte, mas não caiu: {NAO_REBAIXADOS[(a, c)]}")
            else:
                rebaixados.add(c)
        campeao = ordem_final[0]
        if camp.get(a) and camp[a] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {camp[a]} (classificação: {campeao})")
        for pos, c in enumerate(ordem_final, 1):
            j_, v_, e_, d_, gp, gc, p = numeros_cl[c]
            pts_c = p + ajuste_final.get(c, 0)
            obs = None
            if c in fase_de:
                aj = ajuste_final.get(c, 0)
                obs = f"{fase_de[c].lower()}: pontos da fase regular e do play-off somados" + \
                    (f" ({aj:+d} pontos: metade dos pontos da fase regular no play-off europeu, ou punição)" if aj else "")
            nota = (w_reg and next((notas_wiki.traduzir(x["nota"] or x["hth"]) for x in w_reg["times"] if x["clube"] == c), None))
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": pts_c, "ajuste_pontos": pts_c - p,
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None, "fonte": fonte_final,
                "observacao": "; ".join(x for x in (obs, nota) if x) or None})

        # ---- partidas, gols, cartões, estatísticas
        jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["fase"] == "Desempate", j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
            hora = None
            if x and x.get("Time"):
                hora = datetime.fromisoformat(f"{data_fd(x['Date'])}T{x['Time']}").replace(tzinfo=LONDRES).astimezone(ATENAS).strftime("%H:%M")
            elif e:
                local = e["utc"].astimezone(ATENAS)
                if local.date().isoformat() == j["data"]:
                    hora = local.strftime("%H:%M")
            ids = ([f"ogol:{o['id']}"] if o else []) + ([f"espn:{e['id']}"] if e else [])
            fontes = [j["fonte"]] + (["football-data"] if x else []) + (["ESPN"] if e else [])
            obs = j.get("obs")
            if j.get("dois"):
                obs = obs or "derrota para os dois"
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
                "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": j.get("especial"), "estadio": (e or {}).get("estadio") or j.get("estadio"),
                "cidade": (e or {}).get("cidade") or j.get("cidade"), "publico": (e or {}).get("publico") or None,
                "fonte": " + ".join(fontes), "fonte_id": "|".join(ids), "gols_texto": None, "observacao": obs,
                "arbitro": (x or {}).get("Referee") or j.get("arbitro") or None, "_derrota_dois": bool(j.get("dois"))})
            gols_ano += j["gm"] + j["gv"]
            if j.get("gols_wiki") and not j.get("especial"):   # ficha da Wikipédia (desempates)
                gm_, gv_ = j["gols_wiki"]
                if (len(gm_), len(gv_)) == (j["gm"], j["gv"]):
                    for c, lista in ((j["m"], gm_), (j["v"], gv_)):
                        for nome, mi in lista:
                            tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(c), "jogador": nome, "minuto": mi,
                                                "acrescimo": None, "tipo": "normal", "fonte": "Wikipédia (ficha)"})
                    autor_ano += j["gm"] + j["gv"]
            if e and e["lances"] and not j.get("especial"):
                vistos_l = set()   # a ESPN às vezes repete lances (mesmo minuto, lado e jogador)
                e["lances"] = [l for l in e["lances"] if not ((k_ := (l["tipo"], l["minuto"], l["lado"], tuple(l["jogadores"] or ()),
                                                                      l["gol"], l["amarelo"], l["vermelho"])) in vistos_l
                                                              or vistos_l.add(k_))]
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
                parcial = calcular(ate, pts)
                for pos, c in enumerate(ordenar(parcial, ajuste, criterio, ate, pts), 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        # ---- edição, fases, conferência
        fontes_ed = [fonte_base] + (["engsoccerdata"] if a in esd and a >= OGOL_DESDE else []) \
            + (["football-data"] if a in fd else []) + (["ESPN"] if a in espn else []) + (["RSSSF"] if rs else []) \
            + (["Wikipédia"] if w_reg or mz_w else [])
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        formato = "pontos corridos (turno e returno)"
        if a in EUROPEU and fases_po:
            formato = "pontos corridos (turno e returno) e play-off europeu do 2º ao 5º (fora da classificação)"
        elif a >= GRUPOS_DESDE and fases_po:
            formato = ("fase regular em turno e returno e play-offs (título e rebaixamento" +
                       (", e europeu do 5º ao 8º, com metade dos pontos" if a >= 2024 else "") +
                       "), com os pontos da fase regular acumulados")
        sist = {(3, 2, 1): "3 pontos por vitória, 2 por empate e 1 por derrota", (2, 1, 0): "2 pontos por vitória",
                (3, 1, 0): "3 pontos por vitória"}[pts]
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pts[0], "pontos_empate": pts[1] if pts == (3, 2, 1) else None,
                               "pontos_derrota": pts[2] if pts == (3, 2, 1) else None, "formato": formato,
                               "campeao": clubes.exibicao(campeao),
                               "vice": clubes.exibicao(ordem_final[1]), "fontes": " + ".join(dict.fromkeys(fontes_ed)),
                               "observacao": "; ".join(x for x in (sist if pts == (3, 2, 1) else "",
                                                                    f"punições: {pun}" if pun else "",
                                                                    "decidido em jogo-desempate" if any(
                                                                        "título" in (j.get("obs") or "") for j in desempates) else "")
                                                       if x) or None})
        crit_txt = {"vitorias": "pontos, vitórias, saldo de gols, gols pró", "saldo": "pontos, saldo de gols, gols pró",
                    "confronto": "pontos, confronto direto, saldo de gols, gols pró",
                    "media": "pontos, média de gols (goal average)"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": fase_reg, "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        vistas = []
        for fase, grupo, comp, tb in fases_po + ([("Desempate", None, desempates, None)] if desempates else []):
            if fase in vistas:
                continue
            vistas.append(fase)
            tab["fases"].append({"temporada": T, "ordem": len(vistas) + 1, "fase": fase,
                                 "tipo": "mata_mata" if fase == "Desempate" else "grupos", "num_grupos": None if fase == "Desempate" else 1,
                                 "formato_serie": "jogo_unico" if fase == "Desempate" else "pontos_corridos",
                                 "criterio": "jogo-desempate, fora da tabela" if fase == "Desempate" else
                                 "pontos, com bônus pela posição na fase regular" if a in EUROPEU else
                                 "pontos acumulados com a fase regular" + (" (metade)" if fase == "Play-off europeu" else "")})
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

    # era antiga (1927/28-1958/59): a fase nacional entre os campeões regionais (coleta/gre-1/antigo.py)
    linhas_rel = antigo.montar(tab, nomes, ocorr) + linhas_rel

    # ---- clubes
    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = [{"codigo": "GRE", "nome": "Grécia", "confederacao": "UEFA"},
                     {"codigo": "CYP", "nome": "Chipre", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_espn, criterios)


def artilheiros(ocorr) -> list[dict]:
    """Artilheiro(s) de cada temporada pela lista da RSSSF (grktops.html: "1959/60  Kostas Nestoridis  AEK Athens  33";
    empate na linha seguinte, sem temporada)."""
    res, ano = [], None
    for l in rsssf.texto(DADOS / "rsssf" / "grktops.html").split("\n"):
        m = re.match(r"^(\d{4})/\d{2}\s+(\S.*?)\s{2,}(\S.*?)\s{2,}(\d+)\s*$", l)
        m2 = re.match(r"^\s{5,}(\S.*?)\s{2,}(\S.*?)\s{2,}(\d+)\s*$", l)
        if m:
            ano, nome, clube_txt, gols = int(m.group(1)), m.group(2), m.group(3), int(m.group(4))
        elif m2 and ano is not None:
            nome, clube_txt, gols = m2.group(1), m2.group(2), int(m2.group(3))
        else:
            if l.strip() and not l.startswith(" "):
                ano = None
            continue
        if ano not in TEMPORADAS:
            continue
        c = clubes.esd(clube_txt, ano)
        res.append({"temporada": temporada(ano), "jogador": nome.strip(), "clube": clubes.exibicao(c) if c else None,
                    "gols": gols, "fonte": "RSSSF (tablesg/grktops.html)"})
        if c is None:
            ocorr[ano].append(f"artilheiro com clube sem cadastro: {nome} ({clube_txt})")
    return res


def relatorio(linhas, ocorr, tab, mapa_espn, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Grego (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/gre-1/importar.py`. Pacote em `data/coleta/gre-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1927/28 a 2025/26. Sem 1928/29, 1934/35, 1940/41-1944/45, 1949/50 e 1951/52.", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor, {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- RSSSF: fase nacional de 1927/28 a 1958/59 (grkprehist.html); matriz de resultados de 1959/60 a 1992/93 (base "
        "dos jogos, sem data; grkhist.html e a página de cada temporada desde 1968/69); tabelas finais; lista de campeões e "
        "de artilheiros;",
        "- Wikipédia (en): matriz de resultados (conferência), tabelas da fase regular e dos play-offs, fichas dos "
        "jogos-desempate (data, local, autores dos gols);",
        "- ogol (zerozero): base dos jogos de 1993/94 em diante, com data e rodada; o clube pelo código do ogol; calendários "
        "em `data/cache/ogol-gre-1/` para os escudos;",
        "- engsoccerdata e football-data: conferência de placar de 1994/95 em diante; hora, árbitro e estatísticas do "
        "football-data;",
        "- ESPN (liga `gre.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.", "",
        "**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a "
        "oficial (Wikipédia; sem ela, RSSSF). Pontos: 3 por vitória, 2 por empate e 1 por derrota até 1972/73; 2-1-0 de "
        "1973/74 a 1991/92; 3-1-0 desde 1992/93 (`pontos_vitoria` traz o da vitória; o sistema 3-2-1 vai na observação da "
        "edição). Jogos-desempate (título, 3º lugar) entram na fase \"Desempate\", fora da tabela. Play-off europeu de "
        "2007/08 a 2016/17: fora da classificação. Desde 2019/20, a classificação final é a ordem dos grupos do play-off, "
        "com os números de todos os jogos e o ajuste (metade dos pontos no play-off europeu, punições) em `ajuste_pontos`. "
        "Rebaixado = clube que não está na 1ª divisão na temporada seguinte (os cipriotas voltaram à liga deles).", "",
        f"**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em "
        f"{cr['confronto']}, saldo em {cr['saldo']}, vitórias em {cr['vitorias']}, média de gols em {cr['media']}).", "",
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
        "- Cadastro em `coleta/comum-europa/clubes_gre.py`: pela linhagem do clube, como na Wikipédia (o alvo do link na "
        "tabela de cada temporada). Mesmo clube: Apollon Athens e Apollon Smyrnis; Apollon Salonika/Thessaloniki/Kalamarias; "
        "Xanthi e Skoda Xanthi; Pankorinthiakos e Korinthos; Megas Alexandros e Pierikos. Clubes diferentes: Atromitos "
        "Piraeus e Atromitos; Rodos e AE Rodos; AO Kerkyra e PAE Kerkyra; Chalkidona (2004/05, que o ogol põe no Atromitos).",
        f"- A ESPN é casada por votação jogo a jogo (mesma data e placar): {len(mapa_espn)} códigos.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Datas e rodadas de 1959/60 a 1992/93:** a matriz da RSSSF e a da Wikipédia não trazem; o ogol não tem esses "
        "jogos. Rodadas de 1994/95 a 1996/97: o ogol não traz.",
        "- **Era antiga (até 1958/59):** só a fase nacional; as ligas regionais ficam de fora.",
        "- **Autores dos gols antes da ESPN:** nenhuma fonte em lote (só as fichas dos jogos-desempate).",
        "- **Jogos de acesso contra clubes da 2ª divisão:** ficam de fora.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
