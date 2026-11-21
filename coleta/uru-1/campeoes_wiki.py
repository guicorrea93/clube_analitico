"""Lista de campeões da Wikipédia em inglês (página "Liga AUF Uruguaya", seção "List of champions"), segunda fonte do
campeão. A lista é a da AUF: não traz os campeões da FUF (1923 e 1924) nem o Torneo del Consejo Provisorio (1926).

Página guardada em data/coleta/uru-1/wikipedia/en_campeoes.txt (wikitexto, baixado pela API). Os rótulos viram as
temporadas do pacote: "1923" -> "1923 AUF", "2005–06" -> "2005/06"; a temporada 2020 é "2020".

Uso: campeoes() -> {temporada: nome do campeão na Wikipédia}
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "uru-1" / "wikipedia" / "en_campeoes.txt"


def campeoes() -> dict[str, str]:
    t = ARQ.read_text(encoding="utf-8")
    i = t.find("==Champions==")
    t = t[i:t.find("\n|}", i)]
    t = re.sub(r"\{\{refn[^{}]*(\{\{[^{}]*\}\}[^{}]*)*\}\}|<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S | re.I)
    saida = {}
    for r in t.split("\n|-")[1:]:
        cel = [c.strip() for c in re.split(r"\|\||\n\|", r) if c.strip()]
        if len(cel) < 3:
            continue
        m = re.search(r"(\d{4})(?:[–-](\d{2,4}))?", re.sub(r"\[\[[^\]|]*\|", "", cel[1]))
        c = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", cel[2])
        if not m or not c:
            continue
        a = m.group(1)
        temp = f"{a}/{m.group(2)[-2:]}" if m.group(2) else (f"{a} AUF" if a in ("1923", "1924") else a)
        saida[temp] = c.group(1).strip()
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in campeoes().items():
        print(k, v)
