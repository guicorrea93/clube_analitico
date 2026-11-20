"""Revisão CL: download educado com cache (data/cache/revisao/CL/).

Uso: python revisao/CL/baixar.py <url> [<url> ...]   -> imprime o caminho de cada página guardada.
Wikipédia: passe o título com o prefixo wp:pt:<Título> (usa a API parse, wikitext).
Um pedido a cada 2,5 s; 429 -> espera 45 s e tenta de novo (até 4 vezes); nunca baixa de novo o que já tem.
"""
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "data" / "cache" / "revisao" / "CL"
CACHE.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "clube-analitico-revisao/1.0 (uso pessoal)"}


def url_de(alvo: str) -> str:
    if alvo.startswith("wp:"):
        _, lang, titulo = alvo.split(":", 2)
        q = urllib.parse.urlencode({"action": "parse", "page": titulo, "prop": "wikitext", "format": "json", "redirects": 1})
        return f"https://{lang}.wikipedia.org/w/api.php?{q}"
    return alvo


def baixar(alvo: str) -> Path:
    url = url_de(alvo)
    nome = hashlib.md5(url.encode()).hexdigest()[:12] + "_" + "".join(c if c.isalnum() else "_" for c in alvo)[-60:]
    f = CACHE / (nome + (".json" if "api.php" in url else ".html"))
    if f.exists():
        return f
    for tent in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                dados = r.read()
            f.write_bytes(dados)
            (CACHE / "urls.txt").open("a", encoding="utf-8").write(f"{f.name}\t{url}\n")
            time.sleep(2.5)
            return f
        except urllib.error.HTTPError as e:
            if e.code == 429 and tent < 3:
                time.sleep(45)
                continue
            raise
    raise RuntimeError(url)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        try:
            print(baixar(a))
        except Exception as e:  # noqa: BLE001
            print("ERRO", a, e)
