"""Autores dos gols como a RSSSF escreve -> lista de gols por lado.

Formatos vistos nas páginas argentinas:
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


_DATA = re.compile(r"^\s*\[?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? \d{1,2}(?: [A-Z][a-z])?\]?\s*$")


def eh_autores(texto: str) -> bool:
    """Não é autor: árbitro, público ou só uma data ("[Mar 26 Th]", jogo remarcado na Copa Argentina 2014/15)."""
    return (not re.match(r"^\s*(ref\.?|referee|árbitro)\b", texto, re.I) and not re.search(r"tickets|attendance", texto, re.I)
            and not _DATA.match(texto))


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
        # "Alario 11m pen, 40 m pen" (final de 2015/16): "Alario (pen) 11'" e "40' (pen)"
        item = re.sub(r"^(.*[A-Za-zÀ-ÿ.])\s+(\d{1,3})\s?m\s+pen\b", r"\1 (pen) \2'", item)
        item = re.sub(r"^(\d{1,3})\s?m\s+pen\b", r"\1' (pen)", item)
        m = re.fullmatch(r"(\d{1,3}(?:\+\d)?['m]?)(\s*\(pen\))?", item)
        if m and ultimo:   # "Pizzuti 35, 56": outro gol do mesmo jogador
            g = dict(ultimo)
            g["minuto"], g["acrescimo"] = _minuto(m.group(1))
            if m.group(2):
                g["tipo"] = "penalti"
            gols.append(g)
            continue
        minuto = acr = None
        m = re.match(r"^(\d{1,3})(?:\+(\d))?['m]\s*(.+)$", item)   # "11' Calderón"
        if m:
            minuto, acr, item = int(m.group(1)), int(m.group(2)) if m.group(2) else None, m.group(3)
        m = re.search(r"\s(\d{1,3})(?:\+(\d))?['m]?$", item)       # "Tolosa 78"
        if m and minuto is None:
            minuto, acr, item = int(m.group(1)), int(m.group(2)) if m.group(2) else None, item[:m.start()]
        tipo = "normal"
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
    # minuto antes do nome com "and" (páginas de 1995-2001): "76' and 78' (p) Gancedo" -> "76' Gancedo, 78' (p) Gancedo"
    padrao_and = re.compile(r"(\d{1,3}'(?:\s*\(p\))?)\s+and\s+(\d{1,3}'(?:\s*\(p\))?)\s+([^,;]+?)(?=\s*(?:,|;|\s[-–]\s|$))")
    while padrao_and.search(t):
        t = padrao_and.sub(lambda m: f"{m.group(1)} {m.group(3)}, {m.group(2)} {m.group(3)}", t, count=1)
    if re.search(r"\]\s*\[", t):
        casa, fora = re.split(r"\]\s*\[", t, maxsplit=1)
    elif ";" in t:
        casa, fora = t.split(";", 1)
    elif re.search(r"\s[-–/]\s", t):
        casa, fora = re.split(r"\s[-–/]\s", t, maxsplit=1)
    elif gv == 0:
        casa, fora = t, ""
    elif gm == 0:
        casa, fora = "", t
    else:
        return _pelo_placar(t, gm, gv)
    a = _lado(casa.strip(" []")) if casa.strip(" []-") else []
    b = _lado(fora.strip(" []")) if fora.strip(" []-") else []
    if a is None or b is None or len(a) != gm or len(b) != gv:
        return None
    return a, b


def _pelo_placar(t: str, gm: int, gv: int) -> tuple[list[dict], list[dict]] | None:
    """Duas colunas emendadas sem separador (páginas dos anos 1970): "Trossero(2), Marasco, J.Martínez Coronel" num 4-1.
    Tenta cortar no 1º espaço de cada item ("J.Martínez" | "Coronel"); só vale se os dois lados fecham com o placar e
    um único corte fecha."""
    itens = [x.strip() for x in re.split(r",(?![^(]*\))", t)]
    achados = []
    for i, item in enumerate(itens):
        if " " not in item:
            continue
        sp = item.index(" ")
        casa = ", ".join(itens[:i] + [item[:sp]])
        fora = ", ".join([item[sp + 1:]] + itens[i + 1:])
        a, b = _lado(casa), _lado(fora)
        if a is not None and b is not None and len(a) == gm and len(b) == gv:
            achados.append((a, b))
    return achados[0] if len(achados) == 1 else None
