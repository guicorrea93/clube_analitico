"""Baixa as páginas da Wikipédia de de cada temporada da Bundesliga (wikitexto), com cache em data/cache/revisao/DE/."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from rev_baixar import wikitext
def titulo(a):
    return f"Fußball-Bundesliga {a}/{str(a+1)[-2:]}"
if __name__ == "__main__":
    for a in range(1963, 2026):
        t = wikitext("de", titulo(a))
        print(a, len(t), flush=True)
    for p in ["Liste der deutschen Fußballmeister", "Liste der Torschützenkönige der Fußball-Bundesliga",
              "Relegation (Bundesliga)", "Bundesliga-Skandal (1971)", "Deutsche Fußballmeisterschaft",
              "Liste der Bundesligavereine", "Ewige Tabelle der Fußball-Bundesliga", "Liste der Abstiege aus der Fußball-Bundesliga"]:
        print(p, len(wikitext("de", p)), flush=True)
