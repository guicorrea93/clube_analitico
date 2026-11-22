"""Baixa as páginas do Bola n@ Área (bolanaarea.com) da Série C, Série D e Copa do Brasil.

Fonte nova da 3ª rodada da revisão (QC, 22/11/2026). Educado: 1 pedido a cada 2,5 s, cache em
data/cache/revisao/QC/bola/, nunca baixa de novo, espera em 429.
Uso (da raiz do projeto): python -I revisao/QC/baixar_bola.py
"""
import os, re, sys, time, urllib.request, urllib.error

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PASTA = os.path.join(RAIZ, "data", "cache", "revisao", "QC", "bola")
BASE = "https://www.bolanaarea.com/"
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
INDICES = ["gal_brasileirao_serie_c.htm", "gal_brasileirao_serie_d.htm", "gal_copa_do_brasil.htm"]
_ultimo = [0.0]


def baixar(nome):
    caminho = os.path.join(PASTA, nome)
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        return open(caminho, "rb").read().decode("latin-1")
    for tentativa in range(4):
        espera = 2.5 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        try:
            req = urllib.request.Request(BASE + nome, headers={"User-Agent": UA})
            dados = urllib.request.urlopen(req, timeout=60).read()
            open(caminho, "wb").write(dados)
            print("baixou", nome, len(dados))
            return dados.decode("latin-1")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(45)
                continue
            print("erro", nome, e.code)
            open(caminho + ".erro", "w").write(str(e.code))
            return ""
        except Exception as e:  # rede
            print("falha", nome, e)
            time.sleep(10)
    return ""


def links(html):
    return sorted(set(re.findall(r'href="([a-z0-9_\-]+\.htm)"', html, re.I)))


def main():
    os.makedirs(PASTA, exist_ok=True)
    for ind in INDICES:
        h = baixar(ind)
        anos = [l for l in links(h) if re.match(r"(serie_c|serie_d|copa_do_brasil)_\d{4}\.htm$", l)]
        for pag in anos:
            h2 = baixar(pag)
            base = pag[:-4]
            for l in links(h2):
                if l.startswith(base + "_"):
                    baixar(l)


if __name__ == "__main__":
    main()
