"""Jogos e tabelas de cada fonte da liga saudita, já com o nome de exibição dos clubes (clubes_ksa.py), no formato que o
importar usa.

- rsssf_liga(fim) / rsssf_playoff(fim): jogos da fase de liga e do playoff do título da página da RSSSF do ano;
- rsssf_tabelas(fim): as tabelas da liga da página (uma por grupo, ou a final), na ordem, sem a do meio do campeonato e
  sem as repetidas;
- rsssf_artilheiro(fim): o 1º da lista de artilheiros da página, quando há;
- ogol(fim): jogos do calendário do ogol (só a fase de liga: R1, R2...);
- espn(fim): jogos da ESPN com os lances (2022/23 em diante);
- copa_do_rei(): finais da Copa do Rei (saucuphist.html), para as edições de 1957/58 a 1973/74.
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import ler_rsssf  # noqa: E402
from clubes_ksa import clube  # noqa: E402
from edicoes import fase_playoff  # noqa: E402
from explicacoes import OGOL_CORRIGE  # noqa: E402

DADOS = AQUI.parent.parent / "data" / "coleta" / "ksa-1"


def _c(nome: str) -> str:
    c = clube(nome)
    if c is None:
        raise SystemExit(f"clube sem regra: {nome!r} (acrescente em clubes_ksa.REGRAS)")
    return c


def _penaltis(obs: str) -> tuple[int | None, int | None]:
    m = re.search(r"(\d+)\s*-\s*(\d+)\s*(?:pen|p\b)|(\d+)TK(\d+)", obs or "")
    if not m:
        return None, None
    a, b = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
    return int(a), int(b)


def _jogo(j: dict, fonte: str, fase: str, fim: int) -> dict:
    pm, pv = _penaltis(j["obs"])
    rod = re.match(r"(?i)round\s+(\d+)", j["secao"])
    return {"mandante": _c(j["mandante"]), "visitante": _c(j["visitante"]), "gm": j["gm"], "gv": j["gv"], "pm": pm, "pv": pv,
            "prorrogacao": bool(re.search(r"(?i)aet|asdet|extra", j["obs"])),
            "gol_de_ouro": bool(re.search(r"(?i)asdet|golden", j["obs"])), "data": j["data"], "hora": None,
            "rodada": int(rod.group(1)) if rod else None, "fase": fase, "grupo": "", "estadio": None, "publico": None,
            "fonte": fonte, "fonte_id": f"sau{fim}", "autores": j.get("autores", ""), "obs_fonte": j["obs"],
            "perna": j.get("perna"), "secao": j["secao"], "gols": [], "cartoes": [], "obs": [],
            "awd": j.get("awd", False), "campo": j.get("campo")}


def rsssf_liga(fim: int) -> list[dict]:
    p = ler_rsssf.pagina(fim)
    return [_jogo(j, "RSSSF", "Liga", fim) for j in p["jogos"] if not j["fora"] and fase_playoff(j["secao"]) is None
            and not re.search(r"(?i)relegation|promotion|play-?off|\d{2}\s", j["secao"]) or
            (not j["fora"] and re.match(r"(?i)round|group", j["secao"]))]


def rsssf_playoff(fim: int) -> list[dict]:
    p = ler_rsssf.pagina(fim)
    saida = []
    for j in p["jogos"]:
        if j["fora"] or re.match(r"(?i)round|group", j["secao"]):
            continue
        f = fase_playoff(j["secao"])
        if f:
            saida.append(_jogo(j, "RSSSF", f, fim))
    # pênaltis anotados nas duas pernas de um confronto de ida e volta: valem só na 2ª
    por_par = {}
    for j in saida:
        por_par.setdefault((j["fase"], frozenset((j["mandante"], j["visitante"]))), []).append(j)
    for lst in por_par.values():
        if len(lst) == 2 and lst[0]["pm"] is not None and lst[1]["pm"] is not None:
            lst[0]["pm"] = lst[0]["pv"] = None
    return saida


def rsssf_tabelas(fim: int) -> list[list[dict]]:
    """Tabelas da liga na ordem da página; uma nova começa quando a posição volta a 1."""
    tabs = []
    for x in ler_rsssf.pagina(fim)["tabelas"]:
        if x["fora"]:
            continue
        if x["pos"] == 1 or not tabs:
            tabs.append([])
        tabs[-1].append(dict(x, clube=_c(x["nome"])))
    # fora a tabela do meio do campeonato e as repetidas (a página repete a final no fim)
    saida, vistas = [], set()
    for tab in tabs:
        k = tuple((x["clube"], x["pontos"]) for x in tab)
        if re.search(r"(?i)halfway|half-?time|first half|1st half", tab[0]["secao"]) or k in vistas:
            continue
        vistas.add(k)
        saida.append(tab)
    return saida


def rsssf_artilheiro(fim: int) -> list[tuple[str, str, int]]:
    """[(jogador, clube, gols)] do topo da lista de artilheiros da página (os empatados no 1º lugar)."""
    t = ler_rsssf.texto(fim)
    i = re.search(r"(?i)top\s*-?scorers?", t)
    if not i:
        return []
    saida = []
    for linha in t[i.end():].split("\n")[1:25]:
        m = re.match(r"^\s*(?:\d+\.)?\s*([A-Z][^()\d]+?)\s*\(([^)]+)\)\s+(\d+)", linha)
        if m:
            cl = clube(re.split(r"\s+-\s+", m.group(2))[0])
            if cl:
                saida.append((m.group(1).strip(), cl, int(m.group(3))))
        elif saida and not linha.strip():
            break
    if not saida:
        return []
    topo = max(g for _, _, g in saida)
    return [x for x in saida if x[2] == topo]


def ogol(fim: int) -> list[dict]:
    arq = DADOS / "ogol" / f"{fim}.json"
    if not arq.exists():
        return []
    saida = []
    for o in json.loads(arq.read_text(encoding="utf-8")):
        if not re.match(r"^R\d+$", o.get("fase") or "") or o.get("gols_mandante") is None:
            continue
        cor = OGOL_CORRIGE.get(str(o["id"]), {})
        o = dict(o, mandante=cor.get("mandante", o["mandante"]), visitante=cor.get("visitante", o["visitante"]),
                 gols_mandante=cor.get("gm", o["gols_mandante"]), gols_visitante=cor.get("gv", o["gols_visitante"]))
        saida.append({"mandante": _c(o["mandante"]), "visitante": _c(o["visitante"]), "gm": o["gols_mandante"],
                      "gv": o["gols_visitante"], "pm": None, "pv": None, "prorrogacao": False, "gol_de_ouro": False,
                      "data": o["data"], "hora": None, "rodada": o.get("rodada"), "fase": "Liga", "grupo": "",
                      "estadio": None, "publico": None, "fonte": "ogol", "fonte_id": f"ogol:{o['id']}", "autores": "",
                      "obs_fonte": "", "perna": None, "secao": o.get("fase"), "gols": [], "cartoes": [],
                      "obs": [f"corrigido: {cor['motivo']}"] if cor else []})
    return saida


def espn(fim: int) -> dict:
    """{(mandante, visitante, data em Riade): jogo da ESPN}."""
    arq = DADOS / "espn" / f"ksa1_{fim}.json"
    saida = {}
    if not arq.exists():
        return saida
    for e in json.loads(arq.read_text(encoding="utf-8")):
        m, v = clube(e["mandante"]), clube(e["visitante"])
        if not (m and v) or e["situacao"] != "STATUS_FULL_TIME":
            continue   # (amistoso com clube de fora que a ESPN pôs na liga: Al-Raed x Al-Wehdat, 2022)
        local = datetime.fromisoformat(e["data_hora"].replace("Z", "+00:00")) + timedelta(hours=3)
        saida[(m, v, local.date().isoformat())] = dict(e, hora_local=local.strftime("%H:%M"))
    return saida


def copa_do_rei() -> list[dict]:
    """Finais da Copa do Rei de 1956/57 a 1973/74: [{temporada, campeao, vice, gm, gv, pm, pv, linha}]."""
    b = (DADOS / "rsssf" / "saucuphist.html").read_bytes()
    t = html.unescape(re.sub(r"<[^>]+>", "", b.decode("latin-1")))
    t = t[t.find("Kings Cup"):t.find("Crown Prince Cup")]
    saida = []
    for linha in t.split("\n"):
        m = re.match(r"^(\d{4})/(\d{2})\s+(Al-\w+)\s+(\d+)-(\d+)\s+(Al-\w+)\s*(.*)$", linha.strip())
        if m:
            pen = re.search(r"\[(\d+)-(\d+) pen\]", m.group(7))
            saida.append({"fim": int(m.group(1)) + 1, "campeao": _c(m.group(3)), "vice": _c(m.group(6)), "gm": int(m.group(4)),
                          "gv": int(m.group(5)), "pm": int(pen.group(1)) if pen else None,
                          "pv": int(pen.group(2)) if pen else None, "linha": linha.strip()})
    return saida
