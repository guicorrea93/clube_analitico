"""Bola na Área (bolanaarea.com): lê as páginas de tabela de cada edição (jogos com data, placar e, em algumas, local,
público e autores dos gols) e devolve a lista de jogos. Os nomes dos clubes são achados pelos nomes da edição no banco.

Uso: python -I revisao/QA/bna.py bra-serie-b 1985 serie_b_1985_tabela   (mostra os jogos lidos)
"""
import html, io, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import baixar, comum

BASE = "https://www.bolanaarea.com/"


def pagina(nome):
    b = baixar.baixar(BASE + nome + ".htm")
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        t = b.decode("latin-1")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", " | ", t))
    t = re.sub(r"[ \t\xa0\r\n]+", " ", t)
    return t


RX = re.compile(r"(\d{1,2}) ?/ ?(\d{1,2}) ?/ ?(\d{4})|(?<![\d/:])(\*?)(\d{1,2}) ?x ?(\d{1,2})(\*?)(?![\d/])")


def jogos(slug, temporada, paginas, extra=None):
    cas = comum.Casador(slug, temporada, extra)
    out = []
    for pg in paginas:
        t = pagina(pg)
        data = None
        for m in RX.finditer(t):
            if m.group(1):
                d, mm, a = m.group(1), m.group(2), m.group(3)
                data = f"{a}-{int(mm):02d}-{int(d):02d}"
                continue
            antes = re.sub(r"\s*\|\s*", " ", t[max(0, m.start() - 80):m.start()]).split()
            depois = re.sub(r"\s*\|\s*", " ", t[m.end():m.end() + 80]).split()
            h = a_ = None
            hn = an = None
            for k in (5, 4, 3, 2, 1):
                if len(antes) >= k:
                    cand = " ".join(antes[-k:])
                    if cand.startswith("("):
                        continue
                    cid = cas.exato(cand)
                    if cid:
                        h, hn = cid, cand
                        break
            for k in (5, 4, 3, 2, 1):
                if len(depois) >= k:
                    cand = " ".join(depois[:k])
                    cid = cas.exato(cand)
                    if cid:
                        a_, an = cid, cand
                        break
            if not (h and a_):
                continue
            # depois do visitante: local, público e gols até o próximo jogo
            resto = t[m.end():m.end() + 600]
            prox = RX.search(resto, 5)
            trecho = resto[:prox.start()] if prox else resto
            pub = re.search(r"Público: ?(?:\| ?)?([\d\.]+)", trecho)
            gols = re.search(r"Gols?: ?(.*?)(?:\| ?\d{2}/\d{2}/\d{4}|$)", trecho)
            out.append({"data": data, "mandante": hn, "visitante": an, "gm": int(m.group(5)), "gv": int(m.group(6)),
                        "asterisco": bool(m.group(4) or m.group(7)), "publico": int(pub.group(1).replace(".", "")) if pub and pub.group(1).replace(".", "") else None,
                        "gols": re.sub(r"\s*\|\s*", " ", gols.group(1)).strip() if gols else None, "pagina": pg})
    return out


def paginas_edicao(slug, ano):
    pre = ("brasileirao_" if slug == "bra-serie-a" else "serie_b_") + str(ano)
    b = baixar.baixar(BASE + pre + ".htm")
    t = b.decode("utf-8", "replace")
    ls = sorted(set(l[:-4] for l in re.findall(r'href="([^"]+)"', t) if l.startswith(pre) and l.endswith(".htm")))
    return [l for l in ls if not re.search(r"almanaque|partic", l)]


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    slug, temp = sys.argv[1], sys.argv[2]
    js = jogos(slug, temp, sys.argv[3:])
    print(len(js), "jogos")
    for j in js[:15]:
        print(j)
