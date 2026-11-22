"""FR: baixa o calendário completo de cada temporada no transfermarkt (uma página por temporada), com cache."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import baixar
for a in [a for a in range(1932, 2026) if not 1939 <= a <= 1944]:
    d = baixar.pegar(f"https://www.transfermarkt.com/ligue-1/gesamtspielplan/wettbewerb/FR1?saison_id={a}", f"tm_FR1_{a}.html")
    print(a, len(d) if d else None, flush=True)
