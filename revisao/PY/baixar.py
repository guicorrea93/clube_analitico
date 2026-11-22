"""Download educado com cache: python -I revisao/PY/baixar.py <url> <arquivo em data/cache/revisao/PY/>"""
import sys, time, os, urllib.request, urllib.error
PASTA = os.path.join("data", "cache", "revisao", "PY")
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
_ult = [0.0]
def pegar(url, nome, espera=2.0):
    caminho = os.path.join(PASTA, nome)
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        return open(caminho, "rb").read()
    for tent in range(4):
        dt = time.time() - _ult[0]
        if dt < espera: time.sleep(espera - dt)
        _ult[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es,en;q=0.8"})
            b = urllib.request.urlopen(req, timeout=60).read()
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            open(caminho, "wb").write(b)
            return b
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(45); continue
            raise
    raise RuntimeError("429 repetido: " + url)
if __name__ == "__main__":
    b = pegar(sys.argv[1], sys.argv[2])
    print(len(b), "bytes")
