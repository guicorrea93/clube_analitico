"""Baixa o texto-fonte (wikitexto) das páginas da Série B na Wikipédia em português e em inglês.

Grava em data/serie_b/wikipedia/{pt,en}_{ano}.txt. Servem de segunda fonte: tabela final,
matriz de resultados (confrontos), artilharia, público e estádios.

Uso: python serie_b/wikipedia.py [ano ...]     (sem ano: todos os anos com Série B; já baixado é pulado)
"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "data" / "serie_b" / "wikipedia"
UA = {"User-Agent": "clube-analitico/1.0 (projeto pessoal; dashboard de futebol)"}
ANOS = [1971, 1972] + list(range(1980, 1986)) + list(range(1988, 1993)) + list(range(1994, 2000)) + list(range(2001, 2026))
TITULOS = {
    "pt": ["Campeonato Brasileiro de Futebol de {a} - Série B", "Campeonato Brasileiro de Futebol de {a} – Série B",
           "Campeonato Brasileiro de Futebol - Série B de {a}", "Taça de Prata de {a}"],
    "en": ["{a} Campeonato Brasileiro Série B", "{a} Taça de Prata"],
}


def wikitexto(lingua: str, titulo: str) -> str | None:
    q = urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                                "titles": titulo, "redirects": 1, "format": "json", "formatversion": 2})
    for tentativa in range(6):   # a Wikipédia limita o ritmo (429): espera e tenta de novo
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://{lingua}.wikipedia.org/w/api.php?{q}", headers=UA), timeout=40) as r:
                pag = json.loads(r.read())["query"]["pages"][0]
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or tentativa == 5:
                raise
            time.sleep(max(int(e.headers.get("Retry-After") or 0), 30 * (tentativa + 1)))
    if pag.get("missing"):
        return None
    return pag["revisions"][0]["slots"]["main"]["content"]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    anos = [int(a) for a in sys.argv[1:]] or ANOS
    for a in anos:
        for lingua, modelos in TITULOS.items():
            destino = PASTA / f"{lingua}_{a}.txt"
            if destino.exists():
                continue
            for m in modelos:
                txt = wikitexto(lingua, m.format(a=a))
                time.sleep(4)
                if txt:
                    destino.write_text(txt, encoding="utf-8")
                    print(f"{lingua} {a}: {len(txt)} caracteres ({m.format(a=a)})")
                    break
            else:
                print(f"{lingua} {a}: sem página")
