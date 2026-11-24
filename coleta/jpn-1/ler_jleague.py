"""Lê os jogos da J1 (1993-2025) baixados do J.League Data Site (baixar_jleague.py): a lista de cada ano
(data/coleta/jpn-1/jleague/lista_<ano>.json) e a página de cada jogo (data/cache/jleague-asia/jogos/<id>.html.gz).

Da página ("Scoresheet"), em inglês:
- nomes completos dos dois clubes, placar final (com a prorrogação) e placar por tempo ("Extra 1st"/"Extra 2nd" quando
  houve prorrogação; de 1993 a 2002 ela acabava no primeiro gol, a morte súbita ou "V-goal");
- disputa de pênaltis ("Penalty", 1993-1998, quando a prorrogação terminava empatada);
- autores dos gols com minuto ("Own-Goal" = gol contra, sem o nome do jogador; o gol conta para o lado em que aparece);
- cartões ("Cautions" = amarelo, "Ejections" = vermelho);
- data, hora, estádio, público e árbitro.

Uso como biblioteca: jogos(ano) -> list[dict]; para ver: python coleta/jpn-1/ler_jleague.py [ano] [id]
"""
from __future__ import annotations

import gzip
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
LISTAS = RAIZ / "data" / "coleta" / "jpn-1" / "jleague"
CACHE = RAIZ / "data" / "cache" / "jleague-asia" / "jogos"


def _limpo(v: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v.replace("&nbsp;", " ")))).strip()


def _minuto(v: str) -> tuple[int | None, int | None]:
    """"89'" -> (89, None); "90'+2" -> (90, 2); "04'" -> (4, None)."""
    m = re.match(r"^(\d+)'?(?:\+(\d+))?'?$", v.strip())
    if not m:
        return None, None
    return int(m.group(1)), int(m.group(2)) if m.group(2) else None


def _linhas_lado(seg: str) -> list[tuple[str, str]]:
    """Linhas (jogador, minuto) de uma tabela de gols: à esquerda "nome | 77'", à direita "32' | nome"."""
    saida = []
    for tr in re.findall(r"<tr>(.*?)</tr>", seg, flags=re.S):
        cel = [_limpo(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
        cel = [c.replace("　", " ").strip() for c in cel]
        mins = [c for c in cel if re.match(r"^\d+'?(\+\d+)?'?$", c) and "'" in c]   # "89'", "90'+2"
        nomes = [c for c in cel if c and c not in mins]
        if mins and nomes:
            saida.append((nomes[0], mins[0]))
    return saida


def pagina(id_jogo: str) -> dict:
    t = gzip.decompress((CACHE / f"{id_jogo}.html.gz").read_bytes()).decode("utf-8", "ignore")
    j: dict = {"id": id_jogo}
    j["titulo"] = _limpo(m.group(1)) if (m := re.search(r'<p class="t-txt">(.*?)</p>', t, re.S)) else ""
    j["mandante"] = _limpo(re.search(r'id="team-name-l"[^>]*>(.*?)</th>', t, re.S).group(1))
    j["visitante"] = _limpo(re.search(r'id="team-name-r"[^>]*>(.*?)</th>', t, re.S).group(1))
    placar = re.findall(r'<td class="score"[^>]*>\s*(\d+)\s*</td>', t)
    j["gm"], j["gv"] = int(placar[0]), int(placar[1])
    tempos = re.search(r'<td class="time">(.*?)</td>', t, re.S)
    j["prorrogacao"] = bool(tempos and "Extra" in tempos.group(1))
    por_tempo = re.findall(r'<dd class="left-area">\s*(\d+)\s*</dd>\s*<dt[^>]*>\s*([^<]+?)\s*</dt>\s*<dd class="right-area">\s*(\d+)', t)
    j["tempos"] = [(nome, int(a), int(b)) for a, nome, b in por_tempo]
    pen = re.search(r'<td class="left-area">\s*(\d+)\s*</td>\s*<th>Penalty</th>\s*<td class="right-area">\s*(\d+)\s*</td>', t)
    j["pen_m"], j["pen_v"] = (int(pen.group(1)), int(pen.group(2))) if pen else (None, None)
    gols = []
    m = re.search(r'<td class="left-area">\s*<table>(.*?)</table>\s*</td>\s*<th>Scorers</th>\s*<td class="right-area">\s*<table>(.*?)</table>', t, re.S)
    if m:
        for lado, seg in (("m", m.group(1)), ("v", m.group(2))):
            for nome, mi in _linhas_lado(seg):
                minuto, acr = _minuto(mi)
                gols.append({"lado": lado, "jogador": "" if nome == "Own-Goal" else nome, "minuto": minuto, "acrescimo": acr,
                             "tipo": "contra" if nome == "Own-Goal" else "normal"})
    j["gols"] = gols
    cartoes = []
    # o comentário antes do título não pode atravessar outros blocos ([^>]*: senão pega titulares como cartão)
    for lado, rotulo, corpo in re.findall(r'<div class="two-column-table-box-(l|r)">\s*(?:<!--[^>]*-->\s*)?<h4[^>]*>\s*(Cautions|Ejections)\s*</h4>(.*?)</table>', t, re.S):
        for tr in re.findall(r"<tr>(.*?)</tr>", corpo, flags=re.S):
            nome = _limpo(m.group(1)) if (m := re.search(r'<td class="name">(.*?)</td>', tr, re.S)) else ""
            mi = _limpo(m.group(1)) if (m := re.search(r'<td class="time">(.*?)</td>', tr, re.S)) else ""
            minuto, acr = _minuto(mi)
            if nome:
                cartoes.append({"lado": "m" if lado == "l" else "v", "jogador": nome, "minuto": minuto, "acrescimo": acr,
                                "cor": "amarelo" if rotulo == "Cautions" else "vermelho"})
    j["cartoes"] = cartoes
    info = re.search(r"<th>Date</th>.*?<tbody>\s*<tr>(.*?)</tr>", t, re.S)
    cab = re.findall(r"<th>([^<]+)</th>", t[info.start():info.start() + 600]) if info else []
    val = [_limpo(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", info.group(1), re.S)] if info else []
    d = dict(zip(cab, val))
    j["data"] = datetime.strptime(d["Date"], "%d %B %Y").strftime("%Y-%m-%d") if d.get("Date") else None
    j["hora"] = d.get("Kick-off") or None
    j["estadio"] = d.get("Stadium") or None
    j["publico"] = int(d["Attendance"].replace(",", "")) if re.match(r"^[\d,]+$", d.get("Attendance") or "") else None
    j["arbitro"] = _limpo(m.group(1)) if (m := re.search(r"<dt>Referee</dt>\s*<dd>(.*?)</dd>", t, re.S)) else None
    return j


def lista(ano: int) -> list[dict]:
    return json.loads((LISTAS / f"lista_{ano}.json").read_text(encoding="utf-8"))


def jogos(ano: int) -> list[dict]:
    """Jogos do ano: a linha da lista (torneio, rodada, abreviações) mais o que a página traz."""
    saida = []
    for x in lista(ano):
        j = pagina(x["id"]) if x["id"] and (CACHE / f"{x['id']}.html.gz").exists() else {"id": x["id"], "sem_pagina": True}
        j["lista"] = x
        saida.append(j)
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) > 2:
        print(json.dumps(pagina(sys.argv[2]), ensure_ascii=False, indent=1))
    else:
        for j in jogos(int(sys.argv[1]))[:5]:
            print(json.dumps({k: v for k, v in j.items() if k != "lista"}, ensure_ascii=False))
