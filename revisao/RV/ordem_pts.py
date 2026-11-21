"""Edições de fase única (pontos corridos): clube com menos pontos (com o ajuste) acima de clube com mais pontos."""
from comum import *
for s in ("bra-serie-a", "bra-serie-b", "bra-serie-c", "bra-serie-d"):
    d, E = eds(s)
    for k, e in E.items():
        if e["mata"] or len(e["disputa"]) != 1: continue
        t = e["tab"]; pts = lambda r: e["pv"] * r[3] + r[4] + (r[8] or 0)
        for a, b in zip(t, t[1:]):
            if pts(a) < pts(b): print(s, k, f"{a[1]}º {a[0]} {pts(a)} (ajuste {a[8]}) acima de {b[1]}º {b[0]} {pts(b)} (ajuste {b[8]})")
