import sys, re, html, unicodedata
sys.path.insert(0, r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico\revisao\SA")
from baixar import baixar
def txt(url):
    b = baixar(url)
    t = b.decode("latin-1", "replace")
    t = re.sub(r"<[^>]+>", "", t); t = html.unescape(t)
    return t
def k(s): return unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode().lower()
def busca(url, a, b):
    t = txt(url)
    return [l.strip() for l in t.splitlines() if k(a) in k(l) and k(b) in k(l)]
if __name__ == "__main__":
    url = sys.argv[1]
    for par in sys.argv[2:]:
        a, b = par.split("/")
        print(par, "->", busca(url, a, b)[:6])
