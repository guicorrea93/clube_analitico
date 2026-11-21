"""Baixa páginas para a revisão da Liga espanhola (cache em data/cache/revisao/SB/).

Uso: python -I revisao/SB/baixar.py URL [URL...]
Imprime o caminho do arquivo em cache de cada URL. Nunca baixa de novo o que já tem.
"""
import hashlib, os, sys, time, urllib.request, urllib.error, re

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
CACHE = os.path.normpath(os.path.join(RAIZ, "data", "cache", "revisao", "ES"))
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
os.makedirs(CACHE, exist_ok=True)
_ultimo = [0.0]


def nome_cache(url):
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("//", 1)[-1])[:120]
    return os.path.join(CACHE, base + "_" + hashlib.md5(url.encode()).hexdigest()[:8])


def baixar(url):
    arq = nome_cache(url)
    if os.path.exists(arq):
        return arq
    for tent in range(4):
        espera = 2.2 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                dados = r.read()
            with open(arq, "wb") as f:
                f.write(dados)
            return arq
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(45)
                continue
            print("ERRO", e.code, url, file=sys.stderr)
            return None
        except Exception as e:  # noqa
            print("ERRO", e, url, file=sys.stderr)
            time.sleep(5)
    return None


if __name__ == "__main__":
    for u in sys.argv[1:]:
        print(baixar(u))
