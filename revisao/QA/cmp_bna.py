"""Compara placares e datas do banco com o Bola na Área (páginas de tabela de cada edição).

Uso: python -I revisao/QA/cmp_bna.py bra-serie-b 1971 1985 ...
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import comum, bna

if __name__ == "__main__":
    slug = sys.argv[1]
    for ano in sys.argv[2:]:
        pgs = bna.paginas_edicao(slug, ano)
        js = [j for j in bna.jogos(slug, ano, pgs) if not j["asterisco"]]
        r = comum.comparar(slug, ano, js)
        npub = sum(1 for j in js if j["publico"])
        ngol = sum(1 for j in js if j["gols"])
        print(f"== {slug} {ano} (Bola na Área {pgs}): fonte {r['fonte']} jogos, casados {r['casados']}, placar igual {r['placar_ok']}, "
              f"data igual {r['data_ok']}/{r['com_data']}, sem par {len(r['sem_par'])}, mando invertido {len(r['invertido'])}; com público {npub}, com autores {ngol}")
        nb = len(comum.jogos_banco(slug, ano))
        print(f"   banco: {nb} jogos")
        for j, b in r["placar_dif"]:
            print("   PLACAR  fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b), "|", j["pagina"])
        for j, b in r["data_dif"]:
            print("   DATA    fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b), "|", j["pagina"])
        for j, b in r["invertido"]:
            print("   MANDO   fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b), "|", j["pagina"])
        for j, why, n in r["sem_par"][:40]:
            print("   SEMPAR ", why, n, comum.fmt_f(j), "|", j["pagina"])
