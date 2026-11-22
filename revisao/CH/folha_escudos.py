"""Folha de contato dos escudos dos 53 clubes do chi-1 (como o painel mostra: ESCUDOS em painel/index.html).
Grava SCRATCH/CH/folha_escudos.png. Uso: python -I revisao/CH/folha_escudos.py <saida.png>"""
import csv, json, re, sys
from PIL import Image, ImageDraw, ImageFont
h = open("painel/index.html", encoding="utf-8").read()
ESC = json.loads(re.search(r"const ESCUDOS = (\{.*?\});", h).group(1))
clubes = [r["clube"] for r in csv.DictReader(open("data/coleta/chi-1/pacote/clubes.csv", encoding="utf-8"))]
W, H, C = 200, 150, 6
lin = (len(clubes) + C - 1) // C
img = Image.new("RGB", (W * C, H * lin), (30, 40, 35))
d = ImageDraw.Draw(img)
try:
    f = ImageFont.truetype("arial.ttf", 13)
except OSError:
    f = ImageFont.load_default()
sem = []
for i, c in enumerate(clubes):
    x, y = (i % C) * W, (i // C) * H
    p = ESC.get(c)
    if p:
        try:
            e = Image.open("painel/" + p).convert("RGBA"); e.thumbnail((100, 100))
            img.paste(e, (x + (W - e.width) // 2, y + 8), e)
        except Exception as ex:
            d.text((x + 10, y + 40), "ERRO " + str(ex)[:20], fill=(255, 80, 80), font=f)
    else:
        sem.append(c); d.text((x + 60, y + 45), "SEM ESCUDO", fill=(255, 80, 80), font=f)
    d.text((x + 6, y + 115), c[:28], fill=(240, 240, 240), font=f)
    d.text((x + 6, y + 131), (p or "")[8:36], fill=(150, 150, 150), font=f)
img.save(sys.argv[1])
print("sem escudo:", sem)
