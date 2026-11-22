"""Folha de contato dos escudos dos clubes do ecu-1 (painel/escudos/<slug>.webp) -> PNG no scratchpad (arg 1)."""
import csv, os, re, sys, unicodedata, collections
from PIL import Image, ImageDraw, ImageFont
def slug(c):
    c = "".join(ch for ch in unicodedata.normalize("NFD", c) if unicodedata.category(ch) != "Mn").lower()
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", c))
part = collections.Counter(r["clube"] for r in csv.DictReader(open("data/coleta/ecu-1/pacote/classificacao_final.csv", encoding="utf-8")))
cl = [c for c, _ in part.most_common() if os.path.exists(f"painel/escudos/{slug(c)}.webp")]
W, H, COL = 200, 170, 6
img = Image.new("RGB", (W * COL, H * ((len(cl) + COL - 1) // COL)), "white")
d = ImageDraw.Draw(img)
try: f = ImageFont.truetype("arial.ttf", 13)
except Exception: f = ImageFont.load_default()
for k, c in enumerate(cl):
    x, y = (k % COL) * W, (k // COL) * H
    e = Image.open(f"painel/escudos/{slug(c)}.webp").convert("RGBA"); e.thumbnail((120, 120))
    img.paste(e, (x + (W - e.width) // 2, y + 8), e)
    d.text((x + 6, y + 140), c[:28], fill="black", font=f)
img.save(sys.argv[1]); print(len(cl), "escudos")
