"""Download educado com cache para a revisão do per-1 (prefixo PE).

Uso: python -I revisao/PE/baixar.py <url> <nome-do-arquivo-no-cache>
     python -I revisao/PE/baixar.py --wiki <es|en> "<título>" <nome>   (wikitexto pela API, segue redirecionamento)
Grava em data/cache/revisao/PE/<nome>. Não baixa de novo o que já tem. 1 pedido a cada 2 s; 429 -> espera 45 s.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CACHE = RAIZ / "data" / "cache" / "revisao" / "PE"
CACHE.mkdir(parents=True, exist_ok=True)
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
_ultimo = [0.0]


def pegar(url, nome, tentativas=4):
    dest = CACHE / nome
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_bytes()
    for _ in range(tentativas):
        espera = 2.0 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es,en;q=0.8"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                b = r.read()
            dest.write_bytes(b)
            return b
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(45)
                continue
            if e.code == 404:
                return None
            print("HTTP", e.code, url, file=sys.stderr)
            return None
        except Exception as e:  # noqa: BLE001
            print("erro", e, url, file=sys.stderr)
            time.sleep(5)
    return None


def wiki(lingua, titulo, nome):
    url = (f"https://{lingua}.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(titulo)}"
           "&prop=wikitext&format=json&redirects=1&formatversion=2")
    b = pegar(url, nome)
    if not b:
        return None
    d = json.loads(b)
    if "error" in d:
        return None
    return d["parse"]["wikitext"]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "--wiki":
        t = wiki(sys.argv[2], sys.argv[3], sys.argv[4])
        print("sem página" if t is None else f"{len(t)} caracteres")
    else:
        b = pegar(sys.argv[1], sys.argv[2])
        print("sem página" if b is None else f"{len(b)} bytes")
