"""Revisão Série C (SC): campos do infobox da Wikipédia (pt, en, es) de cada edição.

Lê data/cache/revisao/SC/wiki/{lg}_{ano}.txt (se não houver, usa a cópia da coleta, só leitura).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comum import RAIZ, WIKI  # noqa: E402

COLETA = RAIZ / "data" / "coleta" / "bra-serie-c" / "wikipedia"
ANOS = [1981, 1988, 1990, 1992] + list(range(1994, 2000)) + list(range(2001, 2026))
CAMPOS = {
    "campeao": ["campeão", "campeao", "champions", "champion", "campeón"],
    "vice": ["vicecampeão", "vice-campeão", "vice", "runner-up", "runners-up", "runnerup", "subcampeón"],
    "terceiro": ["terceiro", "third", "tercero", "3º"],
    "promovidos": ["promovidos", "promoted", "ascendidos", "ascenso", "promovido"],
    "artilheiro": ["artilheiro", "league topscorer", "top_scorer", "top scorer", "goleador", "máximo goleador", "goleadores"],
    "rebaixados": ["rebaixados", "relegated", "descendidos", "descenso"],
    "jogos": ["jogos", "matches", "partidos"],
    "gols": ["golos", "gols", "total goals", "goals", "goles"],
}


def texto(lg, ano):
    for p in (WIKI / f"{lg}_{ano}.txt", COLETA / f"{lg}_{ano}.txt"):
        if p.exists():
            return p.read_text(encoding="utf-8"), p
    return None, None


def infobox(txt):
    """Campos do primeiro infobox: {nome: valor cru}."""
    m = re.search(r"\{\{\s*(?:Info|Infobox|Ficha)", txt, re.I)
    i = m.start() if m else txt.find("{{")
    prof, j, ini = 0, i, i
    while j < len(txt):
        if txt.startswith("{{", j):
            prof += 1; j += 2; continue
        if txt.startswith("}}", j):
            prof -= 1; j += 2
            if prof == 0:
                break
            continue
        j += 1
    corpo = txt[ini + 2:j - 2]
    campos, prof, atual, k = {}, 0, "", 0
    partes, buf = [], ""
    while k < len(corpo):
        if corpo.startswith("{{", k) or corpo.startswith("[[", k):
            prof += 1; buf += corpo[k:k + 2]; k += 2; continue
        if corpo.startswith("}}", k) or corpo.startswith("]]", k):
            prof -= 1; buf += corpo[k:k + 2]; k += 2; continue
        if corpo[k] == "|" and prof == 0:
            partes.append(buf); buf = ""; k += 1; continue
        buf += corpo[k]; k += 1
    partes.append(buf)
    for p in partes[1:]:
        if "=" in p:
            n, v = p.split("=", 1)
            campos[n.strip().lower()] = v.strip()
    return campos


def limpar(v):
    v = re.sub(r"<ref[^>]*/>", "", v)
    v = re.sub(r"<ref.*?</ref>", "", v, flags=re.S)
    v = re.sub(r"\{\{(?:Futebol|Fb team|Fbaicon|bandeira|flagicon|BR-\w+)[ _]?([^}|]*)(?:\|[^}]*)?\}\}", r"\1", v, flags=re.I)
    v = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", v)
    v = re.sub(r"<br\s*/?>", " / ", v)
    v = re.sub(r"'''?|\{\{[^}]*\}\}", "", v)
    return re.sub(r"\s+", " ", v).strip()


def campos(lg, ano):
    txt, p = texto(lg, ano)
    if not txt:
        return {}
    cb = infobox(txt)
    out = {"_arquivo": str(p)}
    for k, nomes in CAMPOS.items():
        for n in nomes:
            if n in cb and cb[n]:
                out[k] = limpar(cb[n])
                break
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in ANOS:
        for lg in ("pt", "en", "es"):
            c = campos(lg, a)
            if c:
                print(a, lg, {k: v for k, v in c.items() if k != "_arquivo"})
        print()
