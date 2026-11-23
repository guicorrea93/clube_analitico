"""Lista de campeões da Wikipédia em inglês (página "Chilean Primera División", seção "List of champions"), segunda fonte
do campeão.

Página guardada em data/coleta/chi-1/wikipedia/en_campeoes.txt (wikitexto, baixado pela API). Os rótulos viram as
temporadas do pacote: "1997" + "Apertura" -> "1997 Apertura", "2013–14" + "Clausura" -> "2013/14 Clausura",
"Transición" -> "2013 Transición"; "2020" é a temporada 2020/21.

Uso: campeoes() -> {temporada: nome do campeão na Wikipédia}
"""
from __future__ import annotations

import re
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "chi-1" / "wikipedia" / "en_campeoes.txt"
_TORNEIO = {"apertura": "Apertura", "clausura": "Clausura", "transición": "Transición", "transicion": "Transición",
            "transition": "Transición"}


def _texto(c: str) -> str:
    c = re.sub(r"\{\{[^{}]*\}\}", "", c)
    m = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", c)
    return (m.group(1) if m else re.sub(r"^[^|]*\|", "", c)).strip()


def campeoes() -> dict[str, str]:
    t = ARQ.read_text(encoding="utf-8")
    i = t.find("==List of champions==")
    t = t[i:t.find("\n|}", i)]
    t = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    saida, ano = {}, None
    for r in t.split("\n|-")[1:]:
        cel = [c.strip() for c in re.split(r"\|\||\n\|", r) if c.strip() and not c.strip().startswith("!")]
        if len(cel) < 3:
            continue
        k, temp = None, None
        for n, c in enumerate(cel[:3]):
            x = _texto(c)
            if m := re.fullmatch(r"(\d{4})(?:[–-](\d{2,4}))?", x):
                ano = f"{m.group(1)}/{m.group(2)[-2:]}" if m.group(2) else m.group(1)
                k, temp = n, ano
            elif x.lower() in _TORNEIO and ano:
                k, temp = n, f"{ano} {_TORNEIO[x.lower()]}"
        if k is None or k + 1 >= len(cel):
            continue
        if temp.startswith("2020/21"):
            temp = "2020"
        elif temp in ("2013", "2017"):   # os torneios de transição aparecem só com o ano
            temp += " Transición"
        saida.setdefault(temp, _texto(cel[k + 1]))
        if k + 2 < len(cel):
            _VICE.setdefault(temp, _texto(cel[k + 2]))
    return saida


_VICE: dict[str, str] = {}


def vices() -> dict[str, str]:
    """Vice da lista (coluna Runners-up, logo depois do campeão)."""
    campeoes()
    return {t: v for t, v in _VICE.items() if v and not v.startswith("{{")}


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from edicoes import EDICOES
    c = campeoes()
    print(len(c), [e.temporada for e in EDICOES if e.temporada not in c])
    print([k for k in c if k not in {e.temporada for e in EDICOES}])
