"""Monta o pacote da 1ª divisão escocesa (sco-1), 1890/91 a 2025/26, e o relatório docs/coleta/sco-1.md.

Base dos jogos: o calendário do ogol, com a rodada oficial (os jogos depois da divisão em dois grupos, que o ogol às vezes
marca "POff" e "POut" sem número, ficam com a rodada pela ordem de jogos de cada clube). O mesmo par de clubes joga 2, 3 ou
4 vezes na temporada: as outras fontes são casadas pelo par e pela data mais próxima.
  RSSSF          tabela final de 1890/91 a 1998/99 (scothist.html) e da página de cada temporada depois; listas de campeões e
                 de artilheiros;
  engsoccerdata  1994/95-2024/25: conferência de placar;
  football-data  1994/95-2025/26: conferência de placar; hora (2019/20+), árbitro e estatísticas por time;
  ESPN           hora, estádio, público, gols e cartões com minuto (clubes casados pelo código da ESPN);
  Wikipédia      tabela final de cada temporada (ordem oficial, punições) e lista oficial de rebaixados (caixa "relegated").

Regras: o placar é o do ogol; jogo decidido fora de campo entra com o resultado oficial (TRIBUNAL). Os gols da ESPN só
entram quando a soma bate com o placar.

Uso: python coleta/sco-1/importar.py
"""
from __future__ import annotations

import csv
import html
import json
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_sco as clubes  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, nome_oficial, rsssf_url, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from rsssf_sco import ler as ler_hist  # noqa: E402
from wiki_tabela import limpar, resultados as wiki_resultados, tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")   # hora local escocesa
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "sco-1.md"
FD = range(1994, 2026)
ESD = range(1994, 2025)

# placar corrigido no ogol: (ano, mandante, visitante, data) -> (gols, gols, motivo). Chaves de clubes_sco.
CORRECOES: dict[tuple, tuple] = {
    (1950, "Airdrieonians", "Falkirk", "1951-04-28"): (
        11, 1, "o ogol e a matriz da Wikipédia trazem 1-1; as tabelas da RSSSF e da Wikipédia só fecham com 11-1, e o Falkirk "
               "registra o 1-11 como a maior derrota da sua história na liga (fitbastats.com/falkirk, recordes do clube)"),
}

# resultado dado fora de campo: (ano, mandante, visitante, data) -> (gols, gols, vencedor, placar de campo, motivo). Fica `awd`.
TRIBUNAL: dict[tuple, tuple] = {
    (1996, "Aberdeen", "Dunfermline", "1996-09-28"): (
        3, 0, None, None, "derrota administrativa do Dunfermline, 3-0 (ficha do ogol); o football-data traz o mesmo 3-0"),
}

# jogo que falta no ogol: (ano, mandante, visitante) -> (data, gols, gols, rodada, motivo)
ACRESCIMOS: dict[tuple, tuple] = {
    (2015, "St Johnstone", "Hamilton Academical"): (
        "2016-01-16", 0, 0, None, "falta no calendário do ogol; o football-data, o engsoccerdata e a ESPN trazem 0-0 em "
                                  "16/01/2016"),
}

# até 1920/21 não havia rebaixamento: os últimos pediam reeleição à liga (desde 1921/22, acesso e rebaixamento automáticos)
SEM_REBAIXAMENTO = set(range(1890, 1921))
# clube que não está na temporada seguinte sem ter sido rebaixado: (ano, clube) -> motivo
NAO_REBAIXADOS: dict[tuple, str] = {}

# temporada interrompida: aceita menos jogos
INTERROMPIDAS = {2019: "interrompida em março de 2020 pela pandemia de covid-19, depois de 30 rodadas; a classificação final é "
                       "pela média de pontos por jogo (Celtic campeão, Hearts rebaixado)"}
# título dividido: 1890/91, Dumbarton e Rangers empataram em pontos e no jogo de desempate (2-2)
TITULO_DIVIDIDO = {1890: ("Dumbarton", "Rangers")}

# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
EXPLICACOES: dict[int, list[str]] = {
    1915: ["um jogo da temporada não foi disputado (379 de 380); as tabelas da RSSSF e da Wikipédia fecham com os 379"],
    1988: ["a caixa de resumo da Wikipédia não lista rebaixados; o Hamilton Academical, último, não está em 1989/90"],
    1989: ["a caixa de resumo da Wikipédia não lista rebaixados; o Dundee, último, não está em 1990/91"],
    1995: ["o Partick Thistle perdeu o play-off de rebaixamento e caiu; a caixa da Wikipédia lista só o Falkirk"],
}

COMPETICAO = {
    "slug": "sco-1", "nome": "Campeonato Escocês", "nome_curto": "Escocês", "tipo": "liga", "nivel": 1,
    "pais": "SCO", "pais_nome": "Escócia", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Escocês", "menu_painel": "Escócia · 1ª divisão",
    "do_painel": "do Campeonato Escocês", "o_painel": "o Campeonato Escocês",
    "observacao": "1ª divisão escocesa desde a criação da Scottish Football League (1890/91): Division One (até 1974/75), "
                  "Premier Division (1975/76-1997/98), Scottish Premier League (1998/99-2012/13) e Scottish Premiership. Sem "
                  "1939/40-1945/46 (guerra). O mesmo par se enfrenta 2, 3 ou 4 vezes; desde 2000/01 a liga se divide em dois "
                  "grupos de 6 depois da 33ª rodada. Não inclui os jogos de desempate pelo título (1890/91, 1904/05) nem os "
                  "play-offs de rebaixamento contra clubes da 2ª divisão.",
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
def carregar_ogol(a: int) -> list[dict]:
    """Jogos de liga do calendário do ogol: os de rodada ("R12") e os dos grupos depois da divisão ("POff", "POut"), que
    ficam com a rodada pela ordem de jogos de cada clube; nas temporadas antigas o ogol traz a fase "C", sem rodada (não havia
    rodadas fixas): a rodada fica vazia, como no Inglês. Jogos adiados ("ADI") ou anulados ("ANU") ficam de fora."""
    res = []
    for o in json.loads((DADOS / "ogol" / f"sco1_{a}.json").read_text(encoding="utf-8")):
        grupos = a >= 2000 and o["fase"] in ("POff", "POut", "")
        if o["resultado"] in ("ADI", "ANU") or not (o["rodada"] or o["fase"] == "C" or grupos):
            continue   # antes de 2000/01, "POff" é jogo de desempate pelo título (1904/05): fica de fora
        m = clubes.ogol(o["mandante_id"], a) or clubes.esd(o["mandante"], a)
        v = clubes.ogol(o["visitante_id"], a) or clubes.esd(o["visitante"], a)
        if m is None or v is None:
            raise SystemExit(f"{temporada(a)}: clube do ogol sem cadastro: {o['mandante']} ({o['mandante_id']}) x "
                             f"{o['visitante']} ({o['visitante_id']})")
        res.append({"data": o["data"], "m": m, "v": v, "nm": o["mandante"], "nv": o["visitante"], "gm": o["gols_mandante"],
                    "gv": o["gols_visitante"], "rodada": o["rodada"], "fase": "Liga", "grupo": None, "fonte": "ogol", "ogol": o})
    sem = sorted((j for j in res if not j["rodada"] and j["ogol"]["fase"] in ("POff", "POut", "")), key=lambda j: j["data"])
    if sem:   # rodada dos jogos dos grupos: a próxima rodada de cada clube
        feitas = Counter()
        for j in res:
            if j["rodada"]:
                feitas[j["m"]] += 1
                feitas[j["v"]] += 1
        for j in sem:
            r = max(feitas[j["m"]], feitas[j["v"]]) + 1
            j["rodada"] = r
            j["rodada_inferida"] = True
            feitas[j["m"]] = feitas[j["v"]] = r
    return res


def carregar_base() -> dict[int, list[dict]]:
    base = {a: carregar_ogol(a) for a in TEMPORADAS}
    for (a, m, v), (d, gm, gv, r, motivo) in ACRESCIMOS.items():
        base[a].append({"data": d, "m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "rodada": r, "fase": "Liga",
                        "grupo": None, "fonte": "football-data", "acrescimo": motivo})
    return base


def carregar_fd() -> dict[int, list]:
    res = {}
    for a in FD:
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        arq = DADOS / "football-data" / f"SC0_{cod}.csv"
        if not arq.exists():
            continue
        res[a] = [(chave(x["HomeTeam"], a, "football-data"), chave(x["AwayTeam"], a, "football-data"), data_fd(x["Date"]), x)
                  for x in ler_csv(arq) if x.get("HomeTeam") and x.get("FTHG")]
    return res


def carregar_esd() -> dict[int, list]:
    res = defaultdict(list)
    for x in ler_csv(DADOS / "engsoccerdata" / "scotland_tier1.csv"):
        a = int(x["Season"])
        res[a].append((chave(x["home"], a, "engsoccerdata"), chave(x["visitor"], a, "engsoccerdata"), x["Date"], x))
    return res


def inverter(por_par: dict, j: dict, motivo: str, ocorr: list) -> None:
    """Troca o mando de um jogo do ogol (o par aparece invertido em relação às outras fontes)."""
    por_par[(j["m"], j["v"])].remove(j)
    ocorr.append(f"mando corrigido: o ogol traz {j['m']} {j['gm']}-{j['gv']} {j['v']} ({j['data']}); {motivo}")
    j.update(m=j["v"], v=j["m"], gm=j["gv"], gv=j["gm"], nm=j["nv"], nv=j["nm"], invertido=motivo)
    por_par[(j["m"], j["v"])].append(j)


def casar(por_par: dict, usados: set, m: str, v: str, d: str, dias: int = 20) -> dict | None:
    """Jogo da base do par (m, v) com a data mais próxima de `d`, ainda não casado, a até `dias` dias."""
    cand = [j for j in por_par.get((m, v), []) if id(j) not in usados]
    if not cand:
        return None
    j = min(cand, key=lambda j: abs((date.fromisoformat(j["data"]) - date.fromisoformat(d)).days))
    if abs((date.fromisoformat(j["data"]) - date.fromisoformat(d)).days) > dias and len(cand) > 1:
        return None   # com um só jogo do par ainda livre, a data diferente é jogo adiado: casa assim mesmo
    usados.add(id(j))
    return j


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


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for a in range(2001, 2026):
        arq = DADOS / "espn" / f"sco1_{a}.json"
        if not arq.exists():
            continue
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(LONDRES).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
                              gv=int(j["gols_visitante"])))
        if jogos:
            res[a] = jogos
    return res


def texto_wiki(a: int) -> str:
    arq = DADOS / "wikipedia" / f"{wiki_titulo(a)}.wiki"
    return arq.read_text(encoding="utf-8") if arq.exists() else ""


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


def texto_rsssf(nome: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", (DADOS / "rsssf" / nome).read_bytes().decode("latin-1"))).replace("\r", "")


def campeoes_rsssf() -> dict[int, str]:
    """Campeão de cada temporada pela lista da RSSSF (scotchamp.html: "1891   Dumbarton", pelo ano final; "*" e "-" marcam o
    primeiro e o último título do clube). 1890/91 traz os dois campeões; fica o primeiro."""
    res = {}
    for m in re.finditer(r"^(\d{4})\s+[*-]?\s*(\S[^\n]*?)\s*$", texto_rsssf("scotchamp.html"), re.M):
        a = int(m.group(1)) - 1
        if a in TEMPORADAS and a not in res:
            res[a] = clubes.esd(re.split(r"\s{2,}|,| and ", m.group(2))[0], a)
    return res


def rebaixados_wiki(a: int) -> set | None:
    """Rebaixados pela caixa de resumo do artigo da temporada ("| relegated = ..."); "None" = ninguém caiu."""
    arq = DADOS / "wikipedia" / f"{wiki_titulo(a)}.wiki"
    if not arq.exists():
        return None
    m = re.search(r"\|\s*relegated\s*=([^\n]*)", arq.read_text(encoding="utf-8"))
    if not m:
        return None
    if "[[" not in m.group(1):
        return set() if re.search(r"(?i)none|n/a|—", m.group(1)) or not m.group(1).strip() else None
    res = set()
    for alvo, nome in re.findall(r"\[\[([^|\]]+)(?:\|([^\]]*))?\]\]", m.group(1)):
        c = clubes.esd(nome or alvo, a) or clubes.esd(alvo, a)
        if c is None:
            raise SystemExit(f"{temporada(a)}: rebaixado da Wikipédia sem cadastro: {nome or alvo}")
        res.add(c)
    return res


# ------------------------------------------------------------------ RSSSF: tabela final das páginas por temporada
LINHA_A = re.compile(r"^\s*(\d+)\s*\.?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(-?\d+)\b(.*)$")   # J V E D GP-GC Pts
LINHA_B = re.compile(r"^\s*(\d+)\s*\.?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\b(.*)$")         # Pts J V E D GP GC
LINHA_C = LINHA_B   # J V E D GP GC Pts (mesmo desenho, outra ordem)


def tabela_rsssf(a: int, clubes_ano: set, jogos_time: int) -> list[dict] | None:
    """Tabela final de uma página da RSSSF por temporada (1999/00 em diante): as linhas com o número de jogos da temporada
    inteira. Nas temporadas com divisão em dois grupos, a página traz a tabela depois da 33ª rodada e as dos dois grupos,
    com 38 jogos: ficam as dos grupos. Vale a primeira linha de cada clube; a linha só vale se J = V + E + D."""
    arq = DADOS / "rsssf" / rsssf_url(a).rsplit("/", 1)[1]
    if not arq.exists():
        return None
    achados: dict[str, dict] = {}
    for l in texto_rsssf(arq.name).split("\n"):
        for regex, ordem in ((LINHA_A, "jvedgp"), (LINHA_C, "jvedggp"), (LINHA_B, "pjvedgg")):
            m = regex.match(l)
            if not m:
                continue
            g = [int(v) for v in m.groups()[2:9]]
            j, v, e, d, gp, gc, p = g if ordem != "pjvedgg" else (g[1], g[2], g[3], g[4], g[5], g[6], g[0])
            if j != v + e + d or j != jogos_time:
                continue
            nome = re.sub(r"\s*(\(\d\)|\[-?\d+\])\s*$", "", m.group(2)).strip()
            c = clubes.esd(nome, a) or clubes.esd(re.sub(r"\s*\(.*?\)", "", nome), a)
            if c in clubes_ano and c not in achados:
                achados[c] = {"posicao": int(m.group(1)), "nome": nome, "clube": c, "jogos": j, "vitorias": v, "empates": e,
                              "derrotas": d, "gols_pro": gp, "gols_contra": gc, "pontos": p}
            break
    if set(achados) != clubes_ano:
        return None
    return sorted(achados.values(), key=lambda x: x["posicao"])


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pv: int) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        for lado, c, gp, gc in (("m", j["m"], j["gm"], j["gv"]), ("v", j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            if j.get("vencedor"):   # resultado dado fora de campo com o placar mantido; "nenhum": derrota para os dois
                if j["vencedor"] == lado:
                    x[1] += 1; x[6] += pv
                else:
                    x[3] += 1
            elif gp > gc:
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
    if criterio in ("confronto_fora", "confronto_geral"):
        # pontos nos jogos entre os empatados, aplicado de novo entre os que seguem empatados; depois, em "confronto_fora",
        # saldo e gols fora de casa nesses jogos; por fim saldo e gols pró no campeonato
        def rank(g: list[str]) -> list[str]:
            if len(g) == 1 or jogos is None:
                return sorted(g, key=geral)
            jg = [j for j in jogos if j["m"] in g and j["v"] in g]
            mini = calcular(jg, pv)
            fora = Counter()
            for j in jg:
                fora[j["v"]] += j["gv"]
            sub = defaultdict(list)
            for c in g:
                sub[mini[c][6]].append(c)
            res_ = []
            for p in sorted(sub, reverse=True):
                s = sub[p]
                if len(s) < len(g):
                    res_ += rank(s)
                elif criterio == "confronto_fora":
                    res_ += sorted(s, key=lambda c: (-(mini[c][4] - mini[c][5]), -fora[c], *geral(c)))
                else:
                    res_ += sorted(s, key=geral)
            return res_
        por_pts = defaultdict(list)
        for c in t:
            por_pts[pts(c)].append(c)
        return [c for p in sorted(por_pts, reverse=True) for c in rank(por_pts[p])]
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


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    base = carregar_base()
    fd = carregar_fd()
    esd = carregar_esd()
    espn = carregar_espn()
    wiki = carregar_wiki()
    camp_rs = campeoes_rsssf()
    mapa_espn = votar(base, espn, "mandante_id", "visitante_id")
    prox_2026 = {clubes.ogol(o[f"{l}_id"]) or clubes.esd(o[l]) for o in json.loads(
        (DADOS / "ogol" / f"sco1_{TEMPORADAS[-1] + 1}.json").read_text(encoding="utf-8")) for l in ("mandante", "visitante")}
    rs_hist = ler_hist(DADOS / "rsssf" / "scothist.html")

    nomes = defaultdict(lambda: defaultdict(set))   # chave -> "fonte:nome" -> anos
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel = []
    criterios = {}

    for a in TEMPORADAS:
        T = temporada(a)
        ocorr[a].extend(EXPLICACOES.get(a, []))
        jogos = base[a]
        clubes_ano = sorted({j["m"] for j in jogos} | {j["v"] for j in jogos})
        n = len(clubes_ano)
        # o par se repete (2, 3 ou 4 jogos); a temporada deve ter o mesmo número de jogos por par
        pares = Counter((j["m"], j["v"]) for j in jogos)
        k_par = Counter(pares.values())
        divisao = a >= 2000 and n == 12 and max(j["rodada"] or 0 for j in jogos) > 33 and a not in INTERROMPIDAS
        vezes_par = max(1, round(len(jogos) / (n * (n - 1))))
        esperados = n * (n - 1) // 2 * 38 // (n - 1) if divisao else n * (n - 1) * vezes_par
        if len(jogos) != esperados and a not in INTERROMPIDAS:
            ocorr[a].append(f"temporada com {len(jogos)} jogos de {esperados} (jogos por par: {dict(k_par)})")
        por_par = defaultdict(list)
        for j in jogos:
            por_par[(j["m"], j["v"])].append(j)
        pv = 3 if a >= 1994 else 2
        for j in jogos:
            nomes[j["m"]][f"{j['fonte']}:{j['nm']}"].add(a)
            nomes[j["v"]][f"{j['fonte']}:{j['nv']}"].add(a)
            if j.get("acrescimo"):
                ocorr[a].append(f"jogo acrescentado: {j['m']} {j['gm']}-{j['gv']} {j['v']} ({j['data']}) — {j['acrescimo']}")
            k = (a, j["m"], j["v"], j["data"])
            if k in CORRECOES:
                gm, gv, motivo = CORRECOES[k]
                ocorr[a].append(f"placar corrigido: {j['m']} x {j['v']} de {j['gm']}-{j['gv']} para {gm}-{gv} — {motivo}")
                j["gm"], j["gv"] = gm, gv
            if k in TRIBUNAL:
                gm, gv, venc, campo, motivo = TRIBUNAL[k]
                orig = j["ogol"]["resultado"] if j.get("ogol") else f"{j['gm']}-{j['gv']}"
                gm, gv = (j["gm"], j["gv"]) if gm is None else (gm, gv)
                ocorr[a].append(f"resultado decidido fora de campo: {j['m']} x {j['v']} fica {gm}-{gv}"
                                f"{' com vitória do ' + j[venc] if venc in ('m', 'v') else ' com derrota para os dois' if venc == 'nenhum' else ''}"
                                f" (ogol {orig}) — {motivo}")
                j.update(gm=gm, gv=gv, especial="awd", campo=campo, vencedor=venc)
            if j["gm"] is None:
                raise SystemExit(f"{T}: jogo sem placar no ogol ({j['ogol']['resultado']}) e fora de TRIBUNAL: {j['m']} x {j['v']} "
                                 f"({j['data']}, {j['ogol']['url']})")

        dif_mz = []
        # ---- Wikipédia: matriz de resultados (conferência jogo a jogo; o par pode ter 2, 3 ou 4 placares)
        grades = wiki_resultados(texto_wiki(a))
        candidatos: list[tuple[dict, tuple]] = []
        if grades:
            wiki_par: dict[tuple, list] = defaultdict(list)
            for g in grades:
                # código sem nome na matriz: o nome vem da tabela do mesmo artigo, que usa os mesmos códigos
                cod_tab = {x["codigo"]: clubes.esd(x["nome"], a) for tb in wiki.get(a, []) for x in tb["times"]}
                cod = {k: clubes.esd(v, a) or cod_tab.get(k) or clubes.esd(k, a) for k, v in g["nomes"].items()}
                for (c1, c2), placares in g["jogos"].items():
                    if cod.get(c1) is None or cod.get(c2) is None:
                        raise SystemExit(f"{T}: clube da matriz da Wikipédia sem cadastro: {g['nomes'].get(c1, c1)} x "
                                         f"{g['nomes'].get(c2, c2)}")
                    wiki_par[(cod[c1], cod[c2])] += placares
            for (x1, x2), placares in list(wiki_par.items()):
                faltam = list((Counter(placares) - Counter((j["gm"], j["gv"]) for j in por_par.get((x1, x2), []))).elements())
                sobra_volta = len(por_par.get((x2, x1), [])) - len(wiki_par.get((x2, x1), []))
                for g1, g2 in faltam:
                    if sobra_volta <= 0:
                        break
                    r = next((j for j in por_par.get((x2, x1), []) if (j["gv"], j["gm"]) == (g1, g2)), None)
                    if r is not None:
                        inverter(por_par, r, "a matriz da Wikipédia traz o jogo com o outro mandante", ocorr[a])
                        sobra_volta -= 1
            total = sum(len(v) for v in wiki_par.values())
            for par, placares in sorted(wiki_par.items()):
                nossos = sorted((j["gm"], j["gv"]) for j in por_par.get(par, []))
                so_ogol, so_wiki = list((Counter(nossos) - Counter(placares)).elements()), list((Counter(placares) - Counter(nossos)).elements())
                if len(so_ogol) == 1 and len(so_wiki) == 1:
                    jogo = next(j for j in por_par[par] if (j["gm"], j["gv"]) == so_ogol[0])
                    candidatos.append((jogo, so_wiki[0]))
                if sorted(placares) != nossos:
                    dif_mz.append(f"{par[0]} x {par[1]}: ogol {', '.join(f'{x}-{y}' for x, y in nossos) or '—'}; Wikipédia "
                                  f"{', '.join(f'{x}-{y}' for x, y in sorted(placares))}")
            for d in dif_mz:
                ocorr[a].append(f"placar diferente na matriz da Wikipédia — {d}")
            if total != len(jogos):
                ocorr[a].append(f"matriz da Wikipédia com {total} placares (ogol {len(jogos)} jogos)")
        # ---- engsoccerdata e football-data (casados pelo par e pela data mais próxima)
        for fonte, dados, cm, cv in (("engsoccerdata", esd, "hgoal", "vgoal"), ("football-data", fd, "FTHG", "FTAG")):
            if a not in dados:
                continue
            usados = set()
            for m, v, d, x in dados[a]:
                nomes[m][f"{fonte}:{x['home' if fonte == 'engsoccerdata' else 'HomeTeam']}"].add(a)
                b = casar(por_par, usados, m, v, d)
                if b is None:   # o ogol traz o par invertido na mesma data, com o mesmo placar: corrige o mando
                    r = casar(por_par, usados, v, m, d, 3)
                    if r is not None and (r["gv"], r["gm"]) == (int(x[cm]), int(x[cv])):
                        inverter(por_par, r, f"o {fonte} traz {m} x {v} na mesma data", ocorr[a])
                        b = r
                if b is None:
                    ocorr[a].append(f"jogo do {fonte} sem par no ogol: {m} x {v} ({d})")
                    continue
                if fonte == "football-data":
                    b["fd"] = x
                if (int(x[cm]), int(x[cv])) != (b["gm"], b["gv"]) and not b.get("especial"):
                    ocorr[a].append(f"placar diferente no {fonte} — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, "
                                    f"{fonte} {x[cm]}-{x[cv]}")
            if len(dados[a]) != len(jogos):
                ocorr[a].append(f"{fonte} com {len(dados[a])} jogos (ogol {len(jogos)})")

        # ---- ESPN (entre eventos do mesmo par fica o de placar igual e com os gols fechando)
        es_ok = playoffs_espn = 0
        usados = set()
        for e in sorted(espn.get(a, []), key=lambda e: (abs(e["gm"] - e["gv"]), e["id"])):
            m, v = mapa_espn.get(e["mandante_id"], a), mapa_espn.get(e["visitante_id"], a)
            if m not in clubes_ano or v not in clubes_ano:
                playoffs_espn += 1   # play-off de rebaixamento contra clube da 2ª divisão: não é da liga
                continue
            b = casar(por_par, usados, m, v, e["data"], 3)
            if b is None:
                ocorr[a].append(f"jogo da ESPN sem par no ogol: {e['mandante']} {e['gm']}-{e['gv']} {e['visitante']} ({e['data']})")
                continue
            nomes[m][f"espn:{e['mandante']}"].add(a)
            b["espn"] = e
            es_ok += 1
            if (e["gm"], e["gv"]) != (b["gm"], b["gv"]) and not b.get("especial"):
                ocorr[a].append(f"placar diferente na ESPN — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, ESPN {e['gm']}-{e['gv']}")
        if playoffs_espn:
            ocorr[a].append(f"{playoffs_espn} jogos da ESPN com clube da 2ª divisão (play-off de rebaixamento): ficam de fora")
        if a in espn and es_ok != len(jogos):
            falta = [j for j in jogos if "espn" not in j]
            if falta:
                ocorr[a].append(f"ESPN com {es_ok} de {len(jogos)} jogos (ex. sem ESPN: {falta[0]['m']} x {falta[0]['v']}, "
                                f"{falta[0]['data']})")

        # ---- tabelas publicadas e conferência
        ref = calcular(jogos, pv)
        clubes_tab = sorted(ref)
        ajuste: dict[str, int] = {}
        w = max(wiki.get(a, []), key=lambda tb: len({clubes.esd(x["nome"], a) for x in tb["times"]} & set(clubes_tab)), default=None)
        if w:
            for x in w["times"]:
                c = clubes.esd(x["nome"], a)
                if c is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
                x["clube"] = c
                nomes[c][f"wikipedia:{x['nome']}"].add(a)
                if x["ajuste"]:
                    ajuste[c] = x["ajuste"]
            if w["pontos_vitoria"] != pv:
                ocorr[a].append(f"Wikipédia com {w['pontos_vitoria']} pontos por vitória (aqui {pv})")
        rs, url_rs = None, rsssf_url(a)
        if a in rs_hist:
            tb = rs_hist[a]
            for x in tb:
                x["clube"] = clubes.esd(x["nome"], a)
                if x["clube"] is None:
                    raise SystemExit(f"{T}: nome da tabela da RSSSF sem cadastro: {x['nome']}")
                nomes[x["clube"]][f"rsssf:{x['nome']}"].add(a)
            if len(tb) == len(clubes_tab) and {x["clube"] for x in tb} == set(clubes_tab):
                rs = tb
            elif tb:
                ocorr[a].append(f"tabela da RSSSF com outros clubes: {sorted({x['clube'] for x in tb} ^ set(clubes_tab), key=str)}")
        else:
            rs = tabela_rsssf(a, set(clubes_tab), Counter(c for j in jogos for c in (j["m"], j["v"])).most_common(1)[0][1])
        if rs:
            for x in rs:   # punição que só a RSSSF traz (ponto a mais é erro de digitação: fica só anotado)
                c = ref.get(x["clube"])
                if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                        and x["pontos"] < c[6] and x["clube"] not in ajuste:
                    ajuste[x["clube"]] = x["pontos"] - c[6]
                    ocorr[a].append(f"punição tirada da tabela da RSSSF: {x['clube']} {x['pontos'] - c[6]:+d} pontos")
        def erros(jogos_):
            """Linhas das tabelas publicadas (RSSSF e Wikipédia) que não fecham com os jogos."""
            calc = calcular(jogos_, pv)
            n_ = 0
            for linhas_ in ([dict(x, pontos=x["pontos"]) for x in rs] if rs else [],
                            [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                  pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in w["times"]] if w else []):
                for x in linhas_:
                    c = calc.get(x["clube"])
                    if c is None or [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] != c[:6]:
                        n_ += 1
            return n_
        if candidatos and (rs or w):
            atual = erros(jogos)
            for jogo, novo in candidatos:
                antigo = (jogo["gm"], jogo["gv"])
                jogo["gm"], jogo["gv"] = novo
                depois = erros(jogos)
                if depois < atual:
                    ocorr[a].append(f"placar corrigido pela matriz da Wikipédia: {jogo['m']} x {jogo['v']} ({jogo['data']}) de "
                                    f"{antigo[0]}-{antigo[1]} para {novo[0]}-{novo[1]} — com ele, as tabelas publicadas fecham "
                                    f"melhor ({atual} -> {depois} linhas que não fecham)")
                    jogo["corrigido"] = f"o ogol traz {antigo[0]}-{antigo[1]}; a matriz da Wikipédia e as tabelas publicadas, {novo[0]}-{novo[1]}"
                    atual = depois
                else:
                    jogo["gm"], jogo["gv"] = antigo
            # o ogol pode errar mais de um placar que só juntos fecham as tabelas (1989/90): combinações dos que sobraram
            restantes = [(j_, nv) for j_, nv in candidatos if not j_.get("corrigido")]
            if atual and len(restantes) <= 8:
                melhor = None
                for tam in range(2, min(4, len(restantes)) + 1):
                    for comb in combinations(restantes, tam):
                        antigos = [(j_["gm"], j_["gv"]) for j_, _ in comb]
                        for j_, nv in comb:
                            j_["gm"], j_["gv"] = nv
                        e_ = erros(jogos)
                        for (j_, _), an in zip(comb, antigos):
                            j_["gm"], j_["gv"] = an
                        if e_ < atual and (melhor is None or e_ < melhor[0]):
                            melhor = (e_, comb)
                    if melhor:
                        break
                if melhor:
                    for j_, nv in melhor[1]:
                        antigo = (j_["gm"], j_["gv"])
                        j_["gm"], j_["gv"] = nv
                        j_["corrigido"] = (f"o ogol traz {antigo[0]}-{antigo[1]}; a matriz da Wikipédia e as tabelas publicadas, "
                                           f"{nv[0]}-{nv[1]}")
                        ocorr[a].append(f"placar corrigido pela matriz da Wikipédia: {j_['m']} x {j_['v']} ({j_['data']}) de "
                                        f"{antigo[0]}-{antigo[1]} para {nv[0]}-{nv[1]} — junto com outros {len(melhor[1]) - 1}, "
                                        f"as tabelas publicadas fecham melhor ({atual} -> {melhor[0]} linhas que não fecham)")
                    atual = melhor[0]
            ref = calcular(jogos, pv)
        conferidas, divergentes, confere, erros_por_fonte = 0, 0, {}, {}
        publicadas = []
        if rs:
            publicadas.append(("RSSSF", url_rs, rs))
        if w:
            publicadas.append(("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                               [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                     pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in w["times"]]))
        if not publicadas:
            ocorr[a].append("sem tabela publicada legível (RSSSF e Wikipédia)")
        for fonte, url, linhas in publicadas:
            erro = []
            if sorted(x["clube"] for x in linhas) != clubes_tab:
                erro.append(f"clubes diferentes: {sorted(set(x['clube'] for x in linhas) ^ set(clubes_tab), key=str)}")
            for x in linhas:
                c = ref.get(x["clube"])
                if c is None:
                    continue
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = c[:6] + [c[6] + ajuste.get(x["clube"], 0)]
                if pub != meu:
                    erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": "Liga", "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"],
                    "empates": x["empates"], "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"],
                    "pontos": x["pontos"], "fonte": url})
            confere[fonte] = not erro
            erros_por_fonte[fonte] = [e for e in erro if " tabela [" in e]
            if erro:
                divergentes += 1
                for e in erro:
                    ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {e}")
            else:
                conferidas += 1


        erram = {f: {e.split(" tabela ")[0] for e in errs} for f, errs in erros_por_fonte.items() if errs}
        if len(confere) == 2 and not any(confere.values()) and len(erram) == 2 and not (erram["RSSSF"] & erram["Wikipédia"]):
            ocorr[a].append(f"as duas tabelas têm erros de digitação, em clubes diferentes (RSSSF: {', '.join(sorted(erram['RSSSF']))}; "
                            f"Wikipédia: {', '.join(sorted(erram['Wikipédia']))}): em cada clube, a outra tabela fecha com os jogos")
        if len(confere) == 2 and sum(confere.values()) == 1:
            certa, errada = [f for f, ok_ in confere.items() if ok_][0], [f for f, ok_ in confere.items() if not ok_][0]
            ocorr[a].append(f"a tabela da {errada} tem erro de digitação em alguma linha (gols ou V-E-D); a da {certa} fecha com "
                            f"os jogos")

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
            ordem = ordenar(ref, ajuste, "saldo", jogos, pv)
            fonte_ordem = "calculada"
        if rs and w and fonte_ordem.startswith("Wikipédia") and [x["clube"] for x in rs] != ordem:
            dif = [(r["clube"], c) for r, c in zip(rs, ordem) if r["clube"] != c]
            ocorr[a].append(f"ordem diferente entre RSSSF e Wikipédia em {len(dif)} posições (ex.: RSSSF {dif[0][0]}, Wikipédia "
                            f"{dif[0][1]}); fica a da Wikipédia")
        tentativas = {cr: ordenar(ref, ajuste, cr, jogos, pv) for cr in ("confronto", "confronto_geral", "confronto_fora", "saldo", "media")}
        if divisao:   # depois da divisão, os 6 do grupo de cima ficam à frente, mesmo com menos pontos
            cima_ofc = set(ordem[:6])
            tentativas = {cr: [c for c in o if c in cima_ofc] + [c for c in o if c not in cima_ofc] for cr, o in tentativas.items()}
        ok = [cr for cr, o in tentativas.items() if o == ordem]
        # a tabela que não fecha pode errar só nos gols de um clube e trazer a ordem certa: se a ordem escolhida não sai de
        # nenhum critério e a da outra tabela sai, fica a outra
        outra = ([x["clube"] for x in w["times"]], "Wikipédia (ordem oficial)") if fonte_ordem.startswith("RSSSF") and w else \
            ([x["clube"] for x in rs], "RSSSF (ordem oficial)") if fonte_ordem.startswith("Wikipédia") and rs else None
        if not ok and outra and not (fonte_ordem.startswith("Wikipédia") and confere.get("Wikipédia")) and any(o == outra[0] for o in tentativas.values()):
            ocorr[a].append(f"a ordem da {fonte_ordem.split(' ')[0]} não sai de nenhum critério de desempate e a da "
                            f"{outra[1].split(' ')[0]} sai: fica a da {outra[1].split(' ')[0]}")
            ordem, fonte_ordem = outra
            ok = [cr for cr, o in tentativas.items() if o == ordem]
        criterio = ok[0] if ok else min(tentativas, key=lambda cr: sum(x != y for x, y in zip(tentativas[cr], ordem)))
        if not ok:
            dif = [c for c, d in zip(ordem, tentativas[criterio]) if c != d]
            if a < 1921:
                ocorr[a].append("até 1920/21 não havia critério de desempate: clubes empatados em pontos dividiam a posição (o "
                                "título ia para jogo extra); a ordem entre eles é a da tabela publicada")
            elif a in INTERROMPIDAS:
                ocorr[a].append("a ordem oficial é pela média de pontos por jogo (temporada interrompida)")
            else:
                ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo ({criterio}) difere em "
                                f"{len(dif)} posições (ex.: {dif[:2]})")
        criterios[a] = (criterio, bool(ok))

        # rebaixados: quem não está na 1ª divisão na temporada seguinte (até 1920/21, reeleição: sem rebaixamento)
        prox = next((b for b in TEMPORADAS if b > a), None)
        prox_clubes = {j[k] for j in base[prox] for k in ("m", "v")} if prox is not None else prox_2026
        saem = {c for c in clubes_ano if c not in prox_clubes}
        if a in SEM_REBAIXAMENTO or a in INTERROMPIDAS and False:
            rebaixados = set()
            for c in sorted(saem):
                ocorr[a].append(f"{c} não está na temporada seguinte (não foi reeleito; ainda não havia rebaixamento)")
        else:
            rebaixados = {c for c in saem if (a, c) not in NAO_REBAIXADOS}
        for (b_, c), motivo in NAO_REBAIXADOS.items():
            if b_ == a:
                ocorr[a].append(f"{c} não está na temporada seguinte, mas não foi rebaixado: {motivo}")
        marca = rebaixados_wiki(a)
        if marca is not None and marca != rebaixados and a not in SEM_REBAIXAMENTO:
            ocorr[a].append(f"rebaixados: pela temporada seguinte {sorted(rebaixados)}; caixa da Wikipédia {sorted(marca)}")
        campeao, vice = ordem[0], ordem[1]
        dividido = TITULO_DIVIDIDO.get(a)
        if dividido:
            ocorr[a].append(f"título dividido entre {dividido[0]} e {dividido[1]}: empataram em pontos e no jogo de desempate (2-2); "
                            f"os dois ficam como campeões, na 1ª posição")
            campeao, vice = dividido[0], dividido[1]
        if camp_rs.get(a) and camp_rs[a] != campeao and not dividido:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {camp_rs[a]} (tabela: {campeao})")
        pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p = ref[c]
            campeao_c = c in (dividido or (campeao,))
            tab["classificacao_final"].append({
                "temporada": T, "posicao": 1 if campeao_c else pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_,
                "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + ajuste.get(c, 0),
                "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if campeao_c else "rebaixado" if c in rebaixados else None,
                "fonte": fonte_ordem,
                "observacao": ("título dividido (jogo de desempate 2-2)" if dividido and campeao_c else
                               "não foi reeleito para a temporada seguinte" if a in SEM_REBAIXAMENTO and c in saem else
                               (w and next((x["hth"] or x["nota"] for x in w["times"] if x["clube"] == c), None)) or None)})

        # ---- partidas, gols, cartões, estatísticas
        jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
            fuso = LONDRES
            hora = None
            if x and x.get("Time"):   # o football-data dá a hora do Reino Unido
                d = datetime.fromisoformat(f"{data_fd(x['Date'])}T{x['Time']}").replace(tzinfo=LONDRES).astimezone(fuso)
                hora = d.strftime("%H:%M")
            elif e:
                local = e["utc"].astimezone(fuso)
                if local.date().isoformat() == j["data"]:
                    hora = local.strftime("%H:%M")
            ids = [f"ogol:{o['id']}"] if o else []
            if e:
                ids.append(f"espn:{e['id']}")
            fontes = [j["fonte"]] + (["football-data"] if x and j["fonte"] != "football-data" else []) + (["ESPN"] if e else [])
            obs = None
            if j.get("especial"):
                obs = (f"vitória do {j[j['vencedor']]} dada fora de campo; o placar registrado ({j['campo']}) fica"
                       if j.get("vencedor") in ("m", "v") else
                       f"derrota para os dois clubes dada fora de campo; em campo, {j['campo']}" if j.get("vencedor") == "nenhum" else
                       f"resultado dado fora de campo; em campo, {j['campo']}" if j.get("campo") else "resultado dado fora de campo")
            elif j.get("invertido"):
                obs = f"mando corrigido: {j['invertido']}"
            elif j.get("corrigido"):
                obs = f"placar corrigido: {j['corrigido']}"
            elif j.get("rodada_inferida"):
                obs = "jogo da fase de grupos (depois da divisão); rodada pela ordem de jogos de cada clube"
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
                "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": "awd" if j.get("especial") else None,
                "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
                "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids),
                "gols_texto": None, "observacao": obs, "arbitro": (x or {}).get("Referee") or None})
            gols_ano += j["gm"] + j["gv"]
            if e and e["lances"] and not j.get("especial"):
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

        # ---- classificação rodada a rodada
        sem_rodada = [j for j in jogos if not j["rodada"]]
        if sem_rodada:
            ocorr[a].append(f"{len(sem_rodada)} jogos sem rodada no ogol (ex.: {sem_rodada[0]['m']} x {sem_rodada[0]['v']})")
        else:
            cima = set(ordem[:6]) if divisao else set()
            for r in sorted({j["rodada"] for j in jogos}):
                ate = [j for j in jogos if j["rodada"] <= r]
                parcial = calcular(ate, pv)
                ordem_r = ordenar(parcial, ajuste, criterio, ate, pv)
                if divisao and r > 33:   # depois da divisão em dois grupos, o grupo de cima fica nas 6 primeiras posições
                    ordem_r = [c for c in ordem_r if c in cima] + [c for c in ordem_r if c not in cima]
                for pos, c in enumerate(ordem_r, 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        fontes_ed = ["ogol"] + (["engsoccerdata"] if a in esd else []) + (["football-data"] if a in fd else []) \
            + (["ESPN"] if a in espn else []) + (["RSSSF"] if rs else []) + (["Wikipédia"] if w else [])
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        vezes = {2: "turno e returno", 3: "três turnos", 4: "quatro turnos"}.get(vezes_par, f"{vezes_par} turnos")
        formato = ("pontos corridos: 33 rodadas e depois divisão em dois grupos de 6 (5 rodadas)" if divisao
                   else f"pontos corridos ({vezes})")
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pv, "formato": formato,
                               "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(vice),
                               "fontes": " + ".join(fontes_ed),
                               "observacao": "; ".join(x for x in (
                                   f"título dividido: {dividido[0]} e {dividido[1]}" if dividido else "",
                                   f"temporada {INTERROMPIDAS[a]}" if a in INTERROMPIDAS else "",
                                   "sem rebaixamento: os últimos pediam reeleição à liga" if a in SEM_REBAIXAMENTO else "",
                                   f"punições: {pun}" if pun else "") if x) or None})
        crit_txt = {"confronto": "pontos, confronto direto, saldo de gols, gols pró",
                    "confronto_geral": "pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo de gols, gols pró",
                    "confronto_fora": "pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo e gols fora de "
                                      "casa no confronto direto, saldo de gols, gols pró",
                    "saldo": "pontos, saldo de gols, gols pró",
                    "media": "pontos, média de gols (goal average)"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Liga", "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        obs = [f"campeão {clubes.exibicao(campeao)} (RSSSF, lista de campeões: {camp_rs.get(a) or '—'})"]
        if divergentes:
            obs.append("divergências explicadas no relatório")
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": esperados,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autor_ano, "observacao": "; ".join(obs)})
        linhas_rel.append((T, " + ".join(fontes_ed), n, len(jogos), gols_ano, autor_ano, conferidas, divergentes,
                           clubes.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos, tabelas {conferidas} ok / {divergentes} div, gols {gols_ano} ({autor_ano} c/ autor), "
              f"critério {criterio}{'' if criterios[a][1] else ' (aprox.)'}, campeão {clubes.exibicao(campeao)}", flush=True)

    # ---- clubes
    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = [{"codigo": "SCO", "nome": "Escócia", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_espn, criterios)


def artilheiros(ocorr) -> list[dict]:
    """Artilheiro(s) de cada temporada pela lista da RSSSF (tabless/scottops.html: "1890/91  John Bell (Dumbarton)  20";
    empate marcado com "&" e o outro na linha seguinte, sem temporada)."""
    res, ano = [], None
    for l in texto_rsssf("scottops.html").replace("\t", "    ").split("\n"):
        m = re.match(r"^\s*(\d{4})/(\d{2,4})\s+(.*)$", l)
        if m:
            ano, resto = int(m.group(1)), m.group(3)
            if int(m.group(2)) % 100 == ano % 100:   # "1936/36": erro da RSSSF para 1935/36
                ano -= 1
        elif ano is not None and re.match(r"^\s+\S.*\(.*\)\s+\d+", l):
            resto = l.strip()
        else:
            if l.strip():
                ano = None
            continue
        x = re.match(r"^(.*?)\s*\(([^()]+)\)\s*(\d+)", resto)
        if not x or ano not in TEMPORADAS:
            continue
        nome, clube_txt, gols = x.group(1).strip(), x.group(2).strip(), int(x.group(3))
        # jogador que mudou de clube na temporada: "Kilmarnock 15/Rangers 17" -> o clube em que fez mais gols
        partes = re.findall(r"([^/\d]+?)\s*(\d+)", clube_txt)
        c = clubes.esd(max(partes, key=lambda p: int(p[1]))[0].strip() if partes else clube_txt, ano)
        res.append({"temporada": temporada(ano), "jogador": nome, "clube": clubes.exibicao(c) if c else None, "gols": gols,
                    "fonte": "RSSSF (tabless/scottops.html)" + (f"; gols por clube: {clube_txt}" if partes else "")})
        if c is None:
            ocorr[ano].append(f"artilheiro com clube sem cadastro: {nome} ({clube_txt})")
    for a in sorted(set(TEMPORADAS) - {int(x["temporada"][:4]) for x in res}):
        ocorr[a].append("artilheiro: a lista da RSSSF não traz esta temporada")
    return res


def relatorio(linhas, ocorr, tab, mapa_espn, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Escocês (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/sco-1/importar.py`. Pacote em `data/coleta/sco-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1890/91 a 2025/26: Scottish Football League e Division One (até 1974/75), Premier "
        "Division (1975/76-1997/98), Scottish Premier League (1998/99-2012/13) e Scottish Premiership. Sem 1939/40-1945/46 "
        "(guerra: o campeonato de 1939/40 parou na 5ª rodada e os seguintes foram ligas regionais não oficiais).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (ESPN), {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- ogol (zerozero): base dos jogos de todas as temporadas, com a rodada oficial; calendários guardados em "
        "`data/cache/ogol-sco-1/` para os escudos (com 2026/27, baixado só para saber quem caiu em 2025/26);",
        "- RSSSF: tabela final de 1890/91 a 1998/99 (scothist.html) e da página de cada temporada depois; lista de campeões e de "
        "artilheiros (com o clube);",
        "- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): conferência de placar de 1994/95 a 2024/25;",
        "- football-data.co.uk: de 1994/95 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;",
        "- ESPN (liga `sco.1`): hora, estádio, público, gols e cartões com minuto e jogador, nas temporadas que ela cobre;",
        "- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista oficial de rebaixados.", "",
        "**Regras:** o placar é o do ogol; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols "
        "pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). O mesmo par se enfrenta 2, "
        "3 ou 4 vezes por temporada: as outras fontes são casadas pelo par e pela data mais próxima. Desde 2000/01 a liga se "
        "divide em dois grupos de 6 depois da 33ª rodada; na classificação rodada a rodada, o grupo de cima fica nas 6 primeiras "
        "posições a partir da 34ª. Gols da ESPN só entram quando a soma bate com o placar. Hora local (Reino Unido). Rebaixado = "
        "clube que não está na 1ª divisão na temporada seguinte; até 1920/21 não havia rebaixamento (os últimos pediam reeleição "
        "à liga). 2 pontos por vitória até 1993/94, 3 a partir de 1994/95.", "",
        f"**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em "
        f"{cr['confronto']}, saldo de gols em {cr['saldo']}, média de gols em {cr['media']}); é ele que ordena a classificação "
        "rodada a rodada.", "",
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
        "- Cadastro em `coleta/comum-europa/clubes_sco.py` (serve para todas as divisões escocesas): nome de exibição como o "
        "clube é conhecido no Brasil, cidade e país (Escócia, `SCO`, em `paises.csv`). O Rangers é um clube só, também depois da "
        "liquidação da empresa em 2012, como na liga e na lista oficial de campeões.",
        f"- O ogol entra pelo código do clube (tabela `OGOL` do cadastro); a ESPN é casada por votação jogo a jogo (mesma data e "
        f"placar): {len(mapa_espn)} códigos.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.",
        "",
        "## O que não deu para coletar", "",
        "- **Autores dos gols e cartões antes da ESPN:** nenhuma fonte em lote traz.",
        "- **Público e estádio antes da ESPN:** nenhuma fonte em lote.",
        "- **Play-offs de rebaixamento (contra clubes da 2ª divisão) e jogos de desempate pelo título (1890/91, 1904/05):** "
        "ficam de fora.",
        "- **Ligas de guerra (1939/40-1945/46):** não oficiais; ficam de fora.",
        "- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
