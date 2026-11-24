"""Leitor dos jogos da FPF (data/coleta/bra-sp-1/fpf/jogos_{ano}.json, de baixar_fpf.py): casa cada jogo da FPF com o do
pacote e traz a data oficial (de 2007 em diante; achado QS-008) e, nos anos de FASES_DA_FPF, a fase e o grupo (SP-008).
A FPF usa o nome popular de hoje ("Red Bull Bragantino" em 2007): o casamento é pelo par de clubes (começo do nome sem
acento, com os apelidos de APELIDO), data até 10 dias e placar, como na conferência da revisão (revisao/QS/fpf_comparar.py).
"""
from __future__ import annotations

import json
import re
import unicodedata
from datetime import date

from edicoes import PASTA_DADOS

PASTA = PASTA_DADOS / "fpf"
DESDE = 2007
# anos em que a fase e o grupo vêm da FPF: a RSSSF de 2025 parou na 6ª rodada e a de 2024 junta a final à semifinal
FASES_DA_FPF = {"2024", "2025", "2026"}
FASE = {1: "Primeira fase", 2: "Quartas de final", 3: "Semifinal", 4: "Final"}
# nome da FPF (nome popular de hoje) -> começo do nome de exibição no pacote
APELIDO = {"osasco sporting": "oeste", "gremio novorizontino": "novorizontino", "red bull bragantino": "bragantino",
           "agua santa": "ec agua", "inter limeira": "inter de", "gremio barueri": "barueri", "audax": "osasco audax",
           "juventus saf": "juventus", "xv piracicaba": "xv de piracicaba", "sorocaba": "atletico sorocaba",
           "ua barbarense": "uniao barbarense", "portuguesa saf": "portuguesa", "ituano saf": "ituano",
           "primavera saf": "primavera", "sao bernardo fc": "sao bernardo", "comercial rp": "comercial",
           "gremio catanduvense": "catanduvense"}


def _sa(x: str) -> str:
    return unicodedata.normalize("NFKD", x or "").encode("ascii", "ignore").decode().lower().strip()


def chave(nome: str) -> str:
    n = _sa(nome)
    for k, v in APELIDO.items():
        if n.startswith(k):
            n = v
            break
    n = re.sub(r"[^a-z ]", "", n)
    return (n[:8] if n.startswith(("xv", "ec ", "sao ")) else n[:5]).strip()


def iso(d: str) -> str:
    dd, mm, aa = d.split("/")
    return f"{aa}-{mm}-{dd}"


def hora(h: str | None) -> str | None:
    m = re.match(r"(\d{1,2})h(\d{2})", h or "")
    return f"{int(m[1]):02d}:{m[2]}" if m else None


def dias(a: str | None, b: str | None) -> int:
    try:
        return abs((date.fromisoformat(a) - date.fromisoformat(b)).days)
    except (TypeError, ValueError):
        return 999


def jogos(ano) -> list[dict]:
    f = PASTA / f"jogos_{str(ano)[:4]}.json"
    if len(str(ano)) > 4 or int(str(ano)[:4]) < DESDE or not f.exists():
        return []
    return [j for j in json.loads(f.read_text(encoding="utf-8")) if j["ResultadoMandante"] is not None]


def aplicar(ano, partidas: list, nome, log: list[str]) -> None:
    """Data (e hora, quando falta) da FPF em cada jogo casado; fase e grupo nos anos de FASES_DA_FPF."""
    js = jogos(ano)
    if not js:
        return
    t = str(ano)
    usados: set[int] = set()   # id() dos jogos do pacote já casados
    trocadas, sem_par = [], []
    for j in js:
        d = iso(j["Data"])
        km, kv = chave(j["NomePopularMandante"]), chave(j["NomePopularVisitante"])
        g = (j["ResultadoMandante"], j["ResultadoVisitante"])
        cands = []
        for p in partidas:
            if p.gm is None or id(p) in usados:
                continue
            cm, cv = chave(nome(p.mandante)), chave(nome(p.visitante))
            if {cm, cv} != {km, kv} or dias(p.data, d) > 10:
                continue
            gp = (p.gm, p.gv) if cm == km else (p.gv, p.gm)
            cands.append((dias(p.data, d), gp != g, p))
        if not cands:
            sem_par.append(j)
            continue
        _, _, p = min(cands, key=lambda x: x[:2])
        usados.add(id(p))
        if p.data != d:
            trocadas.append(f"{nome(p.mandante)} x {nome(p.visitante)} {p.data} -> {d}")
            p.data = d
        p.hora = p.hora or hora(j["Horario"])
        if t in FASES_DA_FPF:
            p.fase = FASE[j["NumFase"]]
            p.grupo = f"Grupo {j['Grupo']}" if j["NumFase"] == 1 and re.fullmatch(r"[A-H]", j["Grupo"] or "") else ""
    if trocadas:
        log.append(f"{t}: data da FPF (oficial) em {len(trocadas)} jogos (QS-008): " + "; ".join(trocadas))
    if sem_par:
        log.append(f"{t}: {len(sem_par)} jogos da FPF sem par no pacote (ex.: {sem_par[0]['NomePopularMandante']} x "
                   f"{sem_par[0]['NomePopularVisitante']}, {sem_par[0]['Data']}, fase {sem_par[0]['Fase']})")
    if t in FASES_DA_FPF:
        sobra = [p for p in partidas if id(p) not in usados and not p.especial]
        if sobra:
            raise ValueError(f"{t}: {len(sobra)} jogos sem par na FPF, sem fase: "
                             f"{[(nome(p.mandante), nome(p.visitante), p.data) for p in sobra[:5]]}")
