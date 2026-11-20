"""Baixa páginas para a revisão da Copa do Brasil (prefixo CB).

Uso: python -I revisao/CB/baixar.py <wiki> <titulo> [<titulo> ...]
     python -I revisao/CB/baixar.py url <url> [...]
Guarda em data/cache/revisao/CB/. Não baixa de novo o que já existe. 1 pedido a cada 2,5 s; trata 429.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE = os.path.join(RAIZ, "data", "cache", "revisao", "CB")
UA = "clube-analitico-revisao/1.0 (uso pessoal; revisao CB)"
os.makedirs(CACHE, exist_ok=True)
_ultimo = [0.0]


def nome_arquivo(chave):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", chave)[:180]


def pegar(url, arq):
    caminho = os.path.join(CACHE, arq)
    if os.path.exists(caminho):
        return caminho, "cache"
    for tentativa in range(10):
        espera = 4.0 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                dados = r.read()
            with open(caminho, "wb") as f:
                f.write(dados)
            return caminho, "ok"
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(60 + 15 * tentativa)
                continue
            return None, f"HTTP {e.code}"
        except Exception as e:  # noqa
            time.sleep(5)
            err = str(e)
    return None, "falhou"


def wiki(lang, titulo):
    q = urllib.parse.urlencode({"action": "parse", "page": titulo, "prop": "wikitext",
                                "format": "json", "redirects": 1})
    url = f"https://{lang}.wikipedia.org/w/api.php?{q}"
    return pegar(url, nome_arquivo(f"wiki_{lang}_{titulo}") + ".json")


def wikiraw(lang, titulo):
    q = urllib.parse.urlencode({"title": titulo.replace(" ", "_"), "action": "raw"})
    url = f"https://{lang}.wikipedia.org/w/index.php?{q}"
    return pegar(url, nome_arquivo(f"raw_{lang}_{titulo}") + ".txt")


if __name__ == "__main__":
    modo = sys.argv[1]
    for t in sys.argv[2:]:
        if modo == "url":
            print(t, *pegar(t, nome_arquivo(t)))
        elif modo.endswith("raw"):
            print(t, *wikiraw(modo[:2], t), flush=True)
        else:
            print(t, *wiki(modo, t), flush=True)
