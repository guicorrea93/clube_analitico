"""Compara placares e datas do banco com o Transfermarkt (página 'gesamtspielplan', uma por temporada).

Uso: python -I revisao/QA/cmp_tm.py bra-serie-a 1985 1995 ...   (saída no terminal; diferenças listadas)
O saison_id do Transfermarkt para o Brasil varia: tenta ano-1 e ano e fica com o que tem jogos no ano certo.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import comum, tm

WETT = {"bra-serie-a": "BRA1", "bra-serie-b": "BRA2"}


def temporada_tm(slug, ano):
    for s in (ano - 1, ano):
        js = tm.jogos_temporada(WETT[slug], s)
        anos = [int(j["data"][:4]) for j in js if j["data"]]
        if js and len(js) > 12 and anos and sum(1 for a in anos if a == ano) > len(anos) / 2:
            return s, js
    return None, []


if __name__ == "__main__":
    slug = sys.argv[1]
    for ano in map(int, sys.argv[2:]):
        s, js = temporada_tm(slug, ano)
        if not js:
            print(f"== {slug} {ano}: Transfermarkt sem a temporada")
            continue
        extra = {("bra-serie-a", 1998): {"america": "América-RN"}, ("bra-serie-a", 1987): {"atletico paranaense": "Athletico-PR"}}.get((slug, ano), {})
        extra = dict({"botafogo": "Botafogo-SP"}, **extra)   # no TM, "Botafogo FR" é o do Rio e "Botafogo FC" o de Ribeirão Preto
        r = comum.comparar(slug, ano, js, extra)
        print(f"== {slug} {ano} (TM saison_id {s}): fonte {r['fonte']} jogos, casados {r['casados']}, "
              f"placar igual {r['placar_ok']}, data igual {r['data_ok']}/{r['com_data']}, sem par {len(r['sem_par'])}, mando invertido {len(r['invertido'])}")
        print("   url:", tm.url_temporada(WETT[slug], s))
        nao = {k: v for k, v in r["casador"].log.items() if v is None}
        if nao:
            print("   nomes sem casar:", nao)
        for j, b in r["placar_dif"]:
            print("   PLACAR  fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b), "| TM id", j["id"])
        for j, b in r["data_dif"]:
            print("   DATA    fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b), "| TM id", j["id"])
        for j, b in r["invertido"]:
            print("   MANDO   fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b), "| TM id", j["id"])
        for j, why, n in r["sem_par"][:30]:
            print("   SEMPAR ", why, n, comum.fmt_f(j))
