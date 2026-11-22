"""Folha de contato dos escudos dos 69 clubes da ita-1 (painel/escudos/<slug>.webp). Uso: python -I revisao/IT/folha_escudos.py SAIDA.png"""
import csv, os, re, sys, unicodedata
from PIL import Image, ImageDraw
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
def slug(n):
    s = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
nomes = [x["clube"] for x in csv.DictReader(open(os.path.join(R, "data/coleta/ita-1/pacote/clubes.csv"), encoding="utf-8"))]
nomes.sort()
W, H, C = 150, 150, 10
img = Image.new("RGB", (C * W, ((len(nomes) + C - 1) // C) * H), "white")
d = ImageDraw.Draw(img)
falta = []
for i, n in enumerate(nomes):
    x, y = (i % C) * W, (i // C) * H
    p = os.path.join(R, "painel/escudos", slug(n) + ".webp")
    if os.path.exists(p):
        e = Image.open(p).convert("RGBA"); e.thumbnail((110, 110)); img.paste(e, (x + 20, y + 5), e)
    else:
        falta.append(n)
    d.text((x + 5, y + 125), n[:22], fill="black")
img.save(sys.argv[1]); print("sem arquivo:", falta)
