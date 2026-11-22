"""Arquivos finais da marca (escudo Y2): SVG com as letras viradas em desenho e o ícone simplificado.
Grava em <saida>/: escudo.svg, icone.svg e as folhas de teste."""
import re
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

AQUI = Path(__file__).resolve().parent
FONTES = AQUI.parent / "fonte_barlow"
SAIDA = Path(sys.argv[1])
SAIDA.mkdir(parents=True, exist_ok=True)

g = {"__file__": str(AQUI / "escudos4.py"), "__name__": "x"}
exec((AQUI / "escudos4.py").read_text(encoding="utf-8").split('\nVB = "0 0 100 120"')[0], g)

fontes = {800: TTFont(FONTES / "BarlowCondensed-ExtraBold.ttf"), 700: TTFont(FONTES / "BarlowCondensed-Bold.ttf")}


def texto_em_desenho(svg):
    """Troca cada <text> (formato de texto() em escudos3.py) por um <path> com o contorno das letras."""
    def troca(m):
        at, conteudo = m.group(1), m.group(2)
        pega = lambda n, d=None: (re.search(rf'{n}="([^"]*)"', at) or [None, d])[1]
        x, y, tam, esp = float(pega("x")), float(pega("y")), float(pega("font-size")), float(pega("letter-spacing", 0))
        f = fontes[int(pega("font-weight", 800))]
        cmap, gs, upm = f.getBestCmap(), f.getGlyphSet(), f["head"].unitsPerEm
        k = tam / upm
        nomes = [cmap[ord(c)] for c in conteudo]
        larg = sum(gs[n].width * k + esp for n in nomes)
        cx = x - (larg - esp) / 2 if pega("text-anchor") == "middle" else x
        d = ""
        for n in nomes:
            pen = SVGPathPen(gs)
            gs[n].draw(TransformPen(pen, (k, 0, 0, -k, cx, y)))
            d += pen.getCommands()
            cx += gs[n].width * k + esp
        return f'<path d="{d}" fill="{pega("fill")}"/>'
    return re.sub(r"<text ([^>]*)>([^<]*)</text>", troca, svg)


def icone(u, modo):
    """Versão para tamanhos pequenos (aba do navegador): só o escudo, a faixa do alto e a bola."""
    p = g["pal"](modo); f = g["fundo_de"](p)
    s = g["defs"](u, p) + f'<path d="{g["EXT"]}" fill="url(#o{u})"/><path d="{g["INT"]}" fill="{f}"/>'
    s += (f'<g clip-path="url(#c{u})"><rect x="0" y="0" width="100" height="31" fill="{p["v"]}"/>'
          f'<rect x="0" y="31" width="100" height="2.4" fill="url(#o{u})"/></g>')
    return s + g["_bola"](p, u, f, 50, 64, 24)


def arquivo(corpo, vb):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{texto_em_desenho(corpo)}</svg>\n'


escudo = arquivo(g["y2"]("m", "cor"), "-12 -14 124 134")
ico = arquivo(icone("i", "cor"), "-4 -2 108 124")
(SAIDA / "escudo.svg").write_text(escudo, encoding="utf-8")
(SAIDA / "icone.svg").write_text(ico, encoding="utf-8")

# folha de teste: escudo com e sem fonte, ícone em tamanhos de aba
lin = lambda sv, ts: "".join(f'<span style="display:inline-block;margin:6px">{sv.replace("<svg ", f"<svg width={t} height={t} ", 1)}</span>' for t in ts)
(SAIDA / "_teste.html").write_text(
    '<html><body style="margin:0;background:#06140c;padding:10px;color:#fff;font:13px Arial">'
    f'<div>{lin(escudo, (260, 96, 48))}</div>'
    f'<div>{lin(ico, (128, 64, 32, 16))}</div>'
    f'<div style="background:#f4f7f4;display:inline-block">{lin(ico, (32, 16))}{lin(escudo, (48,))}</div></body></html>',
    encoding="utf-8")
print("ok", len(escudo), len(ico))
