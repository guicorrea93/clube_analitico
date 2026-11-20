"""Lê os autores dos gols que a RSSSF escreve logo abaixo de cada jogo.

Formatos: "[Rafael Costa 58',80'p, Edcarlos 81'og; Caíque Sílvio 47']" (mandante antes do ";"),
"[Valmir (2), Ivan (p); Edvaldo, Alberi (2)]" (quantidade entre parênteses, sem minuto),
"[Hélio(2) e Santos]", "[N: Nivaldo(2) e Leo]" (só um lado, com a inicial do clube). O gol contra fica
no lado de quem se beneficiou (como a RSSSF e a ESPN escrevem). Só vale a leitura cujo total de gols de
cada lado bate com o placar; o resto fica só como texto no jogo.

Uso: python serie_b/gols.py     (quantos jogos com gol tiveram os autores lidos, por ano)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ITEM = re.compile(r"^(?P<nome>[^\d(]+?)\s*(?P<resto>(?:\(?\s*\d.*|\(.*)?)$")


MINUTO = re.compile(r"(\d{1,3})\s*'?\s*(?:\+\s*(\d{1,2})\s*'?)?\s*(og|o\.g\.|pen|p)?(?![a-z\d])", re.I)


def _minutos(resto: str, nome: str) -> list[dict]:
    """Gols de um jogador a partir do que vem depois do nome: "58',80'p", "81'og", "45+1'", "43" ou "(2)"."""
    gols = []
    qtd = re.search(r"\(\s*(\d)\s*\)", resto)
    resto_sem = re.sub(r"\(\s*\d\s*\)|\([12]H\)|\(\s*(?:p|og|pen)\s*\)", " ", resto, flags=re.I)
    geral = resto.lower()
    contra_geral = bool(re.search(r"\(\s*og\s*\)|\bcontra\b", geral))
    penal_geral = bool(re.search(r"\(\s*(?:p|pen)\s*\)", geral))
    achados = [m for m in MINUTO.finditer(resto_sem) if m.group(1)]
    if achados:
        for m in achados:
            marca = (m.group(3) or "").lower()
            tipo = "contra" if marca.startswith("o") or contra_geral else "penalti" if marca.startswith("p") or penal_geral else "normal"
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


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import rsssf
    for a in sorted(int(p.name[2:6]) for p in rsssf.PASTA.glob("br*l2.htm")):
        jogos, _ = rsssf.ler(a)
        com_gol = [j for j in jogos if j.gm and (j.gm or j.gv) or (j.gv)]
        com_texto = [j for j in com_gol if j.gols]
        lidos = [j for j in com_texto if ler(j.gols, j.gm, j.gv, j.mandante, j.visitante) is not None]
        print(f"{a}: {len(com_gol)} jogos com gol, {len(com_texto)} com autores, {len(lidos)} lidos")
