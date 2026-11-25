"""Monta o pacote do Campeonato Saudita (ksa-1) em data/coleta/ksa-1/pacote/ e o relatório docs/coleta/ksa-1.md.

- Edições: as 69 temporadas da lista oficial (campeoes_wiki.py), 1957/58 a 2025/26 (edicoes.py diz as eras).
- 1957/58-1973/74: campeão e vice da lista oficial; o jogo da final da Copa do Rei da RSSSF quando é o mesmo par.
- 1974/75 em diante: a tabela da liga da RSSSF (classificação e conferência) e os jogos: da RSSSF até 2005/06 quando ela
  tem a fase de liga completa; do ogol de 2006/07 em diante e nos anos em que a RSSSF não está completa (2003/04,
  2004/05); o playoff do título sempre da RSSSF. Autores dos gols: RSSSF (até 2005/06) e ESPN (2022/23 em diante, com
  cartões, estádio, público e hora).
- Classificação final: o campeão e o vice oficiais em cima; os outros pela ordem da tabela da RSSSF (nos anos de dois
  grupos, por pontos e saldo). Os números são os da tabela da RSSSF (só a fase de liga); quando a RSSSF dá só jogos e
  pontos, ou só a ordem, o resto fica vazio.
- Conferência: a tabela calculada dos jogos contra a tabela da RSSSF; o campeão e o vice contra a lista oficial; os
  placares contra o ogol e a ESPN.

Uso: python coleta/ksa-1/importar.py [fim ...]   (fim = ano em que a temporada termina)
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
import fontes as F  # noqa: E402
from campeoes_wiki import lista  # noqa: E402
from clubes_ksa import CLUBES, clube  # noqa: E402
from edicoes import GRUPOS, nome_oficial  # noqa: E402

RAIZ = AQUI.parent.parent
DADOS = RAIZ / "data" / "coleta" / "ksa-1"
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "ksa-1.md"
ORDEM_FASE = {"Liga": 0, "Primeira fase": 1, "Semifinal": 2, "Segunda fase": 2, "Disputa do 3º lugar": 3, "Final": 4}


def dia(s: str, d: int) -> str:
    return (date.fromisoformat(s) + timedelta(days=d)).isoformat()


def motivo_pt(s: str) -> str:
    s = s.strip()
    for en, pt in (("fielded ineligible player", "escalou jogador irregular"), ("fielded suspended player", "escalou jogador suspenso"),
                   ("used ineligible player", "escalou jogador irregular"), ("used 3 foreigners", "usou 3 estrangeiros"),
                   ("dns", "não compareceu")):
        s = s.replace(en, pt)
    return s


def nome_jogador(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip(" .,'")


# ----------------------------------------------------------------------------------------------------- autores
def autores_rsssf(j: dict) -> tuple[list[dict], str]:
    """Gols da linha de autores da RSSSF quando fecham com o placar: (gols, texto quando não fecham)."""
    if not j["autores"]:
        return [], ""
    a = F.ler_rsssf.autores(j["autores"], j["gm"], j["gv"])
    if not a:
        return [], j["autores"].strip("[] ")
    lados = {0: (j["mandante"], j["visitante"]), 1: (j["visitante"], j["mandante"])}
    gols = []
    for i, lado in enumerate(a):
        for nome, mi, tipo in lado:
            # a RSSSF põe o gol contra do lado de quem ganhou o gol, com o nome de quem chutou
            gols.append({"clube": lados[i][0], "jogador": nome_jogador(nome), "minuto": mi, "acrescimo": None, "tipo": tipo,
                         "fonte": "RSSSF"})
    if len(gols) != j["gm"] + j["gv"] or sum(1 for g in gols if g["clube"] == j["mandante"]) != j["gm"]:
        return [], j["autores"].strip("[] ")
    for g in gols:
        if g["minuto"] is not None and g["minuto"] > 90 and not j["prorrogacao"]:
            g["minuto"], g["acrescimo"] = 90, g["minuto"] - 90
    return gols, ""


def minuto_espn(s: str) -> tuple[int | None, int | None]:
    m = re.match(r"(\d+)'?(?:\+(\d+))?", s or "")
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else (None, None)


def juntar_espn(j: dict, e: dict) -> None:
    lados = {"home": j["mandante"], "away": j["visitante"]}
    gols, cart = [], []
    for l in e["lances"]:
        if not l["jogadores"] or l["lado"] not in lados:
            continue
        mi, ac = minuto_espn(l["minuto"])
        if l["gol"]:
            # na ESPN o gol contra já vem do lado do time que ganhou o gol (conferido nos placares)
            gols.append({"clube": lados[l["lado"]], "jogador": nome_jogador(l["jogadores"][0]),
                         "minuto": mi, "acrescimo": ac, "fonte": "ESPN",
                         "tipo": "contra" if l["contra"] else "penalti" if l["penalti"] else "normal"})
        elif l["amarelo"] or l["vermelho"]:
            cart.append({"clube": lados[l["lado"]], "jogador": nome_jogador(l["jogadores"][0]), "minuto": mi, "acrescimo": ac,
                         "cor": "vermelho" if l["vermelho"] else "amarelo"})
    gm = sum(1 for g in gols if g["clube"] == j["mandante"])
    if (gm, len(gols) - gm) == (j["gm"], j["gv"]):
        j["gols"] = gols
    else:
        j["gols_dif"] = f"{j['mandante']} {j['gm']}-{j['gv']} {j['visitante']}: ESPN {gm}+{len(gols) - gm} autores"
    j["cartoes"] = cart
    j["estadio"] = e.get("estadio") or j["estadio"]
    j["publico"] = e.get("publico") or j["publico"]
    j["hora"] = e.get("hora_local")


# ----------------------------------------------------------------------------------------------------- tabela
def tabela(jogos: list[dict], pv: int) -> dict[str, dict]:
    t = defaultdict(lambda: {"jogos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "gols_pro": 0, "gols_contra": 0, "pontos": 0})
    for j in jogos:
        for c, gp, gc in ((j["mandante"], j["gm"], j["gv"]), (j["visitante"], j["gv"], j["gm"])):
            x = t[c]
            x["jogos"] += 1
            x["gols_pro"] += gp
            x["gols_contra"] += gc
            k = "vitorias" if gp > gc else "derrotas" if gp < gc else "empates"
            x[k] += 1
            x["pontos"] += pv if gp > gc else 1 if gp == gc else 0
    return t


def pontos_vitoria(tab: list[dict]) -> int | None:
    linhas = [x for x in tab if x.get("v") is not None]
    for pv in (2, 3):
        if linhas and all(x["pontos"] == pv * x["v"] + x["e"] for x in linhas):
            return pv
    # uma ou outra linha com punição: vale a regra da maioria
    for pv in (2, 3):
        if linhas and sum(x["pontos"] == pv * x["v"] + x["e"] for x in linhas) >= 0.8 * len(linhas):
            return pv
    return None


# ----------------------------------------------------------------------------------------------------- uma edição
def edicao(of: dict, finais_copa: list[dict], usadas: set) -> dict:
    fim = of["fim"]
    r = {"of": of, "fim": fim, "jogos": [], "clf": [], "pub": [], "fases": [], "difs": [], "obs": [], "conf": {},
         "gols_dif": [], "art": [], "fonte_jogos": "", "pv": None, "esperados": None, "formato": ""}
    if fim <= 1974:
        return edicao_antiga(r, of, finais_copa, usadas)
    tabs = F.rsssf_tabelas(fim)
    n_tab = GRUPOS.get(fim, 1)
    tabs = tabs[:n_tab] if fim != 1986 else tabs
    grupos = {}
    if fim in GRUPOS and fim != 1986:
        for g, tab in zip("AB", tabs):
            for x in tab:
                grupos[x["clube"]] = g
    base = [x for tab in tabs for x in tab] if fim != 1986 else tabs_1986(tabs)
    clubes_tab = {x["clube"] for x in base}
    n = len(clubes_tab) if fim not in GRUPOS else None
    esperados = n * (n - 1) if n else sum(len(t) * (len(t) - 1) for t in tabs) if fim in (1975, 1982) else None
    r["esperados"] = esperados
    pv = pontos_vitoria(base)
    r["pv"] = pv
    # jogos da liga
    liga_r = F.rsssf_liga(fim)
    liga_o = F.ogol(fim)
    if n:   # o ogol põe jogos do playoff como rodadas a mais (2002/03, 2003/04: R23-R25)
        liga_o = [j for j in liga_o if not j["rodada"] or j["rodada"] <= 2 * (n - 1)]
    if fim <= 2006 and esperados and len(liga_r) == esperados:
        liga, r["fonte_jogos"] = liga_r, "RSSSF"
    elif liga_o:
        liga, r["fonte_jogos"] = liga_o, "ogol"
    elif liga_r and esperados and len(liga_r) >= 0.9 * esperados:
        liga, r["fonte_jogos"] = liga_r, "RSSSF"
        if len(liga_r) < esperados:
            r["obs"].append(f"a RSSSF tem {len(liga_r)} dos {esperados} jogos da fase de liga")
    else:
        liga = []
        r["fonte_jogos"] = "nenhuma (só a tabela)" if not liga_r else f"RSSSF incompleta ({len(liga_r)} jogos): fora"
        if liga_r and fim == 1976:   # temporada abandonada: entram os jogos que houve
            liga, r["fonte_jogos"] = liga_r, f"RSSSF (temporada abandonada: {len(liga_r)} jogos)"
    # jogos decididos fora de campo (RSSSF "awd"): vale o placar dado, também quando os jogos vêm do ogol
    for x in (x for x in liga_r if x["awd"]):
        alvo = next((j for j in liga if (j["mandante"], j["visitante"]) == (x["mandante"], x["visitante"])), None)
        if alvo is None:
            liga.append(x)
            alvo = x
        alvo.update(gm=x["gm"], gv=x["gv"], awd=True, campo=x["campo"], gols=[], obs_fonte=x["obs_fonte"])
    for j in liga:
        j["grupo"] = grupos.get(j["mandante"], "")
        if j.get("awd"):
            motivo = re.search(r"([A-Z][\w'-]+ (?:fielded|used)[^\];]*|[A-Z][\w'-]+ dns)", j["obs_fonte"])
            j["obs"].append("decidido fora de campo: placar dado " + f"{j['gm']}-{j['gv']}" +
                            (f", {j['campo'][0]}-{j['campo'][1]} em campo" if j.get("campo") else "") +
                            (f" ({motivo_pt(motivo.group(1))})" if motivo else "") + " (RSSSF)")
    # autores: RSSSF (quando os jogos vêm do ogol, procura o mesmo jogo na RSSSF)
    idx_r = {(x["mandante"], x["visitante"]): x for x in liga_r}
    for j in liga:
        fonte_aut = j if j["fonte"] == "RSSSF" else idx_r.get((j["mandante"], j["visitante"]))
        if fonte_aut and (fonte_aut["gm"], fonte_aut["gv"]) == (j["gm"], j["gv"]):
            j["gols"], txt = autores_rsssf(fonte_aut)
            if txt and not j["gols"]:
                j["gols_texto"] = txt
    playoff = F.rsssf_playoff(fim) if fim in (1975, 1982) or 1991 <= fim <= 2007 else []
    for j in playoff:
        a, txt = autores_rsssf(j)
        j["gols"], j["gols_texto"] = a, (txt if not a else "")
    jogos = liga + playoff
    # ESPN (2022/23 em diante); jogo da liga que o ogol não tem entra pela ESPN
    esp = F.espn(fim)
    if esp and esperados and len(liga) < esperados:
        tem = {(j["mandante"], j["visitante"]) for j in liga}
        for (m, v, d), e in esp.items():
            if (m, v) not in tem and grupos.get(m, "") == grupos.get(v, "") and m in clubes_tab and v in clubes_tab:
                novo = {"mandante": m, "visitante": v, "gm": int(e["gols_mandante"]), "gv": int(e["gols_visitante"]),
                        "pm": None, "pv": None, "prorrogacao": False, "gol_de_ouro": False, "data": d, "hora": None,
                        "rodada": None, "fase": "Liga", "grupo": "", "estadio": None, "publico": None, "fonte": "ESPN",
                        "fonte_id": f"espn:{e['id']}", "autores": "", "obs_fonte": "", "perna": None, "secao": "",
                        "gols": [], "cartoes": [], "obs": ["o ogol não tem este jogo: entra pela ESPN"]}
                liga.append(novo)
                jogos.append(novo)
                r["obs"].append(f"1 jogo que falta no ogol entrou pela ESPN ({m} x {v}, {d})")
    if esp:
        ok = dif = 0
        for j in jogos:
            e = next((esp[k] for d in (0, -1, 1) if (k := (j["mandante"], j["visitante"], dia(j["data"], d))) in esp), None)
            if e and j.get("awd"):
                j["cartoes"] = []
                continue
            if e:
                if (int(e["gols_mandante"]), int(e["gols_visitante"])) == (j["gm"], j["gv"]):
                    ok += 1
                    juntar_espn(j, e)
                else:
                    dif += 1
                    r["difs"].append(f"{j['data']} {j['mandante']} {j['gm']}-{j['gv']} {j['visitante']} (ESPN "
                                     f"{e['gols_mandante']}-{e['gols_visitante']})")
        r["conf"]["ESPN"] = (ok, dif)
        r["gols_dif"] += [j["gols_dif"] for j in jogos if j.get("gols_dif")]
    # conferência dos placares com a outra fonte (RSSSF x ogol)
    if r["fonte_jogos"] == "ogol" and liga_r and len(liga_r) >= 0.9 * (esperados or 0):
        ok = 0
        for j in liga:
            x = idx_r.get((j["mandante"], j["visitante"]))
            if x:
                if (x["gm"], x["gv"]) == (j["gm"], j["gv"]):
                    ok += 1
                else:
                    r["difs"].append(f"{j['data']} {j['mandante']} {j['gm']}-{j['gv']} {j['visitante']} (RSSSF {x['gm']}-{x['gv']})")
        r["conf"]["RSSSF"] = (ok, len(liga) - ok)
    elif r["fonte_jogos"] == "RSSSF" and liga_o:
        idx_o = {(x["mandante"], x["visitante"]): x for x in liga_o}
        ok = 0
        for j in liga:
            x = idx_o.get((j["mandante"], j["visitante"]))
            if x:
                if (x["gm"], x["gv"]) == (j["gm"], j["gv"]):
                    ok += 1
                else:
                    r["difs"].append(f"{j['data']} {j['mandante']} {j['gm']}-{j['gv']} {j['visitante']} (ogol {x['gm']}-{x['gv']})")
        r["conf"]["ogol"] = (ok, len(liga) - ok)
    # tabela calculada x tabela da RSSSF
    if liga and pv and fim != 1976:
        calc = tabela(liga, pv)
        for x in base:
            if x.get("v") is None:
                continue
            c = calc.get(x["clube"])
            pub = {"jogos": x["jogos"], "vitorias": x["v"], "empates": x["e"], "derrotas": x["d"], "gols_pro": x["gp"],
                   "gols_contra": x["gc"], "pontos": x["pontos"]}
            if pv and x.get("v") is not None:
                pub["pontos"] = pv * x["v"] + x["e"]   # o ajuste (punição/bônus) vai na classificação e na observação
            if not c or any(c[k] != v for k, v in pub.items()):
                r["difs"].append(f"tabela, {x['clube']}: RSSSF {pub}, jogos { {k: (c or {}).get(k) for k in pub} }")
    # classificação final
    camp, vice = of["campeao"], of["vice"]
    if fim in GRUPOS and fim != 1986:
        ordem = sorted(base, key=lambda x: (-(x["pontos"] or 0), -((x["gp"] or 0) - (x["gc"] or 0)), -(x["gp"] or 0)))
    else:
        ordem = base
    if camp:
        ordem = sorted(ordem, key=lambda x: (x["clube"] != camp, x["clube"] != vice))
    for i, x in enumerate(ordem, 1):
        ajuste = ""
        if pv and x.get("v") is not None and x["pontos"] != pv * x["v"] + x["e"]:
            ajuste = x["pontos"] - (pv * x["v"] + x["e"])
            r["obs"].append(f"{x['clube']}: {ajuste:+d} ponto(s) na tabela da RSSSF (punição ou bônus)")
        sit = "campeao" if camp and x["clube"] == camp else "rebaixado" if re.search(r"(?i)relegat", x["obs"] or "") else ""
        r["clf"].append({"posicao": i, "clube": x["clube"], "jogos": x["jogos"], "vitorias": x["v"], "empates": x["e"],
                         "derrotas": x["d"], "gols_pro": x["gp"], "gols_contra": x["gc"], "pontos": x["pontos"],
                         "ajuste_pontos": ajuste, "situacao": sit, "fonte": "RSSSF (tabela da fase de liga)" +
                         ("; campeão e vice da lista oficial em cima" if camp else ""),
                         "observacao": (f"grupo {grupos[x['clube']]}" if x["clube"] in grupos else "")})
        r["pub"].append({"fase": "Liga", "grupo": grupos.get(x["clube"], ""), "posicao": x["pos"], "nome_fonte": x["nome"],
                         "clube": x["clube"], "jogos": x["jogos"], "vitorias": x["v"], "empates": x["e"], "derrotas": x["d"],
                         "gols_pro": x["gp"], "gols_contra": x["gc"], "pontos": x["pontos"], "fonte": f"RSSSF (sau{fim})"})
    if camp and camp not in clubes_tab:
        r["difs"].append(f"campeão {camp} não está na tabela da RSSSF")
    # fases
    if jogos or base:
        if fim in GRUPOS and fim != 1986:
            r["fases"].append(("Liga", "grupos", "pontos_corridos", 2))
        else:
            r["fases"].append(("Liga", "liga", "pontos_corridos", ""))
    for f in sorted({j["fase"] for j in playoff}, key=lambda f: ORDEM_FASE[f]):
        lst = [j for j in playoff if j["fase"] == f]
        pares = Counter(frozenset((j["mandante"], j["visitante"])) for j in lst)
        r["fases"].append((f, "mata_mata", "ida_volta" if max(pares.values()) >= 2 else "jogo_unico", ""))
    # o playoff confere o campeão oficial
    final = [j for j in playoff if j["fase"] == "Final"]
    if final and camp:
        fj = final[-1]
        venc = fj["mandante"] if (fj["gm"], fj["pm"] or 0) > (fj["gv"], fj["pv"] or 0) else fj["visitante"]
        if venc != camp:
            r["difs"].append(f"final da RSSSF: {fj['mandante']} {fj['gm']}-{fj['gv']} {fj['visitante']}, campeão oficial {camp}")
    elif camp and 1991 <= fim <= 2007:
        r["obs"].append("a RSSSF não tem o jogo da final; campeão e vice da lista oficial")
    if fim == 1976:
        r["obs"].append("temporada abandonada no meio (lista oficial: cancelada); jogos e tabela até a parada, sem campeão")
    r["art"] = F.rsssf_artilheiro(fim)
    r["jogos"] = jogos
    r["formato"] = formato(fim, len(clubes_tab), bool(playoff), r["fonte_jogos"])
    return r


def tabs_1986(tabs: list[list[dict]]) -> list[dict]:
    """1985/86: a ordem final é a dos grupos finais (título 1-4, classificação 5-8, rebaixamento 9-12)."""
    finais = [x for t in tabs for x in t if re.search(r"(?i)pool", x["secao"])]
    return sorted(finais, key=lambda x: x["pos"])


def edicao_antiga(r: dict, of: dict, finais: list[dict], usadas: set) -> dict:
    fim, camp, vice = of["fim"], of["campeao"], of["vice"]
    r["fonte_jogos"] = "Copa do Rei (RSSSF), só a final"
    r["formato"] = "mata-mata (His Majesty's League)"
    if not camp:
        r["obs"].append(f"temporada {of['situacao']} (lista oficial)")
        r["fonte_jogos"] = "nenhuma"
        return r
    f = next((x for d in (1, 0) for x in finais if x["fim"] == fim - d and id(x) not in usadas
              and {x["campeao"], x["vice"]} == {camp, vice} and x["campeao"] == camp), None)
    if f:
        usadas.add(id(f))
        r["jogos"].append({"mandante": f["campeao"], "visitante": f["vice"], "gm": f["gm"], "gv": f["gv"], "pm": f["pm"],
                           "pv": f["pv"], "prorrogacao": f["pm"] is not None, "gol_de_ouro": False, "data": None, "hora": None,
                           "rodada": None, "fase": "Final", "grupo": "", "estadio": None, "publico": None,
                           "fonte": "RSSSF (Copa do Rei)", "fonte_id": "saucuphist", "autores": "", "gols": [], "cartoes": [],
                           "obs": [f"final da Copa do Rei {f['fim'] - 1}/{f['fim'] % 100:02d} na RSSSF (\"{f['linha']}\"); a "
                                   "federação conta esse torneio como o campeonato da época; mando de campo não informado "
                                   "(campeão como mandante)"]})
        r["fases"].append(("Final", "mata_mata", "jogo_unico", ""))
    else:
        r["obs"].append("a RSSSF não tem a final com esse par de clubes (só campeão e vice da lista oficial)")
    for i, c in enumerate((camp, vice), 1):
        if c:
            r["clf"].append({"posicao": i, "clube": c, "jogos": "", "vitorias": "", "empates": "", "derrotas": "", "gols_pro": "",
                             "gols_contra": "", "pontos": "", "ajuste_pontos": "", "situacao": "campeao" if i == 1 else "",
                             "fonte": "lista oficial (relatório da federação, 2025; Wikipédia)", "observacao": "vice" if i == 2 else ""})
    return r


def formato(fim: int, n: int, playoff: bool, fonte: str) -> str:
    if fim == 1975:
        return "dois grupos de 8 e final"
    if fim == 1982:
        return "dois grupos de 10 e playoff (semifinais, 3º lugar e final)"
    if fim == 1986:
        return "dois grupos de 6 e grupos finais (título, classificação, rebaixamento)"
    if fim == 1976:
        return f"pontos corridos ({n} clubes), abandonado"
    s = f"pontos corridos, {n} clubes"
    if playoff or 1991 <= fim <= 2007:
        s += "; playoff do título entre os 4 primeiros"
    return s


# ----------------------------------------------------------------------------------------------------- saída
def escrever(nome: str, campos: list[str], linhas: list[dict]) -> None:
    with (PACOTE / f"{nome}.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for l in linhas:
            w.writerow({k: ("" if l.get(k) is None else l.get(k)) for k in campos})


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    PACOTE.mkdir(parents=True, exist_ok=True)
    so = {int(a) for a in sys.argv[1:]}
    oficiais = [o for o in lista() if not so or o["fim"] in so]
    finais, usadas = F.copa_do_rei(), set()
    res = [edicao(o, finais, usadas) for o in oficiais]
    ed_l, fa_l, pa_l, go_l, ca_l, cf_l, pu_l, ar_l, co_l = [], [], [], [], [], [], [], [], []
    usados, nomes_fonte = set(), defaultdict(lambda: defaultdict(set))
    for r in res:
        of, fim = r["of"], r["fim"]
        tp = of["temporada"]
        ed_l.append({"temporada": tp, "ano_inicio": fim - 1, "ano_fim": fim, "nome_oficial": nome_oficial(fim),
                     "num_clubes": len(r["clf"]) if fim > 1974 else "", "pontos_vitoria": r["pv"] or "",
                     "formato": r["formato"], "campeao": of["campeao"] or "", "vice": of["vice"] or "",
                     "fontes": "lista oficial (federação, 2025)" + (f"; jogos: {r['fonte_jogos']}" if r["jogos"] else "") +
                               ("; tabela: RSSSF" if r["pub"] else ""),
                     "observacao": "; ".join(r["obs"])})
        for o, (f, tipo, serie, ng) in enumerate(r["fases"], 1):
            fa_l.append({"temporada": tp, "ordem": o, "fase": f, "tipo": tipo, "num_grupos": ng, "formato_serie": serie,
                         "criterio": "pontos, saldo de gols, gols pró" if tipo != "mata_mata" else
                                     "gols no agregado, pênaltis" if serie == "ida_volta" else "prorrogação e pênaltis"})
        gols_ed = autores = 0
        jogos = sorted(r["jogos"], key=lambda j: (ORDEM_FASE[j["fase"]], j["data"] or "", j.get("rodada") or 0))
        for n, j in enumerate(jogos, 1):
            pid = f"{fim}-{n:04d}"
            obs = list(j["obs"])
            if j["prorrogacao"]:
                obs.append("prorrogação" + (" com gol de ouro" if j["gol_de_ouro"] else ""))
            if j["pm"] is not None:
                obs.append(f"{j['mandante'] if j['pm'] > j['pv'] else j['visitante']} venceu nos pênaltis por "
                           f"{max(j['pm'], j['pv'])}-{min(j['pm'], j['pv'])}")
            if j.get("perna"):
                obs.append("jogo de ida" if j["perna"] == 1 else "jogo de volta")
            pa_l.append({"id": pid, "temporada": tp, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"],
                         "data": j["data"], "hora": j["hora"], "mandante": j["mandante"], "visitante": j["visitante"],
                         "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": j["pm"],
                         "penaltis_visitante": j["pv"], "resultado_especial": "awd" if j.get("awd") else "",
                         "estadio": j["estadio"], "cidade": "",
                         "publico": j["publico"], "fonte": j["fonte"], "fonte_id": j["fonte_id"],
                         "gols_texto": j.get("gols_texto", ""), "observacao": "; ".join(obs)})
            usados |= {j["mandante"], j["visitante"]}
            gols_ed += j["gm"] + j["gv"]
            for g in j["gols"]:
                go_l.append(dict(g, partida_id=pid))
                autores += 1
            for c in j["cartoes"]:
                ca_l.append(dict(c, partida_id=pid, fonte="ESPN"))
        for c in r["clf"]:
            cf_l.append(dict(c, temporada=tp))
            usados.add(c["clube"])
        for p in r["pub"]:
            pu_l.append(dict(p, temporada=tp))
            nomes_fonte[p["clube"]]["rsssf"].add((p["nome_fonte"], fim))
        art_fonte = f"RSSSF (sau{fim}, artilheiros)"
        if not r["art"] and gols_ed and autores >= 0.95 * gols_ed:   # soma dos gols com autor (a liga, sem o playoff)
            por = defaultdict(Counter)
            for j in jogos:
                if j["fase"] == "Liga":
                    for g in j["gols"]:
                        if g["tipo"] != "contra":
                            por[g["jogador"]][g["clube"]] += 1
            if por:
                topo = max(sum(c.values()) for c in por.values())
                r["art"] = [(p, c.most_common(1)[0][0], topo) for p, c in por.items() if sum(c.values()) == topo]
                art_fonte = f"soma dos gols com autor ({autores} de {gols_ed})"
        for jog, cl, g in r["art"]:
            ar_l.append({"temporada": tp, "jogador": jog, "clube": cl, "gols": g, "fonte": art_fonte})
        co_l.append({"temporada": tp, "jogos": len(jogos), "jogos_esperados": (r["esperados"] or "") if r["jogos"] else "",
                     "tabelas_conferidas": 1 if r["pub"] and r["jogos"] and r["fonte_jogos"] and fim != 1976 else 0,
                     "tabelas_divergentes": 1 if any(d.startswith("tabela") for d in r["difs"]) else 0, "gols": gols_ed,
                     "gols_com_autor": autores, "observacao": "; ".join(r["difs"][:3])})
    # nomes do ogol e da ESPN (escudos)
    for arq in sorted((DADOS / "ogol").glob("*.json")):
        fim = int(arq.stem)
        for o in json.loads(arq.read_text(encoding="utf-8")):
            for nm in (o["mandante"], o["visitante"]):
                if clube(nm):
                    nomes_fonte[clube(nm)]["ogol"].add((nm, fim))
    for arq in sorted((DADOS / "espn").glob("*.json")):
        fim = int(arq.stem[-4:])
        for e in json.loads(arq.read_text(encoding="utf-8")):
            for nm in (e["mandante"], e["visitante"]):
                if clube(nm):
                    nomes_fonte[clube(nm)]["espn"].add((nm, fim))
    cl_l = []
    for c in sorted(usados):
        cidade, prov = CLUBES[c]
        partes = []
        for fonte, s in sorted(nomes_fonte[c].items()):
            por = defaultdict(set)
            for nm, a in s:
                por[nm].add(a)
            for nm, anos in sorted(por.items(), key=lambda x: min(x[1])):
                partes.append(f"{fonte}:{nm}:{min(anos) if min(anos) == max(anos) else f'{min(anos)}-{max(anos)}'}")
        cl_l.append({"clube": c, "regiao": prov, "cidade": cidade, "pais": "KSA", "nomes_fonte": "|".join(partes)})
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": "ksa-1", "nome": "Campeonato Saudita", "nome_curto": "Saudita", "tipo": "liga", "nivel": 1, "pais": "KSA",
        "pais_nome": "Arábia Saudita", "regiao": None, "confederacao": "AFC", "rotulo_painel": "Saudita",
        "menu_painel": "Arábia Saudita · 1ª divisão", "do_painel": "do Campeonato Saudita", "o_painel": "o Campeonato Saudita",
        "observacao": "His Majesty's League (1957/58-1973/74, mata-mata), Liga de Classificação (1974/75), Premier League "
                      "(1975/76-2006/07) e Pro League (2007/08 em diante), como o relatório oficial da federação (2025)"},
        ensure_ascii=False, indent=1), encoding="utf-8")
    escrever("paises", ["codigo", "nome", "confederacao"], [{"codigo": "KSA", "nome": "Arábia Saudita", "confederacao": "AFC"}])
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
                                      "derrotas", "gols_pro", "gols_contra", "zona"], [])
    escrever("tabelas_publicadas", ["temporada", "fase", "grupo", "posicao", "nome_fonte", "clube", "jogos", "vitorias", "empates",
                                    "derrotas", "gols_pro", "gols_contra", "pontos", "fonte"], pu_l)
    escrever("artilheiros", ["temporada", "jogador", "clube", "gols", "fonte"], ar_l)
    escrever("conferencia", ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols",
                             "gols_com_autor", "observacao"], co_l)
    print(f"{len(ed_l)} edições, {len(pa_l)} jogos, {len(go_l)} gols com autor, {len(ca_l)} cartões, {len(cl_l)} clubes")
    for r in res:
        print(r["of"]["temporada"], "|", r["fonte_jogos"], "| jogos", len(r["jogos"]), "esp", r["esperados"], "| pv", r["pv"],
              "| conf", r["conf"], "| difs", len(r["difs"]), r["difs"][:2], "|", "; ".join(r["obs"])[:80])
    json.dump([{"temporada": r["of"]["temporada"], "difs": r["difs"], "obs": r["obs"], "conf": r["conf"], "gols_dif": r["gols_dif"],
                "fonte_jogos": r["fonte_jogos"], "formato": r["formato"]} for r in res],
              open(PACOTE.parent / "conferencia_detalhe.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    import relatorio
    relatorio.main()


if __name__ == "__main__":
    main()
