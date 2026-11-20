"""Lê os autores dos gols que a RSSSF escreve logo abaixo de cada jogo.

Formatos: "[Rafael Costa 58',80'p, Edcarlos 81'og; Caíque Sílvio 47']" (mandante antes do ";"),
"[Valmir (2), Ivan (p); Edvaldo, Alberi (2)]" (quantidade entre parênteses, sem minuto),
"[Hélio(2) e Santos]", "[N: Nivaldo(2) e Leo]" (só um lado, com a inicial do clube). O gol contra fica
no lado de quem se beneficiou (como a RSSSF e a ESPN escrevem). Só vale a leitura cujo total de gols de
cada lado bate com o placar; o resto fica só como texto no jogo.

Copiado de serie_b/gols.py.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ITEM = re.compile(r"^(?P<nome>[^\d(]+?)\s*(?P<resto>(?:\(?\s*\d.*|\(.*)?)$")


# marcas depois do minuto: og (contra), p/pen/pk (pênalti), f (falta), c (cabeça, só informativa) — "45+3c", "14f", "21p"
MINUTO = re.compile(r"(\d{1,3})\s*'?\s*(?:\+\s*(\d{1,2})\s*'?)?\s*(og|o\.g\.|pen|pk|p|f|c)?(?![a-z\d])", re.I)


def _minutos(resto: str, nome: str) -> list[dict]:
    """Gols de um jogador a partir do que vem depois do nome: "58',80'p", "81'og", "45+1'", "43" ou "(2)"."""
    gols = []
    qtd = re.search(r"\(\s*(\d)\s*\)", resto)
    resto_sem = re.sub(r"\(\s*\d\s*\)|\([12]H\)|\(\s*(?:p|og|pen|pk|contra)\s*\)", " ", resto, flags=re.I)
    geral = resto.lower()
    contra_geral = bool(re.search(r"\(\s*(?:og|contra)\s*\)|\bcontra\b", geral))
    penal_geral = bool(re.search(r"\(\s*(?:p|pen|pk)\s*\)", geral))
    achados = [m for m in MINUTO.finditer(resto_sem) if m.group(1)]
    if achados:
        for m in achados:
            marca = (m.group(3) or "").lower()
            tipo = ("contra" if marca.startswith("o") or contra_geral else "penalti" if marca.startswith("p") or penal_geral
                    else "falta" if marca == "f" else "normal")
            gols.append({"jogador": nome, "minuto": int(m.group(1)), "acrescimo": int(m.group(2)) if m.group(2) else None, "tipo": tipo})
    else:
        for _ in range(int(qtd.group(1)) if qtd else 1):
            gols.append({"jogador": nome, "minuto": None, "acrescimo": None, "tipo": "contra" if contra_geral else "penalti" if penal_geral else "normal"})
    return gols


def _lado(texto: str) -> list[dict] | None:
    gols: list[dict] = []
    ultimo_nome = None
    for parte in re.split(r",|\s+e\s+|\s+and\s+|\s+&\s+", texto):
        parte = parte.strip().strip(".")
        if not parte:
            continue
        if re.match(r"^\d", parte):   # "Marcos Dener 8', 45', 62'": minuto do mesmo jogador
            if not ultimo_nome:
                return None
            gols += _minutos(parte, ultimo_nome)
            continue
        m = ITEM.match(parte)
        if not m:
            return None
        nome, resto = m["nome"].strip(), m["resto"] or ""
        if not nome or len(nome) > 40:
            return None
        ultimo_nome = nome
        gols += _minutos(resto, nome)
    return gols


def ler(texto: str, gm: int | None, gv: int | None, mandante: str = "", visitante: str = "") -> list[dict] | None:
    """[{lado: 'mandante'|'visitante', jogador, minuto, acrescimo, tipo}] ou None se a leitura não fecha com o placar."""
    if gm is None or gv is None or not texto:
        return None
    t = texto.strip()
    t = re.sub(r"^\[|\]\s*\*?$", "", t).replace("][", ";").replace("] [", ";")
    t = re.sub(r"\]\s*\[", ";", t).strip()
    if ";" in t:
        a, b = t.split(";", 1)
        ga, gb = _lado(a), _lado(b)
    else:
        m = re.match(r"^([A-Za-zÀ-ú.]{1,6}):\s*(.*)$", t)   # "N: Nivaldo(2)" - só um lado, com a inicial
        corpo = m.group(2) if m else t
        g = _lado(corpo)
        if g is None:
            return None
        if m:
            ini = m.group(1).lower().rstrip(".")
            lado_m = mandante.lower().startswith(ini) and not visitante.lower().startswith(ini)
            lado_v = visitante.lower().startswith(ini) and not mandante.lower().startswith(ini)
            if lado_m == lado_v:
                return None
            ga, gb = (g, []) if lado_m else ([], g)
        elif gv == 0:
            ga, gb = g, []
        elif gm == 0:
            ga, gb = [], g
        else:
            return None
    if ga is None or gb is None or len(ga) != gm or len(gb) != gv:
        return None
    return [{"lado": "mandante", **x} for x in ga] + [{"lado": "visitante", **x} for x in gb]


ITEM_PLANILHA = re.compile(r"^(?P<og>\[og\]\s*)?(?P<nome>.+?)\s+(?P<min>\d{1,3})(?:\+(?P<ac>\d{1,2}))?'\s*\((?P<t>[12])ºT\)$", re.I)


def ler_planilha(texto: str, gm: int | None, gv: int | None) -> list[dict] | None:
    """Autores no formato das páginas em planilha (Série C 2013-2015, 2020, 2023):
    "Mimica 7' (2ºT), Tiago 10' (2ºT) |  Baiano 13' (1ºT)" (mandante | visitante; minuto do tempo, "(2ºT)" soma 45)
    e "[og]  Julio Terceiro 3' (1ºT)" (gol contra, já no lado de quem ganhou o gol). Só vale se fechar com o placar."""
    if gm is None or gv is None:
        return None
    t = re.sub(r'"\s*$', "", texto or "").strip()
    if not t:
        return [] if gm == gv == 0 else None
    partes = [p.strip() for p in t.split("|")]
    if len(partes) == 1:   # um lado só: é o do time que marcou
        if gm and gv:
            return None
        partes = [partes[0], ""] if gm else ["", partes[0]]
    if len(partes) != 2:
        return None
    saida = []
    for lado, parte in zip(("mandante", "visitante"), partes):
        for item in [x.strip() for x in parte.split(",") if x.strip()]:
            m = ITEM_PLANILHA.match(item)
            if not m:
                return None
            minuto = int(m["min"]) + (45 if m["t"] == "2" else 0)
            ac = int(m["ac"]) if m["ac"] else None
            saida.append({"lado": lado, "jogador": re.sub(r"\s+", " ", m["nome"]).strip(), "minuto": minuto,
                          "acrescimo": ac, "tipo": "contra" if m["og"] else "normal"})
    if sum(g["lado"] == "mandante" for g in saida) != gm or sum(g["lado"] == "visitante" for g in saida) != gv:
        return None
    return saida
