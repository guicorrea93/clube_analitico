"""Baixa da Wikipédia o texto-fonte das temporadas bolivianas que a RSSSF não traz jogo a jogo (1950-1994, menos 1977) e
a página da liga ("FBF División Profesional", com a lista de campeões) para data/coleta/bol-1/wikipedia/.

- inglês: "<ano> Bolivian Primera División" (até 1976) e "<ano> Liga de Fútbol Profesional Boliviano" (1977 em diante),
  gravadas como en_<ano>.txt;
- espanhol: "Campeonato de Primera División <ano> (Bolivia)" e variações, gravadas como es_<ano>.txt;
- en_campeoes.txt: a página da liga.

Uso: python coleta/bol-1/baixar_wikipedia.py [ano ...]
"""
from __future__ import annotations

import sys
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from baixar import pegar  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "bol-1" / "wikipedia"
CACHE = AQUI.parent.parent / "data" / "cache" / "wikipedia-sulamerica" / "bol-1"   # cada título tentado (fora do git)
RAW = "https://{lang}.wikipedia.org/w/index.php?title={t}&action=raw"


def titulos(lang: str, ano: int) -> list[str]:
    if lang == "en":
        return [f"{ano} Bolivian Primera División", f"{ano} Liga de Fútbol Profesional Boliviano",
                f"{ano} Liga de Fútbol Profesional Boliviano season"]
    return [f"Torneo {ano} (Bolivia)", f"Campeonato de Primera División {ano} (Bolivia)",
            f"Primera División de Bolivia {ano}", f"Liga de Fútbol Profesional Boliviano {ano}",
            f"Campeonato Nacional {ano} (Bolivia)"]   # ("Copa Simón Bolívar <ano>" é outro torneio, entre Colômbia e Venezuela)


def baixar(lang: str, ano: int) -> str | None:
    destino = PASTA / f"{lang}_{ano}.txt"
    for t in titulos(lang, ano):
        b = pegar(RAW.format(lang=lang, t=urllib.parse.quote(t.replace(" ", "_"))), CACHE / f"{lang}_{t}.txt",
                  espera=1.0)
        s = (b or b"").decode("utf-8", "ignore")
        if s.startswith("#RED"):   # segue o redirecionamento
            alvo = s.split("[[", 1)[1].split("]]", 1)[0]
            b = pegar(RAW.format(lang=lang, t=urllib.parse.quote(alvo.replace(" ", "_"))), CACHE / f"{lang}_{alvo}.txt",
                      espera=1.0)
            s = (b or b"").decode("utf-8", "ignore")
        if len(s) > 500:
            destino.write_text(s, encoding="utf-8")
            return t
    return None


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    if not sys.argv[1:]:
        pegar(RAW.format(lang="en", t="FBF_Divisi%C3%B3n_Profesional"), PASTA / "en_campeoes.txt", espera=1.0)
    for ano in [int(a) for a in sys.argv[1:]] or [a for a in range(1950, 1995) if a not in (1962, 1977)]:
        for lang in ("en", "es"):
            t = baixar(lang, ano)
            s = (PASTA / f"{lang}_{ano}.txt").read_text(encoding="utf-8") if t else ""
            print(ano, lang, t or "-", len(s), "match_", s.count("match_"), "Partido", s.count("{{Partido") + s.count("{{partido"),
                  "OneLeg", s.count("OneLegResult"), flush=True)
