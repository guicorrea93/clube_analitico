"""Quarta rodada: os quatro finalistas lado a lado, misturas entre eles e formatos novos.
Reaproveita os desenhos da 3ª rodada (escudos3.py) e grava logo/identidade.html e logo/r4/*.svg."""
import math
from pathlib import Path

AQUI = Path(__file__).resolve().parent
_src = (AQUI / "escudos3.py").read_text(encoding="utf-8")
exec(_src.split("# (família, [")[0])          # estrela, pal, defs, texto, bola, faixa, louros, coroa e os escudos da 3ª rodada
(SAIDA / "r4").mkdir(parents=True, exist_ok=True)


def anel(u, p, fundo, cima="CLUBE ANALÍTICO", baixo="DADOS DO FUTEBOL"):
    """Corpo do escudo redondo: aro dourado, nome em arco em cima, frase embaixo, duas estrelas nos lados."""
    s = f'<defs><path id="a{u}" d="M13 60 A37 37 0 0 1 87 60"/><path id="b{u}" d="M7.5 60 A42.5 42.5 0 0 0 92.5 60"/></defs>'
    s += f'<circle cx="50" cy="60" r="49" fill="url(#o{u})"/><circle cx="50" cy="60" r="46" fill="{fundo}"/>'
    s += f'<circle cx="50" cy="60" r="32" fill="none" stroke="{p["v"]}" stroke-width="1.6"/>'
    s += (f'<text font-family="{FONTE}" font-weight="800" font-size="10.5" letter-spacing="2.6" fill="{p["t"] if not p["mono"] else p["v"]}">'
          f'<textPath href="#a{u}" startOffset="50%" text-anchor="middle">{cima}</textPath></text>')
    s += (f'<text font-family="{FONTE}" font-weight="700" font-size="7.6" letter-spacing="2" fill="{p["v"]}">'
          f'<textPath href="#b{u}" startOffset="50%" text-anchor="middle">{baixo}</textPath></text>')
    return s + f'<polygon points="{estrela(10, 60, 3.2)}" fill="url(#o{u})"/><polygon points="{estrela(90, 60, 3.2)}" fill="url(#o{u})"/>'


def fundo_de(p):
    return p["f2"] if p["mono"] else "#0b2416"


# ---------- misturas dos finalistas ----------
def redondo_louros(u, modo):
    """Redondo + louros e estrelas do Completo campeão."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + louros(p) + f'<g transform="translate(0 4)">{coroa(p, u)}</g>' + anel(u, p, f)
    return s + bola(50, 60, 23, f, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])


def redondo_barras(u, modo):
    """Redondo, mas com as barras do campeão no centro em vez da bola."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + anel(u, p, f)
    for i, (x, h) in enumerate(zip((31, 42, 53, 64), (12, 19, 27, 36))):
        s += f'<rect x="{x}" y="{79 - h}" width="8" height="{h}" rx="1.4" fill="{f"url(#o{u})" if i == 3 else p["v"]}"/>'
    s += f'<rect x="28" y="80.5" width="47" height="1.8" rx=".9" fill="{p["v"]}" fill-opacity=".6"/>'
    return s + f'<polygon points="{estrela(37, 41, 4.6)}" fill="url(#o{u})"/>'


def bola_faixas(u, modo):
    """Bola no peito com CLUBE no alto e ANALÍTICO na fita, como no Completo campeão."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{f}"/>'
    s += f'<g clip-path="url(#c{u})"><g fill="{p["v"]}" fill-opacity=".07">' + "".join(
        f'<path d="M{x} 0 L{x + 6} 0 L{x - 40} 120 L{x - 46} 120 Z"/>' for x in range(30, 160, 16)) + "</g>"
    s += f'<rect x="0" y="0" width="100" height="31" fill="{p["v"]}"/><rect x="0" y="31" width="100" height="1.6" fill="url(#o{u})"/></g>'
    s += texto(50, 28, "CLUBE", 12, p["txt"], 5)
    s += f'<path d="{FINO}" fill="none" stroke="url(#o{u})" stroke-opacity=".55" stroke-width=".8"/>'
    s += bola(50, 59, 19, f, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    return s + coroa(p, u) + faixa(86, p["v"], p["f2"], "ANALÍTICO", p["txt"], 10, 2.6)


# ---------- misturas C3 + B3 ----------
def listras_diag(p, u):
    return (f'<g clip-path="url(#c{u})" fill="{p["v"]}" fill-opacity=".07">' + "".join(
        f'<path d="M{x} 0 L{x + 6} 0 L{x - 40} 120 L{x - 46} 120 Z"/>' for x in range(30, 160, 16)) + "</g>")


def podio(p, u, base, hs=(7, 11.5, 16), xs=(37, 46, 55), larg=8):
    return "".join(f'<rect x="{x}" y="{base - h}" width="{larg}" height="{h}" rx="1.4" fill="{f"url(#o{u})" if i == len(hs) - 1 else p["v"]}"/>'
                   for i, (x, h) in enumerate(zip(xs, hs)))


def topo_clube(p, u):
    return (f'<g clip-path="url(#c{u})"><rect x="0" y="0" width="100" height="31" fill="{p["v"]}"/>'
            f'<rect x="0" y="31" width="100" height="1.6" fill="url(#o{u})"/></g>' + texto(50, 28, "CLUBE", 12, p["txt"], 5))


def x1(u, modo):
    """Moldura do C3 (louros, CLUBE, fita ANALÍTICO) com o recheio do B3 (bola, pódio, listras diagonais)."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + louros(p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{f}"/>' + listras_diag(p, u)
    s += topo_clube(p, u) + f'<path d="{FINO}" fill="none" stroke="{p["v"]}" stroke-width="1.2"/>'
    s += bola(50, 48.5, 13.5, f, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    s += podio(p, u, 85.5, (7, 11, 15.5), (37.5, 46, 54.5), 8)
    return s + coroa(p, u) + faixa(88, p["v"], p["f2"], "ANALÍTICO", p["txt"], 10, 2.6)


def x2(u, modo):
    """O B3 inteiro com os louros do C3 e as quatro barras que sobem no lugar do pódio."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + louros(p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{f}"/>'
    s += f'<path d="{FINO}" fill="none" stroke="{p["v"]}" stroke-width="1.4"/>' + listras_diag(p, u)
    s += bola(50, 39, 17, f, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    s += f'<g clip-path="url(#c{u})"><rect x="0" y="61" width="100" height="12" fill="url(#o{u})"/></g>'
    s += texto(50, 70.2, "CLUBE ANALÍTICO", 8.4, p["txt"], 1.1)
    s += podio(p, u, 97, (6, 10, 15, 21), (32, 41, 50, 59), 7.5)
    return s + coroa(p, u)


def x3(u, modo):
    """O C3 com a bola em cima da barra dourada: a bola no topo do pódio."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + louros(p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{f}"/>' + listras_diag(p, u)
    s += topo_clube(p, u) + f'<path d="{FINO}" fill="none" stroke="url(#o{u})" stroke-opacity=".55" stroke-width=".8"/>'
    s += podio(p, u, 86, (11, 18, 25, 32), (26.5, 37.5, 48.5, 59.5), 9)
    s += bola(64, 45, 8.5, f, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    return s + coroa(p, u) + faixa(88, p["v"], p["f2"], "ANALÍTICO", p["txt"], 10, 2.6)


def x4(u, modo):
    """O B3 como está, só ganhando os louros do C3."""
    p = pal(modo)
    return louros(p) + bola_completo(u, modo)


# ---------- entre X1 e X3 ----------
def moldura_c3(p, u, f):
    return (defs(u, p) + louros(p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{f}"/>' + listras_diag(p, u)
            + topo_clube(p, u) + f'<path d="{FINO}" fill="none" stroke="{p["v"]}" stroke-width="1.2"/>')


def fecho_c3(p, u):
    return coroa(p, u) + faixa(88, p["v"], p["f2"], "ANALÍTICO", p["txt"], 10, 2.6)


def _bola(p, u, f, cx, cy, r):
    return bola(cx, cy, r, f, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])


def y1(u, modo):
    """X3 com a bola maior e as barras mais baixas, para a bola ganhar peso."""
    p = pal(modo); f = fundo_de(p)
    s = moldura_c3(p, u, f) + podio(p, u, 86, (9, 15, 21, 27), (25.5, 36.5, 47.5, 58.5), 9)
    return s + _bola(p, u, f, 63, 48.5, 10.5) + fecho_c3(p, u)


def y2(u, modo):
    """X1 com a bola no meio e quatro barras subindo embaixo dela."""
    p = pal(modo); f = fundo_de(p)
    s = moldura_c3(p, u, f) + _bola(p, u, f, 50, 48, 13)
    return s + podio(p, u, 85.5, (5, 9, 13, 17.5), (33, 42, 51, 60), 7.5) + fecho_c3(p, u)


def y3(u, modo):
    """Três barras largas subindo e a bola, grande, em cima da dourada."""
    p = pal(modo); f = fundo_de(p)
    s = moldura_c3(p, u, f) + podio(p, u, 86, (12, 20, 28), (28, 42, 56), 12)
    return s + _bola(p, u, f, 62, 47, 11) + fecho_c3(p, u)


def y4(u, modo):
    """Pódio de verdade (2º, 1º, 3º) com a bola em cima do degrau do campeão."""
    p = pal(modo); f = fundo_de(p)
    s = moldura_c3(p, u, f)
    for x, h, n, cor in ((32.5, 14, "2", p["v"]), (44.5, 22, "1", f"url(#o{u})"), (56.5, 9, "3", p["v"])):
        s += f'<rect x="{x}" y="{86 - h}" width="11" height="{h}" rx="1.2" fill="{cor}"/>'
        s += texto(x + 5.5, 86 - h + 7.2, n, 7, p["txt"], 0)
    return s + _bola(p, u, f, 50, 52, 11.5) + fecho_c3(p, u)


# ---------- formatos novos ----------
def esquartelado(u, modo):
    """Escudo dividido em quatro, como os brasões antigos: bola, barras, estrela e linha."""
    p = pal(modo); f = fundo_de(p)
    claro = p["f2"] if p["mono"] else p["f1"]
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{f}"/>'
    s += (f'<g clip-path="url(#c{u})"><rect x="0" y="0" width="50" height="60" fill="{claro}"/>'
          f'<rect x="50" y="60" width="50" height="60" fill="{claro}"/>'
          f'<rect x="48.6" y="0" width="2.8" height="120" fill="url(#o{u})"/><rect x="0" y="58.6" width="100" height="2.8" fill="url(#o{u})"/></g>')
    if p["mono"]:
        s += f'<path d="{INT}" fill="none" stroke="{p["v"]}" stroke-width="1"/>'
    s += bola(32.5, 39, 11.5, claro, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    for i, (x, h) in enumerate(zip((57, 64.5, 72), (9, 15, 21))):
        s += f'<rect x="{x}" y="{50 - h}" width="5.5" height="{h}" rx="1" fill="{f"url(#o{u})" if i == 2 else p["v"]}"/>'
    s += f'<polygon points="{estrela(33, 78, 10)}" fill="url(#o{u})"/>'
    s += (f'<polyline points="55,90 61,81 67,85 75,70" fill="none" stroke="{p["v"]}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>'
          f'<circle cx="75" cy="70" r="3" fill="url(#o{u})"/>')
    return s + coroa(p, u)


def faixa_diagonal(u, modo):
    """A faixa diagonal das camisas, desenhada como uma linha de gráfico que sobe."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="url(#f{u})"/>'
    pts = [(4, 104), (28, 82), (44, 88), (66, 56), (96, 26)]
    lin = " ".join(f"{x},{y}" for x, y in pts)
    s += (f'<g clip-path="url(#c{u})"><polyline points="{lin}" fill="none" stroke="{p["v"]}" stroke-width="13" stroke-linejoin="round"/>'
          f'<polyline points="{lin}" fill="none" stroke="url(#o{u})" stroke-width="2.4" stroke-linejoin="round"/></g>')
    for x, y in pts[1:4]:
        s += f'<circle cx="{x}" cy="{y}" r="3.2" fill="{f}" stroke="url(#o{u})" stroke-width="1.6"/>'
    s += f'<polygon points="{estrela(34, 40, 10)}" fill="url(#o{u})"/>'
    return s + texto(70, 96, "CA", 15, p["v"], 1)


def losango(u, modo):
    """Formato de losango, diferente dos escudos comuns, com o nome atravessando."""
    p = pal(modo); f = fundo_de(p)
    ext, inn = "50,2 98,60 50,118 2,60", "50,10 90,60 50,110 10,60"
    s = defs(u, p) + f'<clipPath id="z{u}"><polygon points="{inn}"/></clipPath>'
    s += f'<polygon points="{ext}" fill="url(#o{u})"/><polygon points="{inn}" fill="{f}"/>'
    s += f'<g clip-path="url(#z{u})"><rect x="0" y="51" width="100" height="18" fill="{p["v"]}"/>'
    s += f'<rect x="0" y="50" width="100" height="1.4" fill="url(#o{u})"/><rect x="0" y="68.6" width="100" height="1.4" fill="url(#o{u})"/></g>'
    s += texto(50, 63.6, "CLUBE ANALÍTICO", 9.4, p["txt"], 1)
    s += bola(50, 33, 12.5, f, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    for i, (x, h) in enumerate(zip((41, 47.5, 54), (8, 12.5, 17))):
        s += f'<rect x="{x}" y="{93 - h}" width="5" height="{h}" rx="1" fill="{f"url(#o{u})" if i == 2 else p["v"]}"/>'
    return s


def campo(u, modo):
    """O gramado visto de cima, com uma linha de gráfico subindo até a estrela."""
    p = pal(modo); f = fundo_de(p)
    gram = p["f2"] if p["mono"] else "#0f3a24"
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{gram}"/>'
    s += f'<g clip-path="url(#c{u})">'
    if not p["mono"]:
        s += "".join(f'<rect x="0" y="{y}" width="100" height="9" fill="#000" fill-opacity=".14"/>' for y in range(12, 120, 18))
    lin = p["t"] if not p["mono"] else p["v"]
    s += (f'<g fill="none" stroke="{lin}" stroke-opacity=".35" stroke-width="1"><line x1="0" y1="60" x2="100" y2="60"/>'
          f'<circle cx="50" cy="60" r="12"/><rect x="32" y="8" width="36" height="17"/><rect x="40" y="8" width="20" height="7"/></g></g>')
    pts = [(22, 82), (35, 70), (49, 75), (63, 52)]
    s += (f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)} 74,38" fill="none" stroke="url(#o{u})" stroke-width="3.2" '
          f'stroke-linejoin="round" stroke-linecap="round"/>')
    for x, y in pts:
        s += f'<circle cx="{x}" cy="{y}" r="2.8" fill="{p["v"]}" stroke="{gram}" stroke-width="1.2"/>'
    s += f'<polygon points="{estrela(75, 36, 8)}" fill="url(#o{u})"/>'
    return s + faixa(88, p["v"], p["f2"], "CLUBE ANALÍTICO", p["txt"], 8.2, 1.1)


def taca(u, modo):
    """Uma taça cujo bojo é um gráfico de barras."""
    p = pal(modo); f = fundo_de(p)
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="url(#f{u})"/>'
    bojo = "M31 30 H69 V43 C69 57 60.5 65 50 65 C39.5 65 31 57 31 43 Z"
    s += f'<clipPath id="t{u}"><path d="{bojo}"/></clipPath>'
    s += (f'<path d="M32 34 C21 34 20 51 35 53 M68 34 C79 34 80 51 65 53" fill="none" stroke="url(#o{u})" stroke-width="3.4" stroke-linecap="round"/>'
          f'<path d="{bojo}" fill="url(#o{u})"/>')
    s += f'<g clip-path="url(#t{u})">' + "".join(
        f'<rect x="{x}" y="{62 - h}" width="6.5" height="{h + 4}" rx="1" fill="{f}"/>' for x, h in ((37, 10), (46.75, 17), (56.5, 25))) + "</g>"
    s += (f'<rect x="47" y="64" width="6" height="9" fill="url(#o{u})"/><rect x="39" y="72.5" width="22" height="5" rx="1.2" fill="url(#o{u})"/>'
          f'<rect x="36" y="78" width="28" height="4.5" rx="1.2" fill="{p["v"]}"/>')
    s += f'<polygon points="{estrela(50, 21, 5.5)}" fill="{p["v"]}"/>'
    return s + faixa(88, p["v"], p["f2"], "CLUBE ANALÍTICO", p["txt"], 8.2, 1.1)


VB = "0 0 100 120"
VB_FAIXA = "-4 0 108 120"
VB_COROA = "-4 -14 108 134"
VB_LOURO = "-12 -14 124 134"
FAMILIAS = [
    ("Entre X1 e X3", "A moldura do C3 com a bola e as barras em quatro arranjos diferentes.", [
        ("y1", "Bola maior no topo", y1, VB_LOURO, "O X3 com a bola maior e as barras mais baixas, para a bola ganhar peso."),
        ("y2", "Bola no meio, barras embaixo", y2, VB_LOURO, "O X1 com a bola no centro e quatro barras subindo logo abaixo."),
        ("y3", "Três barras largas", y3, VB_LOURO, "Três barras largas subindo e a bola, grande, em cima da dourada."),
        ("y4", "Pódio de verdade", y4, VB_LOURO, "Degraus de 2º, 1º e 3º, com a bola em cima do degrau do campeão."),
    ]),
    ("C3 + B3", "Quatro jeitos de juntar o Campeão completo com o Bola completo.", [
        ("x1", "Moldura do C3, recheio do B3", x1, VB_LOURO, "Louros, CLUBE no alto e fita ANALÍTICO do C3; dentro, a bola, o pódio e as listras diagonais do B3."),
        ("x2", "B3 com louros e barras", x2, VB_LOURO, "O B3 com os louros do C3 e as quatro barras que sobem no lugar do pódio."),
        ("x3", "Bola no topo do pódio", x3, VB_LOURO, "O C3 com a bola apoiada em cima da barra dourada, a do campeão."),
        ("x4", "B3 com louros", x4, VB_LOURO, "O B3 sem mudança nenhuma, só ganhando os ramos de louro do C3."),
    ]),
    ("Seus 4 finalistas", "Os quatro que você separou, sem mudança, para comparar lado a lado.", [
        ("c3", "Campeão completo", campeao_completo, VB_LOURO, "CLUBE no alto, ANALÍTICO na fita, barras que sobem até a dourada, louros e estrelas."),
        ("b3", "Bola completo", bola_completo, VB_COROA, "A bola-gráfico no peito, faixa com o nome, barras de pódio e três estrelas."),
        ("l3", "Listras completo", listras_completo, VB_COROA, "As listras da camisa viram barras; nome no alto e estrela."),
        ("n1", "Redondo", redondo, "0 10 100 100", "Escudo redondo: o nome no anel e a bola-gráfico no centro."),
    ]),
    ("Misturas dos finalistas", "Pedaços de um com o desenho de outro.", [
        ("m1", "Redondo com louros", redondo_louros, VB_LOURO, "O redondo com os ramos de louro e as três estrelas do campeão completo."),
        ("m2", "Redondo com barras", redondo_barras, "0 10 100 100", "O anel do redondo com as barras do campeão no centro, no lugar da bola."),
        ("m3", "Bola com CLUBE e fita", bola_faixas, VB_COROA, "A bola no peito com a faixa CLUBE no alto e a fita ANALÍTICO embaixo, como no campeão."),
    ]),
    ("Formatos novos", "Caminhos que ainda não apareceram nas rodadas anteriores.", [
        ("q1", "Brasão em quatro", esquartelado, VB_COROA, "Dividido em quatro como os brasões antigos: bola, barras, estrela e uma linha que sobe."),
        ("d1", "Faixa diagonal", faixa_diagonal, VB, "A faixa diagonal das camisas, desenhada como uma linha de gráfico que sobe."),
        ("z1", "Losango", losango, VB, "Formato de losango, com o nome atravessando o meio, a bola em cima e o pódio embaixo."),
        ("p1", "Gramado", campo, VB_FAIXA, "O campo visto de cima, com as linhas do gramado e um gráfico subindo até a estrela."),
        ("t1", "Taça", taca, VB_FAIXA, "Uma taça cujo bojo é um gráfico de barras, com a fita do nome embaixo."),
    ]),
]


def svg(fn, u, modo, vb, alt=None, cls=""):
    w, h = (float(x) for x in vb.split()[2:])
    a = f' width="{alt * w / h:.0f}" height="{alt}"' if alt else ""
    return f'<svg viewBox="{vb}"{a}{cls} role="img" aria-label="Clube Analítico">{fn(u, modo)}</svg>'


def completo(fn, u, modo, vb):
    x0, y0, w, h = (float(v) for v in vb.split())
    esc = 120 / h
    cor_nome = CLARO if modo in ("cor", "mono-e") else FUNDO
    p = pal(modo)
    larg = w * esc
    return (f'<svg viewBox="0 0 {larg + 250:.0f} 120" role="img" aria-label="Clube Analítico">'
            f'<g transform="scale({esc:.4f}) translate({-x0} {-y0})">{fn(u, modo)}</g>'
            + texto(larg + 12, 54, "CLUBE", 25, p["v"], 9, 700, "start")
            + texto(larg + 10, 96, "ANALÍTICO", 50, cor_nome, 1, 800, "start") + "</svg>")


secoes = []
for fam, sub, itens in FAMILIAS:
    cards = []
    for chave, nivel, fn, vb, frase in itens:
        tam = "".join(f'<figure class="tam">{svg(fn, f"{chave}t{t}", "cor", vb, t)}<figcaption>{t} px</figcaption></figure>'
                      for t in (56, 32, 20))
        cards.append(f'''
    <article class="card">
      <div class="palco">{svg(fn, f"{chave}g", "cor", vb, None, ' class="grande"')}<span class="rotulo">{chave.upper()}</span></div>
      <div class="info">
        <h3>{nivel}</h3>
        <p class="frase">{frase}</p>
        <div class="tamanhos">{tam}</div>
        <div class="paineis">
          <div class="painel escuro">{completo(fn, f"{chave}ce", "cor", vb)}</div>
          <div class="painel claro">{completo(fn, f"{chave}cc", "claro", vb)}</div>
          <div class="painel escuro">{completo(fn, f"{chave}me", "mono-e", vb)}</div>
          <div class="painel claro">{completo(fn, f"{chave}mc", "mono-c", vb)}</div>
        </div>
      </div>
    </article>''')
        (SAIDA / "r4" / f"{chave}.svg").write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{fn(chave, "cor")}</svg>', encoding="utf-8")
    secoes.append(f'''
  <section class="familia">
    <header class="fam-top"><h2>{fam}</h2><p>{sub}</p></header>
    <div class="grade">{"".join(cards)}
    </div>
  </section>''')

html = f'''<title>Identidade Clube Analítico</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600&display=swap">
<style>
/* Vitrine da 4ª rodada: finalistas, misturas e formatos novos. Tema único escuro, de propósito. */
:root {{
  --fundo: #06140c; --fundo-2: #0a1f13; --linha: #17382a;
  --verde: #1ecb74; --ouro: #fbbf24; --texto: #eafff2; --texto-2: #9fc9b0; --claro: #f4f7f4;
  --f-titulo: "Barlow Condensed", "Arial Narrow", Arial, sans-serif;
  --f-corpo: "Barlow", system-ui, "Segoe UI", Arial, sans-serif;
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--fundo); color: var(--texto); font-family: var(--f-corpo); font-size: 15px; line-height: 1.5;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.topo, .familia, .rodape {{ max-width: 1240px; margin: 0 auto; }}
.topo {{ padding-block: 36px 10px; display: grid; gap: 6px; }}
.topo .sobre {{ font-family: var(--f-titulo); font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: var(--verde); font-size: 14px; }}
.topo h1 {{ margin: 0; font-family: var(--f-titulo); font-weight: 800; font-size: clamp(30px, 6vw, 46px); line-height: 1.05; text-wrap: balance; }}
.topo p {{ margin: 0; color: var(--texto-2); max-width: 64ch; }}
.familia {{ padding-block: 26px 6px; display: grid; gap: 14px; }}
.fam-top {{ display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; border-bottom: 1px solid var(--linha); padding-bottom: 8px; }}
.fam-top h2 {{ margin: 0; font-family: var(--f-titulo); font-weight: 800; font-size: 28px; text-transform: uppercase; letter-spacing: .03em; }}
.fam-top p {{ margin: 0; color: var(--texto-2); }}
.grade {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 290px), 1fr)); gap: 16px; }}
.card {{ border: 1px solid var(--linha); border-radius: 16px; overflow: hidden; background: var(--fundo-2); display: grid; align-content: start; }}
.palco {{ position: relative; display: grid; place-items: center; padding: 26px 16px 18px; background: radial-gradient(circle at 50% 45%, #123a25 0%, var(--fundo) 72%); }}
.palco .grande {{ width: 180px; max-width: 100%; height: auto; filter: drop-shadow(0 10px 20px rgba(0,0,0,.45)); }}
.rotulo {{ position: absolute; top: 10px; left: 12px; font-family: var(--f-titulo); font-weight: 700; font-size: 13px; letter-spacing: .1em; color: var(--texto-2); }}
.info {{ padding: 16px 16px 18px; display: grid; gap: 10px; min-width: 0; }}
.info h3 {{ margin: 0; font-family: var(--f-titulo); font-weight: 800; font-size: 20px; letter-spacing: .12em; text-transform: uppercase; color: var(--ouro); }}
.frase {{ margin: 0; color: var(--texto-2); font-size: 14px; }}
.tamanhos {{ display: flex; align-items: flex-end; gap: 18px; flex-wrap: wrap; }}
.tam {{ margin: 0; display: grid; justify-items: center; gap: 4px; }}
.tam svg {{ display: block; }}
.tam figcaption {{ font-size: 11px; color: var(--texto-2); }}
.paineis {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.painel {{ border-radius: 10px; padding: 10px; display: grid; place-items: center; }}
.painel.escuro {{ background: var(--fundo); border: 1px solid var(--linha); }}
.painel.claro {{ background: var(--claro); }}
.painel svg {{ width: 100%; height: auto; display: block; }}
.rodape {{ padding-block: 24px 32px; color: var(--texto-2); font-size: 13px; }}
</style>
<header class="topo">
  <span class="sobre">Clube Analítico · identidade, 4ª rodada</span>
  <h1>Entre o X1 e o X3</h1>
  <p>Em cima, quatro versões entre o X1 e o X3. Depois, as quatro misturas do C3 com o B3, os quatro que você separou, três misturas entre eles e cinco formatos novos. Cada um tem um código no canto (C3, M1…) para facilitar a escolha.</p>
</header>
{"".join(secoes)}
<p class="rodape">Dá para pedir ajustes em qualquer um: trocar cores, tirar ou pôr louros, estrelas, a frase do anel.</p>
'''
(SAIDA / "identidade.html").write_text(html, encoding="utf-8")
print("ok", len(html))
