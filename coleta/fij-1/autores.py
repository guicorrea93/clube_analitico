"""Separa os autores dos gols do texto da RSSSF ("Mark Elrick 78', 95' - Jeremy Seales 1'") em gols, um por linha.

Formatos vistos:
- mandante e visitante separados por " - " (um lado vazio quando só um time marcou: "- G Gray", "S Elliot, M McGarry -");
- 2000-2007/08: minuto depois do nome, com ou sem apóstrofo ("T Butterfield 48", "Keryn Jordan 60'", "45+2'"), e os
  minutos seguintes do mesmo jogador só com o número ("Ian Robinson 7', 59'");
- 1993-1996/97 (páginas nz93, nz95, nz96, nz97): número depois do nome é a QUANTIDADE de gols ("Halford 4", "D McLennan 2");
- gol contra: "og", "OG", "Own Goal" (sozinho ou depois do nome/minuto); pênalti: "pen", "p" ("89p").

Só devolve os gols quando a soma de cada lado bate com o placar (senão, None: o texto fica em gols_texto).

Uso: gols(texto, gm, gv, pagina) -> ([casa], [fora]) com (jogador, minuto, acréscimo, tipo), ou None.
"""
from __future__ import annotations

import re

CONTAGEM: set[str] = set()   # páginas em que o número depois do nome é a quantidade de gols
_MIN = r"(?P<min>\d{1,3})(?:\s*\+\s*(?P<acr>\d{1,2}))?\s*'?\+?"
_TIPO = r"(?:\s*(?P<tipo>pen\.?|p|og|o\.g\.|own goal))?"


def _lado(txt: str, contagem: bool) -> list[tuple[str, int | None, int | None, str]] | None:
    out: list[tuple[str, int | None, int | None, str]] = []
    txt = txt.strip().strip(",;")
    if not txt:
        return out
    ultimo = None
    # vírgula esquecida entre um minuto e o próximo nome ("A Brown 20, 24 J Campbell 58"; "Hogg 69' Daniel Ellensohn 79'")
    txt = re.sub(r"(\d'?)\s+(?=[A-Z][a-z]*\.?\s|[A-Z][a-z]+'?[a-z]+\s)(?!OG\b|Own\b)", r"\1, ", txt)
    for item in re.split(r"\s*[,;]\s*", txt):
        item = item.strip().strip(".").replace("(pen)", "pen").replace("+1)", "+1")
        if not item:
            continue
        if re.fullmatch(r"\(?pen\.?\)?", item, re.I) and out:   # "pen." sozinho: o gol anterior foi de pênalti
            out[-1] = out[-1][:3] + ("penalti",)
            continue
        if item == "?":
            return None
        item = re.sub(r"\s+\?$", "", item)   # "David Johnston ?": minuto desconhecido
        mm = re.fullmatch(_MIN + r"\s*(?:og|own goal)", item, re.I)
        if mm and not contagem:   # "12' OG"
            out.append(("", int(mm.group("min")), int(mm.group("acr")) if mm.group("acr") else None, "contra"))
            ultimo = None
            continue
        mo = re.fullmatch(r"(?:og|o\.g\.|own goal)(?:\s+" + _MIN + r")?", item, re.I)
        if mo:   # gol contra sem o nome de quem fez
            out.append(("", int(mo.group("min")) if mo.group("min") and not contagem else None,
                        int(mo.group("acr")) if mo.group("acr") else None, "contra"))
            ultimo = None
            continue
        ms = re.fullmatch(_MIN + _TIPO, item, re.I)
        if ms and ultimo is not None and not contagem:   # "95'": outro gol do mesmo jogador
            out.append((ultimo, int(ms.group("min")), int(ms.group("acr")) if ms.group("acr") else None, _tipo(ms.group("tipo"))))
            continue
        mn = re.fullmatch(r"(?P<nome>[^\d]+?)\s*" + _MIN + _TIPO, item, re.I)
        if mn and re.search(r"[A-Za-z]{2}", mn.group("nome")):
            nome = re.sub(r"\s+(og|pen)$", "", mn.group("nome").strip(), flags=re.I)
            tipo = _tipo(mn.group("tipo") or (re.search(r"\s(og|pen)$", mn.group("nome").strip(), re.I) or [None, None])[1])
            if contagem:
                n = int(mn.group("min"))
                if n > 9 or mn.group("acr"):
                    return None
                out += [(nome, None, None, tipo)] * n
            else:
                out.append((nome, int(mn.group("min")), int(mn.group("acr")) if mn.group("acr") else None, tipo))
            ultimo = nome
            continue
        mp = re.fullmatch(r"(?P<nome>[^\d]+?)(?:\s+(?P<tipo>pen\.?|og|o\.g\.))?", item, re.I)
        if mp and re.search(r"[A-Za-z]{2}", mp.group("nome")):
            out.append((mp.group("nome").strip(), None, None, _tipo(mp.group("tipo"))))
            ultimo = mp.group("nome").strip()
            continue
        return None
    return out


def _tipo(t: str | None) -> str:
    t = (t or "").lower().strip(".")
    return "penalti" if t in ("pen", "p") else "contra" if t in ("og", "o.g", "own goal") else "normal"


def gols(texto: str, gm: int | None, gv: int | None, pagina: str):
    if not texto or gm is None or gv is None:
        return None
    t = texto.replace("–", "-").strip().strip("[]").strip()
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\s*Referee:.*$", "", t)                   # árbitro colado no fim da linha dos autores
    t = re.sub(r"(\d)'\s*\+(\d{1,2})\)", r"\1+\2'", t)       # "90' +1)" = 90+1'
    contagem = pagina in CONTAGEM
    if re.search(r"(^|\s)-(\s|$)", t):
        partes = re.split(r"(?:^|\s)-(?:\s|$)", t, maxsplit=1)
        casa, fora = _lado(partes[0], contagem), _lado(partes[1], contagem)
    elif gv == 0:
        casa, fora = _lado(t, contagem), []
    elif gm == 0:
        casa, fora = [], _lado(t, contagem)
    else:
        return None
    if casa is None or fora is None or len(casa) != gm or len(fora) != gv:
        return None
    return casa, fora
