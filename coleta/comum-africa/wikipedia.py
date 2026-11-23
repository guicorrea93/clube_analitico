"""Wikitexto de páginas da Wikipédia (API), com espera e tratamento do 429 (copiado de serie_b/wikipedia.py).

Uso como biblioteca: wikitexto("pt", "Título") -> str | None
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

UA = {"User-Agent": "clube-analitico/1.0 (projeto pessoal; estatisticas de futebol)"}


def wikitexto(lingua: str, titulo: str, espera: float = 3.0) -> str | None:
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
    time.sleep(espera)
    if pag.get("missing"):
        return None
    return pag["revisions"][0]["slots"]["main"]["content"]
