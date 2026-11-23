"""Autores dos gols da Bundesliga nas páginas da RSSSF de cada temporada (tablesd/duit64.html ... duitNN.html), revisão
DE-011.

Formato: "Round 1 [Aug 24]" abre a rodada (outras datas da mesma rodada vêm em "[Aug 31]"); cada jogo é
"Schalke     2-1 K'lautern   (H.Kremers 35, Fischer 51 p - Sandberg 40)", com os gols do mandante, " - " e os do
visitante; o parêntese pode continuar nas linhas de baixo. "p" = pênalti; "o" = gol contra (fica no lado que ganhou o gol);
"Geye 54 p, 75" = dois gols do mesmo jogador. "(sent off: ...)" e "[53 Heiden (...) m/pen]" ficam de fora.

Uso como biblioteca: jogos(arq) -> [{"rodada", "nm", "nv", "gm", "gv", "gols": [(lado "m"/"v", jogador, minuto, tipo)] ou
None se a soma não fecha}]
"""
from __future__ import annotations

import html
import re
from pathlib import Path

JOGO = re.compile(r"^(\S.*?)\s+(\d+)-(\d+)\s+(\S.*?)(?:\s{2,}|\s*\()(.*)$")
TOKEN = re.compile(r"^(?:(.*?\D)\s+)?(\d+)(?:\+\d+)?\s*(p|o|pen|og)?\.?$")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


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
        tipo = {"p": "penalti", "pen": "penalti", "o": "contra", "og": "contra"}.get(m.group(3) or "", "normal")
        res.append((lado, nome, int(m.group(2)), tipo))
    return res


def jogos(arq: Path) -> list[dict]:
    linhas = texto(arq).split("\n")
    res, rodada, atual, aberto = [], None, None, ""
    for l in linhas:
        r = re.match(r"^Round (\d+)\b", l)
        if r:
            rodada, atual, aberto = int(r.group(1)), None, ""
            continue
        if rodada is None:
            continue
        if aberto:   # parêntese dos gols que continua na linha de baixo
            aberto += " " + l.strip()
            if ")" in l:
                atual["texto_gols"] = aberto
                aberto = ""
            continue
        if not l.strip() or l.startswith(" ") or l.startswith("["):
            continue
        m = JOGO.match(l)
        if not m:
            if re.match(r"^\S", l) and not re.search(r"\d-\d", l):
                rodada = None   # acabou a lista de rodadas (tabela, artilheiros...)
            continue
        resto = l[m.start(5) - 1:] if l[m.start(5) - 1:m.start(5)] == "(" else m.group(5)
        nv = m.group(4).strip()
        atual = {"rodada": rodada, "nm": m.group(1).strip(), "nv": nv, "gm": int(m.group(2)), "gv": int(m.group(3)),
                 "texto_gols": "", "gols": [] if int(m.group(2)) + int(m.group(3)) == 0 else None}
        res.append(atual)
        p = resto.find("(")
        if p >= 0 and not resto[p:].startswith("(sent off"):
            if ")" in resto[p:]:
                atual["texto_gols"] = resto[p:]
            else:
                aberto = resto[p:]
    for j in res:
        t = j.pop("texto_gols")
        if not t or j["gm"] + j["gv"] == 0:
            continue
        corpo = t[1:t.index(")")] if ")" in t else t[1:]
        partes = re.split(r"\s+-\s+|^-\s*|\s*,?\s*-\s+", corpo, maxsplit=1)
        if len(partes) == 1:
            partes = [corpo, ""] if j["gv"] == 0 else ["", corpo] if j["gm"] == 0 else partes
        if len(partes) != 2:
            continue
        gm, gv = _lado(partes[0], "m"), _lado(partes[1], "v")
        if gm is None or gv is None or len(gm) != j["gm"] or len(gv) != j["gv"]:
            continue
        j["gols"] = gm + gv
    return res
