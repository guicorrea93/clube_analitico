"""Lê os {{Football box collapsible}} de um artigo de temporada de clube na Wikipédia en (data, times, placar, gols)."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import baixar
def boxes(titulo, lang="en"):
    w = baixar.wikitext(lang, titulo)
    res = []
    for b in re.split(r"\{\{\s*[Ff]ootball box", w)[1:]:
        d = {}
        for k in ("round", "date", "team1", "score", "team2", "goals1", "goals2", "report", "attendance", "referee"):
            m = re.search(r"\|\s*" + k + r"\s*=\s*(.*)", b)
            d[k] = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", m.group(1)).strip() if m else ""
        res.append(d)
    return res
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for d in boxes(sys.argv[1]):
        if len(sys.argv) < 3 or re.search(sys.argv[2], d["team1"] + d["team2"]):
            print(d["round"], d["date"], d["team1"], d["score"], d["team2"], "|", d["goals1"][:80], "|", d["goals2"][:80], "|", d["report"][:80])
