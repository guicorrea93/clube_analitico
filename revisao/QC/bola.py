"""Leitor das páginas de tabela do Bola n@ Área (bolanaarea.com) já baixadas.

jogos(slug, ano) -> lista de dicts: data (aaaa-mm-dd ou ''), mandante, visitante, gm, gv, detalhe (texto),
publico (int ou None), arbitro (str ou ''), gols (lista de nomes, '' quando não há), pagina.
"""
import glob, html, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PASTA = os.path.join(RAIZ, "data", "cache", "revisao", "QC", "bola")
PREFIXO = {"bra-serie-c": "serie_c_", "bra-serie-d": "serie_d_", "bra-copa-do-brasil": "copa_do_brasil_"}

RE_DATA = re.compile(r"(\d{1,2})/(\d{1,2})/(\d{4})")
RE_PLACAR = re.compile(r"^(\d{1,2})\s*[xX]\s*(\d{1,2})(?:\s*\(.*\))?\s*\*?$")
RE_JOGO_CELULA = re.compile(r"^(.+?)\s+(\d{1,2})\s*[xX]\s*(\d{1,2})\s+([^\d(]+?)\s*(\(.*\))?\s*\*?$")


def limpa(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace(" ", " ")
    return re.sub(r"\s+", " ", t).strip()


QUEBRA = "\u0001"


def celulas(s):
    """Linhas de texto da página: quebra em <br>, <p>, <div> e nas células; junta as tags de dentro da linha."""
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"</?(?:font|b|i|u|span|a|strong|em|sup|sub)(?:\s[^>]*)?>", "", s, flags=re.I)
    s = re.sub(r"<(?:br|/p|p|/div|div|/td|td|/th|th|/tr|tr|/li|li|table|/table)(?:\s[^>]*)?/?>", QUEBRA, s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace(" ", " ")
    out = []
    for parte in s.split(QUEBRA):
        parte = re.sub(r"\s+", " ", parte).strip()
        if parte:
            out.append(parte)
    return out


def paginas(slug, ano):
    pre = PREFIXO[slug] + str(ano)
    fs = sorted(glob.glob(os.path.join(PASTA, pre + "_*.htm")))
    return [f for f in fs if not f.endswith(".erro")]


def _detalhe(txt):
    pub = None
    m = re.search(r"P[úu]blico:\s*([\d\.]+)", txt)
    if m:
        try:
            pub = int(m.group(1).replace(".", ""))
        except ValueError:
            pub = None
    arb = ""
    m = re.search(r"[ÁA]rbitro:\s*([^;]+)", txt)
    if m:
        arb = m.group(1).strip()
    gols = ""
    m = re.search(r"Gols?:\s*(.+)$", txt)
    if m:
        gols = m.group(1).strip()
    return pub, arb, gols


def jogos(slug, ano):
    res = []
    for f in paginas(slug, ano):
        s = open(f, "rb").read().decode("latin-1")
        cs = celulas(s)
        data = ""
        i = 0
        n = len(cs)
        while i < n:
            c = cs[i]
            md = RE_DATA.search(c)
            if md and len(c) < 60 and not RE_PLACAR.match(c):
                d, m, a = md.groups()
                if int(a) in (ano, ano + 1, ano - 1):
                    data = "%s-%02d-%02d" % (a, int(m), int(d))
                i += 1
                continue
            jogo = None
            mp = RE_PLACAR.match(c)
            if mp and i > 0 and i + 1 < n and cs[i - 1] and cs[i + 1] and len(cs[i - 1]) < 50 and len(cs[i + 1]) < 50:
                jogo = (cs[i - 1], int(mp.group(1)), int(mp.group(2)), cs[i + 1])
                prox = i + 2
            else:
                mj = RE_JOGO_CELULA.match(c)
                if mj and len(c) < 70 and not RE_DATA.search(c) and "Local" not in c:
                    jogo = (mj.group(1), int(mj.group(2)), int(mj.group(3)), mj.group(4))
                    prox = i + 1
            if jogo:
                det = []
                j = prox
                while j < n and j < prox + 4:
                    cj = cs[j]
                    if RE_PLACAR.match(cj) or (RE_DATA.search(cj) and len(cj) < 60) or RE_JOGO_CELULA.match(cj) and len(cj) < 70 and "Local" not in cj:
                        break
                    if j + 1 < n and RE_PLACAR.match(cs[j + 1]):
                        break
                    det.append(cj)
                    j += 1
                txt = " ".join(x for x in det if x)
                pub, arb, gols = _detalhe(txt)
                data_jogo = data
                md2 = re.search(r"(?<![\d/])(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})(?![\d/])", txt)
                if md2:
                    a2 = int(md2.group(3))
                    a2 = a2 + 2000 if a2 < 50 else (a2 + 1900 if a2 < 100 else a2)
                    if a2 in (ano, ano + 1):
                        data_jogo = "%d-%02d-%02d" % (a2, int(md2.group(2)), int(md2.group(1)))
                res.append(dict(data=data_jogo, mandante=jogo[0].rstrip("* "), visitante=jogo[3].rstrip("* "),
                                gm=jogo[1], gv=jogo[2], detalhe=txt[:400], publico=pub, arbitro=arb,
                                gols=gols, pagina=os.path.basename(f)))
                i = prox
                continue
            i += 1
    return res


if __name__ == "__main__":
    import sys
    slug, ano = sys.argv[1], int(sys.argv[2])
    js = jogos(slug, ano)
    for j in js[:15]:
        print(j["data"], j["mandante"], j["gm"], "x", j["gv"], j["visitante"], "|", j["publico"], "|", j["arbitro"][:30], "|", j["gols"][:60])
    print(len(js), "jogos")
