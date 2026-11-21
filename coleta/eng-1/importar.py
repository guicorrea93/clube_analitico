"""Monta o pacote da 1ª divisão inglesa (eng-1), 1888/89 a 2024/25, e o relatório docs/coleta/eng-1.md.

Base dos jogos: engsoccerdata (2022/23 vem do football-data, que o engsoccerdata não tem). Cada jogo é casado pelo
par mandante x visitante, que é único na temporada (turno e returno), com:
  ogol           rodada oficial e conferência de placar (clubes casados pelo código do ogol, por votação);
  football-data  1993/94+: hora (2019/20+), árbitro e estatísticas por time (2000/01+); conferência de placar;
  ESPN           2001/02+: hora, estádio, público, gols e cartões com minuto (clubes casados pelo código da ESPN);
  RSSSF          até 2006/07: tabela final publicada e, quando há, a matriz de resultados (conferência jogo a jogo);
  Wikipédia      tabela final de todas as temporadas (ordem oficial, punições), campeões e artilheiros.

Regras: o placar é o da base; se uma tabela publicada não fecha com os jogos, a correção fica em CORRECOES, com o
motivo. Os gols da ESPN só entram quando a soma bate com o placar.

Uso: python coleta/eng-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_eng  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, nome_oficial, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from rsssf_eng import ler as ler_rsssf  # noqa: E402
from wiki_tabela import limpar, tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "eng-1.md"

# placar corrigido na base: (ano, mandante, visitante) -> (gols, gols, motivo). Nomes do engsoccerdata.
CORRECOES: dict[tuple, tuple] = {}

# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
EXPLICACOES = {
    1888: ["Wolverhampton x Everton (26/01/1889): o ogol traz 5-0 e a tabela da Wikipédia conta 51 gols pró do Wolverhampton e "
           "47 contra do Everton, como se fosse 5-0; o engsoccerdata, a matriz e a tabela da RSSSF e a matriz da própria Wikipédia "
           "trazem 4-0. Fica o 4-0 (três fontes, e a tabela da RSSSF fecha com ele)"],
    1900: ["a matriz da RSSSF traz Newcastle 4-0 Sheffield United; a tabela da RSSSF e a da Wikipédia fecham com o 3-0 da base: "
           "erro de digitação da matriz"],
    1903: ["a matriz da RSSSF troca os placares de Stoke x West Bromwich (5-0) e Stoke x Wolverhampton (5-1); as tabelas da RSSSF "
           "e da Wikipédia fecham com a base: erro da matriz"],
    1907: ["a RSSSF põe Arsenal e Blackburn empatados em 14º ('14='), com os mesmos pontos e a mesma média de gols; a Wikipédia "
           "ordena Arsenal 14º e Blackburn 15º. Fica a ordem da Wikipédia"],
    1956: ["Birmingham e Chelsea terminaram com 39 pontos e média de gols igual (69/69 e 73/73 = 1,000); a ordem oficial "
           "(RSSSF e Wikipédia) põe o Birmingham em 12º; o critério calculado aqui (gols pró) poria o Chelsea"],
    1909: ["a matriz da RSSSF traz Bolton 0-1 Sheffield Wednesday; as tabelas da RSSSF e da Wikipédia fecham com o 0-2 da base: "
           "erro da matriz"],
}

COMPETICAO = {
    "slug": "eng-1", "nome": "Campeonato Inglês", "nome_curto": "Inglês", "tipo": "liga", "nivel": 1,
    "pais": "ENG", "pais_nome": "Inglaterra", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Inglês", "menu_painel": "Inglaterra · 1ª divisão",
    "do_painel": "do Campeonato Inglês", "o_painel": "o Campeonato Inglês",
    "observacao": "1ª divisão inglesa desde a criação da Football League (1888/89): Football League (1888/89-1891/92), "
                  "First Division (1892/93-1991/92) e Premier League (1992/93 em diante). Sem 1915/16-1918/19 e "
                  "1939/40-1945/46 (guerras; 1939/40 foi anulada na 3ª rodada). Não inclui os test matches (1892/93-1897/98) "
                  "nem os play-offs de 1986/87-1987/88, que eram jogos contra clubes da 2ª divisão.",
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


# ------------------------------------------------------------------ fontes
def carregar_base() -> dict[int, list[dict]]:
    base = defaultdict(list)
    for x in ler_csv(DADOS / "engsoccerdata" / "england_tier1.csv"):
        base[int(x["Season"])].append({"data": x["Date"], "m": x["home"], "v": x["visitor"],
                                       "gm": int(x["hgoal"]), "gv": int(x["vgoal"]), "fonte": "engsoccerdata"})
    for x in ler_csv(DADOS / "football-data" / "E0_2223.csv"):   # o engsoccerdata não tem 2022/23
        base[2022].append({"data": data_fd(x["Date"]), "m": clubes_eng.esd(x["HomeTeam"]), "v": clubes_eng.esd(x["AwayTeam"]),
                           "gm": int(x["FTHG"]), "gv": int(x["FTAG"]), "fonte": "football-data"})
    return base


def carregar_fd() -> dict[int, dict]:
    res = {}
    for a in range(1993, 2025):
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        jogos = {}
        for x in ler_csv(DADOS / "football-data" / f"E0_{cod}.csv"):
            if not x.get("HomeTeam"):
                continue
            m, v = clubes_eng.esd(x["HomeTeam"]), clubes_eng.esd(x["AwayTeam"])
            assert m and v, (a, x["HomeTeam"], x["AwayTeam"])
            jogos[(m, v)] = x
        res[a] = jogos
    return res


def votar(base: dict[int, list[dict]], outra: dict[int, list[dict]], campo_m: str, campo_v: str) -> dict[str, str]:
    """Código do clube na outra fonte -> nome do engsoccerdata, por votação: jogo de mesma data (±1 dia) e mesmo placar,
    quando só um jogo da base serve."""
    votos: dict[str, Counter] = defaultdict(Counter)
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
    return {k: c.most_common(1)[0][0] for k, c in votos.items()}


def carregar_ogol() -> dict[int, list[dict]]:
    res = {}
    for a in TEMPORADAS:
        arq = DADOS / "ogol" / f"eng1_{a}.json"
        if arq.exists():
            res[a] = [dict(j, gm=j["gols_mandante"], gv=j["gols_visitante"]) for j in json.loads(arq.read_text(encoding="utf-8"))]
    return res


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for a in range(2001, 2025):
        arq = DADOS / "espn" / f"eng1_{a}.json"
        if not arq.exists():
            continue
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            local = utc.astimezone(LONDRES)
            jogos.append(dict(j, data=local.date().isoformat(), hora_local=local.strftime("%H:%M"),
                              gm=int(j["gols_mandante"]), gv=int(j["gols_visitante"])))
        res[a] = jogos
    return res


def carregar_wiki() -> dict[int, dict]:
    res = {}
    for a in TEMPORADAS:
        arq = DADOS / "wikipedia" / f"{wiki_titulo(a)}.wiki"
        if not arq.exists():
            continue
        tabs = wiki_tabelas(arq.read_text(encoding="utf-8"))
        if tabs:
            res[a] = tabs   # a página pode trazer as outras divisões; a da 1ª é escolhida pelos clubes (main)
    return res


def campeoes_wiki() -> dict[int, str]:
    """Campeão de cada temporada pela "List of English football champions"."""
    arq = DADOS / "wikipedia" / "List of English football champions.wiki"
    res = {}
    if not arq.exists():
        return res
    for linha in arq.read_text(encoding="utf-8").split("\n|-"):
        m = re.search(r"\[\[(\d{4})[–-](\d{2,4})[^\]]*\]\]", linha)
        if not m:
            continue
        cel = [c.strip() for c in re.split(r"\n\|\s*|\|\|", linha) if c.strip()]
        for c in cel[1:]:
            nome = limpar(c)
            if nome and clubes_eng.esd(re.sub(r"\s*\(.*\)$", "", nome).replace("[a]", "").strip()):
                res[int(m.group(1))] = clubes_eng.esd(re.sub(r"\s*\(.*\)$", "", nome).strip())
                break
    return res


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


def ordenar(t: dict[str, list[int]], ajuste: dict[str, int], a: int) -> list[str]:
    def k(c):
        j, v, e, d, gp, gc, p = t[c]
        p += ajuste.get(c, 0)
        if a <= 1975:   # média de gols (goal average) até 1975/76
            return (-p, -(gp / gc if gc else float("inf")), -gp)
        return (-p, -(gp - gc), -gp)
    return sorted(t, key=k)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    base = carregar_base()
    fd = carregar_fd()
    ogol = carregar_ogol()
    espn = carregar_espn()
    wiki = carregar_wiki()
    camp_wiki = campeoes_wiki()
    deducoes = {(int(x["Season"]), x["team"]): int(x["deduction"]) for x in ler_csv(DADOS / "engsoccerdata" / "deductions.csv")
                if x["tier"] == "1"}
    mapa_ogol = votar(base, ogol, "mandante_id", "visitante_id")
    mapa_espn = votar(base, {a: [dict(j, data=j["data"]) for j in js] for a, js in espn.items()}, "mandante_id", "visitante_id")

    nomes = defaultdict(lambda: defaultdict(set))   # clube esd -> "fonte:nome" -> anos
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel = []
    seq_rodada_faltando = []

    for a in TEMPORADAS:
        T = temporada(a)
        jogos = base[a]
        ocorr[a].extend(EXPLICACOES.get(a, []))
        pares = Counter((j["m"], j["v"]) for j in jogos)
        assert all(n == 1 for n in pares.values()), (a, [p for p, n in pares.items() if n > 1])
        por_par = {(j["m"], j["v"]): j for j in jogos}
        for j in jogos:
            if j["fonte"] == "engsoccerdata":   # 2022/23 vem do football-data, cujos nomes entram abaixo
                nomes[j["m"]][f"engsoccerdata:{j['m']}"].add(a)
            if (a, j["m"], j["v"]) in CORRECOES:
                gm, gv, motivo = CORRECOES[(a, j["m"], j["v"])]
                ocorr[a].append(f"placar corrigido: {j['m']} x {j['v']} de {j['gm']}-{j['gv']} para {gm}-{gv} — {motivo}")
                j["gm"], j["gv"] = gm, gv
        clubes = sorted({j["m"] for j in jogos} | {j["v"] for j in jogos})
        n = len(clubes)
        assert len(jogos) == n * (n - 1), (a, len(jogos), n)
        pv = 2 if a <= 1980 else 3

        # ---- ogol: rodada e conferência
        og_ok = 0
        testes = [o for o in ogol.get(a, []) if o["rodada"] is None and 1892 <= a <= 1897]
        if testes:
            ocorr[a].append(f"{len(testes)} test matches no calendário do ogol (decisão de acesso e rebaixamento contra clubes da "
                            f"2ª divisão; ex.: {testes[0]['mandante']} {testes[0]['resultado']} {testes[0]['visitante']}): ficam de fora")
        for o in ogol.get(a, []):
            if o in testes:
                continue
            m, v = mapa_ogol.get(o["mandante_id"]), mapa_ogol.get(o["visitante_id"])
            if m and v:
                nomes[m][f"ogol:{o['mandante']}"].add(a)
                nomes[v][f"ogol:{o['visitante']}"].add(a)
            b = por_par.get((m, v))
            if b is None:
                inv = por_par.get((v, m))
                ocorr[a].append(f"jogo do ogol sem par na base: {o['mandante']} {o['resultado']} {o['visitante']} ({o['data']})"
                                + (" — mando invertido" if inv else ""))
                continue
            if "ogol" in b:
                ocorr[a].append(f"jogo repetido no ogol: {o['mandante']} x {o['visitante']}")
                continue
            b["ogol"] = o
            og_ok += 1
            if o["gm"] is not None and (o["gm"], o["gv"]) != (b["gm"], b["gv"]):
                ocorr[a].append(f"placar diferente no ogol — {b['m']} x {b['v']} ({b['data']}): base {b['gm']}-{b['gv']}, "
                                f"ogol {o['gm']}-{o['gv']}")
        sem_rodada = [j for j in jogos if not (j.get("ogol") or {}).get("rodada")]
        if sem_rodada:
            ocorr[a].append(f"{len(sem_rodada)} jogos sem rodada do ogol (ex.: {sem_rodada[0]['m']} x {sem_rodada[0]['v']})")
            seq_rodada_faltando.append(a)
        datas_dif = [j for j in jogos if j.get("ogol") and j["ogol"]["data"] != j["data"]]
        if datas_dif:
            x = datas_dif[0]
            ocorr[a].append(f"data diferente no ogol em {len(datas_dif)} jogos (ex.: {x['m']} x {x['v']}: base {x['data']}, "
                            f"ogol {x['ogol']['data']}); fica a da base")

        # ---- football-data
        if a in fd:
            for (m, v), x in fd[a].items():
                nomes[m][f"football-data:{x['HomeTeam']}"].add(a)
                b = por_par.get((m, v))
                if b is None:
                    ocorr[a].append(f"jogo do football-data sem par na base: {m} x {v}")
                    continue
                b["fd"] = x
                if (int(x["FTHG"]), int(x["FTAG"])) != (b["gm"], b["gv"]):
                    ocorr[a].append(f"placar diferente no football-data — {m} x {v}: base {b['gm']}-{b['gv']}, "
                                    f"football-data {x['FTHG']}-{x['FTAG']}")
            if len(fd[a]) != len(jogos):
                ocorr[a].append(f"football-data com {len(fd[a])} jogos (base {len(jogos)})")

        # ---- ESPN (em 2009/10 a ESPN traz, para quase todo jogo, um 2º evento falso, com lances de outra liga:
        #      entre os eventos do mesmo par fica o de placar igual ao da base)
        es_ok = 0
        cand = defaultdict(list)
        for e in espn.get(a, []):
            m, v = mapa_espn.get(e["mandante_id"]), mapa_espn.get(e["visitante_id"])
            if (m, v) not in por_par:
                ocorr[a].append(f"jogo da ESPN sem par na base: {e['mandante']} {e['gm']}-{e['gv']} {e['visitante']} ({e['data']})")
                continue
            cand[(m, v)].append(e)
        descartados = 0
        for (m, v), es in cand.items():
            b = por_par[(m, v)]
            iguais = [e for e in es if (e["gm"], e["gv"]) == (b["gm"], b["gv"])]

            def fecha(e):   # gols da ESPN com clube e soma igual ao placar
                g = [l for l in e["lances"] if l["gol"]]
                return all(l["lado"] in ("home", "away") for l in g) and                     (sum(l["lado"] == "home" for l in g), sum(l["lado"] == "away" for l in g)) == (b["gm"], b["gv"])
            e = sorted(iguais or es, key=lambda e: (not fecha(e), int(e["id"])))[0]
            descartados += len(es) - 1
            nomes[m][f"espn:{e['mandante']}"].add(a)
            b["espn"] = e
            es_ok += 1
            if not iguais:
                ocorr[a].append(f"placar diferente na ESPN — {m} x {v} ({b['data']}): base {b['gm']}-{b['gv']}, ESPN {e['gm']}-{e['gv']}")
        if descartados:
            ocorr[a].append(f"{descartados} eventos repetidos da ESPN descartados (mesmo jogo com outro id e placar e lances de "
                            f"outra liga; fica o evento com o placar da base)")
        if a in espn and es_ok != len(jogos):
            falta = [j for j in jogos if "espn" not in j]
            ocorr[a].append(f"ESPN com {es_ok} de {len(jogos)} jogos (ex. sem ESPN: {falta[0]['m']} x {falta[0]['v']}, {falta[0]['data']})")

        # ---- RSSSF: matriz e tabela
        rs = None
        arq_rs = DADOS / "rsssf" / f"{a}-{str(a + 1)[-2:]}.html"
        if arq_rs.exists():
            rs = ler_rsssf(arq_rs)
            dif_m = 0
            for (nm, nv), (g1, g2) in rs["matriz"].items():
                m, v = clubes_eng.esd(nm), clubes_eng.esd(nv)
                b = por_par.get((m, v))
                if b is None:
                    ocorr[a].append(f"matriz da RSSSF com jogo sem par na base: {nm} x {nv}")
                elif (g1, g2) != (b["gm"], b["gv"]):
                    dif_m += 1
                    ocorr[a].append(f"placar diferente na matriz da RSSSF — {m} x {v}: base {b['gm']}-{b['gv']}, RSSSF {g1}-{g2}")
            if rs["matriz"] and len(rs["matriz"]) != len(jogos):
                ocorr[a].append(f"matriz da RSSSF com {len(rs['matriz'])} jogos (base {len(jogos)})")

        # ---- tabelas publicadas e conferência
        calc = calcular(jogos, pv)
        ajuste: dict[str, int] = {}
        w = max(wiki.get(a, []), key=lambda tb: len({clubes_eng.esd(x["nome"]) for x in tb["times"]} & set(clubes)), default=None)
        if w and len({clubes_eng.esd(x["nome"]) for x in w["times"]} & set(clubes)) < n // 2:
            w = None
        if w:
            for x in w["times"]:
                c = clubes_eng.esd(x["nome"])
                if c is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
                x["clube"] = c
                if x["ajuste"]:
                    ajuste[c] = x["ajuste"]
            if w["pontos_vitoria"] != pv:
                ocorr[a].append(f"Wikipédia com {w['pontos_vitoria']} pontos por vitória (aqui {pv})")
        for (ano, time_), ded in deducoes.items():
            if ano == a and ajuste.get(time_) != -ded:
                if w:
                    ocorr[a].append(f"punição no engsoccerdata: {time_} -{ded}; Wikipédia: {ajuste.get(time_)}")
                ajuste.setdefault(time_, -ded)
        conferidas, divergentes, fontes_tab = 0, 0, []
        publicadas = []
        if rs:
            publicadas.append(("RSSSF", f"https://www.rsssf.org/engpaul/FLA/{a}-{str(a + 1)[-2:]}.html",
                               [dict(x, clube=clubes_eng.esd(x["nome"].title() if x["maiusculas"] else x["nome"])) for x in rs["tabela"]]))
        if w:
            publicadas.append(("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                               [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                     pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in w["times"]]))
        for fonte, url, linhas in publicadas:
            erro = []
            if sorted(x["clube"] for x in linhas) != clubes:
                erro.append(f"clubes diferentes: {sorted(set(x['clube'] for x in linhas) ^ set(clubes))}")
            for x in linhas:
                c = calc.get(x["clube"])
                if c is None:
                    continue
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = c[:6] + [c[6] + ajuste.get(x["clube"], 0)]
                if pub != meu:
                    erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": "Liga", "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes_eng.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"],
                    "empates": x["empates"], "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"],
                    "pontos": x["pontos"], "fonte": url})
            fontes_tab.append(fonte)
            if erro:
                divergentes += 1
                for e in erro:
                    ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {e}")
            else:
                conferidas += 1
        # ordem oficial: a da Wikipédia; sem ela, a da RSSSF; sem nenhuma, calculada
        if w:
            ordem = [x["clube"] for x in w["times"]]
            fonte_ordem = "Wikipédia (ordem oficial)"
        elif rs:
            ordem = [clubes_eng.esd(x["nome"].title() if x["maiusculas"] else x["nome"]) for x in rs["tabela"]]
            fonte_ordem = "RSSSF (ordem oficial)"
        else:
            ordem = ordenar(calc, ajuste, a)
            fonte_ordem = "calculada"
            ocorr[a].append("sem tabela publicada: ordem calculada")
        if rs and w and [clubes_eng.esd(x["nome"].title() if x["maiusculas"] else x["nome"]) for x in rs["tabela"]] != ordem:
            ocorr[a].append("ordem da tabela diferente entre RSSSF e Wikipédia; fica a da Wikipédia")
        calc_ordem = ordenar(calc, ajuste, a)
        if calc_ordem != ordem:
            dif = [c for c, d in zip(ordem, calc_ordem) if c != d]
            ocorr[a].append(f"a ordem oficial não é a do critério calculado em {len(dif)} posições (ex.: {dif[:2]})")

        # rebaixados: quem não está na 1ª divisão no ano seguinte (2024/25: marca da Wikipédia)
        prox = next((b for b in TEMPORADAS if b > a), None)
        if prox is not None:
            prox_clubes = {j["m"] for j in base[prox]}
            rebaixados = {c for c in clubes if c not in prox_clubes}
        elif not w:
            raise SystemExit(f"{T}: sem a tabela da Wikipédia para marcar os rebaixados")
        else:
            textos = {k[5:]: limpar(v) for k, v in w["params"].items() if k.startswith("text_")}
            rebaixados = {x["clube"] for x in w["times"] if "relegat" in textos.get(x["resultado"], "").lower()}
        campeao, vice = ordem[0], ordem[1]
        if camp_wiki.get(a) and camp_wiki[a] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da Wikipédia: {camp_wiki[a]} (tabela: {campeao})")
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p = calc[c]
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes_eng.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + ajuste.get(c, 0), "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None, "fonte": fonte_ordem,
                "observacao": (w and next((x["hth"] or x["nota"] for x in w["times"] if x["clube"] == c), None)) or None})

        # ---- partidas, gols, cartões, estatísticas
        jogos.sort(key=lambda j: (j["data"], ((j.get("ogol") or {}).get("rodada") or 0), j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
            hora = None
            if x and x.get("Time"):
                hora = x["Time"]
            elif e and e["data"] == j["data"]:
                hora = e["hora_local"]
            ids = [f"ogol:{o['id']}"] if o else []
            if e:
                ids.append(f"espn:{e['id']}")
            fontes = [j["fonte"]] + (["ogol"] if o else []) + (["football-data"] if x else []) + (["ESPN"] if e else [])
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": "Liga", "grupo": None, "rodada": (o or {}).get("rodada"), "data": j["data"],
                "hora": hora, "mandante": clubes_eng.exibicao(j["m"]), "visitante": clubes_eng.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": None, "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
                "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids),
                "gols_texto": None, "observacao": None, "arbitro": (x or {}).get("Referee") or None})
            gols_ano += j["gm"] + j["gv"]
            if e and e["lances"]:
                gl = [l for l in e["lances"] if l["gol"]]
                lado = {"home": j["m"], "away": j["v"]}
                if all(l["lado"] in lado for l in gl) and                         (sum(l["lado"] == "home" for l in gl), sum(l["lado"] == "away" for l in gl)) == (j["gm"], j["gv"]):
                    for l in gl:
                        mi, ac = minuto(l["minuto"])
                        tab["gols"].append({"partida_id": pid, "clube": clubes_eng.exibicao(lado[l["lado"]]),
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
                        tab["cartoes"].append({"partida_id": pid, "clube": clubes_eng.exibicao(lado[l["lado"]]),
                                               "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                               "cor": "vermelho" if l["vermelho"] else "amarelo", "fonte": "ESPN"})
            if x and x.get("HS"):
                for c, s in ((j["m"], "H"), (j["v"], "A")):
                    def num(k):
                        v_ = x.get(k)
                        return int(float(v_)) if v_ not in (None, "") else None
                    tab["estatisticas"].append({"partida_id": pid, "clube": clubes_eng.exibicao(c), "chutes": num(f"{s}S"),
                                                "chutes_alvo": num(f"{s}ST"), "faltas": num(f"{s}F"), "escanteios": num(f"{s}C"),
                                                "amarelos": num(f"{s}Y"), "vermelhos": num(f"{s}R"), "fonte": "football-data.co.uk"})

        # ---- classificação rodada a rodada (pela rodada do ogol)
        if not sem_rodada:
            rodadas = sorted({j["ogol"]["rodada"] for j in jogos})
            n_reb = len(rebaixados)
            for r in rodadas:
                parcial = calcular([j for j in jogos if j["ogol"]["rodada"] <= r], pv)
                for pos, c in enumerate(ordenar(parcial, ajuste, a), 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes_eng.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos > n - n_reb else "meio"})

        fontes_ed = ["engsoccerdata" if a != 2022 else "football-data", "ogol"] + (["football-data"] if a in fd and a != 2022 else []) \
            + (["ESPN"] if a in espn else []) + (["RSSSF"] if rs else []) + (["Wikipédia"] if w else [])
        pun = "; ".join(f"{clubes_eng.exibicao(c)} {v:+d} pontos" for c, v in ajuste.items())
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pv, "formato": "pontos corridos (turno e returno)",
                               "campeao": clubes_eng.exibicao(campeao), "vice": clubes_eng.exibicao(vice),
                               "fontes": " + ".join(fontes_ed), "observacao": f"punições: {pun}" if pun else None})
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Liga", "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos",
                             "criterio": "pontos, média de gols (goal average)" if a <= 1975 else "pontos, saldo de gols, gols pró"})
        obs = [f"campeão {clubes_eng.exibicao(campeao)} (Wikipédia, lista de campeões: "
               f"{clubes_eng.exibicao(camp_wiki[a]) if a in camp_wiki else '—'})"]
        if divergentes:
            obs.append("divergências explicadas no relatório")
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": n * (n - 1), "tabelas_conferidas": conferidas,
                                   "tabelas_divergentes": divergentes, "gols": gols_ano, "gols_com_autor": autor_ano,
                                   "observacao": "; ".join(obs)})
        linhas_rel.append((T, " + ".join(fontes_ed), n, len(jogos), og_ok, gols_ano, autor_ano, conferidas, divergentes,
                           clubes_eng.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos, ogol {og_ok}, tabelas {conferidas} ok / {divergentes} div, gols {gols_ano} ({autor_ano} c/ autor), "
              f"campeão {clubes_eng.exibicao(campeao)}", flush=True)

    # ---- clubes
    for c, (exib, cidade, pais) in sorted(clubes_eng.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": exib, "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = [{"codigo": "WAL", "nome": "País de Gales", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros()
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_ogol, mapa_espn)


def artilheiros() -> list[dict]:
    """Artilheiro(s) de cada temporada pela "List of English football first tier top scorers" (Wikipédia).
    Linhas: temporada | jogador | nacionalidade | clube | gols; empate na artilharia vem com rowspan na temporada."""
    arq = DADOS / "wikipedia" / "List of English football first tier top scorers.wiki"
    txt = arq.read_text(encoding="utf-8")
    txt = txt[txt.index('{| class="wikitable sortable"'):]
    txt = txt[:txt.index("\n|}")]
    res, ano = [], None
    for bloco in txt.split("\n|-")[1:]:
        cel = [c for c in re.split(r"\n\|\s*|\s*\|\|\s*", "\n" + bloco.strip()) if c.strip()]
        # tira atributos de célula ("style=...|", "data-sort-value=...|", "rowspan=2|")
        cel = [re.sub(r'^\s*(?:(?:style|data-sort-value|rowspan|align)\s*=\s*"[^"]*"\s*|rowspan\s*=\s*\d+\s*)+\|\s*', "", c) for c in cel]
        m = re.match(r"^\[\[[^|\]]*\|(\d{4})[–-]\d{2,4}\]\]", cel[0].strip())
        if m:
            ano = int(m.group(1)); cel = cel[1:]
        if ano not in TEMPORADAS or len(cel) < 3:
            continue
        jogador = re.sub(r"\s*\(\d+\)$", "", limpar(cel[0])).strip()
        if len(cel) >= 4:   # empate na artilharia: as linhas seguintes herdam os gols (rowspan)
            gols = int(re.match(r"\d+", limpar(re.sub(r"\{\{efn.*", "", cel[3]))).group())
        # um clube ("[[Arsenal F.C.|Arsenal]]") ou vários ("{{ubl|[[Crystal Palace F.C.|...]]|[[Arsenal F.C.|...]]}}"):
        # fica o último, com os gols da temporada inteira
        clubes = [x for x in re.findall(r"\[\[([^|\]]+)(?:\|[^\]]*)?\]\]", cel[2])]
        c = clubes_eng.esd(re.sub(r"\s*(?:F\.C\.|A\.F\.C\.)$", "", clubes[-1]).strip()) if clubes else None
        antes = [clubes_eng.esd(re.sub(r"\s*(?:F\.C\.|A\.F\.C\.)$", "", x).strip()) for x in clubes[:-1]]
        res.append({"temporada": temporada(ano), "jogador": jogador, "clube": clubes_eng.exibicao(c) if c else None, "gols": gols,
                    "fonte": "Wikipédia (List of English football first tier top scorers)"
                             + (f"; gols somados com {', '.join(clubes_eng.exibicao(x) for x in antes)}" if antes else "")})
    return res


def relatorio(linhas, ocorr, tab, mapa_ogol, mapa_espn) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    out = [
        "# Campeonato Inglês (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/eng-1/importar.py`. Pacote em `data/coleta/eng-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1888/89 a 2024/25: Football League (1888/89-1891/92), First Division (1892/93-1991/92), "
        "FA Premier League (1992/93-2006/07) e Premier League (2007/08 em diante). Sem liga em 1915/16-1918/19 e 1939/40-1945/46 "
        "(guerras; a temporada 1939/40 parou na 3ª rodada e foi anulada).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (ESPN), {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1888/89-2024/25, menos 2022/23;",
        "- football-data.co.uk: base de 2022/23; de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time "
        "(chutes, faltas, escanteios, cartões; 2000/01+);",
        "- ogol: rodada oficial de cada jogo e conferência de placar; calendários guardados em `data/cache/ogol-eng-1/` para os escudos;",
        "- ESPN (liga `eng.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;",
        "- RSSSF (engpaul/FLA, Paul Felton e Barry Spencer): tabela final publicada até 2006/07 e matriz de resultados (1888/89-1938/39, "
        "menos 1925/26) — conferência jogo a jogo;",
        "- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições), lista de campeões e lista de artilheiros.", "",
        "**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols "
        "pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando "
        "a soma bate com o placar. Hora local de Londres. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.", "",
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
        "- Cadastro em `coleta/comum-europa/clubes_eng.py` (serve para todas as divisões inglesas): nome de exibição como o clube é "
        "conhecido no Brasil (\"Tottenham\", \"West Ham\", \"Wolverhampton\", \"QPR\"), cidade e país. Cardiff e Swansea são do País "
        "de Gales (`WAL`, em `paises.csv`).",
        f"- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): {len(mapa_ogol)} códigos do "
        f"ogol e {len(mapa_espn)} da ESPN.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv` (ex.: `ogol:Newton Heath`).",
        "- \"Accrington\" é o Accrington FC original (1878-1896), não o Accrington Stanley; \"Wimbledon\" é o Wimbledon FC (1889-2004).",
        "",
        "## O que não deu para coletar", "",
        "- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz. O ogol tem a ficha de muitos jogos, mas "
        "seriam uns 40 mil pedidos; fica como próximo passo, se aprovado.",
        "- **Público e estádio antes de 2001/02:** idem.",
        "- **Test matches (1892/93-1897/98) e play-offs (1986/87-1987/88):** jogos entre clubes da 1ª e da 2ª divisão, que "
        "decidiam o rebaixamento; ficam de fora (entram quando a 2ª divisão for coletada).",
        "- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
