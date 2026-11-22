"""Bloco E: folha de contato com os escudos dos clubes do par-1 (como o painel mostra). Uso: python -I revisao/PY/folha_escudos.py <saida.png>"""
import json, sqlite3, sys
from PIL import Image, ImageDraw, ImageFont
s = open("painel/index.html", encoding="utf-8").read()
i = s.find("const ESCUDOS = ") + len("const ESCUDOS = ")
E = json.loads(s[i:s.find("};", i) + 1])
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
cl = [r[0] for r in c.execute("""select cl.nome from clube cl where clube_id in (select clube_id from classificacao_final cf
        join edicao e using(edicao_id) join competicao co using(competicao_id) where slug='par-1') order by nome""") if r[0] in E]
W, H, COL = 200, 170, 6
img = Image.new("RGB", (W * COL, H * ((len(cl) + COL - 1) // COL)), "white")
d = ImageDraw.Draw(img)
try:
    f = ImageFont.truetype("arial.ttf", 15)
except OSError:
    f = ImageFont.load_default()
for k, n in enumerate(cl):
    x, y = (k % COL) * W, (k // COL) * H
    try:
        e = Image.open("painel/" + E[n]).convert("RGBA")
        e.thumbnail((120, 120))
        img.paste(e, (x + (W - e.width) // 2, y + 8), e)
    except Exception as ex:
        d.text((x + 10, y + 50), "ERRO " + str(ex)[:20], fill="red", font=f)
    d.text((x + 6, y + 140), n[:24], fill="black", font=f)
img.save(sys.argv[1])
print(len(cl), "escudos")
