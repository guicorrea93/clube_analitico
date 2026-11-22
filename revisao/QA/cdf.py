"""Campeões do Futebol (campeoesdofutebol.com.br): listas 'dd/mm- A NxM B' (1937, Robertão) e comparação com o banco.
Uso: python -I revisao/QA/cdf.py <temporada ou chave> <pagina.html> <ano>"""
import html, io, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import baixar, comum

BASE = "https://www.campeoesdofutebol.com.br/"


def jogos(pagina, ano):
    b = baixar.baixar(BASE + pagina)
    t = b.decode("utf-8", "replace")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    out = []
    for d, m, a, ga, gb, v in re.findall(r"(\d{1,2})/(\d{1,2})\s*[-–]\s*([^\n]+?)\s+(\d+)\s*x\s*(\d+)\s+([^\n]+?)\s*$", t, re.M):
        out.append({"data": f"{ano}-{int(m):02d}-{int(d):02d}", "mandante": a.strip(), "visitante": v.strip(), "gm": int(ga), "gv": int(gb)})
    return out


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    temp, pag, ano = sys.argv[1], sys.argv[2], sys.argv[3]
    js = jogos(pag, ano)
    extra = {"athletico mg": "Atlético-MG", "rio branco es": "Rio Branco-ES", "ferroviario pr": "Ferroviário-PR", "ferroviario": "Ferroviário-PR"}
    r = comum.comparar("bra-serie-a", temp, js, extra)
    print(f"== bra-serie-a {temp} (Campeões do Futebol {pag}): fonte {r['fonte']}, casados {r['casados']}, placar igual {r['placar_ok']}, "
          f"data igual {r['data_ok']}/{r['com_data']}, sem par {len(r['sem_par'])}, mando invertido {len(r['invertido'])}; banco {len(comum.jogos_banco('bra-serie-a', temp))}")
    for j, b in r["placar_dif"]:
        print("   PLACAR  fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b))
    for j, b in r["data_dif"]:
        print("   DATA    fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b))
    for j, b in r["invertido"]:
        print("   MANDO   fonte:", comum.fmt_f(j), "| banco:", comum.fmt_b(b))
    for j, why, n in r["sem_par"][:20]:
        print("   SEMPAR ", why, n, comum.fmt_f(j))
