"""Revisão Série C (SC): acessos e rebaixamentos do pacote x infobox da Wikipédia (pt e en)."""
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comum import ler_csv  # noqa: E402
from infobox import ANOS, campos  # noqa: E402
from nomes import casar  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
CF = defaultdict(list)
for r in ler_csv("classificacao_final.csv"):
    CF[int(r["temporada"])].append(r)
for ano in ANOS:
    clubes = [r["clube"] for r in CF[ano]]
    sobe = {r["clube"] for r in CF[ano] if r["situacao"] in ("campeao", "acesso")}
    vice = {r["clube"] for r in CF[ano] if r["situacao"] == "vice"}
    cai = {r["clube"] for r in CF[ano] if r["situacao"] == "rebaixado"}
    for k, pac in (("promovidos", sobe), ("rebaixados", cai)):
        w = {}
        for lg in ("pt", "en"):
            v = campos(lg, ano).get(k)
            if v and v.lower() not in ("none", "nenhum", "-"):
                nomes = [x.strip() for x in re.split(r"\s*/\s*|,", v) if x.strip()]
                w[lg] = {casar(n, clubes, ano) or f"?{n}" for n in nomes}
        if not w:
            print(ano, k, "pacote:", sorted(pac), "| Wikipédia: sem lista")
            continue
        for lg, s in w.items():
            if s != pac:
                print(ano, k, lg, "| só no pacote:", sorted(pac - s), "(vice sem marca de acesso: %s)" % sorted(vice) if vice and k == "promovidos" else "",
                      "| só na Wikipédia:", sorted(s - pac))
