"""Downloader educado da revisão CO (col-1). Guarda em data/cache/revisao/CO/.
Uso: python -I revisao/CO/baixar.py wiki <lang> <titulo> [nome_arquivo]
     python -I revisao/CO/baixar.py url <url> <nome_arquivo>
Nunca baixa de novo o que já tem; 1 pedido a cada 2,5 s; trata 429."""
import json, os, sys, time, urllib.parse, urllib.request

CACHE = os.path.join("data", "cache", "revisao", "CO")
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
os.makedirs(CACHE, exist_ok=True)
_ult = [0.0]


def _get(url):
    for tent in range(5):
        espera = 4.0 - (time.time() - _ult[0])
        if espera > 0:
            time.sleep(espera)
        _ult[0] = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(45)
                continue
            raise
    raise RuntimeError("429 repetido: " + url)


def url(u, nome):
    caminho = os.path.join(CACHE, nome)
    if os.path.exists(caminho):
        return caminho
    dado = _get(u)
    with open(caminho, "wb") as f:
        f.write(dado)
    return caminho


def wiki(lang, titulo, nome=None):
    nome = nome or f"{lang}_" + titulo.replace(" ", "_").replace("/", "_") + ".txt"
    caminho = os.path.join(CACHE, nome)
    if os.path.exists(caminho):
        return caminho
    q = urllib.parse.urlencode({"action": "parse", "page": titulo, "prop": "wikitext",
                                "format": "json", "redirects": 1})
    dado = json.loads(_get(f"https://{lang}.wikipedia.org/w/api.php?{q}"))
    if "error" in dado:
        raise RuntimeError(f"{titulo}: {dado['error'].get('info')}")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(dado["parse"]["wikitext"]["*"])
    return caminho


if __name__ == "__main__":
    if sys.argv[1] == "wiki":
        print(wiki(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None))
    else:
        print(url(sys.argv[2], sys.argv[3]))
