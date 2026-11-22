"""transfermarkt.com.br: calendário completo (gesamtspielplan) da Série C, Série D e Copa do Brasil.

Baixa (educado, cache em data/cache/revisao/QC/tm/) e lê os jogos de uma temporada.
Temporada no transfermarkt = ano - 1 (ex.: saison_id 2014 = Série C 2015).
Cobertura: Série C 2009-2026, Série D 2010-2026, Copa do Brasil 1998-2026.
Uso: python -I revisao/QC/tm.py <slug> <ano>
"""
import html, os, re, sys, time, urllib.request, urllib.error

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PASTA = os.path.join(RAIZ, "data", "cache", "revisao", "QC", "tm")
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
URL = {
    "bra-serie-c": "https://www.transfermarkt.com.br/campeonato-brasileiro-serie-c/gesamtspielplan/pokalwettbewerb/BRA3/saison_id/%d",
    "bra-serie-d": "https://www.transfermarkt.com.br/campeonato-brasileiro-serie-d/gesamtspielplan/pokalwettbewerb/BRA4/saison_id/%d",
    "bra-copa-do-brasil": "https://www.transfermarkt.com.br/copa-do-brasil/gesamtspielplan/pokalwettbewerb/BRC/saison_id/%d",
}
_ultimo = [0.0]


def baixar_url(url, nome):
    os.makedirs(PASTA, exist_ok=True)
    caminho = os.path.join(PASTA, nome)
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        return open(caminho, encoding="utf-8", errors="replace").read()
    for _ in range(4):
        espera = 3 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            dados = urllib.request.urlopen(req, timeout=60).read()
            open(caminho, "wb").write(dados)
            return dados.decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(60)
                continue
            print("erro", url, e.code)
            return ""
    return ""


def baixar(slug, ano):
    return baixar_url(URL[slug] % (ano - 1), "%s_%d.html" % (slug, ano))


def limpa(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).strip()


def jogos(slug, ano):
    s = baixar(slug, ano)
    out = []
    data = ""
    fase = ""
    for bloco in re.split(r"<div class=\"box\"", s)[1:]:
        m = re.search(r"<h2[^>]*>(.*?)</h2>", bloco, re.S) or re.search(r"class=\"content-box-headline[^\"]*\">(.*?)<", bloco, re.S)
        if m:
            fase = limpa(m.group(1))
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", bloco, re.S):
            md = re.search(r"(\d{2})/(\d{2})/(\d{4})", tr)
            if md and "hide-for-small" in tr:
                data = "%s-%s-%s" % (md.group(3), md.group(2), md.group(1))
            if "ergebnis-link" not in tr:
                continue
            mr = re.search(r'class="ergebnis-link"[^>]*id="(\d+)"[^>]*>(.*?)</a>', tr, re.S)
            if not mr:
                continue
            res = limpa(mr.group(2))
            mp = re.match(r"(\d+):(\d+)", res)
            if not mp:
                continue
            times = re.findall(r'<td class="[^"]*hauptlink[^"]*"[^>]*>\s*(?:<[^>]+>\s*)*<a title="([^"]+)"', tr)
            nomes = [html.unescape(t) for t in times]
            if len(nomes) < 2:
                continue
            out.append(dict(data=data, mandante=nomes[0], visitante=nomes[-1], gm=int(mp.group(1)), gv=int(mp.group(2)),
                            extra=res[mp.end():].strip(), id=mr.group(1), fase=fase))
    return out


if __name__ == "__main__":
    js = jogos(sys.argv[1], int(sys.argv[2]))
    sys.stdout.reconfigure(encoding="utf-8")
    for j in js[:10]:
        print(j)
    print(len(js))
