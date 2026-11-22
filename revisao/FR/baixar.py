"""FR: download educado com cache (data/cache/revisao/FR/). Uso: python -I revisao/FR/baixar.py URL [nome]"""
import hashlib, json, os, sys, time, urllib.parse, urllib.request
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE = os.path.join(RAIZ, "data", "cache", "revisao", "FR")
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
_ult = [0.0]

def pegar(url, nome=None):
    os.makedirs(CACHE, exist_ok=True)
    nome = nome or hashlib.md5(url.encode()).hexdigest() + ".html"
    arq = os.path.join(CACHE, nome)
    if os.path.exists(arq) and os.path.getsize(arq) > 0:
        return open(arq, "rb").read()
    for tent in range(4):
        espera = 2.0 - (time.time() - _ult[0])
        if espera > 0:
            time.sleep(espera)
        _ult[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr,en;q=0.8"})
            dados = urllib.request.urlopen(req, timeout=60).read()
            open(arq, "wb").write(dados)
            return dados
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(45); continue
            print("HTTP", e.code, url, file=sys.stderr); return None
        except Exception as e:
            print("erro", e, url, file=sys.stderr); time.sleep(5)
    return None

def wiki(lang, titulo):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(titulo)}&prop=wikitext&format=json&redirects=1"
    nome = f"wiki_{lang}_" + titulo.replace(" ", "_").replace("/", "_") + ".json"
    d = pegar(url, nome)
    if not d:
        return None
    j = json.loads(d)
    if "error" in j:
        return None
    return j["parse"]["wikitext"]["*"]

if __name__ == "__main__":
    d = pegar(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print(len(d) if d else None)
