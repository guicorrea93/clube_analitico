"""Campeão de cada temporada: banco x RSSSF (England - List of Champions, tablese/engchamp.html)."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from comum import banco, temporadas, baixar
txt = baixar("https://www.rsssf.org/tablese/engchamp.html").decode("latin-1")
camp = {}
for bl in re.split(r'<a name="', txt, flags=re.I):
    if not re.match(r'c\d{4}"', bl): continue
    for ln in re.sub(r"<[^>]+>", "", re.search(r"<pre>(.*?)</pre>", bl, re.S | re.I).group(1)).splitlines():
        m = re.match(r"(\d{4})\s+[*\-]*\s*(.+?)\s*$", ln)
        if m: camp[int(m.group(1))] = m.group(2)
ALIAS = {"The Wednesday": "Sheffield Wednesday", "Preston NE": "Preston", "Tottenham Hostpur": "Tottenham", "Tottenham Hotspur": "Tottenham",
         "Wolverhampton Wanderers": "Wolverhampton", "Newcastle United": "Newcastle", "Blackburn Rovers": "Blackburn", "Huddersfield Town": "Huddersfield",
         "West Bromwich Albion": "West Bromwich", "Ipswich Town": "Ipswich", "Leeds United": "Leeds", "Leicester City": "Leicester"}
c = banco(); nm = dict(c.execute("select clube_id, nome from clube"))
ok = 0
for eid, t, ai, af in temporadas(c):
    cb = nm[c.execute("select campeao_id from edicao where edicao_id=?", (eid,)).fetchone()[0]]
    r = camp.get(ai + 1, "?"); r2 = ALIAS.get(r, r)
    if r2 == cb: ok += 1
    else: print(t, "banco", cb, "| RSSSF", r)
print("iguais", ok, "de", len(temporadas(c)), "| RSSSF lista", len(camp))
