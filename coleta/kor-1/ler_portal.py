"""Lê o boletim de um jogo da K League baixado do portal oficial (baixar_portal.py).

A página traz o jogo em JSON (variáveis jsonResultData e basicMatchInfoJson). Os blocos de jsonResultData mudam de ordem
entre as épocas, então cada um é achado pelas chaves:
- dados do jogo (Meet_Year, Game_Date, Game_Time, Field_Name, Audiance_qty, refree_Name*);
- clubes (Home_Team / Away_Team: o código do clube no portal, K01, K04..., e o nome de HOJE);
- totais (H_Goal_Qty / A_Goal_Qty, H_Warn_Qty, H_Exit_Qty: gols, amarelos e vermelhos de cada lado);
- linha do tempo (Half_Type, Min_Seq, Team_Id, Action_Type): "G" gol, "Y" amarelo, "R" vermelho, "Z" segundo amarelo
  (expulsão: "(두 번째 경고)"), "C" substituição, "P" (pênalti, não é gol); Remark1 = "número nome" (sem número: técnico
  ou comissão), Remark2 = "(도18)" (assistência do 18), "(자책)" (gol contra: o Team_Id é o do clube que ganhou o gol),
  "(PK)"...;
- gols (G_NAME, Player_id, Self_Goal_YN), com o código do jogador (para o nome em inglês do site oficial);
- disputa de pênaltis (Player_Name, Gain_YN), quando houve.

Minuto: Half_Type 1 = 1º tempo (minuto como está), 2 = 2º tempo (45 + minuto), 3 e 4 = prorrogação (90 + e 105 +).

Uso como biblioteca: boletim(ano, meet_seq, game_id) -> dict; para ver: python coleta/kor-1/ler_portal.py <ano> <meet> <game>
"""
from __future__ import annotations

import gzip
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "kleague-asia" / "jogos"
BASE_MIN = {1: 0, 2: 45, 3: 90, 4: 105}


def _var(p: str, nome: str):
    m = re.search(r"var " + nome + r"\s*=\s*", p)
    if not m:
        return None
    return json.JSONDecoder().raw_decode(p[m.end():])[0]


def _bloco(blocos: list, chave: str) -> list:
    for b in blocos:
        if b and isinstance(b, list) and isinstance(b[0], dict) and chave in b[0]:
            return b
    return []


def _jogador(remark: str) -> tuple[str | None, str]:
    """"20 정종선" -> ("20", "정종선")."""
    m = re.match(r"^\s*(\d+)?\s*(.*?)\s*$", remark or "")
    return (m.group(1), m.group(2)) if m else (None, remark or "")


def existe(ano: str, meet: str, game: str) -> bool:
    return (CACHE / f"{ano}_{meet}_{game}.html.gz").exists()


@lru_cache(maxsize=None)
def boletim(ano: str, meet: str, game: str) -> dict:
    p = gzip.decompress((CACHE / f"{ano}_{meet}_{game}.html.gz").read_bytes()).decode("utf-8", "ignore")
    blocos = _var(p, "jsonResultData") or []
    info = _var(p, "basicMatchInfoJson") or (_bloco(blocos, "Game_Date") or [{}])[0]
    clubes = (_bloco(blocos, "Home_Team") or [{}])[0]
    tot = next((b[0] for b in blocos if b and isinstance(b[0], dict) and "H_Goal_Qty" in b[0] and "H_Player_Name" not in b[0]), {})
    linha = _bloco(blocos, "Action_Type")
    gols_lista = [g for g in _bloco(blocos, "G_NAME") if g.get("G_NAME")]
    pso = [b for b in blocos if b and isinstance(b[0], dict) and "Gain_YN" in b[0]]
    j = {"ano": ano, "meet": meet, "game": game, "competicao": info.get("Meet_Name"),
         "data": (info.get("Game_Date") or "").replace("/", "-") or None, "hora": info.get("Game_Time") or None,
         "estadio": info.get("Field_Name") or None,
         "publico": int(str(info["Audiance_qty"]).replace(",", "")) if str(info.get("Audiance_qty") or "").replace(",", "").isdigit() else None,
         "arbitro": info.get("refree_Name2") or info.get("refree_Name1") or None,
         "mandante_id": clubes.get("Home_Team"), "mandante_hoje": clubes.get("H_team_name"),
         "visitante_id": clubes.get("Away_Team"), "visitante_hoje": clubes.get("A_team_name"),
         "gm": tot.get("H_Goal_Qty"), "gv": tot.get("A_Goal_Qty"),
         "amarelos": (tot.get("H_Warn_Qty"), tot.get("A_Warn_Qty")), "vermelhos": (tot.get("H_Exit_Qty"), tot.get("A_Exit_Qty")),
         "tempos": sorted({x.get("Half_Type") for x in linha if x.get("Half_Type")}),
         "gols": [], "cartoes": [], "penaltis": None}
    ids = {g.get("G_NAME"): g.get("Player_id") for g in gols_lista}
    for x in linha:
        tipo = x.get("Action_Type")
        if tipo not in ("G", "Y", "R", "Z"):
            continue
        lado = "m" if x.get("Team_Id") == j["mandante_id"] else "v" if x.get("Team_Id") == j["visitante_id"] else None
        num, nome = _jogador(x.get("Remark1", ""))
        meio = int(x.get("Half_Type") or 1)
        mi = x.get("Min_Seq")
        minuto = BASE_MIN.get(meio, 0) + int(mi) if str(mi).isdigit() else None
        disp = str(x.get("Display_Time") or "")
        acr = int(m.group(1)) if (m := re.search(r"\+(\d+)", disp)) else None
        if tipo == "G":
            r2 = x.get("Remark2") or ""
            contra = "자책" in r2
            j["gols"].append({"lado": lado, "jogador": nome, "numero": num, "minuto": minuto, "acrescimo": acr, "meio": meio,
                              "tipo": "contra" if contra else "penalti" if re.search(r"PK|페널티", r2) else "normal",
                              "obs": r2, "player_id": ids.get(nome)})
        else:
            j["cartoes"].append({"lado": lado, "jogador": nome, "numero": num, "minuto": minuto, "acrescimo": acr, "meio": meio,
                                 "cor": "amarelo" if tipo == "Y" else "vermelho", "obs": x.get("Remark2") or ""})
    if pso and any(p_.get("Player_Name") or p_.get("Name") for b in pso for p_ in b):   # 1º bloco: mandante
        conv = [sum(1 for p_ in b if p_.get("Gain_YN") == "Y") for b in pso[:2]]
        j["penaltis"] = tuple(conv) if len(conv) == 2 else None
    return j


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(boletim(*sys.argv[1:4]), ensure_ascii=False, indent=1))
