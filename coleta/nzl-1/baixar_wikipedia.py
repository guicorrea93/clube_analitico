"""Baixa o wikitexto das páginas da Wikipédia em inglês das temporadas da liga neozelandesa para data/coleta/nzl-1/wikipedia/.
Servem de segunda fonte do campeão e do 1º da fase de liga, e para desempatar divergências entre a matriz e a tabela da RSSSF.

Uso: python coleta/nzl-1/baixar_wikipedia.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
from wikipedia import wikitexto  # noqa: E402

DEST = AQUI.parent.parent / "data" / "coleta" / "nzl-1" / "wikipedia"


# títulos alternativos tentados quando o primeiro não existe
OUTROS = {
    "1996": ["1996 New Zealand Summer Soccer League", "1996 New Zealand National Soccer League"],
    "1996-97": ["1996–97 New Zealand Summer Soccer League", "1996–97 New Zealand National Soccer League"],
    "1997-98": ["1997–98 New Zealand Summer Soccer League", "1997–98 New Zealand National Soccer League"],
    **{f"{a}-{(a + 1) % 100:02d}": [f"{a}–{(a + 1) % 100:02d} New Zealand Football Championship",
                                     f"{a}–{(a + 1) % 100:02d} Premiership (New Zealand)",
                                     f"{a}–{(a + 1) % 100:02d} New Zealand Premiership"] for a in range(2016, 2021)},
}


def titulos() -> dict[str, str]:
    t = {"campeoes": "List of New Zealand football champions"}
    for a in range(1970, 1993):
        t[str(a)] = f"{a} New Zealand National Soccer League"
    for a in (1993, 1994, 1995):
        t[str(a)] = f"{a} New Zealand Superclub League"
    t["1996"] = "1996 New Zealand National Summer Soccer League"
    t["1996-97"] = "1996–97 New Zealand National Summer Soccer League"
    t["1997-98"] = "1997–98 New Zealand National Summer Soccer League"
    for a in (1999, 2000, 2001, 2002, 2003):
        t[str(a)] = f"{a} New Zealand National Soccer League"
    for a in range(2004, 2021):
        nome = "New Zealand Football Championship" if a < 2016 else "ISPS Handa Premiership"
        t[f"{a}-{(a + 1) % 100:02d}"] = f"{a}–{(a + 1) % 100:02d} {nome}"
    for a in range(2021, 2026):
        t[str(a)] = f"{a} New Zealand National League"
    return t


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    DEST.mkdir(parents=True, exist_ok=True)
    for chave, titulo in titulos().items():
        arq = DEST / f"{chave}.wiki"
        if arq.exists():
            continue
        txt = wikitexto("en", titulo)
        for alt in OUTROS.get(chave, []):
            if txt:
                break
            titulo, txt = alt, wikitexto("en", alt)
        print(chave, titulo, "-" if txt is None else len(txt), flush=True)
        if txt:
            arq.write_text(txt, encoding="utf-8")


if __name__ == "__main__":
    main()
