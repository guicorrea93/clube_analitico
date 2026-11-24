"""Monta o pacote do Campeonato Sul-Coreano (kor-1) em data/coleta/kor-1/pacote/ e o relatório docs/coleta/kor-1.md.

- Jogos: portal de dados oficial da K League (portal.kleague.com): a lista de jogos de cada ano (calendário até 2012; de
  2013 em diante a lista do site oficial, com fase e rodada) e o boletim de cada jogo (data, hora, estádio, público,
  árbitro, autores dos gols com minuto, pênalti e gol contra, cartões, disputa de pênaltis). Só a 1ª divisão
  (competicoes.py): a liga, com os playoffs e as finais do título; fora a copa da liga e a repescagem contra a 2ª divisão.
- Placar: o total do boletim não conta o gol contra (em nenhuma época); o placar é a soma dos gols do boletim. Quando a
  soma e o total (com os gols contra) não batem, decide a outra fonte (site oficial de 2013 em diante, RSSSF, ogol).
  Sem outra fonte (1997, 2011, 2012), fica o que faz a tabela da RSSSF fechar.
- Fases pela ordem dos jogos (edicoes.py); de 2012 em diante a liga com a divisão em grupos fica numa fase só (como o
  Escocês), com a rodada oficial.
- Classificação: de 2003 em diante a oficial da K League (baixar_tabelas.py; conta o playoff nos jogos, mas os pontos só
  da liga); antes, a soma dos jogos com o campeão e o vice da decisão em cima.
- Casos especiais com prova em explicacoes.py: W.O. (1987 e 2012), gol que falta no boletim (1990), empate nos pênaltis
  decidido no sorteio (1998).
- Conferência: as tabelas da RSSSF (temporada regular, 1983-2009 na skorhist.html; 2010 em diante nas páginas de cada
  ano), a tabela oficial (2003 em diante), os placares da RSSSF e do ogol (2008 em diante), o campeão e o vice e o
  artilheiro da Wikipédia em inglês.

Uso: python coleta/kor-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import ler_oficial  # noqa: E402
import ler_portal  # noqa: E402
import ler_rsssf  # noqa: E402
from campeoes_wiki import artilheiros, podio  # noqa: E402
from clubes_kor import CLUBES, clube  # noqa: E402
from competicoes import eh_primeira  # noqa: E402
from edicoes import ANOS, FASES, nome_oficial, pontos  # noqa: E402
from explicacoes import AWD, GOL_FALTANDO, OBS_CLASSIFICACAO, SORTEIO, TABELA_RSSSF, WO  # noqa: E402
from nomes_kor import _palavra, nome as nome_jog, romanizar  # noqa: E402

RAIZ = AQUI.parent.parent
DADOS = RAIZ / "data" / "coleta" / "kor-1"
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "kor-1.md"
FONTE = "K League (portal oficial)"
GRUPO_SPLIT = {"파이널A": "A", "파이널B": "B"}
ORDEM_MM = {"Final": 4, "Semifinal": 3, "Segunda fase": 2, "Primeira fase": 1}

# estrangeiros sem nome em inglês nem na RSSSF: (nome romanizado, hangul) -> anos
APROXIMADOS: dict[tuple, set] = defaultdict(set)

# nomes dos clubes em cada fonte: código -> fonte -> nome -> anos
NOMES: dict[str, dict[str, dict[str, set]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))


def faixa(anos: set) -> str:
    a = sorted(anos)
    return str(a[0]) if a[0] == a[-1] else f"{a[0]}-{a[-1]}"


def dia(s: str, d: int) -> str:
    return (date.fromisoformat(s) + timedelta(days=d)).isoformat()


# ----------------------------------------------------------------------------------------------------- estádios
ESTADIO_INTEIRO = {"동대문": "Dongdaemun Stadium", "강릉하이원아레나": "Gangneung Hi One Arena", "대구iM뱅크PARK": "Daegu iM Bank Park",
                   "포항 스틸야드": "Pohang Steelyard", "효창": "Hyochang Stadium", "잠실 올림픽": "Seoul Olympic Stadium",
                   "부산 아시아드": "Busan Asiad Stadium", "대구 스타디움": "Daegu Stadium", "울산 문수": "Ulsan Munsu Football Stadium",
                   "창원 축구센터": "Changwon Football Center", "춘천 송암": "Chuncheon Songam Stadium", "부산 구덕": "Busan Gudeok Stadium",
                   "광주 무등": "Gwangju Mudeung Stadium", "순천 팔마": "Suncheon Palma Stadium", "영광 스포티움": "Yeonggwang Sportium"}
TIPO = [("월드컵", "World Cup Stadium"), ("종합", "Sports Complex"), ("전용", "Football Stadium"), ("공설", "Public Stadium"),
        ("시민", "Civic Stadium")]


def estadio(s: str | None) -> str | None:
    if not s:
        return None
    s = re.sub(r"\s+", " ", s.strip())
    if s in ESTADIO_INTEIRO:
        return ESTADIO_INTEIRO[s]
    tipo = "Stadium"
    for k, v in TIPO:
        if s.endswith(k):
            s, tipo = s[: -len(k)].strip(), v
            break
    partes = [_palavra(p).capitalize() for p in s.split()]
    return " ".join(partes + [tipo])


# ----------------------------------------------------------------------------------------------------- jogos do portal
def lista(ano: int) -> list[dict]:
    js = [j for j in json.loads((DADOS / "portal" / f"calendario_{ano}.json").read_text(encoding="utf-8")) if eh_primeira(j)]
    return sorted(js, key=lambda j: (int(j["meet_seq"]), int(j["game_id"])))


def fases(ano: int, js: list[dict]) -> list[str]:
    if ano >= 2012 and ano not in FASES or ano >= 2013:
        return ["Liga"] * len(js)
    if ano not in FASES:
        return ["Liga"] * len(js)
    saida = []
    for nome, n in FASES[ano]:
        saida += [nome] * (len(js) - len(saida) if n is None else n)
    assert len(saida) == len(js), (ano, len(saida), len(js))
    return saida


def minuto(m: int | None, meio: int, acr: int | None) -> tuple[int | None, int | None]:
    """Minuto e acréscimo no formato do pacote (90+2 -> 90, 2)."""
    if m is None:
        return None, None
    limite = {1: 45, 2: 90, 3: 105, 4: 120}.get(meio, 120)
    if acr:
        return limite, acr
    if m > limite:
        return limite, m - limite
    return m, None


def ler_jogo(ano: int, j: dict) -> dict:
    b = ler_portal.boletim(j["ano"], j["meet_seq"], j["game_id"])
    m, v = b["mandante_id"], b["visitante_id"]
    clube(m), clube(v)
    chave = f"{j['ano']}_{j['meet_seq']}_{j['game_id']}"
    if chave in GOL_FALTANDO:
        for lado, h, meio, mi, acr, tipo in GOL_FALTANDO[chave][0]:
            b["gols"].append({"lado": lado, "jogador": h, "numero": None, "minuto": ler_portal.BASE_MIN[meio] + mi + (acr or 0),
                              "acrescimo": acr, "meio": meio, "tipo": tipo, "obs": "", "player_id": None})
        b["gols"].sort(key=lambda g: (g["meio"], g["minuto"] or 0))
    em =sum(1 for g in b["gols"] if g["lado"] == "m")
    ev = sum(1 for g in b["gols"] if g["lado"] == "v")
    om = sum(1 for g in b["gols"] if g["lado"] == "m" and g["tipo"] == "contra")
    ov = sum(1 for g in b["gols"] if g["lado"] == "v" and g["tipo"] == "contra")
    tot = ((b["gm"] or 0) + om, (b["gv"] or 0) + ov)
    return {"ano": ano, "meet": j["meet_seq"], "game": j["game_id"], "m": m, "v": v, "eventos": (em, ev), "total": tot,
            "boletim": b, "rodada": j.get("rodada"), "fase_oficial": j.get("fase_oficial")}


# ----------------------------------------------------------------------------------------------------- fontes de conferência
def casar_nomes(externos: list[dict], por_data: dict) -> dict[str, str]:
    """Liga os nomes de uma fonte aos códigos do portal pelos jogos do mesmo dia com o mesmo placar."""
    votos = defaultdict(Counter)
    for e in externos:
        if not e.get("data"):
            continue
        for d in (0, -1, 1):
            cands = [x for x in por_data.get(dia(e["data"], d), []) if x["placar"] == (e["gm"], e["gv"])]
            if len(cands) == 1:
                votos[e["mandante"]][cands[0]["m"]] += 1
                votos[e["visitante"]][cands[0]["v"]] += 1
                break
    saida = {}
    for n, c in votos.items():   # as páginas da RSSSF têm outras ligas (N-League, K3): só liga o nome com votos firmes
        (cod, k), = c.most_common(1)
        if k >= 3 and k >= 0.6 * sum(c.values()):
            saida[n] = cod
    return saida


def ler_ogol() -> list[dict]:
    saida = []
    for arq in sorted((DADOS / "ogol").glob("*.json")):
        for o in json.loads(arq.read_text(encoding="utf-8")):
            if o.get("gols_mandante") is None:
                continue
            saida.append({"ano": int(arq.stem), "data": o["data"], "mandante": o["mandante"], "visitante": o["visitante"],
                          "gm": o["gols_mandante"], "gv": o["gols_visitante"], "id": o["id"]})
    return saida


# ----------------------------------------------------------------------------------------------------- tabela
def tabela(ano: int, jogos: list[dict]) -> dict[str, dict]:
    t = defaultdict(lambda: {"jogos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "gols_pro": 0, "gols_contra": 0, "pontos": 0})
    for j in jogos:
        if j.get("wo") and j["gm"] is None:
            for c in (j["mandante"], j["visitante"]):
                t[c]["jogos"] += 1
                t[c]["vitorias" if c == j["wo"] else "derrotas"] += 1
                t[c]["pontos"] += pontos(ano, 1, 0) if c == j["wo"] else 0
            continue
        for c, gp, gc, pp, pc in ((j["mandante"], j["gm"], j["gv"], j["pm"], j["pv"]), (j["visitante"], j["gv"], j["gm"], j["pv"], j["pm"])):
            if j.get("sorteio"):
                pp, pc = (1, 0) if c == j["sorteio"] else (0, 1)
            x = t[c]
            x["jogos"] += 1
            x["gols_pro"] += gp
            x["gols_contra"] += gc
            ganhou = gp > gc or (gp == gc and pp is not None and pp > pc)
            perdeu = gp < gc or (gp == gc and pp is not None and pp < pc)
            x["vitorias" if ganhou else "derrotas" if perdeu else "empates"] += 1
            x["pontos"] += pontos(ano, gp, gc, j["prorrogacao"], pp, pc)
    return t


def ordem(ano: int, t: dict, ajuste: dict) -> list[str]:
    def chave(c):
        x = t[c]
        pts = x["pontos"] + ajuste.get(c, 0)
        sg = x["gols_pro"] - x["gols_contra"]
        if ano >= 2016:
            return (-pts, -x["gols_pro"], -sg, -x["vitorias"], c)
        return (-pts, -sg, -x["gols_pro"], c)
    return sorted(t, key=chave)


# ----------------------------------------------------------------------------------------------------- uma edição
def edicao(ano: int, nomes_en: dict, ids_por_nome: dict, rs_map: dict, og_map: dict, rs_jogos: dict, og_jogos: dict,
           rs_nome: dict) -> dict:
    js = lista(ano)
    fs = fases(ano, js)
    brutos = [ler_jogo(ano, j) for j in js]
    jogos, difs_placar, gols_dif, cart_staff = [], [], [], 0
    # placares de fora, por (mandante, visitante, data)
    externos = {}
    for fonte, lst, mapa in (("RSSSF", rs_jogos.get(ano, []), rs_map), ("ogol", og_jogos.get(ano, []), og_map)):
        for e in lst:
            mm, vv = mapa.get(e["mandante"]), mapa.get(e["visitante"])
            if mm and vv and e.get("data"):
                externos.setdefault(fonte, {})[(mm, vv, e["data"])] = (e["gm"], e["gv"])
    conf = {"RSSSF": [0, []], "ogol": [0, []]}
    for x, fase in zip(brutos, fs):
        b = x["boletim"]
        of = ler_oficial.jogo(x["ano"], x["meet"], x["game"]) if ano >= 2013 else None
        ev, tot = x["eventos"], x["total"]
        ext = {}
        for fonte, d in externos.items():
            for dd in (0, -1, 1):
                k = (x["m"], x["v"], dia(b["data"], dd))
                if k in d:
                    ext[fonte] = d[k]
                    break
        obs = []
        completo = True
        alternativa = None
        chave = f"{x['ano']}_{x['meet']}_{x['game']}"
        if chave in WO:
            w = WO[chave]
            venc = clube(x[w["vencedor"]])
            jogos.append({"mandante": clube(x["m"]), "visitante": clube(x["v"]), "gm": w.get("gm_of"), "gv": w.get("gv_of"),
                          "pm": None, "pv": None, "wo": venc, "prorrogacao": False, "fase": fase,
                          "grupo_split": GRUPO_SPLIT.get(x["fase_oficial"] or ""), "rodada": x["rodada"], "data": b["data"],
                          "hora": b["hora"], "estadio": estadio(b["estadio"]), "publico": b["publico"] or None, "arbitro": None,
                          "fonte_id": chave, "gols": [], "cartoes": [], "obs": [f"vitória do {venc} por W.O.; {w['motivo']}"],
                          "m_cod": x["m"], "v_cod": x["v"]})
            continue
        if chave in GOL_FALTANDO:
            obs.append(GOL_FALTANDO[chave][1])
        if chave in AWD:
            placar = (AWD[chave]["gm_of"], AWD[chave]["gv_of"])
            completo = False
            obs.append(f"decidido fora de campo ({AWD[chave]['campo']} em campo): {AWD[chave]['motivo']}")
        elif of is not None and of["gm"] is not None:
            placar = (of["gm"], of["gv"])
            if ev != placar:
                completo = False
                difs_placar.append(f"{b['data']} {clube(x['m'])} x {clube(x['v'])}: soma dos gols do boletim {ev[0]}-{ev[1]}, "
                                   f"site oficial {placar[0]}-{placar[1]}")
        elif ev == tot:
            placar = ev
        else:
            fora = ext.get("RSSSF") or ext.get("ogol")
            if fora == ev:
                placar = ev
                difs_placar.append(f"{b['data']} {clube(x['m'])} x {clube(x['v'])}: total do boletim {tot[0]}-{tot[1]}, gols do boletim "
                                   f"{ev[0]}-{ev[1]} (vale este, como a RSSSF/ogol)")
            else:
                placar = tot
                completo = False
                alternativa = None if fora else ev
                difs_placar.append(f"{b['data']} {clube(x['m'])} x {clube(x['v'])}: total do boletim {tot[0]}-{tot[1]}, gols do boletim "
                                   f"{ev[0]}-{ev[1]}" + (f", outra fonte {fora[0]}-{fora[1]}" if fora else ", sem outra fonte")
                                   + f" (vale {placar[0]}-{placar[1]})")
        for fonte, sc in ext.items():
            if sc == placar:
                conf[fonte][0] += 1
            else:
                conf[fonte][1].append(f"{b['data']} {clube(x['m'])} {placar[0]}-{placar[1]} {clube(x['v'])} ({fonte} {sc[0]}-{sc[1]})")
        prorrog = any(t in (3, 4) for t in b["tempos"])
        pm, pv = b["penaltis"] if b["penaltis"] else (None, None)
        lados = {"m": clube(x["m"]), "v": clube(x["v"])}
        # nomes: código do jogador pelo site oficial (2013+) ou pelo bloco de gols do portal
        ids_jogo = {}
        if of is not None:
            for g in of["gols"]:
                ids_jogo[(g["lado"], g["jogador"])] = g["player_id"]

        def pid(lado, h, pid_portal=None):
            return pid_portal or ids_jogo.get((lado, h)) or ids_por_nome.get(h)

        def exibir(lado, h, pid_portal=None):
            p = pid(lado, h, pid_portal)
            en = nomes_en.get(str(p), ("", ""))[1] if p else ""
            nm, fonte_nm = nome_jog(h, en, rs_nome.get((re.sub(r"\d+$", "", h), x[lado]), ""))
            if "aproximação" in fonte_nm:
                APROXIMADOS[(nm, h)].add(ano)
            return nm

        gols = []
        for g in b["gols"]:
            mi, ac = minuto(g["minuto"], g["meio"], g["acrescimo"])
            gols.append({"clube": lados[g["lado"]], "jogador": exibir(g["lado"], g["jogador"], g.get("player_id")),
                         "minuto": mi, "acrescimo": ac, "tipo": g["tipo"]})
        gols_boletim = gols
        if chave in AWD:
            gols = []
        elif not completo:
            gols = []
            gols_dif.append(f"{lados['m']} {placar[0]}-{placar[1]} {lados['v']}: {ev[0]}+{ev[1]} autores no boletim")
        cartoes = []
        for c in b["cartoes"]:
            if not c["numero"]:
                cart_staff += 1
                continue
            mi, ac = minuto(c["minuto"], c["meio"], c["acrescimo"])
            cartoes.append({"clube": lados[c["lado"]], "jogador": exibir(c["lado"], c["jogador"]), "minuto": mi, "acrescimo": ac,
                            "cor": c["cor"]})
        if prorrog:
            obs.append("prorrogação")
        sorteio = None
        if chave in SORTEIO:
            sorteio = lados[SORTEIO[chave][0]]
            obs.append(f"{sorteio} venceu no sorteio: {SORTEIO[chave][1]}")
        elif pm is not None:
            obs.append(f"{lados['m'] if pm > pv else lados['v']} venceu nos pênaltis por {max(pm, pv)}-{min(pm, pv)}")
        grupo = GRUPO_SPLIT.get(x["fase_oficial"] or "")
        jogos.append({"mandante": lados["m"], "visitante": lados["v"], "gm": placar[0], "gv": placar[1], "pm": pm, "pv": pv,
                      "sorteio": sorteio, "awd": chave in AWD,
                      "prorrogacao": prorrog, "fase": fase, "grupo_split": grupo, "rodada": x["rodada"],
                      "data": b["data"], "hora": b["hora"], "estadio": estadio(b["estadio"]), "publico": b["publico"],
                      "arbitro": romanizar(b["arbitro"]) if b["arbitro"] else None, "fonte_id": f"{x['ano']}_{x['meet']}_{x['game']}",
                      "gols": gols, "cartoes": cartoes, "obs": obs, "m_cod": x["m"], "v_cod": x["v"], "alternativa": alternativa,
                      "gols_boletim": gols_boletim, "dif_idx": len(difs_placar) - 1, "gdif_idx": len(gols_dif) - 1})
    escolher_pela_tabela(ano, jogos, difs_placar, gols_dif)
    return montar(ano, jogos, difs_placar, gols_dif, conf, cart_staff)


def escolher_pela_tabela(ano: int, jogos: list[dict], difs_placar: list[str], gols_dif: list[str]) -> None:
    """Jogo em que o total do boletim e a soma dos gols não batem e não há outra fonte de placar (1997, 2011, 2012): fica a
    soma dos gols quando ela faz mais linhas da tabela da RSSSF fecharem."""
    amb = [j for j in jogos if j.get("alternativa")]
    if not amb:
        return

    def nota() -> int:
        return conferir_tabela(ano, tabela(ano, [j for j in jogos if j["fase"] in ("Liga", "1º turno", "2º turno")]))[0]

    base = nota()
    for j in amb:
        antes = (j["gm"], j["gv"])
        j["gm"], j["gv"] = j["alternativa"]
        n = nota()
        if n > base:
            base = n
            j["gols"] = j["gols_boletim"]
            difs_placar[j["dif_idx"]] = difs_placar[j["dif_idx"]].replace(f" (vale {antes[0]}-{antes[1]})",
                                                                          f" (vale {j['gm']}-{j['gv']}: a tabela da RSSSF fecha com ele)")
            gols_dif[j["gdif_idx"]] = ""
        else:
            j["gm"], j["gv"] = antes
    gols_dif[:] = [g for g in gols_dif if g]


def rodadas_por_ordem(jogos: list[dict]) -> None:
    """Antes de 2013 o portal não dá a rodada: ela é a ordem do jogo de cada clube na fase, quando é a mesma para os dois."""
    por_fase = defaultdict(list)
    for j in jogos:
        por_fase[j["fase"]].append(j)
    for fase, lst in por_fase.items():
        n = Counter()
        for j in sorted(lst, key=lambda j: (j["data"], j["fonte_id"])):
            n[j["mandante"]] += 1
            n[j["visitante"]] += 1
            j["rodada"] = n[j["mandante"]] if n[j["mandante"]] == n[j["visitante"]] else None


def montar(ano, jogos, difs_placar, gols_dif, conf, cart_staff) -> dict:
    liga_f = [f for f in dict.fromkeys(j["fase"] for j in jogos) if f in ("Liga", "1º turno", "2º turno")]
    mm_f = [f for f in dict.fromkeys(j["fase"] for j in jogos) if f not in liga_f]
    if ano < 2013:
        rodadas_por_ordem([j for j in jogos if j["fase"] in liga_f or j["fase"] == "Grupos finais"])
    liga = [j for j in jogos if j["fase"] in liga_f or j["fase"] == "Grupos finais"]
    t = tabela(ano, liga)
    regular = [j for j in jogos if j["fase"] in liga_f and not j["grupo_split"]]
    obs = []
    ajuste = {}
    # 2012: grupos depois da divisão (os 8 primeiros na 1ª fase vão ao grupo A)
    if ano == 2012:
        t1 = tabela(ano, [j for j in jogos if j["fase"] == "Liga"])
        a = set(ordem(ano, t1, {})[:8])
        for j in jogos:
            if j["fase"] == "Grupos finais":
                j["grupo_split"] = "A" if j["mandante"] in a else "B"
                j["fase"] = "Liga"
        liga_f = ["Liga"]
    grupos = {}
    for j in jogos:
        if j["grupo_split"]:
            grupos[j["mandante"]] = grupos[j["visitante"]] = j["grupo_split"]
            j["obs"].insert(0, f"jogo depois da divisão em grupos: grupo {j['grupo_split']} "
                               f"({'título' if j['grupo_split'] == 'A' else 'de baixo'})")
    # mata-mata: campeão, vice e eliminados
    campeao = vice = None
    elim = {}
    mm = [j for j in jogos if j["fase"] not in liga_f]
    nomes_mm = {}
    if mm:
        nomes_mm = nomear_mata_mata(ano, mm)
        for j in mm:
            j["fase"] = nomes_mm[id(j)]
        mm_f = list(dict.fromkeys(j["fase"] for j in mm))
        for f in mm_f:
            for par, lst in confrontos([j for j in mm if j["fase"] == f]).items():
                venc = vencedor(lst)
                perd = (set(par) - {venc}).pop()
                elim[perd] = ORDEM_MM.get(f, 0)
                if f == "Final":
                    campeao, vice = venc, perd
    reg_ord = ordem(ano, tabela(ano, [j for j in jogos if j["fase"] in liga_f]), ajuste)
    pos_reg = {c: i for i, c in enumerate(reg_ord)}
    oficial = DADOS / "oficial" / f"tabela_{ano}.json"
    difs_of = []
    if oficial.exists():
        # a tabela oficial conta todos os jogos do ano, com o playoff (2003-2011), mas os pontos só da liga: a
        # classificação segue ela
        pts_liga = {c: x["pontos"] for c, x in t.items()}
        t = tabela(ano, jogos)
        for c in t:
            t[c]["pontos"] = pts_liga.get(c, 0)
        of = json.loads(oficial.read_text(encoding="utf-8"))["tabela"]
        for r in of:
            c = clube(r["teamId"])
            x = t[c]
            ofi = {"jogos": r["gameCount"], "vitorias": r["winCnt"], "empates": r["tieCnt"], "derrotas": r["lossCnt"],
                   "gols_pro": r["gainGoal"], "gols_contra": r["lossGoal"]}
            if any(x[k] != v for k, v in ofi.items()):
                difs_of.append(f"{c}: oficial {ofi}, jogos { {k: x[k] for k in ofi} }")
            if r["gainPoint"] != x["pontos"]:
                ajuste[c] = r["gainPoint"] - x["pontos"]
        ordem_final = [clube(r["teamId"]) for r in sorted(of, key=lambda r: r["rank"])]
        assert set(ordem_final) == set(t), (ano, set(ordem_final) ^ set(t))
        campeao, vice = ordem_final[0], ordem_final[1]
        fonte_clf = "K League (classificação oficial, www.kleague.com)"
    elif grupos:
        ordem_final = sorted(t, key=lambda c: (grupos.get(c, "B"), ordem(ano, t, ajuste).index(c)))
        campeao, vice = ordem_final[0], ordem_final[1]
        fonte_clf = "soma dos jogos (a ordem de cada grupo depois da divisão: o grupo A em cima)"
    elif campeao:
        ordem_final = sorted(t, key=lambda c: (c != campeao, c != vice, -elim.get(c, 0), pos_reg[c]))
        fonte_clf = "soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela"
    else:
        ordem_final = ordem(ano, t, ajuste)
        campeao, vice = ordem_final[0], ordem_final[1]
        fonte_clf = "soma dos jogos"
    clf = []
    for i, c in enumerate(ordem_final, 1):
        x = dict(t[c])
        if ajuste.get(c):
            x["pontos"] += ajuste[c]
        clf.append({"posicao": i, "clube": c, **x, "ajuste_pontos": ajuste.get(c, "") or "", "situacao": "campeao" if i == 1 else "",
                    "fonte": fonte_clf, "observacao": ("grupo " + grupos[c] + " depois da divisão") if c in grupos else ""})
    # fases do pacote
    fases_pac = []
    for f in liga_f:
        fases_pac.append((f, "liga", "pontos_corridos"))
    for f in dict.fromkeys(j["fase"] for j in mm):
        lst = [j for j in mm if j["fase"] == f]
        serie = "ida_volta" if any(len(v) >= 2 for v in confrontos(lst).values()) else "jogo_unico"
        fases_pac.append((f, "mata_mata", serie))
    # artilheiro pela soma dos gols da liga
    por_jog = defaultdict(Counter)
    for j in jogos:
        if j["fase"] not in liga_f:   # a K League conta só a liga (sem playoff nem final)
            continue
        for g in j["gols"]:
            if g["tipo"] != "contra":
                por_jog[g["jogador"]][g["clube"]] += 1
    tot = {p: sum(c.values()) for p, c in por_jog.items()}
    maximo = max(tot.values(), default=0)
    art = [{"jogador": p, "clube": por_jog[p].most_common(1)[0][0], "gols": n} for p, n in tot.items() if n == maximo]
    return {"jogos": jogos, "clf": clf, "tab": t, "fases": fases_pac, "campeao": campeao, "vice": vice, "art": art, "por_jog": por_jog,
            "difs_placar": difs_placar, "gols_dif": gols_dif, "conf": conf, "cart_staff": cart_staff, "obs": obs,
            "classificacao": fonte_clf, "num_clubes": len(t), "grupos": grupos, "regular": regular, "difs_oficial": difs_of,
            "ajuste": ajuste}


def confrontos(lst: list[dict]) -> dict[tuple, list[dict]]:
    d = defaultdict(list)
    for j in lst:
        d[tuple(sorted((j["mandante"], j["visitante"])))].append(j)
    return d


def vencedor(lst: list[dict]) -> str:
    tot = Counter()
    for j in lst:
        tot[j["mandante"]] += j["gm"]
        tot[j["visitante"]] += j["gv"]
    a, b = lst[0]["mandante"], lst[0]["visitante"]
    if tot[a] != tot[b]:
        return a if tot[a] > tot[b] else b
    ult = lst[-1]
    if ult["pm"] is not None:
        return ult["mandante"] if ult["pm"] > ult["pv"] else ult["visitante"]
    fora = Counter()
    for j in lst:
        fora[j["visitante"]] += j["gv"]
    if fora[a] != fora[b]:
        return a if fora[a] > fora[b] else b
    raise SystemExit(f"confronto sem vencedor: {[(j['data'], j['mandante'], j['gm'], j['gv'], j['visitante']) for j in lst]}")


def nomear_mata_mata(ano: int, mm: list[dict]) -> dict[int, str]:
    """Nome de cada jogo do mata-mata pela ordem: a final é o último confronto; antes dele, semifinal, segunda e primeira
    fase (2007-2011: 1ª fase com dois jogos, 3º x 6º e 4º x 5º; 2ª fase, semifinal e final)."""
    ordem_c = []
    for j in sorted(mm, key=lambda j: (j["data"], j["fonte_id"])):
        k = tuple(sorted((j["mandante"], j["visitante"])))
        if k not in ordem_c:
            ordem_c.append(k)
    # agrupa confrontos em rodadas: confrontos que começam antes de algum clube deles voltar a jogar
    rodadas, vistos = [], set()
    for k in ordem_c:
        if not rodadas or set(k) & vistos:
            rodadas.append([k])
            vistos = set(k)
        else:
            rodadas[-1].append(k)
            vistos |= set(k)
    nomes = ["Final", "Semifinal", "Segunda fase", "Primeira fase"]
    if len(rodadas) > len(nomes):
        raise SystemExit(f"{ano}: mata-mata com {len(rodadas)} rodadas")
    nome_c = {}
    for i, ks in enumerate(reversed(rodadas)):
        for k in ks:
            nome_c[k] = nomes[i]
    return {id(j): nome_c[tuple(sorted((j["mandante"], j["visitante"])))] for j in mm}


# ----------------------------------------------------------------------------------------------------- saída
def escrever(nome: str, campos: list[str], linhas: list[dict]) -> None:
    with (PACOTE / f"{nome}.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for l in linhas:
            w.writerow({k: ("" if l.get(k) is None else l.get(k)) for k in campos})


def por_rodada(temporada: str, ano: int, jogos: list[dict], clf: list[dict]) -> list[dict]:
    clubes = [c["clube"] for c in clf]
    n = len(clubes)
    rebaixados = sum(1 for c in clf if c["situacao"] == "rebaixado")
    acum = {c: [0, 0, 0, 0, 0, 0, 0] for c in clubes}   # pts, j, v, e, d, gp, gc
    saida = []
    for r in sorted({j["rodada"] for j in jogos}):
        for j in (j for j in jogos if j["rodada"] == r):
            if j.get("wo") and j["gm"] is None:
                for c in (j["mandante"], j["visitante"]):
                    acum[c][1] += 1
                    acum[c][0] += pontos(ano, 1, 0) if c == j["wo"] else 0
                    acum[c][2 if c == j["wo"] else 4] += 1
                continue
            for c, gp, gc, pp, pc in ((j["mandante"], j["gm"], j["gv"], j["pm"], j["pv"]), (j["visitante"], j["gv"], j["gm"], j["pv"], j["pm"])):
                if j.get("sorteio"):
                    pp, pc = (1, 0) if c == j["sorteio"] else (0, 1)
                x = acum[c]
                x[1] += 1; x[5] += gp; x[6] += gc
                x[0] += pontos(ano, gp, gc, j["prorrogacao"], pp, pc)
                ganhou = gp > gc or (gp == gc and pp is not None and pp > pc)
                perdeu = gp < gc or (gp == gc and pp is not None and pp < pc)
                x[2 if ganhou else 4 if perdeu else 3] += 1
        ordem_r = sorted(clubes, key=lambda c: (-acum[c][0], -(acum[c][5] - acum[c][6]), -acum[c][5], c))
        for i, c in enumerate(ordem_r, 1):
            x = acum[c]
            zona = "titulo" if i == 1 else "rebaixamento" if i > n - rebaixados else "meio"
            saida.append({"temporada": temporada, "rodada": r, "clube": c, "posicao": i, "pontos": x[0], "jogos": x[1],
                          "vitorias": x[2], "empates": x[3], "derrotas": x[4], "gols_pro": x[5], "gols_contra": x[6], "zona": zona})
    return saida


def conferir_tabela(ano: int, tab: dict) -> tuple[int, list[str]]:
    """Cada linha da nossa tabela (só a liga: sem playoff e final) contra as linhas de tabela da RSSSF do ano, por jogos,
    gols pró, gols contra e pontos."""
    rs = {(x["jogos"], x["gp"], x["gc"], x["pontos"]) for x in ler_rsssf.tabelas(ano)}
    rs_sem_pts = {(x["jogos"], x["gp"], x["gc"]) for x in ler_rsssf.tabelas(ano)}
    ok, difs = 0, []
    for c, x in tab.items():
        k = (x["jogos"], x["gols_pro"], x["gols_contra"], x["pontos"])
        if k in rs:
            ok += 1
        elif k[:3] in rs_sem_pts:
            pts = sorted(r[3] for r in rs if r[:3] == k[:3])
            difs.append(f"{c}: pontos {x['pontos']} aqui, {'/'.join(map(str, pts))} na RSSSF (jogos e gols iguais)")
        else:
            difs.append(f"{c}: {x['jogos']} jogos, {x['gols_pro']}-{x['gols_contra']}, {x['pontos']} pontos não está na RSSSF")
    return ok, difs


def participantes_lista(ano: int) -> set[str]:
    """Clubes da 1ª divisão de um ano pela lista de jogos do site oficial (cache de baixar_portal.lista_oficial)."""
    import gzip
    saida = set()
    for arq in (RAIZ / "data" / "cache" / "kleague-asia" / "lista_oficial").glob(f"{ano}_*.json.gz"):
        for x in json.loads(gzip.decompress(arq.read_bytes()))["data"]["scheduleList"]:
            if str(x["meetSeq"]) == "1" and x["homeTeam"] in CLUBES:
                saida.add(clube(x["homeTeam"]))
    return saida


def nomes_rsssf(so: list[int], rs_jogos: dict, rs_map: dict) -> dict[tuple, str]:
    """{(jogador em hangul, código do clube): nome na RSSSF}: cada gol do boletim ligado ao autor da RSSSF do mesmo jogo, do
    mesmo lado e do mesmo minuto (±1). Serve para os estrangeiros sem nome em inglês (antes de 2013)."""
    votos = defaultdict(Counter)
    for a in so:
        idx = {}
        for e in rs_jogos[a]:
            mm, vv = rs_map.get(e["mandante"]), rs_map.get(e["visitante"])
            if mm and vv and e.get("data") and e.get("autores"):
                idx[(mm, vv, e["data"])] = e
        for j in lista(a):
            b = ler_portal.boletim(j["ano"], j["meet_seq"], j["game_id"])
            e = next((idx[k] for d in (0, -1, 1) if (k := (b["mandante_id"], b["visitante_id"], dia(b["data"], d))) in idx), None)
            aut = ler_rsssf.autores(e["autores"], e["gm"], e["gv"]) if e else None
            if not aut:
                continue
            for g in b["gols"]:
                if g["tipo"] == "contra" or g["minuto"] is None:
                    continue
                cands = {n for n, mi in (aut[0] if g["lado"] == "m" else aut[1]) if abs(mi - g["minuto"]) <= 1}
                if len(cands) == 1:
                    cod = b["mandante_id"] if g["lado"] == "m" else b["visitante_id"]
                    votos[(re.sub(r"\d+$", "", g["jogador"]), cod)][cands.pop()] += 1
    return {k: c.most_common(1)[0][0] for k, c in votos.items()}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    PACOTE.mkdir(parents=True, exist_ok=True)
    so = [int(a) for a in sys.argv[1:]] or ANOS
    nomes_en = ler_oficial.nomes()
    # hangul -> código do jogador, quando o nome é de um jogador só (para achar o inglês de quem não tem código no lance)
    por_nome = defaultdict(set)
    for pid_, (h, _) in nomes_en.items():
        por_nome[re.sub(r"\d+$", "", h)].add(pid_)
    ids_por_nome = {h: next(iter(s)) for h, s in por_nome.items() if len(s) == 1}
    # jogos da RSSSF e do ogol, com os nomes ligados aos códigos do portal
    rs_jogos = {a: ler_rsssf.jogos(a) for a in so}
    og = ler_ogol()
    og_jogos = defaultdict(list)
    for o in og:
        og_jogos[o["ano"]].append(o)
    por_data = defaultdict(list)
    for a in so:
        for j in lista(a):
            b = ler_portal.boletim(j["ano"], j["meet_seq"], j["game_id"])
            por_data[b["data"]].append({"m": b["mandante_id"], "v": b["visitante_id"],
                                        "placar": (sum(g["lado"] == "m" for g in b["gols"]), sum(g["lado"] == "v" for g in b["gols"]))})
    rs_map = casar_nomes([e for a in so for e in rs_jogos[a]], por_data)
    og_map = casar_nomes([e for a in so for e in og_jogos.get(a, [])], por_data)
    rs_nome = nomes_rsssf(so, rs_jogos, rs_map)
    res = {}
    for a in so:
        res[a] = edicao(a, nomes_en, ids_por_nome, rs_map, og_map, rs_jogos, og_jogos, rs_nome)
        print(a, "ok", flush=True)
    # rebaixamento (2012 em diante): quem não está no ano seguinte (o último ano olha a lista de jogos do ano em curso)
    for a in so:
        r = res[a]
        prox = {x["clube"] for x in res[a + 1]["clf"]} if a + 1 in res else participantes_lista(a + 1)
        for c in r["clf"]:
            if a >= 2012 and prox and c["clube"] not in prox:
                c["situacao"] = "rebaixado"
            if (a, c["clube"]) in OBS_CLASSIFICACAO:
                c["observacao"] = "; ".join(filter(None, [c["observacao"], OBS_CLASSIFICACAO[(a, c["clube"])]]))
    wiki = podio()
    wiki_art = artilheiros()
    ed_l, fa_l, pa_l, go_l, ca_l, cf_l, cr_l, pu_l, ar_l, co_l, rel = [], [], [], [], [], [], [], [], [], [], []
    for a in so:
        r = res[a]
        tp = str(a)
        w = wiki.get(a)
        cw, vw = (clube(w[0]), clube(w[1])) if w else (None, None)
        obs_conf = f"campeão {r['campeao']}" + (" (igual à Wikipédia)" if cw == r["campeao"] else f" (Wikipédia: {cw})")
        if vw != r["vice"]:
            obs_conf += f"; vice: {r['vice']} aqui, {vw} na Wikipédia"
        ok_t, difs_t = conferir_tabela(a, {c: x for c, x in tabela(a, r["regular"]).items()} if r["grupos"] else
                                       tabela(a, [j for j in r["jogos"] if j["fase"] in ("Liga", "1º turno", "2º turno")]))
        r["tab_ok"], r["tab_difs"] = ok_t, difs_t
        r["formato"] = formato(a, r)
        ed_l.append({"temporada": tp, "ano_inicio": a, "ano_fim": a, "nome_oficial": nome_oficial(a), "num_clubes": r["num_clubes"],
                     "pontos_vitoria": 2 if a <= 1983 or 1985 <= a <= 1992 else 4 if a == 1993 else 3,
                     "formato": formato(a, r), "campeao": r["campeao"], "vice": r["vice"], "fontes": FONTE,
                     "observacao": "; ".join(r["obs"])})
        for o, (f, tipo, serie) in enumerate(r["fases"], 1):
            fa_l.append({"temporada": tp, "ordem": o, "fase": f, "tipo": tipo, "num_grupos": "", "formato_serie": serie,
                         "criterio": ("pontos, gols pró, saldo de gols" if a >= 2016 else "pontos, saldo de gols, gols pró")
                                     if tipo == "liga" else "gols no agregado, pênaltis" if serie == "ida_volta" else "prorrogação e pênaltis"})
        gols_ed = autores = 0
        for n, j in enumerate(sorted(r["jogos"], key=lambda j: (j["data"], j["fonte_id"])), 1):
            pid = f"{a}-{n:04d}"
            obs = list(j["obs"])
            if j["arbitro"]:
                obs.append(f"árbitro: {j['arbitro']}")
            pa_l.append({"id": pid, "temporada": tp, "fase": j["fase"], "grupo": "", "rodada": j["rodada"], "data": j["data"],
                         "hora": j["hora"], "mandante": j["mandante"], "visitante": j["visitante"], "gols_mandante": j["gm"],
                         "gols_visitante": j["gv"], "penaltis_mandante": j["pm"], "penaltis_visitante": j["pv"],
                         "resultado_especial": "wo" if j.get("wo") else "awd" if j.get("awd") else "", "estadio": j["estadio"], "cidade": "", "publico": j["publico"], "fonte": FONTE,
                         "fonte_id": j["fonte_id"], "gols_texto": gols_texto(j), "observacao": "; ".join(obs)})
            gols_ed += (j["gm"] or 0) + (j["gv"] or 0)
            for g in j["gols"]:
                go_l.append({"partida_id": pid, "clube": g["clube"], "jogador": g["jogador"], "minuto": g["minuto"],
                             "acrescimo": g["acrescimo"], "tipo": g["tipo"], "fonte": FONTE})
                autores += 1
            for c in j["cartoes"]:
                ca_l.append({"partida_id": pid, "clube": c["clube"], "jogador": c["jogador"], "minuto": c["minuto"],
                             "acrescimo": c["acrescimo"], "cor": c["cor"], "fonte": FONTE})
        for c in r["clf"]:
            cf_l.append(dict(c, temporada=tp))
        liga_j = [j for j in r["jogos"] if j["fase"] in ("Liga",)]
        if liga_j and all(j["rodada"] for j in liga_j) and len({j["fase"] for j in r["jogos"]} - {"Liga"}) == 0:
            r["rodada_ok"] = True
            cr_l += por_rodada(tp, a, liga_j, r["clf"])
        oficial = wiki_art.get(a, [])
        for jog, cod, g in oficial:
            # o nome como no gols.csv: o jogador do clube com mais gols na soma dos boletins (no máximo 2 a menos)
            cands = sorted(((n, cl[clube(cod)]) for n, cl in r["por_jog"].items() if cl[clube(cod)] >= g - 2), key=lambda x: -x[1])
            ar_l.append({"temporada": tp, "jogador": cands[0][0] if cands else jog, "clube": clube(cod), "gols": g,
                         "fonte": "Wikipédia (K League Top Scorer Award)" + (f"; lá: {jog}" if cands and cands[0][0] != jog else "")})
        if {(clube(cod), g) for _, cod, g in oficial} != {(x["clube"], x["gols"]) for x in r["art"]}:
            r["art_dif"] = ("Wikipédia: " + "; ".join(f"{j} ({clube(c)}) {g}" for j, c, g in oficial) + "; soma dos boletins: " +
                            "; ".join(f"{x['jogador']} ({x['clube']}) {x['gols']}" for x in r["art"]))
        r["art_oficial"] = [{"jogador": j, "clube": clube(c), "gols": g} for j, c, g in oficial]
        co_l.append({"temporada": tp, "jogos": len(r["jogos"]), "jogos_esperados": len(r["jogos"]), "tabelas_conferidas": 1,
                     "tabelas_divergentes": 1 if r["tab_difs"] else 0, "gols": gols_ed, "gols_com_autor": autores,
                     "observacao": obs_conf})
        rel.append((a, r, gols_ed, autores, obs_conf))
    # clubes: nomes de cada fonte
    for n, c in rs_map.items():
        for a in so:
            if any(e["mandante"] == n or e["visitante"] == n for e in rs_jogos[a]):
                NOMES[c]["RSSSF"][n].add(a)
    for o in og:
        if o["ano"] in so:
            for n in (o["mandante"], o["visitante"]):
                if n in og_map:
                    NOMES[og_map[n]]["ogol"][n].add(o["ano"])
    usados = {x["clube"] for x in cf_l}
    cl_l = []
    for cod, (nome, cidade, prov) in sorted(CLUBES.items(), key=lambda x: x[1][0]):
        if nome not in usados:
            continue
        partes = []
        for fonte, nomes in sorted(NOMES[cod].items()):
            for nm, anos in sorted(nomes.items(), key=lambda x: min(x[1])):
                partes.append(f"{fonte}:{nm}:{faixa(anos)}")
        cl_l.append({"clube": nome, "regiao": prov, "cidade": cidade, "pais": "KOR", "nomes_fonte": "|".join(partes)})
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": "kor-1", "nome": "Campeonato Sul-Coreano", "nome_curto": "Sul-Coreano", "tipo": "liga", "nivel": 1, "pais": "KOR",
        "pais_nome": "Coreia do Sul", "regiao": None, "confederacao": "AFC", "rotulo_painel": "Sul-Coreano",
        "menu_painel": "Coreia do Sul · 1ª divisão", "do_painel": "do Campeonato Sul-Coreano", "o_painel": "o Campeonato Sul-Coreano",
        "observacao": "K League (1983-2012) e K League 1 (2013 em diante)"}, ensure_ascii=False, indent=1), encoding="utf-8")
    escrever("paises", ["codigo", "nome", "confederacao"], [{"codigo": "KOR", "nome": "Coreia do Sul", "confederacao": "AFC"}])
    escrever("clubes", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], cl_l)
    escrever("edicoes", ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "formato", "campeao",
                         "vice", "fontes", "observacao"], ed_l)
    escrever("fases", ["temporada", "ordem", "fase", "tipo", "num_grupos", "formato_serie", "criterio"], fa_l)
    escrever("partidas", ["id", "temporada", "fase", "grupo", "rodada", "data", "hora", "mandante", "visitante", "gols_mandante",
                          "gols_visitante", "penaltis_mandante", "penaltis_visitante", "resultado_especial", "estadio", "cidade",
                          "publico", "fonte", "fonte_id", "gols_texto", "observacao"], pa_l)
    escrever("gols", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "tipo", "fonte"], go_l)
    escrever("cartoes", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "cor", "fonte"], ca_l)
    escrever("classificacao_final", ["temporada", "posicao", "clube", "jogos", "vitorias", "empates", "derrotas", "gols_pro",
                                     "gols_contra", "pontos", "ajuste_pontos", "situacao", "fonte", "observacao"], cf_l)
    escrever("classificacao_rodada", ["temporada", "rodada", "clube", "posicao", "pontos", "jogos", "vitorias", "empates",
                                      "derrotas", "gols_pro", "gols_contra", "zona"], cr_l)
    escrever("tabelas_publicadas", ["temporada", "fase", "grupo", "posicao", "nome_fonte", "clube", "jogos", "vitorias", "empates",
                                    "derrotas", "gols_pro", "gols_contra", "pontos", "fonte"], pu_l)
    escrever("artilheiros", ["temporada", "jogador", "clube", "gols", "fonte"], ar_l)
    escrever("conferencia", ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols",
                             "gols_com_autor", "observacao"], co_l)
    from relatorio import escrever_relatorio
    escrever_relatorio(RELATORIO, rel, cl_l, pa_l, go_l, ca_l, TABELA_RSSSF, APROXIMADOS)
    print(f"{len(ed_l)} edições, {len(pa_l)} jogos, {len(go_l)} gols com autor, {len(ca_l)} cartões, {len(cl_l)} clubes")
    for a, r, *_ in rel:
        print(a, r["campeao"], "| tabela ok", r["tab_ok"], "difs", r["tab_difs"][:3], "| placar", r["difs_placar"][:2],
              "| rsssf", r["conf"]["RSSSF"][0], r["conf"]["RSSSF"][1][:2], "| ogol", r["conf"]["ogol"][0], r["conf"]["ogol"][1][:2],
              "| art", r.get("art_dif", ""))


def gols_texto(j: dict) -> str:
    """Autores do boletim quando eles não fecham com o placar (não entram no gols.csv)."""
    if j["gols"] or not j.get("gols_boletim") or j.get("wo"):
        return ""
    partes = [f"{g['jogador']} ({g['clube']}) {g['minuto']}" + (f"+{g['acrescimo']}" if g["acrescimo"] else "") +
              ("'" if g["minuto"] is not None else "") + (" (contra)" if g["tipo"] == "contra" else " (pênalti)" if g["tipo"] == "penalti" else "")
              for g in j["gols_boletim"]]
    if j.get("awd"):
        return "em campo: " + "; ".join(partes)
    return "; ".join(partes) + f" — o boletim do portal tem {len(partes)} autor(es) para {(j['gm'] or 0) + (j['gv'] or 0)} gol(s)"


def formato(a: int, r: dict) -> str:
    n = r["num_clubes"]
    fs = [f for f, _, _ in r["fases"]]
    if r["grupos"]:
        return f"pontos corridos ({n} clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados"
    if "1º turno" in fs:
        return f"dois turnos de pontos corridos ({n} clubes) e decisão do título" + (" entre os campeões dos turnos" if a <= 1996 else " em playoff")
    if len(fs) > 1:
        return f"pontos corridos ({n} clubes) e playoff do título"
    return f"pontos corridos, {n} clubes"


if __name__ == "__main__":
    main()
