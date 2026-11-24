"""Casa os jogos da RSSSF com o ogol e com a ESPN.

ogol (data/coleta/col-1/ogol/<id>.json, vazio para a Colômbia, 2005/06 em diante): rodada e data quando a RSSSF não traz, conferência
de placar e data, código e nome do clube no ogol (o nomes_fonte "ogol:" leva o agente 1 aos escudos).
ESPN (data/coleta/col-1/espn/col1_<ano>.json, 2005 em diante): hora (de Bogotá, UTC-5), estádio, cidade, público, gols com
minuto e cartões.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

from clubes_col import clube
from edicoes import PASTA_DADOS, Edicao


def _dia(s: str | None) -> int | None:
    try:
        return date.fromisoformat(s[:10]).toordinal() if s and s[:4] != "0000" else None
    except ValueError:
        return None


# ------------------------------------------------------------------------------------------------ ogol

_OGOL: dict[int, list[dict]] | None = None


def ogol_por_ano() -> dict[int, list[dict]]:
    global _OGOL
    if _OGOL is None:
        _OGOL = defaultdict(list)
        pasta = PASTA_DADOS / "ogol"
        for ed in json.loads((pasta / "edicoes.json").read_text(encoding="utf-8")):
            f = pasta / f"{ed['id']}.json"
            if f.exists():
                for g in json.loads(f.read_text(encoding="utf-8")):
                    _OGOL[ed["ano_inicio"]].append({**g, "edicao": ed["id"], "edicao_nome": ed["nome"]})
    return _OGOL


def casar(e: Edicao, jogos: list[dict], fonte: list[dict], nome_m: str, nome_v: str, id_m: str, id_v: str,
          dia_fonte, gols_fonte) -> tuple[dict[int, dict], dict[str, str]]:
    """Liga cada jogo da RSSSF (índice em `jogos`) a um jogo da fonte. Devolve (ligações, código da fonte -> clube)."""
    por_dia: dict[int, list[int]] = defaultdict(list)
    for k, j in enumerate(jogos):
        d = _dia(j["j"].data if j["j"] else None)
        if d:
            por_dia[d].append(k)
    ligado: dict[int, dict] = {}
    usado: set[int] = set()
    votos: dict[str, Counter] = defaultdict(Counter)
    resolve = lambda nome: clube(nome, e.ano_inicio) if nome else None
    # 1º passo: dia e placar
    for g in fonte:
        d = dia_fonte(g)
        gm, gv = gols_fonte(g)
        if d is None or gm is None:
            continue
        m, v = resolve(g[nome_m]), resolve(g[nome_v])
        cands = [k for dd in range(d - 2, d + 3) for k in por_dia.get(dd, []) if k not in usado
                 and (jogos[k]["j"].gm, jogos[k]["j"].gv) == (gm, gv)
                 and (m is None or jogos[k]["m"] == m) and (v is None or jogos[k]["v"] == v)]
        if m is None or v is None:
            cands = [k for k in cands if m == jogos[k]["m"] or v == jogos[k]["v"]] or (cands if len(cands) == 1 else [])
        if len(cands) == 1:
            k = cands[0]
            ligado[k] = g
            usado.add(k)
            votos[str(g[id_m])][jogos[k]["m"]] += 1
            votos[str(g[id_v])][jogos[k]["v"]] += 1
    codigo = {i: c.most_common(1)[0][0] for i, c in votos.items()}
    # 2º passo: mesmo par de clubes, até 10 dias
    for g in fonte:
        if any(x is g for x in ligado.values()):
            continue
        m, v = codigo.get(str(g[id_m])) or resolve(g[nome_m]), codigo.get(str(g[id_v])) or resolve(g[nome_v])
        d = dia_fonte(g)
        if not m or not v:
            continue
        gm, gv = gols_fonte(g)
        # CO-009 (como o CH-023): par de clubes que se repete na edição, sem data na fonte de base, só casa com placar igual
        repete = sum(1 for j in jogos if j["m"] == m and j["v"] == v) > 1
        cands = [k for k, j in enumerate(jogos) if k not in usado and j["m"] == m and j["v"] == v and j["j"]
                 and (d is None or _dia(j["j"].data) is None or abs(_dia(j["j"].data) - d) <= 10)
                 and (not repete or _dia(j["j"].data) is not None or gm is None or j["j"].gm is None
                      or (j["j"].gm, j["j"].gv) == (gm, gv))]
        if len(cands) == 1:
            ligado[cands[0]] = g
            usado.add(cands[0])
    return ligado, codigo


def ogol(e: Edicao, jogos: list[dict]) -> dict:
    fonte = [g for g in ogol_por_ano().get(e.ano_inicio, [])]
    if not fonte:
        return {"ligado": {}, "codigo": {}, "n": 0}
    ligado, codigo = casar(e, jogos, fonte, "mandante", "visitante", "mandante_id", "visitante_id",
                           lambda g: _dia(g["data"]), lambda g: (g["gols_mandante"], g["gols_visitante"]))
    # edição do ogol que corresponde a esta (a que tem mais jogos ligados)
    eds = Counter(g["edicao"] for g in ligado.values())
    ed = eds.most_common(1)[0][0] if eds else None
    return {"ligado": ligado, "codigo": codigo, "n": sum(1 for g in fonte if g["edicao"] == ed), "edicao": ed}


# ------------------------------------------------------------------------------------------------ ESPN

_ESPN: dict[int, list[dict]] = {}


def _local(g: dict) -> datetime:
    return datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")) - timedelta(hours=5)   # Colômbia: UTC-5, sem horário de verão


def espn(e: Edicao, jogos: list[dict]) -> dict:
    fonte = []
    for a in range(e.ano_inicio, e.ano_fim + 1):
        if a not in _ESPN:
            f = PASTA_DADOS / "espn" / f"col1_{a}.json"
            _ESPN[a] = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
        fonte += [g for g in _ESPN[a] if g["situacao"] in ("STATUS_FULL_TIME", "STATUS_FINAL", "STATUS_FINAL_AET", "STATUS_FINAL_PEN")]
    if not fonte:
        return {"ligado": {}, "codigo": {}}
    num = lambda x: int(x) if x not in (None, "") else None
    ligado, codigo = casar(e, jogos, fonte, "mandante", "visitante", "mandante_id", "visitante_id",
                           lambda g: _local(g).date().toordinal(), lambda g: (num(g["gols_mandante"]), num(g["gols_visitante"])))
    return {"ligado": ligado, "codigo": codigo}


def lances_espn(g: dict) -> tuple[list[dict], list[dict]]:
    """Gols e cartões da ESPN: ([{lado, jogador, minuto, acrescimo, tipo}], [{lado, jogador, minuto, acrescimo, cor}])."""
    gols, cartoes = [], []
    for l in g["lances"]:
        mi, ac = None, None
        if l.get("minuto"):
            s = l["minuto"].replace("'", "")
            p = s.split("+")
            mi = int(p[0]) if p[0].isdigit() else None
            ac = int(p[1]) if len(p) > 1 and p[1].isdigit() else None
        jog = (l["jogadores"] or [None])[0]
        if jog:   # como no CH-017: "Gastón 2Fernández" (ESPN): dígito grudado no começo de um nome sai
            jog = re.sub(r"\b\d+(?=[^\W\d_])", "", jog)
        if l["gol"] and l["lado"] not in ("home", "away"):   # CO-018: gol sem lado não entra (o lado viraria palpite)
            continue
        if l["gol"]:
            # gol contra: a ESPN marca o time que ganhou o gol
            gols.append({"lado": l["lado"], "jogador": jog, "minuto": mi, "acrescimo": ac,
                         "tipo": "contra" if l["contra"] else "penalti" if l["penalti"] else "normal"})
        elif l["amarelo"] or l["vermelho"]:
            cartoes.append({"lado": l["lado"], "jogador": jog, "minuto": mi, "acrescimo": ac, "cor": "vermelho" if l["vermelho"] else "amarelo"})
    return gols, cartoes
