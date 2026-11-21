"""Downloads educados para a revisão do Paulista (SP). Guarda em data/cache/revisao/SP/.
Uso como módulo: from baixar import wikitext, html
- 1 pedido a cada 2 s, nunca baixa de novo o que já tem, espera em 429."""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, os, re, time, urllib.parse, urllib.request, urllib.error

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
CACHE = os.path.normpath(os.path.join(RAIZ, "data", "cache", "revisao", "SP"))
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
_ult = [0.0]


def _nome(url):
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("://", 1)[-1])
    return s[:180]


def get(url, sub="web", ext=".html"):
    os.makedirs(os.path.join(CACHE, sub), exist_ok=True)
    caminho = os.path.join(CACHE, sub, _nome(url) + ext)
    if os.path.exists(caminho):
        return open(caminho, encoding="utf-8").read()
    for tent in range(5):
        espera = 2 - (time.time() - _ult[0])
        if espera > 0:
            time.sleep(espera)
        _ult[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                dado = r.read()
            try:
                txt = dado.decode("utf-8")
            except UnicodeDecodeError:
                txt = dado.decode("latin-1")
            open(caminho, "w", encoding="utf-8").write(txt)
            return txt
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("429, esperando", url, flush=True)
                time.sleep(30)
                continue
            if e.code == 404:
                open(caminho, "w", encoding="utf-8").write("")
                return ""
            raise
    raise RuntimeError("falhou: " + url)


def wikitext(titulo, lang="pt"):
    url = (f"https://{lang}.wikipedia.org/w/api.php?action=parse&page="
           + urllib.parse.quote(titulo.replace(" ", "_")) + "&prop=wikitext&redirects=1&format=json")
    caminho = os.path.join(CACHE, "wiki_" + lang, _nome(url) + ".json")
    if os.path.exists(caminho):  # cache antigo (API parse)
        t = open(caminho, encoding="utf-8").read()
        if not t:
            return ""
        d = json.loads(t)
        return "" if "error" in d else d["parse"]["wikitext"]["*"]
    # mais leve: index.php?action=raw (segue um redirecionamento à mão)
    for _ in range(2):
        raw = get(f"https://{lang}.wikipedia.org/w/index.php?title="
                  + urllib.parse.quote(titulo.replace(" ", "_")) + "&action=raw", sub="raw_" + lang, ext=".txt")
        m = re.match(r"#(?:REDIRECIONAMENTO|REDIRECT)\s*\[\[([^]]+)\]\]", raw.strip(), re.I)
        if not m:
            return raw
        titulo = m.group(1)
    return raw


def wikihtml(titulo, lang="pt"):
    url = (f"https://{lang}.wikipedia.org/w/api.php?action=parse&page="
           + urllib.parse.quote(titulo.replace(" ", "_")) + "&prop=text&redirects=1&format=json")
    t = get(url, sub="wikihtml_" + lang, ext=".json")
    if not t:
        return ""
    d = json.loads(t)
    if "error" in d:
        return ""
    return d["parse"]["text"]["*"]


if __name__ == "__main__":
    import sys
    for t in sys.argv[1:]:
        print(t, len(wikitext(t)))
