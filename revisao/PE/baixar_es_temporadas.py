"""Baixa (API, wikitexto) as páginas de temporada da Wikipédia es ligadas no palmarés de 'Primera División del Perú'.
Uso: python -I revisao/PE/baixar_es_temporadas.py [ano ...]"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar import wiki, CACHE
sys.stdout.reconfigure(encoding="utf-8")
t = json.loads((CACHE / "es_primera_division.json").read_text(encoding="utf-8"))["parse"]["wikitext"]
t = t[t.index("=== Títulos por año ==="):t.index("=== Títulos por equipo ===")]
paginas = {int(a): p for p, a in re.findall(r"!\|?\[\[([^|\]]+)\|(\d{4})\]\]", t)}
anos = [int(a) for a in sys.argv[1:]] or sorted(paginas)
for a in anos:
    w = wiki("es", paginas[a], f"es_temporada_{a}.json")
    print(a, paginas[a], "sem página" if w is None else len(w), flush=True)
