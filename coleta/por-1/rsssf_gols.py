"""Autores dos gols do Campeonato Português nas páginas da RSSSF de cada temporada (tablesp/port00.html ... port06.html,
1999/00 a 2005/06), revisão PT-019.

Formato: "Round 1" abre a rodada; "[Aug 18]" é a data; cada jogo é "Beira Mar       2-4 Boavista", e a linha de baixo, com
recuo, traz os autores entre colchetes, os do mandante, ";" e os do visitante (pode continuar em mais linhas):
"  [Oscar Morais 89pen, Ricardo Sousa 90; Elpidio Silva 39, Jose Rogerio 55, Carlos Duda 58, 78]". "pen" = pênalti; "og" =
gol contra (fica no lado que ganhou o gol); "Carlos Duda 58, 78" = dois gols do mesmo jogador.

Uso como biblioteca: jogos(arq) -> [{"rodada", "nm", "nv", "gm", "gv", "gols": [(lado, jogador, minuto, tipo)] ou None}]
"""
from __future__ import annotations

import html
import re
from pathlib import Path

JOGO = re.compile(r"^(\S.*?)\s+(\d+)-?(\d)?\s+(\S.*?)\s*$")
TOKEN = re.compile(r"^(?:(.*?\D)\s+)?(\d+)(?:\+\d+)?\s*(pen|og|p|o)?\.?$")


def texto(arq: Path) -> str:
    # o travessão do placar vem em cp1252 ("1\x960") nas páginas de 2004/05 em diante
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "").replace("\x96", "-")


def _lado(s: str, lado: str) -> list[tuple] | None:
    res, nome = [], None
    for tok in [x.strip() for x in s.split(",")]:
        if not tok:
            continue
        m = TOKEN.match(tok)
        if not m:
            return None
        if m.group(1):
            nome = m.group(1).strip()
        if not nome:
            return None
        tipo = {"pen": "penalti", "p": "penalti", "og": "contra", "o": "contra"}.get(m.group(3) or "", "normal")
        res.append((lado, nome, int(m.group(2)), tipo))
    return res


def jogos(arq: Path) -> list[dict]:
    res, rodada, atual, aberto = [], None, None, ""
    for l in texto(arq).split("\n"):
        r = re.match(r"^Round (\d+)\b", l)
        if r:
            rodada, atual, aberto = int(r.group(1)), None, ""
            continue
        if rodada is None:
            continue
        s = l.strip()
        if aberto:
            aberto += " " + s
            if "]" in s:
                atual["texto"] = aberto
                aberto = ""
            continue
        if l.startswith(" ") and s.startswith("[") and atual is not None:
            if "]" in s:
                atual["texto"] = s
            else:
                aberto = s
            continue
        if not s or s.startswith("["):
            continue
        m = JOGO.match(l)
        if not m:
            if not re.search(r"\d-?\d", l):
                rodada = None
            continue
        if m.group(3) is None:   # "21": placar sem hífen
            if len(m.group(2)) != 2:
                continue
            gm_, gv_ = int(m.group(2)[0]), int(m.group(2)[1])
        else:
            gm_, gv_ = int(m.group(2)), int(m.group(3))
        atual = {"rodada": rodada, "nm": m.group(1).strip(), "nv": m.group(4).strip(), "gm": gm_, "gv": gv_, "texto": "",
                 "gols": [] if gm_ + gv_ == 0 else None}
        res.append(atual)
    for j in res:
        t = j.pop("texto")
        if not t or j["gm"] + j["gv"] == 0:
            continue
        corpo = t[1:t.index("]")] if "]" in t else t[1:]
        partes = corpo.split(";")
        if len(partes) == 1:
            partes = [corpo, ""] if j["gv"] == 0 else ["", corpo] if j["gm"] == 0 else partes
        if len(partes) != 2:
            continue
        gm, gv = _lado(partes[0], "m"), _lado(partes[1], "v")
        if gm is None or gv is None or len(gm) != j["gm"] or len(gv) != j["gv"]:
            continue
        j["gols"] = gm + gv
    return res
