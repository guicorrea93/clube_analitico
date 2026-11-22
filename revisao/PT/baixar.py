"""Baixa páginas com cache em data/cache/revisao/PT/ (1 pedido a cada 2 s, trata 429)."""
import subprocess, hashlib, json, pathlib, re, sys, time, urllib.parse, urllib.request
CACHE = pathlib.Path(r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\data\cache\revisao\PT")
CACHE.mkdir(parents=True, exist_ok=True)
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
_ult = [0.0]
def nome_cache(url):
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("://", 1)[-1])[:120]
    return CACHE / (base + "_" + hashlib.md5(url.encode()).hexdigest()[:8])
def baixar(url, tentativas=4):
    f = nome_cache(url)
    if f.exists():
        return f.read_bytes()
    for k in range(tentativas):
        espera = 2 - (time.time() - _ult[0])
        if espera > 0: time.sleep(espera)
        _ult[0] = time.time()
        tmp = str(f) + ".tmp"
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "45", "-A", UA, "-o", tmp, "-w", "%{http_code}", url], capture_output=True, text=True)
        code = r.stdout.strip()
        if code == "200":
            b = pathlib.Path(tmp).read_bytes(); pathlib.Path(tmp).unlink()
            f.write_bytes(b); return b
        if code == "429":
            time.sleep(45); continue
        if code == "404":
            f.write_bytes(b""); return b""
        time.sleep(5)
    raise RuntimeError("falhou " + url)
def wikitext(lang, pagina, _n=0):
    """wikitext pela action=raw (a API de parse está dando 429); segue redirecionamento."""
    url = f"https://{lang}.wikipedia.org/w/index.php?title={urllib.parse.quote(pagina.replace(' ', '_'))}&action=raw"
    b = baixar(url)
    t = b.decode("utf-8", "replace") if b else ""
    m = re.match(r"\s*#(?:REDIRECT|REDIRECIONAMENTO|REDIRECCIÓN)\s*\[\[([^\]|#]+)", t, re.I)
    if m and _n < 3:
        return wikitext(lang, m.group(1).strip(), _n + 1)
    return t
def html_wiki(lang, pagina):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(pagina)}&prop=text&redirects=1&format=json"
    b = baixar(url)
    if not b: return ""
    d = json.loads(b)
    if "error" in d: return ""
    return d["parse"]["text"]["*"]
if __name__ == "__main__":
    for u in sys.argv[1:]:
        print(len(baixar(u)), u)
