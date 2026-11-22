"""Download educado da revisão QS (3ª rodada do Paulista): cache em data/cache/revisao/QS/, 1 pedido a cada 2,5 s,
espera em 429. Uso: python -I revisao/QS/baixar.py <url> [<url> ...]  (imprime o caminho do arquivo e o status)."""
import hashlib
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CACHE = RAIZ / "data" / "cache" / "revisao" / "QS"
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
_ultimo = [0.0]


def nome_arquivo(url: str) -> Path:
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("://", 1)[-1])[:120]
    h = hashlib.md5(url.encode()).hexdigest()[:8]
    return CACHE / f"{base}_{h}.html"


def baixar(url: str, ua: str = UA) -> tuple[Path | None, str]:
    arq = nome_arquivo(url)
    if arq.exists():
        return arq, "cache"
    CACHE.mkdir(parents=True, exist_ok=True)
    for tentativa in range(3):
        espera = 2.5 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept-Language": "pt-BR,pt;q=0.9"})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                dados = r.read()
            arq.write_bytes(dados)
            return arq, "200"
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(45)
                continue
            return None, str(e.code)
        except Exception as e:  # noqa: BLE001
            return None, type(e).__name__ + ":" + str(e)[:80]
    return None, "429"


if __name__ == "__main__":
    for u in sys.argv[1:]:
        a, s = baixar(u)
        print(s, a.stat().st_size if a else "-", a or u)
