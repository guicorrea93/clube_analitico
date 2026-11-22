"""Datas do pacote que o Bola n@ Área E o transfermarkt contradizem juntos (duas fontes novas, de linhagens diferentes).

Uso (raiz): python -I revisao/QC/datas_3fontes.py -> revisao/QC/saida_datas_3fontes.txt
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bola, comum, tm

ANOS = {
    "bra-serie-c": [2010, 2013, 2015, 2019, 2021, 2023, 2025],
    "bra-serie-d": [2010, 2013, 2015, 2016, 2019, 2020, 2021, 2024],
    "bra-copa-do-brasil": [2001, 2003, 2008, 2010, 2014, 2015, 2018, 2021, 2024],
}


def main():
    out, resumo = [], []
    for slug, anos in ANOS.items():
        pac = comum.pacote(slug)
        uf_de = {k: v["regiao"] for k, v in comum.clubes(slug).items()}
        for ano in anos:
            jp = [p for p in pac if int(p["temporada"]) == ano]
            fb = bola.jogos(slug, ano)
            ft = tm.jogos(slug, ano)
            pb, _ = comum.casar(fb, jp, uf_de)
            pt, _ = comum.casar(ft, jp, uf_de, limite=0.45)
            db = {p["id"]: f["data"] for f, p, inv in pb if f["data"]}
            dtm = {p["id"]: f["data"] for f, p, inv in pt if f["data"]}
            n = errados = so_tm_mais1 = 0
            dif = collections.Counter()
            for p in jp:
                if p["id"] in db and p["id"] in dtm:
                    n += 1
                    if db[p["id"]] == dtm[p["id"]] != p["data"]:
                        errados += 1
                        d = (comum.dt(db[p["id"]]) - comum.dt(p["data"])).days
                        dif[d] += 1
                        out.append("%s %d | pacote %s %s %s-%s %s (fonte %s) | bola e tm: %s (%+d dia)" % (
                            slug, ano, p["data"], p["mandante"], p["gols_mandante"], p["gols_visitante"], p["visitante"],
                            p["fonte"], db[p["id"]], d))
            resumo.append("%s %d: %d jogos nas 3 fontes; %d com a data do pacote contra Bola e tm juntos %s" % (
                slug, ano, n, errados, dict(dif)))
    open(os.path.join(comum.RAIZ, "revisao", "QC", "saida_datas_3fontes.txt"), "w", encoding="utf-8").write(
        "\n".join(resumo) + "\n\n" + "\n".join(out) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(resumo))


if __name__ == "__main__":
    main()
