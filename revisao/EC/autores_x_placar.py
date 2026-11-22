"""Páginas da RSSSF do ecu-1: linha do jogo + lista de autores ("[A 10, 20; B 30]"). Conta os minutos de cada lado e compara
com o placar da linha. Diferença = erro de digitação no placar (ou na lista). Saída: casos e o jogo do pacote (por fonte_id)."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import re, csv, glob
sys.path.insert(0, "coleta/ecu-1"); sys.path.insert(0, "coleta/comum-sulamerica")
from ler_rsssf import linhas
pac = {}
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/partidas.csv", encoding="utf-8")):
    for f in r["fonte_id"].split():
        if f.startswith("rsssf:"): pac[f] = r
JOGO = re.compile(r"^(\S.*?)\s+(\d{1,2})-(\d{1,2})\s+(\S.*?)\s*(\(.*\)|\[.*)?$")
def conta(lado):
    lado = re.sub(r"\(.*?\)", "", lado)
    if re.search(r"\bown goal\b|\bog\b", lado, re.I) and not re.search(r"\d", lado): return None
    return len(re.findall(r"\b\d{1,3}(?:\+\d*)?'?(?:\s*(?:pen|p|og|o\.g\.))?(?=[,\s;\])]|$)", lado))
casos = 0
for f in sorted(glob.glob("data/coleta/ecu-1/rsssf/ecua*.html")):
    pg = f.split("\\")[-1].split("/")[-1][:-5]
    if pg in ("ecuachamp", "ecuahist", "ecuatops"): continue
    ls = linhas(pg)
    for i, l in enumerate(ls):
        m = JOGO.match(l)
        if not m or not ls[i + 1:i + 2] or not ls[i + 1].strip().startswith("["): continue
        txt = ls[i + 1].strip()
        k = i + 1
        while "]" not in txt and k + 1 < len(ls): k += 1; txt += " " + ls[k].strip()
        txt = txt.strip("[] ")
        if re.match(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)", txt) or not re.search(r"[A-Za-z]{3}", txt): continue
        if not pac.get(f"rsssf:{pg}:{i}"): continue
        if re.search(r"awarded|abandon|n/p|annul", txt, re.I) or "-" in txt and re.search(r"\d-\d", txt): continue
        partes = txt.split(";")
        gm, gv = int(m.group(2)), int(m.group(3))
        if len(partes) == 2: cm, cv = conta(partes[0]), conta(partes[1])
        elif len(partes) == 1: cm, cv = (conta(partes[0]), 0) if gv == 0 else (0, conta(partes[0])) if gm == 0 else (None, None)
        else: continue
        if cm is None or cv is None: continue
        if (cm, cv) != (gm, gv) and cm + cv > 0:
            p = pac.get(f"rsssf:{pg}:{i}")
            casos += 1
            print(pg, i, "|", l.strip(), "| autores:", cm, "x", cv, "|", txt[:120], "| pacote:", (p["temporada"], p["data"], p["gols_mandante"], p["gols_visitante"]) if p else "-")
print("casos:", casos)
