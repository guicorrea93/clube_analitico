"""Carrega os dados do painel (local ou site) do par-1."""
import json, sys
def carregar(caminho):
    t = open(caminho, encoding="utf-8").read()
    i = t.index("=") + 1
    t = t[i:].strip()
    if t.endswith(";"): t = t[:-1]
    return json.loads(t)
if __name__ == "__main__":
    d = carregar(sys.argv[1])
    for k, v in d.items():
        print(k, type(v).__name__, len(v) if hasattr(v, "__len__") else v)
        if isinstance(v, list) and v: print("   ", json.dumps(v[0], ensure_ascii=False)[:400])
        if isinstance(v, dict): print("   ", list(v.items())[:3].__repr__()[:400])
