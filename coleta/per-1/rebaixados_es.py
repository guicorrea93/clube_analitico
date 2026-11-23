"""Rebaixados por ano pela Wikipédia em espanhol (PE-014): a seção "Ascensos y descensos" da página de cada temporada
(data/coleta/per-1/wikipedia/es_<ano>.txt, baixadas por baixar_wikipedia.py) traz a tabela "{{salió}} Descendidos del
Descentralizado <ano anterior>". Cada nome vai para a temporada anterior que existe (não houve campeonato em 1922-1925 e
1936). O ano do título da tabela não serve: às vezes é o do destino ("Descendidos a la Liga2 2022").

O importar.py só marca "rebaixado" quem jogou a edição; de 1984 a 1991 (Regionais e Descentralizado, em que cair do
Descentralizado não tirava o clube do campeonato), também só quem não joga a edição seguinte.

Uso: rebaixados() -> {temporada: [clube como na página]}
"""
from __future__ import annotations

import re
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "per-1" / "wikipedia"
# links que não são clube (competição, cidade, lei)
_NAO_CLUBE = re.compile(r"^(Archivo|File|Imagen|Campeonato|Copa|Torneo|Segunda|Liga ?[12]|Ley|Intermedia|Zona)\b", re.I)


def _tabelas(t: str) -> list[str]:
    """Tabelas "{| ... |}" do texto, as de dentro também (a seção costuma ter uma tabela de fora com duas dentro)."""
    saida, pilha = [], []
    for m in re.finditer(r"^\s*(\{\||\|\})", t, re.M):
        if m.group(1) == "{|":
            pilha.append(m.start())
        elif pilha:
            saida.append(t[pilha.pop():m.end()])
    return saida


def rebaixados() -> dict[str, list[str]]:
    anos = sorted(int(f.stem[3:]) for f in PASTA.glob("es_*.txt"))
    saida: dict[str, list[str]] = {}
    for ano in anos:
        t = (PASTA / f"es_{ano}.txt").read_text(encoding="utf-8")
        m = re.search(r"^==\s*Ascensos? y descensos?\s*==\s*$", t, re.M | re.I)
        if not m:
            continue
        fim = re.search(r"^==[^=].*==\s*$", t[m.end():], re.M)
        sec = t[m.end():m.end() + fim.start()] if fim else t[m.end():]
        sec = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", sec, flags=re.S)
        for tb in _tabelas(sec):
            if tb.count("{|") > 1:   # a tabela de fora: as de dentro vêm sozinhas
                continue
            cab = "\n".join(l for l in tb.splitlines() if l.lstrip().startswith("!"))
            if not re.search(r"sali[óo]|descend", cab, re.I):
                continue
            de = max((a for a in anos if a < ano), default=ano - 1)
            nomes = []
            for linha in tb.splitlines():
                l = linha.strip()
                if not l.startswith("|") or l.startswith(("|-", "|}", "|+")) or "[[" not in l or re.search(r"se mantiene", l, re.I):
                    # "Se Mantiene": ganhou a revalidação (Municipal 1998, Wanka 2001), não caiu
                    continue
                for alvo, rot in re.findall(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", l):
                    if not _NAO_CLUBE.match(alvo.strip()) and not (rot or alvo).startswith("Ascen"):
                        nomes.append((rot or alvo).replace("'''", "").strip())
                        break
            if nomes:
                saida.setdefault(str(de), [])
                saida[str(de)] += [n for n in nomes if n not in saida[str(de)]]
    return saida


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k, v in sorted(rebaixados().items()):
        print(k, v)
