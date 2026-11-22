"""Terceira rodada de logos: cada escudo em três níveis (simples, clássico, completo) e duas ideias novas.
Gera logo/identidade.html e um SVG por escudo em logo/r3/."""
import math
from pathlib import Path

SAIDA = Path(__file__).resolve().parent.parent / "logo"
(SAIDA / "r3").mkdir(parents=True, exist_ok=True)

VERDE, OURO, CLARO, FUNDO = "#1ecb74", "#fbbf24", "#eafff2", "#06140c"
EXT = "M50 4 C62 9 78 10 92 8 L92 60 C92 88 74 106 50 116 C26 106 8 88 8 60 L8 8 C22 10 38 9 50 4 Z"
INT = "M50 12 C61 16 74 17 85 15.5 L85 60 C85 84 69 99 50 108 C31 99 15 84 15 60 L15 15.5 C26 17 39 16 50 12 Z"
FINO = "M50 15.5 C60 19 72 20 81.5 19 L81.5 60 C81.5 82 67 96 50 104 C33 96 18.5 82 18.5 60 L18.5 19 C28 20 40 19 50 15.5 Z"
FONTE = "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"


def estrela(cx, cy, r, ri=None):
    ri = ri or r * 0.42
    return " ".join(f"{cx + (r if k % 2 == 0 else ri) * math.cos(math.radians(-90 + 36 * k)):.2f},"
                    f"{cy + (r if k % 2 == 0 else ri) * math.sin(math.radians(-90 + 36 * k)):.2f}" for k in range(10))


def pal(modo):
    if modo == "cor":
        return dict(v=VERDE, o=OURO, o2="#d9950a", f1="#11402a", f2=FUNDO, t=CLARO, txt=FUNDO, mono=False)
    if modo == "claro":
        return dict(v="#149e57", o="#e0a008", o2="#b97f00", f1="#11402a", f2=FUNDO, t=CLARO, txt=FUNDO, mono=False)
    c = CLARO if modo == "mono-e" else FUNDO
    bg = FUNDO if modo == "mono-e" else "#f4f7f4"
    return dict(v=c, o=c, o2=c, f1=bg, f2=bg, t=bg, txt=bg, mono=True)


def defs(u, p):
    return (f'<defs><linearGradient id="f{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["f1"]}"/>'
            f'<stop offset="1" stop-color="{p["f2"]}"/></linearGradient>'
            f'<linearGradient id="o{u}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p["o"]}"/>'
            f'<stop offset="1" stop-color="{p["o2"]}"/></linearGradient>'
            f'<clipPath id="c{u}"><path d="{INT}"/></clipPath></defs>')


def texto(x, y, t, tam, cor, esp=1.5, peso=800, ancora="middle"):
    return (f'<text x="{x}" y="{y}" text-anchor="{ancora}" font-family="{FONTE}" font-weight="{peso}" font-size="{tam}" '
            f'letter-spacing="{esp}" fill="{cor}">{t}</text>')


def bola(cx, cy, r, fundo, ouro, verde, centro):
    """A bola-gráfico: cinco gomos com um em destaque e o pentágono no meio."""
    k = r / 27
    s = f'<g transform="translate({cx - 32 * k:.2f} {cy - 32 * k:.2f}) scale({k:.4f})">'
    for i in range(5):
        a0, a1 = math.radians(-90 + 72 * i), math.radians(-90 + 72 * (i + 1))
        s += (f'<path d="M32 32L{32 + 27 * math.cos(a0):.2f} {32 + 27 * math.sin(a0):.2f}A27 27 0 0 1 '
              f'{32 + 27 * math.cos(a1):.2f} {32 + 27 * math.sin(a1):.2f}Z" fill="{ouro if i == 0 else verde}"/>')
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        s += f'<line x1="32" y1="32" x2="{32 + 31 * math.cos(a):.2f}" y2="{32 + 31 * math.sin(a):.2f}" stroke="{fundo}" stroke-width="3.6"/>'
    pent = lambda rr: " ".join(f"{32 + rr * math.cos(math.radians(-90 + 72 * i)):.2f},{32 + rr * math.sin(math.radians(-90 + 72 * i)):.2f}" for i in range(5))
    s += f'<polygon points="{pent(13.5)}" fill="{fundo}"/><polygon points="{pent(8)}" fill="{centro}" stroke="{centro}" stroke-width="1.5" stroke-linejoin="round"/>'
    return s + "</g>"


def faixa(y, cor, sombra, txt, cortxt, tam=9, esp=2):
    """Fita que atravessa o escudo, com as pontas em rabo de andorinha."""
    return (f'<path d="M-2 {y} H102 L96 {y + 7} L102 {y + 14} H-2 L4 {y + 7} Z" fill="{cor}"/>'
            f'<path d="M4 {y + 14} L10 {y + 18} L10 {y + 14} Z M96 {y + 14} L90 {y + 18} L90 {y + 14} Z" fill="{sombra}" fill-opacity=".55"/>'
            + texto(50, y + 10.4, txt, tam, cortxt, esp))


def louros(p):
    """Dois ramos de louro abraçando o escudo por baixo."""
    s = ""
    for i in range(11):
        g = 108 + i * 9                      # ângulo no arco (90 = embaixo, 180 = à esquerda)
        th = math.radians(g)
        for desvio, giro in ((2.6, 28), (-2.6, -28)):   # folha de fora e folha de dentro
            r = 56 + desvio
            x, y = 50 + r * math.cos(th), 58 + r * math.sin(th)
            rot = g + 90 + giro
            for xx, rr in ((x, rot), (100 - x, 180 - rot)):   # ramo esquerdo e o espelho à direita
                s += (f'<ellipse cx="{xx:.2f}" cy="{y:.2f}" rx="4.4" ry="1.8" transform="rotate({rr:.1f} {xx:.2f} {y:.2f})" '
                      f'fill="{p["v"]}" fill-opacity="{.95 - i * .035:.2f}"/>')
    return s


def coroa(p, u):
    """Três estrelas sobre a ponta do escudo."""
    return (f'<polygon points="{estrela(50, -5, 6.5)}" fill="url(#o{u})"/>'
            f'<polygon points="{estrela(35, -1, 3.8)}" fill="url(#o{u})"/><polygon points="{estrela(65, -1, 3.8)}" fill="url(#o{u})"/>')


# ---------- família 1: escudo campeão ----------
def barras4(p, u, base, larg=9):
    s = ""
    for i, (x, h) in enumerate(zip((27.5, 39.5, 51.5, 63.5), (18, 28, 40, 52))):
        s += f'<rect x="{x}" y="{base - h}" width="{larg}" height="{h}" rx="1.6" fill="{f"url(#o{u})" if i == 3 else p["v"]}"/>'
    return s


def campeao_simples(u, modo):
    p = pal(modo)
    return (defs(u, p) + f'<path d="{EXT}" fill="{p["o"]}"/><path d="{INT}" fill="{p["f2"]}"/>'
            + barras4(dict(p, v=p["v"]), u, 92).replace(f"url(#o{u})", p["o"]))


def campeao_classico(u, modo):
    p = pal(modo)
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="url(#f{u})"/>'
    s += f'<g clip-path="url(#c{u})" fill="{p["v"]}" fill-opacity=".09">' + "".join(f'<rect x="{x}" y="0" width="10" height="120"/>' for x in (20, 40, 60, 80)) + "</g>"
    s += f'<path d="M50 17 C60 20.5 72 21.5 81 20.5 M50 17 C40 20.5 28 21.5 19 20.5" fill="none" stroke="{p["v"]}" stroke-opacity=".45" stroke-width="1"/>'
    s += barras4(p, u, 86)
    s += f'<polygon points="{estrela(68, 25, 6.5)}" fill="url(#o{u})"/>'
    s += f'<polygon points="{estrela(32, 30, 2.6)}" fill="{p["v"]}" fill-opacity=".55"/><polygon points="{estrela(42, 24, 2.2)}" fill="{p["v"]}" fill-opacity=".4"/>'
    return s + faixa(88, p["v"], p["f2"], "CLUBE ANALÍTICO", p["txt"], 8.2, 1.1)


def campeao_completo(u, modo):
    p = pal(modo)
    s = defs(u, p) + louros(p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="url(#f{u})"/>'
    s += f'<g clip-path="url(#c{u})"><g fill="{p["v"]}" fill-opacity=".09">' + "".join(f'<rect x="{x}" y="0" width="10" height="120"/>' for x in (20, 40, 60, 80)) + "</g>"
    s += f'<rect x="0" y="0" width="100" height="31" fill="{p["v"]}"/><rect x="0" y="31" width="100" height="1.6" fill="url(#o{u})"/></g>'
    s += texto(50, 28, "CLUBE", 12, p["txt"], 5)
    s += f'<path d="{FINO}" fill="none" stroke="url(#o{u})" stroke-opacity=".55" stroke-width=".8"/>'
    s += barras4(p, u, 86, 8.5)
    s += coroa(p, u)
    return s + faixa(88, p["v"], p["f2"], "ANALÍTICO", p["txt"], 10, 2.6)


# ---------- família 2: bola no peito ----------
def bola_simples(u, modo):
    p = pal(modo)
    fundo = p["f2"] if p["mono"] else "#0b2416"
    return (defs(u, p) + f'<path d="{EXT}" fill="{p["v"]}"/><path d="{INT}" fill="{fundo}"/>'
            + bola(50, 54, 27, fundo, p["o"], p["v"], p["v"] if p["mono"] else p["t"]))


def bola_classico(u, modo):
    p = pal(modo)
    fundo = p["f2"] if p["mono"] else "#0b2416"
    s = defs(u, p) + f'<path d="{EXT}" fill="{p["v"]}"/><path d="{INT}" fill="{fundo}"/>'
    s += f'<path d="M50 17 C60 20.5 72 21.5 81 20.5 M50 17 C40 20.5 28 21.5 19 20.5" fill="none" stroke="{p["v"]}" stroke-opacity=".4" stroke-width="1"/>'
    s += bola(50, 38, 18.5, fundo, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    s += f'<g clip-path="url(#c{u})"><rect x="0" y="62" width="100" height="8" fill="url(#o{u})"/></g>'
    for i, (x, h) in enumerate(zip((36, 46, 56), (9, 15, 21))):
        s += f'<rect x="{x}" y="{93 - h}" width="8" height="{h}" rx="1.4" fill="{f"url(#o{u})" if i == 2 else p["v"]}"/>'
    return s


def bola_completo(u, modo):
    p = pal(modo)
    fundo = p["f2"] if p["mono"] else "#0b2416"
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="{fundo}"/>'
    s += f'<path d="{FINO}" fill="none" stroke="{p["v"]}" stroke-width="1.4"/>'
    s += f'<g clip-path="url(#c{u})" fill="{p["v"]}" fill-opacity=".07">' + "".join(
        f'<path d="M{x} 0 L{x + 6} 0 L{x - 40} 120 L{x - 46} 120 Z"/>' for x in range(30, 160, 16)) + "</g>"
    s += bola(50, 39, 17, fundo, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])
    s += f'<g clip-path="url(#c{u})"><rect x="0" y="61" width="100" height="12" fill="url(#o{u})"/></g>'
    s += texto(50, 70.2, "CLUBE ANALÍTICO", 8.4, p["txt"], 1.1)
    for i, (x, h) in enumerate(zip((36, 46, 56), (8, 13, 18))):
        s += f'<rect x="{x}" y="{95 - h}" width="8" height="{h}" rx="1.4" fill="{f"url(#o{u})" if i == 2 else p["v"]}"/>'
    return s + coroa(p, u)


# ---------- família 3: camisa listrada ----------
def listras(p, u, tops, brilho=True):
    s = f'<g clip-path="url(#c{u})">'
    for i, (x, t) in enumerate(zip(range(15, 85, 10), tops)):
        cor, op = (f"url(#o{u})", 1) if i == 6 else (p["v"], 1 if i % 2 else .62)
        s += f'<rect x="{x}" y="{t}" width="10" height="{120 - t}" fill="{cor}" fill-opacity="{op}"/>'
        if brilho and not p["mono"]:
            s += f'<rect x="{x}" y="{t}" width="10" height="2.2" fill="{p["t"]}" fill-opacity=".25"/>'
    return s + "</g>"


def listras_simples(u, modo):
    p = pal(modo)
    return (defs(u, p) + f'<path d="{EXT}" fill="{p["v"]}"/><path d="{INT}" fill="{p["f2"]}"/>'
            + listras(p, u, (82, 74, 65, 56, 46, 35, 22), False).replace(f"url(#o{u})", p["o"])
            + f'<path d="{INT}" fill="none" stroke="{p["f2"]}" stroke-width="1.6"/>')


def listras_classico(u, modo):
    p = pal(modo)
    s = defs(u, p) + f'<path d="{EXT}" fill="{p["v"]}"/><path d="{INT}" fill="url(#f{u})"/>'
    s += listras(p, u, (82, 74, 65, 56, 46, 35, 22))
    s += f'<path d="{INT}" fill="none" stroke="{p["f2"]}" stroke-width="1.6"/>'
    s += f'<polygon points="{estrela(33, 38, 9)}" fill="url(#o{u})"/>'
    s += f'<path d="M22 22 H56" stroke="{p["v"]}" stroke-opacity=".5" stroke-width="1.2"/>'
    return s + texto(22, 31.5, "C · A", 8, p["v"], 1.6, ancora="start")


def listras_completo(u, modo):
    p = pal(modo)
    s = defs(u, p) + f'<path d="{EXT}" fill="url(#o{u})"/><path d="{INT}" fill="url(#f{u})"/>'
    s += listras(p, u, (86, 79, 71, 63, 55, 46, 36))
    s += f'<g clip-path="url(#c{u})"><rect x="0" y="0" width="100" height="31" fill="{p["f2"]}"/><rect x="0" y="31" width="100" height="1.6" fill="url(#o{u})"/></g>'
    s += texto(50, 28, "CLUBE ANALÍTICO", 7.2, p["o"] if not p["mono"] else p["v"], .5)
    s += f'<path d="{INT}" fill="none" stroke="{p["f2"]}" stroke-width="1.4"/>'
    s += f'<polygon points="{estrela(30, 47, 7.5)}" fill="url(#o{u})"/>'
    return s + coroa(p, u)


# ---------- ideias novas ----------
def redondo(u, modo):
    """Escudo redondo, à moda europeia: nome no anel, bola-gráfico no centro."""
    p = pal(modo)
    fundo = p["f2"] if p["mono"] else "#0b2416"
    s = defs(u, p)
    s += f'<defs><path id="a{u}" d="M13 60 A37 37 0 0 1 87 60"/><path id="b{u}" d="M7.5 60 A42.5 42.5 0 0 0 92.5 60"/></defs>'
    s += f'<circle cx="50" cy="60" r="49" fill="url(#o{u})"/><circle cx="50" cy="60" r="46" fill="{fundo}"/>'
    s += f'<circle cx="50" cy="60" r="32" fill="none" stroke="{p["v"]}" stroke-width="1.6"/>'
    s += f'<text font-family="{FONTE}" font-weight="800" font-size="10.5" letter-spacing="2.6" fill="{p["t"] if not p["mono"] else p["v"]}"><textPath href="#a{u}" startOffset="50%" text-anchor="middle">CLUBE ANALÍTICO</textPath></text>'
    s += f'<text font-family="{FONTE}" font-weight="700" font-size="7.6" letter-spacing="2" fill="{p["v"]}"><textPath href="#b{u}" startOffset="50%" text-anchor="middle">DADOS DO FUTEBOL</textPath></text>'
    s += f'<polygon points="{estrela(10, 60, 3.2)}" fill="url(#o{u})"/><polygon points="{estrela(90, 60, 3.2)}" fill="url(#o{u})"/>'
    return s + bola(50, 60, 23, fundo, f"url(#o{u})", p["v"], p["v"] if p["mono"] else p["t"])


def monograma(u, modo):
    """Monograma CA no escudo, com três barras de coroa."""
    p = pal(modo)
    s = defs(u, p) + f'<path d="{EXT}" fill="{p["v"]}"/><path d="{INT}" fill="url(#f{u})"/>'
    s += f'<path d="{FINO}" fill="none" stroke="url(#o{u})" stroke-width="1"/>'
    for i, (x, h) in enumerate(zip((40, 47, 54), (7, 11, 15))):
        s += f'<rect x="{x}" y="{36 - h}" width="5.5" height="{h}" rx="1" fill="{f"url(#o{u})" if i == 2 else p["v"]}"/>'
    s += texto(50, 82, "CA", 50, p["t"] if not p["mono"] else p["v"], 0)
    return s + f'<rect x="30" y="88" width="40" height="2.4" rx="1.2" fill="url(#o{u})"/>'


# (família, [(chave, nível, função, viewBox, frase, ícone?)])
VB = "0 0 100 120"
VB_FAIXA = "-4 0 108 120"
VB_COROA = "-4 -14 108 134"
VB_LOURO = "-12 -14 124 134"
FAMILIAS = [
    ("Escudo campeão", "Barras que sobem até a dourada, a do campeão.", [
        ("c1", "Simples", campeao_simples, VB, "Só o aro e as quatro barras, em cores chapadas. Serve também de ícone da aba."),
        ("c2", "Clássico", campeao_classico, VB_FAIXA, "O da rodada passada, agora com CLUBE ANALÍTICO inteiro na faixa."),
        ("c3", "Completo", campeao_completo, VB_LOURO, "CLUBE no alto do escudo, ANALÍTICO na faixa, três estrelas em cima e ramos de louro."),
    ]),
    ("Bola no peito", "A bola vira um gráfico de pizza, com um gomo dourado.", [
        ("b1", "Simples", bola_simples, VB, "Só o escudo e a bola grande no meio."),
        ("b2", "Clássico", bola_classico, VB, "O da rodada passada: bola, faixa dourada e barras de pódio."),
        ("b3", "Completo", bola_completo, VB_COROA, "Aro dourado com filete verde, faixa com o nome, listras diagonais e três estrelas."),
    ]),
    ("Camisa listrada", "As listras do uniforme são as barras do gráfico.", [
        ("l1", "Simples", listras_simples, VB, "Só as listras subindo até a dourada."),
        ("l2", "Clássico", listras_classico, VB, "O da rodada passada, com a estrela e as iniciais."),
        ("l3", "Completo", listras_completo, VB_COROA, "Aro dourado, faixa do alto com o nome, estrela e três estrelas em cima."),
    ]),
    ("Ideias novas", "Dois caminhos diferentes dos três acima.", [
        ("n1", "Redondo", redondo, "0 10 100 100", "Escudo redondo, como o de muitos clubes europeus: o nome no anel e a bola-gráfico no centro."),
        ("n2", "Monograma", monograma, VB, "As iniciais CA no escudo, com três barras de coroa por cima."),
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
      <div class="palco">{svg(fn, f"{chave}g", "cor", vb, None, ' class="grande"')}</div>
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
        (SAIDA / "r3" / f"{chave}.svg").write_text(
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
/* Vitrine por família: cada família numa faixa, os níveis lado a lado do mais simples ao mais completo. Tema único escuro, de propósito. */
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
.grade {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 16px; }}
.card {{ border: 1px solid var(--linha); border-radius: 16px; overflow: hidden; background: var(--fundo-2); display: grid; align-content: start; }}
.palco {{ display: grid; place-items: center; padding: 26px 16px 18px; background: radial-gradient(circle at 50% 45%, #123a25 0%, var(--fundo) 72%); }}
.palco .grande {{ width: 190px; max-width: 100%; height: auto; filter: drop-shadow(0 10px 20px rgba(0,0,0,.45)); }}
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
  <span class="sobre">Clube Analítico · identidade, 3ª rodada</span>
  <h1>Cada escudo do simples ao completo</h1>
  <p>Os três escudos da rodada passada, cada um em três níveis de detalhe, e duas ideias novas. Embaixo de cada um: tamanhos pequenos e a versão com o nome, em fundo escuro, claro e em uma cor só.</p>
</header>
{"".join(secoes)}
<p class="rodape">Dá para misturar: por exemplo, o aro e a faixa de um com o desenho de outro.</p>
'''
(SAIDA / "identidade.html").write_text(html, encoding="utf-8")
print("ok", len(html))
