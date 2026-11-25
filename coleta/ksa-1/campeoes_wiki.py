"""Campeão e vice de cada temporada da liga saudita pela Wikipédia em inglês (página "Saudi Pro League", seção "List of
champions", em data/coleta/ksa-1/wikipedia/en_spl.txt), que segue o relatório oficial da federação (2025): a "His
Majesty's League" (1957-58 a 1973-74), a "Saudi Categorization League" (1974-75), a Premier League (1975-76 a 2006-07) e
a Pro League (2007-08 em diante).

Uso como biblioteca: lista() -> [{"temporada": "1957/58", "fim": 1958, "era": ..., "campeao": nome de exibição ou None,
"vice": ..., "situacao": "" | "não concluída" | "não disputada" | "cancelada"}].
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from clubes_ksa import clube  # noqa: E402

ARQ = AQUI.parent.parent / "data" / "coleta" / "ksa-1" / "wikipedia" / "en_spl.txt"
SITUACAO = {"not completed": "não concluída", "not held": "não disputada", "cancelled": "cancelada"}


def _clube(cel: str) -> str | None:
    l = re.search(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", cel)
    txt = (l.group(2) or l.group(1)) if l else re.sub(r"'''|\{\{[^}]*\}\}|<[^>]+>", "", cel).strip()
    if not txt:
        return None
    c = clube(txt)
    if c is None:
        raise SystemExit(f"clube sem regra na lista de campeões: {txt!r}")
    return c


def lista() -> list[dict]:
    t = ARQ.read_text(encoding="utf-8")
    t = t[t.find("===List of champions==="):]
    t = t[:t.find("\n|}")]
    saida, era = [], ""
    for bloco in t.split("\n|-"):
        cab = re.search(r"!colspan=4[^|]*\|\s*([^<\n]+)", bloco)
        if cab:
            era = cab.group(1).strip()
            continue
        celulas = [c.strip() for c in re.split(r"\n\|", "\n" + bloco.strip()) if c.strip()]
        if len(celulas) < 3 or not re.search(r"\d{4}", celulas[1]):
            continue
        m = re.search(r"(\d{4})\s*[–-]\s*(\d{2,4})", celulas[1])
        ini = int(m.group(1))
        fim = ini + 1
        temporada = f"{ini}/{fim % 100:02d}"
        resto = " ".join(celulas[2:])
        sit = next((v for k, v in SITUACAO.items() if k in resto.lower()), "")
        campeao = vice = None
        if not sit:
            campeao = _clube(celulas[2])
            vice = _clube(celulas[3]) if len(celulas) > 3 else None
        saida.append({"temporada": temporada, "fim": fim, "era": era, "campeao": campeao, "vice": vice, "situacao": sit})
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for x in lista():
        print(x["temporada"], x["era"][:28], "|", x["campeao"], "|", x["vice"], "|", x["situacao"])
