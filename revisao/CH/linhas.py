"""Mostra linhas do texto puro de uma página da RSSSF do chi-1 (como o leitor da coleta numera).
Uso: python -I revisao/CH/linhas.py <pagina> <ini> <fim>"""
import sys
from pathlib import Path
RAIZ = Path.cwd()
sys.path.insert(0, str(RAIZ / "coleta" / "comum-sulamerica"))
import rsssf_sul
pg, ini, fim = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
txt = rsssf_sul.texto(RAIZ / "data" / "coleta" / "chi-1" / "rsssf" / f"{pg}.html")
ls = txt.splitlines() if isinstance(txt, str) else txt
for i in range(ini, min(fim, len(ls))):
    print(i, ls[i])
