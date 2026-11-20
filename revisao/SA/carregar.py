import json, sqlite3, pathlib
RAIZ = pathlib.Path(r"C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico")
def painel(slug="bra-serie-a"):
    t = (RAIZ/"painel"/"dados"/f"{slug}.js").read_text(encoding="utf-8")
    i = t.index("=")
    s = t[i+1:].strip().rstrip(";")
    return json.loads(s)
def db():
    return sqlite3.connect(f"file:{RAIZ/'db'/'futebol.db'}?mode=ro", uri=True)
