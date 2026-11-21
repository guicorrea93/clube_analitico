"""Prints do site com o Chrome sem janela. Uso: python revisao/RV/prints.py lista.txt  (linhas: nome|slug|rota|largura|altura)"""
import subprocess, sys, os
S = r"C:/Users/GUILHE~1/AppData/Local/Temp/claude/c--Users-guilhermecorrea-Downloads-Gui-GitHub/a75361b9-f474-4b01-be59-ef64c90aa262/scratchpad/RV"
CH = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
for l in open(sys.argv[1], encoding="utf-8"):
    if not l.strip() or l.startswith("#"): continue
    nome, slug, rota, w, h = [x.strip() for x in l.split("|")]
    out = f"{S}/telas/{nome}.png"
    if os.path.exists(out): continue
    url = f"https://clubeanalitico.pages.dev/?c={slug}#{rota}"
    subprocess.run([CH, "--headless=new", "--disable-gpu", f"--user-data-dir={S}/chrome-perfil", f"--window-size={w},{h}",
                    "--virtual-time-budget=10000", "--hide-scrollbars", f"--screenshot={out}", url], capture_output=True, timeout=120)
    print(nome, os.path.exists(out))
