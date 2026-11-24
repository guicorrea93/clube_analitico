"""Autores dos gols como a RSSSF escreve -> lista de gols por lado.

Formatos vistos nas páginas argentinas e uruguaias:
- "Denda, Quadri; L.Monti, Torres"                 (mandante; visitante)
- "Carignano, Graf - Villa (2), J. González"       (mandante - visitante)
- "11' J.L. Calderón - 7' R. Rojas (o.g.)"         (minuto antes do nome)
- "Pizzuti 35, 56, Tolosa 78"                      (minutos depois do nome)
- "Cano]     [Silva"                                (duas colunas, uma por lado)
- "Sava (2, 1 pen)", "Drago o/g", "Lagorio (pen)"  (quantidade, pênalti, gol contra)
O gol contra aparece do lado de quem ganhou o gol. Linha de árbitro e público ("Ref. X; tickets 6,900") não é autor.

Uso: separar(texto, gols_mandante, gols_visitante) -> ([gol], [gol]) ou None quando a soma não bate.
"""
from __future__ import annotations

import re

_CONTRA = re.compile(r"\(?\b(o\.?\s?g\.?|o/g|own goal|og|e\.?c\.?|autogol|en contra)\b\)?", re.I)
_PEN = re.compile(r"\(?\b(pen\.?|p\.?|pk|penalty|penal)\)?$", re.I)


def publico(texto: str) -> int | None:
    m = re.search(r"(?:tickets|att(?:endance)?\.?|público|espectadores)\s*:?\s*~?([\d.,]{3,})", texto, re.I)
    return int(re.sub(r"\D", "", m.group(1))) if m else None


def eh_autores(texto: str) -> bool:
    return not re.match(r"^\s*(ref\.?|referee|árbitro)\b", texto, re.I) and not re.search(r"tickets|attendance", texto, re.I)


def _partes(lado: str) -> list[str]:
    """Separa por vírgula fora dos parênteses."""
    saida, nivel, atual = [], 0, ""
    for ch in lado:
        if ch == "(":
            nivel += 1
        elif ch == ")":
            nivel = max(0, nivel - 1)
        if ch == "," and nivel == 0:
            saida.append(atual)
            atual = ""
        else:
            atual += ch
    saida.append(atual)
    return [s.strip() for s in saida if s.strip()]


def _lado(lado: str) -> list[dict] | None:
    gols: list[dict] = []
    ultimo: dict | None = None
    for item in _partes(lado):
        item = item.strip(" .;")
        # páginas uruguaias: pênalti e gol contra grudados no minuto ("Cabrera 77pen", "Álvez 31og", "Carboni 14pen, 73pen")
        suf = None
        if (ms := re.fullmatch(r"(\d{1,3}(?:\+\d)?)(pen|og)", item)) and ultimo:
            g = dict(ultimo)
            g["minuto"], g["acrescimo"] = _minuto(ms.group(1))
            g["tipo"] = "penalti" if ms.group(2) == "pen" else "contra"
            gols.append(g)
            continue
        if ms := re.search(r"\s(\d{1,3}(?:\+\d)?)(pen|og)$", item):
            item, suf = f"{item[:ms.start()]} {ms.group(1)}", ms.group(2)
        if re.fullmatch(r"\d{1,3}(\+\d)?['m]?", item) and ultimo:   # "Pizzuti 35, 56": outro gol do mesmo jogador
            g = dict(ultimo)
            g["minuto"], g["acrescimo"] = _minuto(item)
            gols.append(g)
            continue
        minuto = acr = None
        m = re.match(r"^(\d{1,3})(?:\+(\d))?['m]\s*(.+)$", item)   # "11' Calderón"
        if m:
            minuto, acr, item = int(m.group(1)), int(m.group(2)) if m.group(2) else None, m.group(3)
        m = re.search(r"\s(\d{1,3})(?:\+(\d))?['m]?$", item)       # "Tolosa 78"
        if m and minuto is None:
            minuto, acr, item = int(m.group(1)), int(m.group(2)) if m.group(2) else None, item[:m.start()]
        tipo = "contra" if suf == "og" else "normal"
        if suf == "pen":
            item += " (pen)"
        if _CONTRA.search(item):
            tipo = "contra"
            item = _CONTRA.sub("", item)
        qtd, pens = 1, 0
        m = re.search(r"\((\d)(?:\s*,\s*(\d)?\s*(?:pen|p|pk)\.?)?\)", item)
        if m:
            qtd, pens = int(m.group(1)), int(m.group(2) or (1 if "pen" in m.group(0) and not m.group(2) else 0))
            item = item[:m.start()] + item[m.end():]
        if re.search(r"\((pen|p|pk|penalty)\.?\)", item, re.I):
            pens = qtd if qtd == 1 else max(pens, 1)
            item = re.sub(r"\((pen|p|pk|penalty)\.?\)", "", item, flags=re.I)
        nome = re.sub(r"\s+", " ", item).strip(" .-()")
        if not nome or not re.search(r"[A-Za-zÀ-ÿ]{2}", nome) or len(nome) > 40:
            return None
        for k in range(qtd):
            g = {"jogador": nome, "minuto": minuto if qtd == 1 else None, "acrescimo": acr if qtd == 1 else None,
                 "tipo": tipo if tipo == "contra" else ("penalti" if k < pens else "normal")}
            gols.append(g)
        ultimo = {"jogador": nome, "tipo": "contra" if tipo == "contra" else "normal"}
    return gols


def _minuto(s: str) -> tuple[int | None, int | None]:
    m = re.match(r"(\d{1,3})(?:\+(\d))?", s)
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else (None, None)


def separar(texto: str, gm: int | None, gv: int | None) -> tuple[list[dict], list[dict]] | None:
    if gm is None or gv is None or not texto or not eh_autores(texto):
        return None
    t = texto.strip()
    if re.search(r"\]\s*\[", t):
        casa, fora = re.split(r"\]\s*\[", t, maxsplit=1)
    elif ";" in t:
        casa, fora = t.split(";", 1)
    elif re.search(r"\s[-–]\s", t):
        casa, fora = re.split(r"\s[-–]\s", t, maxsplit=1)
    elif gv == 0:
        casa, fora = t, ""
    elif gm == 0:
        casa, fora = "", t
    else:
        return None
    a = _lado(casa.strip(" []")) if casa.strip(" []-") else []
    b = _lado(fora.strip(" []")) if fora.strip(" []-") else []
    if a is None or b is None or len(a) != gm or len(b) != gv:
        return None
    return a, b
