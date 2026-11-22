"""FR: tabela final de uma temporada no footballdatabase.eu (limite de ~50 páginas por dia por visitante; usar pouco).
Uso: python -I revisao/FR/fdb.py 1937 1946 1958"""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import baixar
TEMPS = dict(l.split()[::-1] for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fdb_temporadas.txt"), encoding="utf-8") if l.strip().count(" ") == 1)
for a in sys.argv[1:]:
    a = int(a)
    caminho = TEMPS.get(f"{a}/{a + 1}")
    d = baixar.pegar("https://www.footballdatabase.eu" + caminho, f"fdb_{a}.html")
    t = d.decode("utf-8", "replace")
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", "|", s)); s = re.sub(r"\|[\s|]*", "|", s)
    i = s.find("General ranking")
    print(a, "https://www.footballdatabase.eu" + caminho)
    print(s[i:i + 1400])
    j = s.find("Relegated")
    print(s[s.find("Promoted"):j + 120] if j > 0 else "")
