"""Revisão CL: folhas de contato dos escudos (o arquivo que o painel mostra de fato: ESCUDOS do painel/index.html).

Para cada competição, todos os clubes dela no painel (PART de painel/dados/<slug>.js), 60 por página
(escudo + nome + UF + cidade). Grava SCRATCH/CL/folhas/<slug>_<n>.html e tira o print com o Chrome sem janela.
Uso: python revisao/CL/folhas.py <SCRATCH>
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(sys.argv[1]) / "CL"
PASTA = OUT / "folhas"
PASTA.mkdir(parents=True, exist_ok=True)
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
SLUGS = ["bra-serie-a", "bra-serie-b", "bra-serie-c", "bra-serie-d", "bra-copa-do-brasil"]
L = {c["exib"]: c for c in json.loads((OUT / "mestre.json").read_text(encoding="utf-8"))}
html = (ROOT / "painel" / "index.html").read_text(encoding="utf-8")
ESC = json.loads(re.search(r"ESCUDOS = (\{.*?\});", html).group(1))
POR = 60
CSS = """body{margin:0;background:#f3f3f3;font-family:Segoe UI,Arial,sans-serif}
h1{font-size:14px;margin:4px 8px}
.g{display:grid;grid-template-columns:repeat(10,1fr);gap:4px;padding:4px 8px}
.c{background:#fff;border:1px solid #ccc;height:128px;text-align:center;overflow:hidden}
.c img{width:76px;height:76px;object-fit:contain;margin-top:4px;background:#eef4ee;border-radius:50%;padding:3px}
.sem{display:inline-block;width:76px;height:76px;margin-top:4px;border-radius:50%;background:#e33;color:#fff;line-height:76px;font-size:11px}
.n{font-size:12px;font-weight:700;line-height:13px;white-space:nowrap}
.u{font-size:10px;color:#444;line-height:11px;white-space:nowrap}"""
indice = []
for s in SLUGS:
    t = (ROOT / "painel" / "dados" / f"{s}.js").read_text(encoding="utf-8")
    nomes = sorted(json.loads(t[t.index("{"):].rstrip().rstrip(";"))["PART"].keys(), key=str.casefold)
    for p in range(0, len(nomes), POR):
        parte = nomes[p:p + POR]
        cel = []
        for i, n in enumerate(parte, start=p + 1):
            c = L[n]
            e = ESC.get(n)
            img = f'<img src="{(ROOT / "painel" / e).as_uri()}">' if e else '<span class="sem">SEM</span>'
            cel.append(f'<div class="c">{img}<div class="n">{i}. {n}</div><div class="u">{c["regiao"]} · {c["cidade"] or "-"}</div></div>')
        nome = f"{s}_{p // POR + 1:02d}"
        f = PASTA / f"{nome}.html"
        f.write_text(f"<!doctype html><meta charset='utf-8'><style>{CSS}</style><h1>{s} {p + 1}-{p + len(parte)} de {len(nomes)}</h1>"
                     f"<div class='g'>{''.join(cel)}</div>", encoding="utf-8")
        png = PASTA / f"{nome}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", f"--user-data-dir={OUT / 'chrome-perfil'}",
                        "--window-size=1400,900", "--hide-scrollbars", "--virtual-time-budget=4000",
                        f"--screenshot={png}", f.as_uri()], capture_output=True, timeout=120)
        indice.append(f"{png}\t{len(parte)}")
(PASTA / "indice.txt").write_text("\n".join(indice), encoding="utf-8")
print("\n".join(indice))
