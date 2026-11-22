"""FR: baixa as páginas por temporada da Wikipédia fr (wikitexto pela API), com cache. Rodar em segundo plano."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import baixar
anos = [a for a in range(1932, 2026) if not 1939 <= a <= 1944]
extra = ["Championnat de France de football", "Palmarès du championnat de France de football", "Liste des meilleurs buteurs du championnat de France de football", "Barrages de promotion et de relégation du championnat de France de football"]
for t in [f"Championnat de France de football {a}-{a+1}" for a in anos] + extra:
    w = baixar.wiki("fr", t)
    print(t, len(w) if w else None, flush=True)
