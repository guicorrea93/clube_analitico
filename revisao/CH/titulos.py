"""Lista títulos suspeitos (liguillas, pré-Libertadores/Sudamericana, promoção, playoff) nas páginas da RSSSF
e diz se a linha cai dentro de algum trecho de edição do chi-1 (coleta/chi-1/edicoes.py), e o FIM_PADRAO.
Uso: python -I revisao/CH/titulos.py"""
import re, sys
from pathlib import Path
RAIZ = Path.cwd()
sys.path.insert(0, str(RAIZ / "coleta" / "comum-sulamerica")); sys.path.insert(0, str(RAIZ / "coleta" / "chi-1"))
import rsssf_sul, edicoes
FIM = re.compile(edicoes.FIM_PADRAO, re.I)
RX = re.compile(r"(liguilla|pre-?sudamericana|pre-?libertadores|promotion|relegation|playoff|play-off|qualif|sudamericana|libertadores|desempate|definici)", re.I)
pags = {}
for e in edicoes.EDICOES:
    for pg, a, b in e.trechos:
        pags.setdefault(pg, []).append((e.temporada, a, b))
for pg, tr in sorted(pags.items()):
    ls = rsssf_sul.texto(RAIZ / "data/coleta/chi-1/rsssf" / f"{pg}.html")
    for t, a, b in tr:
        fim = b
        if fim is None:
            fim = len(ls)
            for i in range(a + 1, len(ls)):
                if FIM.search(ls[i].strip()):
                    fim = i; break
        for i in range(a, fim):
            l = ls[i].strip()
            if l and len(l) < 70 and RX.search(l) and not re.search(r"\d-\d", l):
                print(f"{t:18s} {pg}:{i:5d} (trecho {a}-{fim}) | {l}")
