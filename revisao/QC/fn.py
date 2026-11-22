"""Futebol Nacional (futebolnacional.com.br): teste por amostra na Série C e D (códigos achados por busca).

Leitor copiado de revisao/QS/fn_jogos.py (ler). Cache em data/cache/revisao/QC/fn/.
Uso (raiz): python -I revisao/QC/fn.py -> revisao/QC/saida_fn.txt
"""
import collections, html, os, re, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum

PASTA = os.path.join(comum.RAIZ, "data", "cache", "revisao", "QC", "fn")
URL = "https://futebolnacional.com.br/siteapp/controller.jsp?module=championship&code={code}&lang=pt-br"
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
RESUMOS = {
    "bra-serie-c": "FF88639175B9D71CA5BA0FEB60F782147FD12C6AFF06D23AEBD904AC62E27DA22526449B61B4766C27264E370B4B142A",
    "bra-serie-d": "FF88639175B9D71CA5BA0FEB60F78214C43668F23AD5E29950385393678F35912526449B61B4766C27264E370B4B142A",
    "bra-copa-do-brasil": "51E612B97CC3E60E6BA884B54CBBEEC7",
}
URL_RESUMO = "https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name={name}&state=--&country=BR"


def codigos(slug):
    """Ano -> código da edição, pela página-resumo da competição."""
    f = os.path.join(PASTA, "resumo_" + slug + ".html")
    if not os.path.exists(f):
        time.sleep(2.5)
        req = urllib.request.Request(URL_RESUMO.format(name=RESUMOS[slug]), headers={"User-Agent": UA})
        open(f, "wb").write(urllib.request.urlopen(req, timeout=60).read())
    s = open(f, "rb").read().decode("latin-1")
    out = {}
    for r in re.split(r"<tr", s):
        m = re.search(r"module=championship&code=([0-9A-F]+)", r)
        a = re.search(r">\s*(\d{4})\s*<", r)
        if m and a and int(a.group(1)) not in out:
            out[int(a.group(1))] = m.group(1)
    return out


def conserta(s):
    try:
        return s.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def limpo(s):
    return conserta(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip())


def baixar(code):
    os.makedirs(PASTA, exist_ok=True)
    f = os.path.join(PASTA, code + ".html")
    for espera in (3, 30, 60):
        if os.path.exists(f) and os.path.getsize(f) > 1000:
            break
        time.sleep(espera)
        req = urllib.request.Request(URL.format(code=code), headers={"User-Agent": UA})
        open(f, "wb").write(urllib.request.urlopen(req, timeout=60).read())
    return open(f, "rb").read().decode("latin-1")


def ler(t):
    cab = limpo(t.split('<table class="table table-striped break">')[0])
    info = {}
    for chave, rx in [("jogos_registrados", r"Total de Jogos Registrados: (\d+)"), ("gols", r"Núm\. de Gols: (\d+)")]:
        m = re.search(rx, cab)
        info[chave] = m[1] if m else None
    jogos, data = [], None
    for pedaco in re.split(r"(?=<thead>|<tr>)", t):
        if pedaco.startswith("<thead>"):
            x = limpo(pedaco)
            if re.match(r"\d\d/\d\d/\d{4}", x):
                data = x[6:10] + "-" + x[3:5] + "-" + x[0:2]
            continue
        if 'class="td-item"><b>' in pedaco and "matchdetails" in pedaco:
            tds = re.split(r"<td[^>]*>", pedaco)
            cel = [limpo(c) for c in tds]
            i = next((k for k, c in enumerate(tds) if c.startswith("<b>")), None)
            if i is None:
                continue
            m = re.match(r"(\d+)\s*[xX-]\s*(\d+)", cel[i])
            if not m:
                continue
            jogos.append(dict(data=data or "", mandante=re.sub(r"/[A-Z]{2}$", "", cel[i - 2]), visitante=re.sub(r"/[A-Z]{2}$", "", cel[i + 2]),
                              gm=int(m[1]), gv=int(m[2]), nota=""))
        elif pedaco.startswith('<tr><td><td colspan="7">') and jogos:
            jogos[-1]["nota"] = limpo(pedaco)
    info["jogos"] = jogos
    return info


def main():
    out = []
    est = collections.defaultdict(collections.Counter)
    for slug in RESUMOS:
      pac = comum.pacote(slug)
      cods = codigos(slug)
      for ano in sorted({int(p["temporada"]) for p in pac}):
        if ano not in cods:
            out.append("%s %d: sem edição no Futebol Nacional" % (slug, ano))
            continue
        info = ler(baixar(cods[ano]))
        jp = [p for p in pac if int(p["temporada"]) == ano]
        uf = {k: v["regiao"] for k, v in comum.clubes(slug).items()}
        pares, sobra = comum.casar(info["jogos"], jp, uf)
        pl = sum(comum.placar_igual(f, p, inv) for f, p, inv in pares)
        dtq = sum(f["data"] == p["data"] for f, p, inv in pares)
        com_nota = sum(1 for j in info["jogos"] if re.search(r"\d+'", j["nota"]))
        e = est[(slug, comum.decada(ano))]
        e["jogos_pacote"] += len(jp); e["fn"] += len(info["jogos"]); e["casados"] += len(pares); e["placar"] += pl; e["data"] += dtq; e["nota_autores"] += com_nota
        out.append("%s %d: FN %s jogos registrados, %d lidos; casados %d; placar igual %d; data igual %d; jogos com autores na nota %d" % (
            slug, ano, info["jogos_registrados"], len(info["jogos"]), len(pares), pl, dtq, com_nota))
        for f, p, inv in pares:
            if not comum.placar_igual(f, p, inv) or f["data"] != p["data"]:
                out.append("   %s %s %s-%s %s | FN %s %s %dx%d %s" % (p["data"], p["mandante"], p["gols_mandante"], p["gols_visitante"], p["visitante"], f["data"], f["mandante"], f["gm"], f["gv"], f["visitante"]))
    res = ["%s %s %s" % (k[0], k[1], dict(v)) for k, v in sorted(est.items())]
    open(os.path.join(comum.RAIZ, "revisao", "QC", "saida_fn.txt"), "w", encoding="utf-8").write("\n".join(res + [""] + out) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(res))


if __name__ == "__main__":
    main()
