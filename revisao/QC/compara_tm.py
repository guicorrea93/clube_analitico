"""Compara o pacote com o calendário completo do transfermarkt (amostra de temporadas por década).

Uso (raiz do projeto): python -I revisao/QC/compara_tm.py
Saída: revisao/QC/saida_tm.txt
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum, tm

AMOSTRA = {
    "bra-serie-c": [2010, 2015, 2019, 2021, 2023, 2025],
    "bra-serie-d": [2010, 2013, 2016, 2019, 2021, 2024],
    "bra-copa-do-brasil": [1998, 2003, 2008, 2010, 2014, 2018, 2021, 2024],
}


def main():
    linhas = ["transfermarkt x pacote (revisão QC, 22/11/2026)", ""]
    resumo = []
    for slug, anos in AMOSTRA.items():
        pac = comum.pacote(slug)
        uf_de = {k: v["regiao"] for k, v in comum.clubes(slug).items()}
        est = collections.defaultdict(collections.Counter)
        for ano in anos:
            fonte = tm.jogos(slug, ano)
            jp = [p for p in pac if int(p["temporada"]) == ano]
            pares, sobra = comum.casar(fonte, jp, uf_de, limite=0.45)
            e = est[comum.decada(ano)]
            e["edicoes"] += 1
            e["pacote"] += len(jp)
            e["fonte"] += len(fonte)
            e["casados"] += len(pares)
            for f, p, inv in pares:
                if "pen" in f["extra"] and p["penaltis_mandante"] != "":
                    pm, pv = int(p["gols_mandante"]) + int(p["penaltis_mandante"]), int(p["gols_visitante"]) + int(p["penaltis_visitante"])
                    ok_pl = (f["gm"], f["gv"]) == ((pv, pm) if inv else (pm, pv))
                    e["com_penaltis"] += 1
                else:
                    ok_pl = comum.placar_igual(f, p, inv)
                ok_dt = f["data"] == p["data"]
                e["placar"] += ok_pl
                e["data"] += ok_dt
                e["data_mais1"] += (not ok_dt and comum.dt(f["data"]) and comum.dt(p["data"]) and (comum.dt(f["data"]) - comum.dt(p["data"])).days == 1) or 0
                e["inv"] += inv
                if not ok_pl or not ok_dt or inv:
                    linhas.append("%s %d | %s %s %s-%s %s | tm: %s %s %d:%d %s %s%s%s%s" % (
                        slug, ano, p["data"], p["mandante"], p["gols_mandante"], p["gols_visitante"], p["visitante"],
                        f["data"], f["mandante"], f["gm"], f["gv"], f["visitante"], f["extra"],
                        " MANDO" if inv else "", "" if ok_pl else " PLACAR", "" if ok_dt else " DATA"))
            for f in sobra:
                linhas.append("%s %d | tm sem par: %s %s %d:%d %s (%s)" % (slug, ano, f["data"], f["mandante"], f["gm"], f["gv"], f["visitante"], f["fase"]))
        for dec in sorted(est):
            resumo.append("%s %s %s" % (slug, dec, dict(est[dec])))
    open(os.path.join(comum.RAIZ, "revisao", "QC", "saida_tm.txt"), "w", encoding="utf-8").write(
        "\n".join(resumo) + "\n\n" + "\n".join(linhas) + "\n")
    print("\n".join(resumo))


if __name__ == "__main__":
    main()
