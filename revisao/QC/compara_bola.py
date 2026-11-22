"""Compara o pacote (Série C, D e Copa do Brasil) com o Bola n@ Área, por década.

Uso (raiz do projeto): python -I revisao/QC/compara_bola.py
Saída: revisao/QC/saida_bola_<slug>.txt (resumo por década + diferenças de placar e data, + cobertura de
público, árbitro e autores dos gols no Bola).
"""
import collections, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bola, comum

RE_GOL = re.compile(r"(\d{1,3})'")


def gols_bola(txt):
    """Número de gols com autor no texto do Bola ('Alcindo 29' do 1º; Alcindo 10' do 2º')."""
    if not txt:
        return 0
    return len(RE_GOL.findall(txt))


def main():
    for slug in comum.SLUGS:
        pac = comum.pacote(slug)
        gols_pac = comum.gols(slug)
        uf_de = {k: v["regiao"] for k, v in comum.clubes(slug).items()}
        por_ano = collections.defaultdict(list)
        for p in pac:
            por_ano[int(p["temporada"])].append(p)
        est = collections.defaultdict(collections.Counter)
        linhas_dif, linhas_sobra = [], []
        for ano in sorted(por_ano):
            fonte = bola.jogos(slug, ano)
            if not fonte:
                continue
            dec = comum.decada(ano)
            pares, sobra = comum.casar(fonte, por_ano[ano], uf_de)
            e = est[dec]
            e["edicoes"] += 1
            e["jogos_pacote"] += len(por_ano[ano])
            e["jogos_fonte"] += len(fonte)
            e["casados"] += len(pares)
            for f in fonte:
                tot = f["gm"] + f["gv"]
                e["fonte_com_publico"] += f["publico"] is not None
                e["fonte_com_arbitro"] += bool(f["arbitro"])
                e["fonte_gols"] += tot
                e["fonte_gols_autor"] += min(gols_bola(f["gols"]), tot)
            for f, p, inv in pares:
                ok_pl = comum.placar_igual(f, p, inv)
                ok_dt = f["data"] == p["data"]
                e["placar_igual"] += ok_pl
                e["data_igual"] += ok_dt
                e["com_data_fonte"] += bool(f["data"])
                e["mando_invertido"] += inv
                tot = int(p["gols_mandante"] or 0) + int(p["gols_visitante"] or 0)
                com_autor_pac = len(gols_pac.get(p["id"], []))
                if com_autor_pac < tot and gols_bola(f["gols"]) >= tot and tot > 0:
                    e["gols_que_o_bola_completa"] += tot - com_autor_pac
                if f["publico"] is not None and not p["publico"]:
                    e["publico_que_o_bola_completa"] += 1
                if not ok_pl or (f["data"] and not ok_dt) or inv:
                    linhas_dif.append("%s | %s %s %s-%s %s | bola: %s %s %dx%d %s%s | %s%s%s" % (
                        ano, p["data"], p["mandante"], p["gols_mandante"], p["gols_visitante"], p["visitante"],
                        f["data"], f["mandante"], f["gm"], f["gv"], f["visitante"],
                        " (mando invertido)" if inv else "", "" if ok_pl else "PLACAR ", "" if (ok_dt or not f["data"]) else "DATA ",
                        p["fase"]))
            for f in sobra:
                linhas_sobra.append("%s | bola sem par no pacote: %s %s %dx%d %s (%s)" % (
                    ano, f["data"], f["mandante"], f["gm"], f["gv"], f["visitante"], f["pagina"]))
        saida = os.path.join(comum.RAIZ, "revisao", "QC", "saida_bola_%s.txt" % slug)
        with open(saida, "w", encoding="utf-8") as out:
            out.write("Bola n@ Área x pacote %s (revisão QC, 22/11/2026)\n\n" % slug)
            for dec in sorted(est):
                e = est[dec]
                out.write("%s: %s\n" % (dec, dict(e)))
            out.write("\n## Diferenças (placar, data ou mando) entre jogos casados\n")
            out.write("\n".join(linhas_dif) + "\n")
            out.write("\n## Jogos do Bola sem par no pacote\n")
            out.write("\n".join(linhas_sobra) + "\n")
        print(slug, "->", saida)
        for dec in sorted(est):
            e = est[dec]
            print("  %s ed=%d pac=%d fonte=%d casados=%d placar=%d data=%d/%d inv=%d publico=%d arbitro=%d autores=%d/%d completa_gols=%d completa_publico=%d" % (
                dec, e["edicoes"], e["jogos_pacote"], e["jogos_fonte"], e["casados"], e["placar_igual"], e["data_igual"],
                e["com_data_fonte"], e["mando_invertido"], e["fonte_com_publico"], e["fonte_com_arbitro"], e["fonte_gols_autor"],
                e["fonte_gols"], e["gols_que_o_bola_completa"], e["publico_que_o_bola_completa"]))


if __name__ == "__main__":
    main()
