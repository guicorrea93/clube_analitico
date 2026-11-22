"""Disputas de pênaltis do Bola n@ Área ("Nos pênaltis: A NxM B") que faltam no pacote.

Uso (raiz): python -I revisao/QC/penaltis_bola.py -> revisao/QC/saida_penaltis_bola.txt
"""
import glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bola, comum

RE_PEN = re.compile(r"p[êe]naltis:?\s*(.+?)\s+(\d{1,2})\s*[xX]\s*(\d{1,2})\s+([^*#(]+)", re.I)


def main():
    out, resumo = [], []
    for slug in comum.SLUGS:
        pac = comum.pacote(slug)
        uf_de = {k: v["regiao"] for k, v in comum.clubes(slug).items()}
        anos = sorted({int(p["temporada"]) for p in pac})
        tot = falta = 0
        for ano in anos:
            fs = bola.paginas(slug, ano)
            if not fs:
                continue
            jp = [p for p in pac if int(p["temporada"]) == ano]
            pens = []
            for f in fs:
                data = ""
                for c in bola.celulas(open(f, "rb").read().decode("latin-1")):
                    md = bola.RE_DATA.search(c)
                    if md and len(c) < 60 and int(md.group(3)) in (ano, ano + 1):
                        data = "%s-%02d-%02d" % (md.group(3), int(md.group(2)), int(md.group(1)))
                    m = RE_PEN.search(c)
                    if m:
                        pens.append(dict(data=data, mandante=m.group(1).strip(" *#"), visitante=m.group(4).strip(" *#"),
                                         gm=int(m.group(2)), gv=int(m.group(3))))
            # casa a disputa com o jogo do pacote (mesmos clubes, data até 3 dias)
            for pe in pens:
                tot += 1
                best = None
                for p in jp:
                    dd = abs((comum.dt(pe["data"]) - comum.dt(p["data"])).days) if pe["data"] and p["data"] else 99
                    if dd > 3:
                        continue
                    s1 = min(comum.sim(pe["mandante"], p["mandante"], uf_de.get(p["mandante"], "")), comum.sim(pe["visitante"], p["visitante"], uf_de.get(p["visitante"], "")))
                    s2 = min(comum.sim(pe["mandante"], p["visitante"], uf_de.get(p["visitante"], "")), comum.sim(pe["visitante"], p["mandante"], uf_de.get(p["mandante"], "")))
                    s = max(s1, s2)
                    if s >= 0.5 and (best is None or (s, -dd) > best[0]):
                        best = ((s, -dd), p, s2 > s1)
                if not best:
                    out.append("%s %d | sem jogo no pacote: %s %s %dx%d %s" % (slug, ano, pe["data"], pe["mandante"], pe["gm"], pe["gv"], pe["visitante"]))
                    continue
                _, p, inv = best
                if p["penaltis_mandante"] == "":
                    falta += 1
                    pm, pv = (pe["gv"], pe["gm"]) if inv else (pe["gm"], pe["gv"])
                    out.append("%s %d | FALTA: %s %s %s %s-%s %s | bola: pênaltis %s %d x %d %s -> penaltis_mandante=%d, penaltis_visitante=%d" % (
                        slug, ano, p["data"], p["fase"], p["mandante"], p["gols_mandante"], p["gols_visitante"], p["visitante"],
                        pe["mandante"], pe["gm"], pe["gv"], pe["visitante"], pm, pv))
        resumo.append("%s: %d disputas de pênaltis no Bola; %d faltam no pacote" % (slug, tot, falta))
    open(os.path.join(comum.RAIZ, "revisao", "QC", "saida_penaltis_bola.txt"), "w", encoding="utf-8").write(
        "\n".join(resumo) + "\n\n" + "\n".join(out) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(resumo))


if __name__ == "__main__":
    main()
