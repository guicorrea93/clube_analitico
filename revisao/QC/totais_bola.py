"""Totais de cada edição (participantes, jogos, gols) no resumo do Bola n@ Área x pacote.

Uso (raiz): python -I revisao/QC/totais_bola.py  -> revisao/QC/saida_totais_bola.txt
"""
import collections, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bola, comum


def numeros(slug, ano):
    f = os.path.join(bola.PASTA, "%s%d.htm" % (bola.PREFIXO[slug], ano))
    if not os.path.exists(f):
        return None
    t = " ".join(bola.celulas(open(f, "rb").read().decode("latin-1")))
    out = {}
    for campo, rot in (("clubes", "PARTICIPANTES"), ("jogos", "JOGOS"), ("gols", "GOLS")):
        m = re.search(r"([\d\.]+)\s+" + rot + r"\b", t)
        if m:
            out[campo] = int(m.group(1).replace(".", ""))
    return out


def main():
    linhas = []
    for slug in comum.SLUGS:
        pac = comum.pacote(slug)
        tot = collections.defaultdict(collections.Counter)
        clubes = collections.defaultdict(set)
        for p in pac:
            a = int(p["temporada"])
            tot[a]["jogos"] += 1
            if p["gols_mandante"] != "":
                tot[a]["gols"] += int(p["gols_mandante"]) + int(p["gols_visitante"])
            clubes[a].update([p["mandante"], p["visitante"]])
        iguais = difs = 0
        for a in sorted(tot):
            n = numeros(slug, a)
            if not n:
                continue
            pacn = {"jogos": tot[a]["jogos"], "gols": tot[a]["gols"], "clubes": len(clubes[a])}
            dif = {k: (pacn[k], n[k]) for k in n if n[k] != pacn[k]}
            if dif:
                difs += 1
                linhas.append("%s %d: diferenças (pacote, bola) %s" % (slug, a, dif))
            else:
                iguais += 1
        linhas.append("%s: %d edições iguais em clubes, jogos e gols; %d com diferença" % (slug, iguais, difs))
    open(os.path.join(comum.RAIZ, "revisao", "QC", "saida_totais_bola.txt"), "w", encoding="utf-8").write("\n".join(linhas) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(linhas))


if __name__ == "__main__":
    main()
