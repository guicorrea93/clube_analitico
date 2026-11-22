"""1947-1966: os jogos do pacote (vindos da Wikipédia pt) x a lista "Matches of the winner" das páginas da RSSSF (outra fonte).
Casa pela data (dd/mm) e confere o placar."""
import csv, re, html, sys
sys.stdout.reconfigure(encoding="utf-8")
pac = [r for r in csv.DictReader(open("data/coleta/bra-sp-2/pacote/partidas.csv", encoding="utf-8")) if r["temporada"] <= "1966"]
ok = dif = sem = 0
for p in pac:
    a = p["temporada"]
    try:
        t = open(f"data/coleta/bra-sp-2/rsssfbrasil/sp{a}l2.htm", "rb").read().decode("latin-1")
    except FileNotFoundError:
        sem += 1; continue
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    d = p["data"]; dd, mm = d[8:10], d[5:7]
    achou = None
    for m in re.finditer(rf"^\s*{dd}/{mm}(?:/\d+)?\s*:\s*(.+?)\s+(\d+)\s*[-x]\s*(\d+)\s+(.+?)\s*$", t, re.M):
        achou = m.groups(); break
    if not achou:
        sem += 1; print("sem na RSSSF", a, d, p["mandante"], p["gols_mandante"], "x", p["gols_visitante"], p["visitante"]); continue
    m1, g1, g2, v1 = achou
    pl = {(int(g1), int(g2)), (int(g2), int(g1))}
    if (int(p["gols_mandante"]), int(p["gols_visitante"])) in pl: ok += 1
    else:
        dif += 1; print("DIF", a, d, p["mandante"], p["gols_mandante"], "x", p["gols_visitante"], p["visitante"], "| RSSSF:", m1, g1, "-", g2, v1)
print(f"bateu {ok}, difere {dif}, sem par na RSSSF {sem}")
